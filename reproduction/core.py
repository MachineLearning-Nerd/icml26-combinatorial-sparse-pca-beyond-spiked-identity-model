from __future__ import annotations

import math

import numpy as np


def unit(vector: np.ndarray) -> np.ndarray:
    return vector / np.linalg.norm(vector)


def sin2_angle(left: np.ndarray, right: np.ndarray) -> float:
    return float(max(0.0, 1.0 - (left @ right) ** 2))


def sample_gaussian(
    covariance: np.ndarray, n: int, seed: int
) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)
    square_root = eigenvectors @ np.diag(np.sqrt(np.maximum(eigenvalues, 0.0)))
    rng = np.random.default_rng(seed)
    return rng.standard_normal((n, covariance.shape[0])) @ square_root.T


def sample_covariance(samples: np.ndarray) -> np.ndarray:
    return samples.T @ samples / samples.shape[0]


def diagonal_counterexample(d: int, s: int) -> tuple[np.ndarray, np.ndarray]:
    vector = np.zeros(d)
    vector[:s] = 1 / math.sqrt(s)
    covariance = np.outer(vector, vector)
    covariance[s : 2 * s, s : 2 * s] += 0.9 * np.eye(s)
    return covariance, vector


def covariance_threshold_counterexample(
    s: int, m: int, alpha: float
) -> tuple[np.ndarray, np.ndarray]:
    d = s + m
    vector = np.zeros(d)
    vector[:s] = 1 / math.sqrt(s)
    signal = 0.5 * np.eye(s) + 0.5 * np.outer(vector[:s], vector[:s])
    decoy = 0.3 * np.eye(m) + alpha * (np.ones((m, m)) - np.eye(m))
    covariance = np.zeros((d, d))
    covariance[:s, :s] = signal
    covariance[s:, s:] = decoy
    return covariance, vector


def equal_first_coordinate_basis(s: int) -> np.ndarray:
    vector = np.ones(s) / math.sqrt(s)
    _, _, vh = np.linalg.svd(vector.reshape(1, -1), full_matrices=True)
    basis = vh[1:].T
    current = basis[0]
    target = np.ones(s - 1) / math.sqrt(s)
    direction = current - target
    if np.linalg.norm(direction) > 1e-12:
        direction /= np.linalg.norm(direction)
        rotation = np.eye(s - 1) - 2 * np.outer(direction, direction)
        basis = basis @ rotation
    return basis


def greedy_counterexample(s: int) -> tuple[np.ndarray, np.ndarray]:
    d = 2 * s - 1
    vector = np.zeros(d)
    vector[:s] = 1 / math.sqrt(s)
    basis = equal_first_coordinate_basis(s)
    nuisance = np.zeros((d, s - 1))
    nuisance[:s] = basis / math.sqrt(2)
    nuisance[s:] = np.eye(s - 1) / math.sqrt(2)
    covariance = np.outer(vector, vector) + 0.9 * nuisance @ nuisance.T
    return covariance, vector


def top_r_columns(values: np.ndarray, r: int) -> np.ndarray:
    keep = np.argpartition(np.abs(values), -r, axis=0)[-r:]
    truncated = np.zeros_like(values)
    columns = np.arange(values.shape[1])[None, :]
    truncated[keep, columns] = values[keep, columns]
    norms = np.linalg.norm(truncated, axis=0)
    return truncated / np.maximum(norms, 1e-15)


def historical_rtpm(samples: np.ndarray, r: int, iterations: int) -> np.ndarray:
    covariance = sample_covariance(samples)
    candidates = np.eye(samples.shape[1])
    for _ in range(iterations):
        candidates = top_r_columns(covariance @ candidates, r)
    rayleigh = np.sum(candidates * (covariance @ candidates), axis=0)
    return candidates[:, int(np.argmax(rayleigh))]


def deflation_counterexample(
    d: int, delta: float, gamma: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    eye = np.eye(d)
    first = (eye[:, 0] + eye[:, 1]) / math.sqrt(2)
    second = (eye[:, 0] - eye[:, 1]) / math.sqrt(2)
    dense_tail = np.sum(eye[:, 3:], axis=1) / math.sqrt(d - 3)
    nuisance = (eye[:, 2] + dense_tail) / math.sqrt(2)
    approximate = math.sqrt(1 - delta) * first + math.sqrt(delta) * eye[:, 2]
    covariance = (
        np.outer(first, first) / delta
        + np.outer(second, second)
        + (1 - gamma) * np.outer(nuisance, nuisance)
    )
    projector = eye - np.outer(approximate, approximate)
    return covariance, first, projector


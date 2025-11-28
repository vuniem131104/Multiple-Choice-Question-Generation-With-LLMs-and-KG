from __future__ import annotations

import numpy as np


def calculate_cosine_similarity_matrix(embeddings: np.ndarray) -> np.ndarray:
    """Calculate the cosine similarity matrix for the given data.

        Args:
            embeddings (np.ndarray): The input embeddings for which to calculate similarities.

        Returns:
            np.ndarray: The cosine similarity matrix.
        """

    norms = np.linalg.norm(embeddings, axis=1)

    cosine_similarity_matrix = np.dot(embeddings, embeddings.T) / (norms[:, None] * norms[None, :])

    cosine_similarity_matrix = np.nan_to_num(cosine_similarity_matrix)

    cosine_similarity_matrix = cosine_similarity_matrix / cosine_similarity_matrix.max()

    return cosine_similarity_matrix

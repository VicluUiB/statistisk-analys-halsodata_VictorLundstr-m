import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class HealthAnalyzer:
    """Analysera hälsodata som lagras i en pandas DataFrame."""

    def __init__(self, data):
        """Spara en kopia av datasetet för analys."""
        self.data = data.copy()

    def descriptive_statistics(self, columns):
        """Returnera medelvärde, median, minimum och maximum."""
        return self.data[columns].agg(
            ["mean", "median", "min", "max"]
        )

    def plot_histogram(self, column, title, xlabel, bins=25):
        """Rita ett histogram för en numerisk kolumn."""
        plt.figure(figsize=(8, 5))

        sns.histplot(data=self.data, x=column, bins=bins)

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel("Antal personer")

        plt.tight_layout()
        plt.show()

    def plot_scatter(self, x, y, title, xlabel, ylabel):
        """Rita ett spridningsdiagram för två numeriska kolumner."""
        plt.figure(figsize=(8, 5))

        sns.scatterplot(data=self.data, x=x, y=y, alpha=0.5,color="#00868B")

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.tight_layout()
        plt.show()

    def linear_regression(self, predictors, outcome):
        """Skatta linjär regression och returnera modellens resultat."""
        data = self.data[predictors + [outcome]].dropna()

        # Förklarande variabler som matris och utfall som vektor
        X = data[predictors].to_numpy(dtype=float)
        y = data[outcome].to_numpy(dtype=float)

        # En kolumn med ettor gör att modellen får ett intercept
        X = np.column_stack([np.ones(len(data)), X])

        coefficients = np.linalg.lstsq(X, y, rcond=None)[0]

        predicted = X @ coefficients
        residuals = y - predicted

        ss_residual = np.sum(residuals ** 2)
        ss_total = np.sum((y - y.mean()) ** 2)

        r_squared = (
            1 - ss_residual / ss_total
            if ss_total > 0 else np.nan
        )

        return {
            "intercept": coefficients[0],
            "coefficients": dict(zip(predictors, coefficients[1:])),
            "r_squared": r_squared,
            "predicted": predicted,
            "residuals": residuals,
            "n": len(data)
        }

    def plot_residuals(self, model):
        """Rita residualer mot modellens skattade värden."""
        plt.figure(figsize=(8, 5))

        plt.scatter(
            model["predicted"],
            model["residuals"],
            color="blue",
            alpha=0.5
        )

        plt.axhline(0, color="red", linestyle="--")

        plt.title("Residualer för multipel linjär regression")
        plt.xlabel("Skattat systoliskt blodtryck")
        plt.ylabel("Residual: observerat − skattat")

        plt.tight_layout()
        plt.show()

    def pca(self, columns):
        """Beräkna PCA med SVD efter standardisering av valda kolumner.

        Rader med saknade värden utesluts. Returnerar standardiserade
        data, komponentvikter, komponentpoäng och förklarad varians.
        """
        data = self.data[columns].dropna()

        if len(data) < 2:
            raise ValueError("PCA kräver minst två kompletta observationer.")

        std = data.std(ddof=1)

        if (std == 0).any():
            raise ValueError("PCA kräver kolumner med variation.")

        standardized = (data - data.mean()) / std
        X = standardized.to_numpy(dtype=float)

        _, singular_values, Vt = np.linalg.svd(
            X, full_matrices=False
        )

        variance = singular_values ** 2 / (len(data) - 1)
        explained_ratio = variance / variance.sum()

        components = [
            f"PC{i + 1}" for i in range(len(explained_ratio))
        ]

        weights = pd.DataFrame(
            Vt.T,
            index=columns,
            columns=components
        )

        scores = pd.DataFrame(
            X @ Vt.T,
            index=data.index,
            columns=components
        )

        variance_table = pd.DataFrame({
            "component": components,
            "explained_percent": explained_ratio * 100,
            "cumulative_percent": np.cumsum(explained_ratio) * 100
        })

        return {
            "standardized": standardized,
            "weights": weights,
            "scores": scores,
            "explained_ratio": explained_ratio,
            "variance_table": variance_table
        }                        
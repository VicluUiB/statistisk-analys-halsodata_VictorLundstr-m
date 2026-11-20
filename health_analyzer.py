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

    def plot_histogram(self, bins=25):
        """Visa histogram för fem numeriska hälsovariabler."""
        columns = [
            "age", "height", "weight", "systolic_bp", "cholesterol"
        ]

        labels = {
            "age": "Ålder",
            "height": "Längd",
            "weight": "Vikt",
            "systolic_bp": "Systoliskt blodtryck",
            "cholesterol": "Kolesterol"
        }

        fig, axes = plt.subplots(2, 3, figsize=(14, 8))
        axes = axes.flatten()

        for ax, column in zip(axes, columns):
            sns.histplot(
                data=self.data,
                x=column,
                bins=bins,
                color="#00C5CD",
                edgecolor="#00C5CD",
                linewidth=0.5,
                ax=ax
            )

            ax.set_title(labels[column])
            ax.set_xlabel(labels[column])
            ax.set_ylabel("Antal personer per intervall")

        axes[-1].set_visible(False)

        fig.suptitle(
            "Fördelning av numeriska hälsovariabler",
            fontsize=16
        )

        fig.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    def plot_smoking_by_sex(self):
        """Visa procentuell fördelning av rökstatus inom varje kön."""
        smoker_percent = (
            self.data.groupby("sex")["smoker"]
            .value_counts(normalize=True)
            .mul(100)
            .rename("andel")
            .reset_index()
        )

        smoker_percent["kön"] = smoker_percent["sex"].map({
            "F": "Kvinnor",
            "M": "Män"
        })

        smoker_percent["rökstatus"] = smoker_percent["smoker"].map({
            "No": "Icke-rökare",
            "Yes": "Rökare"
        })

        colors = {"Kvinnor": "#00C5CD", "Män": "#FFC125"}

        plt.figure(figsize=(8, 5))

        sns.barplot(
            data=smoker_percent,
            x="rökstatus",
            y="andel",
            hue="kön",
            palette=colors,
            order=["Icke-rökare", "Rökare"],
            hue_order=["Kvinnor", "Män"],
            errorbar=None
        )

        plt.title("Andel rökare och icke-rökare inom respektive kön")
        plt.xlabel("Rökstatus")
        plt.ylabel("Andel inom respektive kön (%)")
        plt.ylim(0, 100)
        plt.legend(title="Kön")

        plt.tight_layout()
        plt.show()

        return smoker_percent[["kön", "rökstatus", "andel"]]    

    def plot_boxplot(self):
        """Visa viktfördelning per kön med boxplot och individpunkter."""
        plt.figure(figsize=(8, 5))

        colors = {"F": "#00C5CD", "M": "#FFC125"}

        sns.boxplot(
            data=self.data,
            x="sex",
            y="weight",
            order=["F", "M"],
            hue="sex",
            palette=colors,
            fill=False,
            linewidth=1.5,
            dodge=False,
            legend=False,
            showfliers=False
        )

        sns.swarmplot(
            data=self.data,
            x="sex",
            y="weight",
            order=["F", "M"],
            hue="sex",
            palette=colors,
            dodge=False,
            legend=False,
            alpha=0.6
        )

        plt.title("Viktfördelning per kön")
        plt.xlabel("Kön")
        plt.ylabel("Vikt [kg]")
        plt.xticks([0, 1], ["Kvinnor", "Män"])

        plt.tight_layout()
        plt.show()

    def plot_confidence_interval(self, mean, lower, upper):
        """Visa ett medelvärde med dess 95-procentiga konfidensintervall."""
        fig, ax = plt.subplots(figsize=(8, 3))

        ax.errorbar(
            x=mean,
            y=0,
            xerr=[[mean - lower], [upper - mean]],
            fmt="o",
            color="#00C5CD",
            capsize=6,
            markersize=8,
            linewidth=2
        )

        ax.set_yticks([])
        ax.set_xlabel("Systoliskt blodtryck")
        ax.set_title("Medelblodtryck med 95 % konfidensintervall")

        ax.annotate(
            f"{mean:.2f}",
            xy=(mean, 0),
            xytext=(0, 12),
            textcoords="offset points",
            ha="center"
        )

        fig.tight_layout()
        plt.show()    

    def plot_ci_comparison(
        self, mean, normal_lower, normal_upper,
        bootstrap_lower, bootstrap_upper
    ):
        """Jämför två 95-procentiga konfidensintervall för samma medelvärde."""
        fig, ax = plt.subplots(figsize=(9, 4))

        intervals = [
            ("Normalapproximation", normal_lower, normal_upper, "#00868B"),
            ("Bootstrap", bootstrap_lower, bootstrap_upper, "#E69F00")
        ]

        for position, (label, lower, upper, color) in enumerate(intervals):
            ax.hlines(position, lower, upper, color=color, linewidth=2)
            ax.plot(
                [lower, upper],
                [position, position],
                "|",
                color=color,
                markersize=12
            )
            ax.plot(mean, position, "o", color=color)

            ax.annotate(
                f"[{lower:.2f}; {upper:.2f}]",
                xy=(mean, position),
                xytext=(0, 12),
                textcoords="offset points",
                ha="center"
            )

        ax.set_yticks([0, 1])
        ax.set_yticklabels(["Normalapproximation", "Bootstrap"])
        ax.set_ylim(-0.5, 1.5)
        ax.set_xlabel("Systoliskt blodtryck")
        ax.set_title("Jämförelse av 95 % konfidensintervall")
        ax.grid(axis="x", alpha=0.3)

        fig.tight_layout()
        plt.show()

    def plot_scatter(self, x, y, title, xlabel, ylabel):
        """Rita ett spridningsdiagram för två numeriska kolumner."""
        plt.figure(figsize=(8, 5))

        sns.scatterplot(data=self.data, x=x, y=y, alpha=0.5,color="#00C5CD")

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
            color="#00C5CD",
            alpha=0.5
        )

        plt.axhline(0, color="#FFC125", linestyle="--")

        plt.title("Residualer för multipel linjär regression")
        plt.xlabel("Skattat systoliskt blodtryck")
        plt.ylabel("Residual: observerat − skattat")

        plt.tight_layout()
        plt.show()          
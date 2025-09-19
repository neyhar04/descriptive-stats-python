import numpy as np
import pandas as pd
from scipy import stats

scores = [
    88,45,53,86,33,86,85,30,89,53,41,96,56,38,62,
    71,51,86,68,29,28,47,33,27,25,36,33,94,73,46,
    42,34,79,72,88,99,82,62,57,42,28,55,67,62,60,
    96,61,57,75,93,34,75,53,32,28,73,51,69,91,35
]

data = pd.Series(scores)

# Descriptive statistics
stats_dict = {
    "Valid": data.count(),
    "Mode": data.mode().iloc[0],   # only first mode like SPSS
    "Median": data.median(),
    "Mean": data.mean(),
    "Std. Deviation": data.std(ddof=1),
    "Variance": data.var(ddof=1),
    "Skewness": stats.skew(data),
    "Std. Error of Skewness": stats.skew(data) / np.sqrt(data.count()),
    "Kurtosis": stats.kurtosis(data),
    "Std. Error of Kurtosis": stats.kurtosis(data) / np.sqrt(data.count()),
    "Minimum": data.min(),
    "Maximum": data.max(),
    "25th percentile": np.percentile(data, 25),
    "50th percentile": np.percentile(data, 50),
    "75th percentile": np.percentile(data, 75),
    "90th percentile": np.percentile(data, 90),
    "95th percentile": np.percentile(data, 95),
}

# Convert to table format
table = pd.DataFrame.from_dict(stats_dict, orient="index", columns=["Score"])

print("\nDescriptive Statistics")
print(table)
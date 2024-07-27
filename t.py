import math
from scipy.stats import norm
import numpy as np

def two_sample_u_test(x, y, significance_level=0.05):
    """
    Perform a two-sample u-test.

    Parameters:
    x (list or numpy array): Sample data from the first population
    y (list or numpy array): Sample data from the second population
    significance_level (float): Significance level for the test (default is 0.05)

    Returns:
    dict: Results of the test containing the u statistic, critical value, and conclusion
    """
    # Calculate the means
    x_bar = np.mean(x)
    y_bar = np.mean(y)

    # Calculate the standard deviations
    sigma_x = np.std(x, ddof=1)  # Sample standard deviation
    sigma_y = np.std(y, ddof=1)  # Sample standard deviation

    # Calculate the sample sizes
    n_x = len(x)
    n_y = len(y)

    # Calculate the u statistic
    u = (x_bar - y_bar) / math.sqrt((sigma_x ** 2 / n_x) + (sigma_y ** 2 / n_y))

    # Determine the critical value for the given significance level
    critical_value = norm.ppf(1 - significance_level / 2)

    # Decision based on the critical value
    if abs(u) >= critical_value:
        conclusion = "Reject the null hypothesis: The means of the two samples are significantly different."
    else:
        conclusion = "Fail to reject the null hypothesis: No significant difference between the means of the two samples."

    return {
        "u_statistic": u,
        "critical_value": critical_value,
        "conclusion": conclusion
    }

# Example usage:
x = [5.1, 4.9, 5.0, 5.2, 5.3, 4.8, 5.1]  # Sample data from the first population
y = [4.5, 4.6, 4.4, 4.6, 4.7, 4.5, 4.4]  # Sample data from the second population

result = two_sample_u_test(x, y, significance_level=0.05)
#print(result)

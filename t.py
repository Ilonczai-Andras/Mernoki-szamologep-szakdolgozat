import numpy as np  
from scipy import stats
import statistics
from sympy import sqrt, N

def t_test(self, mu=None, alpha=None, x=None, y=None):

    if x is not None and mu is not None and alpha is not None:
        result_string = ""

        avg = statistics.mean(x)
        stan_dev = statistics.stdev(x)
        m = mu
        n = len(x)

        Alpha = 1 - alpha
        df = n - 1


        t = N( (avg - m) / (stan_dev / sqrt(n)) )

        t_p = stats.t.ppf(q= Alpha/2,df= df)
        print(f"df: {df} t: {t}")
        p_value = 2 * (1 - stats.t.sf(abs(float(t)), df))

        if abs(t) >= t_p:
            
            result_string += f"\nA nullhipotézist elvetjük t: {t} p: {2 - p_value}\n"
            result_string += f"two tail  p:{stats.t.ppf(q= Alpha/2,df= df)}" +"\n"
            result_string += f"one tail  p:{stats.t.ppf(q= Alpha,df= df)}" +"\n"
        elif abs(t) < t_p:
            result_string += f"\nA nullhipotézist elfogadjuk t: {t} p: {2 - p_value}\n"
            result_string += f"two tail  p:{stats.t.ppf(q= Alpha/2,df= df)}" +"\n"
            result_string += f"one tail  p:{stats.t.ppf(q= Alpha,df= df)}" +"\n"

        print(result_string)
    if (x is not None and y is not None and alpha is not None):

        # Perform two-sample t-test
        t_statistic, p_value = stats.ttest_ind(x, y)

        Alpha = 1 - alpha
        if p_value < Alpha:
            print("H0-t elvetjük")
        else:
            print("H0-t elfogadjuk")

        print(f"P: {p_value} T: {t_statistic}")

x = [41, 34, 33, 36, 40, 25, 31, 37, 34, 30, 38]
y = [52, 57, 62, 55, 64, 57, 56, 55]

t_test(mu=40,alpha=0.95, x=[41, 34, 33, 36, 40, 25, 31, 37, 34, 30, 38])

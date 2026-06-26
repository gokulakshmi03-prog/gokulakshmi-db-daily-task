import numpy as np
import pandas as pd
data=pd.read_csv("employee_salary_dataset.csv")
salary=data["Monthly_Salary"]
population_mean=np.mean(salary)
print("population mean salary=",population_mean)

sample=[118179,65764,99543,70714,81835,127946,134616,
        130983,98744,81491,149123,43589,68484,107989,61212,68525,57635]

from scipy import stats
sample_mean=np.mean(sample)
ci=stats.t.interval(
    confidence=0.95,
    df=len(sample)-1,
    loc=sample_mean,
    scale=stats.sem(sample)
)
print("sample mean=",sample_mean)
print("95% confidence Interval=",ci)

from scipy.stats import norm
sample=[55746,74377,73404,79045,122888,64790,132455,30600
        ,119660,118179,65764,99543,70714,81835,127946,134616,130983,
        98744,81491,149123,43589,68484,107989,61212,68525,72202,57635,88208,58828,43711,28420]
sample_mean=np.mean(sample)
sample_std=np.std(sample,ddof=1)
n=len(sample)
z=1.96
margin_error=z*(sample_std/np.sqrt(n))
lower_ci=sample_mean-margin_error
upper_ci=sample_mean+margin_error
print("sample size=",n)
print("sample mean=",round(sample_mean,2))
print("sample standard deviation=",round(sample_std,2))
print("margin of error=",round(margin_error,2))
print("\n95% z-confidence Interval")
print("lower bound=",round(lower_ci,2))
print("upper bound=",round(upper_ci,2))
      
            




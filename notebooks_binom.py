import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np
n=15
p=0.5
k=4
prob=binom.pmf(k,n,p)
print(prob)

x=np.arange(0,n+1)
pmf_values=binom.pmf(x,n,p)
plt.bar(x,pmf_values,color="PURPLE",edgecolor="black",label="binomial pmf")
plt.bar(k,prob,color="darkblue",edgecolor="black",label=f"k={k}")
plt.xlabel("number of successes")
plt.ylabel("probability")
plt.title(f"binomial distribution")
plt.legend()
plt.grid(axis="y",alpha=0.4)
plt.show()

from scipy.stats import binom
n=12
p=0.6
k=10
p=binom.cdf(k,n,p)
print(p)




from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt
mean_time=5
t=1
lambda_value=1/mean_time
prob_within=expon.cdf(t,scale=1/lambda_value)
print("probability cash within one hours",round(prob_within*100,2),"%")

import numpy as np
import matplotlib.pyplot as plt
mean_time=5
data=np.random.exponential(mean_time,10000)
plt.hist(data,bins=30,density=True)
plt.title("exponencial distribution - histogram")
plt.xlabel("time(hours)")
plt.ylabel("cash")
plt.grid(True)
plt.show()

from scipy.stats import uniform 
import numpy as np
import matplotlib.pyplot as plt
a=1
b=100
low=30
high=60
dist=uniform(loc=a,scale=b-a)
probability=dist.cdf(high)-dist.cdf(low)
print("probability of getting the number between 30 and 60:",round(probability*100,2),"%")

import numpy as np
import matplotlib.pyplot as plt
data=np.random.uniform(1,100,1000)
plt.hist(data,bins=30,edgecolor="black")
plt.title("uniform distribution")
plt.xlabel("numbers(1 to 100)")
plt.ylabel("frequency")
plt.grid(True)
plt.show()


from scipy.stats import uniform 
import numpy as np
import matplotlib.pyplot as plt
a=0
b=20
low=5
high=10
dist=uniform(loc=a,scale=b-a)
probability=dist.cdf(high)-dist.cdf(low)
print("probability of getting the number between 30 and 60:",round(probability*100,2),"%")

import numpy as np
import matplotlib.pyplot as plt
data=np.random.uniform(1,100,1000)
plt.hist(data,bins=30,edgecolor="black")
plt.title("uniform distribution")
plt.xlabel("numbers(1 to 100)")
plt.ylabel("frequency")
plt.grid(True)
plt.show()




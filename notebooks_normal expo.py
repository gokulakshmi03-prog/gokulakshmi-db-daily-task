from scipy.stats import norm
mu=100
sigma=15
x=90-110
prob_grather=1-norm.cdf(x,mu,sigma)
print("probability is greather x",round(prob_grather*100,2),"%")


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
mu=100
sigma=15
x=np.random.normal(mu,sigma,10000)
plt.hist(x,bins=35,density=True,alpha=0.6)
xmin,xmax=plt.xlim()
x=np.linspace(xmin,xmax,1000)
y=norm.pdf(x,mu,sigma)
plt.plot(x,y,linewidth=2)
plt.title("normal distribution histogram\n bell shaped curve")
plt.xlabel("iQ (cm)")
plt.ylabel("density")
plt.grid(True)
plt.show()

from scipy.stats import norm
mu=65
sigma=8
x=60
prob_greater=1-norm.cdf(x,mu,sigma)
print("probability is",round(prob_greater*100,2),"%")


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
mu=65
sigma=8
x=np.random.normal(mu,sigma,10000)
plt.hist(x,bins=35,density=True,alpha=0.6)
xmin,xmax=plt.xlim()
x=np.linspace(xmin,xmax,1000)
y=norm.pdf(x,mu,sigma)
plt.plot(x,y,linewidth=2)
plt.title("normal distribution histogram\n bell shaped curve")
plt.xlabel("weight")
plt.ylabel("density")
plt.grid(True)
plt.show()

from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt
mean_time=10
t=3
lamda_value=1/mean_time
prob_within=expon.cdf(t,scale=1/lamda_value)
print("probabily customer arrives in 3 mins:",round(prob_within*100,2),"%")


import numpy as np
import matplotlib.pyplot as plt
mean_time=10
data=np.random.exponential(mean_time,10000)
plt.hist(data,bins=30,density=True)
plt.title("exponencial distribution,histogram")
plt.xlabel("time(MIN)")
plt.ylabel("density")
plt.grid(True)
plt.show()





import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
df=pd.read_csv("penguins_lter.csv")
stats.probplot(
    df["Culmen Length (mm)"],
    dist="norm",
    plot=plt
)
plt.title("normal distribution qq plot")
plt.show()

df=pd.read_csv("penguins_lter.csv")
df

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
df=pd.read_csv("student.csv")
stats.probplot(
    df["age"],
    dist="norm",
    plot=plt
)
plt.title("qq plot-age")
plt.show()




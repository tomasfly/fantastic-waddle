# Linear regression model
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

data_root="./resources/"
lifesat=pd.read_csv(data_root+"lifesat.csv")
x = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

lifesat.plot(kind='scatter', x="GDP per capita (USD)", y='Life satisfaction',grid=True)
plt.axis([23_500, 62_500, 4, 9])
plt.show()
model=LinearRegression()
model.fit(x,y)
X_new=[[37_655.2]]
print(model.predict(X_new))
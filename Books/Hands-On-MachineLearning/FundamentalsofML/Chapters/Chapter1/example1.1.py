# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# %%
data = "https://github.com/ageron/data/raw/main/lifesat/lifesat.csv"
lifesat = pd.read_csv(data)
print(lifesat)

X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# %%
print(X)

# %%
print(y)
# %%
plt.scatter(X,y,color='blue', marker='o')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.axis([23_500, 62_500, 4, 9])
plt.grid(True)
plt.show()
# %%
# Visualize the data
lifesat.plot(kind='scatter', grid=True,
x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()
# %%
model = LinearRegression()

model.fit(X,y)
# %%
# Make a prediction for Cyprus
X_new = [[37_655.2]] # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # output: [[6.30165767]]
# %%
from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=3)
model.fit(X,y)
# Make a prediction for Cyprus
X_new = [[37_655.2]] # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # output: [[6.30165767]]
# %%

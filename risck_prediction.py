from sklearn.linear_model import LinearRegression
import numpy as np

def predict_water_level(levels):
    X = np.arange(len(levels)).reshape(-1, 1)
    y = np.array(levels)

    model = LinearRegression()
    model.fit(X, y)

    future = model.predict([[len(levels) + 2]])
    return round(future[0], 2)

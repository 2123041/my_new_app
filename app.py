import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Simple Linear Regression App")

st.write("This app finds the best line that fits a set of points.")

# Creating the form to get inputs
x = st.slider("x", 0, 10, 5)
y = st.slider("y", 0, 10, 5)

# Creating the linear regression model
model = LinearRegression()

# Fitting the model
X = np.array(x).reshape(-1, 1)
Y = np.array(y).reshape(-1, 1)
model.fit(X, Y)

# Predicting the y value
y_pred = model.predict([[x]])[0][0]

# Plotting the points
st.write("Points")
st.scatter_chart(pd.DataFrame({'x':x, 'y':y}))

# Plotting the line
st.write("Line")
st.line_chart(pd.DataFrame({'x':x, 'y':y_pred}))

st.write("y = {:.2f}x + {:.2f}".format(model.coef_[0][0], model.intercept_[0]))

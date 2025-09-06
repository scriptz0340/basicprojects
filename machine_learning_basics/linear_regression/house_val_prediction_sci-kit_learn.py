import numpy as np
from sklearn.linear_model import LinearRegression

# Define input features (2 samples, 2 features each: [rooms, year built])
x = np.array([[3, 2015], [5, 2023]])

# Define target values (house prices in millions)
y = np.array([0.8, 1.6])

# Create the linear regression model
model = LinearRegression()

# Fit the model to the data using least squares minimization
# This finds the best-fit line in 2D feature space, minimizing total error
model.fit(x, y)

# Extract the learned coefficients (slopes for each feature)
# b0 = slope for 'rooms', b1 = slope for 'year built'
b0, b1 = model.coef_

# Extract the y-intercept (where the plane crosses the value axis)
a = model.intercept_

# Define a new house with 4 rooms and built in 2021
new_sample = np.array([[4, 2021]])

# Predict the house price using the learned model
# This internally uses: y = a + b0 * x[0] + b1 * x[1]
result = model.predict(new_sample)

# Output the results: coefficients and predicted value
print("b0: {}, b1: {}, y: {}".format(
    b0, b1, result[0]
))



## Key Differences Between Manual Version and scikit-learn Version

# 1. Slope Calculation:
#    Manual: Uses (y2 - y1) / (x2 - x1) for each feature individually.
#    sklearn: Uses least squares regression to find the best-fit slopes 
#    across all features and samples.

# 2. Intercept Calculation:
#    Manual: Calculated manually using one data point and the slopes.
#    sklearn: Computed automatically as part of the model fitting process 
#    to minimize overall prediction error.

# 3. Prediction:
#    Manual: Uses the linear formula explicitly (y = a + b0*x[0] + b1*x[1]).
#    sklearn: Uses the model's .predict() method, which applies the same 
#    formula internally.

# 4. Scalability:
#    Manual: Only works with two points and becomes impractical with more data.
#    sklearn: Can handle thousands of samples and multiple features efficiently.

# 5. Statistical Accuracy:
#    Manual: Good for learning, but not statistically reliable.
#    sklearn: Uses a proven statistical method (least squares) to find the 
#    optimal model for the data.



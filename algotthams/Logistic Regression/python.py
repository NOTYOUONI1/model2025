import numpy as np
from sklearn.linear_model import LogisticRegression

# Example data
X_train = np.array([[50],[40],[30],[15],[10],[5]])  # 6 samples, 1 feature each
Y_train = np.array([1, 1, 1, 0, 0, 0])  # 6 samples (binary classification)

# Create and fit the model
module = LogisticRegression()
model = module.fit(X_train, Y_train)

# Example test data
X_test = np.array([[41], [42],[43],[44],[45],[46],[47],[48],[49]])

# Predict
y_pred = model.predict(X_test)
print(y_pred)

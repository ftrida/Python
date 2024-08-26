import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example sales data (date, sales)
data = {
    'date': pd.date_range(start='1/1/2020', periods=30, freq='M'),
    'sales': [100, 120, 130, 140, 160, 180, 200, 210, 220, 230, 250, 260,
              270, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600]
}
df = pd.DataFrame(data)

# Prepare data for model
df['month'] = df['date'].dt.month
X = df[['month']]
y = df['sales']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Visualize results
plt.plot(df['date'], df['sales'], label='Actual Sales')
plt.plot(df['date'][X_test.index], y_pred, label='Predicted Sales', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Forecasting')
plt.legend()
plt.show()

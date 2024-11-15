import requests
import pandas as pd
import matplotlib.pyplot as plt

# тестируем Requests
response = requests.get('https://www.example.com')
print(response.text)

# тестируем Pandas
data = pd.read_csv('data.csv')
print(data.head())
mean_value = data['average_score'].mean()
median_value = data['average_score'].median()
std_deviation = data['average_score'].std()
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation}")

# тестируем Matplotlib
x = data['average_score']
y = data['total_score']
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()




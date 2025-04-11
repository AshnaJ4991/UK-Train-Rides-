import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st

# Importing the dataset
df = pd.read_csv("railway.csv")
'''# Checking the dimensions of the dataset
print(df.shape)
# Listing the columns of the dataset
print(df.columns)
# Viewing the first five rows of the dataset
print(df.head())
# Viewing the last five rows of the dataset
print(df.tail())
# Viewing all the information about the dataset
print(df.info())
# Viewing all the information about the dataset
print(df.info())
# Descriptive statistics of the dataset
print(df.describe())
# Checking for missing values in the dataset and their total count
print(df.isnull().sum())
# Viewing the maximum values in the dataset
# Select the numerical column
price = df["Price"]
# Calculate statistics
mean_price = price.mean()
median_price = price.median()
mode_price = price.mode().tolist()
max_price = price.max()
min_price = price.min()
count_price = price.count()

# Display results
print("Mean Price:", mean_price)
print("Median Price:", median_price)
print("Mode Price:", mode_price)
print("Max Price:", max_price)
print("Min Price:", min_price)
print("Count:", count_price)

# Cleaning the dataset by dropping rows with missing values
print(df.dropna(inplace=True))

#Objective 1: Average Ticket Price by Departure Station and Ranked them
average_price_by_station = df.groupby('Departure Station')['Price'].mean().sort_values(ascending=False)
print(average_price_by_station)
print("\n")

# Objective 2: Identify outliers in ticket prices using the IQR method
print("Objective 2: Outliers in Ticket Prices (IQR Method)")
Q1 = np.percentile(df['Price'], 25)
Q3 = np.percentile(df['Price'], 75)
IQR = Q3 - Q1
outliers = df[(df['Price'] < (Q1 - 1.5 * IQR)) | (df['Price'] > (Q3 + 1.5 * IQR))]
print(outliers[['Departure Station', 'Arrival Destination', 'Price']])
print("\n")

# Objective 3: Analyze the percentage of delayed journeys by reason for delay
print("Objective 3: Percentage of Delayed Journeys by Reason")
delayed_journeys = df[df['Journey Status'] == 'Delayed']
delay_reason_counts = delayed_journeys['Reason for Delay'].value_counts(normalize=True) * 100
print(delay_reason_counts)
print("\n")

# Objective 4: Compare the average ticket price for different ticket classes
print("Objective 4: Average Ticket Price by Ticket Class")
average_price_by_class = df.groupby('Ticket Class')['Price'].mean()
print(average_price_by_class)

# Objective 5: Analyze the distribution of payment methods
print("Objective 5: Distribution of Payment Methods")
payment_method_distribution = df['Payment Method'].value_counts(normalize=True) * 100
print(payment_method_distribution)


# 1. HISTOGRAM
plt.figure(figsize=(8, 4))
sns.histplot(df['Price'], kde=False, bins=30, color='skyblue')
plt.title('Histogram of Ticket Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 2. Bar Plot – Average ticket price by class
plt.figure(figsize=(6, 4))
sns.barplot(x='Ticket Class', y='Price', data=df, estimator=np.mean, palette='muted')
plt.title('Average Ticket Price by Class')
plt.ylabel('Average Price')
plt.tight_layout()
plt.show()

# 3. Boxplot - Price by Ticket Type
sns.boxplot(x='Ticket Type', y='Price', data=df, palette="Set3")
plt.title("Boxplot: Price by Ticket Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#4. Donut Chart - Purchase Type Distribution
purchase_counts = df ['Purchase Type']. value_counts()
colors = sns.color_palette('pastel')[0:len(purchase_counts)]

fig, ax = plt.subplots()
ax.pie(purchase_counts, labels=purchase_counts.index, colors=colors, startangle=90, wedgeprops={'width': 0.4})
ax.set_title('Donut Chart: Purchase Type Distribution')
plt.tight_layout()
plt.show()

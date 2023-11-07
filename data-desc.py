import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the data
data = pd.read_csv('C:/Users/victo/Downloads/simulated_insurance_data.csv') # Change path to the location of the downloaded simulated_insurance_data.csv 
# Checking for missing values
missing_values = data.isnull().sum()
# Checking for duplicates
duplicates = data.duplicated().sum()
# Checking for data types
data_types = data.dtypes

# Summary statistics
summary_statistics = data.describe()
summary_category = data.describe(include=['object'])

# Set the aesthetic style of the plot
sns.set_style('whitegrid')

# Histograms for age, coverage amount, premium, and risk factor
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distributions of Key Numerical Variables')

# Age Distribution
sns.histplot(data['Age'], bins=30, kde=False, ax=axes[0, 0])
axes[0, 0].set_title('Age Distribution')

# Coverage Amount Distribution
sns.histplot(data['Coverage_Amount'], bins=30, kde=False, ax=axes[0, 1])
axes[0, 1].set_title('Coverage Amount Distribution')

# Premium Distribution
sns.histplot(data['Premium'], bins=30, kde=False, ax=axes[1, 0])
axes[1, 0].set_title('Premium Distribution')

# Risk Factor Distribution
sns.histplot(data['Risk_Factor'], bins=30, kde=False, ax=axes[1, 1])
axes[1, 1].set_title('Risk Factor Distribution')

# Adjust subplots to fit the title
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Box plots for claims count and total claim cost
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Box Plots for Claims Data')

# Claims Count Box Plot
sns.boxplot(y=data['Claims_Count'], ax=axes[0])
axes[0].set_title('Claims Count Box Plot')

# Total Claim Cost Box Plot
sns.boxplot(y=data['Total_Claim_Cost'], ax=axes[1])
axes[1].set_title('Total Claim Cost Box Plot')

# Adjust subplots to fit the title
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Select only the numeric data for correlation matrix
numeric_cols = ['Policy_ID', 'Age', 'Coverage_Amount', 'Premium', 'Deductible',
                'Risk_Factor', 'Claims_Count', 'Total_Claim_Cost', 'Customer_Feedback_Score']

# Correlation matrix heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data[numeric_cols].corr(), annot=True, fmt=".2f")
plt.title('Correlation Matrix Heatmap')

plt.show()


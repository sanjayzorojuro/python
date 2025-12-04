import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)
print(df)


# # Read from CSV
# df = pd.read_csv('data.csv')

# # Write to CSV
# df.to_csv('output.csv', index=False)


# View top rows
print(df.head())

# Info and stats
print(df.info())
print(df.describe())


# Single column
print(df['Name'])

# Multiple columns
print(df[['Name', 'Age']])

# Row by index
print(df.iloc[1])        # Second row
print(df.loc[1])         # Row with label/index = 1


# People older than 30
print(df[df['Age'] > 30])

# Filter by multiple conditions
print(df[(df['Age'] > 25) & (df['City'] == 'London')])


# Add new column
df['Country'] = ['USA', 'France', 'UK']

# Modify existing column
df['Age'] = df['Age'] + 1


# Drop rows with any NaNs
df.dropna(inplace=True)

# Fill missing values
df.fillna('Unknown', inplace=True)


# Example group by
grouped = df.groupby('City')['Age'].mean()
print(grouped)


# Sort by Age
print(df.sort_values(by='Age'))

# Sort descending
print(df.sort_values(by='Age', ascending=False))

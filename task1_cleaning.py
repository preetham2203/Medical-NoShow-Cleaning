import pandas as pd

# Load the dataset
df = pd.read_csv("KaggleV2-May-2016.csv")

# Rename columns (clean column names)
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
print("✅ Column names cleaned:")
print(df.columns)

# Convert scheduledday and appointmentday to datetime
df['scheduled_date'] = pd.to_datetime(df['scheduledday']).dt.date
df['appointment_date'] = pd.to_datetime(df['appointmentday']).dt.date

# Drop the original columns
df.drop(['scheduledday', 'appointmentday'], axis=1, inplace=True)

print("\n✅ Date columns converted and cleaned.")
print(df[['scheduled_date', 'appointment_date']].head())

# Clean 'age' column: keep only reasonable values (0-100)
df = df[(df['age'] >= 0) & (df['age'] <= 100)]

# Clean 'handcap' column: convert all values > 1 to 1
df['handcap'] = df['handcap'].apply(lambda x: 1 if x > 1 else x)

# Rename 'no-show' values for better understanding
df['no-show'] = df['no-show'].map({'No': 'Show', 'Yes': 'No-Show'})

print("\n✅ Cleaned 'age', 'handcap', and 'no-show' columns:")
print(df[['age', 'handcap', 'no-show']].head())

# Check for missing/null values
print("\n🔍 Checking for missing values:")
print(df.isnull().sum())


# Save the cleaned dataset to a new file
df.to_csv("cleaned_medical_appointments.csv", index=False)
print("\n💾 Cleaned dataset saved as 'cleaned_medical_appointments.csv'")

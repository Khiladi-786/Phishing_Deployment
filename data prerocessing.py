import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Load Data
df = pd.read_csv('dataset_phishing.csv')

# 2. Data Cleaning
# (No missing values or duplicates found to remove)
df_clean = df.drop(columns=['url'])  # Remove ID column

# 3. Feature Encoding
le = LabelEncoder()
df_clean['status'] = le.fit_transform(df_clean['status'])
# Mapping: {'legitimate': 0, 'phishing': 1}

# 4. Data Splitting
X = df_clean.drop('status', axis=1)
y = df_clean['status']

# Stratify ensures equal distribution of legitimate/phishing in both sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Normalization (Fit on Train, Transform Test)
scaler = StandardScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

# 6. Final Export
# Reattach target variable for the final CSVs
train_processed = pd.concat([X_train_scaled, y_train.reset_index(drop=True)], axis=1)
test_processed = pd.concat([X_test_scaled, y_test.reset_index(drop=True)], axis=1)

# Save to CSV
train_processed.to_csv('train_processed.csv', index=False)
test_processed.to_csv('test_processed.csv', index=False)

print("Preprocessing Complete. Files saved: train_processed.csv, test_processed.csv")
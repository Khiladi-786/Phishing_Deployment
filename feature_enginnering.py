import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# 1. Load Original Data
df = pd.read_csv('dataset_phishing.csv')

# 2. Feature Engineering
# Create sum of all special character columns (columns starting with 'nb_')
count_cols = [col for col in df.columns if col.startswith('nb_')]
df['total_special_chars'] = df[count_cols].sum(axis=1)
# Create ratio of special characters to length
df['special_char_ratio'] = df['total_special_chars'] / (df['length_url'] + 1)

# 3. Encode Target
le = LabelEncoder()
df['status_encoded'] = le.fit_transform(df['status'])

# 4. Feature Selection (Top 20 + New Features)
X = df.drop(columns=['url', 'status', 'status_encoded'])
y = df['status_encoded']

# Train simple model to get importance
rf = RandomForestClassifier(n_estimators=50, random_state=42)
rf.fit(X, y)

# Get Top 20 features
feature_imp = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
top_20_features = feature_imp.head(20).index.tolist()

# Ensure our new features are included (they likely are in top 20, but just in case)
final_features = list(set(top_20_features + ['total_special_chars', 'special_char_ratio']))

# 5. Create and Save Refined Dataset
refined_df = df[final_features + ['status_encoded']]
refined_df.to_csv('refined_dataset.csv', index=False)

print(f"Refined dataset created with {refined_df.shape[1]} columns.")
print("Top 5 Features:", top_20_features[:5])
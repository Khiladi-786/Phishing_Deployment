import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import joblib

# 1. Load Data
df = pd.read_csv('dataset_phishing.csv')

# 2. Feature Engineering
# Create 'total_special_chars' and 'special_char_ratio'
count_cols = [col for col in df.columns if col.startswith('nb_')]
df['total_special_chars'] = df[count_cols].sum(axis=1)
df['special_char_ratio'] = df['total_special_chars'] / (df['length_url'] + 1)

# 3. Preprocessing
# Drop ID 'url' and redundant 'longest_word_path'
df_clean = df.drop(columns=['url', 'longest_word_path'])
le = LabelEncoder()
df_clean['status'] = le.fit_transform(df_clean['status'])

X = df_clean.drop('status', axis=1)
y = df_clean['status']

# Split 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train Random Forest (Best Model)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# 5. Evaluate
y_pred = rf_model.predict(X_test_scaled)
y_prob = rf_model.predict_proba(X_test_scaled)[:, 1]

print(f"Random Forest Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Random Forest F1 Score: {f1_score(y_test, y_pred):.4f}")
print(f"Random Forest ROC AUC:  {roc_auc_score(y_test, y_prob):.4f}")

# 6. Save Model
joblib.dump(rf_model, 'best_phishing_model.pkl')
print("Model saved as 'best_phishing_model.pkl'")
import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt

# 1. Load Data & Model
df = pd.read_csv('dataset_phishing.csv') # Use refined/processed data if available
model = joblib.load('best_phishing_model.pkl')

# Re-engineer features (Must match training time)
count_cols = [col for col in df.columns if col.startswith('nb_')]
df['total_special_chars'] = df[count_cols].sum(axis=1)
df['special_char_ratio'] = df['total_special_chars'] / (df['length_url'] + 1)

# Prepare X (Ensure columns match model training exactly)
# Drop non-feature columns used in training
cols_to_drop = ['url', 'status', 'longest_word_path'] 
X = df.drop(columns=cols_to_drop, errors='ignore')

# 2. SHAP Explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# 3. Generate Plots
# Summary Plot (Global Importance)
plt.figure()
shap.summary_plot(shap_values[1], X, plot_type="bar", show=False)
plt.title("Feature Importance (SHAP)")
plt.savefig('shap_summary.png')

# Detailed Dot Plot
plt.figure()
shap.summary_plot(shap_values[1], X, show=False)
plt.savefig('shap_beeswarm.png')

print("SHAP plots saved as 'shap_summary.png' and 'shap_beeswarm.png'")
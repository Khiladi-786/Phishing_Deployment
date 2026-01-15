import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('dataset_phishing.csv')

# --- SECTION A: DESCRIPTIVE STATISTICS ---
print("--- 1. Summary Statistics (Numerical) ---")
# We transpose (.T) the output to make it easier to read in the terminal
print(df[['length_url', 'nb_dots', 'nb_hyphens', 'ratio_digits_url']].describe().T)

print("\n--- 2. Frequency Distribution (Categorical) ---")
# The main categorical column is 'status'
print(df['status'].value_counts())
print("\nMode of Status:", df['status'].mode()[0])

# --- SECTION B: VISUAL ANALYSIS ---
# IMPORTANT: We only use a subset of columns to prevent crashing
selected_features = ['length_url', 'nb_dots', 'nb_hyphens', 'ratio_digits_url']

# 1. Histograms (Distribution Analysis)
plt.figure(figsize=(12, 5))
for i, col in enumerate(['length_url', 'nb_dots']):
    plt.subplot(1, 2, i+1)
    sns.histplot(df, x=col, hue='status', element="step", stat="density", common_norm=False)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# 2. Pair Plot (Relationships)
# We add 'status' to the list so we can color-code the points
print("Generating Pair Plot... (This might take 10 seconds)")
sns.pairplot(df[selected_features + ['status']], hue='status', palette='husl')
plt.show()

# 3. Heatmap (Correlation)
plt.figure(figsize=(8, 6))
# Calculate correlation only on the selected numerical columns
corr = df[selected_features].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Key Features')
plt.show()

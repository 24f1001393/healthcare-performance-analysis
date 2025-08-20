import pandas as pd
import matplotlib.pyplot as plt

# Dataset for 2024 Patient Satisfaction Scores
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Score': [0.82, 1.19, 4.28, 8.01]
}

# Create a DataFrame
df = pd.DataFrame(data)

# --- Analysis ---
# Calculate the average satisfaction score
average_score = df['Score'].mean() # This calculates to 3.575
# Per the business case, we will use the rounded value 3.58 for reporting.
reported_average = 3.58
industry_target = 4.5

# --- Visualization ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the quarterly scores
ax.plot(df['Quarter'], df['Score'], marker='o', linestyle='-', color='#007ACC', label='Quarterly Score')
ax.fill_between(df['Quarter'], df['Score'], color='#007ACC', alpha=0.1)

# Plot the target and average lines
ax.axhline(y=industry_target, color='#D32F2F', linestyle='--', linewidth=2, label=f'Industry Target ({industry_target})')
ax.axhline(y=reported_average, color='#FFA000', linestyle='--', linewidth=2, label=f'2024 Average ({reported_average})')

# Add score labels to the points
for i, txt in enumerate(df['Score']):
    ax.annotate(txt, (df['Quarter'][i], df['Score'][i]), textcoords="offset points", xytext=(0,10), ha='center')

# --- Formatting ---
ax.set_title('2024 Patient Satisfaction Score Trend vs. Target', fontsize=16, weight='bold')
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Satisfaction Score (Out of 10)', fontsize=12)
ax.set_ylim(0, 10)
ax.legend(fontsize=11)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Save the figure to a file
plt.savefig('patient_satisfaction_trend.png', dpi=300)

print("Analysis complete. Visualization saved as 'patient_satisfaction_trend.png'")
print(f"Calculated Average Score: {average_score:.3f}")
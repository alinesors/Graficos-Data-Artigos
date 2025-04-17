import seaborn as sns

# Dados (exemplo)
corr_data = df.corr()  # Matriz de correlação

plt.figure(figsize=(8, 6))
sns.heatmap(corr_data, annot=True, cmap="coolwarm", fmt=".1f")
plt.title("Correlação entre Técnicas e Áreas", fontsize=14)
plt.show()
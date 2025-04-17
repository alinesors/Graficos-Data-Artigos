import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios baseados na planilha (ajuste conforme seus dados reais)
data = {
    "Área Aplicada": ["Detecção de e-mails", "Detecção de websites", "Sites miméticos", "IA contra phishing"],
    "NLP": [3, 1, 0, 1],  # Quantidade de estudos que usam NLP
    "Deep Learning": [1, 2, 1, 0],  # Quantidade que usam DL
    "Machine Learning": [0, 1, 0, 1]  # Quantidade que usam ML
}

df = pd.DataFrame(data)
df.set_index("Área Aplicada", inplace=True)

# Plot
df.plot(kind="bar", stacked=True, figsize=(10, 6), color=["#4C72B0", "#DD8452", "#55A868"])
plt.title("Técnicas Usadas por Área Aplicada", fontsize=14)
plt.xlabel("Área Aplicada")
plt.ylabel("Número de Estudos")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Técnica")
plt.tight_layout()
plt.show()
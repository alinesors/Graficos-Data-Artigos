import matplotlib.pyplot as plt

# Dados
areas = [
    "Detecção de e-mails", 
    "Detecção de websites", 
    "Sites miméticos", 
    "IA contra phishing",
    "Análise linguística"
]
quantidade = [3, 2, 1, 1, 1]

# Configurar o gráfico
plt.figure(figsize=(10, 5))  # Tamanho da figura
plt.bar(areas, quantidade, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

# Personalizar
plt.title("Frequência de Áreas Aplicadas em Estudos sobre Phishing", fontsize=14)
plt.xlabel("Área Aplicada", fontsize=12)
plt.ylabel("Número de Estudos", fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo X
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Linhas de grade horizontais

# Mostrar o gráfico
plt.tight_layout()  # Ajusta layout para evitar cortes
plt.show()
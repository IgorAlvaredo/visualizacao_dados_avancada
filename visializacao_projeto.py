import plotly.express as px
import pandas as pd

df = pd.read_csv('../dados/clientes-v3-preparado.csv')

# Mapa de calor interativo de correlações
df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()
fig = px.imshow(df_corr, text_auto=True, aspect="auto", color_continuous_scale="Viridis", title="Mapa de Calor de Correlação")

# Área Plot do salário ao longo da idade
fig = px.area(df, x='idade', y='salario', line_group='estado_civil', color='estado_civil', title="Evolução do Salário por Idade e Estado Civil")
fig.show()

# Visualização dos Resultados dos Modelos de Classificação e Regressão

# Gráficos para a classificação

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Matriz de confusão para Regressão Logística
cm_lr = confusion_matrix(Y_test, Y_prev_lr)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Matriz de Confusão: Regressão Logística')
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.show()

# Matriz de confusão para Árvore de Decisão
cm_dt = confusion_matrix(Y_test, Y_prev_dt)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title('Matriz de Confusão: Árvore de Decisão')
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.show()



# Gráfico para a Regressão Linear

import matplotlib.pyplot as plt

# Plot de regressão
plt.figure(figsize=(10, 6))
plt.scatter(Y_test, Y_prev, alpha=0.5)
plt.plot([Y_test.min(), Y_prev.max()], [Y_test.min(), Y_test.max()], 'k--', lw=4)
plt.title('Valores Reais vs. Predições: Regressão Linear')
plt.xlabel('Real')
plt.ylabel('Previsto')
plt.show()


# Visualização de Correlação
import seaborn as sns
import matplotlib.pyplot as plt

# Heatmap de correlação de Pearson
plt.figure(figsize=(10, 6))
sns.heatmap(pearson_corr, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title('Correlação de Pearson entre Variáveis')
plt.show()

# Heatmap de correlação de Spearman
plt.figure(figsize=(10, 6))
sns.heatmap(spearman_corr, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title('Correlação de Pearson entre Variáveis')
plt.show()



import plotly.express as px

# Visualização interativa usando Plotly para a correlação de Pearson
fig = px.imshow(pearson_corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu', title="Correlação de Pearson Interativa")
fig.show()

# Visualização interativa usando Plotly para a correlação de Spearman
fig = px.imshow(spearman_corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu', title="Correlação de Spearman Interativa")
fig.show()
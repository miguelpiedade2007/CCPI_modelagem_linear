import pandas as pd
import numpy as np

# Configuração para reprodutibilidade
np.random.seed(42)

# 1. GERAÇÃO DA BASE (120 linhas e 16 colunas)
n_registros = 120

nomes_base = ["Jose", "Maria", "Carlos", "Eduarda", "Joao", "Ana", "Luiz", "Fabio", "Letícia", "Ricardo"]
sobrenomes = ["Almeida", "Teixeira", "Martins", "Nunes", "Rocha", "Silva", "Barbosa", "Cardoso", "Mendes"]
tipos_sanguineos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

data = {
    'ID_Paciente': range(1, n_registros + 1),
    'Nome_Completo': [f"{np.random.choice(nomes_base)} {np.random.choice(sobrenomes)}" for _ in range(n_registros)],
    'Genero': np.random.choice(['Masculino', 'Feminino'], n_registros),
    'Tipo_Sanguineo': np.random.choice(tipos_sanguineos, n_registros), # Trocado aqui!
    'Idade': np.random.randint(18, 85, n_registros),
    'Altura_m': np.random.uniform(1.50, 1.95, n_registros).round(2),
    'Peso_kg': np.random.uniform(50, 110, n_registros).round(1),
    'Glicose_mgdL': np.random.randint(70, 140, n_registros),
    'Frequencia_Cardiaca_BPM': np.random.randint(60, 100, n_registros),
    'Horas_Exercicio_Semana': np.random.randint(0, 15, n_registros),
    'Consumo_Agua_L': np.random.uniform(1.0, 4.0, n_registros).round(1),
    'Qualidade_Sono_1a10': np.random.randint(1, 11, n_registros),
    'Setor': np.random.choice(['Geral', 'Cardio', 'Endo'], n_registros),
    'Consultas_Ano': np.random.randint(1, 12, n_registros),
    'Historico_Familiar': np.random.choice(['Sim', 'Não'], n_registros)
}

df = pd.DataFrame(data)

# 2. CÁLCULO DE COERÊNCIA (A 16ª coluna)
df['IMC'] = (df['Peso_kg'] / (df['Altura_m']**2)).round(2)

# 3. VALIDAÇÃO E EXIBIÇÃO NO TERMINAL (Ideal para prints dos slides)
print("\n" + "="*40)
print("    ---RELATÓRIO DE VALIDAÇÃO---      ")
print("="*40)
print(f"Total de Linhas: {df.shape[0]}")
print(f"Total de Colunas: {df.shape[1]}")
print(f"Valores Nulos: {df.isnull().sum().sum()}")
print("-"*40)
print("AMOSTRA DOS DADOS (Primeiras 5 linhas):")
print(df[['Nome_Completo', 'Tipo_Sanguineo', 'Idade', 'IMC']].head())
print("="*40)

# 4. EXPORTAÇÃO
df.to_excel("Checkpoint2_Saude_Final.xlsx", index=False)
print("\nArquivo 'Checkpoint2_Saude_Final.xlsx' gerado com sucesso!")
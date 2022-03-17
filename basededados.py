import pandas as pd 
import plotly.express as px


dados = pd.read_csv(r"F:\Automação\telecom_users.csv")
dados = dados.drop(["Unnamed: 0"], axis=1)
dados["TotalGasto"] = pd.to_numeric(dados["TotalGasto"], errors="coerce")
dados = dados.dropna(how="all", axis=1)
dados = dados.dropna(how="any", axis=0)

for coluna in dados.columns:
    
    grafico = px.histogram(dados, x=coluna, color="Churn")
    
    grafico.show()

print(dados["Churn"].value_counts())
print(dados["Churn"].value_counts(normalize=True).map("{:.1%}".format))
print(dados)
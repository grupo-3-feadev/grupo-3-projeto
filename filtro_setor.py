import yfinance as yf
import pandas as pd
import tabulate as tb

# Em "papeis_solidos" teremos o código das ações e em "dados_coletados" o setor destas ações 

# Ações para teste do código: ["ITUB4", "VALE3", "WEGE3", "PETR4"]

papeis_solidos = ["ITUB4", "VALE3", "WEGE3", "PETR4"] # <---- aqui é onde será feito o input das ações
dados_coletados = []

# Aqui teremos um loop onde usaremos o código da ação para encontrar o setor da empresa através da biblioteca "yfinance"

for i in range(0,len(papeis_solidos)):
    acao = papeis_solidos[i] + ".SA"
    info = yf.Ticker(acao).info
    setor = info.get("sector")
    nome = info.get("longName")

    dado_atual = {
            "Nome": nome,
            "Papel": papeis_solidos[i],
            "Setor": setor
        }

    dados_coletados.append(dado_atual)

# Agora, usando a biblioteca "pandas" iremos filtrar a tabela para que fique apenas as empresas que sejam do nosso setor de interesse

df_tabela = pd.DataFrame(dados_coletados)

setores_alvo = ["Financial Services", "Utilities", "Energy", "Basic Materials"]
filtro_empresas = df_tabela[df_tabela["Setor"].isin(setores_alvo)]


# Usando a biblioteca "tabulate" conseguiremos mostrar a tabela organizada no terminal

tabela_completa = tb.tabulate(df_tabela, headers='keys', tablefmt='fancy_grid', stralign='center')
tabela_filtro = tb.tabulate(filtro_empresas, headers='keys', tablefmt='fancy_grid', stralign='center')


largura_tabela = len(tabela_completa.split('\n')[0])
titulo = "--- Tabela Completa ---"
print("\n" + titulo.center(largura_tabela))
print(tabela_completa)

largura_tabela = len(tabela_filtro.split('\n')[0])
titulo = "--- Tabela Filtrada ---"
print("\n" + titulo.center(largura_tabela))
print(tabela_filtro)
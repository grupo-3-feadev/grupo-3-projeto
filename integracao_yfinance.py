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

# Transformar a coluna de papéis em lista

lista_papeis = [papel + '.SA' for papel in filtro_empresas['Papel']]

dfs = [] # ---> Vai armazenar o df de cada papel

for papel in lista_papeis:
    df = yf.download( # ---> Consulta na lib
        papel,
        period="5y",
        interval="1d",
        progress=False
    )
    if df.empty:
        continue

    # Remove MultiIndex/ linha com o nome do papel, se existir

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Data vira coluna

    df = df.reset_index()

    # Nome do papel vira COLUNA

    df.insert(0, "Papel", papel)
    dfs.append(df)

# Junta todos os dfs em um df único

df_final = pd.concat(dfs, ignore_index=True)

# Remove o horário, mantendo apenas a data (AAAA-MM-DD)

df_final['Date'] = df_final['Date'].dt.date

# Imprime a tabela 

print(tb.tabulate(df_final.head(20), headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')) # ---> O número dentro do argumento da função .head() 
                                                                                                                   # diz quantas linhas da tabela serão mostradas no terminal
# Projeto: Como criar uma carteira previdenciária do zero? (06/12/2025)

## A Ideia
 Usar dados e matemática para montar a carteira de aposentadoria que gere a maior renda possível: **segura, diversificada e focada em dividendos.**

---

## Como Vai Funcionar? 
Vamos criar um funil de 3 etapas que nos permite escolher as melhores ações para se investir:

### 1. O Filtro de Qualidade 
* **O que faz:** Só passam neste filtro empresas que pagam bons dividendos e são sólidas (ex: Bancos, Elétricas, Saneamento).
* **Objetivo:** Garantir que a base da carteira seja sólida.

### 2. A Seleção Inteligente (Machine Learning / Clustering)
* **O que faz:** O algoritmo vai analisar o comportamento das ações e separa elas em "famílias" diferentes.
* **Objetivo:** O algoritmo vai selecionar apenas a **melhor ação** de cada "família".
* **Resultado:** Diversificação das ações permitindo que o investimento não fique alocado todo no mesmo lugar.

### 3. A Matemática Financeira (Finanças Quantitativas)
* **O que faz:** Agora que temos as melhores ações (ex: 10 papéis), quanto dinheiro colocamos em cada uma? 50% em uma? 10% em outra?
* **Objetivo:** Um cálculo de otimização definirá os pesos exatos para ter a carteira com o **menor risco possível** (Mínima Variância) e os **maiores dividendos** .
* **Resultado:** Uma carteira que oscila pouco e gera renda constante.

---

# Atualização do Projeto (14/12/2025)

* Adicionado a "Etapa de Validação" em que será feito testes de risco (+ para cenários extremos), onde veremos como a carteira montada irá se comportar e assim ter um veredito da sua qualidade
* Definir a categorização dos conjuntos para a aplicação do clustering
  
**Arquitetura da Base de Dados:** 
* Usaremos a biblioteca "fundamentus" do python na etapa 1 "Filtro de Qualidade" para analisar os dados da empresa atualmente e filtrar elas pela perenidade e solidez
* Em seguinda usaremos a biblioteca "yfinance" na etapa 2 "A Seleção Inteligente" para analisar como as empresas que passaram no primeiro filtro se comportaram em determinado intervalo de tempo decidido, assim aplicando o método de clustering

# Atualização do Projeto (28/12/2025)

## Versão [1.0.0] dos códigos:

* **Script 1:** Com base em métricas de perenidade de ativos, será aplicado um filtro que seliciona apenas as empresas que tenham valores positivos perante estas métricas, as empresas selecionadas serão colocadas em um DataFrame. **(este código ainda não está finalizado)**

* **Script 2:** Dadas as empresas que passaram pelo filtro de perenidade, será criado um DataFrame e aplicado um outro  filtro para manter apenas empresas de setores específicos, assim podendo manipular a diversidade dos nossos ativos.
  Segue o link para o arquivo .py: [filtro_setor.py](./filtro_setor.py)

* **Script 3:** Com base no DataFrame do script 2, este código usa um mecanismo de busca através da biblioteca yfinance, onde são obtidos os valores das ações das empresas nos últimos 5 anos. Tais dados serão utilizados na aplicação do método de clustering.
  Segue o link para o arquivo .py: [integracao_yfinance.py](./integracao_yfinance.py)

**Obs:** nos códigos usamos algumas empresas de teste para para observar o comportamento do script, se ele estava rodando da forma que imaginávamos.


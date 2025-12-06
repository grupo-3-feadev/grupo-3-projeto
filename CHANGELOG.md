# Ideia 1 do projeto: Como criar uma carteira previdenciária do zero?

## A Ideia
 usar dados e matemática para montar a carteira de aposentadoria que gere a maior renda possível: **segura, diversificada e focada em dividendos.**

---

## Como vai funcionar? 
vamos criar um funil de 3 etapas que nos permite escolher as melhores ações para se investir em 3 etapas:

### 1. O Filtro de Qualidade 
* **O que faz:** Só passam neste filtro empresas que pagam bons dividendos e são sólidas (ex: Bancos, Elétricas, Saneamento).
* **Objetivo:** Garantir que a base da carteira seja sólida.

### 2. A Seleção Inteligente (Machine Learning / Clustering)
* **O que faz:** O algoritmo vai analisar o comportamento das ações e separa elas em "famílias" diferentes.
* **Objetivo:** O vai selecionar apenas a **melhor ação** de cada "família".
* **Resultado:** Diversificação das ações permitindo que o investimento não fique alocado todo no mesmo lugar.

### 3. A Matemática Financeira 
* **O que faz:** Agora que temos as melhores ações (ex: 10 papéis), quanto dinheiro colocamos em cada uma? 50% em uma? 10% em outra?
* **Objetivo:** Um cálculo de otimização define os pesos exatos para ter a carteira com o **menor risco possível** (Mínima Variância).
* **Resultado:** Uma carteira que oscila pouco e gera renda constante.

---


## 🤝 Sugestão de Divisão de Tarefas
* **Dados:** Baixar histórico de preços e filtrar os dividendos (API Yahoo Finance).
* **Clustering (IA):** Criar o código que agrupa as ações parecidas (Scikit-Learn).
* **Otimização:** Fazer a matemática que define as porcentagens ideais da carteira (Scipy).

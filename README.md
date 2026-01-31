# 📊 Carteira Previdenciária Quantitativa

Projeto de construção **automatizada de uma carteira previdenciária**, utilizando **análise fundamentalista, métodos quantitativos e machine learning**, com foco em **dividendos, diversificação e controle de risco** no longo prazo.

---

## 📌 Objetivo
Desenvolver um **pipeline quantitativo replicável** para seleção e alocação de ações da B3, reduzindo vieses subjetivos e priorizando geração de renda recorrente.

---

## ⚙️ Metodologia
- Coleta de dados via web scraping do Fundamentus  
- Filtros de qualidade:
  - Setores perenes  
  - Métricas fundamentalistas (P/L, ROE, EV/EBITDA, Liquidez, Volatilidade)  
- Clusterização com K-Means (k definido pelo Método do Cotovelo)  
- Ranqueamento multivariado dos ativos  
- Seleção por rodízio entre clusters  
- Ponderação composta focada em dividendos (`DY / P/VP`)  
- Limite máximo de **25% por ativo**

---

## 🧠 Tecnologias
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Requests, BeautifulSoup  

---

## 👥 Autores
- Gabriela Saito  
- Lucas Marino  
- Maria Eduarda Alonso  

---

## ⚠️ Aviso
# Projeto com **fins educacionais**.  
# Não constitui recomendação de investimento.


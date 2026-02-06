# real estate budget system
Sistema de orçamento Imobiliário
# 🏠 Sistema de Orçamento Imobiliário

Projeto desenvolvido para a disciplina **Algoritmic Think e Introdução à Programação Orientada a Objetos** – UNIFecaf.

## 📌 Objetivo
Automatizar o cálculo de orçamentos de aluguel de imóveis (apartamento, casa e estúdio), considerando características adicionais como número de quartos, garagem, vagas de estacionamento e presença de crianças.  
O sistema gera um **arquivo CSV** com as 12 parcelas mensais do contrato.

---

## ⚙️ Funcionalidades
- Menu interativo para escolha do tipo de imóvel.
- Cálculo automático do valor do aluguel com base em regras:
  - Apartamento: base R$ 700 (+200 se 2 quartos, +300 garagem, -5% se não tiver crianças).
  - Casa: base R$ 900 (+250 se 2 quartos, +300 garagem).
  - Estúdio: base R$ 1200 (+250 até 2 vagas, +60 por vaga adicional).
- Inclusão da parcela do contrato imobiliário (R$ 2000 ÷ 5 = R$ 400).
- Exibição do orçamento no console.
- Geração de arquivo `Orcamento.csv` com 12 parcelas mensais.

---

## 🗂️ Estrutura do Projeto

---

## 🚀 Como executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/Imobiliaria_app.git
cd Imobiliaria_app
python src/main.py

######## R.M IMOBILIÁRIA - LTDA ########
Escolha o Tipo de Imóvel:
1 - Apartamento
2 - Casa
3 - Estúdio
0 - Sair

👨‍💻 Autor
Francisco José Dos Santos
Curso de Análise e Desenvolvimento de Sistemas – UNIFecaf

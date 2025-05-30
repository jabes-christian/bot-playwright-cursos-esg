# 🌿 Bot Playwright para Cursos Gratuitos de ESG com Certificado 🎓

Este projeto é um **bot de automação** desenvolvido com **Python**, **Playwright** e integração com **Google Sheets**. Ele busca cursos gratuitos e com certificado sobre ESG (Environmental, Social, and Governance) na web, coleta os resultados no formato de planilha e atualiza automaticamente em uma planilha do Google Sheets.

## 🚀 Funcionalidades

✅ Acessa o **Google Gemini** para buscar cursos ESG  
✅ Formata a resposta em formato de tabela compatível com Google Sheets  
✅ Atualiza automaticamente uma planilha no Google Sheets com os resultados  
✅ Utiliza **credenciais seguras** via `credentials.json`  
✅ Automação **headless** (ou não, se preferir visualizar o navegador)  
✅ Código simples e adaptável para outras pesquisas  

---

## 🔧 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Playwright](https://playwright.dev/python/)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [gspread](https://gspread.readthedocs.io/en/latest/)

---

## 📋 Pré-requisitos

1. **Clonar o repositório:**

```bash
git clone https://github.com/jabes-christian/bot-playwright-cursos-esg.git
cd bot-playwright-cursos-esg
```

2. **Criar e ativar o ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. **Instalar as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configurar as credenciais do Google Sheets:**

- Baixe o credentials.json da conta de serviço no Google Cloud e coloque na raiz do projeto.

---

## 📊 Como Usar

1. **Abra o terminal e execute:**

```bash
python main.py
```

2. **O bot irá:**

- Abrir o navegador, acessar o Gemini e buscar cursos de ESG
- Capturar e formatar a resposta
- Atualizar sua planilha no Google Sheets com os dados

---

## 🛡️ Observações de Segurança

🔒 Lembre-se de NÃO fazer commit do seu credentials.json no repositório.
Seu arquivo **.gitignore** já está configurado para evitar isso.

---

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.
Se quiser sugerir novas funcionalidades ou melhorar o código, é só avisar!

---

## 🧑‍💻 Autor
Feito com 💙 por Jabes Christian
📬 LinkedIn | GitHub

---

## 📜 Licença
Este projeto está licenciado sob a MIT License.

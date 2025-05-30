from playwright.sync_api import sync_playwright
import time
import csv
import io
import gspread
from google.oauth2.service_account import Credentials

# Configurações da API Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'
# (sem o /edit... no final)
SPREADSHEET_ID = '1DV0vmiVowp3tBW5B_St0HctNTs0B5XljdYUtIanosrk'
SHEET_NAME = 'Página1'  # Nome da aba

# Configuração do acesso ao Google Sheets
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(creds)
sheet = gc.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# Pergunta para o Gemini
PERGUNTA = """quero cursos gratuitos com certificados atuais sobre ESG com links para os cursos, quero a lista desses cursos fornecidos para estar copiando no formato compatível do Google Sheets."""

with sync_playwright() as p:
    # headless=False para visualizar o navegador
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Passo 1: Acessar o ChatGPT
    page.goto("https://gemini.google.com/app")
    time.sleep(3)

    # Passo 2: Enviar a pergunta
    page.fill('xpath=//*[@id="app-root"]/main/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div[2]/div/div[2]/chat-window/div/input-container/div/input-area-v2/div/div/div[2]/div/div/rich-textarea/div[1]', PERGUNTA)
    page.locator('xpath=//*[@id="app-root"]/main/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div[2]/div/div[2]/chat-window/div/input-container/div/input-area-v2/div/div/div[4]/div/div[2]/button').click()

    print("Aguardando resposta...")
    time.sleep(5)

    # Passo 3: Rolar para o centro da página
    page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(2)

    # Capturar a resposta
    try:
        elemento_resposta = page.locator(
            'response-element code-block pre code').first
        conteudo = elemento_resposta.text_content(timeout=10000)
        print("Conteúdo capturado com sucesso:")
        print(conteudo)
    except Exception as e:
        print(f"Erro ao pegar o conteúdo: {e}")
        browser.close()
        exit()

    # Passo 4: Processar o CSV para lista de listas
    conteudo_csv = list(csv.reader(io.StringIO(conteudo)))

    # Passo 5: Inserir os dados na planilha
    sheet.update('A1', conteudo_csv)
    print("Dados inseridos com sucesso na planilha!")

    # Opcional: Espera para visualização antes de fechar o navegador
    page.wait_for_timeout(5000)
    browser.close()

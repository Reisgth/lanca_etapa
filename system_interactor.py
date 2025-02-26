from playwright.sync_api import sync_playwright

def handle_alert(dialog):
    dialog.accept()

def login(page, user, password):
    page.goto("https://sippes.eb.mil.br/jsp/login/formLogin.jsp")
    page.fill("#campo_username", user)
    page.fill("#campo_password", password)
    page.click("#botao")
    page.wait_for_load_state("networkidle", timeout=30000)

def new_entry(page):
    page.click("#link-menu-item15")
    page.wait_for_timeout(1000)
    page.click("#link-submenu-item15-2")
    page.wait_for_timeout(1000)
    page.click("a[href='/manterLancamentos.do?metodo=exibirTelaConsultaLancamentosIndividuais&limparSessao=true']")
    page.wait_for_timeout(1000)
    page.click("[name='btnNovo']")
    page.wait_for_timeout(1000)

def document_entry(page, doc_date, doc_number):
    page.select_option("select[name='codigoTipoDocumento']", "12")
    page.wait_for_timeout(1000)
    page.fill("#dataDocumento", doc_date)
    page.wait_for_timeout(1000)
    page.fill("[name='numeroDocumento']", doc_number)
    page.wait_for_timeout(1000)
    page.fill("#codomDocumento", "001453")
    page.wait_for_timeout(1000)
    page.click("#siglaOM")
    page.wait_for_timeout(1000)
    page.select_option("select[name='codigoEmissorDocumento']", "1")

def initialize_entry(page, precp, entry_type, entry_quantity):
    page.on("dialog", handle_alert)

    page.click("a[href='javascript:pesquisarFavorecido()']")
    page.wait_for_timeout(1000)
    page.fill("#precCpFiltroFav", precp) 
    page.click("[name='btnPesquisar']")  # Pesquisar
    page.wait_for_timeout(1000)
    
    # Clicar no Usuário selecionado
    page.click(".impar_rel td a")
    page.wait_for_timeout(1000)

    # Dados do lançamento
    page.fill("[name='codigoRubricaLancamento']", entry_type)
    page.wait_for_timeout(1000)
    page.click("#descricaoRubricaLancamento")
    page.wait_for_timeout(1000)
    page.select_option("select[name='codigoFormaPagamento']", "M")
    page.wait_for_timeout(1000)

    # Parâmetros
    page.select_option("#PR_L_2543", "2025")
    page.wait_for_timeout(1000)
    
    if entry_type == "NR0053":
        page.type("#PR_I_1407", entry_quantity)
        page.wait_for_timeout(1000)
        page.select_option("#PR_L_5144", "10861")
        page.wait_for_timeout(1000)
    else:
        page.type("#PR_I_2863", entry_quantity)
        page.wait_for_timeout(1000)
        page.select_option("#PR_L_5148", "10880")
        page.wait_for_timeout(1000)
        
    page.click("[name='btnSalvar']")
    page.wait_for_timeout(1000)
    
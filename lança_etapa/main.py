from playwright.sync_api import sync_playwright
from system_interactor import login, new_entry, document_entry, initialize_entry
from data_tables import extract_data, columns_name 
from info_screen import InfoScreen
from drop_archive import get_file_path

import tkinter as tk
from tkinter import ttk

def showTables():
    # Exibir os dados extraídos usando os nomes das colunas
    print("\n🔹 Oficiais:")
    for linha in oficiais:
        print(linha['ord'],linha['pg_name'],linha['preccp'],linha['entry_type'],linha['days'], linha['entry_quantity'])

    print("\n🔹 ST e Sgt:")
    for linha in st_sgt:
        print(linha['ord'],linha['pg_name'],linha['preccp'],linha['entry_type'],linha['days'], linha['entry_quantity'])
        
    print("\n🔹 Cb e Sd:")
    for linha in cb_sd:
        print(linha['ord'],linha['pg_name'],linha['preccp'],linha['entry_type'],linha['days'], linha['entry_quantity'])

    print("\n🔹 Of e Praças PTTC:")
    for linha in oficiais_pracas_pttc:
        print(linha['ord'],linha['pg_name'],linha['preccp'],linha['entry_type'],linha['days'], linha['entry_quantity'])
        
def verify_entry_type(verify_entry):
    
    if verify_entry == 'A': 
        entry_type = "NR0052"
        
    elif verify_entry == 'B':
        entry_type = "NR0053"
        
    elif verify_entry == 'C':
        entry_type = 'NR0058'
        
    return entry_type

path_to_archive = get_file_path()

oficiais, st_sgt, cb_sd, oficiais_pracas_pttc = extract_data(path_to_archive)

oficiais = columns_name(oficiais)
st_sgt = columns_name(st_sgt)
cb_sd = columns_name(cb_sd)
oficiais_pracas_pttc = columns_name(oficiais_pracas_pttc)

user = ""
password = ""
doc_value = ""
doc_date = ""
doc_number = ""

showTables()

def handle_info(data):
    global user, password, doc_value, doc_date, doc_number
    
    user = data["user"]
    password = data["password"]
    doc_date = data["doc_date"]
    doc_number = data["doc_number"]

root = tk.Tk()
app = InfoScreen(root, handle_info)
root.mainloop()

print(f"{user} {password} {doc_date} {doc_number}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    try: 
        
        login(page, user, password) # Faz Login no sistema
        new_entry(page) # Inicia um novo lançamento
        document_entry(page, doc_date, doc_number) # Iserção do das informações do BAR que gerou os lançamentos
        
        # Lançamentos para ST e Sgt
        for linha in st_sgt:
            preccp = linha['preccp']
            quantity = linha['entry_quantity']
            entry_type = verify_entry_type(linha['entry_type'])
                
            initialize_entry(page, preccp, entry_type, quantity)
            
        # Lançamentos para Cb e Sd
        for linha in cb_sd:
            preccp = linha['preccp']
            quantity = linha['entry_quantity']
            entry_type = verify_entry_type(linha['entry_type'])
                
            initialize_entry(page, preccp, entry_type, quantity)
    except Exception as e:
        print(f"Erro: {e}")
        page.wait_for_timeout(5000)

    browser.close()
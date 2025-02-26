from docx import Document

def extract_data(arquivo_docx):
    """
    Extrai e filtra as tabelas de um documento Word (.docx), removendo linhas onde a coluna 5 contém "0".
    
    Parâmetros:
    - arquivo_docx (str): Caminho do arquivo .docx

    Retorno:
    - tuple: (oficiais, st_sgt, cb_sd, oficiais_pracas_pttc) - Listas contendo os dados de cada tabela filtrada.
    """

    doc = Document(arquivo_docx)

    oficiais = []
    st_sgt = []
    cb_sd = []
    oficiais_pracas_pttc = []

    tables = [filter_table([[celula.text.strip() for celula in linha.cells] for linha in table.rows]) 
               for table in doc.tables]
    
    for i, table in enumerate(tables):
        if i == 0:
            oficiais = table
        elif i == 1:
            st_sgt = table
        elif i == 2:
            cb_sd = table
        else:
            oficiais_pracas_pttc = table

    return oficiais, st_sgt, cb_sd, oficiais_pracas_pttc

def filter_table(tabela):
        return [linha for linha in tabela if len(linha) > 5 and linha[5] != "0"]
    
def columns_name(tabela):
    """
    Converte cada linha da tabela em um dicionário para fácil compreensão.
    """
    nomeadas = []
    for linha in tabela:
        linha_nomeada = {
            "ord": linha[0],
            "pg_name": linha[1],
            "preccp": linha[2],
            "entry_type": linha[3],
            "days": linha[4],
            "entry_quantity": linha[5],
        }
        nomeadas.append(linha_nomeada)
    return nomeadas
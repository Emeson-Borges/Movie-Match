import pandas as pd

def extract_data():
    url = 'https://en.wikipedia.org/wiki/List_of_American_films_of_2018'
    tables = pd.read_html(url)
    
    if tables:
        # Iterar sobre as tabelas para encontrar a que contém as colunas desejadas
        for df in tables:
            # Verificar se as colunas 'Title' e 'Distributor' estão presentes
            if 'Title' in df.columns and 'Distributor' in df.columns:
                # Selecionar apenas as colunas desejadas
                df = df[['Title', 'Distributor']]
                return df
        
        # Se nenhum DataFrame contiver as colunas desejadas, levantar uma exceção
        raise ValueError("Colunas necessárias não encontradas em nenhuma tabela.")
    else:
        raise ValueError("Nenhuma tabela encontrada na página.")
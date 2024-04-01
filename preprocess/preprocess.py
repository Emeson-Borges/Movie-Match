from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def preprocess_data(data):
    # Verificar se os dados fornecidos não estão vazios
    if data is None or data.empty:
        raise ValueError("Os dados fornecidos estão vazios.")
    
    # Verificar se os dados fornecidos contêm as colunas necessárias
    if 'Title' not in data.columns or 'Distributor' not in data.columns:
        raise ValueError("Os dados fornecidos não contêm as colunas necessárias.")
    
    # Concatenar informações relevantes para vetorização
    concatenated_info = data['Title'] + " " + data['Distributor']
    
    # Verificar se há valores nulos ou vazios após a concatenação
    if concatenated_info.isnull().any() or concatenated_info.empty:
        raise ValueError("Os dados fornecidos contêm valores nulos ou vazios após a concatenação.")
    
    # Vetorizar os títulos dos filmes e distribuidores
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(concatenated_info)
    
    return X, vectorizer

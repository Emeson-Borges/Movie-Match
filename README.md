# Movie Match

Este é um aplicativo da web desenvolvido com Streamlit que ajuda os usuários a encontrar recomendações de filmes com base em suas seleções. As recomendações são geradas usando um modelo de machine learning treinado com dados de filmes.

## Instruções:

1. Instale as dependências necessárias usando `pip install -r requirements.txt`.
2. Execute o aplicativo usando `streamlit run app.py`.
3. Selecione um filme no menu suspenso.
4. Veja os filmes recomendados com base na sua seleção.

## Como usar:

- O aplicativo permite que você escolha um filme da lista disponível.
- Após a seleção do filme, o aplicativo calculará e exibirá uma lista de filmes recomendados com base na entrada do usuário.
- Os filmes recomendados são classificados de acordo com a porcentagem de recomendação, com os filmes mais relevantes no topo da lista.


## Arquivos e Diretórios:

- `app.py`: Contém o código principal do aplicativo Streamlit.
- `preprocess/`: Diretório contendo os scripts para pré-processamento de dados.
- `models/`: Diretório contendo os scripts para construção e treinamento do modelo de machine learning.
- `api/`: Diretório contendo o script para extração de dados da API.
- `requirements.txt`: Arquivo de texto contendo todas as dependências do projeto.

## Dependências:

- Streamlit
- Pandas

## Licença:

@emeson-borges

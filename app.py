import streamlit as st
import pandas as pd
from preprocess.preprocess import preprocess_data
from models.models import build_model
from api.api import extract_data

def main():
    st.header('Movie Match')
    # Extrair lista de filmes da API
    movie_list = extract_data()
    
    if movie_list is not None:
        # Permitir que o usuário escolha um filme da lista
        selected_movie = st.selectbox('Escolha um filme:', movie_list['Title'])

        # Pré-processar os dados
        X, vectorizer = preprocess_data(movie_list)

        # Construir e treinar o modelo
        model = build_model(X)

        # Transformar todos os filmes em vetores
        movie_vectors = X

        # Transformar a entrada do usuário em um vetor
        selected_movie_index = movie_list.index[movie_list['Title'] == selected_movie][0]
        selected_movie_vectorized = movie_vectors[selected_movie_index]

        # Obter recomendações com base na entrada do usuário
        distances, indices = model.kneighbors(selected_movie_vectorized)

        # Armazenar os índices dos filmes recomendados
        recommended_movies = list(indices.flatten())

        # Calcular a porcentagem da recomendação (distância) para todos os filmes
        max_distance = distances.max()
        recommendation_percentages = ((max_distance - distances.flatten()) / max_distance) * 100

        # Formatando a porcentagem como string com o símbolo "%"
        recommendation_percentages = [f"{percent:.2f}%" for percent in recommendation_percentages]

        # Criar DataFrame com os resultados
        recommendations_df = pd.DataFrame({
            'Filme': movie_list['Title'].iloc[recommended_movies],
            'Distributor': movie_list['Distributor'].iloc[recommended_movies],
            'Porcentagem de Recomendação': recommendation_percentages
        })

        # Ordenar os resultados pela porcentagem de recomendação
        recommendations_df = recommendations_df.sort_values(by='Porcentagem de Recomendação', ascending=False)

        # Destacar o filme mais recomendado em verde no topo da tabela
        recommendations_df_style = recommendations_df.style.apply(lambda x: ['background: lightgreen' if x.name == recommendations_df.index[0] else '' for i in x], axis=1)

        # Exibir recomendações em forma de tabela
        st.title('Recomendações de Filmes')
        st.write("Filme de entrada:", selected_movie)
        st.write("Recomendações:")
        st.table(recommendations_df_style)

if __name__ == "__main__":
    main()

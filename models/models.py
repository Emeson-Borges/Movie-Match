from sklearn.neighbors import NearestNeighbors


def build_model(X):
    # Construir e treinar o modelo NearestNeighbors
    model = NearestNeighbors(n_neighbors=5, algorithm='brute')
    model.fit(X)
    return model

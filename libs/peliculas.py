class Pelicula:

    """la clase pelicula cuenta con un metodo inicial para recibir por
        parametros cada atributo de una pelicula"""

    def __init__(self, genero, titulo, actor):
        self.genero = genero
        self.titulo = titulo
        self.protagonista = actor

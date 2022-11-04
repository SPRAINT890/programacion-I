from exceptions.ContenidosYaExiste import ContenidoYaExiste
from exceptions.ContenidoNoExiste import ContenidoNoExiste


from entities.Pelicula import Pelicula
from entities.Serie import Serie
from entities.Episodio import Episodio
from entities.Contenido import Contenido
from entities.Usuario import Usuario


class PortalContenido:
    def __init__(self) -> None:
        self._usuarios = []
        self._contenidos = []

    @property
    def usuarios(self):
        return self._usuarios

    @usuarios.setter
    def usuarios(self, usuarios):
        self._usuarios = usuarios

    @property
    def contenidos(self):
        return self._contenidos

    @contenidos.setter
    def contenidos(self, contenidos):
        self._contenidos = contenidos

    def crear_pelicula(self, nombre, generos, anio):
        for contenido in self._contenidos:
            if contenido.nombre == nombre:
                try:
                    raise ContenidoYaExiste("Esta Pelicula ya existe")
                except Exception as error :
                    print(error)
        self._contenidos.append(Pelicula(nombre, generos, anio))

    def crear_serie(self, nombre, generos):
        for contenido in self._contenidos:
            if contenido.nombre == nombre:
                try:
                    raise ContenidoYaExiste("Esta Serie ya existe")
                except Exception as error :
                    print(error)
        self._contenidos.append(Serie(nombre, generos))

    def agregar_episodio_serie(self, nombre_serie, numero_temporada, numero_episodio, nombre_episodio):

        existe_serie = False
        for serie in self._contenidos:
            if nombre_serie == serie.nombre:
                if serie.episodios is None:
                    serie.episodios.append(Episodio(numero_temporada, numero_episodio, nombre_episodio))
                    existe_serie = True
                else:
                    for episodio in serie.episodios:
                        if episodio.nombre == nombre_episodio:
                            try:
                                raise ContenidoYaExiste("Este episodio ya existe")
                            except Exception as error :
                                print(error)
                    serie.episodios.append(Episodio(numero_temporada, numero_episodio, nombre_episodio))
                    existe_serie = True

        if not existe_serie:
            try:
                raise ContenidoNoExiste("Esta serie no existe")
            except Exception as error :
                print(error)
        
    def visualizar_contenido(self, email_usuario, nombre_contenido):
        existe_usuario = False
        existe_contenido = False
        
        for contenido in self._contenidos:
            if nombre_contenido == contenido.nombre:
                contenido_visto = contenido
                existe_contenido = True
        if not existe_contenido:
            try:
                raise ContenidoNoExiste("Esta serie o Pelicula no esta registrado")
            except Exception as error :
                print(error)
        
        
        for usuario in self._usuarios:
            if usuario.mail == email_usuario:
                usuario.contenido_visto.append(contenido_visto)
                existe_usuario = True
        
        if not existe_usuario:
            self._usuarios.append(Usuario(email_usuario, contenido_visto))
    
    def recomendar_contenido(self, email_usuario):
        pass


if __name__ == '__main__':
    netflix = PortalContenido()
    # Primera Funcion
    # netflix.crear_pelicula("Matrix", ["Ciencia Ficcion", "+18", "Drogas"], 1999)
    # netflix.crear_pelicula("Matrix", ["Ciencia Ficcion", "romance"], 2022)
    netflix.crear_pelicula("Matrix", None, 2022)

    # Segunda Funcion
    netflix.crear_serie("Better Call Saul", ["Abogados", "Pollo Frito"])
    # Netflix.crear_serie("Better Call Saul", ["Abogados", "Walter Withe"])
    # Netflix.crear_serie("Better Call Saul", None)

    # tercera Funcion
    netflix.agregar_episodio_serie("Better Call Saul", 1, 1, "el inicio")
    netflix.agregar_episodio_serie("Better Call Saul", 1, 2, "el diabolo")
    # netflix.agregar_episodio_serie("Better Call Saul", 1, 3, "el diabolo")
    # netflix.agregar_episodio_serie("The Boys", 1, 3, "el diabolo")
    # netflix.agregar_episodio_serie("Better Call Saul", None, 3, "Armagedon")
    
    # cuarta Funcion
    netflix.visualizar_contenido("gasparmorales1@gmail.com", "Better Call Saul")
    netflix.visualizar_contenido("gasparmorales1@gmail.com", "Matrix")
    # netflix.visualizar_contenido("gasparmorales1@gmail.com", "el señor de los anillos")
    
    # quinta Funcion
    print("hola")

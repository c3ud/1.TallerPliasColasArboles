from libs.Peliculas import Pelicula
from libs.pila import Pila

def main():
    """Creo un objeto de nombre apila de tipo Pila()"""
    apila = Pila()
    """Para evaluar la continuidad del proceso de
    busqueda se crea el atributo booleano continuar"""
    continuar = True

    while continuar:
        #El elemento a buscar se introduce por el usuario.
        nombre = raw_input("Ingrese (Actor, Genero o Titulo de pelicula): ")

        """Cada pelicula cuenta con un genero un titulo y un actor"""

        pelicula0 = Pelicula("Accion","Romeo debe morir", "Jet Li")
        pelicula1 = Pelicula("Accion","The transporter", "jason statham")
        pelicula2 = Pelicula("Terror","El Aro", "Naomi Watts")
        pelicula4 = Pelicula("Accion","El beso del dragon", "Jet Li")
        pelicula3 = Pelicula("Humor","Locos de ira", "Adam Sandler")
        pelicula5 = Pelicula("Humor","Dos tontos muy tontos", "Jim Carrey")
        pelicula6 = Pelicula("Terror","Saw", "Tobin Bell")

        #Agrega cada pelicula
        apila.apilar(pelicula0)
        apila.apilar(pelicula1)
        apila.apilar(pelicula2)
        apila.apilar(pelicula3)
        apila.apilar(pelicula4)
        apila.apilar(pelicula5)
        apila.apilar(pelicula6)


        while apila.es_vacia == False:
            #Regresa cada elemento de la pila.
            pelicula = apila.desapilar()

            """Se evalua el elemento a buscar y dependiendo del atrubuto
                pelicula existente se regresa la informacion deseada"""

            if pelicula.genero == nombre:
                print("Titulo pelicula: " + pelicula.titulo +"\n Protagonista: "+ pelicula.protagonista)

            elif pelicula.titulo == nombre:
                print "La protagoniza: " + pelicula.protagonista +"\n pertenece al genero de: "+ pelicula.genero

            elif pelicula.protagonista == nombre:
                print "Titulo pelicula: " + pelicula.titulo +"\n pertenece al genero de:: "+ pelicula.genero


        continuar = ("s" == raw_input("Desea continuar? s/n").lower())


main()

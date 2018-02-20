def main():
    """Creo un objeto de nombre apila de tipo Pila()"""
    apila = Pila()
    """Para evaluar la continuidad del proceso de
    busqueda se crea el atributo booleano continuar"""
    continuar = True
    
    while continuar:
        #El elemento a buscar se introduce por el usuario.
        nombre = input("Ingrese (Actor, Genero o Título de peicula): ")
        
        """Cada pelicula cuenta con un genero un título y un actor"""
        
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
    

        while apila.vacia() == False:
            #Regresa cada elemento de la pila.
            pelicula = apila.desapilar()
            
            """Se evalua el elemento a buscar y dependiendo del atrubuto
                película existente se regresa la información deseada"""
            
            if pelicula.genero == nombre:
                print "Titulo pelicula: " + pelicula.titulo +"\n Protagonista: "+ pelicula.protagonista

            elif pelicula.titulo == nombre:
                print "La protagoniza: " + pelicula.protagonista +"\n pertenece al género de: "+ pelicula.genero

            elif pelicula.protagonista == nombre:
                print "Titulo pelicula: " + pelicula.titulo +"\n pertenece al género de:: "+ pelicula.genero


        continuar = ("s" == raw_input("Desea continuar? s/n").lower())
        
class Pila:
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.pila = []
        
    def apilar(self, elemento):
        """Cada tipo atributo de cada pelicula se apila"""
         # Apilar es agregar al final de la lista.
        self.pila.append(elemento)
        
    def desapilar(self):
        if self.vacia()==False:
            return self.pila.pop()
        else:
            return "Pila vacia"
        
    def vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.pila == []

class Pelicula:
    
    """la clase pelicula cuenta con un método inicial para recibir por
        parámetros cada atributo de una pelicula"""
    
    def __init__(self, genero, titulo, actor):
        self.genero = genero
        self.titulo = titulo
        self.protagonista = actor

main()

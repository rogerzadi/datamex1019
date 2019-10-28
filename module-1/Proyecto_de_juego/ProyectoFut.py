import random

t = ["q", "w", "e", "a", "s", "d"]
p = [1, 2, 3, 4, 5]
marcador = []
Ganador = []
play = ["Messi", "Ronaldo", "Huiqui"]


def porteria():
    print(
        """
        Estas en la final de la copa del mundo, México va 2-2 vs España y tu, tiraras los penales, elige a tu mejor jugador
        y anota¡¡¡recuerda, es una serie de 5 penales, Suerte¡¡¡¡
    
                          ___________________________________________   
                          |                                         |                                     
                          |                                         |    
                          |                     O                   |
                          |                  <--|-->                |
                          |                     |                   |
                          |                    / \                  |
        """
    )


def tiro(tir=None):
    print(
        """Elije el tiro:
    
             a = Izquierda abajo     w = Centro arriba
             q = Izquiera arriba     d = Derecha abajo
             s = Centro abajo        e = Derecha arriba""")
    while tir not in t:
        tir = str(input(tir))
    return tir


def elige():
    class portero:
        # aplicar booster como, tu novia esta viendote jugar, hoy es tu dia de suerte
        def __init__(self, name):
            self.name = name
            self.gol = 0
            self.suerte = 0
            self.rapidez = 0
            self.exp = 0
            self.fallo = 0
            self.final = 0

    class tirador(portero):
        def __init__(self, name):
            self.name = name
            self.fuerza = 0
            self.habilidad = 0
            self.final = 0

    nombre1 = input(
        str("Elige a tu jugador //Tienes 3 opciones,cada uno con diferentes habilidades [Messi, Ronaldo, Huiqui]: "))
    nombre = input((str("Nombre del portero: ")))

    global portero1
    portero1 = portero(nombre)
    global tirador1
    tirador1 = tirador(nombre1)

    if tirador1.name == "Huiqui":
        tirador1.suerte = 0
        tirador1.rapidez = 6
        tirador1.exp = 6
        tirador1.fallo = 1
        tirador1.fuerza = 5
        tirador1.habilidad = 6
        tirador1.gol = 0
        tirador1.final = 24 + tirador1.suerte + tirador1.gol

    elif tirador1.name == "Messi":
        tirador1.suerte = 0
        tirador1.rapidez = 8
        tirador1.exp = 8
        tirador1.fallo = 3
        tirador1.fuerza = 6
        tirador1.habilidad = 8
        tirador1.gol = 0
        tirador1.final = 33 + tirador1.suerte + tirador1.gol

    elif tirador1.name == "Ronaldo":
        tirador1.suerte = 0
        tirador1.rapidez = 8
        tirador1.exp = 8
        tirador1.fallo = 3
        tirador1.fuerza = 8
        tirador1.habilidad = 6
        tirador1.gol = 0
        tirador1.final = 33 + tirador1.suerte + tirador1.gol
    else:
        print("Jugador no registrado, EL PORTERO PARARA TODOOOOO!!!!")
        portero1.gol = 60

    return


def jugada(para=None):
    acuo = marcador.count("O")
    acux = marcador.count("X")

    while para not in p:
        para = random.choice(p)

    if para == 1 and tiro(tir=None) in ["a", "s", "d"]:
        portero1.gol = 40
        print("""      
                      ___________________________________________   
                      |                                         |                                     
                      |            Poorterooooooooo!!!!!        |    
                      |                                         |
                      |                    \                    |
                      |            >------------O               |
                      |                    /                    |
        """)
    elif para == 2 and tiro(tir=None) in ["q", "a", "s"]:
        portero1.gol = 40
        print(""""      
                      ___________________________________________   
                      |               Poorterooooooooo!!!!      |                                     
                      |           O  /                          |    
                      |      >----  \                           |
                      |              \                          |
                      |             /   \                       |
                      |            /      \                     |
        """)
    elif para == 3 and tiro(tir=None) in ["s", "w"]:
        portero1.gol = 40
        print("""      
                      ___________________________________________   
                      |               Poorterooooooooo!!!!      |                                     
                      |                                         |    
                      |                     O                   |
                      |                  <--|-->                |
                      |                     |                   |
                      |                    / \                  |
        """)
    elif para == 4 and tiro(tir=None) in ["s", "e", "d"]:
        portero1.gol = 40
        print("""      
                      ___________________________________________   
                      |               Poorterooooooooo!!!!      |                                     
                      |                        \ O              |    
                      |                        /------<         |
                      |                       /                 |
                      |                    /   \                |
                      |                   /     \               |
        """)
    elif para == 5 and tiro(tir=None) in ["q", "s", "w", "e"]:
        portero1.gol = 40
        print("""      
                      ___________________________________________   
                      |                     O                   |                  
                      |           <-------- |---------->        |    
                      |                     |                   |
                      |                     |                   |
                      |                     |                   |
                      |  Poorterooooooooo!!/ \                  |
        """)
    else:
        tirador1.gol = 40
        print("""      
                      ___________________________________________   
                      |                                         |                                     
                      |      GOOOOOOOOOOOOOOOOOOOOOOOO          |    
                      |         OOOOOOOOOOOOOOOOOOOOOO          |
                      |           OOOOOOOOOOOOOOOOOOOO          |
                      |                     OOOOOLLLLL!!!!!     |
                      |                                         |
        """)

    return (acuo, acux)


def calculo():
    tirador1.suerte = random.randrange(10)
    print(tirador1.suerte)
    tirosue = tirador1.final + tirador1.suerte
    print(tirosue)
    print(portero1.gol)

    if tirosue > portero1.gol:
        marcador.append("O")
        print("Goooooollll de {}".format(tirador1.name))

    else:
        marcador.append("X")
        print("Pooorteroooo {} salva a su equipo una vez mas".format(portero1.name))

    tirador1.gol = 0
    portero1.gol = 0
    tirador1.suerte = 0


def juego():
    porteria()
    elige()
    while Ganador == []:
        acuo = marcador.count("O")
        acux = marcador.count("X")
        if acuo == 3:
            Ganador.append("México es campeeeeeeeoooooooooooon del mundooooooooo")

            break
        elif acux == 3:
            Ganador.append("México se queda a un paso de nuevo!!!!! :( ")

            break
        jugada()
        calculo()
        print(marcador)
    return print(Ganador)

juego()


class Posicion(object):
    def __init__(self):
        self.__y = None
        self.__x = None
        self.__z = None
        self.robotManipulador = None
        self.camara = None
  
    def Setx(self):
        return None

    def Getx(self):
        return None

    def Sety(self):
        return None

    def Gety(self):
        return None

    def Setz(self):
        return None

    def Getz(self):
        return None


class Imagen(object):
    def __init__(self):
        self.Datos = None
        self.contenedor = None
        self.camara = None
        
    def GetDatos(self):
        return None

    def SetDatos(self):
        return None


class Objeto(object):
    def __init__(self):
        self.__Categoria = ""
        self.__Orientacion = None
        self.robotManipulador = None
        self.contenedor = None
        self.garra = None
        
    def SetCategoria(self):
        return ""

    def GetCategoria(self):
        return ""

    def SetOrientacion(self):
        return None

    def GetOrientacion(self):
        return None


class Camara(object):
    def __init__(self):
        self.Posicion = None
        self.Imagen = None
        self.robotManipulador = None
        self.posicion = None
        self.imagen = None
        
    def CapturarImagen(self):
        return None

    def ProcesarImagen(self, parameter):
        return None

    def ObtenerObjetoEnImagen(self):
        return None


class Garra(object):
    def __init__(self):
        self.Posicion = None
        self.Apertura = None
        self.robotManipulador = None
        self.objeto = None
        
    def abrir(self):
        return None

    def cerrar(self):
        return None

    def MejorDistancia(self):
        return None

    def AjustarPosicion(self, parameter):
        return None


class Contenedor(object):
    def __init__(self):
        self.__Categoria = ""
        self.objeto = None
        self.imagen = None
        
    def SetCategoria(self):
        return ""

    def GetCategoria(self):
        return ""


class RobotManipulador(object):
    def __init__(self):
        self.PosicionInicial = None
        self.Camara = None
        self.Garra = None
        self.Contenedor = None
        self.garra = None
        self.posicion = None
        self.objeto = None
        self.camara = None
        
    def Mover(self, parameter2):
        return None

    def ExplorarTerreno(self):
        return None

    def DepositarObjeto(self):
        return None

    def CambiarCategoria(self, parameter):
        return None
x = input("presione cualquer tecla para continuar")

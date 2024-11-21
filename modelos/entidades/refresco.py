from modelos.entidades.bebida import Bebida

class Refresco(Bebida):
    def __init__(self, nombre:str, costo:float, stock:int, mililitros:int, sabor: str, gasificada: bool):
        super().__init__(nombre, costo, stock, mililitros)
        if not isinstance(sabor, str) or sabor == "" or sabor.isspace():
            raise ValueError("El sabor debe ser un string")
        if not isinstance(gasificada, bool):
            raise ValueError("'gasificada' debe ser un valor booleano")
        self.__sabor = sabor
        self.__gasificada = gasificada

    def obtenerPrecio(self):
        return self._costo * 1.5
    
    def obtenerSabor(self):
        return self.__sabor
    
    def esGasificada(self):
        return self.__gasificada
    
    def establecerSabor(self, sabor:str):
        if not isinstance(sabor, str) or sabor == "" or sabor.isspace():
            raise ValueError("El sabor debe ser un string")
        self.__sabor = sabor

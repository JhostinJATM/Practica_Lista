
import json
from model.historial_comando import HistorialComando
from controller.tda.linked.linkedList import LinkedList
from controller.tda.stack.StackO import StackO

class HistorialComandoControl:
    def __init__(self):
        self.__historial_comando = None
        self.__lista = StackO()

    @property
    def _historial_comando(self):
        if self.__historial_comando == None:
            self.__historial_comando = StackO()
        return self.__historial_comando

    @_historial_comando.setter
    def _historial_comando(self, value):
        self.__historial_comando = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self.__lista.add(self.__historial_comando, self.__lista._length)
        
    def generate_id(self):
        return self.__lista._length + 1
    
    def guardar_crear_json(self,nombre ,data ):
        with open(f'{nombre}.json', 'w') as f: 
            json.dump(data, f)


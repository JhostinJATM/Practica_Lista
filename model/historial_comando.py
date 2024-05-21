
import sys 

sys.path.append("../")
from controller.exception.arrayPositionException import ArrayPositionException
from datetime import datetime

class HistorialComando:
    def __init__(self):
        self.__id = 0
        self.__nombre_comando =  ""
        self.__fecha_agregado = datetime.now()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre_comando(self):
        return self.__nombre_comando

    @_nombre_comando.setter
    def _nombre_comando(self, value):
        self.__nombre_comando = value

    @property
    def _fecha_agregado(self):
        return self.__fecha_agregado

    @_fecha_agregado.setter
    def _fecha_agregado(self, value):
        self.__fecha_agregado = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre_comando": self._nombre_comando,
            "fecha_agregado": self._fecha_agregado.strftime("%Y-%m-%d %H:%M:%S")  
        }

    @staticmethod
    def deserializar(data):
        comando = HistorialComando()
        comando._id = data["id"]
        comando._nombre_comando = data["nombre_comando"]
        comando._fecha_agregado = datetime.strptime(data["fecha_agregado"], "%Y-%m-%d %H:%M:%S")  
        return comando

    def __str__(self) -> str:
        return f"{self._nombre_comando}"
   

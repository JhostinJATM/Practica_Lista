from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from model.historial_comando import HistorialComando
from config.logging_config import log
import colorama

class HistorialComandoDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(HistorialComando)
        self.__historial_comando = None

    @property
    def _historial_comando(self):
        if self.__historial_comando == None:
            self.__historial_comando = HistorialComando()
        return self.__historial_comando

    @_historial_comando.setter
    def _historial_comando(self, value):
        self.__historial_comando = value

    @property
    def _lista(self):
        return self._list()
    
    def merge(self, pos):
        self._merge(self._historial_comando, pos)
    
    @property
    def save(self):
        try:
            
            log.debug(colorama.Fore.RED + f"iD: {self._lista._length}" + colorama.Fore.RESET)
            self._historial_comando._id = self._lista._length + 1
            
            log.info(colorama.Fore.BLUE + f"nuevo id = {self._historial_comando._id}" + colorama.Fore.RESET)
            self._save(self._historial_comando)
        except Exception as e:
            log.debug(colorama.Fore.GREEN + f"Error en save es: {e}" + colorama.Fore.RESET)



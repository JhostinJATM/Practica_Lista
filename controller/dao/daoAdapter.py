from typing import TypeVar, Generic, Type
import logging as log
from controller.tda.linked.linkedList import LinkedList
import os.path
import json
import os
from controller.tda.stack.StackO import StackO 

T = TypeVar("T")
class DaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T, size = 20):
        self.atype = atype
        self.lista = StackO(size)
        self.file = atype.__name__.lower()+".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/data/"

    def _list(self) -> T:
        try:
            if os.path.isfile(self.URL+self.file):
                f = open(self.URL+self.file, "r")
                datos = json.load(f)
                self.lista.clear
                for data in datos:
                    a = self.atype.deserializar(data)
                    self.lista.push(a)
                f.close()
            return self.lista
        except Exception as e:
            print(f"Error en list es: {e}")
   
    def _save(self, data: T) -> T:
        try:
            self._list()
            if self.lista._length < 20:
                self.lista.push(data)
            else:
                data._id = self.lista.get(19)._id
                self.lista.pop
                self.lista.push(data)

            auxiliar = []
            if os.path.isfile(self.URL+self.file):
                with open(self.URL+self.file, "r") as f:
                    auxiliar = json.load(f)
            auxiliar.append(data.serializable)
            personas_ordenadas = sorted(auxiliar, key=lambda x: x["id"], reverse = True)
            with open(self.URL+self.file, "w") as f:
                f.write(json.dumps(personas_ordenadas, indent=4))

        except Exception as e:  
            print(f"Error en save es: {e}")

    def _merge(self, data: T, pos) -> T:
        try:
            self._list()
            self.lista.edit(data, pos)
            a = open(self.URL+self.file, "w")
            a.write(self.__tranform__())
            a.close()
        except Exception as e:
            log.debug(f"Error en merge es: {e}")

    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._length):
            aux.append(self.lista.get(i).serializable)
        return aux

    def __tranform__(self):
        try:
            aux = "["
            for i in range(0, self.lista._length):
                if i < self.lista._length - 1:
                    aux += str(json.dumps(self.lista.get(i).serializable))+","
                else:
                    aux += str(json.dumps(self.lista.get(i).serializable))
            aux += "]"
            return aux
        except Exception as e:
                print(f"Error en transform es: {e}")
                

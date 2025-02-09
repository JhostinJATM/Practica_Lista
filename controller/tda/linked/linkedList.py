
from controller.tda.linked.node import Node
from controller.exception.arrayPositionException import ArrayPositionException
from controller.exception.vacioException import VacioException


class LinkedList(object):

    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value


    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0
    
    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length = self.__length +1
        else:
            headOdl = self.__head
            node = Node(data, headOdl)
            self.__head = node
            self.__length = self.__length +1

    
    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)
        else:
            node = Node(data)
            self.__last._next = node 
            self.__last = node
            self.__length += 1

    def getNode(self, pos):
        if self.isEmpty:
            raise VacioException("Error, la lista esta vacia")
        elif pos < 0  or pos >= self.__length:
            raise ArrayPositionException("Error, Esta fuera de los limites de la lista ")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length -1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:
            self.__addLast__(data)
        else:
            node_preview = self.getNode(pos-1)
            node_last =  node_preview.__next #self.__getNode__(pos)
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1

    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:
            self.__last._data = data
        else:
            node = self.getNode(pos)
            node._data = data

    @property
    def toArray(self):
        #Todo
        clazz = None
        matriz = None
        if self.__length > 0:
            clazz = type(self.__head.__data)
            matriz = [None] * self.__length
            aux = self.__head
            for i in range(self.__length):
                matriz[i] = aux.__data
                aux = aux.__next
        return matriz
    
    @property
    def toArray2(self):
        if self.isEmpty:
            return []
        else:
            array = []
            node = self.__head
            while node is not None:
                persona_dict = {
                    "id": node._data._id,
                    "apellido": node._data._apellido,
                    "nombre": node._data._nombres,
                    "telefono": node._data._telefono
                }
                array.append(persona_dict)
                node = node._next
            return array

    def deleteFirst(self):
        if self.isEmpty:
            raise VacioException("Lista Vacia")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self._length == 1:
                self.__last = None
            self._length -= 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise VacioException("Lista Vacia")
        else:
            node = self.__head
            while node._next != self.__last:
                node = node._next
            element = self.__last._data
            node._next = None
            self.__last = node
            self._length -= 1
            return element


    def delete(self, pos):
        if self.isEmpty:
            raise VacioException("Lista Vacia")
        elif pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Posición fuera de los límites de la lista")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == self.__length - 1:
            return self.deleteLast()
        else:
            prev_node = self.getNode(pos - 1)
            node_to_delete = prev_node._next
            prev_node._next = node_to_delete._next
            element = node_to_delete._data
            del node_to_delete
            self._length -= 1
            return element
        
    def list_all(self):
        if self.isEmpty:
            print("La lista está vacía.")
        else:
            current_node = self.__head
            while current_node is not None:
                print(current_node._data)
                current_node = current_node._next

    def arreglo_de_diccionarios(self):
        if self.isEmpty:
            return []
        else:
            array = []
            node = self.__head
            while node is not None:
                array.append(node._data.persona_to_dict())
                node = node._next
            return array
        
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def get(self, pos):
        if self.isEmpty:
            raise VacioException("Error, la lista esta vacia")
        elif pos < 0  or pos >= self.__length:
            raise ArrayPositionException("Error, Esta fuera de los limites de la lista ")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__length -1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data


    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = 'List is Empty'
        else:
            node = self.__head
            while node != None:
                out += str(node._data) + " "
                node = node._next
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node is not None:
            data += str(node._data) + "    "
            node = node._next
        print(f'Lista de datos\n{data}')
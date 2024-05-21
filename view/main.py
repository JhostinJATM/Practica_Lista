import sys
import os
import colorama 

sys.path.append('../')
# from controller.tda.queque.quequeOperation import QuequeOperation
# from controller.tda.stack.stackOperation import StackOperation
from controller.historialComandoDaoControl import HistorialComandoDaoControl
from model.historial_comando import HistorialComando
from controller.historialComandoControl import HistorialComandoControl

colorama.init()

def limpira_consola():
    os.system('cls||cls||clear')

#--------------------------------------------------------------------

if __name__ == "__main__":
    hc = HistorialComandoControl()
    hcd = HistorialComandoDaoControl()
    
    try:
        # hcd._historial_comando = HistorialComando() 
        # hcd._historial_comando._id = hc.generate_id()
        # hcd._historial_comando._nombre_comando = "node index.js"
        # hcd.save
        
        # hcd._historial_comando = HistorialComando() 
        # hcd._historial_comando._id = hc.generate_id()
        # hcd._historial_comando._nombre_comando = "node index.js"
        # hcd.save
        
        hcd = HistorialComandoDaoControl()
        registro = hcd.to_dict()
        print(registro)
        
    except Exception as error:
        print(error)

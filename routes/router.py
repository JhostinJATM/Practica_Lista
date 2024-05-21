
import time
from flask import Flask, Blueprint, url_for, jsonify, make_response, request, render_template, redirect, abort
from controller.historialComandoDaoControl import HistorialComandoDaoControl
from config.logging_config import log
import colorama
# from flask_cors import CORS

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template('template.html')

#* Lista Personas
@router.route('/personas')
def lista_persona():
    hc = HistorialComandoDaoControl()
    return render_template('comando/lista.html', lista=hc.to_dict())
  
@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    hc = HistorialComandoDaoControl()
    comando = hc._list().get(int(pos) - 1)
    return render_template('comando/editar.html', data=comando)

@router.route('/personas/ver')
def ver_guardar():
    return render_template('comando/guardar.html')


@router.route('/personas/guardar', methods = ['POST'])  
def guardar_persona():
    start_time = time.time()
    hc = HistorialComandoDaoControl()
    data = request.form
    if not "nombre_comando" in data.keys():
       abort(400)
    #TODO ...Validar 
    hc._historial_comando._nombre_comando = data['nombre_comando']
    hc.save
    end_time = time.time()
    print(f"Tiempo de ejecución de guardar_atencion (GET): {end_time - start_time} segundos")
    return redirect("/personas", code=302)

@router.route('/personas/modificar', methods = ['POST'])  
def modifcar_personas():
    start_time = time.time()
    hc = HistorialComandoDaoControl()
    data = request.form
    pos_int = int(data["id"])
    comando = hc._list().get(pos_int - 1)
    if not "nombre_comando" in data.keys():
        abort(400)
    #TODO ...Validar 
    hc._historial_comando = comando
    hc._historial_comando._nombre_comando = data['nombre_comando']
    hc.merge(pos_int - 1)
    end_time = time.time()
    print(f"Tiempo de ejecución de guardar_atencion (GET): {end_time - start_time} segundos")
    return redirect("/personas", code=302)

from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoBebidas
from modelos.entidades.bebida import Bebida
from modelos.entidades.refresco import Refresco 
from modelos.entidades.agua import Agua

repo_bebidas = obtenerRepoBebidas()

@bp_bebidas.route("/bebidas", methods = ["GET"])
def listar_bebidas():
    return jsonify([bebida.toDiccionario() for bebida in repo_bebidas.obtenerBebidas()])

@bp_bebidas.route("/bebidas/<string:nombre>", methods = ["GET"])
def obtener_bebida(nombre):
    bebida = repo_bebidas.obtenerBebidaPorNombre(nombre)
    if bebida == None:
        return jsonify({"error": "Bebida no encontrada"}), 404
    return jsonify(bebida.toDiccionario()), 404

@bp_bebidas.route("/bebidas/<string:nombre>", methods = ["DELETE"])
def eliminar_bebida(nombre):
    if repo_bebidas.eliminarBebida(nombre):
        return jsonify({"Mensaje":f"Bebida eliminada con éxito."}),200
    return jsonify({"error": "No se encontró la bebida a eliminar"}), 404

@bp_bebidas.route("/bebidas/<string:nombre>/precio", methods=["GET"])
def obtener_precio_bebida(nombre):
    bebida = repo_bebidas.obtenerBebidaPorNombre(nombre)
    if bebida is None:
        return jsonify({"error": "Bebida no encontrada"}), 404
    return jsonify({"nombre": bebida.obtenerNombre(), "precio": bebida.obtenerPrecio()})400
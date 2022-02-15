import connexion
import six

from ..models.temperature import Temperature  # noqa: E501
from .. import util
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/service/temperature/delete/<id>', methods=['DELETE'])
def delete_temperature(id_temperature):  # noqa: E501
    """Eliminación de datos de temperatura.

    Eliminación un dato de temperatura en la base de datos. # noqa: E501

    :param id_temperature: Id del dato de temperatura
    :type id_temperature: int

    :rtype: str
    """
    data = db.session.query(Temperature).get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify('Deleted')


@app.route('/service/temperature/<id>', methods=['GET'])
def get_temperature(date):  # noqa: E501
    """Devuelve todos los datos relacionados con la temperatura.

    Devuelve todos los datos relacionados con la temperatura. # noqa: E501

    :param date: Fecha de la recogida de la i

    información
    :type date: str

    :rtype: str
    """
    return db.session.query(Temperature.id_temperature, Temperature.date, Temperature.amount).filter(
        Temperature.date == date).first()


@app.route('/service/temperature/post/<id>', methods=['POST'])
def post_temperature(temperature):  # noqa: E501
    """Registra un nuevo dato de temperatura.

    Creacion de nuevos datos asociados a la temperatura. # noqa: E501

    :param temperature: 
    :type temperature: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        temperature = Temperature.from_dict(connexion.request.get_json())  # noqa: E501

        data = request.get_json()
        date = data.get('date')
        amount = data.get('amount')
        db.session.add(Temperature(date, amount))
        db.session.commit()

    return jsonify('Post')


@app.route('/service/temperature/put/<id>', methods=['PUT'])
def put_temperature(temperature):  # noqa: E501
    """Modifica un dato de temperatura previamente registrado

    Modifica un dato de temperatura previamente registrado # noqa: E501

    :param temperature: 
    :type temperature: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        temperature = Temperature.from_dict(connexion.request.get_json())  # noqa: E501
        data = request.get_json()
        date = data.get('date')
        amount = data.get('amount')
        temp = db.session.query(Temperature).get(temperature.id_temperature)
        temp.date = date
        temp.amount = amount
        db.session.commit()

    return jsonify('Update')

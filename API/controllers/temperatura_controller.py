import connexion
import six

from openapi_server.models.temperature import Temperature  # noqa: E501
from openapi_server import util


def delete_temperature(id_temperature):  # noqa: E501
    """Eliminación de datos de temperatura.

    Eliminación un dato de temperatura en la base de datos. # noqa: E501

    :param id_temperature: Id del dato de temperatura
    :type id_temperature: int

    :rtype: str
    """
    return 'do some magic!'


def get_temperature(date):  # noqa: E501
    """Devuelve todos los datos relacionados con la temperatura.

    Devuelve todos los datos relacionados con la temperatura. # noqa: E501

    :param date: Fecha de la recogida de la información
    :type date: str

    :rtype: str
    """
    return 'do some magic!'


def post_temperature(temperature):  # noqa: E501
    """Registra un nuevo dato de temperatura.

    Creacion de nuevos datos asociados a la temperatura. # noqa: E501

    :param temperature: 
    :type temperature: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        temperature = Temperature.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_temperature(temperature):  # noqa: E501
    """Modifica un dato de temperatura previamente registrado

    Modifica un dato de temperatura previamente registrado # noqa: E501

    :param temperature: 
    :type temperature: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        temperature = Temperature.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

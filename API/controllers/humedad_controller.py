import connexion
import six

from openapi_server.models.humidity import Humidity  # noqa: E501
from openapi_server import util


def delete_humidity(id_humidity):  # noqa: E501
    """Eliminación de datos de humedad.

    Eliminación un dato de humedad en la base de datos. # noqa: E501

    :param id_humidity: Id del dato de humedad
    :type id_humidity: int

    :rtype: str
    """
    return 'do some magic!'


def get_humidity(date):  # noqa: E501
    """Devuelve todos los datos relacionados con la humedad.

    Devuelve todos los datos relacionados con la humedad. # noqa: E501

    :param date: Fecha de la recogida de la información
    :type date: str

    :rtype: str
    """
    return 'do some magic!'


def post_humidity(humidity):  # noqa: E501
    """Registra un nuevo dato de humedad.

    Creacion de nuevos datos asociados a la humedad. # noqa: E501

    :param humidity: 
    :type humidity: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        humidity = Humidity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_humidity(humidity):  # noqa: E501
    """Modifica un dato de humedad previamente registrado

    Modifica un dato de humedad previamente registrado # noqa: E501

    :param humidity: 
    :type humidity: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        humidity = Humidity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

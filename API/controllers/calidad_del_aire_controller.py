import connexion
import six

from openapi_server.models.air_quality import AirQuality  # noqa: E501
from openapi_server import util


def delete_air_quality(id_air_quality):  # noqa: E501
    """Eliminación de datos de la calidad del aire.

    Eliminación de un dato de la calidad del aire guardado en la base de datos. # noqa: E501

    :param id_air_quality: Id de la calidad del aire
    :type id_air_quality: int

    :rtype: str
    """
    return 'do some magic!'


def get_air_quality(date):  # noqa: E501
    """Devuelve todos los datos relacionados con la calidad del aire.

    Devuelve todos los datos relacionados con la calidad del aire. # noqa: E501

    :param date: Fecha de la recogida de la información
    :type date: str

    :rtype: str
    """
    return 'do some magic!'


def post_air_quality(air_quality):  # noqa: E501
    """Registra un nuevo dato de calidad del aire.

    Creacion de nuevos datos asociados a la calidad del aire. # noqa: E501

    :param air_quality: 
    :type air_quality: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        air_quality = AirQuality.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_air_quality(air_quality):  # noqa: E501
    """Modifica un dato de calidad del aire previamente registrado

    Modifica un dato de calidad del aire previamente registrado # noqa: E501

    :param air_quality: 
    :type air_quality: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        air_quality = AirQuality.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

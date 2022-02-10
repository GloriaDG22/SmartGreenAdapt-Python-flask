import connexion
import six

from openapi_server.models.luminosity import Luminosity  # noqa: E501
from openapi_server import util


def delete_luminosity(id_luminosity):  # noqa: E501
    """Eliminación de datos de luminosidad.

    Eliminación un dato de luminosidad en la base de datos. # noqa: E501

    :param id_luminosity: Id del dato de luminosidad
    :type id_luminosity: int

    :rtype: str
    """
    return 'do some magic!'


def get_luminosity(date):  # noqa: E501
    """Devuelve todos los datos relacionados con la luminosidad.

    Devuelve todos los datos relacionados con la luminosidad. # noqa: E501

    :param date: Fecha de la recogida de la información
    :type date: str

    :rtype: str
    """
    return 'do some magic!'


def post_luminosity(luminosity):  # noqa: E501
    """Registra un nuevo dato de luminosidad.

    Creacion de nuevos datos asociados a la luminosidad. # noqa: E501

    :param luminosity: 
    :type luminosity: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        luminosity = Luminosity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_luminosity(luminosity):  # noqa: E501
    """Modifica un dato de luminosidad previamente registrado

    Modifica un dato de luminosidad previamente registrado # noqa: E501

    :param luminosity: 
    :type luminosity: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        luminosity = Luminosity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

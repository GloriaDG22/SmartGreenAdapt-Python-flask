import connexion
import six

from openapi_server.models.notification import Notification  # noqa: E501
from openapi_server import util


def delete_notification(id_notification):  # noqa: E501
    """Eliminación de datos de notificación.

    Eliminación de una notificación en la base de datos. # noqa: E501

    :param id_notification: Id del dato de notificación
    :type id_notification: int

    :rtype: str
    """
    return 'do some magic!'


def get_notification(date):  # noqa: E501
    """Devuelve todos los datos relacionados con notificaciones.

    Devuelve todos los datos relacionados con notificaciones. # noqa: E501

    :param date: Fecha de la recogida de la información
    :type date: str

    :rtype: str
    """
    return 'do some magic!'


def post_notification(notification):  # noqa: E501
    """Registra una nueva notificación.

    Creacion de nuevas notificaciones. # noqa: E501

    :param notification: 
    :type notification: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        notification = Notification.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_notification(notification):  # noqa: E501
    """Modifica una notificación previamente registrado

    Modifica una notificacion previamente registrada # noqa: E501

    :param notification: 
    :type notification: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        notification = Notification.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

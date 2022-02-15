import connexion
import six

from ..models.notification import Notification  # noqa: E501
from .. import util


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

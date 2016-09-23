from photos.settings import PROJECT_BADWORDS
from django.core.exceptions import ValidationError

def badwords_detector(value):
    """
    Valida si en en value se han puesto tacos definidos en settings.BADWORDS
    :return: Boolean
    """
    for badword in PROJECT_BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

    # Si todo va OK, devuelvo True
    return True
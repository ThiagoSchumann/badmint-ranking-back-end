from api.models import Athlete

def athlete_get_all():
    return Athlete.objects.all()


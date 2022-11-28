from api.models import File


def file_get_all():
    return File.objects.all()

from api.models import Category


# __author:Barth
def category_get_all():
    return Category.objects.all()


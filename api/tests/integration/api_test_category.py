from .authenticated_api_test import AuthenticatedAPITestCase


class APICategoryTestCase(AuthenticatedAPITestCase):
    list_url = 'category-list'

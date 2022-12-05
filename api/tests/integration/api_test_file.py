from .authenticated_api_test import AuthenticatedAPITestCase


class APIFileTestCase(AuthenticatedAPITestCase):
    list_url = 'file-list'

from .authenticated_api_test import AuthenticatedAPITestCase


class APIRankingTestCase(AuthenticatedAPITestCase):
    list_url = 'ranking-list'

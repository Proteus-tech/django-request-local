from unittest import TestCase
from mock import Mock

from ..middleware import RequestLocal

class FakeRequest(object):
    """
    a fake request object so we don't have to depend on Django to test this
    """
    def __init__(self):
        self.session = Mock()
        self.session.session_key = 'abcde'

class TestRequestLocal(TestCase):
    def setUp(self):
        self.request_local = RequestLocal()
        self.request = FakeRequest()
        self.request_local.process_request(self.request)

    def test_get_current_request(self):
        current_request = RequestLocal.get_current_request()
        self.assertEqual(self.request,current_request)

    def test_get_current_sessionid(self):
        current_sessionid = RequestLocal.get_current_session_id()
        self.assertEqual(self.request.session.session_key,current_sessionid)
#!/usr/bin/env python
try:
    import threading
except ImportError:
    from django.utils import _threading_local as threading

class RequestLocal(object):
    """
    Installation:

        - Add 'django_request_local.middleware.RequestLocal' to your settings.MIDDLEWARE_CLASSES

    Example:

    .. highlight:: python

        from django_request_local.middleware import RequestLocal
        current_request = RequestLocal.get_current_request()

    """

    _threading_local = threading.local()

    def process_request(self, request):
        setattr(self._threading_local, 'request', request)

    @classmethod
    def get_current_request(cls):
        return getattr(cls._threading_local, 'request', None)

    @classmethod
    def get_current_session_id(cls):
        request = cls.get_current_request()
        try:
            return request.session.session_key
        except AttributeError:
            pass

        return None

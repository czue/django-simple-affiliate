from datetime import datetime
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone
from . import const


def affiliate_middleware(get_response):
    """
    Sets `request.affiliate_id` and `request.affiliate_date` in the session and on the request object
    if the `PARAM_NAME` is found in the request or if an affiliate already existed in the session.
    """
    # very loosely inspired by https://github.com/st4lk/django-affiliate

    def middleware(request):
        session = getattr(request, 'session', None)
        if not session:
            raise ImproperlyConfigured(
                "session attribute should be set for request. Please add "
                "'django.contrib.sessions.middleware.SessionMiddleware' "
                "to your MIDDLEWARE_CLASSES")

        now = timezone.now()
        affiliate_id = request.GET.get(const.AFFILIATE_PARAM_NAME, None)
        if affiliate_id:
            print('setting affiliate id!')
            session[const.AFFILIATE_SESSION_KEY] = affiliate_id
            session[const.AFFILIATE_DATE_SESSION_KEY] = now.isoformat()
        else:
            print('no affiliate id!')
        request.affiliate_id = session.get(const.AFFILIATE_SESSION_KEY, None)
        unparsed_date = session.get(const.AFFILIATE_DATE_SESSION_KEY, None)
        try:
            request.affiliate_date = datetime.strptime(unparsed_date, "%Y-%m-%dT%H:%M:%S.%fZ") if unparsed_date else None
        except ValueError:
            request.affiliate_date = None

        return get_response(request)

    return middleware

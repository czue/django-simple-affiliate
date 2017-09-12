from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone


def get_affiliate_id(request, expiry_period=None):
    expiry_period = expiry_period or getattr(settings, 'AFFILIATE_EXPIRY_PERIOD', None)
    try:
        affiliate_id = request.affiliate_id
    except AttributeError:
        raise ImproperlyConfigured('You need to add "simple_affiliate.middleware.affiliate_middleware" to '
                                   'your MIDDLEWARE in settings.py to use this function!')

    if expiry_period and affiliate_id and timezone.now() - expiry_period > request.affiliate_date:
        # a valid affiliate ID has expired
        return None
    else:
        return affiliate_id

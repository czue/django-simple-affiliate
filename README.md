# Simple Affiliate System for Django


This is a very simple library that can be used to provide affiliate links in your django application.
It is intentionally very lightweight, allowing your application to do whatever it wants with the data.

The project is very loosely inspired by the [django-affiliate](https://github.com/st4lk/django-affiliate) library,
though seeks to provide a lighter-weight way to provide the core set of functionality without requiring the
use of any additional data models.

If you are looking for a more heavyweight/comprehensive solution you may be better off with
[django-affiliate](https://github.com/st4lk/django-affiliate).

## How it Works


You give a code to each partner you want to send links to your application.
They choose a link that includes their code in an `aid` parameter in the URL. E.g.

`http://example.com/?aid=12345`

This code is saved in the django session using a middleware, which also adds the id to the request
as `request.affiliate_id` (note: the ID will also be added if there was no URL param but an id was found
already in the session).

Then you can use whatever custom processing logic you want on the `request.affiliate_id` throughout the
rest of your code.

## Requirements

- python (only tested on 3.5 but should work in 2.7)
- django (only tested in 1.11 but might work with older versions)


## Quick start

1. Install this package to your python distribution

`pip install django-simple-affiliate`

2. Add `'simple_affiliate.middleware.affiliate_middleware'` to `MIDDLEWARE`:

```python
MIDDLEWARE = (
    # ...
    'simple_affiliate.middleware.affiliate_middleware',
)
```

3. Reward / track affiliate

```python
if request.affiliate_id and made_some_cash(request):
    pay_affiliate_by_id(request.affiliate_id, dollar_value(request)
```

## Project Todos

  - [] Add / document expiration timeout functionality
  - [] Add tests

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toms_portfolio_3.settings')

application = get_wsgi_application()

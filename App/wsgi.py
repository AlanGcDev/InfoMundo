import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App.settings')

# Aquí define tu aplicación como 'app'
app = get_wsgi_application()

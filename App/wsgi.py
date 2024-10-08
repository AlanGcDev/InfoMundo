import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App.settings')

# Obtén la aplicación WSGI de Django
django_app = get_wsgi_application()

# Envuelve la aplicación con WhiteNoise para servir archivos estáticos
app = WhiteNoise(django_app, root=os.path.join(os.path.dirname(__file__), 'staticfiles'))

# Opcional: Configuración adicional de WhiteNoise (compressión, cache)
app.add_files(os.path.join(os.path.dirname(__file__), 'media'), prefix='media/')

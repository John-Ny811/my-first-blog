from django.contrib import admin
from .models import Post   # Post wurde selber erstellt in der models-Datei

admin.site.register(Post)  # notwendiger Befehl damit das Post-Model auf der Admin-Seite sichtbar wird

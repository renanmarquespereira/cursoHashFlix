from django.apps import AppConfig

class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import Usuario
        import os

        email = os.getenv('EMAIL_ADMIN')
        password = os.getenv('SENHA_ADMIN')

        if email and password and not Usuario.objects.filter(email=email).exists():
            Usuario.objects.create_superuser(
                username="admin",
                email=email,
                password=password,
                is_active=True,
                is_staff=True
            )

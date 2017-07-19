from django.conf import settings


def setting_to_context(request):
    return {
        "settings": settings,
    }

"""
ASGI config for firstProject1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
# 현재 프로젝트를 서비스하기 위한 ASGI(Asynchronous Server Gateway Interface)
# 호환 웹서버 진입점

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstProject1.settings')

application = get_asgi_application()

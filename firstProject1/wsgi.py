"""
WSGI config for firstProject1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
# 현재 프로젝트를 서비스하기 위한 WSGI(Web Server Gateway Interface)
# 호환 웹 서버의 진입점

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstProject1.settings')

application = get_wsgi_application()

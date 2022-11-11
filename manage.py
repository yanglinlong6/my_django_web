#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_web.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # django-admin startproject my_django_web

    # 在Django项目(my_project)的根目录下执行
    # python3 manage.py startapp my_app

    # make new migrations
    # python3 manage.py makemigrations

    # apply all migrations
    # python3 manage.py migrate

    # run server
    # python3 manage.py runserver

    main()

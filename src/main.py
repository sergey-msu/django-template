"""
   Application entry point.
"""
import sys

from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line


if __name__ == '__main__':
    execute_from_command_line(sys.argv)
else:
    application = get_wsgi_application()

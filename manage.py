#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This script is used to manage the Django project, including running the server,
applying migrations, and executing various administrative commands.
"""

import os
import sys


def main():
    """Run administrative tasks, setting the Django settings module."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mySite.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available "
            "on your PYTHONPATH environment variable. Did you forget to "
            "activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()


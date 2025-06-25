#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')  # or your path
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')  # Or 'Prod' depending on your class

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django configurations. Make sure it's installed and in your virtualenv."
        )
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

#!/usr/bin/env python

"""
Django administration utility.
"""

import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enterprise_catalog.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

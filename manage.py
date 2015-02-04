#!/usr/bin/env python
import os
import envvars
import sys

envvars.load()
if __name__ == "__main__":
	
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", envvars.get("DJANGO_SETTINGS_MODULE"))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# https://qiita.com/ymto/items/e00e95543aab2d4d45ee ⇦ModuleNotFoundError: No module named 'djoser'が出たのでこちらの記事を参考にした
sys.path.append('/Users/ta93n/学習/iidx_app/.venv/lib/python3.9/site-packages')


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
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
    main()

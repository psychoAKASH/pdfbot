import os
import sys
import pathlib

NBS_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = NBS_DIR.parent

def init_django(project_name="akhome"):
    os.chdir(BASE_DIR)
    sys.path.insert(0, os.getcwd()) #os.getenv('PWD')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"{project_name}.settings")
    os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
    import django
    django.setup()


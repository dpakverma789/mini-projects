import secrets
import os
import sys
PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(PROJECT_DIRECTORY,'requirements.txt')
root_dir = os.path.dirname(PROJECT_DIRECTORY)
sys.path.insert(0, root_dir)

def install_requirements(file=None):
    return os.system(f'pip install -r {file}')

def remove_requirements(file=None):
    if os.path.isfile(file):
        return os.system(f'pip uninstall -y -r {file}')
    return False

try:
    from django.core.management.utils import get_random_secret_key
except ModuleNotFoundError:
    try:
        if not os.path.isfile(REQUIREMENTS_FILE):
            raise FileNotFoundError
        install_requirements(REQUIREMENTS_FILE)
    except FileNotFoundError:
        os.system('python -m pip install --upgrade pip')
        for pack in ('django',):
            os.system(f'pip install {pack}')
        from django.core.management.utils import get_random_secret_key
    finally:
        os.system('pip freeze > requirements.txt')


if __name__ == "__main__":
    flag = True
    # while flag:
    #     key = get_random_secret_key()
    #     if '#' not in key:
    #         break
    # print('Django Key: ',key)
    key = secrets.token_urlsafe(50)
    print('Django Key: ', key)
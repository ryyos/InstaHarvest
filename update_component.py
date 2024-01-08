import os

from dotenv import *
from src import file

if __name__ == '__main__':

    cookies = input('INSERT YOUR COOKIES (enter for skip): ')
    claim = input('INSERT YOUR IG CLAIM (enter for skip): ')
    path = input('INSERT YOUR PATH TO SAVE: ')
    if not os.path.exists('.env'): file.write('.env', '')

    load_dotenv()
    file_env = find_dotenv()

    if cookies and claim:
        set_key(file_env, 'COOKIES', cookies.replace('\\', '\\\\'))
        set_key(file_env, 'IG_CLAIM', claim)

    if path: set_key(file_env, 'PATH_TO_SAVE', path)

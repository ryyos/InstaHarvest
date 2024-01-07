import os

from dotenv import *
from src import file

if __name__ == '__main__':

    cookies = input('INSERT YOUR COOKIES: ')
    claim = input('INSERT YOUR IG CLAIM: ')
    if not os.path.exists('.env'): file.write('.env', '')

    load_dotenv()
    file_env = find_dotenv()
    set_key(file_env, 'COOKIES', cookies.replace('\\', '\\\\'))
    set_key(file_env, 'IG_CLAIM', claim)

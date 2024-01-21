import os

from dotenv import *
from src import Instagram
from src import ArgumentParserCustom
from src import PathNotFoundExceptions
from src import ExpiredExceptions
from src import file

#v.0.0.4
if __name__ == '__main__':

    if not os.path.exists('.env'): file.write('.env', '')

    instagram = Instagram()
    arg = ArgumentParserCustom()

    arg.add_argument('--username', '-u', type=str, help='Enter the target username', required=True)
    
    arg.add_argument('--cookies', '-c', type=str, help='Insert your COOKIES')
    arg.add_argument('--igclaim', '-ic', type=str, help='Insert your IG CLAIM')
    arg.add_argument('--path', '-p', type=str, help='Insert your PATH TO SAVE')
    arg = arg.parse_args()

    file_env = find_dotenv()

    if arg.cookies and arg.igclaim:
        load_dotenv()

        set_key(file_env, 'COOKIES', arg.cookies.replace('\\', '\\\\'))
        set_key(file_env, 'IG_CLAIM', arg.igclaim)

    if arg.path: set_key(file_env, 'PATH_TO_SAVE', arg.path)

    try:
        instagram.main(username=arg.username)

    except KeyError:
        raise ExpiredExceptions()
    except FileNotFoundError:
        raise PathNotFoundExceptions()

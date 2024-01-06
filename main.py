import os

from dotenv import *
from src import Instagram
from src import ArgumentParserCustom
from src import file

if __name__ == '__main__':

    if not os.path.exists('.env'): file.write('.env', '')

    instagram = Instagram()
    arg = ArgumentParserCustom()

    arg.add_argument('--username', '-u', type=str, help='Enter the target username', required=True)
    arg.add_argument('--userid', '-id', type=str, help='Enter the target user id', required=True)
    
    arg.add_argument('--cookies', '-c', type=str, help='Insert your COOKIES')
    arg.add_argument('--igclaim', '-ic', type=str, help='Insert your IG CLAIM')
    arg = arg.parse_args()

    if arg.cookies and arg.igclaim:
        print(arg.cookies)
        load_dotenv()

        file_env = find_dotenv()
        set_key(file_env, 'COOKIES', arg.cookies.replace('_', '; '))
        set_key(file_env, 'IG_CLAIM', arg.igclaim)

    instagram.main(username=arg.username, user_id=arg.userid)
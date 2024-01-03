import sys
from argparse import ArgumentParser

class ArgumentParserCustom(ArgumentParser):
    def exit(self, status=0, message=None):
            if status:
                print("""
to run please insert flags

--usernmae    or -e    YOUR_EMAIL
                      
if your COOKIES and IG CLAIM is expired please insert this flag for update your env
                      
--cookies   or -p    YOUR_COOKIES
--igclaim   or -s    YOUR_IG_CLAIM

Example: python main.py --username jkt48.freya --cookies dfcgvjkml --igclaim waesdfcgvbhjn
                      
                      OR

Example: python main.py --username jkt48.freya
""")
            sys.exit(status)

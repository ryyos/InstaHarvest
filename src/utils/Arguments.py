import sys
from argparse import ArgumentParser

class ArgumentParserCustom(ArgumentParser):
    def exit(self, status=0, message=None):
            if status:
                print("""
to run please insert flags

--username    or -u   <USERNAME_TARGET>

                   ⚠️ATTENTIONS⚠️                      
if your COOKIES and IG CLAIM is expired please insert this flag for update your env,
and wrap the cookies in single quotes '<YOUR_COOKIES>'
                      
--cookies   or -p     '<YOUR_COOKIES>'
--igclaim   or -ic    '<YOUR_IG_CLAIM>'
--path      or -p     '<YOUR_PATH_TO_SAVE>'
                      
                   ⚠️SUGGESTION⚠️
or if you don't understand you can run the update_component.py file
                      
python update_component.py

                      
                 ⚠️EXAMPLE USAGES⚠️

python main.py --username jkt48.freya --cookies 'dfcgvjkml' --igclaim 'waesdfcgvbhjn' --path 'data/content'
                      
                       ⚠️OR⚠️

python main.py --username jkt48.freya
""")
            sys.exit(status)

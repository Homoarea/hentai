import os
import sys
from codecs import open
about={}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here,'src','hentai','__version__.py'),'r','utf-8') as f:
    exec(f.read(),about)
print(about)
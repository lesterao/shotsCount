import sys
from distutils.core import setup

kwargs = {}
if 'py2exe' in sys.argv:
    import py2exe
    kwargs = {
        'console' : [{
            'script'         : 'info4.py',
            'description'    : 'Script contar acciones y tiempo'#,
            #'icon_resources' : [(0, 'icon.ico')]
            }],
        'zipfile' : None,
        'options' : { 'py2exe' : {
            'bundle_files'   : 1,
            'compressed'     : True,
            'optimize'       : 2
            }},
         }

setup(
    name='actannCount',
    author='Lester A. Oropesa Morales',
    author_email='lesteroropesa@gmail.com',
    **kwargs)
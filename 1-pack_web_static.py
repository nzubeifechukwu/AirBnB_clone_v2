#!/usr/bin/python3
'''A Fabric script that generates a .tgz archive from the contents of the
    web_static folder
'''
from fabric.api import local
from datetime import datetime

def do_pack():
    '''Creates a .tgz archive from the contents of the folder `web_static`

    Return:
        Path to the archive if successful. None otherwise
    '''
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    local(f'tar -cvzf versions/web_static_{now}.tgz web_static')
    if local('echo $?') == 0:
        return local(f'readlink -f versions/web_static_{now}.tgz')
    return None

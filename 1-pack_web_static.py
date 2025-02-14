#!/usr/bin/python3
'''A Fabric script that generates a .tgz archive from the contents of the
    web_static folder
'''
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    '''Creates a .tgz archive from the contents of the folder `web_static`

    Return:
        Path to the archive if successful. None otherwise
    '''
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = 'versions/web_static_{}.tgz'.format(now)

    local('mkdir -p versions')
    local('tar -cvzf {} web_static'.format(file_path))

    if os.path.exists(file_path):
        return file_path
    return None

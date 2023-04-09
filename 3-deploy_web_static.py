#!/usr/bin/python3
'''This Fabric script creates and distributes a tar (.tgz) archive to my
    web servers, using a function deploy
'''
from fabric.api import env, local, put, run
from datetime import datetime
import os.path

env.hosts = ['34.204.82.149', '107.23.209.253']


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


def do_deploy(archive_path):
    '''Distribute an archive to web servers

    Args:
        archive_path: Path to a .tgz archive

    Return:
        True if all operations succeed. False otherwise
    '''
    try:
        file_no_ext = archive_path.split('/')[1].split('.')[0]
        uncomp_folder = '/data/web_static/releases/{}'.format(file_no_ext)
        put(local_path=archive_path, remote_path='/tmp/')
        run('mkdir -p {}'.format(uncomp_folder))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(file_no_ext, uncomp_folder))
        run('rm /tmp/{}.tgz'.format(file_no_ext))
        run('mv {}/web_static/* {}'.format(uncomp_folder, uncomp_folder))
        run('rm -rf {}/web_static'.format(uncomp_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(uncomp_folder))
        return True
    except Exception as e:
        return False


def deploy():
    '''Uses do_pack and do_deploy functions to create and distribute a tar
        archive to my web servers

    Return: True on success, False on failure
    '''
    archive_path = do_pack()

    if os.path.exists(archive_path):
        status = do_deploy(archive_path)
        return status
    return False

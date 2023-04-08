#!/usr/bin/python3
'''A Fabric script that distributes an archive to my web servers
'''
from fabric.api import env, put, run


env.hosts = ['34.204.82.149', '107.23.209.253']

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
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(uncomp_folder))
        return True
    except Exception as e:
        return False

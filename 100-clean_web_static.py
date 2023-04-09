#!/usr/bin/python3
'''This Fabric Script deletes outdated tar (.gzp) archives,
    using the function do_clean
'''
from fabric.api import local, env, run

env.hosts = ['34.204.82.149', '107.23.209.253']


def do_clean(number=0):
    '''Deletes outdated tar archives

    Args:
        number: Number of archives to keep, defaults to 0. If 0 or 1, keep the
            most recent. Otherwise, keep the <number> most recent archives
    '''
    archives = str(local('ls versions', capture=True)).split('\n')
    number = int(number)
    if number < 2:
        for archive in archives[:-1]:
            local('rm versions/{}'.format(archive))
            run('rm -rf /data/web_static/releases/{}'.format(archive[:-4]))
    else:
        for archive in archives[:-number]:
            local('rm versions/{}'.format(archive))
            run('rm -rf /data/web_static/releases/{}'.format(archive[:-4]))

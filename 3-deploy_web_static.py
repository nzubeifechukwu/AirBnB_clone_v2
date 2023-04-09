#!/usr/bin/python3
'''This Fabric script creates and distributes a tar (.tgz) archive to my
    web servers, using a function deploy
'''
from fabric.api import env, local, put, run
from datetime import datetime
import os.path
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static.py import do_deploy

env.hosts = ['34.204.82.149', '107.23.209.253']


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

#!/usr/bin/python3
"""
Scrit used to Deploy archive!
"""
import os
# First we import the Fabric api
from fabric.api import *

env.hosts = ['35.175.135.174', '18.234.169.222']


def do_deploy(archive_path):
    """
    Write a Fabric script (based on the file
    1-pack_web_static.py) that distributes an archive
     to your web servers, using the function
    """
    if (os.path.exists(archive_path)):
        try:
            f_name = archive_path.split('/')[-1]
            name = f_name.split('.')[0]
            store = '/data/web_static/releases/{}'.format(name)
            rf_path = '/tmp/{}'.format(f_name)
            l1 = '/data/web_static/current/web_static/*'
            l2 = '/data/web_static/current'
            run('mkdir -p /tmp')
            run('mkdir -p {}'.format(store))
            put(archive_path, '/tmp')
            run('tar -xzvf {} -C {}'.format(rf_path, store))
            run('rm -rf /tmp/{}'.format(f_name))
            # run('rsync -av --remove-source-files {} {}'.format(l1, l2)
            run('cp -r {}/web_static/* {}'.format(store, store))
            run('rm -rf {}/web_static'.format(store))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(store))
            return (True)
        except Exception:
            return(False)
    else:
        return (False)

#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz
"""
from fabric.api import (local)
import tarfile
from datetime import datetime


def do_pack():
    """
    used to create a tar file.
    """
    try:
        folder = "web_static"
        tyme = datetime.now().strftime("%Y%m%d%H%M%S")
        tar_name = "versions/web_static_{}.tgz".format(tyme)
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(tar_name))
        return (tar_name)
    except:
        return (None)

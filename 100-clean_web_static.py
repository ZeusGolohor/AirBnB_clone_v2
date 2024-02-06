#!/usr/bin/python3
"""
Scrit used to Deploy archive!
"""
import os
# First we import the Fabric api
from fabric.api import *
env.hosts = ['35.175.135.174', '18.234.169.222']


def do_clean(number=0):
    """
    Delete all unnecessary archives (all archives minus the number to keep)
    """
    if (number == '1' or number == '0' or number == 0):
        local('ls -t /versions | tail -n +2 | xargs rm -rf')
        run('ls -t /data/web_static/releases | tail -n +2 | xargs rm -rf')
    elif (number == '2'):
        local('ls -t /versions | tail -n +3 | xargs rm -rf')
        run('ls -t /data/web_static/releases | tail -n +3 | xargs rm -rf')

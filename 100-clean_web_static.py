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
        local('ls -1tr versions/ | grep -v "total" | head -n -1 |  \
            xargs -I {} rm -rf versions/{}')
        run('ls -1tr /data/web_static/releases | grep -v "total" | \
            head -n -1 |  xargs -I {} rm -rf /data/web_static/releases/{}')
    elif (number == '2'):
        local('ls -1tr versions/ | grep -v "total" | head -n -2 |  \
            xargs -I {} rm -rf versions/{}')
        run('ls -1tr /data/web_static/releases | grep -v "total" | \
            head -n -2 |  xargs -I {} rm -rf /data/web_static/releases/{}')
    else:
        local('ls -1tr versions/ | grep -v "total" | head -n -{} \
            |'.format(number) + '  xargs -I {} rm versions/{}')
        run('ls -1tr /data/web_static/releases | grep -v "total" \
            | head -n -{} |'.format(number) + '  xargs -I {} rm \
            /data/web_static/releases/{}')

#!/usr/bin/python3
"""
Script used to deploy an archive.
"""
import os
from fabric.api import *

env.hosts = ['35.175.135.174', '18.234.169.222']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    :param archive_path: Path to the archive file.
    :return: True if all operations are done correctly, False otherwise.
    """
    if not os.path.exists(archive_path):
        print(f"Error: Archive not found at {archive_path}")
        return False

    try:
        # Extract necessary information from the archive_path
        archive_name = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_name)[0]

        # Define paths for deployment
        store_path = '/data/web_static/releases/{}'.format(archive_no_ext)
        remote_archive_path = '/tmp/{}'.format(archive_name)

        # Create necessary directories
        run('mkdir -p {}'.format(store_path))
        run('mkdir -p /tmp')

        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp')

        # Uncompress the archive to the specified folder
        run('tar -xzvf {} -C {}'.format(remote_archive_path, store_path))

        # Remove the uploaded archive from /tmp/
        run('rm -rf {}'.format(remote_archive_path))

        # Remove the existing symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(store_path))

        # Sync contents and remove source files
        run('rsync -av --remove-source-files {}/web_static/ \
        /data/web_static/current/'.format(store_path))

        print("Deployment successful!")
        return True

    except Exception as e:
        print(f"Error during deployment: {e}")
        return False

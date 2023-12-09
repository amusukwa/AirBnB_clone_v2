#!/usr/bin/python3
"""
Fabric script distributes an archive to your web servers, using do_deploy
"""

from fabric.api import *
from os import path

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_no_ext = archive_name.split('.')[0]

        # Upload archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Uncompress archive
        run('mkdir -p /data/web_static/releases/{}'.format(archive_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_name, archive_no_ext))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_name))

        # Delete the symbolic link /data/web_static/current on the server
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_no_ext))

        print("New version deployed!")

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


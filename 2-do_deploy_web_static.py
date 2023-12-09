#!/usr/bin/env python3
"""
Fabric script that distributes an archive to web servers using do_deploy
"""

from fabric.api import *
from os.path import exists

env.hosts = ['<54.173.33.118>', '<34.207.62.11>']
env.user = '<ubuntu>'
env.key_filename = '</root/.ssh/id_rsa>'

def do_deploy(archive_path):
    """
    Distribute an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        archive_name = archive_path.split('/')[-1]
        archive_no_ext = archive_name.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_name, archive_no_ext))

        # Remove the archive from the web server
        run('rm /tmp/{}'.format(archive_name))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_no_ext))

        print("New version deployed!")

        return True

    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    # Example usage:
    archive_path = '/path/to/your/archive.tar.gz'
    do_deploy(archive_path)


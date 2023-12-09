#!/usr/bin/env python3
"""
Fabric script creates and distributes an archive to web servers using deploy
"""

from fabric.api import local, put, run, env
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_pack():
    """
    Create a .tgz archive of the web_static folder
    """
    local("mkdir -p versions")
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -czvf {} web_static".format(archive_path))
    return archive_path


def do_deploy(archive_path):
    """
    Distribute an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_no_ext = archive_name.split('.')[0]

        # Upload archive to /tmp/ directory on the web servers
        put(archive_path, '/tmp/')

        # Uncompress archive
        run('mkdir -p /data/web_static/releases/{}'.format(archive_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_name, archive_no_ext))

        # Delete the archive from the web servers
        run('rm /tmp/{}'.format(archive_name))

        # Delete the symbolic link /data/web_static/current from the web servers
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_no_ext))

        print("New version deployed!")

        return True

    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Deploy a new version by calling do_pack and do_deploy
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)

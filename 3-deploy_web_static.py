#!/usr/bin/env python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers
"""
from fabric.api import local, put, run, env
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder
    """
    try:
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to your web servers
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        no_extension = archive_name.split(".")[0]
        remote_path = "/data/web_static/releases/{}/".format(no_extension)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(remote_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, remote_path))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}web_static/* {}".format(remote_path, remote_path))
        run("rm -rf {}web_static".format(remote_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(remote_path))
        return True

    except Exception as e:
        return False


def deploy():
    """
    Deploy the web_static content to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)

if __name__ == "__main__":
    deploy()

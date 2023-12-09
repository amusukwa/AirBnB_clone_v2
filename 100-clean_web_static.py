#!/usr/bin/env python3
"""
Fabric script deletes out-of-date archives using do_clean
"""

from fabric.api import local, run, env, cd
from datetime import datetime
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """
    Delete unnecessary archives from versions and web_static/releases folders
    """
    number = int(number)
    if number < 0:
        return

    try:
        # Delete unnecessary archives in versions folder
        local("cd versions && ls -t | tail -n +{} | xargs rm -rf".format(number + 1))

        # Delete unnecessary archives in web_static/releases folder on both web servers
        for server in env.hosts:
            with cd('/data/web_static/releases'):
                releases = run('ls -lt --time=atime').split()
                releases_to_delete = releases[number * 2::2]
                for release in releases_to_delete:
                    run('rm -rf {}'.format(release))

        print("Cleaned up old versions!")

    except Exception as e:
        print(e)


def do_pack():
    """
    Create a .tgz archive of the web_static folder
    """
    local

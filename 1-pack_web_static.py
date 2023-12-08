#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Creates a compressed archive from the web_static folder.

    Returns:
        Path to the created archive or None if archive creation fails.
    """
    try:
        # Create the 'versions' folder if it doesn't exist
        local("mkdir -p versions")

        # Generate archive filename using current timestamp
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Create the compressed archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the path to the created archive
        return os.path.join("versions", archive_name)
    except Exception as e:
        # Print an error message and return None if archive creation fails
        print("Error creating archive:", str(e))
        return None

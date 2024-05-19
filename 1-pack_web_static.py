#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    curr_date = datetime.now().strftime("%Y%m%d%H%M%S")

    if isdir("versions") is False:
        local("mkdir versions")
    file_ = "versions/web_static_{}.tgz".format(curr_date)
    local("tar -cvzf {} web_static".format(file_))
    return file_

#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """
    compress into tgz
    """
    f_date = "%Y%m%d%H%M%S"
    curr_date = datetime.now().strftime(f_date)
    if not os.path.isdir("versions"):
        os.makedirs("versions")
    file = "versions/web_static_{}.tgz".format(curr_date)
    try:
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None

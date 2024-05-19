#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
   """Archives the static files."""
   if not os.path.isdir("versions"):
       with os.mkdir("versions"):
           pass
   cur_time = datetime.now().strftime("%Y%m%d%H%M%S")
   output = f"versions/web_static_{cur_time}.tgz"
   try:
       print(f"Packing web_static to {output}")
       local("tar -cvzf {} web_static".format(output))
       archive_size = os.stat(output).st_size
       print(f"web_static packed: {output} -> {archive_size} Bytes")
   except Exception:
       output = None
   return output

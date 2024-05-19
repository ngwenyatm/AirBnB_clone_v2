#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
  """
  This function creates a tar.gz archive of the contents of the web_static directory.

  Returns:
      str: The path to the created archive file, or None if there was an error.
  """
  now = datetime.now()
  filename = os.path.join("web_static_", "{:%Y%m%d%H%M%S}.tgz".format(now))
  run("mkdir -p versions", warn=True)
  archive_path = os.path.join("versions", filename)
  run(f"tar -cvzf {archive_path} web_static")
  return archive_path

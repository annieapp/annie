# This is a template for a WSGI configuration file
# If you know what that is, great!
# If you don't, just ignore it (unless you need to run your own Annie instance)
# Documentation: https://modwsgi.readthedocs.io/en/develop/index.html

# -----------------------------------------------------------------------

import sys

project_home = u'/path/to/annie/server'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from server import app as application  # Do NOT remove, it is used by WSGI

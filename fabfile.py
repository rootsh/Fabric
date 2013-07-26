"""
	fabfile.py
"""

import os 
from fabric.api import *
from fabric.contrib.files import append


@task
def debian_upgrade():
	run("sudo aptitude update && aptitude safe-upgrade -y")



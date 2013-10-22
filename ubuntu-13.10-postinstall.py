#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# My script of Ubuntu 13.10 post installation
#
# Syntax: # sudo ./ubuntu-13.10-postinstall.py
#
# Shiquan Wang <shiquanwang@gmail.com>
# http://shiquanwang.github.io
# Distributed under the GPL version 3 license


__appname__ = 'ubuntu-13.10-postinstall'
__version__ = '0.1'
__author__ = 'Shiquan Wang <shiquanwang@gmail.com>'
__licence__ = 'LGPL'

"""
Post installation script for Ubuntu 13.10
"""


# Global variables
_FOR_UBUNTU = "saucy"
_DEBUG = 1
_LOG_FILE = "/tmp/%s.log" % __appname__
_CONF_FILE = ""


# System commands
_APT_ADD = "add-apt-repository -y"
_APT_INSTALL = "DEBIAN_FRONTEND=noninteractive apt-get -y -f install"
_APT_REMOVE = "DEBIAN_FRONTEND=noninteractive apt-get -y -f remove"
_APT_UPDATE = "DEBIAN_FRONTEND=noninteractive apt-get -y update"
_APT_UPGRADE = "DEBIAN_FRONTEND=noninteractive apt-get -y upgrade"
_APT_KEY = "apt-key adv --keyserver keyserver.ubuntu.com --recv-keys"
_WGET = "wget"


# Classes
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    ORANGE = '\033[93m'
    NO = '\033[0m'

    def disable(self):
        self.RED = ''
        self.GREEN = ''
        self.BLUE = ''
        self.ORANGE = ''
        self.NO = ''

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


# Functions
def init():
    """
    Init the script
    """
    # Globals variables
    global _VERSION
    global _DEBUG

    # Set the log configuration
    logging.basicConfig( \
        filename=_LOG_FILE, \
        level=logging.DEBUG, \
        format='%(asctime)s %(levelname)s - %(message)s', \
         datefmt='%d/%m/%Y %H:%M:%S', \
     )


def syntax():
    """
    Print the script syntax
    """
    print(_("Ubuntu 13.04 post installation script version %s for %s")
                                            % (__version__, _FOR_UBUNTU))
    print("")
    print(_("Syntax: %s.py [-c cfgfile] [-h] [-v]") % __appname__)
    print(_("  -c cfgfile: Use the cfgfile instead of the default one"))
    print(_("  -h        : Print the syntax and exit"))
    print(_("  -v        : Print the version and exit"))
    print(_(""))
    print(_("Exemples:"))
    print(_(""))
    print(_(" # %s.py") % __appname__)
    print(_(" > Run the script with the default configuration file"))
    print(_("   %s") % _CONF_FILE)
    print("")
    print(_(" # %s.py -c ./myconf.cfg") % __appname__)
    print(_(" > Run the script with the ./myconf.cfg file"))
    print("")
    print(_(" # %s.py -c http://mysite.com/myconf.cfg") % __appname__)
    print(_(" > Run the script with the http://mysite.com/myconf.cfg configuration file"))
    print("")


def version():
    """
    Print the script version
    """
    sys.stdout.write(_("Script version %s") % __version__)
    sys.stdout.write(_(" (running on %s %s)\n") % (platform.system(), platform.machine()))


def isroot():
    """
    Check if the user is root
    Return TRUE if user is root
    """
    return (os.geteuid() == 0)


def showexec(description, command, exitonerror = 0, presskey = 0, waitmessage = ""):
    """
    Exec a system command with a pretty status display (Running / Ok / Warning / Error)
    By default (exitcode=0), the function did not exit if the command failed
    """

    if _DEBUG:
        logging.debug("%s" % description)
        logging.debug("%s" % command)

    # Wait message
    if (waitmessage == ""):
        waitmessage = description

    # Manage very long description
    if (len(waitmessage) > 65):
        waitmessage = waitmessage[0:65] + "..."
    if (len(description) > 65):
        description = description[0:65] + "..."

    # Display the command
    if (presskey == 1):
        status = _("[ ENTER ]")
    else:
        status = _("[Running]")
    statuscolor = colors.BLUE
    sys.stdout.write (colors.NO + "%s" % waitmessage + statuscolor + "%s" % status.rjust(79-len(waitmessage)) + colors.NO)
    sys.stdout.flush()

    # Wait keypressed (optionnal)
    if (presskey == 1):
        try:
            input = raw_input
        except:
            pass
        raw_input()

    # Run the command
    returncode = os.system ("/bin/sh -c \"%s\" >> /dev/null 2>&1" % command)

    # Display the result
    if ((returncode == 0) or (returncode == 25600)):
        status = "[  OK   ]"
        statuscolor = colors.GREEN
    else:
        if exitonerror == 0:
            status = "[Warning]"
            statuscolor = colors.ORANGE
        else:
            status = "[ Error ]"
            statuscolor = colors.RED

    sys.stdout.write (colors.NO + "\r%s" % description + statuscolor + "%s\n" % status.rjust(79-len(description)) + colors.NO)

    if _DEBUG:
        logging.debug (_("Returncode = %d") % returncode)

    # Stop the program if returncode and exitonerror != 0
    if ((returncode != 0) & (exitonerror != 0)):
        if _DEBUG:
            logging.debug (_("Forced to quit"))
        exit(exitonerror)


def getpassword(description = ""):
    """
    Read password (with confirmation)
    """
    if (description != ""):
        sys.stdout.write ("%s\n" % description)

    password1 = getpass.getpass(_("Password: "));
    password2 = getpass.getpass(_("Password (confirm): "));

    if (password1 == password2):
        return password1
    else:
        sys.stdout.write (colors.ORANGE + _("[Warning] Password did not match, please try again") + colors.NO + "\n")
        return getpassword()


def getstring(message = _("Enter a value: ")):
    """
    Ask user to enter a value
    """
    try:
        input = raw_input
    except:
        pass
    return raw_input(message)


def waitenterpressed(message = _("Press ENTER to continue...")):
    """
    Wait until ENTER is pressed
    """
    try:
        input = raw_input
    except:
        pass
    raw_input(message)
    return 0

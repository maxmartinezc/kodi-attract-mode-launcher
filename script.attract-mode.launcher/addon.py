# Kodi modules
import xbmc
import xbmcaddon
import xbmcgui

# Python modules
import platform
import os.path
import subprocess


# Getting constants
__addon__ = xbmcaddon.Addon('script.kodi.attract-mode.launcher')
__addonId__ = __addon__.getAddonInfo('id')
__addonName__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__localizedMessages__ = __addon__.getLocalizedString


# Method to print logs on a standard way
def log(message, level=xbmc.LOGNOTICE):
    xbmc.log('[%s:v%s] %s' % (__addonId__, __version__, message.encode('utf-8')), level)
# end of log

# Starting the Addon
log("Starting " + __addonName__)

# Var to hold  the path where the Attract-mode executable is
executable = ""

# We are going to ask on which platform
if platform.system() == "Windows":
    # If is Windows
    executable = __addon__.getSetting('windowsExecutable').decode('utf-8')
    log("Loaded Windows executable location from Settings: " + executable)

else:
    # Linux and others
    executable = __addon__.getSetting('linuxExecutable').decode('utf-8')
    log("Loaded Linux executable location from Settings: " + executable)


# if the executable exists
if not os.path.isfile(executable):
    # Message: Attract-mode executable was not found, go to Addon-Configure and change it
    xbmcgui.Dialog().ok("Error launching Attract-Mode", "The Attract-Mode executable was not found","Please change its location on the Addon-Configure section based on your OS.", "File not found: " + executable)
    # Log the error
    log("Attract-Mode executable was not found on this specified location: " + executable, xbmc.LOGERROR)

else:
    log("Starting Attract-mode executable: " + executable)
    subprocess.call([executable])
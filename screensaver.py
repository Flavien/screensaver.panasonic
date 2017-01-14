import xbmcaddon
import xbmcgui
import xbmc
import os
import panasonic_viera
import xml.etree.ElementTree

addon = xbmcaddon.Addon()
addonName = addon.getAddonInfo("name")
addonPath = addon.getAddonInfo("path")

class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            self.exit_callback()

    def onInit(self):
        self.log("Start Screensaver")
        self.exit_monitor = self.ExitMonitor(self.exit)

        rc = panasonic_viera.RemoteControl("192.168.0.250")
        rc.turn_off()

    def exit(self):
        self.exit_monitor = None
        self.close()
        self.log("Stop Screensaver")

    def log(self, msg):
        xbmc.log(u"%(name)s: %(message)s" % {"name": addonName, "message": msg})

if __name__ == "__main__":
    screensaver = Screensaver("screensaver.xml", addonPath, "default")
    screensaver.doModal()
    del screensaver
    sys.modules.clear()

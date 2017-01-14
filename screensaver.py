# Copyright 2016 Flavien Charlon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import xbmcaddon
import xbmcgui
import xbmc
import os
import panasonic_viera
import xml.etree.ElementTree

addon = xbmcaddon.Addon()
addonName = addon.getAddonInfo("name")
addonPath = addon.getAddonInfo("path")
addonId = addon.getAddonInfo("id")

class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            self.exit_callback()

    def onInit(self):
        self.log("Start Screensaver")
        self.exit_monitor = self.ExitMonitor(self.exit)

        rc = self.create_remote_control()

        rc.turn_off()

    def exit(self):
        self.exit_monitor = None
        self.close()
        self.log("Stop Screensaver")

    def create_remote_control(self):
        file_path = xbmc.translatePath("special://userdata/addon_data/{addon}/settings.xml".format(addon = addonId))
        root = xml.etree.ElementTree.parse(file_path).getroot()
        return panasonic_viera.RemoteControl(root.find("host").text)

    def log(self, msg):
        xbmc.log(u"%(name)s: %(message)s" % {"name": addonId, "message": msg})

if __name__ == "__main__":
    screensaver = Screensaver("screensaver.xml", addonPath, "default")
    screensaver.doModal()
    del screensaver
    sys.modules.clear()

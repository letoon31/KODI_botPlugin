import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hi"
line2 = "The Kodi plugin structure"
line3 = "Using Python"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)

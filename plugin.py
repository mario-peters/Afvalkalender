# Basic Python Plugin Example
#
# Author: GizMoCuz
#
"""
<plugin key="Afvalkalender" name="Afvalkalender" author="mario-peters" version="1.0.0" wikilin="https://github.com/mario-peters/Afvalkalender" externallink="https://github.com/mario-peters/Afvalkalender">
    <description>
        <h2>Afvalkalender</h2><br/>
        TODO Test
        <h3>Configuration</h3><br/>
        TODO TEST
    </description>
    <params>
        <param field="Mode1" label="Postcode" width="50px" required="true" default="1234AB"/>
        <param field="Mode2" label="Huisnummer" width="50px" required="true" default="1"/>
        <param field="Mode3" label="Protocol" width="100px" required="true">
            <options>
                <option label="HTTP" value="HTTP"/>
                <option label="HTTPS" value="HTTPS" default="true"/>
            </options>
        </param>
        <param field="Mode4" label="Gemeente" widht="100px">
            <options>
                <option label="Berkelland" value="afvalkalender.gemeenteberkelland.nl" default="true"/>
                <option label="Cyclus NV" value="afvalkalender.cyclusnv.nl"/>
                <option label="Dar" value="afvalkalender.dar.nl"/>
                <option label="HVC" value="apps.hvcgroep.nl"/>
            </options>
        </param>
        <param field="Mode5" label="Notification system" width="200px">
            <options>
                <option label="email" value="email" default="true"/>
                <option label="gmc" value="gmc"/>
                <option label="http" value="http"/>
                <option label="kodi" value="kodi"/>
                <option label="lms" value="lms"/>
                <option label="nma" value="nma"/>
                <option label="prowl" value="prowl"/>
                <option label="pushalot" value="pushalot"/>
                <option label="pushbullet" value="pushbullet"/>
                <option label="pushover" value="pushover"/>
                <option label="pushsafer" value="pushsafer"/>
            </options>
        </param>
    </params>
</plugin>
"""
import Domoticz
#import requests
#import json
#import datetime

class Baseplugin:
    URL = None
    URL_IMAGES = "https://afvalkalender.gemeenteberkelland.nl/opzet/fatfree/www/media/svg"
    
    def __init__(self):
        #self.var = 123
        return

    def onStart(self):
        Domoticz.Log("onStart called")
        #Domoticz.Heartbeat(30)
        Domoticz.Heartbeat(10)

        port = None
        if Parameters["Mode3"] == "HTTP":
            port = "80"
        else:
            port = "443"

        conn = Domoticz.Connection(Name="BagId", Transport="TCP/IP", Protocol=Parameters["Mode3"], Address=Parameters["Mode4"], Port=port)
        conn.Connect()


    def onStop(self):
        Domoticz.Log("onStop called")

    def onConnect(self, Connection, Status, Description):
        Domoticz.Log("onConnect called")
        Domoticz.Log("Connection name: "+Connection.Name)
        #if Connection.Name == "BagId":
            #sendData = { 'Verb' : 'GET',
                    #'URL' : 'https://afvalkalender.gemeenteberkelland.nl/rest/adressen/'+'7261za-27',
                    #}
            #Connection.Send(sendData)

        """
        url_authorization="https://api.home-connect.com/security/oauth/device_authorization"
        scope="IdentifyAppliance Dishwasher-Monitor"
        data_authorization = {"client_id": CLIENT_ID, "scope": scope}
        HEADER_URLENCODED = {"content-type": "application/x-www-form-urlencoded"}
        response_authorization = requests.post(url_authorization,data_authorization,HEADER_URLENCODED)
        Domoticz.Log("request headers: "+str(response_authorization.request.headers))

        Domoticz.Log(str(Connection))
        Domoticz.Log(str(Status))
        Domoticz.Log(str(Description))
        if (Status == 0):
            Domoticz.Log("Connection succesfull")
            #headers = {"Connection": "keep-alive", "Accept": "Content-Type: text/html; charset=UTF-8"}
            #headers = {"Connection": "keep-alive", "Accept": "Content-Type: application/x-www-form-urlencoded"}
            #HEADER_URLENCODED = {"content-type": "application/x-www-form-urlencoded"} 
            #scope = "IdentifyAppliance Dishwasher-Monitor"
            #data_authorization = {"client_id": CLIENT_ID, "scope": scope}
            #Get moet nog worden omgebouwd naar post + data_authorization erin
            #sendData = { "Verb": "POST", "URL": "/security/oauth/device_authorization", "Data": data_authorization}

            sendData = { 'Verb' : 'POST',
                    'URL' : 'https://api.home-connect.com/security/oauth/device_authorization',
                         'Data' : { 'client_id' : CLIENT_ID, 'scope' : 'IdentifyAppliance' },
                         'Headers' : { "User-Agent": "python-requests/2.19.1", "Accept": "*/*", "Content-Length": "117", "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded", "Accept-Encoding": "gzip, deflate" }
                       }

            Domoticz.Log(str(sendData))
            Connection.Send(sendData)
            #self.homeconnectConn.Send(sendData)
        else:
            Domoticz.Error("Failed to connect ("+str(Status)+") to: "+self.domoticzserver+":"+self.domoticzport+" with error: "+Description)
        """
    def onMessage(self, Connection, Data):
        Domoticz.Log("onMessage called")
        Domoticz.Log(str(Data))

    def onCommand(self, Unit, Command, Level, Hue):
        Domoticz.Log("onCommand called for Unit " + str(Unit) + ": Parameter '" + str(Command) + "', Level: " + str(Level))

    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Domoticz.Log("Notification: " + Name + "," + Subject + "," + Text + "," + Status + "," + str(Priority) + "," + Sound + "," + ImageFile)

    def onDisconnect(self, Connection):
        Domoticz.Log("onDisconnect called")

    def onHeartbeat(self):
        Domoticz.Log("onHeartbeat called")
        #self.homeconnectConn.Connect()

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)

def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)

def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)

def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

    # Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return
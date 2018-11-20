# Basic Python Plugin Example
#
# Author: GizMoCuz
#
"""
<plugin key="Afvalkalender" name="Afvalkalender" author="mario-peters" version="1.0.0" wikilin="https://github.com/mario-peters/Afvalkalender" externallink="https://github.com/mario-peters/Afvalkalender">
    <description>
        <h2>Afvalkalender</h2><br/>
        TODO
        <h3>Configuration</h3><br/>
        TODO
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
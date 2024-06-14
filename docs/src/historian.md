# Setting up the Historian

1. In a browser open <http://localhost:4002/> (local) or <https://hist-plctb.aisec.fraunhofer.de> (prod) **(Note: Chronograf sometimes has issues running correctly on Firefox, try using a Chromium
based browser if you run into any issues.)**
2. Click through the Chronograf setup, no entries have to be changed.
Skip setting up any dashboards at this moment.
   - for the database replace `localhost` with `influxdb`
   - for the Kapacitator replace `localhost` with `kapacitator`
3. On the left bar click on Dashboards.
4. Click 'Import Dashboard' and select the file from:
`historian/chronograf/` for both Modbus and OPCUA.
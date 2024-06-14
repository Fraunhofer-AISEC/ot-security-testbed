# Historian

The historian uses the TICK (Telegraf, InfluxDB, Chronograf and Kapacitator) stack. If one wants to improve the testbed the most interesting component is Telegraf, because it is the only one that directly interacts with the others.

## Telegraf Plugins

We use the following plugins. Consult these links to change the setup.

- [Modbus plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/modbus)
- [OPCUA plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/opcua)
- [InfluxDB v1 plugin](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/influxdb)
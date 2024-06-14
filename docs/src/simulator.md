# Simulator

## Technical Details:

The simulation itself is handled by the `Simulator` object, the `Middleware` implements an interface to access the data from the simulation and handles synchronization and caching (in order to reduce load on the simulation model).
The abstract `Server` can be used to extend the simulator with new protocols, we implemented this for Modbus (using the PyModbus library) and OPC UA (using the asyncua library).

Additionally, we also implemented a simple web application that visualizes the physical process independently of any outside interference (such as attackers).

All of the components run in their own thread(s).

## Extension

If you want to modify the simulation code you can do this in: `industrial-process/simulator`.
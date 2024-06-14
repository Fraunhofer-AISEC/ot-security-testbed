# Launching the Attacks

## Modbus Modification Attack

```sh
# Assumes you are connected to the attacker.

cd /usr/src/exploits
python3 ./start_mitm_modification.py

# Terminate with Ctrl-C  when you want to stop the attack. (might require multiple signals.)
```

### What it does

- Begins with ARP cache poisoning.
- Modifies Modbus traffic between:
  - PLC <-> Industrial Process
  - PLC <-> Historian
- Leads to temperature values being underreported, which damages our simulated system.


## Sniff OpenPLC Login Credentials.


1. Execute the following:
```sh
# Assumes you are connected to the attacker.

cd /usr/src/exploits
python3 ./password_sniff.py
```

2. Wait for someone to login to the [OpenPLC webinterface](https://plc-plctb.aisec.fraunhofer.de/) with the [credentials](./credentials.md).
3. The terminal of the attacker will print out the credentials, which were sniffed from unencrypted HTTP traffic. 

### What it does

- ARP cache poisoning, allowing us to inspect HTTP traffic.
- The attacker has obtained the credentials for further attacks.
- Alternative: use dictionary attack against weak credentials which are very common.


## Upload Malicious Program and Blind Historian

### Assumptions

- The attacker has obtained the credentials to the PLC (look above on how to obtain them).
- The attacker has created a malicious PLC program which is available [here.](./files/heater-malicious.st). If you want to restore the default program you can use [this one](./files/heater-malicious.st).

### How to launch it.

1. Go to the [OpenPLC web interface](https://plc-plctb.aisec.fraunhofer.de/).
2. Go to the [programs section.](https://plc-plctb.aisec.fraunhofer.de/programs)
3. Upload the malicious program. (`heater-malicious.st`)
4. Wait for it to compile (currently slightly slow due to increased compile time due to open62541 usage) and start the PLC again.
5. In an attacker terminal run the following:
```sh
# Assumes you are connected to the attacker.

cd /usr/src/exploits
python3 ./start_mitm_modification_hist_plc.py

# Terminate with Ctrl-C when you want to stop the attack.
```
6. Observe how values are reflected depending on protocol.

### What it does

- PLC behvaior is altered and it ignores too high temperature values.
- Begins with ARP cache poisoning to hide malcious behavior of PLC.
- Modifies Modbus traffic between: PLC <-> Historian
- Modbus based historian loses vision of real values.
- OPC UA based HMI and historian maintain true and umodified vision [(compare here)](https://hist-plctb.aisec.fraunhofer.de/sources/1/dashboards/4).
- Leads to unsafe temperature values being underreported, which damages our simulated system.

# Developer Manual

This part of the documentation explains how to develop with the testbed.

## Folder Structure

The repository has the following structure.

```
├── attacker:                        Files related to the attacker
├── certificates:                    Everything related to the CA and certificate management
├── docker-compose.dev.yml:          Makes the components accessible outside the docker network.
├── docker-compose.external.yml      Redirects some connections to outside the docker networks.
├── docker-compose.prod.yml:         Adds the webserver to the base setup.
├── docker-compose.yml:              Base compose file.
├── docs:                            Sources related to this documentation.
├── FUXA:                            Files related to the HMI
├── historian:                       Files related to the TICK stack
├── industrial-process:              Files related to the process simulator and visualizer
├── nginx:                           Files related to the webserver
├── PLC:                             Files related to OpenPLC
├── readme.md:                       This file.

```
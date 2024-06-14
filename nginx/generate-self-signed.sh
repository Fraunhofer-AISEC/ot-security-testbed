#!/usr/bin/env sh
sudo openssl req -x509 -nodes -days 7 -newkey rsa:2048 -keyout plctestbed.aisec.fraunhofer.de.key -out plctestbed.aisec.fraunhofer.de.crt
sudo openssl dhparam -out dhparam.pem 4096
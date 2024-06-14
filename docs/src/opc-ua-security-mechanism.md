# OPC UA based Security Mechanism

Within the testbed we use the mechanism OPC UA already provides in order to secure the network of our small industrial control system.
As mentioned in this [previous section](./protocols.md#opc-unified-architecture-opc-ua-iec62541) OPC UA already provides many mechanism on its own.
Which is a big step forward from previous generations of industrial protocols, which lacked many of these and either had to retrofit them or left them out entirely.
The security of OPC UA has been [analyzed by the German Federal Office for Information Security (BSI)](https://opcfoundation.org/wp-content/uploads/2017/04/OPC_UA_security_analysis-OPC-F-Responses-2017_04_21.pdf), 
with results confirming good design regarding the security of the protocol.


This section describes the mechanisms themselves in more detail and how we use OPC UA's mechanisms.


## Access Control

OPC UA provides mechanisms for access control to each nodes.
This allows control over which users are allowed to start a session and which nodes they can access.

### User Authentication

OPC UA has four different kind of authentication mechanism:

- **no authentication:** also called anonymous login, actions cannot be mapped to actors and users are not authenticated in any way whatsoever.
- **X.509 Certificates:** these kind of certificates are used widely, in many technologies and can be used as part of public-key-infrastructure in order to establish trust top-down from trusted root-certificates or by trusting individual self-signed certificates. Users have a certificate and the corresponding secret private key, and are authenticated based on proving their knowledge of it.
- **username/password:** another widely used method of authentication, that needs no introduction.
- **[JSON Web Token (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: a method of authentication that is very popular in the world of web development. Listed here only for the sake of completeness, as it is not supported by our used OPC UA library (open62541) and is not widely supported by other libraries either.

These mechanism are used to create sessions.

#### User Authentication inside the Testbed

We use certificates and username/password based authentication in the testbed for critical nodes.
Where possible we use certificate-based authentication and username/password otherwise.

All application certificates are signed by a CA, which serves as the trust anchor and is manually distributed to the hosts along with a certificate revocation list. This CA is outlined [here]([./certificates.md).
With OPC UA, it would also be possible to use self-signed certificates, by adding certain rejected certificates to the trust store, however this approach has drawbacks such as complicated trust revocation issues and scales badly with a big number of applications and corresponding certificates.
OPC UA also defines another way of certificate management via the use of a [GlobalDiscoveryServer (GDS)](https://reference.opcfoundation.org/v104/GDS/docs/6.1/), which are however out of the scope of this testbed.

Access for non-authenticated users is restricted.
Allowing session


### Per-Node Access Control

OPC UA also allows us to limit which nodes can be access by which user.
For instance, we can hide confidential information from third parties which might only need limited access to an OPC UA server, by hiding these nodes from them and preventing access.
This could be a vendor providing remote administration or maintenance services.

We can also control read/write access, for instance, it would make little sense to allow the modification of sensor values.
Whereas it would make a lot of sense to allow certain users the modification of input values, such as goal temperatures and others.

**Per-Node Access Control is still work in progress in the testbed.**

## Message Protection

The protection of messages is affected by two properties of a session, the *SecurityMode* and the *SecurityPolicy*.

There are three different security modes:
- None: no cryptographic protection
- Sign: messages are signed, this ensures their authenticity and integrity. However, this does not protect against eavesdropping.
- SignAndEncrypt: messages are a signed and encrypted, providing additional protection against eavesdropping.

There are [many different](https://profiles.opcfoundation.org/category/47) security policies, these among others affect the utilized cryptographic algorithms used for signing and encryption, can mandate the usage of certificate.
Some standardized security policies are not recommended for use anymore. One example would be [Basic256](http://opcfoundation.org/UA/SecurityPolicy#Basic256), due to using SHA1, which is not considered secure anymore. Additionally, there is also the 'None' mode which provides no security at all and is only compatible with the 'None' security mode.

In the testbed we use SignAndEncrypt in combination with the most secure security polices supported by our OPC UA library (open62541).

## Further References

- [https://reference.opcfoundation.org/v104/Core/docs/Part2/5.2.3/](https://reference.opcfoundation.org/v104/Core/docs/Part2/5.2.3/)
- [https://reference.opcfoundation.org/v104/Core/docs/Part2/4.9/](https://reference.opcfoundation.org/v104/Core/docs/Part2/4.9/)
- [Practical Security Guidelines for Building OPC UA Applications (1)](https://opcconnect.opcfoundation.org/2018/06/practical-security-guidelines-for-building-opc-ua-applications/)
- [Practical Security Recommendations for building OPC UA Applications (2)](https://opcfoundation.org/wp-content/uploads/2017/11/OPC-UA-Security-Advise-EN.pdf)
- [Exploring OPC UA Security Concepts](https://opcconnect.opcfoundation.org/2020/06/exploring-opc-ua-security-concepts/)
- [BSI - OPC UA Security Analysis](https://opcfoundation.org/wp-content/uploads/2017/04/OPC_UA_security_analysis-OPC-F-Responses-2017_04_21.pdf)
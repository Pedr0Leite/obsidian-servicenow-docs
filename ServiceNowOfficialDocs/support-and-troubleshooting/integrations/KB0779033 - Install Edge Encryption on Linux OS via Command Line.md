---
title: "Install Edge Encryption on Linux OS via Command Line"
aliases:
  - KB0779033
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779033
kb_number: KB0779033
last_modified: 2025-01-03
---

## Install Edge Encryption on Linux OS via Command Line

  

### Summary

This KB articulates detailed instructions to setup an Edge Encryption Proxy for your ServiceNow Instance

### Release

Kingston, London, Madrid, New York

### Instructions

This KB articulates commands that you need to execute on a Ubuntu 64 bit OS as the Edge Proxy's Host OS for installing Servicenow Edge Encryption Proxy.   
These commands are common for most of the Linux flavors.  
  
ssh to the Proxy host VM and perform the following:  
  
1) Install Java and other dependencies

```
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
```

2) Install MySQL Server, not older than 5.5

```
sudo  apt-add-repository ppa:ondrej/mysql-5.6
sudo apt-get update
sudo apt-get install mysql-server
```

  
Since this is a dry run, I kept id & password = "root".  
  
3) Install Edge Encryption Plugin on your ServiceNow Instance  
4) Login to your ServiceNow instance with an Admin account, unlock high-Security rights and navigate to  
Edge Encryption Configuration Installation & Downloads Download  
![image](https://community.servicenow.com/9cfde7fddbd893049c9ffb651f961992.iix)  
  
5) Download the relevant installer, in this example: Linux 64 bit.  
6) FTP this installer to your Proxy Server. In this example, we saved the installer at: /home/ubuntu/EDGE/edgeencryption-madrid-12-18-2018\_\_patch4b-07-17-2019\_08-12-2019\_1850-all  
7) Execute below to understand your command:

```
java -jar edgeencryption-madrid-12-18-2018__patch4b-07-17-2019_08-12-2019_1850-all
```

8) above command gives below:

```
ubuntu@ip-172-31-28-4:~/EDGE$ java -jar edgeencryption-madrid-12-18-2018__patch4b-07-17-2019_08-12-2019_1850-all
option: [--mode] MODE required

--help
  -m|--mode                           MODE                   [required, modes: install, upgrade]
  -s|--dst-dir                        DESTINATION DIRECTORY  [optional for mode: install: default: $(PROXY_NAME)_$(PORT)]
  -d|--proxy-dir                      PROXY DIRECTORY        [required for mode: upgrade]
  -n|--proxy-name                     PROXY NAME             [required for mode: install]
  -h|--host                           INSTANCE HOST          [required for mode: install]
  -p|--port                           INSTANCE PORT          [required for mode: install]
  -proto|--protocol                   INSTANCE PROTOCOL      [required for mode: install]
```

_Examples:_  
_a) Example command to Install EdgeEncryption proxy into directory test\_16001:_

```
java -jar edgeencryption-madrid-12-18-2018__patch4b-07-17-2019_08-12-2019_1850-all.jar -m install -n test -h 1.2.3.4 -p 16001 -proto http
```

b) _Example command to_ Install EdgeEncryption proxy into SecureProxy directory, and configure to use secure HTTPS connection:

```
java -jar edgeencryption-madrid-12-18-2018__patch4b-07-17-2019_08-12-2019_1850-all.jar -m install -n test -s SecureProxy -h 1.2.3.4 -p 443 -proto https
```

c) _Example command to_ Upgrade EdgeEncryption proxy installed in directory test\_16001:

```
java -jar edgeencryption-madrid-12-18-2018__patch4b-07-17-2019_08-12-2019_1850-all.jar -m upgrade -d test_16001
```

  
9) We are installing with below: (update parameters as per your details)

```
java -jar edgeencryption-madrid-12-18-2018__patch4b-07-17-2019_08-12-2019_1850-all.jar -m install -n VabEdgeUbuntu1 -h instance_name.service-now.com -p 443 -proto https
```

10) Logs from a successfull execution:

```
ubuntu@ip-172-31-28-4:~/EDGE$ java -jar edgeencryption-madrid-12-18-2018__patch4b-07-17-2019_08-12-2019_1850-all.jar -m install -n VabEdgeUbuntu1 -h instance_name.service-now.com -p 443 -proto https
Sep 17, 2019 5:32:53 AM com.snc.cloudedge_zip.CommandProcessor buildCommand
INFO: option: dist-file: file:/home/ubuntu/EDGE/edgeencryption-madrid-12-18-2018__patch4b-07-17-2019_08-12-2019_1850-all.jar
Sep 17, 2019 5:32:53 AM com.snc.cloudedge_zip.CommandProcessor buildCommand
INFO: option: dst-dir: /home/ubuntu/EDGE/VabEdgeUbuntu1_443
Sep 17, 2019 5:32:53 AM com.snc.cloudedge_zip.CommandProcessor buildCommand
INFO: option: proxy-name: VabEdgeUbuntu1
Sep 17, 2019 5:32:53 AM com.snc.cloudedge_zip.CommandProcessor buildCommand
INFO: option: port: 443
Sep 17, 2019 5:32:53 AM com.snc.cloudedge_zip.CommandProcessor buildCommand
INFO: option: protocol: https
Sep 17, 2019 5:32:53 AM com.snc.cloudedge_zip.CommandProcessor buildCommand
INFO: option: extra-properties: 0
Sep 17, 2019 5:32:53 AM com.snc.dist.upgrade.common.extract.ZipExtractor extract
INFO: extracting: file:/home/ubuntu/EDGE/edgeencryption-madrid-12-18-2018__patch4b-07-17-2019_08-12-2019_1850-all.jar  /home/ubuntu/EDGE/VabEdgeUbuntu1_443
Sep 17, 2019 5:32:54 AM com.snc.cloudedge_zip.CloudedgePermissions execute
INFO: setting permissions: /home/ubuntu/EDGE/VabEdgeUbuntu1_443
Sep 17, 2019 5:32:54 AM com.snc.dist.upgrade.common.extract.ZipExtractor extract
INFO: extracting: file:/home/ubuntu/EDGE/VabEdgeUbuntu1_443/java/mid-jre-1.8.0_40-4-linux-x86-64.zip  /home/ubuntu/EDGE/VabEdgeUbuntu1_443/java
```

  
11) go to <proxy-installation-directory>/conf and open "edgeencryption.properties" to update

```
ubuntu@ip-----:~/EDGE$ cd VabEdgeUbuntu1_443/conf
ubuntu@ip-----:~/EDGE/VabEdgeUbuntu1_443/conf$ vi edgeencryption.properties
```

12) Update below Properties:

```

<edgeencryption.target.host= <Your_ServiceNow_Instance_Name>.service-now.com
---
<edgeencryption.target.username= User_Name_With_Edge_Role_In_Your_Instance
<edgeencryption.target.password= Password_Of_User_With_Edge_Role_In_Your_Instance
---
<edgeencryption.proxy.host= IP_Address_OF_Proxy_Host
---
<edgeencryption.proxy.https.keystore.password= default is "changeme"  set it to the password you want to create alias with.
<edgeencryption.proxy.https.cert.alias= alias1httscerti  set it to the value you want to create alias with.
---
<edgeencryption.db.user= root  This is the user of your sql db server installed earlier
<edgeencryption.db.password= root  Password you set while installing
---
<edgeencryption.proxy.signature.keystore.password= default is "changeme"  set it to the password you want to create alias with.
<edgeencryption.proxy.signature.keystore.keyalias= alias2proxysig  set it to the value you want to create alias with.
---
<#edgeencryption.encrypter.properties.password= <ChangeMe>   Comment this out. This is for password for config encryption
---
< edgeencryption.keystore.path= keystore/keystore.jceks  Uncomment this
<edgeencryption.keystore.password= <ChangeMe>  Uncomment this and set it to default password "changeme" (the password of your encryption key)
```

13) Save "edgeencryption.properties" file.  
14) Go to <proxy-installation-directory>/keystore  
15) Execute below to generate 3 keys:  
  
a) Generating the certificate for the Web server holding the proxy. This is the one you want sign with a CA authority

```
edgeencryption.proxy.https.cert.alias = alias1httscerti
../java/jre/bin/keytool -genkey -alias alias1httscerti -keyalg rsa -keystore keystore.jceks -storetype jceks 
```

b) This is another certificate, internal to edge: the signature

```
edgeencryption.proxy.signature.keystore.keyalias = alias2proxysig
../java/jre/bin/keytool -genkey -alias alias2proxysig -keyalg rsa -keystore keystore.jceks -storetype jceks 
```

c) Generate the encryption certificate on AES format so Edge can encrypt, 128 bit

```
../java/jre/bin/keytool -genseckey -alias jsaes128 -keyalg aes -keystore keystore.jceks -storetype jceks -keysize 128
```

  
  
16) List all certificates in this keystore, it will have 4 now, password for my example keystore is "changeme"

```
../java/jre/bin/keytool -list -v -keystore keystore.jceks -storepass changeme -storetype jceks
```

17) Login to ServiceNow with your admin account, and unlock high-Security rights and navigate to  
Edge Encryption and Configuration Encryption Key Configuration Set Up Keys  
  
![image](https://community.servicenow.com/195a0046db109fc068c1fb651f961983.iix)  
![image](https://community.servicenow.com/a8a22c06db90d704ed6af3231f96198a.iix)  
  
18) Now, you are all set to start up your Edge Encryption Server.  
  
19) Navigate to <proxy-installation-directory> and execute

```
./startup.sh
```

  
![image](https://community.servicenow.com/19b2d182db9897049c9ffb651f96193a.iix)  
  
20) If you see This error:

```
 bin/./wrapper-linux-x86-32: not found
```

  
![image](https://community.servicenow.com/1daf600edb9c57041dcaf3231f96195f.iix)  
Execute below:

```
sudo apt-get install libc6-i386 libc6-dev-i386
```

21) Validate from logs, logs are located at:  
<proxy-installation-directory>/logs  
  
22) Validate if your proxy is up:  
<Your\_ServiceNow\_Instance\_Name>.service-now.com/xmlstats.do?include=edgeencryption  
  
![](/sys_attachment.do?sys_id=aa474089db8038d0fec4fb243996190a)

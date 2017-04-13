# OpenDXL-Tracelog2DXL

## Introduction
The project works as a bridge between standalone logs systems and the DXL fabric. In this way it is possibile to share log update information in real time within the dxl fabric.


![Alt text](https://cloud.githubusercontent.com/assets/24607076/25011318/db5a38ba-2064-11e7-9e2d-480ec3c19c18.png "Structure")

## Requirements
####  Server

* **Linux kernel version 2.6.13 and above:** Inotify (inode notify) is a Linux kernel subsystem that acts to extend filesystems to notice changes to the filesystem and it was merged into the Linux kernel mainline in the kernel version 2.6.13

* **Pyinotify:** Pyinotify is a Python module that leverages inotify


#### McAfee OpenDXL

https://www.mcafee.com/us/developers/open-dxl/index.aspx

1. Python SDK Installation [link](https://opendxl.github.io/opendxl-client-python/pydoc/installation.html)
2. Certificate Files Creation [link](https://opendxl.github.io/opendxl-client-python/pydoc/certcreation.html)
3. ePO Certificate Authority (CA) Import [link](https://opendxl.github.io/opendxl-client-python/pydoc/epocaimport.html)
4. ePO Broker Certificates Export  [link](https://opendxl.github.io/opendxl-client-python/pydoc/epobrokercertsexport.html)


## Pyinotify and DXL client Setup

#### Example of Installing pyinotify from Package in a Ubuntu OS.

> $ sudo apt-get install python-pyinotify

#### edit the dxl.conf
```clj
[Certs]
BrokerCertChain=certs/brokercert.crt
CertFile=certs/client.crt
PrivateKey=certs/client.key

[Brokers]
{}={};8883;
```

## Instructions and example
In order to use the script, you need to run the **tracelog2dxl.py** specifying the topic destination and the log file to trace


```clj
python tracelog2dxl.py -t <topic destination> -f <logfile>
```


#### example of Sophos anti-virus with eicar file in a linux machine



>python tracelog2dxl.py -t /antivirus/sophos -f /opt/sophos-av/log/savd.log 

output:
```clj
DXL message: 

{"TYPE_PAYLOAD": "log", "PAYLOAD": 

"<log><category>log.threat</category><level>ERROR</level><domain>savscand</domain>

<msg>NOTIFY-THREAT-INFECTED-NO-ACCESSED-PATH</msg>

<time>1492086958</time>

<arg>/home/filippo/Downloads/eicar.com.txt</arg>

<arg>EICAR-AV-Test</arg><arg>OPERATION_OPEN</arg></log>", 

"SRC_HOST": "host01"}
```


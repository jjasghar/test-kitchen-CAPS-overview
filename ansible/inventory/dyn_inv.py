#!/usr/bin/env python
# coding=utf-8
import json

aa = {
    "tomcat-servers": {
        "hosts": ['172.28.128.7'],
    }
}

print json.dumps(aa, indent=4)
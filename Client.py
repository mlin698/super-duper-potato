#!/usr/bin/env python

import http.client
import sys

#connects client to the server
http_server = sys.argv[1]
conn = http.client.HTTPConnection(http_server)

while 1:
    #[GET] [command]
    cmd = input()
    cmd = cmd.split()

    #send command to server
    conn.request(cmd[0], cmd[1])

    rsp = conn.getresponse()

    #get server response
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    data_received = str(data_received).strip('b\"')
    print(data_received)

conn.close()

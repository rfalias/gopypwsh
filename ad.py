#!/bin/env python3
import argparse
from pypsrp.client import Client
import getpass
par = argparse.ArgumentParser(description='Move computer object to specified DN')
par.add_argument('--name', type=str, help='Name of computer object', required=True)
par.add_argument('--target', type=str, help='Target to run on', required=True)
par.add_argument('--user', type=str, help='Username', required=True)
par.add_argument('--password', type=str, help='Password')
par.add_argument('--command', type=str, help='Command', required=True)
par.add_argument('--askpass', action='store_true', help='Target DN')
args = par.parse_args()
print(args)

if args.askpass:
    pw = getpass.getpass("Enter password: ")
else:
    if not args.password:
        print("Specify password if askpass not setup")
        exit(-1)
    pw = args.password

ms = Client(args.target, username=args.user,password=pw, ssl=False)

#ps_cmd = "Get-ADComputer '%s' | move-adobject -targetpath '%s'" % (args.name, args.target)
ps_cmd = args.command
output, streams, had_errors = ms.execute_ps(ps_cmd)
print(output)
print(streams)
print(dir(streams))
print("ERROR:\n%s" % "\n".join([str(s) for s in streams.error]))
print("DEBUG:\n%s" % "\n".join([str(s) for s in streams.debug]))
print("VERBOSE:\n%s" % "\n".join([str(s) for s in streams.verbose]))
print("Status: %s, Success: %s" % (output, not had_errors))


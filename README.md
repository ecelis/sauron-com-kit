SauronOS Communications Kit
===========================

Built on top of pjsua library, SCK aims to provide VoIP capabilities to
Citizenship's Towers System. It is a SIP client writen in python for a
very specific purpose. Runs right in the command line without need for
any graphic desktop environment. Designed to run on Unix like (mainly
GNU/Linux) embedded systems, SCK uses the operating system log
capabilities.

Copyright 2013 Ernesto Celis, this software is released under the terms
of the GNU Public License version 3

SCK relies on third party softwre libraries which may be released under
diferent license terms, read the COPY file to get more info.

SCK is sponsored by [Valk Technologies](http://valktechnologies.com/)

Features
--------

* Auto-answer
* Fixed set of extension numbers to dial
* One key press speed dial
* Logs to system's log
* Command line only
* Plain text config file
* Database or config file backend for phone book


Install
-------

### CentOS 

    cd sauron-com-kit
    su
    ./build.sh

### Ubuntu

    cd sauron-com-kit
    sudo ./build.sh


Run
---

   cd sauron-com-kit/ve-phone
   python vephone.py


Enjoy!
Ernesto Celis

P.S. Thank you Teluu Ltd. for the great [pjsip/pjsua](http://www.pjsip.org/) libraries!

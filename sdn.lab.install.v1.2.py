###############################################################
# This installs OpenvSwitch, KVM, Git(Hub) and an OpenFlow    #
# Controller FloodLight (optional). It also downloads a 16Mb  #
# linux-0.2.img.bz2 file that from http://wiki.qemu.org that  #
# is great for testing networking since it is so lightweight  #
# you can simulate lots of VMs running in nested a hypervisors#
# on your laptop or older desktop rather than needing a server#
# for learning or labbing. This is for *Ubuntu* only since it #
# is using apt-get for pkg management.                        #
# This is NOT for anything other than labbing and testing but #
# the KVM and OpenvSwitch install would run production easily.#
# Feel free to use this however you like. Python is a great   #
# language for infrastrcuture applications. It has clean      #
# abstraction leaving it easy to read but also has the power  #
# of object oriented programming. This wil install a fully    #
# working Software Defined Networking (SDN) and OpenFlow      #
# lab in a few minutes. See the accompanying post             #
# I recommend starting in a VM using VMware Fusion as the     #
# first option only becuase it seems to deal with OVS better  #
# than VirtualBox but both work. I would also recommend using #
# snapshots heavily. Install your base Linux 12.04 build and  #
# then take a snapshot in case you have problems with the     #
# App you can rollback to the original snapshot and start over#
# Comments at Twitters @networkstatic, Thanks-Brent Salisbury # 
###############################################################
#http://networkstatic.net/openflow-openvswitch-and-kvm-sdn-lab-installation-app/
#!/usr/bin/python
import subprocess
import os
import time

def git():
    #Install Git
    gitProc = subprocess.Popen('apt-get install -y git', shell=True, stdin=None, executable="/bin/bash")
    gitProc.wait()
    print("Finished installing Git")

def kvm():
    #Install KVM
    kvmProc = subprocess.Popen('apt-get install -y kvm qemu-kvm', shell=True, stdin=None, executable="/bin/bash")
    kvmProc.wait()
    print("Finished installing KVM")

def OVSinst():
    #Download and compile the OpenvSwitch unless a directory name openvswitch exists. 
    #This Git pulls latest dev snapshot from main the branch @ git://openvswitch.org/openvswitch.
    if os.path.exists('openvswitch'):
        print('It appears you already have cloned openvswitch, skipping the clone')
    if not os.path.exists('openvswitch'):
        print('Cloning OVS from GitHub and then compiling the code, may take a few minutes...')
        ovs0Proc = subprocess.Popen("""apt-get install -y git python-simplejson python-qt4 python-twisted-conch automake autoconf 
gcc uml-utilities libtool build-essential git pkg-config linux-headers-`uname -r`""", shell=True, stdin=None, executable="/bin/bash")
        ovs0Proc.wait()
        ovs1Proc = subprocess.Popen('apt-get install -y openvswitch-controller', shell=True, stdin=None, executable="/bin/bash")
        ovs1Proc.wait()
        ovs2Proc = subprocess.Popen(' git clone git://openvswitch.org/openvswitch', shell=True, stdin=None, executable="/bin/bash")
        ovs2Proc.wait()
        os.chdir("openvswitch")
        ovs4Proc = subprocess.Popen('./boot.sh', shell=True, stdin=None, executable="/bin/bash")
        ovs4Proc.wait()
        ovs5Proc = subprocess.Popen('./configure --with-linux=/lib/modules/`uname -r`/build', shell=True, stdin=None, executable="/bin/bash")
        ovs5Proc.wait()
        ovs6Proc = subprocess.Popen('make && make install', shell=True, stdin=None, executable="/bin/bash")
        ovs6Proc.wait()
        ovs7Proc = subprocess.Popen('insmod datapath/linux/openvswitch.ko', shell=True, stdin=None, executable="/bin/bash")
        ovs7Proc.wait()
        ovs8Proc = subprocess.Popen('insmod datapath/linux/brcompat.ko', shell=True, stdin=None, executable="/bin/bash")
        ovs8Proc.wait()
        ovs9Proc = subprocess.Popen('mkdir -p /usr/local/etc/openvswitch', shell=True, stdin=None, executable="/bin/bash")
        ovs9Proc.wait()
        ovs10Proc = subprocess.Popen('ovsdb-tool create /usr/local/etc/openvswitch/conf.db vswitchd/vswitch.ovsschema', shell=True, stdin=None, executable="/bin/bash")
        ovs10Proc.wait()
        ovs11Proc = subprocess.Popen("""ovsdb-server /usr/local/etc/openvswitch/conf.db \
--remote=punix:/usr/local/var/run/openvswitch/db.sock \
--remote=db:Open_vSwitch,manager_options \
--private-key=db:SSL,private_key \
--certificate=db:SSL,certificate \
--bootstrap-ca-cert=db:SSL,ca_cert --pidfile --detach --log-file""", shell=True, stdin=None, executable="/bin/bash")
        ovs11Proc.wait()
        ovs12Proc = subprocess.Popen('ovs-vsctl --no-wait init', shell=True, stdin=None, executable="/bin/bash")
        ovs12Proc.wait()
        ovs13Proc = subprocess.Popen('ovs-vswitchd --pidfile --detach', shell=True, stdin=None, executable="/bin/bash")
        ovs13Proc.wait()
        os.chdir("../")

def ovsVXinst():
    #Download and compile the VXLan OpenvSwitch unless a directory name ovs-vxlan exists.
    if os.path.exists('ovs-vxlan'):
        print('It appears you already have cloned ovs-vxlan, skipping the clone')
    if not os.path.exists('ovs-vxlan'):
        print('Cloning OVS from GitHub and then compiling the code, may take a few minutes...')
        ovs0Proc = subprocess.Popen("""apt-get install -y git python-simplejson python-qt4 python-twisted-conch automake autoconf 
gcc uml-utilities libtool build-essential git pkg-config linux-headers-`uname -r`""", shell=True, stdin=None, executable="/bin/bash")
        ovs0Proc.wait()
        ovs1Proc = subprocess.Popen('apt-get install -y openvswitch-controller', shell=True, stdin=None, executable="/bin/bash")
        ovs1Proc.wait()
        ovs2Proc = subprocess.Popen('git clone https://github.com/mestery/ovs-vxlan.git', shell=True, stdin=None, executable="/bin/bash")
        ovs2Proc.wait()
        os.chdir("ovs-vxlan")
        ovs3Proc = subprocess.Popen('git checkout vxlan', shell=True, stdin=None, executable="/bin/bash")
        ovs3Proc.wait()
        ovs4Proc = subprocess.Popen('./boot.sh', shell=True, stdin=None, executable="/bin/bash")
        ovs4Proc.wait()
        ovs5Proc = subprocess.Popen('./configure --with-linux=/lib/modules/`uname -r`/build', shell=True, stdin=None, executable="/bin/bash")
        ovs5Proc.wait()
        ovs6Proc = subprocess.Popen('make && make install', shell=True, stdin=None, executable="/bin/bash")
        ovs6Proc.wait()
        ovs7Proc = subprocess.Popen('insmod datapath/linux/openvswitch.ko', shell=True, stdin=None, executable="/bin/bash")
        ovs7Proc.wait()
        ovs8Proc = subprocess.Popen('insmod datapath/linux/brcompat.ko', shell=True, stdin=None, executable="/bin/bash")
        ovs8Proc.wait()
        ovs9Proc = subprocess.Popen('mkdir -p /usr/local/etc/openvswitch', shell=True, stdin=None, executable="/bin/bash")
        ovs9Proc.wait()
        ovs10Proc = subprocess.Popen('ovsdb-tool create /usr/local/etc/openvswitch/conf.db vswitchd/vswitch.ovsschema', shell=True, stdin=None, executable="/bin/bash")
        ovs10Proc.wait()
        ovs11Proc = subprocess.Popen("""ovsdb-server /usr/local/etc/openvswitch/conf.db \
--remote=punix:/usr/local/var/run/openvswitch/db.sock \
--remote=db:Open_vSwitch,manager_options \
--private-key=db:SSL,private_key \
--certificate=db:SSL,certificate \
--bootstrap-ca-cert=db:SSL,ca_cert --pidfile --detach --log-file""", shell=True, stdin=None, executable="/bin/bash")
        ovs11Proc.wait()
        ovs12Proc = subprocess.Popen('ovs-vsctl --no-wait init', shell=True, stdin=None, executable="/bin/bash")
        ovs12Proc.wait()
        ovs13Proc = subprocess.Popen('ovs-vswitchd --pidfile --detach', shell=True, stdin=None, executable="/bin/bash")
        ovs13Proc.wait()
        os.chdir("../")

def OVSinstOF():
    #Download and compile the VXLan OpenvSwitch unless a directory name ovs-vxlan exists.
    if os.path.exists('ovs-vxlan'):
        print('It appears you already have cloned ovs-vxlan, skipping the clone')
    if not os.path.exists('ovs-vxlan'):
        print('Cloning OVS from GitHub and then compiling the code, may take a few minutes...')
        ovsf1Proc = subprocess.Popen("""apt-get install -y git python-simplejson python-qt4 python-twisted-conch automake autoconf 
gcc uml-utilities libtool build-essential git pkg-config linux-headers-`uname -r`""", shell=True, stdin=None, executable="/bin/bash")
        ovsf1Proc.wait()
        ovsf2Proc = subprocess.Popen('git clone https://github.com/mestery/ovs-vxlan.git', shell=True, stdin=None, executable="/bin/bash")
        ovsf2Proc.wait()
        os.chdir("ovs-vxlan")
        ovsf3Proc = subprocess.Popen('git checkout vxlan', shell=True, stdin=None, executable="/bin/bash")
        ovsf3Proc.wait()
        ovsf4Proc = subprocess.Popen('./boot.sh', shell=True, stdin=None, executable="/bin/bash")
        ovsf4Proc.wait()
        ovsf5Proc = subprocess.Popen('./configure --with-linux=/lib/modules/`uname -r`/build', shell=True, stdin=None, executable="/bin/bash")
        ovsf5Proc.wait()
        ovsf6Proc = subprocess.Popen('make && make install', shell=True, stdin=None, executable="/bin/bash")
        ovsf6Proc.wait()
        ovsf7Proc = subprocess.Popen('insmod datapath/linux/openvswitch.ko', shell=True, stdin=None, executable="/bin/bash")
        ovsf7Proc.wait()
        ovsf8Proc = subprocess.Popen('insmod datapath/linux/brcompat.ko', shell=True, stdin=None, executable="/bin/bash")
        ovsf8Proc.wait()
        ovsf9Proc = subprocess.Popen('mkdir -p /usr/local/etc/openvswitch', shell=True, stdin=None, executable="/bin/bash")
        ovsf9Proc.wait()
        ovsf10Proc = subprocess.Popen('ovsdb-tool create /usr/local/etc/openvswitch/conf.db vswitchd/vswitch.ovsschema', shell=True, stdin=None, executable="/bin/bash")
        ovsf10Proc.wait()
        ovsf11Proc = subprocess.Popen("""ovsdb-server /usr/local/etc/openvswitch/conf.db \
--remote=punix:/usr/local/var/run/openvswitch/db.sock \
--remote=db:Open_vSwitch,manager_options \
--private-key=db:SSL,private_key \
--certificate=db:SSL,certificate \
--bootstrap-ca-cert=db:SSL,ca_cert --pidfile --detach --log-file""", shell=True, stdin=None, executable="/bin/bash")
        ovsf11Proc.wait()
        ovsf12Proc = subprocess.Popen('ovs-vsctl --no-wait init', shell=True, stdin=None, executable="/bin/bash")
        ovsf12Proc.wait()
        ovsf13Proc = subprocess.Popen('ovs-vswitchd --pidfile --detach', shell=True, stdin=None, executable="/bin/bash")
        ovsf13Proc.wait()
        os.chdir("../")

def images():
    img = ('linux-0.2.img')
    print('Checking if the Host Linux Image ' + img + ' exists')
    if os.path.exists(img):
        print(img + ' is already in the current working directory, delete if a partial download\n')
    else:
        print('Downloading ' + img + ' from http://wiki.qemu.org/Testing approximately 8Mb')
        lnxDlProc = subprocess.Popen('wget http://wiki.qemu.org/download/linux-0.2.img.bz2', shell=True, stdin=None, executable="/bin/bash")
        lnxDlProc.wait()
        bunzipProc = subprocess.Popen('bunzip2 linux-0.2.img.bz2', shell=True, stdin=None, executable="/bin/bash")
        bunzipProc.wait()
    
def etcifup():
    print('Adding OVS interface script /etc/ovs-ifup')
    fhup = ('/etc/ovs-ifup')
    if os.path.exists(fhup):
        print('file /etc/ovs-ifup exists skipping')
    else:
        print ('Adding /etc/ovs-ifup')
        ovsup = ("""#!/bin/sh
switch='br-int'
/sbin/ifconfig $1 0.0.0.0 up promisc
ovs-vsctl add-port ${switch} $1""")
        ovsupf = open('/etc/ovs-ifup', 'w')
        ovsupf.write(ovsup)
        ovsupf.close()
        os.chmod('/etc/ovs-ifup', 0755)

def etcifdown():
    print('Adding OVS interface script /etc/ovs-ifdown')
    fhdown = ('/etc/ovs-ifdown')
    if os.path.exists(fhdown):
        print('file /etc/ovs-ifdown exists skipping')
    else:
        print ('Adding /etc/ovs-ifdown')
        ovsdown = ("""#!/bin/sh
switch='br-int'
/sbin/ifconfig $1 0.0.0.0 down
ovs-vsctl del-port ${switch} $1""")
        ovsdownf = open('/etc/ovs-ifdown', 'w')
        ovsdownf.write(ovsdown)
        ovsdownf.close()
        os.chmod('/etc/ovs-ifdown', 0755)

def OVSconf():
    print('Adding an OpenvSwitch bridged interface br-int')
    ovsCnf1Proc = subprocess.Popen('ovs-vsctl add-br br-int', shell=True, stdin=None, executable="/bin/bash")
    ovsCnf1Proc.wait()
    ovsCnf2Proc = subprocess.Popen('ovs-vsctl add-port br-int eth0', shell=True, stdin=None, executable="/bin/bash")
    ovsCnf2Proc.wait()
    
def ovsOFconf(strIP):
    print('Adding an OpenvSwitch bridged interface br-int and Attaching to an OF Controller')
    ovsOFconf1Proc = subprocess.Popen('sudo ovs-vsctl add-br br-int', shell=True, stdin=None, executable="/bin/bash")
    ovsOFconf1Proc.wait()
    ovsOFconf2Proc = subprocess.Popen('sudo ovs-vsctl add-port br-int eth0', shell=True, stdin=None, executable="/bin/bash")
    ovsOFconf2Proc.wait()
    ovsOFconf3Proc = subprocess.Popen('sudo ovs-vsctl set-controller br-int tcp:' + strIP + ':6633', shell=True, stdin=None, executable="/bin/bash")
    ovsOFconf3Proc.wait()

def IPaddrs(strGW, strIP, strNetMask):
    print ('Moving Default Gateway to use (br-int) using --> ' + strGW)
    print ('Moving IP address on Eth0 to (br-int) for OpenvSwitch to use --> ' +strIP)
    ipbrProc = subprocess.Popen('ifconfig br-int ' + strIP + ' netmask 255.255.255.0', shell=True, stdin=None, executable="/bin/bash")
    ipbrProc.wait()
    gwProc = subprocess.Popen('route add default gw ' + strGW + ' br-int', shell=True, stdin=None, executable="/bin/bash")
    gwProc.wait()
    ipdelProc = subprocess.Popen('ifconfig eth0 0', shell=True, stdin=None, executable="/bin/bash")
    ipdelProc.wait()

def floodlight():
    imgfl = ('floodlight.jar')
    jreProc = subprocess.Popen('apt-get install -y default-jre python-dev curl', shell=True, stdin=None, executable="/bin/bash")
    jreProc.wait()
    if os.path.exists(imgfl):
        print('It appears you already have already downloaded floodlight.jar')
        print(imgfl + ' is already in the current working directory\n redownload or delete if a partial download now Installing deps..')
        devnull = open('/dev/null', 'w')
        subprocess.Popen('xterm -e java -jar floodlight.jar  & > /dev/null', shell=True, stdin=None, stderr=devnull, executable="/bin/bash")
        devnull.close()
        print('Floodlight OpenFlow Controller Started in a new Xterm console')
    if not os.path.exists(imgfl):
        print('Cloning OVS from GitHub and then compiling the code, may take a few minutes...')
        print('Installing openjdk6 and cloning Floodlight from GitHub')
        gitflProc = subprocess.Popen('wget http://floodlight.openflowhub.org/files/floodlight.jar', shell=True, stdin=None, executable="/bin/bash")
        gitflProc.wait()
        devnull = open('/dev/null', 'w')
        subprocess.Popen('xterm -e java -jar floodlight.jar  & > /dev/null', shell=True, stdin=None, stderr=devnull, executable="/bin/bash")
        devnull.close()
        print('Floodlight OpenFlow Controller Started in a new Xterm console')
    
def pox():
        #Download and compile the VXLan OpenvSwitch unless a directory name ovs-vxlan exists.
    if os.path.exists('pox'):
        print('It appears you already have cloned POX, skipping the clone')
    if not os.path.exists('pox'):
        print('Cloning POX from GitHub and then compiling the code, may take a few minutes...')
        print('Pox requires Python 2.7 to run')
        gitPoxProc = subprocess.Popen('git clone http://github.com/noxrepo/pox', shell=True, stdin=None, executable="/bin/bash")
        gitPoxProc.wait()
        devnull = open('/dev/null', 'w')
        subprocess.Popen('xterm -e python pox/pox.py  forwarding.l2_learning web.webcore &', shell=True, stdin=None, stderr=devnull, executable="/bin/bash")
        devnull.close()
        print('POX OpenFlow Controller Started using the forwarding.l2_learning in a new Xterm console')  

def boot():
    print ('Installation complete! The text above has instructions, Happy Labbing!\nBooting a VM in 10 seconds. Press Control+C to abort.')
    time.sleep(15)
    devnull = open('/dev/null', 'w')
    gitPoxProc = subprocess.Popen('kvm -m 128 -net nic,macaddr=33:22:22:00:cc:01 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &', shell=True, stdin=None, stderr=devnull, executable="/bin/bash")
    devnull.close() 

def msgEof():
    print("""############################################################################
# Installation complete! Now start a VM or run the bash script in the post.#
############################################################################
# Copy and paste all three lines into the console from the SAME directory  #
# you installed the script from that has the downloaded "linux-0.2.img"    #
# image. Do this with in the Ubuntu GUI. Then in the window give it an     #
# address on your subnet and a default gateway in the VM that boots in the #
# QEMU window that pops up. Break out of the QEMU window inside VirtualBox #
# use alt + control + command a few times to free the mouse pointer.       #
# Example IP--> ** ifconfig eth0 192.168.1.20 netmask 255.255.255.0 **     #
# Example Default Gateway-->** route add default gateway 192.168.1.1 **    #
# To start a VM copy and paste this into the console                       #
############################################################################
#Use unique Mac addresses for hosts e.g. cc:10, cc:11 see details in post  #
############################################################################
Examples to copy and paste (Notice unique MAC addresses on each VM 01, 02, 03)
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:01 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:02 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:03 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
Booting one VM with a MAC address of AA:AA:12:34:56:78 as an example.
When it boots you give it an IP address and gatewat as explanined above.
Type 'ovs-vsctl show' to the the VNIC (tap0) and OVS configuration
################################################################################
# -More information about what you can do with this Lab at:                    #
# http://networkstatic.net/openflow-openvswitch-and-kvm-sdn-lab-installation-app/ #
# Comments at Twitters @networkstatic, Thanks- Brent Salisbury                 #
################################################################################""")

def floodEof(strIP):
    print("""############################################################################
# Installation complete! Now start a VM or run the bash script in the post.#
############################################################################
# Copy and paste all three lines into the console from the SAME directory  #
# you installed the script from that has the downloaded "linux-0.2.img"    #
# image. Do this with in the Ubuntu GUI. Then in the window give it an     #
# address on your subnet and a default gateway in the VM that boots in the #
# QEMU window that pops up. Break out of the QEMU window inside VirtualBox #
# use alt + control + command a few times to free the mouse pointer.       #
# Example IP--> **ifconfig eth0 192.168.1.20 netmask 255.255.255.0**       #
# Example Default Gateway-->**route add default gateway 192.168.1.1**      #
# To start a VM copy and paste this into the console                       #
############################################################################
#Use unique Mac addresses for hosts e.g. cc:10, cc:11 see details in post  #
############################################################################
Examples to copy and paste (Notice unique MAC addresses on each VM 01, 02, 03)
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:01 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:02 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:03 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
Booting one VM with a MAC address of AA:AA:12:34:56:78 as an example.
When it boots you give it an IP address and gatewat as explanined above.
Type 'ovs-vsctl show' to the the VNIC (tap0) and OVS configuration
############################################################################
# FloodLight Controller running at http://"""+strIP+""":8080/ui/index.html #
# Put the URL above in a web browser to see the web UI                     #
################################################################################
# -More information about what you can do with this Lab at:                    #
# http://networkstatic.net/openflow-openvswitch-and-kvm-sdn-lab-installation-app/ #
# Comments at Twitters @networkstatic, Thanks- Brent Salisbury                 #
################################################################################""")

def poxEof():
    print("""############################################################################
# Installation complete! Now start a VM or run the bash script in the post.#
############################################################################
# Copy and paste all three lines into the console from the SAME directory  #
# you installed the script from that has the downloaded "linux-0.2.img"    #
# image. Do this with in the Ubuntu GUI. Then in the window give it an     #
# address on your subnet and a default gateway in the VM that boots in the #
# QEMU window that pops up. Break out of the QEMU window inside VirtualBox #
# use alt + control + command a few times to free the mouse pointer.       #
# Example IP--> **ifconfig eth0 192.168.1.20 netmask 255.255.255.0**       #
# Example Default Gateway-->**route add default gateway 192.168.1.1**      #
# To start a VM copy and paste this into the console                       #
############################################################################
#Use unique Mac addresses for hosts e.g. cc:10, cc:11 see details in post  #
############################################################################
Examples to copy and paste (Notice unique MAC addresses on each VM 01, 02, 03)
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:01 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:02 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:03 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
Booting one VM with a MAC address of AA:AA:12:34:56:78 as an example.
When it boots you give it an IP address and gatewat as explanined above.
Type 'ovs-vsctl show' to the the VNIC (tap0) and OVS configuration
################################################################################
# -More information about what you can do with this Lab at:                    #
# http://networkstatic.net/openflow-and-openvswitch-sdn-lab-scripted-in-minutes#
# Comments at Twitters @networkstatic, Thanks- Brent Salisbury                 #
################################################################################""")

def vxEof():
    print("""############################################################################
# Installation complete! Now start a VM or run the bash script in the post.#
############################################################################
# Copy and paste all three lines into the console from the SAME directory  #
# you installed the script from that has the downloaded "linux-0.2.img"    #
# image. Do this with in the Ubuntu GUI. Then in the window give it an     #
# address on your subnet and a default gateway in the VM that boots in the #
# QEMU window that pops up. Break out of the QEMU window inside VirtualBox #
# use alt + control + command a few times to free the mouse pointer.       #
# Example IP--> **ifconfig eth0 192.168.1.20 netmask 255.255.255.0**       #
# Example Default Gateway-->**route add default gateway 192.168.1.1**      #
# To start a VM copy and paste this into the console                       #
############################################################################
#Use unique Mac addresses for hosts e.g. cc:10, cc:11 see details in post  #
############################################################################
Examples to copy and paste (Notice unique MAC addresses on each VM 01, 02, 03)
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:01 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:02 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
kvm -m 128 -net nic,macaddr=22:22:22:00:cc:03 -net tap,script=/etc/ovs-ifup,downscript=/etc/ovs-ifdown -hda linux-0.2.img &
Booting one VM with a MAC address of AA:AA:12:34:56:78 as an example.
When it boots you give it an IP address and gatewat as explanined above.
Type 'ovs-vsctl show' to the the VNIC (tap0) and OVS configuration
################################################################################
# -More information about what you can do with this Lab at:                    #
# http://networkstatic.net/openflow-openvswitch-and-kvm-sdn-lab-installation-app/ #
# Comments at Twitters @networkstatic, Thanks- Brent Salisbury                 #
################################################################################""")

def main():
    opt = input("""#####################################################################
# This is for lab and learning purposes only to simplify getting    #
# a lab to learn OpenFlow, OpenvSwitch and KVM. The usage is        #
# documented at http://networkstatic.net. I recommend doing these   #
# lab installations with a VM  snapshot to rollback to in           #
# case a setting doesnt fit your install. This will only work on    #
# Ubuntu Linux that has connectivity to the Internet.               #
# For the Impatient :) There are four install builds:               #
# 1) *Base install* KVM & OpenvSwitch, Git(hub), Test Kernel image. #
# 2) Base + FloodLight OpenFlow Controller (Java -Open Source).     #
# 3) Base + POX OpenFlow Controller (Python -Open Source).          #
# 4) Base + OpenvSwitch v1.8.90 with VXlan encapsulation support.   #
#####################################################################
# Press *1* to install the KVM & OpenvSwitch Lab:                   #
# Option 1 includes Git(GitHub), KVM, OpenvSwitch, a 16Mb           #
# test guest host image and configures OpenvSwitch for use.         #
# This will only run on *Ubuntu* since it uses apt-get for packages.#
# Run this from the command line in a VM. It will run on a          #
# physical host but will likely cut you off an SSH session since    #
# it changes your eth0 IP to the new OpenvSwitch br-int interface.  #
#####################################################################
# Press *2* for the base applications along with the Floodlight     #
# OpenFlow Controller. The controller and OpenvSwitch processes     #
# are started in the application and OpenvSwitch is attached.       #
#####################################################################
# Press *3* for the base applications along with the Floodlight     #
# OpenFlow Controller. The controller and OpenvSwitch processes     #
# are started in the application and OpenvSwitch is attached to     #
# the controller by the App.                                        #
#####################################################################
# Press *4* for the base applications with a developmentatl build   #
# of OpenvSwitch that includes the VXLan L2 encapsulation.          #
# This OVS build comes from Mestery at Cisco and Pfaff at Nacira    #
# and is getting pulled from GitHub. This option includes the       #
# OpenvSwitch OF controller with it.                                #
Here is a tutorial for configuring VXLan tunnels if you choose #4   #
http://networkstatic.net/configuring-vxlan-and-gre-tunnels-on-openvswitch/
#####################################################################
# At then end of the App one example VM is booted at the end of the # 
# program. If the inststall fails, tshoot and restore your orig VM  #
# Installation host does not support HW virtualization KVM defaults #
# to QEMU which is why it is nice using this small Linux Kernel     #
# since all we need for testing applications is something that has  #
# a client IP stack/functionality. Run the app as root e.g.         #
# "$sudo passwd root" set a passwd then "su" and 'python script.py' #
#####################################################################
# Labs that can be used when you have your VMs up can be found here:#
# http://networkstatic.net/openflow-starter-tutorial-lab-1/         #
# This works very well with VMware Fusion from my testing, I have   #
# seen some issues with VirtualBox talking outside of the VMs spun  #
# up, but you really just need the VMs talking to eachother with    #
# to do labs with an OpenFlow controller. VM Fusion is g2g tho. I   #
# havent tested on a Linux or Windows host yet but it should work   #
# fine on both as Python is cross platform goodness. Cheers! -Brent #
#####################################################################
"""'\nEnter Option 1, 2, 3 or 4 (Control+C to quit): ')
    print('')
    if opt == 1:
        print('Installing SDN Lab #1..\n')
        #Install Lab for KVM and OpenvSwitch testing.
        #Get the default gateway
        GW = subprocess.check_output("""route -n | grep 'UG[ \t]' | awk '{print $2}'""", shell=True)
        strGW = GW.strip()
        #Get the IP address bound to eth0 we will move this to br0
        IP = subprocess.check_output("""ifconfig eth0 | awk '/inet addr/ {split ($2,A,":"); print A[2]}'""", shell=True)
        strIP = IP.strip()
        Netmask = subprocess.check_output("""ifconfig eth0 | sed -rn '2s/ .*:(.*)$/\1/p'""", shell=True)
        strNetMask = Netmask.strip()
        git()
        kvm()
        OVSinst()
        images()
        etcifup()
        etcifdown()
        OVSconf()
        IPaddrs(strGW, strIP, strNetMask)
        msgEof()
        boot()
        
    elif opt == 2:
        #Install Lab w/FloodLight Controller OpenFlow along with KVM and OpenvSwitch
        print('Installing SDN Lab #2...\n')
        # the main code goes here
        #Get the default gateway
        GW = subprocess.check_output("""route -n | grep 'UG[ \t]' | awk '{print $2}'""", shell=True)
        strGW = GW.strip()
        #Get the IP address bound to eth0 we will move this to br0
        IP = subprocess.check_output("""ifconfig eth0 | awk '/inet addr/ {split ($2,A,":"); print A[2]}'""", shell=True)
        strIP = IP.strip()
        Netmask = subprocess.check_output("""ifconfig eth0 | sed -rn '2s/ .*:(.*)$/\1/p'""", shell=True)
        strNetMask = Netmask.strip()
        git()
        kvm()
        OVSinstOF()
        images()
        etcifup()
        etcifdown()
        ovsOFconf(strIP)
        IPaddrs(strGW, strIP, strNetMask)
        floodlight()
        floodEof(strIP)
        boot()
        
    elif opt == 3:
        #Install Lab w/POX Controller OpenFlow along with KVM and OpenvSwitch
        print('Installing SDN Lab #3...\n')
        # the main code goes here
        #Get the default gateway
        GW = subprocess.check_output("""route -n | grep 'UG[ \t]' | awk '{print $2}'""", shell=True)
        strGW = GW.strip()
        #Get the IP address bound to eth0 we will move this to br0
        IP = subprocess.check_output("""ifconfig eth0 | awk '/inet addr/ {split ($2,A,":"); print A[2]}'""", shell=True)
        strIP = IP.strip()
        Netmask = subprocess.check_output("""ifconfig eth0 | sed -rn '2s/ .*:(.*)$/\1/p'""", shell=True)
        strNetMask = Netmask.strip()
        git()
        kvm()
        OVSinstOF()
        ovsOFconf(strIP)
        images()
        etcifup()
        etcifdown()
        ovsOFconf(strIP)
        IPaddrs(strGW, strIP, strNetMask)
        pox()
        poxEof()
        boot()
    
    elif opt == 4:
        print('Installing SDN Lab #4..\n')
        #Install Lab for KVM and OpenvSwitch testing.
        #Get the default gateway
        GW = subprocess.check_output("""route -n | grep 'UG[ \t]' | awk '{print $2}'""", shell=True)
        strGW = GW.strip()
        #Get the IP address bound to eth0 we will move this to br0
        IP = subprocess.check_output("""ifconfig eth0 | awk '/inet addr/ {split ($2,A,":"); print A[2]}'""", shell=True)
        strIP = IP.strip()
        Netmask = subprocess.check_output("""ifconfig eth0 | sed -rn '2s/ .*:(.*)$/\1/p'""", shell=True)
        strNetMask = Netmask.strip()
        git()
        kvm()
        ovsVXinst()
        images()
        etcifup()
        etcifdown()
        OVSconf()
        IPaddrs(strGW, strIP, strNetMask)
        vxEof()
        boot()
        
    else:
        exit()


if __name__ == "__main__":
    main()



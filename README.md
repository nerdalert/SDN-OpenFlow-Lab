SDN-OpenFlow-Lab
================

OpenFlow, OpenvSwitch and KVM SDN Lab Installation App

Post with more information:
http://networkstatic.net/openflow-openvswitch-and-kvm-sdn-lab-installation-app/
Twitters @networkstatic or Brent Salisbury


 This installs OpenvSwitch, KVM, Git(Hub) and an OpenFlow    
 Controller FloodLight (optional). It also downloads a 16Mb  
 linux-0.2.img.bz2 file that from http://wiki.qemu.org that  
 is great for testing networking since it is so lightweight  
 you can simulate lots of VMs running in nested a hypervisors
 on your laptop or older desktop rather than needing a server
 for learning or labbing. This is for *Ubuntu* only since it 
 is using apt-get for pkg management.                        
 This is NOT for anything other than labbing and testing but 
 the KVM and OpenvSwitch install would run production easily.
 Feel free to use this however you like. Python is a great   
 language for infrastrcuture applications. It has clean      
 abstraction leaving it easy to read but also has the power  
 of object oriented programming. This wil install a fully    
 working Software Defined Networking (SDN) and OpenFlow      
 lab in a few minutes. See the accompanying post             
 I recommend starting in a VM using VMware Fusion as the     
 first option only becuase it seems to deal with OVS better  
 than VirtualBox but both work. I would also recommend using 
 snapshots heavily. Install your base Linux 12.04 build and  
 then take a snapshot in case you have problems with the     
 App you can rollback to the original snapshot and start over
 Comments at Twitters @networkstatic, Thanks-Brent Salisbury  


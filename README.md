# DexterRedTool
Author: Dexter Delandro
CSEC 473 - Spring 2022

This tool persistently creates users every minute on Windows and Linux Machines.

On Windows, the Ansible written will create a Windows Scheduled Task that will call the user-creating script every minute.
On Linux, the ansible will create a cron job that will call the user-creating script every minute.

To use the tool, all you need to do is run the corresponding ansible file. 
This means that if the target machine is Windows use the windows_createUsers folder,
but if the target machine is Linux, use the linux_createUsers folder.

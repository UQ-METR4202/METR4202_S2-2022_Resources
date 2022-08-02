# Instructions for using the VMDK on VirtualBox
- The following steps will guide you on how to set up the virtual machine that has ROS Noetic pre-
installed. This tutorial will assume that you have Virtualbox installed:
If you haven't installed it, you can go [here](https://www.virtualbox.org/wiki/Downloads)

# Steps for setting up the VM in VirtualBox
1. Install VM VirtualBox
2. Choose the settings for the Ubuntu VM
- **(a)**
Click new to create a new VM.

- **(b)**
Fill out the 'settings' dialog with the following:
  - Name: METR4202_VM (You can assign this any name) 
  - Machine Folder: (leave as default)
  - Type: Linux
  - Version: Ubuntu (64-bit)
- **(c)**
Click next.

- **(d)**
Allocate as much RAM as you would like.
  - Note: The recommended amount of RAM for a VM is typically less than *half* of the system memory.
E.g. for a typical modern laptop, 4 GB for the virtual and 4 GB for the host machine is fine.
You can locate the file with the green arrow symbol.

- **(e)**
The following screen will appear.
Click "Add".

- **(f)**
Add the supplied VMDK file (ROSUBUNTU 20.04) downloaded from [here](https://drive.google.com/file/d/1e6I4A24Sasa3JptdhnwxKrrS-176HNa)

- **(g)**
Then, select the VMDK file you just added and press "Choose".

- **(h)**
Complete the VM setup process by pressing "Create"

3. Launch the VM

- **(a)**
Click "Start" to launch the newly created VM.

- **(b)**
After Ubuntu boots up and loads the login screen, login with the password:
- Password: metr4202

[LvmMenu.py](./LvmMenu.py) is a python menu program for automating partitioning using **LVM**

## What is LVM?

Managing disk space has always been a significant task for sysadmins. Running out of disk space used to be the start of a long and complex series of tasks to increase the space available to a disk partition. It also required taking the system off-line. This usually involved installing a new hard drive, booting to recovery or single-user mode, creating a partition and a filesystem on the new hard drive, using temporary mount points to move the data from the too-small filesystem to the new, larger one, changing the content of the /etc/fstab file to reflect the correct device name for the new partition, and rebooting to remount the new filesystem on the correct mount point.

![alt text](https://miro.medium.com/max/268/1*McIB2KyIOmL-CYdABgl4dw.png "LVM")

LVM allows for very flexible disk space management. It provides features like the ability to add disk space to a logical volume and its filesystem while that filesystem is mounted and active ( Dynamically / ONLINE ) and it allows for the collection of multiple physical hard drives and partitions into a single volume group which can then be divided into logical volumes.

***

[LvmMenu.py](./LvmMenu.py) can do the following operations automatically for you:

- Create a Physical Volume
- Create a Volume Group
- Create a Logical Volume and mount it
- Display Physical Volume
- Display Volume Group
- Display Logical Volume
- Extend the size of a Logical Volume
- Reduce the size of a Logical Volume
- Add more Physical Volumes to Volume Group

***


Note: This program is written for RHEL8(RedHat Linux) as the Base Operating System. You can make slight changes (if needed) according to your Linux distro.

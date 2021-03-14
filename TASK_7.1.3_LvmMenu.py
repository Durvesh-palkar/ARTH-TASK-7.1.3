import os
from time import sleep
os.system("clear")
os.system("tput setaf 57")
print("*"*80)
os.system("tput setaf 9")
os.system("figlet -kc LVM-MENU -f small")
os.system("tput setaf 57")
print("*"*80)

while True:
    os.system("tput setaf 10")
    print("\n\tPRESS:")
    print("\t\t1. To create a Physical Volume")
    print("\t\t2. To create a Volume Group")
    print("\t\t3. To create a Logical Volume and mount it")
    print("\t\t4. To display Physical Volume")
    print("\t\t5. To display Volume Group")
    print("\t\t6. To display Logical Volume")
    print("\t\t7. To extend the size of a Logical Volume")
    print("\t\t8. To reduce the size of a Logical Volume")
    print("\t\t9. To add more Physical Volumes to Volume Group")
    print("\t\t0. To exit")
    #os.system("tput setaf 11")

    ch = int(input("\n\nEnter your choice: "))

    #create PV
    if ch == 1:
        os.system("tput setaf 3")
        print("\n\n","-"*28,"CreatingPV","-"*28,"\n")
        #n = input("Enter the number of PVs you want to create: ")
        print("Displaying all the devices for your reference...\n\n")
        sleep(2)
        os.system("tput setaf 15")
        os.system("fdisk -l")
        os.system("tput setaf 51")
        devs = input("\n\nEnter the device names (space separated) from which you want to create PVs: ")
        os.system("tput setaf 15")
        os.system("pvcreate {}".format(devs))
        
        os.system("tput setaf 3")
        print("\n","-"*80,"\n")

    #create VG
    if ch == 2:
        os.system("tput setaf 3")
        print("\n\n","-"*28,"CreatingVG","-"*28,"\n")
        os.system("tput setaf 51")
        vgName = input("Enter a name for this VG: ")
        dev = input("Enter the PV names (space separated) from which you want to create a VG: ")
        os.system("tput setaf 15")
        os.system("vgcreate {} {}".format(vgName, dev))
        
        os.system("tput setaf 3")
        print("\n","-"*80,"\n")

    #create LV
    if ch == 3:
        os.system("tput setaf 3")
        print("\n\n","-"*28,"CreatingLV","-"*28,"\n")
        os.system("tput setaf 51")
        lvName = input("Enter a name for this LV: ")
        size = input("Enter the size(in GiB) of LV: ")
        vgName = input("Enter the VG name from which you wish to create this LV: ")
        os.system("tput setaf 15")
        os.system("lvcreate --size {}G --name {} {}".format(size, lvName, vgName)) 

        print("\n\nFormatting LV using mkfs")
        os.system("mkfs.ext4 /dev/{}/{}".format(vgName, lvName))
        os.system("tput setaf 10")
        print("\n\tPress:")
        print("\n\t\t1. to create a directory for mounting this PV")
        print("\n\t\t2. to continue")
        #os.system("tput setaf 11")
        c = input("\nEnter your choice: ")
        os.system("tput setaf 51")
        if c == '1':
            mountPath = input("Enter the directory name (along with full path) for mounting this LV: ")
            os.system("tput setaf 15")
            os.system("mkdir {}".format(mountPath))
        if c == '2':    
            os.system("tput setaf 51")
            mountPath = input("\nEnter the mount path: ")
        os.system("tput setaf 15")
        s = os.system("mount /dev/{}/{} {}".format(vgName, lvName, mountPath))
        if s == 0:
            os.system("tput setaf 2")
            print("\nLV created and Mounted Successfully!! ")
        os.system("tput setaf 3")
        print("\n","-"*80,"\n")

    #display PV
    if ch == 4:
        os.system("tput setaf 3")
        print("\n\n","-"*28,"DisplayingPV","-"*28,"\n")
        os.system("tput setaf 10")
        print("\n\tEnter:")
        print("\n\t\t1. for displaying all PVs")
        print("\n\t\t2. for displaying a specific PV\n")
        #os.system("tput setaf 11")
        c = input("Enter your choice: ")
        if c == '1':
            os.system("tput setaf 15")
            os.system("pvdisplay")
        else:
            os.system("tput setaf 51")
            pvName = input("Enter the name of PV to be displayed: ")
            os.system("tput setaf 15")
            os.system("pvdisplay {}".format(pvName))

        os.system("tput setaf 3")
        print("\n","-"*80,"\n")
        sleep(4)

    #display VG
    if ch == 5:
        os.system("tput setaf 3")
        print("\n\n","-"*28,"DisplayingVG","-"*28,"\n")
        os.system("tput setaf 10")
        print("\n\tEnter:")
        print("\n\t\t1. for displaying all VGs")
        print("\n\t\t2. for displaying a specific VG\n")
        #os.system("tput setaf 11")
        c = input("Enter your choice: ")
        os.system("tput setaf 15")
        if c == '1':
            os.system("vgdisplay")
        else:
            os.system("tput setaf 51")
            vgName = input("Enter the name of VG to be displayed: ")
            os.system("tput setaf 15")
            os.system("vgdisplay {}".format(vgName))
        sleep(4)
        os.system("tput setaf 3")
        print("\n","-"*80,"\n")

    #display LV
    if ch == 6:
        os.system("tput setaf 3")
        print("\n\n","-"*28,"DisplayingLV","-"*28,"\n")
        os.system("tput setaf 10")
        print("\n\tEnter:")
        print("\n\t\t1. for displaying all LVs")
        print("\n\t\t2. for displaying a specific LV\n")
        #os.system("tput setaf 11")
        c = input("Enter your choice: ")
        os.system("tput setaf 15")
        if c == '1':
            os.system("lvdisplay")
        else:
            os.system("tput setaf 51")
            lvName = input("Enter the name of LV to be displayed: ")
            vgName = input("Please also provide the corresponding VG name: ")
            os.system("tput setaf 15")
            os.system("lvdisplay {}/{}".format(vgName, lvName))
        sleep(4)
        os.system("tput setaf 3")
        print("\n","-"*80,"\n")

    #extendLV
    if ch == 7:
        os.system("tput setaf 3")
        print("\n\n","-"*28,"ExtendingLV","-"*28,"\n")
        os.system("tput setaf 51")
        ilvName = input("Enter the name of LV you wish to extend: ")
        vgName = input("Please also provide the corresponding VG name: ")
        os.system("tput setaf 15")
        print("Please ensure that you have appropriate size available in vg: {}".format(vgName))
        os.system("tput setaf 51")
        size = input("Enter the size (in GiB) by which you want to extend LV : ")
        os.system("tput setaf 15")
        os.system("lvextend --size +{}G /dev/{}/{}".format(size, vgName, lvName))
        os.system("resize2fs /dev/{}/{}".format(vgName, lvName))
        os.system("tput setaf 3")
        print("\n","-"*80,"\n")

    #reduceLV
    if ch == 8:
        os.system("tput setaf 3")
        print("\n\n","-"*28,"ReducingLV","-"*28,"\n")
        os.system("tput setaf 51")
        lvName = input("Enter the name of LV you wish to reduce: ")
        vgName = input("Please also provide the corresponding VG name: ")
        size = input("Enter the new (reduced) size of the LV you want (in GiB): ")
        dirPath = input("Enter the directory path on which {} is mounted: ".format(lvName))
        os.system("tput setaf 15")
        os.system("umount {}".format(dirPath))
        os.system("e2fsck -f /dev/{}/{}".format(vgName, lvName))
        os.system("resize2fs /dev/{}/{} {}G".format(vgName, lvName, size))
        os.system("lvreduce --size {}G /dev/{}/{}".format(size, vgName, lvName))
        os.system("mount /dev/{}/{} {}".format(vgName, lvName,dirPath))
        os.system("tput setaf 3")
        print("\n","-"*80,"\n")

    #extendVG
    if ch == 9:
        os.system("tput setaf 3")
        print("\n\n","-"*28,"ExtendingVG","-"*28,"\n")
        os.system("tput setaf 51")
        vgName = input("Enter the name of VG  you wish to extend: ")
        pvName = input("Enter the PV names (space separated) from which you want to extend this VG: ")
        os.system("tput setaf 15")
        os.system("vgextend {} {}".format(vgName, pvName))
        os.system("tput setaf 3")
        print("\n","-"*80,"\n")
   
    #exit
    if ch == 0: 
        os.system("tput setaf 15")
        exit()



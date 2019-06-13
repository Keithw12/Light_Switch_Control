#Created on Tue Apr  9 14:23:59 2019
#
#@author: Keith Wilcox
#         w976985


lights = 0b00000000
while True:
    mask = 0b1
    print()
    print("Options:")
    print("   1 - Show Status of All Light")
    print("   2 - Show Status of a Single Light")
    print("   3 - Turn ON  ALL Lights")
    print("   4 - Turn OFF ALL Lights")
    print("   5 - Turn ON  a single light")
    print("   6 - Turn OFF a single light")
    print("   7 - Toggle a single light (ON >> OFF ..OR.. OFF >> ON)")
    print("   q - Quit")
    print()
    ans = input("Select option? ")
    print()

    if ans == "q":
        break

    if not (ans in [ "1", "2", "3", "4", "5", "6", "7"]):
        print("Invalid option, select 1, 2, 3, 4, 5, 6, 7, or q")
        continue

    if ans == "1":
        print("Light Number","7","6","5","4","3","2","1","0",sep="  |  ",end="  |\n")
        print("--------------","-----","-----","-----","-----","-----","-----","-----","-----",sep="|",end="|\n")
        print("Status       ",end=" | ")
        mask = 0b10000000
        for i in range(8):
            if lights & mask:
                print("ON ",end=" | ")
            else:
                print("OFF",end=" | ")
            mask >>= 1
        print()
        continue

    if ans == "2":
        lightnum = int(input("Enter light number to use (0-7)? "))
        if lightnum > 7 or lightnum < 0:
            print("Needs to be a light between 0-7")
            continue
        
        for i in range(lightnum):
            mask <<= 1
        
        if lights & mask:
            print("Light",lightnum,"set ON")
        else:
            print("Light",lightnum,"set OFF")
            
        continue

    if ans == "3":
        lights = 0b11111111
        print("ALL Lights Turned ON")
        continue

    if ans == "4":
        lights = 0b00000000
        print("ALL Lights Turned OFF")
        continue
    
    if ans == "5":
        lightnum = int(input("Enter light number to turn on (0-7)? "))
        if lightnum > 7 or lightnum < 0:
            print("Needs to be a light between 0-7")
            continue
        
        for i in range(lightnum):
            mask <<= 1
        
        lights |= mask
        print("Light",lightnum,"set ON")
        continue
    
    if ans == "6":
        lightnum = int(input("Enter light number to turn off (0-7)? "))
        if lightnum > 7 or lightnum < 0:
            print("Needs to be a light between 0-7")
            continue
        
        for i in range(lightnum):
            mask <<= 1
        
        lights &= ~mask
        print("Light",lightnum,"set OFF")
        continue
    
    if ans == "7":
        lightnum = int(input("Enter light number to toggle (0-7)? "))
        if lightnum > 7 or lightnum < 0:
            print("Needs to be a light between 0-7")
            continue
        
        for i in range(lightnum):
            mask <<= 1
        
        lights ^= mask
        
        if lights & mask:
            print("Light",lightnum,"toggle ON")
        else:
            print("Light",lightnum,"toggle OFF")
        continue

print("That's All Folks!")
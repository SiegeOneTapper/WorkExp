import random
systwo = list(range(1, 12 + 1))
sysone = list(range(1, 12 + 1))
sysshrimp = list(range(1, 20 + 1))
sysmain = list(range(1, 24 + 1))
#RandomNumberGenerator

print("Systems: sysmain, sysone, systwo, sysshrimp \n Makre sure all system names are entered in lowercase")
systemChoice = input("Enter name of the system: ")
noFeed = input("Enter number of feed: ")

if systemChoice == "sysmain":
    sysmain2 = sysmain
    listLen = len(sysmain2) / int(noFeed)
    for i in range(int(noFeed)):
        numbers = random.sample(sysmain2,int(listLen))
        print(numbers)
        for k in numbers:
            sysmain2.remove(k)
elif systemChoice == "sysone":
    sysone2 = sysone
    listLen = len(sysone2) / int(noFeed)
    for i in range(int(noFeed)):
        numbers = random.sample(sysone2,int(listLen))
        print(numbers)
        for k in numbers:
            sysone2.remove(k)
elif systemChoice == "systwo":
    systwo2 = systwo
    listLen = len(systwo2) / int(noFeed)
    for i in range(int(noFeed)):
        numbers = random.sample(systwo2,int(listLen))
        print(numbers)
        for k in numbers:
            systwo2.remove(k)
elif systemChoice == "sysshrimp":
    sysshrimp2 = sysshrimp
    listLen = len(sysshrimp2) / int(noFeed)
    for i in range(int(noFeed)):
        numbers = random.sample(sysshrimp2,int(listLen))
        print(numbers)
        for k in numbers:
            sysshrimp2.remove(k)

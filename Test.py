
import os
import sys
import time

from source import *


PORT=25565
cores = ''
versions = ''
selectCoreCorrect = False
selectVersionCorrect = False
downloadSuccess = False

with open('Welcome','r',encoding = "UTF-8") as f:
    lines=f.readlines()
    for line in lines:
        print(line,end='')

#login 
print('')
print('Press "Enter" to continue... ')
input()
os.system('clear')
print('='*40)
print('Checking java version...')
os.system("java -version 2>&1 | awk -F[\\\"_] 'NR==1{print $2}'")
print('-'*40)

#core
print('Minecraft Server Core lists:')
while(not selectCoreCorrect):

    for core in source.keys():
        print('-   '+core)

    print('Please select a Minecraft Server Core:',end=' ')
    cores = input().strip()
    if cores in source.keys():
        selectCoreCorrect = True


#version

os.system('clear')
print("Minecraft-"+cores+'-'+(versions if versions!='' else '?')+'.')
print('------------------------------')

print(cores + ' is selected!\n')
print('Minecraft version lists:')
while(not selectVersionCorrect):

    for version in source[cores].keys():
        print('-    '+version)

    print('Please select a Minecraft version:',end=' ')
    versions = input().strip()
    if versions in source[cores].keys():
        selectVersionCorrect = True
        


#channel
os.system('clear')
print("Minecraft-"+cores+'-'+(versions if versions!='' else '?')+'.')
print('------------------------------')
print('We provide cpolar channel though you need to get token on https://www.cpolar.com/.')
print('Create a channel (y/n): ', end='')
createChannel = False if input() == 'n' else True
if createChannel:
    print('Enter your cpolar token (Empty if already setted): ',end='')
    token = input()
    print()
    
    if token!='':
        os.system('cpolar authtoken ' + token.strip())


    # os.system('rm -rf ./cpolar')
    
    cmd = 'cpolar tcp 25565 -log=stdout | grep --color=auto -m 1 "1.tcp.cpolar.cn:"'
    # cmd = 'cpolar tcp '+str(PORT)+' -log="./cpolar/cpolar.log" &'
    os.system(cmd)
    # time.sleep(5)
    print('Coppy the following sockets and Press "Enter" to continue.')
    
    input()


#download
os.system('clear')
print("Minecraft-"+cores+'-'+(versions if versions!='' else '?')+'.')
print('------------------------------')

print(versions + ' is selected!\n')


while(not downloadSuccess):
    # os.system('rm -rf ./LocalServer')
    # os.system('mkdir LocalServer')
    os.system('wget '+source[cores][versions] + ' -O ./LocalServer/server.jar')
    print(os.listdir(os.getcwd() + '/LocalServer'))

    if 'server.jar' in os.listdir(os.getcwd() + '/LocalServer'):
        downloadSuccess = True
        print('Download Success!!')
        # input()
        break
    else:
        print('Download Failed ~')
        print('You can:\n1.Retry\n2.Exit\n----')
        choice = input().strip()
        if choice == 'Exit' or choice == '2':
            exit()


#install 
os.system('clear')
os.chdir(os.getcwd()+'/LocalServer')
print("Minecraft-"+cores+'-'+(versions if versions!='' else '?')+'.')
print('------------------------------')
print('set RAM? (y/n) ',end='')
choice = input()
if choice == 'y':
    maxRAM = -1
    minRAM = -1
    try:
        print('Set Memory MB.')
        print('Max RAM: ',end='')
        maxRAM = int(input())
        print('\nMin RAM: ',end='')
        minRAM = int(input())
        print()
        if maxRAM >= minRAM:
            os.system('java -Xmx'+maxRAM+'M -Xms'+minRAM+'M -jar server.jar nogui')
        else:
            print('parameter error using default')
            os.system('java -jar server.jar nogui')
    except:
        print('parameter error using default')
        os.system('java -jar server.jar nogui')
else:
    os.system('java -jar server.jar nogui')



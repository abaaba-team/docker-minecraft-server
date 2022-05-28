from asyncio import FastChildWatcher
import os



source = {
    'Vanila':'',
    'Mohist':{
        '1.7.10':'https://mohistmc.com/builds/1.7.10/Mohist-1.7.10-46-server.jar',
        '1.12.2':'https://mohistmc.com/builds/1.12.2/mohist-1.12.2-321-server.jar',
        '1.16.5':'https://mohistmc.com/builds/1.16.5/mohist-1.16.5-1008-server.jar',
        '1.18.2':'https://mohistmc.com/builds/1.18.2-testing/mohist-1.18.2-40.1.25-47-installer.jar'
    }
}
cores = ''
versions = ''
selectCoreCorrect = False
selectVersionCorrect = False

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
    cores = input()
    if cores in source.keys():
        selectCoreCorrect = True

os.system('clear')

print(cores + ' is selected!\n')

#version
print('Minecraft version lists:')
while(not selectVersionCorrect):

    for version in source[cores].keys():
        print('-    '+version)

    print('Please select a Minecraft version:',end=' ')
    versions = input()
    if versions in source[cores].keys():
        selectVersionCorrect = True

os.system('clear')
print(versions + ' is selected!\n')

#download
os.system('wget '+source[cores][versions])

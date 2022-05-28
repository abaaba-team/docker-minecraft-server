import os

with open('Welcome','r',encoding = "UTF-8") as f:
    lines=f.readlines()
    for line in lines:
        print(line,end='')
print('')
print('Press "Enter" to continue... ')
input('')
os.system('clear')
print('='*40)
print('Checking java version...')
os.system("java -version 2>&1 | awk -F[\\\"_] 'NR==1{print $2}'")
print('-'*40)
print('Please select a Minecraft version:')



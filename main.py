import os

def open_():
    current = os.listdir()
    for i,j in enumerate(current,1):
        print(i,j)
    x = int(input('Open Enter to continue :'))
    try:
        with open(str(current[x-1]),'r') as f:
            f.read()
            print(f)
    except:
        print('ERROR!!')
    finally:
        f.close()

def file(): 
    current = os.listdir()
    for i,j in enumerate(current):
        print(i,j)
    input('Enter to continue ...')

def new_dir():
    x = int(input('1 New Dir \r\n2 New File\r\nEnter option : '))
    if x == 1:
        n = str(input('Enter name : '))
        os.mkdir(n)
    elif x == 2:
        n = str(input('Enter name : '))
        f = open(n,'x')
        f.close()
    input('Enter to continue ...')

def move():    
    file = os.listdir()
    for i,j in enumerate(file,1):
        print(i,j)
    x = int(input('Select file to move : '))
    for i,j in enumerate(file,1):
        print(i,j)
    
    n = int(input('Move file to : '))
    y = str(input('Move {} to {} Enter (y) to continue :'.format(file[x-1],file[n-1])))
    if x == 'Y' or 'y':
        try:
            os.rename(str(file[x-1]),str(file[n-1])+"\\"+str(file[x-1]))
        except:
            print('ERROR !!! ')
    input('Enter to continue ...')


def ch_dir():     
    file = os.listdir()
    for i,j in enumerate(file,1):
        print(i,j)
    print(len(file)+1,'Go back')
    file.append('..')
    x = int(input('Select file : '))
    input('Move to {} Enter to continue :'.format(file[x-1]))
    try:
        os.chdir(str(file[x-1]))
    except:
        print('ERROR !!! ')

def rename():   
    file = os.listdir()
    for i,j in enumerate(file,1):
        print(i,j)
    x = int(input('Select file : '))
    n = str(input('Enter file name : '))
    y = str(input('Rename {} to {} Enter (y) to continue :'.format(file[x-1],n)))
    if x == 'Y' or 'y':
        try:
            os.rename(str(file[x-1]),n)
        except:
            print('ERROR !!! ')
    input('Enter to continue ...')

def remove():   
    file = os.listdir()
    for i,j in enumerate(file,1):
        print(i,j)
    x = int(input('Select file : '))
    y = str(input('Remove {} Enter (y) to continue :'.format(file[x-1])))
    if x == 'Y' or 'y':
        os.remove(str(file[x-1]))
    input('Enter to continue ...')

def main():
    option = ['Get file name','Chang Dir','Remove File','Rename File','Move File','New File/Dir','Open File']
    while(True):      
        print('Current Path : ',os.getcwd())
        for i,j in enumerate(option):
            print(i,j)
        x = int(input('Enter option : '))
        if x < 0 or x > 6:
            break
        elif x == 0:
            file()
        elif x == 1:
            ch_dir()
        elif x == 2:
            remove()
        elif x == 3:
            rename()
        elif x == 4:
            move()
        elif x == 5:
            new_dir()
        elif x == 6:
            open_()
        
main()
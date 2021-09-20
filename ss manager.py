import os

print('''
==================
==  SS Manager  ==
==================
''')

def exit_():
    os.system(r'move "C:\Users\Yiğit\Pictures\ss\*" "C:\Users\Yiğit\Pictures\udemy"')
    print('''
=======
= BYE =
=======
''')
    input("Press Enter")
    quit()

print('ss moving to standart\n')
os.system(r'move "C:\Users\Yiğit\Pictures\ss\*" "C:\Users\Yiğit\Pictures\arsiv\standart"')
try:
    while True:
        print("----------------------------------------------")
        ls= os.listdir('C:/Users/Yiğit/Pictures/ss/')
        for i in ls:
            print(i)

        choice= input('''Do you want rename new file?
1) Yes
2) No
3) Open Explorer
4) Exit
5) Refresh(enter)
6) Delete photo

->''').lower()

        if choice == "1":
            new_name= input("New Name: ")
            with open(r"C:\Users\Yiğit\Pictures\udemy\last file.txt", "r") as last_name:
                l_name= last_name.read()
            
            with open(r"C:\Users\Yiğit\Pictures\udemy\last file.txt", "w") as last_name:
                last_name.write(str( int(l_name)+1 ))
            
            with open(r"C:\Users\Yiğit\Pictures\udemy\last file.txt", "r") as last_name:
                l_name= last_name.read()
                
            os.system('cd "C:\\Users\\Yiğit\\Pictures\\ss" && ren "{}" "{}_{}.png"'.format(ls[-1], l_name, new_name))
        
        if choice == "3":
            os.system(r'explorer "C:\Users\Yiğit\Pictures\ss\"')
            
        if choice == "4":
            exit_()
        
        if choice == "6":
            pass#delete
        
except KeyboardInterrupt:
    exit_()
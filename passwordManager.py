from cryptography.fernet import Fernet #will be used for encryption
''' 
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()
'''

def load_key():
    file =  open("key.key","rb")
    key = file.read()
    file.close
    return key

key = load_key()
master_pwd = input("What is the master password? ")
key = load_key() #+ master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt','r') as f:
        for line in f.readline():
            data = line.rstrip()
            user, pwd = data.split(":")
            print("User:",user,",Password:",fer.decrypt(pwd.encode()).decode())

def add():
    name= input("Account Name: ")
    pwd = input("Password: ")

    #saving the inout data into a file
    # either appending to the end of a file and if it doesn't exist create a new file.
    #the above is done using 'a'
    with open('passwords.txt','a') as f:
        f.write(name + ":" + fer.encrypt(pwd.encode()) + "\n")

while True:
    # two modes:add or view 
    mode = input("Would you like to add a password or view existing ones (view/add) orpress 'Q' to exit " )
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
    

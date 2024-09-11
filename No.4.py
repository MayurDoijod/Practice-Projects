#this project has a problem as wrong master_pwd aslo opens the file
# this program has problem while encrpying and decrypting data

'''from cryptography.fernet import Fernet
def write_key():
    key=Fernet.generate_key()
    with open("key.key",'wb') as key_file:
        key_file.write(key)

def Load_key():
    file=open("key.key",'rd')
    key=file.read()
    return key

master_pwd=input("What is Master password? ")
key=Load_key() + master_pwd.encode
fer=Fernet(key)'''


def New():
    name=input("Account Name: ")
    pwd=input("Password: ")
    with open("password.txt",'+a') as T:
        T.write(name+"|"+pwd+"\n") # T.write(name+"|"+fer.encrypt(pwd.encode()).decode+"\n")
def Open():
    with open("password.txt",'r') as T:
        for line in T.readlines():
            data=line.rstrip()
            user,passw =data.split('|')
            print("User:",user ,"Password:",passw) #print("User:",user ,"Password:",fer.decrypt(passw.encodecode()).decode)



while True:
    pwd=input("Would you like to creat new Password or open existing one(New/Open)? OR type q to quit: ").lower()
    if pwd=="q":
        quit()
    if pwd=="new":
        New()
    elif pwd=="open":
        Open()
    else:
        print("Pleas enter Valid input")
        continue



def task1():
    for i in range(5):
        print(i)
    print("--------")
    for i in range(2,7):
        print(i)
    print("--------")
    for i in range(20,5,-1):
        print(i)
    print("--------")
    for i in "hello":
        print(i)


def task2():
    encrypted_message = "Wyh earne  eclaenp hIa nbtu?"
    decrypted_message = ""
    for i in range(0,len(encrypted_message),2): #pair : [0,2,4,...,28]
        decrypted_message+=encrypted_message[i]
    for i in range(0,len(encrypted_message),2): #impair : [1,3,5,...,27]
        decrypted_message+=encrypted_message[i]
    print(decrypted_message)
task2()

def task3(): #encrypt a message with a step like the romans
    step=3
    new_decrypted_message = "Hello, my name is George and I am 17 years old"
    encrypt_message=""
    for letter in new_decrypted_message:
        num=ord(letter)+step
        encrypt_message+=chr(num)
    print(encrypt_message)
task3()
def task4(): #decrypt a message with a step like the romans
    step=3
    new_decrypted_message = "Khoor/#p|#qdph#lv#Jhrujh#dqg#L#dp#4:|hduv#rog"
    encrypt_message=""
    for letter in new_decrypted_message:
        num=ord(letter)-step
        encrypt_message+=chr(num)
    print(encrypt_message)
task4()

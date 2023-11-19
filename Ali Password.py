import random
import string

def passGen(length):
    char = string.ascii_letters + string.digits
    password =''.join(random.choice(char) for _ in range(length))
    return password

def generate_password():
    try:
        length=int(input("Enter the length of the password:"))
        if length<=0:
            print("Plz enter a valid length.")
            raise ValueError
    except ValueError:
        print("Plz ennter a valid length.")
    else:
        password=passGen(length)
        print("Generated Password:",password)


def main():
    while True:
        generate_password()
        another_password = input("Do you want to geenerate another password? (y/n):")
        if another_password.lower()!='y':
            print("Thnaks for generating!")
            break
        

if __name__=="__main__":
    main()

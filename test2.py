# Importing random to generate  
# random string sequence  
import random

# Importing string library function  
import string


def rand_pass(size):
    # Takes random choices from
    # ascii_letters and digits  
    generate_pass = ''.join([random.choice(string.ascii_uppercase +
                                           string.ascii_lowercase +
                                           string.digits          +
                                           string.punctuation )
                             for n in range(size)])

    return generate_pass


count = input("Wie viele Zeichen? ")
site = input("Für welche Seite generieren Sie das Passwort? ")
# Driver Code
password = rand_pass(int(count))
password_list = {}
password_list.join(site, password)
print("Dein Passwort für >>> " + site + " <<< lautet: " + password)
print(password_list)

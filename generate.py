# Importing random, string hashlib
import random, string, hashlib, shelve, time, os

salt = os.urandom(256) # create salt

def rand_pass(size):
    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice(string.ascii_uppercase +
                                           string.ascii_lowercase +
                                           string.digits          +
                                           string.punctuation )
                             for n in range(size)])

    return generate_pass

# abfrage
count = input("Wie viele Zeichen? ")
site = input("Für welche Seite generieren Sie das Passwort? ")
user = input("Wie lautet der Benutzername / E-Mailadresse? ")

# Driver Code
password = rand_pass(int(count))

# show password
print("Dein Passwort für >>> " + site + " <<< lautet: " + password)

# hash with hashlib and encode password utf8
password_salt = hashlib.pbkdf2_hmac(
    "sha256", # The hash digest algorithm for HMAC
    password.encode("utf-8"), # Convert the password to bytes
    salt, # Provide the salt
    500000, # 500.000 iterations
    dklen = 128 # 128 byte key (32bit recommend, 64, 128, 256, 512 possible. standard: 128)
)
#print("Der passende Hash: " + password_salt)

# write user, hashed password and site into file. If file doesn't exist, create new tresor.
save = shelve.open("tresor")
created = time.strftime("%m/%d/%Y")
# Time: Short Weekday, Short Month, Hour, Minute, Second, Year
save[time.strftime("%a.%b.%H%M%S%Y")] = {"User": user, "Password": password_salt, "Salt": salt, "Site": site, "Created": created}
save.close()


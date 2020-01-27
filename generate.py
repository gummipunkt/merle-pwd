# Importing random, string hashlib
import random, string, hashlib, shelve, time


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
password_salt = hashlib.sha3_224(password.encode("utf-8")).hexdigest()
print(password_salt)

# write user, hashed password and site into file
save = shelve.open("tresor")
created = time.strftime("%m/%d/%Y")
# Time: Short Weekday, Short Month, Hour, Minute, Second, Year
save[time.strftime("%a.%b.%H%M%S%Y")] = {"User": user, "Password": password_salt, "Site": site, "Created": created}
save.close()


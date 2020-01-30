# Importing random, string hashlib
import random, string, hashlib, time, os, sqlite3

salt = os.urandom(64)  # create salt

def rand_pass(size):
    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice(string.ascii_uppercase +
                                           string.ascii_lowercase +
                                           string.punctuation     +
                                           string.digits)
                             for n in range(size)])

    return generate_pass

# abfrage
count = input("Wie viele Zeichen? ")
url = input("Für welche Seite generieren Sie das Passwort? ")
user = input("Wie lautet der Benutzername / E-Mailadresse? ")
while user == url:
    print("URL = Benutzer nicht möglich.")
    user = input("Wie lautet der Benutzername / E-Mailadresse? ")
else:
   print("Passwort wird berechnet und in die Datenbank eingetragen!")

# Driver Code
password = rand_pass(int(count))

# show password
print("Dein Passwort für >>> " + url + " <<< lautet: " + password)

# hash with hashlib and encode password utf8
password_salt = hashlib.pbkdf2_hmac(
    "sha256",  # The hash digest algorithm for HMAC
    password.encode("utf-8"), # Convert the password to bytes
    salt,  # Provide the salt
    200000,  # 200.000 iterations
    dklen = 64  # 64 byte key (32bit recommend, 64, 128, 256, 512 eg possible. standard: 65)
)

storage = salt + password_salt  # store salt and key

#salt_from_storage = storage[:64] # 32bit is the  salt
#key_from_storage = storage[64:]

created = time.strftime("%m%d%Y%.%H%M%S")
userdata = [ (user, password_salt, url, storage, created ) ]

connection = sqlite3.connect("tresor_sql.db") # connect to sqlite3
cursor = connection.cursor() # cursor sql

for p in userdata:
    format_str = """INSERT INTO entries (unique_id, user_email, password, url, storage, created)
    VALUES (NULL, "{user_email}", "{password}", "{url}", "{storage}", "{created}");"""

    sql_command = format_str.format(user_email=p[0], password=p[1], url=p[2], storage=p[3], created=p[4])
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
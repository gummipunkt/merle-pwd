import PySimpleGUI as sg, random, string, hashlib, time, os, sqlite3, os.path, binascii

salt = hashlib.sha256(os.urandom(256)).hexdigest().encode('ascii')  # create salt

##  THEME


sg.theme("TanBlue")  # please make your windows colorful

tab1_layout = [[sg.Text('Number of Characters'), sg.Text(size=(50, 1), key='count')],
               [sg.Slider(range=(1, 100), orientation='h', size=(20, 15), default_value=25, tick_interval=25)],
               [sg.Text('Website URL'), sg.Text(size=(12, 2), key='url')],
               [sg.Input(key='url_input')],
               [sg.Text('Username or E-mail address'), sg.Text(size=(12, 1), key='user')],
               [sg.Input(key='user_input')],
               [sg.Frame(layout=[
                   [sg.Checkbox('Numbers', size=(20, 1), default=True), sg.Checkbox('Letters', default=True)],
                   [sg.Checkbox('Special Character', size=(20, 1), default=True)]], title='Options',
                   title_color='red')],
               [sg.Text('Your password:'), sg.Text(size=(30,1), key='password_output')],
               [sg.Button('Generate'), sg.Button('Close')],
               ]
list_layout = [[sg.Text('hier gehts bald weiter'), sg.Text(size=(50, 1), key='count1')],

               ]

layout = [[sg.Text('merle-pwd - password manager', background_color='lightblue', justification='center', size=(30, 1), font=("Ubuntu", 25))],
          [sg.TabGroup([[sg.Tab('Generate', tab1_layout), sg.Tab('List', list_layout)]])]]

window = sg.Window("merle-pwd v0.2 - NO PRODUCTIVE USE! IT IS CRAP!", layout)

while True:  # Event Loop
    event, values = window.read()  # can also be written as event, values = window()

    if event is None or event == 'Exit':
        break

    elif event == 'Show':
        # change the "output" element to be the value of "input" element
        window['count'].update(values['count_input'])
        window['url'].update(values['url_input'])
        window['user'].update(values['user_input'])
        # above line can also be written without the update specified

    print(values.get(0))
    count = values.get(0)
    url = values["url_input"]
    user = values["user_input"]

    if values.get(1) == True:
        numbers_dec = string.digits
    else:
        numbers_dec = ""
    if values.get(2) == True:
        letters_dec = string.ascii_uppercase + string.ascii_lowercase
    else:
        letters_dec = ""
    if values.get(3) == True:
        special_dec = string.punctuation
    else:
        special_dec = ""


    def rand_pass(size):
        # Takes random choices from
        # ascii_letters and digits
        generate_pass = ''.join([random.choice(letters_dec +
                                               numbers_dec +
                                               special_dec)
                                 for n in range(size)])

        return generate_pass


    # Driver Code
    password = rand_pass(int(count))

    # password hash with hashlib and encode password utf8
    password_salt = hashlib.pbkdf2_hmac(
        "sha256",  # The hash digest algorithm for HMAC
        password.encode("utf-8"),  # Convert the password to bytes
        salt,  # Provide the salt
        500000,  # 200.000 iterations
        dklen=256  # 64 byte key (32bit recommend, 64, 128, 256, 512 eg possible. standard: 65)
    )

    password_salt = binascii.hexlify(password_salt)

    storage = (salt + password_salt).decode('ascii')  # store salt and key

    # user hash with hashlib and encode password utf8
    user_salt = hashlib.pbkdf2_hmac(
        "sha256",  # The hash digest algorithm for HMAC
        user.encode("utf-8"),  # Convert the password to bytes
        salt,  # Provide the salt
        500000,  # 200.000 iterations
        dklen=256  # 64 byte key (32bit recommend, 64, 128, 256, 512 eg possible. standard: 65)
    )

    user_salt = binascii.hexlify(user_salt)

    user_storage = (salt + user_salt).decode('ascii')  # store salt and key

    # salt_from_storage = storage[:64] # 32bit is the  salt
    # key_from_storage = storage[64:]

    created = time.strftime("%m%d%Y%.%H%M%S")
    userdata = [(user_salt, password_salt, url, storage, created)]

    if os.path.isfile("tresor.sql.db") == True:
        connection = sqlite3.connect("tresor_sql.db")  # create database
        cursor = connection.cursor()  # set cursor

        # create database with uniqueID, user or email, password, storage, creation date
        sql_command = """ 
        CREATE TABLE entries ( 
        unique_id INTEGER PRIMARY KEY, 
        user_email VARCHAR(50), 
        password VARCHAR(100),
        url VARCHAR(255),
        storage VARCHAR(255),
        created VARCHAR(10));"""

        cursor.execute(sql_command)  # execute

        connection.commit()
        connection.close()
    else:
        connection = sqlite3.connect("tresor_sql.db")  # connect to sqlite3
        cursor = connection.cursor()  # cursor sql

        for p in userdata:
            format_str = """INSERT INTO entries (unique_id, user_email, password, url, storage, created)
                    VALUES (NULL, "{user_email}", NULL, "{url}", "{storage}", "{created}");"""
        sql_command = format_str.format(user_email=p[0], password=p[1], url=p[2], storage=p[3], created=p[4])
        cursor.execute(sql_command)
        connection.commit()
        connection.close()

        password_result = password

        window['password_output'].update(password_result)

        ## Export Database

        connection = sqlite3.connect("tresor_sql.db")  # connect database
        cursor = connection.cursor()

        sql = "SELECT * FROM entries"

        cursor.execute(sql)
        for dsatz in cursor:
            unique_id = dsatz[0]
            user_email = dsatz[1]
            password = dsatz[2]
            url = dsatz[3]
            storage = dsatz[4]
            created = dsatz[5]
        connection.close()

window.close()
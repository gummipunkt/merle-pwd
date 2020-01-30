###### Welcome to merle-pwd.


merle-pwd will be a password manager to create and organize all of your passwords - for free.
It's public domain. Forever. It will work on every device you've. merle-pwd will sync your
passwords, if you want with your self hosted on your server. 

**Disclaimer: Here's nothing for a productive use case at the moment.**

**What works**
- Password creation (in a basic way)
- Storing into a sqlite3 database
    - Dictonary: UniqueID, Timecode, Password User (Password Hash & Salt), Site, Password Key (Password Hash & Salt)
- Password creation only with ASCII/digits e.g.
- Salt Hash Keys
- Salt Hash User

**Next**
- Show the list of saved websites
- Restore Passwords

**Ongoing**
- GUI

**What should work**
- How to: create a secure password
- Remember to change an old password
- 2FA 
- Login into merle-pwd with Master Password and/or 2FA-Key, Fingerprint
- App: Android, iOS
- Desktop: macOS, Linux, Windows
- Edit passwords

**Important**
- This isn't safe. Use a good password manager like 1Password, KeyPass, LastPass e.g.
- This is a "how to learn coding with python". I tried it several times and I failed every single
time. So I try it this way, perhaps it will work.

**How to start**

0) pip3 install PySimpleGui

1) Clone Git
clone git https://github.com/gummipunkt/merle-pwd.git

2) move into folder

3) python3 database.py (create database)

4) python3 gui.py

5) another terminal window
python3 open.py
to check

6) python3 database_delete.py to delete database

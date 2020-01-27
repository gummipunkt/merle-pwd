import shelve
save = shelve.open("tresor")

for entries in save.values():
    print(entries)
save.close()

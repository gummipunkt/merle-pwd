import generate
print("Möchten Sie ein Passwort anlegen?")
decision = input(">>>Y<<< or >>>N<<<")
if decision == "Y":
    generate.generator()

import time

'''def Timer(seconds):
    print("Début chrono : 40s")
    for i in range(seconds):
        time.sleep(1)
        seconds -= 1
    if seconds == 0:
        print("Fin")'''

class Minuteur :

    def __init__ (self, sec):
        self.sec = sec

    def temps (self):
        for i in range(self.sec):
            time.sleep(1)
            self.sec -= 1
        if self.sec == 0:
            print("Fin")


a = Minuteur(2)
a.temps()
v =3
i = str(v)
name = "bernard"
fichier = open("tab score.txt", "r")
print (fichier.read())
fichier.close()

#ecrire dans un fichier
fichier = open("tab score.txt", "a")

fichier.write("\n")
fichier.write(name)
fichier.write(" ")
fichier.write(i)
fichier.close()

print("modifié")

fichier = open("tab score.txt", "r")
print (fichier.read())
fichier.close()

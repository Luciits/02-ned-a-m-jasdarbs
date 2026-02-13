# Python papat tipi
virkne = "Mani sauc Artūrs"
skaitlis = 21
decimal_skaitlis = 3.14
ja_ne = True
# Konsoles izvade imantojot type()
print (type(virkne))
print (type(skaitlis))
print (type(decimal_skaitlis))
print (type(ja_ne))
# truthy/falsy piemēri
print (bool(0)) # Falsy
print (bool(skaitlis)) # Truthy netukša virkne
print (bool("")) # Falsy tukša virkne
# tiešā datu tipa pārveide
print (str(skaitlis)) # Pārvērš skaitli par virkni
print (int(decimal_skaitlis)) # Pārvērš decimāldaļu par veselu skaitli (noapaļo uz leju)
print (float(skaitlis)) # Pārvērš veselu skaitli par decimāldaļu
print (int(virkne)) # Mēģina pārvērst virkni par skaitli, bet tas neizdosies, jo virkne nav skaitlis
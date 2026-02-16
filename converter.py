#Vienību konvertors
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020
# Funkcijas, kas konvertē vienības un parbauda kļūdas

def km_to_mi(km):
    return km * KM_TO_MI
def mi_to_km(mi):
    return mi / KM_TO_MI
def kg_to_lb(kg):
    return kg * KG_TO_LB
def lb_to_kg(lb):
    return lb / KG_TO_LB
def l_to_gal(l):
    return l * L_TO_GAL
def gal_to_l(gal):
    return gal / L_TO_GAL
def usd_to_eur(usd):
    return usd * USD_TO_EUR
def eur_to_usd(eur):
    return eur / USD_TO_EUR
def check_valid_input(value):
    while True:
        try: 
            is_number = float(input(value))
            return is_number

        except ValueError:
              print("Kļūda!: Lūdzu, ievadiet vērtību ar cipariem.")
        
# Programmas izvēlne un lietotāja ievade
while True:
  print("**Unit Converter**")
  print()
  print("1. Kilometri uz jūdzēm")
  print("2. Kilogrami uz mārciņām")
  print("3. Litri uz galoniem")
  print("4. Dolāri uz eiro")
  print("5. Pārtraukt konvertoru")
  print()
  
  conversion_choice = check_valid_input("Izvēlieties konversijas veidu (1-5): ")
  if conversion_choice == 1:
    conversion_type = check_valid_input("Izvēlieties konversijas veidu (1: Kilometri uz jūdzēm, 2: Jūdzes uz kilometriem): ")
    if conversion_type == 1:
        km = check_valid_input("Ievadiet attālumu kilometros: ")
        mi = km_to_mi(km)
        print(f"{km} kilometri ir {mi:.2f} jūdzes.")
    elif conversion_type == 2:
        mi = check_valid_input("Ievadiet attālumu jūdzēs: ")
        km = mi_to_km(mi)
        print(f"{mi} jūdzes ir {km:.2f} kilometri.")
  elif conversion_choice == 2:
    conversion_type = check_valid_input("Izvēlieties konversijas veidu (1: Kilogrami uz mārciņām, 2: Mārciņas uz kilogramiem): ")
    if conversion_type == 1:
        kg = check_valid_input("Ievadiet svaru kilogramos: ")
        lb = kg_to_lb(kg)
        print(f"{kg} kilogrami ir {lb:.2f} mārciņas.")
    elif conversion_type == 2:
        lb = check_valid_input("Ievadiet svaru mārciņās: ")
        kg = lb_to_kg(lb)
        print(f"{lb} mārciņas ir {kg:.2f} kilogrami.")
  elif conversion_choice == 3:
    conversion_type = check_valid_input("Izvēlieties konversijas veidu (1: Litri uz galoniem, 2: Galoni uz litriem): ")
    if conversion_type == 1:
        l = check_valid_input("Ievadiet tilpumu litros: ")
        gal = l_to_gal(l)
        print(f"{l} litri ir {gal:.2f} galoni.")
    elif conversion_type == 2:
        gal = check_valid_input("Ievadiet tilpumu galonos: ")
        l = gal_to_l(gal)
        print(f"{gal} galoni ir {l:.2f} litri.")
  elif conversion_choice == 4:
    conversion_type = check_valid_input("Izvēlieties konversijas veidu (1: Dolāri uz eiro, 2: Eiro uz dolāriem): ")
    if conversion_type == 1 :
        usd = check_valid_input("Ievadiet summu dolāros: ")
        eur = usd_to_eur(usd)
        print(f"{usd} dolāri ir {eur:.2f} eiro.")
    elif conversion_type == 2:
        eur = check_valid_input("Ievadiet summu eiro: ")
        usd = eur_to_usd(eur)
        print(f"{eur} eiro ir {usd:.2f} dolāri.")
  elif conversion_choice == 5:
    print("Paldies, ka izmantojāt konvertoru!")
    break
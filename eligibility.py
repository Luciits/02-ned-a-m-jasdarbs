# Informācijas ievades menu un pārbaude
def valid_age():
    while True:
        try:
            age = int(input("Ievadiet savu vecumu: "))
            if age < 0:
                print("Kļūda!: Vecums nevar būt negatīvs. Lūdzu, ievadiet derīgu vecumu.")
            else:
                return age
        except ValueError:
            print("Kļūda!: Lūdzu, ievadiet derīgu skaitli vecumam.")
def yes_no_to_bool(response):
    while True:
        response = input(response).strip().lower()
        if response in ['jā', 'yes', 'y', 'j']:
            return True
        elif response in ['nē', 'no', 'n']:
            return False
        else:
            print("Kļūda!: Lūdzu, atbildiet ar 'jā' vai 'nē'.")
# Ievades pārbaude un informācijas ievade
vecums = valid_age()
ir_auto_aplieciba = yes_no_to_bool("Vai jums ir derīga autovadītāja apliecība? (jā/nē): ")
ir_students = yes_no_to_bool("Vai jūs esat students? (jā/nē): ")
ir_veterans = yes_no_to_bool("Vai jūs esat veterāns? (jā/nē): ")

var_balsot = (vecums >= 18)
var_nomat_auto = (vecums >= 21 and ir_auto_aplieciba)
ir_senioru_atlaide = (vecums >= 65) or ir_veterans
ir_studentu_atlaide = 16 <= vecums <= 26 and ir_students

print("\n---")
print(f"Jūs varat balsot: {'Jā \u2713' if var_balsot else 'Nē \u2717'}")
if var_nomat_auto:
    print("Jūs varat nomāt auto. \u2713")
else:
    if not ir_auto_aplieciba:
        print("Jūs nevarat nomāt auto, jo jums nav derīgas autovadītāja apliecības. \u2717")
    else:
        print("Jūs nevarat nomāt auto, jo jums nav pietiekami daudz gadu.")
print(f"Jūs saņemat senioru atlaidi: {'Jā \u2713' if ir_senioru_atlaide else 'Nē \u2717'}")
print(f"Jūs saņemat studentu atlaidi: {'Jā \u2713   ' if ir_studentu_atlaide else 'Nē \u2717'}")

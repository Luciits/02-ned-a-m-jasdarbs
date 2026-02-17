# Informācijas ievades menu un pārbaude
print("Lūdzu, ievadiet savu informāciju:")
age = int(input("Ievadiet savu vecumu: "))
has_valid_license = (input("Vai jums ir derīga autovadītāja apliecība? (j/n): ")).lower() == "j"
is_student = (input("Vai esat students? (j/n): ")).lower() == "j"
is_veteran = (input("Vai esat veterāns? (j/n): ")).lower() == "j"
# Konstantes atbilstības pārbaudei
can_vote = (age >= 18)
can_rent_car = (age >= 21 and has_valid_license == True)
senior_discount = (age >= 65 and is_veteran == True)
student_discount = (age >= 16 and age <= 26 and is_student == True)

if can_vote and can_rent_car and senior_discount and student_discount:
    print(f"Jūs esat tiesīgs balsot, iznomāt automašīnu, saņemt senioru atlaidi un studentu atlaidi. \u2713")
elif can_vote or can_rent_car or senior_discount or student_discount:
    print(f"Jūs esat tiesīgs saņemt dažas priekšrocības, bet ne visas. \u2713")
else:
    print(f"Jūs neesat tiesīgs saņemt visas priekšrocības. \u2717")

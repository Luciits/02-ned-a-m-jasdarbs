import random
r = random.randint(1, 100)
guess = None
count = 1
while True:
  print("Es izvēlējos skaitli no 1 līdz 100. Vai vari to uzminēt?")
  # Galvenā spēles loģika
  while guess != r:
    try:
      guess = int(input("Ievadi savu minējumu: "))
      if guess < r:
        print("Pārāk zems! Mēģini vēlreiz.")
        print(f"Minējumu skaits: {count} no 10")
        count += 1
      elif guess > r:
        print("Pārāk augsts! Mēģini vēlreiz.")
        print(f"Minējumu skaits: {count} no 10")
        count += 1
      else:
        print("Apsveicu! Tu uzminēji skaitli!")
        print(f"Minējumu skaits: {count} no 10")
        break
      # Pārbauda, vai minējumu skaits ir sasniedzis 10
      if count > 10:
        print("Diemžēl, tu neuzminēji skaitli 10 minējumu laikā.")
        print(f"Pareizais skaitlis bija: {r}")
        break
    except ValueError:
        print("Kļūda! Lūdzu, ievadi derīgu skaitli.")
  # Spēles beigas un iespēja spēlēt vēlreiz      
  play_again = input("Vai vēlies spēlēt vēlreiz? (jā/nē): ").strip().lower()
  if play_again in ['jā', 'yes', 'y', 'j', 'ja']:
    guess = None
    count = 1
    r = random.randint(1, 100)
    print("\nJauna spēle sākas!")
  else:
    print("Paldies par spēli! Uz redzēšanos!")
    break       
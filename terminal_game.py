print("WELCOME\nI'm Fred and I will be your guide through this journey...\nLike a sort of Gandalf but less gay and more autistic.\n\n")
tries = 0
p_name = input("First thing, what's your name? ")
print(f"\nHello, {p_name}.")


while tries < 3:
  p_type = input("\nWhat you want to be? \n1)Dwarf\n2)Orc\n\n")
  if p_type == "1":
    print("\nYou short as fuck! ahahaha")
    p_type = "Dwarf"
    break
  elif p_type == "2":
    print("\nYou fat and ugly...Nothing changed.")
    p_type = "Orc"
    break
  else:
    print("\nWrong input!")
  tries += 1
  if tries == 3:
    print("No more tries, idiot!\nNow you are a stupid monkey with a space helmet\n")
    p_type = "monkey"


dragon = input("\nOk, now let's start! You like Dragons?\n1)Yes\n2)No\n\n")
if dragon == "1":
  print("\nYeah no shit, everyone normal like dragon.\nYou think you are special?\n")
elif dragon == "2":
  print("\nI doN'T lIke DrAGons.... You Fucking Stupid CUNT!\n")
else:
  print("\nWrong input, but it doesn't matter for the plot anyway so...\n")

first_quest = input("First real question for the story.\nYou are in the middle of a forest and in front of you there are two pubs, you have to enter one of them:\n\n1)Nice place, cool people and normal prices.\n2)One beer for 2 euros.\n3)Why the fuck there are two pubs in the middle of a forest.\n\n")
tries = 0
wasted = int(0)
while tries in range(3):
	if p_type == "monkey":
		print("You were autistic in the first question so now you'll skip the pre-adventure drink.\n")
		break
	elif first_quest == "1" and p_type == "Dwarf":
		print("\nBoring answer but safe. You are a little weird midget so they leave you drink alone.\n")
		wasted += 1
		break
	elif first_quest == "2" and p_type == "Dwarf":
		print("\nYou little fucking alcoholic, good job!\n")
		wasted += 3
		break
	elif first_quest == "1" and p_type == "Orc":
		print("\nWrong answer for a orc but they gave you a bottle of wine to go away.\n You obviously chug the whole thing.\n")
		wasted += 2
		break
	elif first_quest == "2" and p_type == "Orc":
		print("\nFree beer cause you scary as fuck! You are now wasted congratulation\n")
		wasted += 7
		break
	elif first_quest == "3":
		print("\nYou are right but this adventure is imaginary so don't break my balls and play\n")
		first_quest = input("Same question(1-2): ")
	else:
		print("Wrong input!\n")
		first_quest = input("Same question(1-3): ")
	"""da aggiungere chiusura ciclo dopo 3 errori"""

second_quest = input("\nYou are outside, near to a lake there is a purple frog jumping next to some blue mushrooms. What do you do:\n1)Lick the frog\n2)Eat the mushrooms\n3)Jump into the lake\n")
while tries in range(3):
	if p_type == "monkey":
		print("\nYou have an helmet you can't use your mouth")
	elif second_quest == "1":
		print("\nIt was not a normal frog.....Good luck\n")
		wasted += 10
		break
	elif second_quest == "2" and p_type == "Dwarf":
		print("\nYou're stomach hurt but it doesn't matter cause you you see things.\n")
		wasted += 8
		break
	elif second_quest == "2" and p_type == "Orc":
		print("\nYou eat them all, but you are also a living tank so you are a little high\n")
		wasted += 5
		break
	elif second_quest == "3":
		print("\nYou are right but this adventure is imaginary so don't break my balls and play\n")
		second_quest = input("Same question(1-2): ")
	else:
		print("Wrong input!\n")
		second_quest = input("Same question(1-3): ")
print("fine")
    

""" elif p_type == "Orc": """
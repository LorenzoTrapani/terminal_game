import sys

print("\nWELCOME\n\nI'm Fred and I will be your guide through this journey...\nLike a sort of Gandalf but less gay and more autistic.\n\n")
tries = 0
healt = 100
p_name = input("First thing, what's your name? ")
print(f"\nHello, {p_name}.")


while tries < 3:
  p_type = input("\nWhat you want to be? \n1)Dwarf\n2)Orc\n\n")
  if p_type == "1":
    print("\nYou short as fuck! Ahahahaha.")
    p_type = "Dwarf"
    break
  elif p_type == "2":
    print("\nYou fat and ugly...Nothing changed.")
    p_type = "Orc"
    break
  else:
    print("\nWrong input!(1-2)")
  tries += 1
  if tries == 3:
    print("No more tries, idiot!\n\nNow you are a stupid monkey with a space helmet.")
    p_type = "monkey"


dragon = input("\nOk, now let's start! You like Dragons?\n1)Yes\n2)No\n\n")
if dragon == "1":
  print("\nYeah no shit, everyone normal like dragon.\nYou think you're special?\n\n")
elif dragon == "2":
  print("\nI doN'T lIke DrAGons.... You Fucking Stupid CUNT!\n")
else:
  print("\nWrong input, but it doesn't matter for the plot anyway so...\n")

first_quest = input("First real question for the story.\nYou are in the middle of a forest and in front of you there are two pubs, you have to enter one of them:\n\n1)Nice place, cool people and normal prices.\n2)One beer for 2 euros.\n3)Why the fuck there are two pubs in the middle of a forest.\n\n")
tries = 0
wasted = int(0)
while tries < 3:
	if p_type == "monkey" and first_quest != "3":
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
		print("\nFree beer cause you scary as fuck! You are now wasted congratulations!!!\n")
		wasted += 6
		break
	elif first_quest == "3":
		print("\nYou are right but this adventure is imaginary so don't break my balls and play\n")
		first_quest = input("Same question(1-2): ")
	else:
		print("Wrong input!\n")
		first_quest = input("Same question(1-3): ")

secret_quest = 0
second_quest = input("\nYou are outside, near to a lake there is a purple frog jumping next to some blue mushrooms. What do you do:\n\n1)Lick the frog\n2)Eat the mushrooms\n3)Jump into the lake\n\n")
while tries in range(3):
	if p_type == "monkey" and second_quest != "3":
		print("\nYou are a stupid monkey with an helmet, you can't use your mouth dumbass!")
		break
	elif p_type == "monkey" and second_quest == "3":
		print("\nYou are a stupid monkey with an helmet and you jump into a lake, you obviusly start to drown...\n\n")
		secret_quest = input("As you were about to pass out you see a shadow trying to reach you from above. What do you do?\n\n1)Pull your arm up hoping the shadow will save you\n2)Don't move\n\n")
		break
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
		print("\nYou are refresh as fuck! Good move.\n")
		wasted -= 1
		break
	else:
		print("Wrong input!\n")
		second_quest = input("Same question(1-3): ")

if secret_quest == "1":
	print("You get pulled out by an old man that gave you a towel to dry you.\nBut he also slap you 'cause it was a dumb move.\n")
	wasted += 1
elif secret_quest == "2":
	enter = input(print("You are......DEAD\n"))
	sys.exit()

attack = input("\n           BOOOOOOOOOOOOOOM!!!!!!!\n\nThe two pubs behind you explode and you see an angry wizard coming towards you. You have to attack!\n\n1)Climb a tree and do a jump attack from above\n2)Hide in the bushes ready for a counter attack\n\n")
while tries in range(3):
	if p_type == "monkey" and attack == "1":
		print("\nYou climb and do an incredible attack using your head and you kill the wizards. But the glass of the helmet breaks and you die too.\n\n             STUPID MONKEY..")
		break
	elif p_type == "monkey" and attack == "2":
		print("\nYou wait till the Wizard is near and you go crazy. You jump on his face and start ripping him apart till the point that there was nothing left....\n\n           MONKEY WIN!!!!\n")
		break
	elif attack == "1" and wasted >= 10:
		print("\nYou fall trying to climb the three cause you are too wasted.\nYou break your leg\nThe Wizards annihilates you\n")
		break
	elif attack == "1" and wasted < 10 and p_type == "Orc":
		print("\nYou move like a gorilla and swing an incredible punch\nWizard go say hi to jesus.\n")
		break
	elif attack == "1" and wasted < 10 and p_type == "Dwarf":
		print("\nYou move like a monkey and swing an incredible punch\nWizard destroy you anyway 'cause you are a Dwarf.\n")
		break
	elif attack == "2" and p_type == "Dwarf":
		print("\nYou wait till the Wizard is near and you go for the throat, killing the Wizard in a brutal way\n")
		break
	elif attack == "2" and p_type == "Orc":
		print("\nYou can't hide you are obese. The Wizard sees you and throw a fireball that demolish you.\n\n             DEAD\n")
		break
	else:
		print("Wrong input!\n")
		attack = input("Same question(1-3): ")

print("\nTHE END")
sys.exit()
    
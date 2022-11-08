import random, os, time
def rollDice(sides):
  result = random.randint(1,sides)
  return result
def sideRolls():
  roll6sideddice = rollDice(6)
  roll8sideddice = rollDice(8)
  health =((roll6sideddice * roll8sideddice)/2) + 10
  return health
def secondsideRolls():
  roll6sideddice = rollDice(6)
  roll12sideddice = rollDice(12)
  strength =((roll6sideddice * roll12sideddice)/2) + 12
  return strength
while True:
  print("   CHARACTER BUILDER   ")
  print()
  otherCharacter = input("Name your Legend:")
  type = input("Character Type ('Human, Elf, Wizard, Orc'):")
  print()
  print(otherCharacter)
  print("HEALTH:", sideRolls())
  print("STRENGTH:", secondsideRolls())
  print()
  print("May your name go down in legend....")
  print()
  again = input("Again?:")
  if again == "No" or again == "no":
    break
  time.sleep(1)
  os.system("clear")
  
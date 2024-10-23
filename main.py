

bidders = {}

offers = True

while offers:
  name = input("what's your name? ")
  bid = int(input("What's your bid? $"))
  bidders[name] = bid 
  people = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if people == "no":
    offers = False

for key in bidders:
  
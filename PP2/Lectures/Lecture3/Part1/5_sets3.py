# Sets

ourset = {"Batman", "Wonder Woman", "Superman"}

ourset.add("Lex Luthor")
ourset.add("Flash")
ourset.add("Joker")

print(ourset)

ourset.add("Joker")

print(ourset)

if "Lex Luthor" in ourset:
    print("Lex found")
else:
    print("Lex not found, he is hiding")

if "Batman" in ourset:
    print("Batman found")
else:
    print("Batman not found, he's in Gotham")

if "Homelander" not in ourset:
    print("Happily, not found")
else:
    print("He's here! Run!")
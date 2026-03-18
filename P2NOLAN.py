print("Dog Breed Finder\n")

points = 0

print("How active are you?")
print("1 - Not active")
print("2 - A little active")
print("3 - Very active")
answer = int(input("Enter 1, 2, or 3: "))

if answer == 1:
    points += 1
elif answer == 2:
    points += 2
elif answer == 3:
    points += 3

walks = int(input("\nHow many walks can you give per day? (0-3): "))
points += walks

yard = input("\nDo you have a yard? (yes/no): ")

if yard == "yes":
    points += 2

print("\nYour total points:", points)

print("\n Recommended dog breeds:")

if points <= 3:
    print("- Bulldog")
    print("- Pug")
    print("- Shih Tzu")
elif points <= 6:
    print("- Chihuahua")
    print("- Basset Hound")
    print("- French Bulldog")
elif points <= 9:
    print("- Beagle")
    print("- Cocker Spaniel")
    print("- Cavalier King Charles Spaniel")
else:
    print("- Labrador Retriever")
    print("- Golden Retriever")
    print("- Border Collie")

print("\nDone!")
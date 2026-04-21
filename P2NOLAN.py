questions_answered = 0
print("How is your day")
print("1 - Good")
print("2 - bad")
print("3 - nutral")
answer1 = int(input("Enter 1, 2, 3:"))
if answer1 == 1:
   print("Im glad")
   questions_answered += 1
if answer1 == 2:
   print("oh no") 
   questions_answered += 1
if answer1 == 3:
   print("Glad it was calm")
   questions_answered += 1
ready = input("Okay ready to find out which dog bread is best for you?")
print(f"{ready}")
if ready == "yes" and questions_answered > 0:
    print("Ok here we go")
    questions_answered += 1
    print("Ok here we go")
    questions_answered += 1
print("Dog Breed Finder\n")
points = 0
bonus_points = 0
print("How active are you?")
print("1 - Not active")
print("2 - A little active")
print("3 - Very active")
answer = int(input("Enter 1, 2, or 3: "))
if answer == 1:
   points += 1
   questions_answered += 1
elif answer == 2:
   points += 2
   questions_answered += 1
elif answer == 3:
   points += 3
   questions_answered += 1
if answer == 123:
   bonus_points += 50
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
   print("- Bulldog")
   print("- Basset Hound")
   print("- French Bulldog")
elif points <= 9:
   print("- Beagle")
   print("- Husky")
print(f"You answered {questions_answered} questions")
print(f"you got{bonus_points} bonus points")
print("A small, chill dog fits you" if points <= 3 or walks == 0 else "A more active dog fits you")
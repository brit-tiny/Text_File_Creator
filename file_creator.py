name = input("What's your name? \n")
color = input("What's your favorite color? \n")

creator = f"{name} created this file."
favorite = f"Their favorite color is {color}"

with open('example.txt', 'w') as file:
    file.write(creator)
    file.write(favorite)

print(creator)
print(favorite)
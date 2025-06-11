name = input("What's your name? \n")
color = input("What's your favorate color? \n")

creator = f"{name} created this file.\n"
favorite = f"Their favorite color is {color}.\n"

with open('example.txt', 'w') as file:
    file.write(creator)
    file.write(favorite)

print(creator)
print(favorite)

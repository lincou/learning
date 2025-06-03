
inputuser1 =input("Please enter your first name:")
inputuser2 =input("Please enter your last name:")
filename = "guest_user.txt"
with open(filename, "r+") as file:
    file.write(inputuser1 + inputuser2 + '\n')
    contents = file.read()
print(contents)
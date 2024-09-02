name = "Harry is a good  boy and  "

print(name.replace("  ", " "))
print(name) # Strings are immutable which means that you cannot change them by running functions on them


name = "Harry is a good boy and"

print(name.replace("good", "bad"))
print(name)
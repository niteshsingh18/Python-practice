marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}
print(marks.items())

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}
print(marks.keys())

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}
print(marks.values())

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}
marks.update({"Harry": 99, "Renuka": 100})
print(marks)


print(marks.get("Harry"))
print(marks["Harry"])

print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error
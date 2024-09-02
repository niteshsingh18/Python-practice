class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


j = programmer("Jordan", 900000, 226023)
print(j.name, j.salary, j.pin, j.company)

k = programmer("kenny", 1100000, 226025)
print(k.name, k.salary, k.pin, k.company)
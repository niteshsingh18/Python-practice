class employee:
    language = "python" # this is a class attribute
    salary = 1200000


a = employee()
a.language = 'Javascript' # this is an instance attribute
print(a.language, a.salary)
from sys import argv, exc_info

try:
    path, h, r, p = argv


    def salary(h, r, p):
        try:
            result = float(h) * float(r) + float(p)
            return (round(result, 4))
        except ValueError:
            print("At least one of the parameters has incorrect type!")


    print(f"Salary = {salary(h, r, p)}") if salary(h, r, p) != None else print("Try to execute script one more time!")

except ValueError:
    print(f"Unexpected error: {exc_info()[1]}")

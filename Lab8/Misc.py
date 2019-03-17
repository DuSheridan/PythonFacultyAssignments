
def deschiderefisier():
    numbers = []
    filename="Numbers"
    f = open(filename, "r")
    row = f.readline()
    while(row):
        line = row.split(" ")
        for el in line:
            numbers.append(int(el))
        row=f.readline()
    f.close()
    return numbers

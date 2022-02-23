inp1 = input("Write only a number, see if it is Armstrong number: ")
result = 0

while not inp1.isdecimal() :
    inp1 = input("Invalid Syntax! Please write only integer number: ")

for i in range(len(inp1)):
    result += (int(inp1[i]) ** len(inp1))
if result == int(inp1):
    print(f"{inp1} is an Armstrong number!!!")
else:
    print(f"{inp1} is not an Armstrong number...")

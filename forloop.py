"""for i in range(5):
    print(i)"""

"""for i in range(1, 6):
    print(i)"""

"""for ch in "shazra":
    print(ch)"""

"""fruits=["apple","cherry","mango","banana"]
for fruits in fruits:
    print(fruits)
    for i in fruits:
        print(i)"""

"""print("Make a table")
num= int(input("Enter a number : "))
for i in range(1, 11):
    print(num, "X", i, "=", num*i)"""

#Step

"""for i in range(0,11,2):
    print(i)"""

#Odd even analyzer
print("Welcome to odd even Analyzer")

start= int(input("Enter starting number \n"))
end= int(input("Enter ending number \n"))

print(f"your starting number is {start} and ending number is {end}")

for i in range(start,end +1):
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")
print("Thank you to Analyze")
from datetime import datetime

startTime = datetime.now()

print("Enter a number to count to: ")
count = int(input()) + 1


for i in range(0, count):
    print(i)

endTime = datetime.now()

timeDifference = endTime - startTime

print(timeDifference)
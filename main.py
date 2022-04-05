#Isiah Williams
#Coding For All-P6
#Mr. Burns

n = int(input("Please enter your number"))
sequence = 1

while n != 1:
  if n % 2 == 0:
    n /= 2
    print(int(n))
    sequence += 1
  else:
    n = 3 * n + 1
    print(int(n))
    sequence += 1
print("The length of the sequence is " + str(sequence) + " numbers")

#40 gave me the longest sequence because it had many odd values which would make the numbers bigger and the output also gave me the length of the sequence
message = input("what message do you want to repeat? ")
times = int(input("how many times do you want to repeat it? ")) + 1

for n in range(times):
    print(message, + n)
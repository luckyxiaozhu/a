import random
guessesTaken = 0

print('hello!What is your name?')
myname = input('')

number = random.randint(1,20)
print ('well,%s,I am thinkin of a number between 1 and 20.' %myname)

while guessesTaken < 6:
    print('Take a guess.')
    guess = int(input())

    guessesTaken += guessesTaken

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job %s! You guessed my number in guessesTaken %s!'%(myname,guess))
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was %s'% number)

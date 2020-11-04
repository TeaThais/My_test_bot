def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("What is Django?")
    print("1. A new language")
    print("2. Some unknown technology")
    print("3. A handsome cowboy")
    print("4. A Python-based framework")

    answer = int(input())
    print("Completed, have a nice day!" if answer == 4 else "Please, try again.")
    while answer < 4:
        answer = int(input())
        print("Completed, have a nice day!" if answer == 4 else "Please, try again.") 


def end():
    print('Congratulations, have a nice day!')


greet('Tom', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()

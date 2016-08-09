for score in range(1,11):
    print('Enter your score\n')
    score = input()
    if score <= 69:
        print('Your grade is D')
    elif score <= 79:
        print('Your grade is C')
    elif score <= 89:
        print('Your grade is B')
    elif score <= 100:
        print('Your grade is A')
print('End of the program. Bye!')
input('Press enter to exit')
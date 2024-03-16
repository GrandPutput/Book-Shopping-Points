point_test = True
while point_test == True:
    customer_books = 0
    continue_test = True

    customer_books = int(input('Please Enter Amount of Books Purchased : '))
    if customer_books >= 2 and customer_books <= 3:
        print('You earn 5 points!\n')
    elif customer_books >= 4 and customer_books <= 5:
        print('You earn 15 points!\n')
    elif customer_books >= 6 and customer_books <= 7:
        print('You earn 30 points!\n')
    elif customer_books >= 8:
        print('You earn 60 points!\n')
    else:
        print('You earn 0 points!\n')
    
    while continue_test == True:
        response = input('Would you like to test again? : ')
        if response.lower() == 'yes':
            point_test = True
            continue_test =False
            print('')
        elif response.lower() == 'no':
            point_test = False
            continue_test = False
            print('')
        else:
            print('Please enter Yes or No!\n')
    
print('Goodbye!')
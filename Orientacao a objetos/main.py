from bank_classes import CheckingAccount, CreditCard

# help(CheckingAccount)
# help(CheckingAccount._get_current_date_and_time)

my_account = CheckingAccount('111.222.333-44', '0001', '12345')
destination_account = CheckingAccount('555.666.777-88', '0002', '67890')

while True:
    print('Make a deposit - 1 | ' \
          'Withdraw cash - 2 | ' \
          'Check your balance - 3 | ' \
          'Transfer to another account - 4 | ' \
          'Finish - 5')

    user_choice = input('Choose an option: ')

    if user_choice == '1':
        my_account.deposit()

    elif user_choice == '2':
        my_account.withdraw()

    elif user_choice == '3':
        balance = my_account.check_balance()
        print(f'\nYour current balance is: ${balance}\n')

    elif user_choice == '4':
        my_account.transfer(destination_account)

    elif user_choice == '5': break

    else: print('\nInvalid option.\n')

my_account.show_transactions_log()
destination_account.show_transactions_log()

my_credit_card = CreditCard('Álvaro', my_account)
secondary_credit_card = CreditCard('Álvaro', my_account)

my_account.show_credit_cards()

my_credit_card.password = '1792'

my_account.show_credit_cards()

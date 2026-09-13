card_inserted = True
Pin_number = 1234
balance = 10_000
Pin_number = int(input("Enter the Pin number : "))
amount_withdraw = int(input("Enter the amount to withdraw : "))
daily_withdraw_limit = 50_000


if card_inserted:
    if Pin_number == 1234:
        if balance >= amount_withdraw:
            if amount_withdraw <= daily_withdraw_limit:
                print(f"You can withdraw amount {amount_withdraw}")
            else:
                print("Amount exceed daily limit")
        else:
            print("Insufficient balance")
    else:
        print("Incorrect Pin")
else:
    print("Card Decline")

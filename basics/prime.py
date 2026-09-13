for num in range(1,101):                # run for 100 times
    if num>1:                           # ingnore one and number should be greater than one
        for i in range(2,num):          # run from 2
            if num%i==0:
                break                  # the concept here is the number 2 should only divisible by 2 same for 3/3
        else:
            print(num)
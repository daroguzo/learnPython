user1, user2 = map(int, input().split())
for user1 in range(user1, user2 + 1):
    if user1 % 5 == 0 and user1 % 7 == 0:
        print('FizzBuzz')
    elif user1 % 5 == 0:
        print('Fizz')
    elif user1 % 7 == 0:
        print('Buzz')
    else:
        print(user1)
        user1 += 1
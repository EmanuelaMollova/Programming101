def calculate_coins(sum):
    money = round(sum * 100)
    coins = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}

    for coin in sorted(coins)[::-1]:
        while money >= coin:
            coins[coin] += 1
            money -= coin

    return coins

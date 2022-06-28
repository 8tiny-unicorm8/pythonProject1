# Hапишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры.
# Остальные должны заменяться звездочками
card = int(input('Номер карты, 16 цифр: '))
card = str(card)
def credit_card():
    for i in card:
        card2 = card.replace(card[0:12], '************')
    print(card2)

credit_card()
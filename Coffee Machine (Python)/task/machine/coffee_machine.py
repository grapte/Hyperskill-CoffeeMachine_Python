from dataclasses import dataclass
from textwrap import dedent


@dataclass
class VendingMachine:
    water: int = 400
    milk: int = 540
    beans: int = 120
    cups: int = 9
    money: int = 550
    
    def __str__(self):
        return dedent(f'''\
            The coffee machine has:
            {self.water} ml of water
            {self.milk} ml of milk
            {self.beans} g of coffee beans
            {self.cups} disposable cups
            ${self.money} of money''')

    def __add__(self, other):
        return VendingMachine(
            water=self.water + other.water,
            milk=self.milk + other.milk,
            beans=self.beans + other.beans,
            cups=self.cups + other.cups,
            money=self.money + other.money
        )


cm = VendingMachine()

while True:
    print('Write action (buy, fill, take, remaining, exit):')
    match input():
        case 'remaining':
            print(cm)
        case 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            match input():
                case '1':
                    delta = VendingMachine(water=-250, milk=0, beans=-16, cups=-1, money=+4)
                case '2':
                    delta = VendingMachine(water=-350, milk=-75, beans=-20, cups=-1, money=+7)
                case '3':
                    delta = VendingMachine(water=-200, milk=-100, beans=-12, cups=-1, money=+6)
                case 'back':
                    continue

            if all(attr >= 0 for attr in vars(cm + delta).values()):
                print('I have enough resources, making you a coffee!')
                cm += delta
            else:
                missing = [attr for attr, value in vars(cm + delta).items() if value < 0 and attr != 'money']
                print(f'Sorry, not enough {', '.join(missing)}!')

        case 'fill':
            lines = [
                'Write how many ml of water you want to add:',
                'Write how many ml of milk you want to add:',
                'Write how many grams of coffee beans you want to add:',
                'Write how many disposable cups you want to add:',
            ]
            for attr, line in zip(['water', 'milk', 'beans', 'cups'], lines):
                print(line)
                setattr(cm, attr, getattr(cm, attr)+int(input()))
        case 'take':
            print(f'I gave you ${cm.money}')
            cm.money = 0
        case 'exit':
            break

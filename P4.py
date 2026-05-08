from utils import *
import time

set_background("soccerfield")

money = 0
money_per_click = 1
auto_money = 0
junko = 0

junko_sprites = []

m1 = create_sprite("alien", -200, 150)
m1.hideturtle()

m2 = create_sprite("turtle", 155, 150)
m2.hideturtle()


def update_screen():
    m1.clear()
    m1.write(
        f"Money: ${round(money, 1)}\nJunko: {junko}",
        align="center",
        font=("Arial", 20, "bold")
    )


def earn_money():
    global money
    money += money_per_click
    update_screen()


def upgrade_click():
    global money, money_per_click

    if money >= 10:
        money -= 10
        money_per_click += 1

        m2.clear()
        m2.write("Upgraded click!", align="left")
    else:
        m2.clear()
        m2.write("Not enough money", align="left")

    update_screen()


def buy_passive():
    global money, auto_money

    if money >= 25:
        money -= 25
        auto_money += 1

        m2.clear()
        m2.write("Passive income bought!", align="left")
    else:
        m2.clear()
        m2.write("Need $25", align="left")

    update_screen()


def buy_junko():
    global money, junko

    if money >= 10:
        money -= 10
        junko += 1

        # Create a new Junko sprite on screen
        x = -200 + (junko * 40)
        y = 0

        new_junko = create_sprite("junko", x, y)
        junko_sprites.append(new_junko)

        m2.clear()
        m2.write(f"Junko bought! Total: {junko}", align="left")
    else:
        m2.clear()
        m2.write("Need $10", align="left")

    update_screen()


# Controls
window.onkeypress(earn_money, "space")
window.onkeypress(upgrade_click, "w")
window.onkeypress(buy_passive, "s")
window.onkeypress(buy_junko, "x")

window.listen()

# Game loop
for i in range(1000000000):

    money += auto_money * 0.1
    money += junko * 0.2

    update_screen()

    time.sleep(0.01)
    window.update()
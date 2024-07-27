#Variables
print("Welcome to the GC")
name = input("""What is your name?
> """)
sub_total = 0
apples = 0
grapes = 0
oranges = 0


buy = int(input((f"""Welcome {name}. Which Fruit would you like to buy?
1. Apple $2
2. Grape $1
3. Orange $3
> """)))
if buy == 1:
    print("You bought 1 apple at $2")
    sub_total += 2
    apples += 1
elif buy == 2:
    print("You bought 1 grape at $1")
    sub_total += 1
    grapes += 1
elif buy == 3:
    print("You bought 1 orange at $3")
    sub_total += 3
    oranges += 1

add_fruit = input("""Would you like to buy another piece of fruit?
    > """)

while add_fruit == "y":
    buy = int(input((f"""Welcome {name}. Which Fruit would you like to buy?
    1. Apple $2
    2. Grape $1
    3. Orange $3
    > """)))
    if buy == 1:
        print("You bought 1 apple at $2")
        sub_total += 2
        apples += 1
    elif buy == 2:
        print("You bought 1 grape at $1")
        sub_total += 1
        grapes += 1
    elif buy == 3:
        print("You bought 1 orange at $3")
        sub_total += 3
        oranges += 1

    add_fruit = input("""Would you like to buy another piece of fruit?
        > """)
tax = sub_total * 0.05
total = tax + sub_total

if add_fruit == "n":
    print(f"Order for {name}")
    print(f"You bought {apples} apple(s) at $2")
    print(f"You bought {grapes} grape(s) at $1")
    print(f"You bought {oranges} orange(s) at $3")
    print(f"Sub Total: ${sub_total}")
    print(f"5% Tax: {tax}")
    print(f"Total: {total}")







meal_cost =float(input())
tippercent = int(input())
taxpercent = int(input())
def solve(meal_cost, tippercent, taxpercent):
    tip = meal_cost * tippercent /100
    tax = meal_cost * taxpercent /100
    total = meal_cost + tip +tax
    print (round(total))
solve(meal_cost,tippercent,taxpercent)


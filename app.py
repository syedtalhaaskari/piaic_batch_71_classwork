def separator():
    print('--------------------------------------------------------')

def isFloat(num: str) -> bool:
    try:
        float(num)
        return True
    except:
        return False

# Uncomment to view results
# babar_runs = input("Enter babar runs: ")
# balls_played = input("Enter babar balls: ")

# if isFloat(babar_runs) and balls_played.isdigit():
#     if float(babar_runs) >= 50 and balls_played < babar_runs:
#         print("King")
#     else:
#         print("Parchi")
# else:
#     print("Invalid Input")

separator()

babar_runs = 60
balls_played = 59

if float(babar_runs) >= 50 and balls_played < babar_runs:
    print("King")
else:
    print("Parchi")

separator()

# 3rd task
babar_runs = 36
balls_played = 8
total_sixes = 5

if (babar_runs >= 50 and balls_played < babar_runs) or total_sixes >= 5:
    print("King")
else:
    print("Parchi")

separator()

# 4th Task
items = ["Hara Dhaniya", "Podina", "Dahi", "Andey", "Dahi"]

print(items)
print(items[2])
print(items[1], items[2])
print(items[1:3])
print(items.count('Dahi'))
print(items.index('Dahi'))

items.pop()

print(items)

separator()

# 5th Task
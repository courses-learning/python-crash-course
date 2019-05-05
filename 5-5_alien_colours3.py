# Same as 5-4 with if elif else chain

score = 0
alien1 = "blue"
if alien1 == "green":
    score += 5
    print('You scored 5 points')
elif alien1 == "yellow":
    score += 10
    print('You scored 10 points')
else:
    score += 15
    print('You scored 15 points')
print(f'Score: {score}')

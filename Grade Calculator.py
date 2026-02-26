while True:
    try:
        number_of_student = int(input('Enter the number of student: '))
        break
    except ValueError:
        print( "Invalid input. Please enter a valid number (e.g., 12 )." )

scores = []
for i in range(number_of_student):
    score = float(input(f'Enter score of student {i+1}: '))
    scores.append(score)

print('All scores', scores)
average = sum(scores)/len(scores)
print("Average score: ", average)

if 0 <= average < 50:
    print('Need improvement.')
elif 50 <= average <= 80:
    print('Good class.')
else:
    print('Excellent!')

larg = max(scores)
small = min(scores)

print('Highest score: ',larg)
print('Lowest score: ',small)


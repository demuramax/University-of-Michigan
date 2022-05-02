score = input("Enter Score: ")
sc = float(score)

try:
    0 <= sc <= 1
except:
    print('Error, write the float number between 0 and 1')
       
if sc >= 0.9:
    print('A')
elif sc >= 0.8:
    print('B')
elif sc >= 0.7:
    print('C')
elif sc >= 0.6:
    print('D')
else:
    print('F')


    

if 0 <= sc <= 1:
    if sc >= 0.9:
        print('A')
    elif sc >= 0.8:
        print('B')
    elif sc >= 0.7:
        print('C')
    elif sc >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('Please write the number between 0 and 1')
    

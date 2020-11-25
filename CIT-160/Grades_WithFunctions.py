print('Hi, let\'s build your report card: ')

engClass = int(input('What is your English class final score?: '))
mathClass = int(input('What is your Math class final score?: '))
compClass = int(input('What is your Computer class final score?: '))
sciClass = int(input('What is your Science class final score?: '))
peClass = int(input('What is your PE class final score?: '))

def engScore(engClass):
    if(engClass >= 90):
       print('You got an A')
    elif(engClass >= 80):
        print('You got a B')
    elif(engClass >= 70):
        print('You got a C')
    elif(engClass >= 60):
        print('You got a D')
    elif(engClass <= 59):
        print('You got an F')
    else:
        print('You Failed')

def mathScore(mathClass):
    if(mathClass >= 90):
       print('You got an A')
    elif(mathClass >= 80):
        print('You got a B')
    elif(mathClass >= 70):
        print('You got a C')
    elif(mathClass >= 60):
        print('You got a D')
    elif(mathClass <= 59):
        print('You got an F')
    else:
        print('You Failed')

def compGrade(compClass):
    if(compClass >= 90):
       print('You got an A')
    elif(compClass  >= 80):
        print('You got a B')
    elif(compClass >= 70):
        print('You got a C')
    elif(compClass >= 60):
        print('You got a D')
    elif(compClass <= 59):
        print('You got an F')
    else:
        print('You Failed')

def sciScore(sciClass):
    if(sciClass >=90):
        print('You got an A')
    elif(sciClass >=80):
        print('You got a B')
    elif(sciClass >= 70):
        print('You got a C')
    elif(sciClass >= 60):
        print('You got a D')
    elif(sciClass <= 59):
        print('You got an F')
    else:
        print('You Failed')

def peScore():
    peGrade = int(peClass)
    if(peClass >=90):
        print('You got an A')
    elif(engClass >=80):
        print('You got a B')
    elif(engClass >= 70):
        print('You got a C')
    elif(engClass >= 60):
        print('You got a D')
    elif(engClass <= 59):
        print('You got an F')
    else:
        print('You Failed')

print('Here is you report card: ')
print('PE: ' + str(peScore))

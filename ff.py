import random

template = input("Pick one of the templates 1->3 \n1 - Hospital\n2 - Camping\n3 - Castle\n")
if template == 1:
    number = input("Input Number: ")
    measure = input("Input Measure of time (ex. seconds, minutes, days etc.): ")
    
    transport = random.choice([
        'on a boat',
        'on a plane',
        'on a helicopter',
        'on a horse',
        'in a taxi',
        'in a submarine'
    ])

    adj = input("Input an Adjective: ")

    adj2 = input("Input another Adjective: ")

    noun = input("Input a Noun for the last adjective: ")
    color = input("Input a Color and a Part of the Body: ")
    verb = input("Input a Verb: ")
    number2 = input("Input a Number: ")
    
    decoration = random.choice([
        'Christmas Trees',
        'Toys',
        'Chairs'
    ])

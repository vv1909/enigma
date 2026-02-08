import random

template = input("Pick one of the templates 1->3 \n1 - Hospital\n2 - Camping\n3 - Castle\n")
if template == '1':
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
    color = input("Input a Color + Part of the Body: ")
    verb = input("Input a Verb: ")
    number2 = input("Input a Number: ")
    
    decoration = random.choice([
        'Christmas Trees',
        'Toys',
        'Chairs'
    ])


    noun3 = input("Input a Noun: ")
    part2 = input("Input a Part of the body: ")
    bkfst = input("Input Verb + Noun: ")
    adj3 = input("Input another Adjective: ")
    silly = input("Input a Silly Word + Noun: ")
    print(f"It was about {number} {measure} ago when I arrived at the hospital in a {transport}. The hospital is a/an {adj} place, there are a lot of {adj2} {noun} here. There are nurses here who have {color}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number2} {decoration}. Today I talked to a doctor and they were wearing a {noun3} on their {part2}. I heard that all doctors {bkfst} every day for breakfast. The most {adj3} thing about being in the hospital is the {silly} ! ")

elif template == '2':
    name = input('Input Name: ')
    noun = input('Input Noun: ')
    adj = input('Input Adjective(Feeling): ')
    verb = input('Input Verb: ')
    adj2 = input('Input Adjective(Feeling): ')

    animal = input('Input Animal')
    verb2 = input('Input Verb: ')
    color = input('Input Color: ')
    verb3 = input('Input Verb+ing: ')


    adverb = input('Input an Adverb (ending in ly): ')

    number = input("Input Number: ")
    measure = input("Input Measure of time (ex. seconds, minutes, days etc.): ")
    
    color2 = random.choice([
        'red','blue','pink','green','grey','black','yellow','white'
    ])
    animal2 = input('Input Animal: ')

    noun2 = input('Input Noun: ')
    number2 = input('Input Number: ')
    silly = input('Input Silly word: ')
    print(f"This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun}. I am so {adj} to {verb} in a tent. I am {adj2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb3}. Then we will {adverb} hike through the forest for {number2} {measure}. If I see a {color} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {silly} stories and roast {number2} around the campfire!! ")

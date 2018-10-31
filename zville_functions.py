#! python 3
import random, time, sys


def intro_game():  # Runs when user choose Intro Game
    """ Text intro for game take and returns nothing
    :return: None
    """

    story = """ A STORY. How shit hit the fun?
    An isolated village. 
    Great place for testing stuff on human subjects, isn't it?
    Somewhere THEY have been attached to the idea. 
    Concerns about value of human life, dignity and work ethics since long had 
    their own spin-off. 
    They simply admit such an experiment because they CAN get away with it.
    Let's call it ... 
    LACK OF TRANSPARENCY. 
    A viral sample has been released. 
    Something bad, creepy stuff take my word. 
    Somewhere in the village, patient zero has been exposed to a sample. 
    ================================================================================
    NOW. 

    XX:XX
    village_name, pop_size
    """

    for item in story:
        print(item, end='', sep='')
        if item in '.?!':
            time.sleep(1)
            continue
        time.sleep(0.05)


def village_gen(random_village):
    """ GENERATES RANDOM VILLAGE OR USER CUSTOMISED
    :takes True|False random True or custom False
    :returns village_name, pop_size, time
    """
    if not random_village:  # user designed village
        while True:  # return village name and correct size

            try:
                village_name, pop_size = input(
                    'Enter village name and population size '
                    'between 200 and 2500 eg. Yeovil '
                    '1500').split()
                if not pop_size.isdecimal():
                    print('Wrong format for population size. Enter integer.')
                    continue
                if not pop_size or int(pop_size) not in range(100, 2501):
                    continue

            except:
                print('Something went wrong')
            else:
                print('Your choice is ', village_name, pop_size, 'Is that '
                                                                 'correct? '
                                                                 '(y)|(n)')
                spam = input()
                if spam.lower() == 'y':
                    break
                else:
                    continue

    elif random_village:
        spam = open('dictio//names_village.txt')
        village_name = random.choice(spam.read().split('\n'))
        spam.close()
        pop_size = random.randint(100, 2500)

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return [village_name.title(), pop_size, time]


def user_menu_choice():
    """  MAIN MENU
    Can exit game on user choice 6
    :return: integer representing user choice from main menu
    """
    print('='*80)
    print('+' * 30 + ' OUTBREAK IN ZVILLE ' + '+' * 30)
    menu_choices = ['Intro Game', 'Start Random Sim', 'Start Custom Sim',
                    'Design Village', 'Design Family', 'Set Sim Speed', 'Exit']

    for item in menu_choices:
        print(str(menu_choices.index(item)) + '. ' + item +
              ' '.join(['' for i in range(21 - len(item))]) + '+')

    main_choice = []
    while main_choice not in range(len(menu_choices)):
        main_choice = input()
        if main_choice == str(menu_choices.index('Exit')):  # quits game if user chose '1'
            sys.exit()
        elif main_choice.isdigit() and int(main_choice) \
                in range(len(menu_choices)):  # user choses number in range of options available
            return int(main_choice)
        else:
            print('Choose number corresponding to an option')


def family_gen(random_family):
    """ Generates family names and stats appending them into existing lists
    :param  True or False - random or custom genration
    :return: [familyChar], [familyStats]
    """
    if not random_family:  # user defined family names
        familyChar = []

        while True:
            name = input('Type family member name or enter:  ')
            if name:
                familyChar.append(name.title())
            elif not name:
                continue
    elif random_family:  # family size 1 - 8 , most likely  3-6 family , other ranges less likely
        k100_roll = random.randint(1,100)

        if k100_roll in range(1,51):
            size_f = random.randint(3,5)
        elif k100_roll in range(51,81):
            size_f = int(random.choice('126'))
        elif k100_roll in range(82,101):
            size_f = int(random.choice('78'))

        m_txt = open('dictio//names_male.txt')
        f_txt = open('dictio//names_female.txt')
        male_names = m_txt.read().split('\n')
        female_names = f_txt.read().split('\n')

        """OK HERE IS WHAT NEEDS TO BE DONE
        if family size is 2 then its 80 % there will be male or female, rest gender is random.
        """
        if size_f == 2:
            if random.randint(1, 100) < 80:  # if family 2 members there is 80 % gender is opposite
                familyChar.append(random.choice(male_names))
                familyChar.append(random.choice(female_names))
        else:

            for i in range(size_f):
                gender = random.choice('m', 'f')
                if size_f != 2:
                    if gender == 'm':
                        familyChar.append(random.choice(male_names))
                    elif gender == 'f':
                        familyChar.append(random.choice(female_names))




        spam = open('dictio//')


    familyStats = []  # stats of family members [physical, mental, HP, morale]

    for i in familyChar:  # returns stats of family members (semi-randomised)
        physical = random.randint(2, 5)
        mental = random.randint(2, 5)
        HP = physical * 2  # HP is double of physical
        morale = 3  # not used in game
        familyStats.append([physical, mental, HP, morale])

    return familyChar, familyStats












# FOR EXPORT (doesn't belong to simulation)


def letters_correction(a_list):  # an example that removes all newlines from list items
    """    Removes unwanted characters from strings
    example: spam = ['zajebany \njabol', 'akuku\n kurwa']
             print(letters_correction(spam))
             -> ['zajebany jabol', 'akuku kurwa']
    :param a_list: list data type
    :return: corrected list
    """
    a_list_corrected = []

    for item in a_list:
        if '\n' in item:  # for custom changes
            item = ''.join([letter for letter in item if letter != '\n'])  # for custom changes
            a_list_corrected.append(item)
            continue
        a_list_corrected.append(item)
    return a_list_corrected
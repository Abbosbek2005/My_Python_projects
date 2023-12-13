'''
Abbosbek Ahmadjonov
CSC 110
Project 6
This program has four functions 
that works accordingly below by the 
given instrucions(information) and rules

'''

def load_game():
    """
    This function Iterate over each line by splitting and splitting 
    and get them into dictionary as key and value pairs
    key: the first value in the line type cast it to integer
    value: list containing all the second values associated 
    with the same key in multiple lines

    """
    game_file = open("game.txt", "r")
    game = {}

    # read lines in file
    lines = game_file.readlines()
    
    for line in lines:
        # strip and split by tab each line
        new = line.strip().split("\t")
        # get the first value(integer) in the list 
        key = int(new[0])
        # check if the key not in dictionary
        # if so create new list otherwise add it acordingly
        if key not in game:
            game[key] = []
        game[key].append(new[1])
    
    game_file.close()
    return game

def load_objects():

    """
    This function Iterate over each line by splitting and splitting 
    and get them into dictionary as key and value pairs
    key: tuple with the first three values of each line  cast the first two values to integer
    value: list with the rest of the values in each line (starting at index 3)

    """
    object_file = open("objects.txt", "r")
    objects = {}
    # read lines in file
    lines = object_file.readlines()
    for line in lines:
        # strip and split by tab each line
        each = line.strip().split("\t")
        #get the first three values in a tuple(the first two are integers) 
        empty_tuple = (int(each[0]), int(each[1]), each[2])
        # the rest starting from index 3 is a list
        list = each[3:]
        # get them into a dictionary as key and value pairs
        objects[empty_tuple] = list

    object_file.close()
    return objects

def load_travel_table():
    """
    This function Iterate over each line by splitting and splitting 
    and get them into dictionary as key and value pairs
    key: tuple with the first two values of each line cast these first two values to integer
    value: third value in each line

    """
    travel_file = open("travel_table.txt", "r")
    travel_table = {}
    # read lines in file
    lines = travel_file.readlines()
    for line in lines:
        # strip and split by tab each line
        all = line.strip().split("\t")
        # get the first two values in a tuple(both of them are integers) 
        key = (int(all[0]), int(all[1]))
        # the rest starting from index 2 is a list
        value = all[2]
         # get them into a dictionary as key and value pairs
        travel_table[key] = value 
    
    travel_file.close()
    return travel_table

def print_instructions():
    """
    Open instructions.txt in read mode and 
    Print the contents of the file

    """

    f = open("instructions.txt", "r")
    file_contents = f.read()
    # read file and print it
    print(file_contents)
    f.close()

def get_location(location, game, objects, player_objects):
    '''
    This function gets the next location from the game data.
    It doesn't return anything, it prints messages related to
    objects (if the user has them or not) and location information
    Args:
        location: integer
        game: dictionary with location and string information
        objects: dictionary of location, binary (0 or 1), and object name
        player_objects: list of strings
    Returns:
        None
    '''
    # for each string associated with that location in the game
    # dictionary, print that line
    for line in game[location]:
        print(line)

    # check if location has an object associated with it
    for key, value in objects.items():
        # if there's an object associated with this location
        # and the possible action is to take it (0)
        # and user hasn't taken it yet, print message associate with
        # object
        if key[0] == location and key[1] == 0 and key[2] not in player_objects:
            print(value[0])

        # if there's an object associated with this location
        # and we need to check if the user has it (1)
        if key[0] == location and key[1] == 1:
            if key[2] in player_objects:
                # user has the object
                print(value[1])
            else:
                # user does not have the object
                print(value[0])


def go_to_location(location, travel_table, objects, player_objects, answer):
    '''
    This function checks for the user's input (their answer), the objects
    that are available for the users to take, and the objects the user
    has in their object list
    Args:
        location: integer
        travel_table: dictionary with current location, possible to go
                      location and verb that takes user to to go location
        objects: dictionary of location, binary (0 or 1), and object name
        player_objects: list of strings
        answer: input from the user (string)
    Returns:
        next location (integer)
    '''
    # check if user wants to take an object
    if "take" in answer.lower():
        for key in objects:
            # check if there's an object to take
            if key[0] == location and key[1] == 0:
                # add object to user's object list
                player_objects.append(key[2])

    # check if the user needs to have an object to proceed
    for key in objects:
        # if there's a needed object for this location
        # but the user does not have it, return current location 
        # meaning the user doesn't go anywhere
        if key[0] == location and key[1] == 1 and key[2] not in player_objects:
            return location

    # no objects to take or needed to go anywhere
    # check where to go based on user's answer
    for x_y, verb in travel_table.items():
        if x_y[0] == location and verb in answer.upper():
            return x_y[1]


def play_game():
    '''
    This function is the main game playing function.
    It loads all text files for the game, and asks
    for the player's input
    '''
    # load game.txt
    game = load_game()
    # load objects.txt
    objects = load_objects()
    # load travel_table.txt
    travel_table = load_travel_table()
    # player starts with no objects
    player_objects = []
    # player starts at location 0
    location = 0
    # get info for location 0
    get_location(location, game, objects, player_objects)
    # ask if player wants instructions
    answer = input("> ")
    if "y" in answer.lower():
        print_instructions()
    # go to location 1 (start game for real)
    location += 1
    # this is just a demo with 11 locations
    while location < 12:
        # print info on current location
        get_location(location, game, objects, player_objects)
        # request player input
        answer = input("> ")
        # extra line break
        print()
        # player can exit at any time by inputting "exit"
        if "exit" not in answer.lower():
            # player doesn't want to exit
            # get next location based on player's input
            where_to_go = go_to_location(location, travel_table, objects, 
                                      player_objects, answer)
            # if a possible location was found
            if where_to_go:
                # change location
                location = where_to_go
        else: # user entered "exit"
            location = 12
    print("This is the end of this game demo.")


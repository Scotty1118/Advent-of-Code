'''
--- Day 2: Cube Conundrum ---
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
'''





'''this takes the total number of colors per game and cast the strings to ints for of each color and determines if the game is possible'''
def is_possible(numblue, numred, numgreen):
    total_blue = []
    total_red = []
    total_green = []
    possible = False
    for nb in num_blue:
        blue = nb.split()
        if 'blue' in blue[1]:
            total_blue.append(int(blue[0]))
    for nr in num_red:
        red = nr.split()
        if 'red' in red[1]:
            total_red.append(int(red[0]))
    for ng in num_green:
        green = ng.split()
        if 'green' in green[1]:
            total_green.append(int(green[0]))

    for t_b in total_blue:
        if t_b<=14:
            blue=True
        else:
            blue=False
            break
    for t_r in total_red:
        if t_r<=12:
            red=True
        else:
            red=False
            break
    for t_g in total_green:
        if t_g<=13:
            green=True
        else:
            green=False
            break


    if blue and red and green:
        possible=True
    return possible


'''this parses each pull per game each and loops though each element of each pull and groups the colors and the amounts of color together  '''
def color_group(pullspergame):
    '''this parces each pull per game each  '''
    num_blue.clear()
    num_red.clear()
    num_green.clear()

    for t in pullspergame:
        pull = t.split(',')

        blue = "blue"
        red = "red"
        green = "green"

        ''' this loops though each element of each pull and groups the colors and the amounts of color together '''
        for g in range(len(pull)):

            if blue in pull[g]:
                num_blue.append(pull[g])

            if red in pull[g]:
                num_red.append(pull[g])
            if green in pull[g]:
                num_green.append(pull[g])
    return num_blue,num_red,num_green

with open('2023_DAY2.txt', 'r') as games:
    records=[record.strip() for record in games]

    num_blue = []
    num_red = []
    num_green = []
    id_total=0

    '''this loops though the games and splits the game number from the pulls'''

    for game in records:
        gamenumber=game.split(":")
        pullspergame=gamenumber[1].split(';')

        '''parce game id number '''
        gameid=gamenumber[0].split()

        '''this parces each pull per game each and loops though each element of each pull and groups the colors and the amounts of color together  '''
        color_group(pullspergame)

        '''Uses defined function to return if each game is possible '''
        game_status=is_possible(num_blue, num_red, num_green)



        if game_status:
            print(f'  Possible {game_status} {gamenumber[0]}')
            id_total+=int(gameid[1])
        else:
            print(f'Impossible {game_status} {gamenumber[0]}')
    print(f'Part 1 The total Game ID for possible games is {id_total}')



'''--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?'''



'''this takes the total number of colors per game and cast the strings to ints for of each color and gets the max of each color per game and gets the product of them  '''
def power_per_game(numblue, numred, numgreen):
    total_blue = []
    total_red = []
    total_green = []

    for nb in num_blue:
        blue = nb.split()
        if 'blue' in blue[1]:
            total_blue.append(int(blue[0]))
    for nr in num_red:
        red = nr.split()
        if 'red' in red[1]:
            total_red.append(int(red[0]))
    for ng in num_green:
        green = ng.split()
        if 'green' in green[1]:
            total_green.append(int(green[0]))

    few_blue = max(total_blue)
    few_red = max(total_red)
    few_green = max(total_green)
    power= few_blue*few_red*few_green
    return power

'''this parces each pull per game each and loops though each element of each pull and groups the colors and the amounts of color together  '''
def color_group(pullspergame):
    '''this parces each pull per game each  '''
    num_blue.clear()
    num_red.clear()
    num_green.clear()

    for t in pullspergame:
        pull = t.split(',')

        blue = "blue"
        red = "red"
        green = "green"

        ''' this loops though each element of each pull and groups the colors and the amounts of color together '''
        for g in range(len(pull)):

            if blue in pull[g]:
                num_blue.append(pull[g])

            if red in pull[g]:
                num_red.append(pull[g])
            if green in pull[g]:
                num_green.append(pull[g])
    return num_blue,num_red,num_green

with open('2023_DAY2.txt', 'r') as games:
    records=[record.strip() for record in games]

    num_blue = []
    num_red = []
    num_green = []
    answer=[]

    '''this loops though the games and splits the game number from the pulls'''

    for game in records:
        gamenumber=game.split(":")
        pullspergame=gamenumber[1].split(';')

        '''this parces each pull per game each and loops though each element of each pull and groups the colors and the amounts of color together  '''
        color_group(pullspergame)

        '''Uses defined function to return if each game is possible '''
        answer.append(power_per_game(num_blue, num_red, num_green))

    print(f'Part_2 The sum of the Powers {sum(answer)}')
    
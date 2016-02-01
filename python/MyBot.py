#!/usr/bin/env python

from ants import *
from ant import *
from intel import *
from pick import *
from sys import *

# define a class with a do_turn method
# the Ants.run method will parse and update bot input
# it will also run the do_turn method for us
class MyBot:
    def __init__(self):
        # define class level variables, will be remembered between turns
        self.food_locs = {}
        self.hill_locs = {}
        self.hill_location = None
        self.terrain = []
        self.visibility = None
        self.map_rows = None
        self.map_cols = None
        
    # do_setup is run once at the start of the game
    # after the bot has received the game settings
    # the ants class is created and setup by the Ants.run method
    def do_setup(self, ants):
        # initialize data structures after learning the game settings

        #self.terrain = terrain_info(ants)
        self.map_cols = ants.cols #len(ants.map[0])
        self.map_rows = ants.rows #len(ants.map)
        
        self.visibility = [[sys.maxint for col in range(self.map_cols)] for row in range(self.map_rows)]
        
    
    # do turn is run once per turn
    # the ants class has the game state and is updated by the Ants.run method
    # it also has several helper methods to use
    def do_turn(self, ants):
        # loop through all my ants and try to give them orders
        # the ant_loc is an ant location tuple in (row, col) form

        ants.visible((0,0))

        for row in range(self.map_rows):
            for col in range(self.map_cols):
                if ants.vision[row][col]:
                    self.visibility[row][col] = 0
                else:
                    self.visibility[row][col] += 1

        for loc in self.food_locs:
            row, col = loc
            if ants.vision[row][col]:
                pass
        
        for food in ants.food_list:
            self.food_locs[food] = True

                    
        free_ants = [ant for ant in ants.my_ants() if ants.get_food_amount(ant) == 0]
        food_ants = [ant for ant in ants.my_ants() if ants.get_food_amount(ant) > 0]

        for ant in food_ants:
            path = compute_path(ant, self.hill_location)
            ants.issue_order(ant, execute(ant, hill_location, path, ants))
        
        for food in self.food_locs.keys():
            if len(free_ants) > 0:
                ant = pick(food, free_ants)
                path = compute_path(ant, food)
                ants.issue_order(ant, execute(ant, food, path, ants))
                free_ants.remove(ant)
            else:
                break;

        if len(free_ants) > 0:
            #explore
            pass

        
        # for ant_loc in ants.my_ants():
        #     # try all directions in given order
        #     directions = ('n','e','s','w')
        #     for direction in directions:
        #         # the destination method will wrap around the map properly
        #         # and give us a new (row, col) tuple
        #         new_loc = ants.destination(ant_loc, direction)
        #         # passable returns true if the location is land
        #         if (ants.passable(new_loc)):
        #             # an order is the location of a current ant and a direction
        #             ants.issue_order((ant_loc, direction))
        #             # stop now, don't give 1 ant multiple orders
        #             break
        #     # check if we still have time left to calculate more orders
        #     if ants.time_remaining() < 10:
        #         break
            
if __name__ == '__main__':
    # psyco will speed up python a little, but is not needed
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    
    try:
        # if run is passed a class with a do_turn method, it will do the work
        # this is not needed, in which case you will need to write your own
        # parsing function and your own game state class
        Ants.run(MyBot())
    except KeyboardInterrupt:
        print('ctrl-c, leaving ...')

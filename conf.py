from collections import OrderedDict
import sys, getopt, argparse

# ########### GLOBAL CONFIGURATION ############

# appkey and token (see trello api doc to get yours)

# CHANGE THIS !!!!! (otherwise you will see my fantastic TodoList)

# ########### trello2txt CONFIGURATION ############

# Board id (see Trello url)
# CHANGE THIS !!!!!
board = u'MHDVMYyz'

# Possible behaviour
BY_COLOR = 0
BY_NUMBER = 1

# list here the name of  lists to be monitored and the desired behaviour for each list
# list all = BY_COLOR with no color filter specified
# CHANGE THIS !!!!!
toanalyse = OrderedDict()
toanalyse[u'List1_name'] = BY_COLOR
toanalyse[u'List2_name'] = BY_COLOR
toanalyse[u'List3_name'] = BY_NUMBER

# IF you choose a by number behaviour, the number of cards to retrieve
BY_NUMBER_COUNT = 10

# color filter
# List the card colors you wan't to display
# the dic value is a prefix added to the card text in the rendered list
# set an empty dic to display all cards
COLOR_TO_DISPLAY = {}
COLOR_TO_DISPLAY['red'] = '!'
COLOR_TO_DISPLAY['orange'] = ""
# COLOR_TO_DISPLAY[u'yellow']=""
# COLOR_TO_DISPLAY[u'green']=""

# ########### trellomerge CONFIGURATION ############

masterboards = ['MHDVMYyz','yugU3B6P', 'Swk9BQBM', 'v1ScRAKq', 'TjR2jnBP', 'zsUN741N', 'iZyf0GjK', '786lfaUx', 'rSUVxNt5', 'Yr94hDJG']
slaveboard = u'e2n3iU6h'
testboard = u'e2n3iU6h'

# prefix to add to cards copied from the master list
# slavecardsprefix = '[kr] '

# theses slave lists will be sorted by due date and not by priority [default behaviour]
orderbyduedate = ['Calendar']

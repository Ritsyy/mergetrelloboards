from collections import OrderedDict
import sys, getopt, argparse

# ########### GLOBAL CONFIGURATION ############

# appkey and token (see trello api doc to get yours)

# CHANGE THIS !!!!! (otherwise you will see my fantastic TodoList)

appkey = u'baef042af8a9bfc88ffe0227038bdb5a'
secret = u'730d8cff5ae8c5dcff5ec9d79ace2bce6cef6fb7d716db9777fc08acea9058be'
token = u'e973c0dd6fb7636c8325eac7010da5e1f8b4de535c17f4170bade04d9c3536e9'

# ########### trello2txt CONFIGURATION ############

# Board id (see Trello url)
# CHANGE THIS !!!!!
board = u'zBZT2VLZ'

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

masterboards = ['zBZT2VLZ', 'dKMNdKhT', '5noZ6YXd']
slaveboard = u'dn2IAOP1'
testboard = u'dn2IAOP1'

# prefix to add to cards copied from the master list
# slavecardsprefix = '[kr] '

# theses slave lists will be sorted by due date and not by priority [default behaviour]
orderbyduedate = ['Calendar']

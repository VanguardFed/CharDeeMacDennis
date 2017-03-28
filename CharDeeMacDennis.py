#------------------------------------------------------------#
#                                                            #
# CharDee MacDennis                                          #
#                                                            #
# Authors: Trent Thompson, Nicole Riker, Collin Tidwell      #
#                                                            #
# Started: 03-27-2017                                        #
#                                                            #
#------------------------------------------------------------#

# TO-DO:
#   [X] Card class
#   [X] Barebones card display function
#   [ ] Card storage system (PRIORITY)
#       [ ] Card save function (PRIORITY)
#       [ ] Card load function (PRIORITY)
#   [ ] Card submission function (user input)
#   [X] Team class
#   [ ] Team creation function (user input)
#   [?] Team storage system
#   [?] Team editing system
#   [ ] Game set-up function (utilizing card storage system and team creation

class Card:

    #sets up a card with given variables
    def __init__(self,author,level,category,content,tags):
        self.aut=author
        self.lev=level
        self.cat=category
        self.con=content
        self.tag=tags

    #displays a card
    def display(self):
##        blankline="|                                                    |||"
##        characters=len(blankline)
##        print "   "+"_"*(characters-3)
##        print "  /"+("_"*(characters-4))+"/"
##        print " /____________________________________________________/|"
##        print blankline
##        print "|                    Level",self.lev,"                        |||"
        print "Level:",self.lev
        print "Category:",self.cat
        print "Content:",self.con

class Team:

    #sets up a card with given variables
    def __init__(self,name,points,*members):
        self.nom=name
        self.pnt=point
        self.mem=members


# TEST CALLS
test=Card("dev",0,"test","null","N/A")
test.display()

#CharDee MacDennis

class Card:

    #sets up a card with given variables
    def __init__(self,level,category,content):
        self.lev=level
        self.cat=category
        self.con=content

    #displays a card
    def display(self):
        blankline="|                                                    |||"
        characters=len(blankline)
        print "_"*characters
        print "  /"+("_"*(characters-4))+"/"
        print " /____________________________________________________/|"
        print blankline
        print "|                    Level",self.lev,"                        |||"
        print self.lev
        print self.cat
        print self.con
    

test=Card(0,"null","null")
test.display()

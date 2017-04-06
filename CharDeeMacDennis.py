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
'''
    [X] Card class
    [X] Barebones card display function
    [X] Card storage system
        [X] Card save function
        [X] Card load function
    [ ] Card submission function (user input) (PRIORITY)
        [X] Creates and saves valid Card object
        [ ] Ensures valid input
       
    [X] Team class
    [ ] Team creation function (user input) (PRIORITY)
    [?] Team storage system
    [?] Team editing system
    [ ] Game function
        [X] Loads saved deck
        [ ] Sets up teams
        [ ] Randomizes starting team, keeps turn order in the order that they were submitted
        [ ] Turn loop
            [ ] Draws card for current team at current team level
            [ ] Awards or does not award card to teams
            [ ] displays current scores
'''
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

    def play(self):
        self.display()

    #stores all parts of a card into an array and prints it to a file
    def save(self):
        tmp_strg=[]
        tmp_strg.append(self.aut)
        tmp_strg.append(self.lev)
        tmp_strg.append(self.cat)
        tmp_strg.append(self.con)
        tmp_strg.append(self.tag)
        try:
            deck_old=open("deck.cards","r")
            tmp_deck=deck_old.read()
            deck_new=open("deck.cards","w")
            deck_new.write(tmp_deck+str(tmp_strg)+'\n')
            deck_new.close()
        except:
            deck_new=open("deck.cards","w")
            deck_new.write(str(tmp_strg)+'\n')
            deck_new.close()

class Team:

    #sets up a card with given variables
    def __init__(self,name,points,*members):
        self.nom=name
        self.pnt=point
        self.mem=members

        
def load():
    try:
        deck=open("deck.cards","r")
        stack=[]
        for line in deck:
            stack.append(eval(line))
        return stack
    except:
        print "Error: No cards stored"

def create_card():
    submitting=True
    tags=[]
    tmp_aut=raw_input("Who is the author of this card?: ")
    tmp_lev=input("What is the level of this card?: ")
    tmp_cat=raw_input("What category is this card in?: ")
    tmp_con=raw_input("What does this card say?: ")
    while submitting:
        print "Adding 'q' as a tag will quit the submission sequence."
        tmp_tag=raw_input("Add a tag to the card: ")
        if tmp_tag.lower()=='q':
            submitting=False
        else:
            tags.append(tmp_tag)
    tmpCard=Card(tmp_aut,tmp_lev,tmp_cat,tmp_con,tags)
    tmpCard.save()
        
def game():
    deck=load()
    if raw_input("Welcome to Chardee MacDennis, press enter to continue. ")=='submit':
        submitting=True
        while submitting:
            create_card()
            if raw_input("Do you want to submit another card? (y/n): ").lower()!='y':
                submitting=False
    else:
        print "Game sequence here"
game()

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

        
##def load():
##    try:
##        deck=open("deck.cards","r")
##        i=0
##        for line in deck:
##            stack=[]
##            stack.append(deck.readline())
##            i+=1
##        return stack
##    except:
##        print "Error: No cards stored"

# TEST CALLS
test=Card("dev",0,"test","null",["N/A","test","nonvalid1"])
test2=Card("dev",0,"test","null",["N/A","save test","nonvalid2"])
test.display()
test.save()
test2.save()

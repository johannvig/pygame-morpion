import pygame


class Grid:

    def __init__(self, ecran):

        self.ecran = ecran

        #create the position of the lines

        self.lignes=[((200,0),(200,600)),
                     ((400,0),(400,600)),
                     ((0,200),(600,200)),
                     ((0,400),(600,400)),]

        #initialisation of the grid
        #after we will change the value of None by X or 0 according to the player
        self.grid=[[None for x in range(0,3)] for y in range(0,3)]

        #initiate a variable to know if the counter is "ON"

        self.counter_on = False


    def show(self):

        for ligne in self.lignes:

            #define the color, thickness of the lines
            
            pygame.draw.line(self.ecran, (23,145,135), ligne[0], ligne[1], 15)


            #show "X" and "O"
            for y in range(0,len(self.grid)):
                for x in range(0, len(self.grid)):
                    if self.grid[y][x] == "X":
                        pygame.draw.line(self.ecran, (66,66,66), (x * 200 + 55, y * 200 + 200 - 55), (x * 200 + 200 - 55, y * 200 + 55), 25)
                        pygame.draw.line(self.ecran, (66,66,66), (x * 200 + 55, y * 200 +55), (x * 200 + 200 - 55, y * 200 + 200 - 55), 25)

                    elif self.grid[y][x] == "O":

                        pygame.draw.circle(self.ecran, (239,231,200), (100 + (x * 200), 100 + (y * 200)), 60, 15)




    def fix_value(self,x,y,value):


        #if a box has a None value
        if self.grid[y][x]==None:
            self.grid[y][x]= value
            #the counter is "ON"
            self.counter_on=True


    #set the value to None

    def set_None(self,row,column,value):

        self.grid[row][column] = value






class morpion:

    def __init__(self):

        #define the size of the screen
        self.ecran = pygame.display.set_mode((600, 600))

        #name the game "morpion"
        pygame.display.set_caption("morpion")


        # for the loop
        # allows you to play continuously
        self.jeu_en_cours =True


        self.grid= Grid(self.ecran)

        #variable X and 0

        self.player_X="X"
        self.player_O = "O"

        #fix the counter

        self.counter = 0

        self.ecran_debut = True


    def main(self):

        while self.jeu_en_cours:

            while self.ecran_debut:
                for event in pygame.event.get():

                    # allow to leave the game
                    if event.type == pygame.QUIT:
                        self.jeu_en_cours = False


                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.ecran_debut = False


                self.ecran.fill((28, 170, 156))

                self.show_message('big','Morpion',(0,0,0), [200,30,200,50])

                self.show_message('medium', 'Tap:', (0, 0, 0), [70, 150, 200, 50])

                self.show_message('small', '1    player vs player mode', (0, 0, 0), [70, 200, 200, 50])

                self.show_message('small', '2    player vs IA mode', (0, 0, 0), [70, 250, 300, 50])

                self.show_message('small', 'SPACE     Start the game', (0, 0, 0), [70, 350, 200, 50])

                self.show_message('small', 'ESC       Return to this screen', (0, 0, 0), [70, 400, 200, 50])

                self.show_message('small', 'ENTER     Restart a game', (0, 0, 0), [70, 450, 200, 50])

                pygame.display.flip()

            #event processing
            for event in pygame.event.get():

                #allow to leave the game
                if event.type == pygame.QUIT:
                    self.jeu_en_cours = False

                #event when you make a right click
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:

                    #allows to get the position of the mouse when you click on a place (x,y)
                    position= pygame.mouse.get_pos()

                    #show position which corresponds to the box
                    position_x, position_y= position[0]//200, position[1]//200


                    #know if the counter is odd or even
                    if self.counter % 2 == 0:
                        self.grid.fix_value(position_x, position_y, self.player_X)
                    else:
                        self.grid.fix_value(position_x, position_y, self.player_O)

                    #if the counter "ON" is True
                    if self.grid.counter_on:
                        self.counter+=1

                        self.grid.counter_on=False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.reset_morpion()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.ecran_debut =True

            # color of the screen
            self.ecran.fill((28, 170, 156))


            liste_X=[]
            liste_O=[]
            liste_row_X=[]
            liste_column_X = []
            liste_row_O = []
            liste_column_O = []


            for line in range(0, len(self.grid.grid)):
                for column in range(0, len(self.grid.grid)):

                    if self.grid.grid[line][column] == "X":

                        X_position = (line,column)
                        liste_X.append(X_position)

                    if self.grid.grid[line][column] == "O":

                        O_position = (line,column)
                        liste_O.append(O_position)

            if len(liste_X)>=3:
                for (line,column) in liste_X:
                    liste_row_X.append(line)
                    liste_column_X.append(column)


                if liste_row_X.count(0)==3 or liste_row_X.count(1)==3 or liste_row_X.count(2)==3:
                    print("X gagne")

                if liste_column_X.count(0)==3 or liste_column_X.count(1)==3 or liste_column_X.count(2)==3:
                    print("X gagne")

                if liste_row_X==liste_column_X or liste_row_X==liste_column_X[::-1]:
                    print("X gagne")



            if len(liste_O)>=3:
                for (line,column) in liste_O:
                    liste_row_O.append(line)
                    liste_column_O.append(column)


                if liste_row_O.count(0)==3 or liste_row_O.count(1)==3 or liste_row_O.count(2)==3:
                    print("O gagne")

                if liste_column_O.count(0)==3 or liste_column_O.count(1)==3 or liste_column_O.count(2)==3:
                    print("O gagne")

                if liste_row_O==liste_column_O or liste_row_O==liste_column_O[::-1]:
                    print("O gagne")

            # make the lines of the game appear
            self.grid.show()

            # update the screen
            pygame.display.flip()



    def reset_morpion(self):

        for row in range(0, len(self.grid.grid)):
            for column in range(0, len(self.grid.grid)):
                self.grid.set_None(row,column,None)
                morpion.__init__(self)


    def show_message(self,font, message, color,message_rectangle):

        if font == "small":

            font= pygame.font.SysFont('impact', 20, False)

        if font == "medium":

            font= pygame.font.SysFont('impact', 30, False)

        if font == "big":

            font= pygame.font.SysFont('arial', 40, True)

        message = font.render(message, False, color)

        self.ecran.blit(message, message_rectangle)



if __name__ == '__main__':
    pygame.init()
    morpion().main()
    pygame.quit()

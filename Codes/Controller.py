    def wait_click():
        '''Get user input and return the x,y coordinates in pixels where user clicked'''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit() # Force quit the game by closing window


            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                print("mouse clicked -> (" + str(x) + ", " + str(y) + ")") #Temp output to check the clicked position
                return (x,y)

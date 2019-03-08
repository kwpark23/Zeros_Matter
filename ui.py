import pygame

 class Gui:
    """ Create the graphics of the game. """

HUMAN = "human"
BLACK = 1
WHITE = 2


class Gui:
    def __init__(self):
        """ Initializes graphics. """

        pygame.init()

        # colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.TEAL = (112, 174, 199)

        # display
        self.SCREEN_SIZE = (640, 480)
        self.BOARD_POS = (100, 20) #8 by 8 board
        self.BOARD = (120, 40) #pieces
        self.BOARD_SIZE = 400
        self.SQUARE_SIZE = 50
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        # messages
        self.BLACK_LABEL_POS = (25, self.SCREEN_SIZE[1] / 4)
        self.WHITE_LABEL_POS = (540, self.SCREEN_SIZE[1] / 4)
        self.font = pygame.font.SysFont("Avenir", 50)
        self.scoreFont = pygame.font.SysFont("Avenir", 58)

        # image files
        self.board_img = pygame.image.load(os.path.join("images", "board.bmp")).convert()
        self.black_img = pygame.image.load(os.path.join("images", "black.bmp")).convert()
        self.white_img = pygame.image.load(os.path.join("images", "white.bmp")).convert()
        self.tip_img = pygame.image.load(os.path.join("images", "tip.bmp")).convert()
        self.clear_img = pygame.image.load(os.path.join("images", "blank.bmp")).convert()

     def title_screen(self):
        """
        Make title screen according to design requirements:
        - background: black fill, blue borders
        - image: black and white circles
        - font: Avenir, blue, 50/80/150 px, centre alignment
        """

         # Objects
        self.screen.fill(0, 0, 0)
        pygame.draw.rect(self.screen, (97, 148, 175), pygame.Rect(20, 20, 610, 430), 10)
        pygame.draw.circle(self.screen, (255, 255, 255), (340, 270), 30, 0)
        pygame.draw.circle(self.screen, (255, 255, 255), (300, 250), 30, 3)
        pygame.draw.circle(self.screen, (0, 0, 0), (300, 250), 30, 0)

         # Title label
        title_fnt = pygame.font.SysFont("Avenir", 150)
        title = title_fnt.render("Flipsies", True, (97, 148, 175))
        title_pos = title.get_rect(centerx=self.screen.get_width() / 2, centery=160)

         # Start label
        start_fnt = pygame.font.SysFont("Avenir", 80)
        start_txt = start_fnt.render("PLAY", True, (97, 148, 175))
        start_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2, centery=350)

         # Instructions label
        ins_fnt = pygame.font.SysFont("Avenir", 50)
        ins_txt = ins_fnt.render("How to play", True, (97, 148, 175))
        ins_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2.3, centery=430)

         # Add all to screen
        self.screen.blit(title, title_pos)
        self.screen.blit(start_txt, start_pos)
        self.screen.blit(ins_txt, ins_pos)

         pygame.display.flip()
            
    def wait_quit(self):
        """Waits until a player has chosen to quit, then
        quits game.

        """
        # wait user to close window
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break

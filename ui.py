import pygame

class Gui:
    """ Create the graphics of the game. """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))

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
        title = title_fnt.render("Flipsies", True, self.TEAL)
        title_pos = title.get_rect(centerx=self.screen.get_width() / 2, centery=160)

        # Start label
        start_fnt = pygame.font.SysFont("Avenir", 80)
        start_txt = start_fnt.render("PLAY", True, self.TEAL)
        start_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2, centery=350)

        # Instructions label
        ins_fnt = pygame.font.SysFont("Avenir", 50)
        ins_txt = ins_fnt.render("How to play", True, self.TEAL)
        ins_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2.3, centery=430)

        # Add all to screen
        self.screen.blit(title, title_pos)
        self.screen.blit(start_txt, start_pos)
        self.screen.blit(ins_txt, ins_pos)

        pygame.display.flip()

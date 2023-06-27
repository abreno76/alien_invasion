import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        gf.check_events(ship)

        ship.update()

        # Redesenha a tela a cada passagem pelo laço
        gf.update_screen(ai_settings, screen, ship)
        
run_game()
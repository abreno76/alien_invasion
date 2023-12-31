import pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStats
from settings import Settings
from ship import Ship


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()

    # Cria um grupo no qual serão armazenados os alienigenas
    aliens = Group()

    # Cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Cria um alienígena
    # alien = Alien(ai_settings, screen)

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # Redesenha a tela a cada passagem pelo laço
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
run_game()
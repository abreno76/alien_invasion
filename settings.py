class Settings():
    """Uma classe para armazenar todas as configurações da Invasão
    Alienígena."""
    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) # Define a cor de fundo

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Configurações dos projéteis
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Configurações dos alienígenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5

        # fleet_direction igual a 1 representa a direita; -1 representa
        # a esquerda
        self.fleet_direction = 1
        
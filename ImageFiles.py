import pygame
import Helper

pygame.init()

screen = pygame.display.set_mode(Helper.RESOLUTION, 0, 32)

images = dict()
images['Tilemap'] = pygame.image.load(
    './Resources/Visual/Tilemaps/tilemap_export.png'
    ).convert_alpha()

images['DeadTree'] = pygame.image.load(
    './Resources/Visual/Sprites/dead_tree.png'
    ).convert_alpha()

images['Background'] = pygame.image.load(
    './Resources/Visual/Rooms/room.png'
    )

images['Player'] = pygame.image.load(
    './Resources/Visual/Sprites/player.png'
    ).convert_alpha()

images['Player_Attack'] = pygame.image.load(
    './Resources/Visual/Sprites/player_attack.png'
    ).convert_alpha()

images['Enemy_Attack'] = pygame.image.load(
    './Resources/Visual/Sprites/enemy_attack.png'
    ).convert_alpha()


images['Enemy'] = pygame.image.load(
    './Resources/Visual/Sprites/enemy.png'
    ).convert_alpha()

images['Handle'] = pygame.image.load(
    './Resources/Visual/Items/handle.png'
    ).convert_alpha()

images['Blade'] = pygame.image.load(
    './Resources/Visual/Items/blade.png'
    ).convert_alpha()

images['Bonus'] = pygame.image.load(
    './Resources/Visual/Items/bonus.png'
    ).convert_alpha()

images['Handle_Thumbnail'] = pygame.image.load(
    './Resources/Visual/Items/handle_thumbnail.png'
    ).convert_alpha()

images['Blade_Thumbnail'] = pygame.image.load(
    './Resources/Visual/Items/blade_thumbnail.png'
    ).convert_alpha()

images['Bonus_Thumbnail'] = pygame.image.load(
    './Resources/Visual/Items/bonus_thumbnail.png'
    ).convert_alpha()

images['Potion_Spirit'] = pygame.image.load(
    './Resources/Visual/Items/spirit.png'
    ).convert_alpha()

images['Potion_Body'] = pygame.image.load(
    './Resources/Visual/Items/body.png'
    ).convert_alpha()

images['Rooms'] = dict(
            Tutorial=pygame.image.load(
                './Resources/Visual/Rooms/room.png').convert_alpha()
                        )

images['UI'] = dict(
        Inventory_Background=pygame.image.load(
            './Resources/Visual/UI/inv_background.png').convert_alpha(),
        GameOverScreen=pygame.image.load(
            './Resources/Visual/UI/game_over.png').convert_alpha()
                    )

images['Enemies'] = [
    pygame.image.load(
        './Resources/Visual/Sprites/enemy.png'
        )]

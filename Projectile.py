import pygame
import ImageFiles
import Helper
import Player
import Entity

pygame.init()
DISPLAY_SURFACE = Helper.DISPLAY_SURFACE

attackSprites = []


class EnemyProjectile:

    projectile_speed = 10  # Put in Helper at a later point

    def __init__(self, lane, parent_enemy):
        self.sprite = ImageFiles.images['Enemy_Attack']
        self.rect = self.sprite.get_rect()
        self.lane = lane
        self.damage = parent_enemy.damage()

        print('this will deal '
              + str(self.damage)
              + ' to the player with '
              + str(Player.Player.health) + 'hp')

        self.pos_y = self.rect.y = Helper.LANES[lane][0][1] \
                                   - int(self.rect.height/2)
        self.pos_x = self.rect.x = Helper.LANES[lane][0][0] \
                                   - int(self.rect.width/2)

        attackSprites.append(self)

    def update(self):

        collision_with_player = False

        if self.rect.colliderect(Player.Player.playerRect):
            collision_with_player = True
            Player.Player.is_hit(self.damage)

        if self.pos_y < 1334 and collision_with_player is False:
            self.pos_y += EnemyProjectile.projectile_speed
            self.rect.y += EnemyProjectile.projectile_speed
        elif self.pos_y >= 1334 and collision_with_player is False:
            attackSprites.remove(self)
        elif collision_with_player is True:
            attackSprites.remove(self)
            del self


class PlayerProjectile:

    projectile_speed = Helper.PROJECTILE_SPEED

    def __init__(self, lane):
        PlayerProjectile.projectile_speed = Player.Player.projectileSpeed
        self.sprite = ImageFiles.images['Player_Attack']
        self.rect = self.sprite.get_rect()
        self.lane = lane
        self.damage = Player.Player.weaponEquipped.damage \
            if Player.Player.weaponEquipped \
            else Player.Player.baseDamage

        print('this will deal '
              + str(self.damage)
              + ' to the enemy it hits')

        self.pos_x = self.rect.x = Player.Player.playerPos[0] + self.rect.width/2
        self.pos_y = self.rect.y = Player.Player.playerPos[1] + self.rect.height/2

        attackSprites.append(self)

    def update(self):

        collision_with_enemy = False

        for enemy in Entity.enemy_list:
            if self.rect.colliderect(enemy.rect):
                collision_with_enemy = True
                enemy.is_hit(self.damage)

        if self.pos_y > 0 and collision_with_enemy is False:
            self.pos_y -= PlayerProjectile.projectile_speed
            self.rect.y -= PlayerProjectile.projectile_speed
        elif self.pos_y <= 0 and collision_with_enemy is False:
            attackSprites.remove(self)
        elif collision_with_enemy is True:
            attackSprites.remove(self)
            del self


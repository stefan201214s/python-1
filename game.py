import pygame
import math
import random
pygame.init()
selected_tower_obj = None

# =========================
# CONFIG
# =========================

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# =========================
# COULEURS
# =========================

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
BLUE = (50, 100, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
BROWN = (160, 110, 60)
GRASS = (40, 180, 40)

# =========================
# CHEMIN
# =========================

path = [
    (0, 100),
    (250, 100),
    (250, 250),
    (600, 250),
    (600, 500),
    (900, 500)
]

base_pos = (950, 500)

# =========================
# JOUEUR
# =========================

money = 300
base_hp = 20

selected_tower = 1

MAX_TOWERS = 20

# =========================
# TOURELLES
# =========================

tower_types = {
    1: {
        "cost": 50,
        "range": 120,
        "damage": 8,
        "speed": 40,
        "color": BLUE
    },

    2: {
        "cost": 100,
        "range": 150,
        "damage": 15,
        "speed": 35,
        "color": GREEN
    },

    3: {
        "cost": 150,
        "range": 180,
        "damage": 25,
        "speed": 30,
        "color": RED
    },

    4: {
        "cost": 250,
        "range": 220,
        "damage": 40,
        "speed": 25,
        "color": YELLOW
    },

    5: {
        "cost": 400,
        "range": 280,
        "damage": 70,
        "speed": 20,
        "color": BLACK
    },

    6: {
        "cost": 700,
        "range": 320,
        "damage": 120,
        "speed": 18,
        "color": (0, 255, 255)  # cyan
    },

    7: {
        "cost": 1200,
        "range": 360,
        "damage": 200,
        "speed": 15,
        "color": (255, 0, 255)  # violet
    },

    8: {
        "cost": 2000,
        "range": 420,
        "damage": 350,
        "speed": 12,
        "color": (255, 140, 0)  # orange
    }
}


# =========================
# CLASSES
# =========================

class Enemy:

    def __init__(self, wave):

        self.x, self.y = path[0]
        self.path_index = 1

        # Boss toutes les 5 vagues

        if wave % 5 == 0:

            self.enemy_type = "boss"

            self.color = (180, 0, 255)

            self.max_hp = 400 + wave * 50
            self.speed = 1.5

            self.reward = 150

        else:

            r = random.randint(1, 3)

            if r == 1:

                self.enemy_type = "normal"

                self.color = RED

                self.max_hp = 50 + wave * 8
                self.speed = 2.5

                self.reward = 15

            elif r == 2:

                self.enemy_type = "fast"

                self.color = YELLOW

                self.max_hp = 30 + wave * 5
                self.speed = 4

                self.reward = 20

            else:

                self.enemy_type = "tank"

                self.color = GRAY

                self.max_hp = 120 + wave * 20
                self.speed = 1.5

                self.reward = 40

        self.hp = self.max_hp

    def update(self):

        global base_hp

        if self.path_index >= len(path):
            base_hp -= 1
            return False

        target_x, target_y = path[self.path_index]

        dx = target_x - self.x
        dy = target_y - self.y

        dist = math.hypot(dx, dy)

        if dist < self.speed:

            self.x = target_x
            self.y = target_y

            self.path_index += 1

        else:

            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed

        return True

    def draw(self):

        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            15
        )

        pygame.draw.rect(
            screen,
            RED,
            (self.x - 20, self.y - 30, 40, 5)
        )

        pygame.draw.rect(
            screen,
            GREEN,
            (
                self.x - 20,
                self.y - 30,
                40 * (self.hp / self.max_hp),
                5
            )
        )


class Bullet:

    def __init__(self, x, y, target, damage):

        self.x = x
        self.y = y

        self.target = target
        self.damage = damage

        self.speed = 8

    def update(self):

        if self.target not in enemies:
            return False

        dx = self.target.x - self.x
        dy = self.target.y - self.y

        dist = math.hypot(dx, dy)

        if dist < self.speed:

            self.target.hp -= self.damage
            return False

        self.x += dx / dist * self.speed
        self.y += dy / dist * self.speed

        return True

    def draw(self):

        pygame.draw.circle(
            screen,
            BLACK,
            (int(self.x), int(self.y)),
            4
        )


class Tower:

    def __init__(self, x, y, tower_type):
        self.level = 1
        self.x = x
        self.y = y

        self.tower_type = tower_type

        data = tower_types[tower_type]

        self.cost = data["cost"]
        self.range = data["range"]
        self.damage = data["damage"]
        self.speed = data["speed"]
        self.color = data["color"]

        self.cooldown = 0

    def update(self):

        if self.cooldown > 0:
            self.cooldown -= 1

        if self.cooldown == 0:

            target = None

            for enemy in enemies:

                dist = math.hypot(
                    enemy.x - self.x,
                    enemy.y - self.y
                )

                if dist <= self.range:
                    target = enemy
                    break

            if target:

                bullets.append(
                    Bullet(
                        self.x,
                        self.y,
                        target,
                        self.damage
                    )
                )

                self.cooldown = self.speed

    def draw(self):

        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            18
        )

    def upgrade(self):
        self.level += 1

        self.damage = int(self.damage * 1.5)
        self.range = int(self.range * 1.2)

        self.cooldown = max(10, self.speed - 5)

# =========================
# LISTES
# =========================

enemies = []
towers = []
bullets = []

# =========================
# VAGUES
# =========================

wave = 1

enemies_to_spawn = 5
enemies_spawned = 0

spawn_timer = 0

between_waves = False
wave_timer = 180

# =========================
# JEU
# =========================

running = True

while running:

    clock.tick(60)

    # =====================
    # EVENTS
    # =====================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        # ======================
        # CLAVIER
        # ======================
    
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                selected_tower = 1

            elif event.key == pygame.K_2:
                selected_tower = 2

            elif event.key == pygame.K_3:
                selected_tower = 3

            elif event.key == pygame.K_4:
                selected_tower = 4

            elif event.key == pygame.K_5:
                selected_tower = 5
            
            elif event.key == pygame.K_6:
                selected_tower = 6

            elif event.key == pygame.K_7:
                selected_tower = 7

            elif event.key == pygame.K_8:
                selected_tower = 8

        # ======================
        # SOURIS
        # ======================

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            if event.button == 1:

                if selected_tower_obj:

                    # bouton upgrade (zone écran gauche)
                    if 10 <= mx <= 200 and 200 <= my <= 250:

                        upgrade_cost = 100 * selected_tower_obj.level

                        if money >= upgrade_cost:

                            money -= upgrade_cost
                            selected_tower_obj.upgrade()

                # ======================
                # SELECTION TOUR
                # ======================
                selected_tower_obj = None

                for tower in towers:
                    dist = math.hypot(mx - tower.x, my - tower.y)

                    if dist <= 20:
                        selected_tower_obj = tower
                        break

                # Placement
                if selected_tower and selected_tower_obj is None:

                    cost = tower_types[selected_tower]["cost"]

                    if (
                        money >= cost and
                        len(towers) < MAX_TOWERS
                    ):

                        towers.append(
                            Tower(mx, my, selected_tower)
                        )

                        money -= cost

            elif event.button == 3:

                for tower in towers[:]:

                    dist = math.hypot(
                        mx - tower.x,
                        my - tower.y
                    )

                    if dist <= 20:

                        refund = int(
                            tower.cost * 0.40
                        )

                        money += refund

                        towers.remove(tower)

                        break

    # =====================
    # SPAWN
    # =====================

    if not between_waves:

        spawn_timer += 1

        if (
            spawn_timer >= 60 and
            enemies_spawned < enemies_to_spawn
        ):

            enemies.append(
                Enemy(wave)
            )

            enemies_spawned += 1
            spawn_timer = 0

        if (
            enemies_spawned >= enemies_to_spawn and
            len(enemies) == 0
        ):

            between_waves = True

    # =====================
    # VAGUE SUIVANTE
    # =====================

    if between_waves:

        wave_timer -= 1

        if wave_timer <= 0:

            wave += 1

            enemies_to_spawn += 3

            enemies_spawned = 0

            wave_timer = 180

            between_waves = False

    # =====================
    # UPDATE ENNEMIS
    # =====================

    alive = []

    for enemy in enemies:

        if enemy.hp <= 0:

            money += enemy.reward
            continue

        if enemy.update():
            alive.append(enemy)

    enemies = alive

    # =====================
    # UPDATE TOURS
    # =====================

    for tower in towers:
        tower.update()

    # =====================
    # UPDATE BALLES
    # =====================

    alive_bullets = []

    for bullet in bullets:

        if bullet.update():
            alive_bullets.append(bullet)

    bullets = alive_bullets

    # =====================
    # DESSIN
    # =====================

    screen.fill(GRASS)

    pygame.draw.lines(
        screen,
        BROWN,
        False,
        path,
        40
    )

    pygame.draw.rect(
        screen,
        BLUE,
        (
            base_pos[0] - 25,
            base_pos[1] - 25,
            50,
            50
        )
    )

    for tower in towers:
        tower.draw()

    for enemy in enemies:
        enemy.draw()

    for bullet in bullets:
        bullet.draw()

    pygame.draw.rect(
        screen,
        GRAY,
        (0, 0, WIDTH, 40)
    )

    hud = font.render(
        f"Argent: {money} | Base HP: {base_hp} | Vague: {wave} | Tours: {len(towers)}/{MAX_TOWERS}",
        True,
        WHITE
    )

    screen.blit(hud, (10, 10))

    info_y = 50

    for i in tower_types:

        txt = font.render(
            f"{i} = Tour {i} ({tower_types[i]['cost']}$)",
            True,
            BLACK
        )

        screen.blit(txt, (10, info_y))
        info_y += 25

    if between_waves:

        txt = font.render(
            "Preparation prochaine vague...",
            True,
            YELLOW
        )

        screen.blit(txt, (350, 50))

    if base_hp <= 0:

        over = pygame.font.SysFont(
            None,
            80
        ).render(
            "GAME OVER",
            True,
            RED
        )

        screen.blit(
            over,
            (
                WIDTH // 2 - 180,
                HEIGHT // 2
            )
        )

        if selected_tower_obj:

            pygame.draw.rect(screen, (30, 30, 30), (0, 40, 220, 200))

            txt1 = font.render("TOUR SELECTIONNEE", True, WHITE)
            screen.blit(txt1, (10, 50))

            txt2 = font.render(f"Degats: {selected_tower_obj.damage}", True, WHITE)
            screen.blit(txt2, (10, 80))

            txt3 = font.render(f"Range: {selected_tower_obj.range}", True, WHITE)
            screen.blit(txt3, (10, 110))

            txt4 = font.render(f"Niveau: {selected_tower_obj.level}", True, WHITE)
            screen.blit(txt4, (10, 140))

            upgrade_cost = 100 * selected_tower_obj.level

            txt5 = font.render(f"Upgrade: {upgrade_cost}$", True, YELLOW)
            screen.blit(txt5, (10, 1700))

    pygame.draw.rect(screen, BLUE, (10, 280, 180, 40))
    txt6 = font.render("AMELIORER", True, WHITE)
    screen.blit(txt6, (20, 210))

    pygame.display.flip()

    

    pygame.display.flip()

pygame.quit()
from pgzero.actor import Actor


class Pacman:
    def __init__(self, keys):
        self.images = ['pacman_o', 'pacman_or', 'pacman_c', 'pacman_cr']
        self.keys = keys
        self.keys_active = {'right': False, 'up': False, 'left': False, 'down': False}
        self.pacman = Actor('pacman_o')
        self.pacman.x = 290
        self.pacman.y = 570
        self.lives = 3

    def on_key_down(self, key):
        if key == self.keys.RIGHT:
            self.keys_active['right'] = True
        if key == self.keys.UP:
            self.keys_active['up'] = True
        if key == self.keys.LEFT:
            self.keys_active['left'] = True
        if key == self.keys.DOWN:
            self.keys_active['down'] = True

    def on_key_up(self, key):
        if key == self.keys.RIGHT:
            self.keys_active['right'] = False
        if key == self.keys.UP:
            self.keys_active['up'] = False
        if key == self.keys.LEFT:
            self.keys_active['left'] = False
        if key == self.keys.DOWN:
            self.keys_active['down'] = False

    def draw(self, screen):
        self.pacman.draw()
        for live in range(self.lives):
            screen.blit('pacman_o', (10 + live * 40, 30))

    def move_pressed(self):
        pressed = any(value for value in self.keys_active.values())
        return pressed

    def update(self):
        move_pressed = self.move_pressed()
        #  Animacja pacmana

        straight_pacman_image = 'pacman_o'
        flipped_pacman_image = 'pacman_or'

        if self.keys_active['right']:
            self.pacman.x += 1
            self.pacman.image = straight_pacman_image
            self.pacman.angle = 0
        if self.keys_active['up']:
            self.pacman.y -= 1
            self.pacman.image = flipped_pacman_image
            self.pacman.angle = 90
        if self.keys_active['left']:
            self.pacman.x -= 1
            self.pacman.image = straight_pacman_image
            self.pacman.angle = 180
        if self.keys_active['down']:
            self.pacman.y += 1
            self.pacman.image = flipped_pacman_image
            self.pacman.angle = 270

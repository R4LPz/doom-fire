import pygame
import random

from collor_pallet import ColorsPalette

class DoomFire():

    def __init__(self, width, height, pixel_size, decay_rate, wind_force, colors = ColorsPalette()):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.decay_rate = decay_rate
        self.wind_force = wind_force
        self.pixel_array = [0] * self.width * self.height
        self.colors = colors
        self.logo = pygame.image.load('doom-logo.png')
        self.logo_x = self.width * self.pixel_size / 2 - self.logo.get_width() / 2
        self.logo_y = self.height * self.pixel_size

    def create_fire_source(self):
        self.pixel_array[-self.width:] = [36] * self.width

    def calculate_fire_propagation(self):
        for column in range(self.width):
            for row in range(self.height-1):
                current_pixel_index = column + row * self.width
                below_pixel_index = current_pixel_index + self.width
                below_pixel_intensity = self.pixel_array[below_pixel_index]
                current_pixel_intensity = 0
                decay = random.randint(0, self.decay_rate)
                wind_direction = random.randint(-self.wind_force, self.wind_force)                
                if below_pixel_intensity - decay > 0 :
                    current_pixel_intensity = below_pixel_intensity - decay
                if current_pixel_index + wind_direction >= len(self.pixel_array) or \
                    current_pixel_index + wind_direction < 0:
                    wind_direction = -wind_direction    
                self.pixel_array[current_pixel_index + wind_direction] = current_pixel_intensity
    
    def render(self,screen):
        for row in range(self.height):
            for column in range(self.width):
                pixel_index = column + row * self.width
                pixel_intensity = self.pixel_array[pixel_index]
                color = self.colors.get_color(pixel_intensity)
                pixel_rect = (column * self.pixel_size, row * self.pixel_size, self.pixel_size, self.pixel_size)
                pygame.draw.rect(screen,color,pixel_rect)
        
        if self.logo_y >= self.height * self.pixel_size / 2 - self.logo.get_height() / 2:
            self.logo_y = self.logo_y - 3
        screen.blit(self.logo, (self.logo_x, self.logo_y))
        

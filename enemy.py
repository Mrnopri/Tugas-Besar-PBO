import pygame

# Inisialisasi Pygame
pygame.init()

# Lebar dan tinggi window game
screen_width = 1280
screen_height = 700

#font
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render('Game Over', False, 'black')

# Warna
white = (255, 255, 255)

# Inisialisasi window game
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jungle Dash")

game_active=True

# karakter Mario
mario_surface = pygame.image.load('idle.gif')
mario_rect = mario_surface.get_rect(midbottom=(100, 700))
mario_gravity = 50

# # Koordinat karakter Mario
mario_x = 50
mario_y = screen_height - 100


# Kecepatan karakter Mario
mario_speed = 70

# # Kecepatan vertikal dan gravitasi
vertical_speed = 0


# Batas map
map_limit_left = 0
map_limit_right = screen_width - 50

# rintangan
rintangan_surface = pygame.image.load('idle.gif')
rintangan_rect = rintangan_surface.get_rect(bottomright=(700, 600))

# Main loop
running = True
while running:
    # Clear layar dengan warna putih
    screen.fill(white)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            # Menggerakkan karakter Mario
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_SPACE and mario_rect.bottom >= 700:
                    mario_gravity = -40
                if keys[pygame.K_LEFT]:
                    mario_rect.x -= mario_speed
                    if mario_rect.x < map_limit_left:
                        mario_rect.x = map_limit_left
                if keys[pygame.K_RIGHT]:
                    mario_rect.x += mario_speed
                    if mario_rect.x > map_limit_right:
                        mario_rect.x = map_limit_right
                if keys[pygame.K_DOWN]:
                    mario_rect.y += mario_speed
                    if mario_rect.y > map_limit_right:
                        mario_rect.y = map_limit_right
        else :
            if event.type == pygame.KEYDOWN and event.key  == pygame.K_SPACE:
                game_active = True

    # Membatasi pemain di dalam batas map
    if mario_rect.y > screen_height - 50:
        mario_rect.y = screen_height - 50
        vertical_speed = 2

    # game start
    if game_active:
        # Menggambar karakter Mario
        mario_gravity += 1
        mario_rect.y += mario_gravity
        if mario_rect.bottom >= 700: mario_rect.bottom = 700
        screen.blit(mario_surface, mario_rect)

        # memanggil perintah rintangan surface
        screen.blit(rintangan_surface, rintangan_rect)

        # Membuat rintangan bergerak
        rintangan_rect.x -= 0
        if rintangan_rect.right <= 0:
            rintangan_rect.left = 1320

        # Collision (tabrakan)
        if rintangan_rect.colliderect(mario_rect):
            game_active = False
    else:
        screen.fill('black')

    # Update layar
    pygame.display.flip()
    screen.blit(text_surface, (250, 100))
    

# Keluar dari game
pygame.quit()
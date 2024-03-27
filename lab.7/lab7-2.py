import pygame
import os

pygame.init()
L, H = 500, 400
screen = pygame.display.set_mode((L, H))
pygame.display.set_caption('Music player')
running = True
music_dir = r"C:\Users\akim0\Desktop\music"
music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
current_index = 0
pygame.mixer.music.load(os.path.join(music_dir, music_files[current_index]))
pygame.mixer.music.play()
font = pygame.font.Font(None, 36)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                current_index = (current_index + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_index = (current_index - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_index]))
                pygame.mixer.music.play()
    screen.fill((255, 255, 255))
    current_track = font.render(music_files[current_index], True, (0, 0, 0))
    screen.blit(current_track, (10, 10))
    pygame.display.flip()
pygame.quit()

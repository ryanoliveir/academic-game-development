import pygame
import random
import os

class MemeHandler:
    def __init__(self):
        # Define directories for memes
        self.capture_memes = self.load_memes(os.path.join('memecheckers/assets','midia', 'capture'))
        self.queen_memes = self.load_memes(os.path.join('memecheckers/assets','midia', 'queen'))
        self.invalid_move_memes = self.load_memes(os.path.join('memecheckers/assets','midia', 'invalid_moves'))
        self.multi_capture_memes = self.load_memes(os.path.join('memecheckers/assets','midia', 'multi_capture'))
        # self.time_memes = os.path.join('memecheckers/assets','midia', 'time')
        self.winn_memes = self.load_memes(os.path.join('memecheckers/assets','midia', 'winner'))
    def load_memes(self, directory):
        memes = []
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if filename.endswith('.wav') or filename.endswith('.mp3'):
                memes.append(('sound', pygame.mixer.Sound(filepath)))
            elif filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
                memes.append(('image', pygame.image.load(filepath)))
            elif filename.endswith('.mp4') or filename.endswith('.avi'):
                memes.append(('video', filepath))  # Handle video differently
            
        return memes

    def play_meme(self, meme_type):
        meme = random.choice(meme_type)
        if meme[0] == 'sound':
            meme[1].play()
        elif meme[0] == 'image':
            self.show_image(meme[1])
        elif meme[0] == 'video':
            self.play_video(meme[1])

    def show_image(self, image):
        # Display image logic (simplified example)
        screen = pygame.display.get_surface()
        screen.blit(image, (100, 100))  # Adjust position as needed
        pygame.display.update()
        pygame.time.delay(2000)  # Show for 2 seconds

    def play_video(self, video_path):
        # Play video logic
        pass

from PIL import Image, ImageDraw

# Create a new image with a white background
width, height = 400, 400
img = Image.new(mode="RGB", size=(width, height), color="white")

# Create a drawing context
draw = ImageDraw.Draw(img)

# Draw the face
radius = 150
x, y = width // 2, height // 2
draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill="yellow")

# Draw the eyes
eye_radius = 30
eye_spacing = 70
left_eye_center = (x - eye_spacing, y - eye_spacing)
right_eye_center = (x + eye_spacing, y - eye_spacing)
draw.ellipse((left_eye_center[0] - eye_radius, left_eye_center[1] - eye_radius, left_eye_center[0] + eye_radius, left_eye_center[1] + eye_radius), fill="black")
draw.ellipse((right_eye_center[0] - eye_radius, right_eye_center[1] - eye_radius, right_eye_center[0] + eye_radius, right_eye_center[1] + eye_radius), fill="black")

# Draw the mouth
mouth_width, mouth_height = 100, 50
mouth_top_left = (x - mouth_width // 2, y + radius // 2 - mouth_height // 2)
mouth_bottom_right = (x + mouth_width // 2, y + radius // 2 + mouth_height // 2)
draw.arc((mouth_top_left, mouth_bottom_right), start=0, end=180, fill="black", width=10)

# Save the image
img.save("smiley_face.png")

"""
    This function creates the classic Snake game using the Pygame library.
    The game involves controlling a snake to eat food and grow longer while avoiding obstacles.
    """
# Import necessary libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up the game variables
snake_block_size = 10
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    """
    This function displays a message on the game window.
    
    Parameters:
    msg (str): The message to be displayed
    color (tuple): The color of the message in RGB format
    """
    message = font_style.render(msg, True, color)
    game_window.blit(message, [window_width/6, window_height/3])

def game_loop():
    """
    This function contains the main game loop.
    """
    game_over = False
    game_close = False
    
    # Set up the initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0
    
    # Generate the first food block
    food_x = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0
    
    while not game_over:
        while game_close == True:
            game_window.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        create_snake_game()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0
        
        # Check if the snake hits the boundary
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        
        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change            
        game_window.fill(white)
        
        # Draw the food block
        pygame.draw.rect(game_window, green, [food_x, food_y, snake_block_size, snake_block_size])
        
        # Draw the snake
        pygame.draw.rect(game_window, black, [x1, y1, snake_block_size, snake_block_size])
        pygame.display.update()
        
        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            print("Yummy!!")
        
        clock.tick(20)
    
    pygame.quit()
    quit()

game_loop()
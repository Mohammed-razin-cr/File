import pygame
import pygame.freetype

def text_to_handwriting(text, font_path, output_image):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Handwriting Text")
    # Load the font
    font = pygame.freetype.Font(font_path, 30)
    # Set up the text surface
    text_surface, _ = font.render(text, (0, 0, 0))
    
    # Create a white background surface
    background = pygame.Surface((800, 600))
    background.fill((255, 255, 255))

    # Draw the text onto the background
    background.blit(text_surface, (50, 50))

    # Save the resulting image
    pygame.image.save(background, output_image)

    pygame.quit()

# Replace this font "QEDaveMergens.ttf" with your font file
font_path = 'font/QEDaveMergens.ttf'
text_to_convert = input("Enter the text you want to convert to handwriting: ")
output_image = "handwriting.png"

text_to_handwriting(text_to_convert, font_path, output_image)
print(f"Handwriting image saved as {output_image}")
import pygame
import button
import os
import sys
import time
from generate import Problem
from input_box import InputBox

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)

# pygame setup
pygame.init()
pygame.display.set_caption("Flash Mental")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# CORRECT PAGE
def correct(answer):
    
    # okay button
    okay_button_img = pygame.image.load("../img/okay.png").convert_alpha()
    okay_button = button.Button(500, 300, okay_button_img, 0.16)

    # font for the correct answer
    font = pygame.font.Font(None, 60)
    correct_text = f"Correct, the answer was: {answer:,}!"
    text_surface = font.render(correct_text, True, BLACK)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('lightblue') 

        screen.blit(text_surface, (300, 300))

        if okay_button.draw(screen):
            return
        
        pygame.display.update()

    pygame.quit() 

# INCORRECT PAGE
def incorrect(answer):
    # okay button
    okay_button_img = pygame.image.load("../img/okay.png").convert_alpha()
    okay_button = button.Button(500, 300, okay_button_img, 0.16)

    # font for the correct answer
    font = pygame.font.Font(None, 60)
    correct_text = f"Incorrect, the answer was: {answer:,}"
    text_surface = font.render(correct_text, True, BLACK)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('lightblue') 

        screen.blit(text_surface, (300, 300))

        if okay_button.draw(screen):
            return
        
        pygame.display.update()

    pygame.quit() 

# add / sub display (actually playing now)
def play_add_sub(numbers, digits, speed):
    # Generating problems using the generate module
    p1 = Problem() 
    font = pygame.font.Font(None, 200)
    question = p1.add_sub(int(numbers), int(digits))

    # input box for answer
    input_box = InputBox(600, 400, 140, 50, left_text="Answer")

    # buttons
    submit_button_img = pygame.image.load("../img/submit.png").convert_alpha()
    submit_button = button.Button(500, 500, submit_button_img, 0.16)

    # Time settings for Flash mental
    flash_duration = 1.0
    flash_interval = int(speed)
    last_flash_time = 0
    current_number_index = 0
    display_answer = False

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = int(time.time() * 1000)

        # Start the Flashing numbers        
        if not display_answer and current_time - last_flash_time >= flash_interval:
            last_flash_time = current_time
            if current_number_index < len(question):
                current_number = f"{question[current_number_index]:,}"
                current_number_index += 1
            else:
                display_answer = True

        screen.fill("lightblue")
        
        if display_answer:
            while True:
                for event in pygame.event.get():
                    input_box.handle_event(event)

                input_box.update()
                input_box.draw(screen)
                user_ans = input_box.get_text()
                
                if submit_button.draw(screen):
                    if user_ans == f"{sum(question):,}":
                        correct(sum(question))
                        return
                    else:
                        incorrect(sum(question))
                        return

                pygame.display.update()
            pygame.quit()

        elif current_number is not None:
            text = font.render(str(current_number), True, BLACK)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

        #if submit_button.draw(screen):
        #    return

        pygame.display.update()

    pygame.quit()

# add / sub game options
def add_sub_game():
    # setting game title
    pygame.display.set_caption("Addition/Subtraction")
    running = True

    # create a "back button" & "start button" instance
    back_button_img = pygame.image.load("../img/back.png").convert_alpha()
    start_button_img = pygame.image.load("../img/start.png").convert_alpha()
    back_button = button.Button(20, 500, back_button_img, 0.16)
    start_button = button.Button(900, 500, start_button_img, 0.16)

    # create input boxes
    input_boxes = [
        InputBox(600, 200, 140, 32, left_text="# of digits"),
        InputBox(600, 300, 140, 32, left_text="# of numbers"),
        InputBox(600, 400, 140, 32, left_text="Speed (ms)"),
    ]
    
    # Creates a setup page for the game inputs
    while running:
        screen.fill("lightblue")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                box.handle_event(event)
        
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen) 

        # Getting inputs
        digits = input_boxes[0].get_text()
        numbers = input_boxes[1].get_text()
        speed = input_boxes[2].get_text()

        if back_button.draw(screen):
            return
        if start_button.draw(screen):
            play_add_sub(numbers, digits, speed) 

        pygame.display.update()
    
    pygame.quit()

# Start multiplication game
def play_mult(num1, num2):
    # generate the problem
    p2 = Problem()
    question = p2.mult(int(num1), int(num2))

    # displaying text settings
    font = pygame.font.Font(None, 200)
    text = f"{question[0]:,} x {question[1]:,}"    
    text_surface = font.render(text, True, BLACK)
    text_x = (SCREEN_WIDTH - text_surface.get_width()) // 2
    text_y = (SCREEN_HEIGHT - text_surface.get_height()) // 2

    # input box for answer
    input_box = InputBox(600, 450, 140, 50, left_text="Answer")

    # buttons
    submit_button_img = pygame.image.load("../img/submit.png").convert_alpha()
    submit_button = button.Button(500, 500, submit_button_img, 0.16)
    
    # show new screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            input_box.handle_event(event) 
        
        screen.fill('lightblue')

        # display question        
        screen.blit(text_surface, (text_x, text_y)) 

        # input box & handling the inputs
        input_box.update()
        input_box.draw(screen)
        user_ans = input_box.get_text()

        if submit_button.draw(screen):
            answer = int(question[0]) * int(question[1])
            if user_ans == f"{answer:,}":
                correct(answer)
                return
            else:
                incorrect(answer)
                return
        
        pygame.display.update()

    pygame.quit() 
        
# mult game menu
def mult_game():
    # setting game title
    pygame.display.set_caption("Multiplication")
    running = True

    # create a "back button" & "start button" instance
    back_button_img = pygame.image.load("../img/back.png").convert_alpha()
    start_button_img = pygame.image.load("../img/start.png").convert_alpha()
    back_button = button.Button(20, 500, back_button_img, 0.16)
    start_button = button.Button(900, 500, start_button_img, 0.16)

    # create input boxes
    input_boxes = [
        InputBox(600, 300, 140, 32, left_text="size of 1st number"),
        InputBox(600, 400, 140, 32, left_text="size of 2nd number"),
    ]
    
    # Creates a setup page for the game inputs
    while running:
        screen.fill("lightblue")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                box.handle_event(event)
        
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen) 

        # Getting inputs
        num1 = input_boxes[0].get_text()
        num2 = input_boxes[1].get_text()

        if back_button.draw(screen):
            return
        if start_button.draw(screen):
            play_mult(num1, num2)

        pygame.display.update()
    
    pygame.quit()

# Start multiplication game
def play_div(num1, num2):
    # generate the problem
    p2 = Problem()
    question = p2.div(int(num1), int(num2))

    # displaying text settings
    font = pygame.font.Font(None, 200)
    text = f"{question[0]:,} ÷ {question[1]:,}"    
    text_surface = font.render(text, True, BLACK)
    text_x = (SCREEN_WIDTH - text_surface.get_width()) // 2
    text_y = (SCREEN_HEIGHT - text_surface.get_height()) // 2

    # input box for answer
    input_box = InputBox(600, 450, 140, 50, left_text="Answer")

    # buttons
    submit_button_img = pygame.image.load("../img/submit.png").convert_alpha()
    submit_button = button.Button(500, 500, submit_button_img, 0.16)
    
    # show new screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            input_box.handle_event(event) 
        
        screen.fill('lightblue')

        # display question        
        screen.blit(text_surface, (text_x, text_y)) 

        # input box & handling the inputs
        input_box.update()
        input_box.draw(screen)
        user_ans = input_box.get_text()

        if submit_button.draw(screen):
            answer = int(int(question[0]) / int(question[1]))
            if user_ans == f"{answer:,}":
                correct(answer)
                return
            else:
                incorrect(answer)
                return
        
        pygame.display.update()


# div game menu
def div_game():
    # setting game title
    pygame.display.set_caption("Division")
    running = True

    # create a "back button" & "start button" instance
    back_button_img = pygame.image.load("../img/back.png").convert_alpha()
    start_button_img = pygame.image.load("../img/start.png").convert_alpha()
    back_button = button.Button(20, 500, back_button_img, 0.16)
    start_button = button.Button(900, 500, start_button_img, 0.16)

    # create input boxes
    input_boxes = [
        InputBox(600, 300, 140, 32, left_text="size of 1st number"),
        InputBox(600, 400, 140, 32, left_text="size of 2nd number"),
    ]
    
    # Creates a setup page for the game inputs
    while running:
        screen.fill("lightblue")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                box.handle_event(event)
        
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen) 

        # Getting inputs
        num1 = input_boxes[0].get_text()
        num2 = input_boxes[1].get_text()

        if back_button.draw(screen):
            return
        if start_button.draw(screen):
            play_div(num1, num2)

        pygame.display.update()
    
    pygame.quit()

# main menu
def main():
    
    print("Copyright © Adam Wu 2023\nFlash Mental Math!\nHave Fun!")

    # load button images
    add_sub_img = pygame.image.load('../img/add_sub.png').convert_alpha()
    mult_img = pygame.image.load('../img/mult.png').convert_alpha()
    div_img = pygame.image.load('../img/div.png').convert_alpha()

    # creating button instances
    add_sub_btn = button.Button(450, 200, add_sub_img, 0.16)
    mult_btn = button.Button(450, 350, mult_img, 0.16)
    div_btn = button.Button(450, 500, div_img, 0.16)

    # create a font object for the menu title
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 60)
    copyright_text = "Copyright © Adam Wu 2023"
    
    # Render the copyright text
    cp_right_surface = font.render(copyright_text, True, BLACK)
    cp_right_rect = cp_right_surface.get_rect()
    cp_right_rect.bottomleft = (10, SCREEN_HEIGHT - 10)

    running = True
    while running:

        screen.fill("lightblue")
        # Render the menu title text
        title_text = title_font.render("Flash Mental Math Menu", True, BLACK)
        screen.blit(title_text, (400, 50))
        screen.blit(cp_right_surface, cp_right_rect)

        if add_sub_btn.draw(screen):
            add_sub_game()
        if mult_btn.draw(screen):
            mult_game()
        if div_btn.draw(screen):
            div_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()

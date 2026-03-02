# import pygame library
import pygame
from button import Button

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900

# initialise the pygame font
pygame.font.init()

# import Button class
new_game_button = Button("New Game", 420, 820, 180, 60)
restart_button = Button("Restart", 610, 820, 180, 60)

# Total window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon 
pygame.display.set_caption("4x4 Sudoku")


x = 0
y = 0
dif = SCREEN_WIDTH /4
val = 0
wrong_cells = set()
# Default Sudoku Board.
grid =[
        [4, 3, 2, 1],
        [0, 0, 3, 0],
        [0, 4, 0, 0],
        [2, 1, 0, 0],
    ]
# error message timer
error_time = pygame.time.get_ticks()

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 200)
font2 = pygame.font.SysFont("comicsans", 20)
font3 = pygame.font.SysFont("comicsans", 40)

def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

# Highlight the cell selected
def draw_box():
    if 0 <= x < 4 and 0 <= y < 4:
        for row in range(2):
            pygame.draw.line(screen, (255,222,33),
                             (x * dif-3, (y + row)*dif),
                             (x * dif + dif + 3, (y + row)*dif), 7)
            pygame.draw.line(screen, (255,222,33),
                             ((x + row)* dif, y * dif),
                             ((x + row) * dif, y * dif + dif), 7)
            
# Function to draw required lines for making Sudoku grid         
def draw():
    # Draw the lines
       
    for row in range (4):
        for col in range (4):
            if grid[row][col]!= 0:

                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (221,221,231), (col * dif, row * dif, dif + 1, dif + 1))

                if (row, col) in wrong_cells:
                    color = (255, 0, 0)
                else:
                    color = (0, 0, 0)


                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[row][col]), 1, color)
                text_rect = text1.get_rect()
                text_rect.center = (
                    col * dif + dif / 2,
                    row * dif + dif / 2
                )

                screen.blit(text1, text_rect)
    # Draw lines horizontally and verticallyto form grid           
    for row in range(10):
        if row % 2 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, row * dif), (SCREEN_WIDTH, row * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (row * dif, 0), (row * dif, SCREEN_WIDTH), thick)      

# Fill value entered in cell      
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))    

# Check if the value entered in board is valid
def is_valid(board, row, col, val):
    for index in range(4):
        if board[row][index]== val:
            return False
        if board[index][col]== val:
            return False
    start_row = row//2
    start_col = col//2
    for row in range(start_row * 2, start_row * 2 + 2):
        for col in range (start_col * 2, start_col * 2 + 2):
            if board[row][col]== val:
                return False
    return True

# Solves the sudoku board using Backtracking Algorithm
def solve(grid, row, col):
    
    while grid[row][col]!= 0:
        if row<4:
            row+= 1
        elif row == 4 and col<4:
            row = 0
            col+= 1
        elif row == 4 and col == 4:
            return True
    pygame.event.pump()    
    for start_row in range(1, 5):
        if is_valid(grid, row, col, start_row)== True:
            grid[row][col]= start_row
            global x, y
            x = row
            y = col
            # whstart_rowe color background\
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, row, col)== 1:
                return True
            else:
                grid[row][col]= 0
            # white color background\
            screen.fill((255, 255, 255))
        
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)    
    return False  


# Display instruction for the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, SCREEN_HEIGHT - 80))        
    screen.blit(text2, (20, SCREEN_HEIGHT - 60))

# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, SCREEN_HEIGHT - 30))    

run = True
flag1 = 0
flag2 = 0
is_solved = 0
error = 0
# The loop thats keep the window running
while run:
    
    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False  
        # Get the mouse position to insert number 
        # Check if mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:   
            # Check if button clicked
            if new_game_button.is_clicked(event):
                # Reset board (new_button logic)
                is_solved = 0
                error = 0
                flag2 = 0
                grid = [
                    [4, 3, 2, 1],
                    [0, 2, 3, 0],
                    [0, 4, 0, 0],
                    [2, 1, 0, 0],
                ]
            elif restart_button.is_clicked(event):
                # Reset board (Restart logic)
                is_solved = 0
                error = 0
                flag2 = 0
                grid = [
                    [0, 3, 2, 1],
                    [0, 0, 3, 0],
                    [0, 4, 0, 0],
                    [2, 1, 0, 0],
                ]
            else:
                pos = event.pos

                # Only allow clicks inside grid
                if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_WIDTH:
                    flag1 = 1
                    get_cord(pos)

        # Get the number to be inserted if key pressed    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1   
            # setting max amount of cells that arrows can move 
            x = max(0, min(3, x))
            y = max(0, min(3, y))
            if event.key in (pygame.K_1, pygame.K_KP1):
                val = 1
            if event.key in (pygame.K_2, pygame.K_KP2):
                val = 2    
            if event.key in (pygame.K_3, pygame.K_KP3):
                val = 3
            if event.key in (pygame.K_4, pygame.K_KP4):
                val = 4
            if event.key == pygame.K_RETURN:
                flag2 = 1   
            # If D is pressed reset the board to default 
            if event.key == pygame.K_d:
                is_solved = 0
                error = 0
                flag2 = 0
                grid =[
                [0, 3, 2, 1],
                [0, 0, 3, 0],
                [0, 4, 0, 0],
                [2, 1, 0, 0],
                ]
            if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, 
                                pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4):

                val = int(event.unicode)

                row = int(y)
                col = int(x)

                # Change num color when answer is incorrect
                if grid[row][col] == 0:

                    if is_valid(grid, row, col, val):
                        grid[row][col] = val
                        wrong_cells.discard((row, col))
                    else:
                        error = 1   
                        grid[row][col] = val
                        wrong_cells.add((row, col))

            # erase number from the cell
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_e, pygame.K_DELETE, pygame.K_BACKSPACE):
                    row = int(y)
                    col = int(x)

                    # Make a cell empty/0
                    grid[row][col] = 0



    if flag2 == 1:
        if solve(grid, 0, 0)== False:
            error = 1
        else:
            is_solved = 1
        flag2 = 0     
        
    if is_solved == 1:
        result()        
    draw()  
    if flag1 == 1:
        draw_box()       
    instruction()   

    # draw button
    mouse_pos = pygame.mouse.get_pos()
    new_game_button.draw(screen, mouse_pos) 
    restart_button.draw(screen, mouse_pos)  

    # Update window
    pygame.display.update()  

# Quit pygame window    
pygame.quit()
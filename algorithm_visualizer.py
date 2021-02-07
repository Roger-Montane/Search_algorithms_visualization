import pygame
from constants import *
from solver import *

pygame.init()
pygame.display.set_caption('Algorithm visualization')
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


smallfont = pygame.font.SysFont("Arial", 17)
medfont = pygame.font.SysFont("Arial", 50)
largefont = pygame.font.SysFont("Arial", 85)

start_cnt = 1
finish_cnt = 1

start = None
finish = None

class Button:
    def __init__(self, color, primary_color, secondary_color, x, y, width, height, text = '', outline = ''):
        self.color = color
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.outline = outline

    def draw(self, scr):
        if self.outline:
            pygame.draw.rect(scr, self.outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(scr, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            text = smallfont.render(self.text, 1, (0, 0, 0))
            scr.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        
        return False

STARTbutton = Button(ORANGE, ORANGE, LIGHT_ORANGE, 15, 760, 70, 85, 'START', BLACK)
FINISHbutton = Button(ORANGE, ORANGE, LIGHT_ORANGE, 97, 760, 70, 85, 'FINISH', BLACK)
WALLbutton = Button(ORANGE, ORANGE, LIGHT_ORANGE, 180, 760, 70, 85, 'WALLS', BLACK)
OKbutton = Button(CYAN, CYAN, LIGHT_CYAN, 265, 760, 75, 85, 'OK', BLACK)
BFSbutton = Button(DIM_GRAY, DIM_GRAY, LIGHT_GRAY, 355, 760, 75, 25, 'BFS', BLACK)
DFSbutton = Button(DIM_GRAY, DIM_GRAY, LIGHT_GRAY, 355, 790, 75, 25, 'DFS', BLACK)
UCSbutton = Button(DIM_GRAY,DIM_GRAY, LIGHT_GRAY, 355, 820, 75, 25, 'UCS', BLACK)
IDSbutton = Button(DIM_GRAY, DIM_GRAY, LIGHT_GRAY, 445, 760, 75, 25, 'IDS', BLACK)
GREEDYbutton = Button(DIM_GRAY, DIM_GRAY, LIGHT_GRAY, 445, 790, 75, 25, 'GREEDY', BLACK)
ASTARbutton = Button(DIM_GRAY, DIM_GRAY, LIGHT_GRAY, 445, 820, 75, 25, 'A*', BLACK)
BEGINbutton = Button(GREEN, GREEN, LIGHT_GREEN, 535, 760, 100, 85, 'BEGIN', BLACK)
CLEARbutton = Button(PURPLE, PURPLE, LIGHT_PURPLE, 650, 760, 95, 37, 'CLEAR', BLACK)
STOPbutton = Button(RED, RED, LIGHT_RED, 650, 808, 95, 37, 'STOP', BLACK)

def redraw_window(grid):
    screen.fill(GRAY)
    for row in range(SQUARES):
        for column in range(SQUARES):
            if grid[row][column] == PATH:
                color = WHITE
            elif grid[row][column] == START or grid[row][column] == FINAL_PATH:
                color = GREEN
            elif grid[row][column] == VISITED:
                color = RED
            elif grid[row][column] == WALL:
                color = GRAY
            elif grid[row][column] == FINISH:
                color = PURPLE
            pygame.draw.rect(screen, color, 
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH, HEIGHT])

    STARTbutton.draw(screen)
    FINISHbutton.draw(screen)
    OKbutton.draw(screen)
    DFSbutton.draw(screen)
    BFSbutton.draw(screen)
    IDSbutton.draw(screen)
    UCSbutton.draw(screen)
    GREEDYbutton.draw(screen)
    ASTARbutton.draw(screen)
    BEGINbutton.draw(screen)
    CLEARbutton.draw(screen)
    WALLbutton.draw(screen)
    STOPbutton.draw(screen)


def clear_grid(grid):
    global start_cnt
    global finish_cnt

    start_cnt = 1
    finish_cnt = 1

    for row in range(SQUARES):
        for column in range(SQUARES):
            grid[row][column] = 0

def clear_visited(grid):
    global start_cnt
    global finish_cnt

    start_cnt = 1
    finish_cnt = 1

    for row in range(SQUARES):
        for column in range(SQUARES):
            if grid[row][column] == VISITED or grid[row][column] == FINAL_PATH:
                grid[row][column] = PATH

def select_start(grid):
    global start_cnt
    global start
    done = False

    while not done:
        redraw_window(grid)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                if OKbutton.is_over(pos):
                    for row in range(SQUARES):
                        print(grid[row])
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                if start_cnt > 0:
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if row >= SQUARES or column >= SQUARES:
                        break
                    if grid[row][column] != FINISH:
                        start = (column, row)
                        grid[row][column] = START
                        start_cnt -= 1
                    print(grid[row][column], start_cnt)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if grid[row][column] == START:
                    if row >= SQUARES or column >= SQUARES:
                        break
                    grid[row][column] = PATH
                    start_cnt += 1
                    print(grid[row][column], start_cnt)

        pygame.display.update()

def select_finish(grid):
    global finish_cnt
    global finish
    done = False

    while not done:
        redraw_window(grid)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                if OKbutton.is_over(pos):
                    for row in range(SQUARES):
                        print(grid[row])
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                if finish_cnt > 0:
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if row >= SQUARES or column >= SQUARES:
                        break
                    if grid[row][column] != START:
                        grid[row][column] = FINISH
                        finish = (column, row)
                        finish_cnt -= 1
                    print(grid[row][column], finish_cnt)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if grid[row][column] == FINISH:
                    if row >= SQUARES or column >= SQUARES:
                        break
                    grid[row][column] = PATH
                    finish_cnt += 1
                    print(grid[row][column], finish_cnt)

        pygame.display.update()

def select_walls(grid):
    done = False

    dragging_and_drawing = False
    dragging_and_erasing = False

    while not done:
        redraw_window(grid)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                if OKbutton.is_over(pos):
                    for row in range(SQUARES):
                        print(grid[row])
                    done = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                dragging_and_drawing = True
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if row >= SQUARES or column >= SQUARES:
                    break
                if grid[row][column] != START and grid[row][column] != FINISH:
                    grid[row][column] = WALL

            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                dragging_and_drawing = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                dragging_and_erasing = True
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if row >= SQUARES or column >= SQUARES:
                    break
                if grid[row][column] == WALL:
                    if grid[row][column] != START and grid[row][column] != FINISH:
                        grid[row][column] = PATH

            if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                dragging_and_erasing = False

            if event.type == pygame.MOUSEMOTION:
                if dragging_and_drawing:
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if row >= SQUARES or column >= SQUARES:
                        break
                    if grid[row][column] != START and grid[row][column] != FINISH:
                        grid[row][column] = WALL

                if dragging_and_erasing:
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if row >= SQUARES or column >= SQUARES:
                        break
                    if grid[row][column] == WALL:
                        if grid[row][column] != START and grid[row][column] != FINISH:
                            grid[row][column] = PATH

        pygame.display.update()

def main():
    grid = []
    algorithm = ''

    for row in range(SQUARES):
        grid.append([])
        for column in range(SQUARES):
            grid[row].append(0)

    done = False

    while not done:
        redraw_window(grid)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                """
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if row >= SQUARES or column >= SQUARES:
                    break
                grid[row][column] = 1
                """
                #print("click ", pos, " Grid coordinates: ", row, column)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if STARTbutton.is_over(pos):
                    select_start(grid)
                    print(start_cnt)
                    print('clicked POSITION button (still does nothing)')
                if FINISHbutton.is_over(pos):
                    select_finish(grid)
                    print(finish_cnt)
                    print('clicked POSITION button (still does nothing)')
                if WALLbutton.is_over(pos):
                    select_walls(grid)
                    print('clicked WALL button (still does nothing)')
                if DFSbutton.is_over(pos):
                    algorithm = 'DFS'

                    DFSbutton.primary_color = GREEN
                    BFSbutton.primary_color = DIM_GRAY
                    IDSbutton.primary_color = DIM_GRAY
                    UCSbutton.primary_color = DIM_GRAY
                    GREEDYbutton.primary_color = DIM_GRAY
                    ASTARbutton.primary_color = DIM_GRAY

                    DFSbutton.outline = WHITE
                    BFSbutton.outline = BLACK
                    IDSbutton.outline = BLACK
                    UCSbutton.outline = BLACK
                    GREEDYbutton.outline = BLACK
                    ASTARbutton.outline = BLACK
                    print('clicked DFS button (still does nothing)')
                if BFSbutton.is_over(pos):
                    algorithm = 'BFS'

                    DFSbutton.primary_color = DIM_GRAY
                    BFSbutton.primary_color = GREEN
                    IDSbutton.primary_color = DIM_GRAY
                    UCSbutton.primary_color = DIM_GRAY
                    GREEDYbutton.primary_color = DIM_GRAY
                    ASTARbutton.primary_color = DIM_GRAY

                    DFSbutton.outline = BLACK
                    BFSbutton.outline = WHITE
                    IDSbutton.outline = BLACK
                    UCSbutton.outline = BLACK
                    GREEDYbutton.outline = BLACK
                    ASTARbutton.outline = BLACK
                    print('clicked BFS button (still does nothing)')
                if IDSbutton.is_over(pos):
                    algorithm = 'IDS'

                    DFSbutton.primary_color = DIM_GRAY
                    BFSbutton.primary_color = DIM_GRAY
                    IDSbutton.primary_color = GREEN
                    UCSbutton.primary_color = DIM_GRAY
                    GREEDYbutton.primary_color = DIM_GRAY
                    ASTARbutton.primary_color = DIM_GRAY

                    DFSbutton.outline = BLACK
                    BFSbutton.outline = BLACK
                    IDSbutton.outline = WHITE
                    UCSbutton.outline = BLACK
                    GREEDYbutton.outline = BLACK
                    ASTARbutton.outline = BLACK
                    print('clicked IDS button (still does nothing)')
                if UCSbutton.is_over(pos):
                    algorithm = 'UCS'

                    DFSbutton.primary_color = DIM_GRAY
                    BFSbutton.primary_color = DIM_GRAY
                    IDSbutton.primary_color = DIM_GRAY
                    UCSbutton.primary_color = GREEN
                    GREEDYbutton.primary_color = DIM_GRAY
                    ASTARbutton.primary_color = DIM_GRAY

                    DFSbutton.outline = BLACK
                    BFSbutton.outline = BLACK
                    IDSbutton.outline = BLACK
                    UCSbutton.outline = WHITE
                    GREEDYbutton.outline = BLACK
                    ASTARbutton.outline = BLACK
                    print('clicked UCS button (still does nothing)')
                if GREEDYbutton.is_over(pos):
                    algorithm = 'GREEDY'

                    DFSbutton.primary_color = DIM_GRAY
                    BFSbutton.primary_color = DIM_GRAY
                    IDSbutton.primary_color = DIM_GRAY
                    UCSbutton.primary_color = DIM_GRAY
                    GREEDYbutton.primary_color = GREEN
                    ASTARbutton.primary_color = DIM_GRAY

                    DFSbutton.outline = BLACK
                    BFSbutton.outline = BLACK
                    IDSbutton.outline = BLACK
                    UCSbutton.outline = BLACK
                    GREEDYbutton.outline = WHITE
                    ASTARbutton.outline = BLACK
                    print('clicked GREEDY button (still does nothing)')
                if ASTARbutton.is_over(pos):
                    algorithm = 'ASTAR'

                    DFSbutton.primary_color = DIM_GRAY
                    BFSbutton.primary_color = DIM_GRAY
                    IDSbutton.primary_color = DIM_GRAY
                    UCSbutton.primary_color = DIM_GRAY
                    GREEDYbutton.primary_color = DIM_GRAY
                    ASTARbutton.primary_color = GREEN

                    DFSbutton.outline = BLACK
                    BFSbutton.outline = BLACK
                    IDSbutton.outline = BLACK
                    UCSbutton.outline = BLACK
                    GREEDYbutton.outline = BLACK
                    ASTARbutton.outline = WHITE
                    print('clicked A* button (still does nothing)')
                if BEGINbutton.is_over(pos):
                    clear_visited(grid)
                    solver(algorithm, grid, start, finish)
                    print('clicked BEGIN button (still does nothing)')
                if CLEARbutton.is_over(pos):
                    clear_grid(grid)
                    print('clicked CLEAR button (still does nothing)')
                #if row >= SQUARES or column >= SQUARES:
                #    break
                #grid[row][column] = -1
                print("click ", pos, " Grid coordinates: ", row, column)

            elif event.type == pygame.MOUSEMOTION:
                if STARTbutton.is_over(pos):
                    STARTbutton.color = STARTbutton.secondary_color
                else:
                    STARTbutton.color = STARTbutton.primary_color

                if FINISHbutton.is_over(pos):
                    FINISHbutton.color = FINISHbutton.secondary_color
                else:
                    FINISHbutton.color = FINISHbutton.primary_color

                if WALLbutton.is_over(pos):
                    WALLbutton.color = WALLbutton.secondary_color
                else:
                    WALLbutton.color = WALLbutton.primary_color

                if OKbutton.is_over(pos):
                    OKbutton.color = OKbutton.secondary_color
                else:
                    OKbutton.color = OKbutton.primary_color

                if DFSbutton.is_over(pos):
                    DFSbutton.color = DFSbutton.secondary_color
                else:
                    DFSbutton.color = DFSbutton.primary_color

                if BFSbutton.is_over(pos):
                    BFSbutton.color = BFSbutton.secondary_color
                else:
                    BFSbutton.color = BFSbutton.primary_color

                if IDSbutton.is_over(pos):
                    IDSbutton.color = IDSbutton.secondary_color
                else:
                    IDSbutton.color = IDSbutton.primary_color

                if UCSbutton.is_over(pos):
                    UCSbutton.color = UCSbutton.secondary_color
                else:
                    UCSbutton.color = UCSbutton.primary_color

                if GREEDYbutton.is_over(pos):
                    GREEDYbutton.color = GREEDYbutton.secondary_color
                else:
                    GREEDYbutton.color = GREEDYbutton.primary_color

                if ASTARbutton.is_over(pos):
                    ASTARbutton.color = ASTARbutton.secondary_color
                else:
                    ASTARbutton.color = ASTARbutton.primary_color

                if BEGINbutton.is_over(pos):
                    BEGINbutton.color = BEGINbutton.secondary_color
                else:
                    BEGINbutton.color = BEGINbutton.primary_color

                if CLEARbutton.is_over(pos):
                    CLEARbutton.color = CLEARbutton.secondary_color
                else:
                    CLEARbutton.color = CLEARbutton.primary_color

                if STOPbutton.is_over(pos):
                    STOPbutton.color = STOPbutton.secondary_color
                else:
                    STOPbutton.color = STOPbutton.primary_color

        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

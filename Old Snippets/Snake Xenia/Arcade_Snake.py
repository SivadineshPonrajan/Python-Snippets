import curses
import random

curses.initscr()

win = curses.newwin(25,80,0,0)
win.border(0)
curses.noecho()
curses.curs_set(0)
win.keypad(1)
win.nodelay(1)
win.timeout(100)

score = 0

snake = [[12,15],[12,14],[12,13]]

food = [13,40]
win.addch(food[0],food[1],'*')

key = curses.KEY_RIGHT

win.addstr(0, 30, 'Python is here!!!')

while True:
    win.addstr(0, 3, 'Score: ' + str(score) + ' ')                                  
    win.timeout(100)
    
    prev_key = key

    newKey = win.getch()
    
    
    if newKey not in [curses.KEY_LEFT,curses.KEY_RIGHT,curses.KEY_UP,curses.KEY_DOWN]:
        key = key
    else:
        key = newKey
    
    if snake[0][0] == 0: snake[0][0] = 23
    if snake[0][1] == 0: snake[0][1] = 78
    if snake[0][0] == 24: snake[0][0] = 1
    if snake[0][1] == 79: snake[0][1] = 1
        
    if snake[0] in snake[1:]:
        break
        
    newHead = [snake[0][0],snake[0][1]]
    
    if key == curses.KEY_DOWN:
        newHead[0] += 1
    if key == curses.KEY_UP:
        newHead[0] -= 1
    if key == curses.KEY_LEFT:
        newHead[1] -= 1
    if key == curses.KEY_RIGHT:
        newHead[1] += 1

    snake.insert(0,newHead)
    
    if snake[0] == food:
        score += 1
        food = []
        food = [random.randint(2,23),random.randint(2,78)]
        win.addch(food[0],food[1],'*')
        
    else:
        tail = snake.pop()
        win.addch(tail[0],tail[1],' ')
        
    win.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)

print('Score: '+str(score))
curses.endwin()
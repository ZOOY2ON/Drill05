import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
hand_x, hand_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
frame = 0
bottom = 0

def rand_point():
    global hand_x, hand_y

    points = [(random.randint(0, TUK_WIDTH)), (random.randint(0, TUK_HEIGHT))]
    hand_x = points[0]
    hand_y = points[1]

def handle_events():
    global running
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def character_move():
    global x, y

    x1, y1 = x, y
    x2, y2 = hand_x, hand_y

    for i in range(0,100+1, 4):
        t=i/100
        x = (1-t)*x1 + t*x2 # 1-t : t의 비율로 x1, x2를 섞는다. 더한다.
        y = (1-t)*y1 + t*y2
        Draw()


def Draw():
    global frame
    global bottom

    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(hand_x, hand_y)

    character.clip_draw(frame * 100, bottom, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

def bottom_check():
    global bottom

    if x < hand_x:
        bottom = 100
    else:
        bottom = 0

# === main ===
while running:
    Draw()

    if x == hand_x and y == hand_y:
        rand_point()
        bottom_check()

    elif x != hand_x or y != hand_y:
        character_move()

    handle_events()

pico2d.close_canvas()

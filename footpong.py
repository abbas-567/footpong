#!/usr/bin/python
# -*- coding: utf-8 -*-
# Welcome to the code to my footpong game!
# Resolution:1280x720

from tkinter import Tk, Canvas, Label, Frame, Button, CENTER, Entry, \
    Toplevel
from PIL import ImageTk, Image
from time import sleep

window = Tk()
window.geometry('1280x720')
window.title('F O O T P O N G')

# Creating football pitch

canvas = Canvas(window, width=1280, height=720)
canvas.pack()

# Green background(grass)

canvas.config(bg='green')

# rectifying dimensions as I made a mistake with dimensions before

x_rect = 1280 / 900
y_rect = 720 / 500

# Game Title

Title = Label(canvas, text='fOoTpOnG', font=('Arial bold italic', 35),
              fg='white', bg='black')
Title.place(relx=0.5, rely=0.15, anchor='center')

# Adding ball
# source of ball image: https://www.clipartmax.com/middle/m2H7d3d3G6i8Z5K9_classic-football-banner-royalty-free-soccer-ball-clipart/

img = Image.open('clipart4576908.png')
resized_image = img.resize((35, 35), Image.Resampling.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)
ball = canvas.create_image(450 * x_rect, 250 * y_rect, image=new_image)

# Adding lines on the pitch

canvas.create_line(
    20 * x_rect,
    10 * y_rect,
    880 * x_rect,
    10 * y_rect,
    fill='white',
    width=5,
    )
canvas.create_line(
    20 * x_rect,
    490 * y_rect,
    880 * x_rect,
    490 * y_rect,
    fill='white',
    width=5,
    )
canvas.create_line(
    20 * x_rect,
    10 * y_rect,
    20 * x_rect,
    490 * y_rect,
    fill='white',
    width=5,
    )
canvas.create_line(
    880 * x_rect,
    10 * y_rect,
    880 * x_rect,
    490 * y_rect,
    fill='white',
    width=5,
    )
canvas.create_line(
    450 * x_rect,
    10 * y_rect,
    450 * x_rect,
    490 * y_rect,
    fill='white',
    width=5,
    )

# Creating a centre circle

centre_circle_xy = (325 * x_rect, 125 * y_rect, 575 * x_rect, 375
                    * y_rect)
centre_circle = canvas.create_oval(centre_circle_xy, outline='white')

# Creating goalposts
# red goalpost

red_post1 = canvas.create_line(
    0 * x_rect,
    160 * y_rect,
    30 * x_rect,
    160 * y_rect,
    fill='black',
    width=10,
    )
red_post2 = canvas.create_line(
    0 * x_rect,
    380 * y_rect,
    30 * x_rect,
    380 * y_rect,
    fill='black',
    width=10,
    )

# blue goalpost

blue_post1 = canvas.create_line(
    870 * x_rect,
    160 * y_rect,
    900 * x_rect,
    160 * y_rect,
    fill='black',
    width=10,
    )
blue_post2 = canvas.create_line(
    870 * x_rect,
    380 * y_rect,
    900 * x_rect,
    380 * y_rect,
    fill='black',
    width=10,
    )

# Creating our player

red_box_position = (50 * x_rect, 210 * y_rect, 65 * x_rect, 290
                    * y_rect)
red_box = canvas.create_rectangle(red_box_position, fill='red')

# Creating keeper

blue_box_position = (835 * x_rect, 210 * y_rect, 850 * x_rect, 290
                     * y_rect)
blue_box = canvas.create_rectangle(blue_box_position, fill='skyblue')

# variable bank

paused = False
cheat = False
boss_image = False
ball_y = 3
ball_x = 3
keeper_y = 3
keeper_x = 3
goals = 0
current_score = 'Score:' + ' ' + str(goals)
score_display = canvas.create_text(120, 40, text=current_score,
                                   fill='purple', font=('Verdana Bold',
                                   20))


def get_score():
    global x_rect
    global y_rect
    global ball_x, ball_y
    global goals
    global current_score
    global goal_msg
    ball_pos = canvas.coords(ball)
    current_score = 'Score:' + ' ' + str(goals)
    if ball_pos[1] > 158 * y_rect and ball_pos[1] < 382 * y_rect:
        if ball_pos[0] >= 1280:

            goals += 1

            # increasing ball speed/level as goal is scored

            ball_y *= 1.1
            ball_x *= 1.1
            if goals > 1:
                goal_msg = canvas.create_text(800, 60,
                        text='GOOOOL! Ball speed increase lvl'
                        + str(goals), fill='orange',
                        font=('Verdana Bold', 30))
                window.after(1000, canvas.delete, goal_msg)

            canvas.itemconfig(score_display, text=current_score)


def gameplay_start():
    while True:
        global ball, x_rect, y_rect, ball_x, ball_y, keeper_y, \
            ball_pos, keeper_pos, player_pos, start_button, paused, \
            cheat
        ball_pos = canvas.coords(ball)
        keeper_pos = canvas.coords(blue_box)
        player_pos = canvas.coords(red_box)
        red_post1_pos = canvas.coords(red_post1)
        red_post2_pos = canvas.coords(red_post2)
        blue_post1_pos = canvas.coords(blue_post1)
        blue_post2_pos = canvas.coords(blue_post2)

        if ball_pos[0] > 900 * x_rect or ball_pos[0] < 0:
            ball_x = -ball_x
            get_score()

        if ball_pos[1] > 500 * y_rect or ball_pos[1] < 0:
            ball_y = -ball_y

        if keeper_pos[1] < 100 * y_rect or keeper_pos[3] > 400 * y_rect:
            keeper_y = -keeper_y

        # Collision of ball with keeper:

        if ball_pos[0] < keeper_pos[2] and ball_pos[0] > keeper_pos[0] \
            and ball_pos[1] < keeper_pos[3] and ball_pos[1] \
            > keeper_pos[1]:
            ball_x = -ball_x

            # ball_y = -ball_y

        # Collision of ball with player

        if ball_pos[0] < player_pos[2] and ball_pos[0] > player_pos[0] \
            and ball_pos[1] < player_pos[3] and ball_pos[1] \
            > player_pos[1]:
            ball_x = -ball_x

            

        # Collision of ball with red post1

        if ball_pos[0] < red_post1_pos[2] and ball_pos[0] \
            > red_post1_pos[0] and ball_pos[1] < red_post1_pos[3] \
            and ball_pos[1] > red_post1_pos[1]:
            ball_x = -ball_x
            ball_y = -ball_y

        # Collision of ball with red post2

        if ball_pos[0] < red_post2_pos[2] and ball_pos[0] \
            > red_post2_pos[0] and ball_pos[1] < red_post2_pos[3] \
            and ball_pos[1] > red_post2_pos[1]:
            ball_x = -ball_x
            ball_y = -ball_y

        # Collision of ball with blue post1

        if ball_pos[0] < blue_post1_pos[2] and ball_pos[0] \
            > blue_post1_pos[0] and ball_pos[1] < blue_post1_pos[3] \
            and ball_pos[1] > blue_post1_pos[1]:
            ball_x = -ball_x
            ball_y = -ball_y

        # Collision of ball with blue post2

        if ball_pos[0] < blue_post2_pos[2] and ball_pos[0] \
            > blue_post2_pos[0] and ball_pos[1] < blue_post2_pos[3] \
            and ball_pos[1] > blue_post2_pos[1]:
            ball_x = -ball_x
            ball_y = -ball_y
        if not paused:
            canvas.move(ball, ball_x, ball_y)
            canvas.move(blue_box, 0, keeper_y)
        sleep(0.0000004)

        if ball_pos[1] > 158 * y_rect and ball_pos[1] < 382 * y_rect:
            if ball_pos[0] < 2:

                # print("here")

                gameplay_end()

        window.update()


# Function for when we concede and game ends

def gameplay_end():
    global ball_x, ball_y, keeper_y, keeper_x, submit_button
    keeper_x = 0
    keeper_y = 0
    ball_x = 0
    ball_y = 0
    canvas.move(ball, 0, 0)
    canvas.move(blue_box, 0, 0)

    # canvas.move(red_box,x,y)

    canvas.create_text(630, 300, text='GAME OVER', fill='darkred',
                       font=('Arial Bold', 50))
    canvas.create_text(630, 400, text='Your score: ' + str(goals - 1),
                       fill='darkred', font=('Arial Bold', 30))
    submit_button = Button(
        canvas,
        command=open_name_window,
        bg='red',
        text='Submit name',
        fg='white',
        font=('Verdana', 14),
        )
    submit_button.place(relx=0.5, rely=0.76, anchor='center')


# Moving our player (By WASD and arrow keys)
# Restrictions in player movement (can only move in our half) with the 'and' in if statements

def wasd(event):
    global red_box
    x = 0
    y = 0
    if event.char == 'a' and player_pos[0] > 30 * x_rect:
        x = -12
    if event.char == 'd' and player_pos[2] < 445 * x_rect:
        x = 12
    if event.char == 'w' and player_pos[1] > 20 * y_rect:
        y = -12
    if event.char == 's' and player_pos[3] < 480 * y_rect:
        y = 12

    if not paused:
        canvas.move(red_box, x, y)
    if paused:
        canvas.move(red_box, 0, 0)


def left(event):
    global x, y
    x = -12
    y = 0
    if player_pos[0] > 30 * x_rect:
        canvas.move(red_box, -12, 0)


def right(event):
    global x, y
    x = 12
    y = 0
    if player_pos[2] < 445 * x_rect:
        canvas.move(red_box, 12, 0)


def up(event):
    global x, y
    x = 0
    y = -12
    if player_pos[1] > 20 * y_rect:
        canvas.move(red_box, 0, -12)


def down(event):
    global x, y
    x = 0
    y = 12
    if player_pos[3] < 480 * y_rect:
        canvas.move(red_box, 0, 12)


def cheat_code(event):
    global blue_box_position, keeper_x, keeper_y
    blue_box_position = (25 * x_rect, 210 * y_rect, 40 * x_rect, 290
                         * y_rect)
    keeper_y = 0
    keeper_x = 0


# cheat for which a goal counts as 10

def goal_cheat(event):
    global goals
    goals += 10


# pause function

def pause(event):
    global paused
    paused = not paused


# adding boss key

def boss_key(event):
    global paused, boss_key_image
    if not paused:
        paused = not paused
        img2 = Image.open('bosskeypic.png')
        resized_bosskey = img2.resize((1280, 720),
                Image.Resampling.LANCZOS)
        new_bosskey_image = ImageTk.PhotoImage(resized_bosskey)
        boss_key_image = canvas.create_image(640, 360,
                image=new_bosskey_image)
        canvas.pack(boss_image)
    else:
        paused = not paused
        canvas.delete(boss_key_image)


# save and quit function function
# saves score and ball speed

def save(event):
    global ball, blue_box, red_box, save_file, ball_y, ball_x
    save_file = open('savedgame.txt', 'w')
    save_file.write(str(goals - 1) + '\n')
    save_file.write(str(ball_y) + '\n')
    save_file.write(str(ball_x) + '\n')
    save_file.close()
    window.destroy()


# load function

def continue_game():
    global save_file, ball, blue_box, red_box, goals, list, \
        current_score, ball_y, ball_x
    save_file = open('savedgame.txt', 'r')
    list = save_file.readlines()
    goals = int(int(list[0]) + 1)
    ball_y = float(list[1])
    ball_x = float(list[2])
    current_score = 'Score:' + ' ' + str(goals)
    start_game()


    # list_ball_coords = save_file.readline(2)

# binding keys to events

window.bind('<Left>', left)
window.bind('<Right>', right)
window.bind('<Up>', up)
window.bind('<Down>', down)

window.bind('<a>', left)
window.bind('<d>', right)
window.bind('<w>', up)
window.bind('<s>', down)
window.bind('<p>', pause)
window.bind('<b>', boss_key)
window.bind('<m>', save)

# window.bind("<KeyPress>", wasd)

window.bind('<c>', cheat_code)
window.bind('<g>', goal_cheat)


# function for when we click start so game starts and widgets disappear

def start_game():
    Title.destroy()
    start_button.destroy()
    continue_button.destroy()
    leaderboard_button.destroy()
    about_button.destroy()
    sleep(0.2)
    gameplay_start()


# function to add player's score to the leaderboard file

def add_to_leaderboard():
    with open('leaderboard.txt', 'a') as leaderboard:
        leaderboard.write(str(name_box.get()) + ' = ' + str(goals - 1)
                          + '\n')
    name_window.destroy()


# function to open the window which allows the user to enter their name

def open_name_window():
    global enter_Name_prompt, name_box, name_window
    name_window = Toplevel(window)
    name_window.title('Enter Name')
    name_window.geometry('200x200')
    name_canvas = Canvas(name_window, width=200, height=200,
                         bg='lightgreen')

    enter_Name_prompt = name_canvas.create_text(100, 50,
            text='Enter Your Name!', font=('Arial Bold', 10))

    name_box = Entry(name_canvas, width=10, borderwidth=6)
    name_box.place(relx=0.5, rely=0.6, anchor='center')
    enter_name_button = Button(name_canvas, command=add_to_leaderboard,
                               bg='red', text='Enter Name', fg='white')
    enter_name_button.place(relx=0.5, rely=0.8, anchor='center')
    name_canvas.pack()


# function to open about window

def open_about_window():
    global about_title, about_description, about_window
    about_window = Toplevel(window)
    about_window.title('About')
    about_window.geometry('700x500')
    about_canvas = Canvas(about_window, width=700, height=500,
                          bg='lightgreen')

    about_title = about_canvas.create_text(250, 40,
            text='About Footpong', font=('Arial Bold', 20))
    about_description = about_canvas.create_text(200, 60,
            text='Footpong is inspired by pong and the beautiful game',
            font=('Arial Bold', 10))
    about_description = about_canvas.create_text(200, 80,
            text='First goal is to warm up the keeper',
            font=('Arial Bold', 10))
    about_description = about_canvas.create_text(200, 100,
            text='User gets the option to move using wasd or arrow keys'
            , font=('Arial Bold', 10))
    about_description = about_canvas.create_text(200, 120,
            text='p to pause', font=('Arial Bold', 10))
    about_description = about_canvas.create_text(200, 140,
            text='b as bosskey', font=('Arial Bold', 10))
    about_description = about_canvas.create_text(200, 160,
            text='m to save', font=('Arial Bold', 10))
    about_description = about_canvas.create_text(200, 400,
            text='g for goal cheat', font=('Arial Bold', 4))
    about_description = about_canvas.create_text(200, 405,
            text='c for keeper cheat', font=('Arial Bold', 4))
    about_canvas.pack()


# function which displays leaderboard in the window

def display_leaderboard_window():
    global leaderboard_title
    leaderboard_window = Toplevel(window)
    leaderboard_window.title('Leaderboard')
    leaderboard_window.geometry('300x700')
    leaderboard_canvas = Canvas(leaderboard_window, width=300,
                                height=700, bg='lightgreen')
    leaderboard_title = leaderboard_canvas.create_text(120, 30,
            text='LEADERBOARD', font=('Arial Bold', 15), fill='red')
    with open('leaderboard.txt', 'r') as leaderboard:
        leaderboard_lines = leaderboard.readlines()

        # leaderboard_lines = leaderboard.readlines(6)[1]
        # leaderboard_lines = leaderboard.readlines()[3]
        # leaderboard_lines = leaderboard.readlines()[4]
        # leaderboard_lines = leaderboard.readlines()[5]

    leaderboard_canvas.create_text(100, 100, text=leaderboard_lines,
                                   fill='red', font=('Verdana Bold',
                                   13))
    leaderboard_canvas.pack()


# Designing start button

start_button = Button(
    canvas,
    command=start_game,
    bg='red',
    text='START NEW GAME',
    font=('Verdana bold', 20),
    fg='white',
    )
start_button.place(relx=0.5, rely=0.3, anchor='center')

# Designing leaderboard button

leaderboard_button = Button(
    canvas,
    command=display_leaderboard_window,
    bg='red',
    text='   LEADERBOARD   ',
    font=('Verdana bold', 20),
    fg='white',
    )
leaderboard_button.place(relx=0.5, rely=0.5, anchor='center')

# Designing continue game button

continue_button = Button(
    canvas,
    bg='red',
    command=continue_game,
    text=' CONTINUE GAME ',
    font=('Verdana bold', 20),
    fg='white',
    )
continue_button.place(relx=0.5, rely=0.4, anchor='center')

# Designing about button

about_button = Button(
    canvas,
    bg='red',
    command=open_about_window,
    text='         ABOUT         ',
    font=('Verdana bold', 20),
    fg='white',
    )
about_button.place(relx=0.5, rely=0.6, anchor='center')

window.mainloop()

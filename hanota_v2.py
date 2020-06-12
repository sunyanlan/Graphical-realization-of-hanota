'''
Author:sunyan
Date:2020/5/17
'''
import time
import tkinter
from tkinter import ttk
from tkinter import *

global slp_ti
global disc_num_A

def hanmu_move(n, a, b, c):
    global resu_list
    if n == 1:
        resu_list.append(a + '->' + c)
    else:
        hanmu_move(n-1, a, c, b)
        hanmu_move(1, a, b, c)
        hanmu_move(n-1, b, a, c)

def up_move(old_aim, dis_aim, len_who):
    global slp_ti
    for i in range(30 - len(len_who)):
        time.sleep(slp_ti)
        old_aim.move(dis_aim, 0, -10)
        old_aim.update()

def right_move(old_aim, dis_aim, tis):
    global slp_ti
    for i in range(tis * 25):
        time.sleep(slp_ti)
        old_aim.move(dis_aim, 10, 0)
        old_aim.update()

def down_move(old_aim, dis_aim, len_who):
    global slp_ti
    for i in range(29 - len(len_who)):
        time.sleep(slp_ti)
        old_aim.move(dis_aim, 0, 10)
        old_aim.update()

def left_move(old_aim, dis_aim, tis):
    global slp_ti
    for i in range(tis * 25):
        time.sleep(slp_ti)
        old_aim.move(dis_aim, -10, 0)
        old_aim.update()

def A_to_B(old_aim, dis_aim, disc_num):
    global disc_num_A
    global disc_num_B
    if len(disc_num_A) > 0:
        up_move(old_aim, dis_aim, disc_num_A)
        right_move(old_aim, dis_aim, 1)
        down_move(old_aim, dis_aim, disc_num_B)

        disc_num_A.remove(disc_num)
        disc_num_B.append(disc_num)

def A_to_C(old_aim, dis_aim, disc_num):
    global disc_num_A
    global disc_num_C
    if len(disc_num_A) > 0:
        up_move(old_aim, dis_aim, disc_num_A)
        right_move(old_aim, dis_aim, 2)
        down_move(old_aim, dis_aim, disc_num_C)
    
        disc_num_A.remove(disc_num)
        disc_num_C.append(disc_num)

def B_to_C(old_aim, dis_aim, disc_num):
    global disc_num_B
    global disc_num_C
    if len(disc_num_B) > 0:
        up_move(old_aim, dis_aim, disc_num_B)
        right_move(old_aim, dis_aim, 1)
        down_move(old_aim, dis_aim, disc_num_C)   

        disc_num_B.remove(disc_num)
        disc_num_C.append(disc_num)


def B_to_A(old_aim, dis_aim, disc_num):
    global disc_num_A
    global disc_num_B
    if len(disc_num_B) > 0:
        up_move(old_aim, dis_aim, disc_num_B)
        left_move(old_aim, dis_aim, 1)
        down_move(old_aim, dis_aim, disc_num_A)

        disc_num_B.remove(disc_num)
        disc_num_A.append(disc_num)

def C_to_A(old_aim, dis_aim, disc_num):
    global disc_num_A
    global disc_num_C
    if len(disc_num_C) > 0:
        up_move(old_aim, dis_aim, disc_num_C)
        left_move(old_aim, dis_aim, 2)
        down_move(old_aim, dis_aim, disc_num_A)

        disc_num_C.remove(disc_num)
        disc_num_A.append(disc_num)

def C_to_B(old_aim, dis_aim, disc_num):
    global disc_num_B
    global disc_num_C
    if len(disc_num_C) > 0:
        up_move(old_aim, dis_aim, disc_num_C)
        left_move(old_aim, dis_aim, 1)
        down_move(old_aim, dis_aim, disc_num_B)

        disc_num_C.remove(disc_num)
        disc_num_B.append(disc_num)

def auto_hanmota(canvas, combobox_data):
    global disc_num_A
    global disc_num_B
    global disc_num_C
    global resu_list

    clear_disc(canvas, combobox_data)

    or_num = int(combobox_data.get())
    hanmu_move(or_num, 'A', 'B', 'C')

    for index in resu_list:
        print(index)
        if index == 'A->B':
            A_to_B(canvas, globals()['disc' + disc_num_A[-1][-1:]], disc_num_A[-1])
        elif index == 'A->C':
            A_to_C(canvas, globals()['disc' + disc_num_A[-1][-1:]], disc_num_A[-1])
        elif index == 'B->C':
            B_to_C(canvas, globals()['disc' + disc_num_B[-1][-1:]], disc_num_B[-1])
        elif index == 'B->A':
            B_to_A(canvas, globals()['disc' + disc_num_B[-1][-1:]], disc_num_B[-1])
        elif index == 'C->A':
            C_to_A(canvas, globals()['disc' + disc_num_C[-1][-1:]], disc_num_C[-1])
        elif index == 'C->B':
            C_to_B(canvas, globals()['disc' + disc_num_C[-1][-1:]], disc_num_C[-1])
        else:
            print('no strategy!')

def show_disc(canvas, combobox_data):
    if (len(disc_num_A) > 0) or (len(disc_num_B) > 0) or (len(disc_num_C) > 0):
        clear_disc(canvas, combobox_data)

    or_num = int(combobox_data.get())
    for i in range(or_num):
        disc_num_A.append('disc' + str(i))
    for i in range(or_num):
        globals()['disc' + str(i)] = canvas.create_rectangle(40 + i*10, 440 - i*10, 280 - i*10, 450 - i*10, fill = 'blue')

def clear_disc(canvas, combobox_data):
    or_num = int(combobox_data.get())

    global disc_num_A
    global disc_num_B
    global disc_num_C
    global resu_list

    resu_list = []
    disc_num_A = []
    disc_num_B = []
    disc_num_C = []
    for i in  range(or_num):
        canvas.delete(globals()['disc' + str(i)])
    for i in range(or_num):
        disc_num_A.append('disc' + str(i))
    for i in range(or_num):
        globals()['disc' + str(i)] = canvas.create_rectangle(40 + i*10, 440 - i*10, 280 - i*10, 450 - i*10, fill = 'blue')

def main():

    global slp_ti
    global resu_list
    global disc_num_A
    global disc_num_B
    global disc_num_C


    resu_list = []
    disc_num_A = []
    disc_num_B = []
    disc_num_C = []
    slp_ti = 0.001


    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width=850, height=700, bg='white')
    canvas.pack()
    canvas.create_rectangle(150, 250, 170, 450, fill = 'yellow')
    canvas.create_rectangle(400, 250, 420, 450, fill = 'yellow')
    canvas.create_rectangle(650, 250, 670, 450, fill = 'yellow')
    canvas.create_rectangle(20, 450, 830, 470, fill = 'yellow')

    data_or_num = tkinter.StringVar()
    combobox_data = ttk.Combobox(canvas, textvariable=data_or_num, width=10, font=("宋体", 13))
    combobox_data["value"] = [3, 4, 5, 6, 7, 8, 9, 10]  
    combobox_data.current(0)
    combobox_data.place(x=100, y=100)
    button_start = tkinter.Button(canvas, text="开始", command=lambda:show_disc(canvas, combobox_data), font=("宋体", 13), width=13, height=1)
    button_start.place(x=300, y=100)
    button_choice = tkinter.Button(canvas, text="自动搬", command=lambda:auto_hanmota(canvas, combobox_data), font=("宋体", 13), width=13, height=1)
    button_choice.place(x=500, y=100)
    button_start = tkinter.Button(canvas, text="重新开始", command=lambda:clear_disc(canvas, combobox_data), font=("宋体", 13), width=13, height=1)
    button_start.place(x=700, y=100)

    button_A_B = tkinter.Button(canvas, text="A到B", command=lambda:A_to_B(canvas, globals()['disc' + disc_num_A[-1][-1:]], disc_num_A[-1]), font=("宋体", 13), width=13, height=1)
    button_A_B.place(x=50, y=500)

    button_A_C = tkinter.Button(canvas, text="A到C", command=lambda:A_to_C(canvas, globals()['disc' + disc_num_A[-1][-1:]], disc_num_A[-1]), font=("宋体", 13), width=13, height=1)
    button_A_C.place(x=50, y=600)

    button_B_C = tkinter.Button(canvas, text="B到C", command=lambda:B_to_C(canvas, globals()['disc' + disc_num_B[-1][-1:]], disc_num_B[-1]), font=("宋体", 13), width=13, height=1)
    button_B_C.place(x=350, y=500)

    button_B_A = tkinter.Button(canvas, text="B到A", command=lambda:B_to_A(canvas, globals()['disc' + disc_num_B[-1][-1:]], disc_num_B[-1]), font=("宋体", 13), width=13, height=1)
    button_B_A.place(x=350, y=600)

    button_C_B = tkinter.Button(canvas, text="C到B", command=lambda:C_to_B(canvas, globals()['disc' + disc_num_C[-1][-1:]], disc_num_C[-1]), font=("宋体", 13), width=13, height=1)
    button_C_B.place(x=650, y=500)

    button_C_A = tkinter.Button(canvas, text="C到A", command=lambda:C_to_A(canvas, globals()['disc' + disc_num_C[-1][-1:]], disc_num_C[-1]), font=("宋体", 13), width=13, height=1)
    button_C_A.place(x=650, y=600)

    root.mainloop()

if __name__ == '__main__':
    main()



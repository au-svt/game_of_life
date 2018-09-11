'''
GOL - conway's GAME OF LIFE
0 player game not your typical computer game
The Rules
    For a space that is 'populated':
        Each cell with one or no neighbors dies, as if by solitude.
        Each cell with four or more neighbors dies, as if by overpopulation.
        Each cell with two or three neighbors survives.
    For a space that is 'empty' or 'unpopulated'
        Each cell with three neighbors becomes populated.

python3 - tkinter
python2 - Tkinter
import accordingly
'''

# for python3 - tkinter, python2 - Tkinter; import accordingly

from tkinter import *
import numpy as np

np.set_printoptions(threshold=np.inf)  # to print all elements of array irrespective of its size

# globals
start = False
ROWS = 50
COLS = 75
generations = 0
DELAY = 376  # time in ms, v = input from speed slider, used formula- DELAY = (100 - v) * 15 + 1, that is v( init speed)= 75


############################

# Stores(and update the grid array when called) pre defined patterns (in OptionMenu) as array[ROWS][COLS]


class Patterns(object):
    def __init__(self):
        self.current_grid = np.zeros((ROWS, COLS))  # will be used as init grid array

    def new_pattern(self, pattern):
        current_grid = np.zeros((ROWS, COLS), int)

        if pattern == 'glider':
            glider = [[0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0]]
            current_grid[11:16, 11:16] = glider
            self.current_grid = current_grid

        elif pattern == 'exploder 1':
            exploder_1 = [[0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 1, 1, 1, 0],
                          [0, 1, 0, 1, 0],
                          [0, 0, 1, 0, 0]]
            current_grid[20:25, 35:40] = exploder_1
            self.current_grid = current_grid

        elif pattern == 'exploder 2':
            exploder = [[0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 0, 0, 1],
                        [0, 1, 0, 0, 0, 1],
                        [0, 1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 0, 1]]
            current_grid[20:26, 35:41] = exploder
            self.current_grid = current_grid

        elif pattern == 'row':
            ten_cell_row = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            current_grid[25:27, 25:35] = ten_cell_row
            self.current_grid = current_grid

        elif pattern == 'glider 2':  # found on http://pentadecathlon.com/lifenews/
            glider2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                       [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            current_grid[20:28, 19:29] = glider2
            self.current_grid = current_grid

        elif pattern == 'spaceship':
            spaceship = [[0, 1, 1, 1, 1],
                         [1, 0, 0, 0, 1],
                         [0, 0, 0, 0, 1],
                         [1, 0, 0, 1, 0]]
            current_grid[10:14, 20:25] = spaceship
            self.current_grid = current_grid

        elif pattern == 'tumbler':
            tumbler = [[0, 1, 1, 0, 1, 1, 0],
                       [0, 1, 1, 0, 1, 1, 0],
                       [0, 0, 1, 0, 1, 0, 0],
                       [1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1],
                       [1, 1, 0, 0, 0, 1, 1]]
            current_grid[25:31, 20:27] = tumbler
            self.current_grid = current_grid

        elif pattern == 'glider gun':
            glider_gun = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0]]
            current_grid[13: 24, 13: 51] = glider_gun
            self.current_grid = current_grid

        else:
            return

        # self.pattern = pattern

    def patt_count_alives(self):
        patt_count_alives = 0
        for i in range(ROWS):
            for j in range(COLS):
                if self.current_grid[i][j]:
                    patt_count_alives += 1
        return patt_count_alives


############################


class Grid(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.geometry("+550+200")
        self.master.title("GOL ~ani")
        self.pack()
        self.rows = ROWS  # no of rows
        self.cols = COLS  # no of cols
        self.cell_size = 10  # in pixels
        self.grid = np.zeros((self.rows, self.cols), int)

        self.draw_grid_gui()  # buttons, labels, slider, canvas, option menu, status bar(bottom most)
        self.draw_grid()  # rectangles drawn acc to array value 0 / 1
        self.select_pattern()  # initial grid (whichever is default var of option menu) on canvas i.e. draws rows*cols rectangles

    def draw_grid_gui(self):
        self.canv = Canvas(self, bg='gray', relief=SUNKEN)
        self.canv_y = self.rows * self.cell_size
        self.canv_x = self.cols * self.cell_size

        self.canv.config(width=self.canv_x, height=self.canv_y)
        self.canv.grid(row=0, column=1, rowspan=15, columnspan=14)
        self.canv.config(highlightthickness=0)

        quitButton = Button(self, text='QUIT', command=self.client_exit, fg='red')
        quitButton.bind("<Enter>", self.turn_red)
        quitButton.grid(row=14, column=15, sticky=E)

        start_Button = Button(self, text='start', command=self.start_game)  # , bg='green')
        start_Button.bind("<Enter>", self.turn_green)
        start_Button.grid(row=0, column=15)

        stop_Button = Button(self, text='stop', command=self.stop_game)  # , bg='green')
        stop_Button.bind("<Enter>", self.turn_red)
        stop_Button.grid(row=1, column=15)

        step_Button = Button(self, text='next', command=self.step_game)  # , bg='green')
        step_Button.bind("<Enter>", self.turn_blue)
        step_Button.grid(row=2, column=15)

        reset_Button = Button(self, text='reset', command=self.reset_game)
        reset_Button.bind("<Enter>", self.turn_red)
        reset_Button.grid(row=3, column=15)

        # ################  initial pattern ->  option menu

        choices = ['clear',
                   'row',
                   'glider',
                   'glider 2',
                   'tumbler',
                   'exploder 1',
                   'exploder 2',
                   'spaceship',
                   'glider gun']

        self.var1 = StringVar(self)  # var string to be shown on option menu
        self.var1.set(choices[6])
        label1 = Label(self, text='Init. Pattern')
        label1.grid(row=2, column=0, sticky=S)
        w = OptionMenu(self, self.var1, *choices)
        w.config(width=8)
        w.grid(row=3, column=0, sticky=EW)
        go_button = Button(self, text="Go", command=self.select_pattern)  # draws above selected variable pattern
        go_button.grid(row=4, column=0, sticky=N)

        # ##########  speed scale

        label2 = Label(self, text='Speed')
        label2.grid(row=5, column=15, sticky=S)
        scale = Scale(self, from_=0, to=100, width=10, length=125, command=self.onScale, orient='vertical')
        scale.grid(row=6, column=15, rowspan=4)

        self.var2 = IntVar()
        self.var2.set(75)

        # ############# status 1 -> generation count

        status1a = Label(self, text='generation :', bd=1, relief=SUNKEN)
        status1a.grid(row=15, column=14, sticky=E)
        self.var3 = StringVar(self)
        status1b = Label(self, textvariable=self.var3, bd=1, relief=SUNKEN)
        status1b.grid(row=15, column=15, sticky=W + E)
        self.var3.set(str(generations))

        # ######## status 2 -> for count of living cells

        status2a = Label(self, text='alive cells :', bd=1, relief=SUNKEN)
        status2a.grid(row=15, column=0, sticky=W + E)
        self.var4 = IntVar(self)
        status2b = Label(self, textvariable=self.var4, bd=1, relief=SUNKEN)
        status2b.grid(row=15, column=1, sticky=W + E)
        self.var4.set(0)
        no_of_cells = self.rows * self.cols
        status2c = Label(self, text=' /    ' + str(no_of_cells) + ' ', bd=1, relief=SUNKEN)
        status2c.grid(row=15, column=2, sticky=W)

        # ################## custom patt

        label3 = Label(self, text='User added patt')
        label3.grid(row=6, column=0, sticky=S)

        custom_new_patt_button = Button(self, text="Custom new", command=self.new_custom_window)
        custom_new_patt_button.grid(row=7, column=0, sticky=S)

        # ### ...WORK REQ in these optionmenu and button, now doing same as above
        w2 = OptionMenu(self, self.var1, *choices)
        w2.config(width=8)
        w2.grid(row=8, column=0, sticky=EW)

        go_button2 = Button(self, text="Go", command=self.select_pattern)
        go_button2.grid(row=9, column=0, sticky=N)
        # ### ...

    def new_custom_window(self):
        self.master.attributes("-topmost", 0)
        Custom_Grid(self)

    def select_pattern(self):
        '''
        set state back to initial - living and generation
        gets and set, a grid array to be used to make living/dead initial cells(rectangles)

        :return: nothing significant
        '''
        global generations, start  # set everything to 0, and pause/stop game
        start = False
        generations = 0

        patt1_name = self.var1.get()  # name of pattern to display
        patt1 = Patterns()
        patt1.new_pattern(
            patt1_name)  # a grid of ROWSxCOLS is made with init pattern of above is embedded, if not clear

        self.var4.set(
            patt1.patt_count_alives())  # to print initial live count which can't be calc in rules(), as start is != True

        self.grid = patt1.current_grid  # the new grid is copied to main grid holding variable

        self.canv.delete('all')  # to clear memory of canvas objs, if any
        self.draw_grid()  # draw the grid bcs it is not called again and again, to save memory

    def draw_grid(self):
        '''
        draws all rectangle whether alive or dead
        so shouldn't be called more often
        THUS rules() is implemented that way
        :return: nothing significant
        '''
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] != 0:
                    self.canv.create_rectangle(j * self.cell_size, i * self.cell_size, (j + 1) * self.cell_size,
                                               (i + 1) * self.cell_size, fill='yellow')
                else:
                    self.canv.create_rectangle(j * self.cell_size, i * self.cell_size, (j + 1) * self.cell_size,
                                               (i + 1) * self.cell_size, fill='gray')

    def alive_nebour(self, i, j):
        '''
        returns total alive neighbor
        :param i: row coordinate of the curent cell whose alive neighbor we want
        :param j: column coordinate
        '''
        x1 = i - 1 if not i <= 0 else i  # left and topmost neighbour has coord- (x1,y1)
        x2 = i + 1 if not i >= self.rows - 1 else i  # right and bottommost neighbour coord -(x2,y2)
        y1 = j - 1 if not j <= 0 else j
        y2 = j + 1 if not j >= self.cols - 1 else j
        count = 0
        for a in range(x1, x2 + 1):
            for b in range(y1, y2 + 1):
                if self.grid[a][b] != 0 and not (a == i and b == j):
                    count += 1
        return count

    def rules(self):
        global generations
        count_alive = 0
        if start == True:
            alives = np.zeros((self.rows, self.cols), int)
            for i in range(self.rows):
                for j in range(self.cols):
                    alives[i][j] = self.alive_nebour(i, j)  # array of alive neighbour count

            for i in range(self.rows):
                for j in range(self.cols):
                    if self.grid[i][j] == 1:
                        count_alive += 1

                    if (self.grid[i][j] == 0 and alives[i][j] == 3) or (
                            self.grid[i][j] == 1 and alives[i][j] not in (2, 3)):
                        self.cell_toggle_update(i, j,
                                                count_alive)  # cell updated (new rectangle drawn there ) as well as value 0/1 toggled
            generations += 1
            self.var3.set(str(generations))
            self.var4.set(count_alive)

        self.after(DELAY, g1.rules)

    def cell_toggle_update(self, i, j, count_alive):
        val = self.grid[i][j]
        if val == 0:
            self.canv.create_rectangle(j * self.cell_size, i * self.cell_size,
                                       (j + 1) * self.cell_size, (i + 1) * self.cell_size, fill='yellow')
            count_alive += 1
        else:
            self.canv.create_rectangle(j * self.cell_size, i * self.cell_size, (j + 1) * self.cell_size,
                                       (i + 1) * self.cell_size, fill='gray')
            count_alive -= 1

        self.grid[i][j] = 1 - self.grid[i][j]
        return count_alive

    def onScale(self, val):
        global DELAY, start
        v = int(float(val))
        if v == 0:
            start = False
        elif v:
            start = True
        self.var2.set(v)
        DELAY = (100 - v) * 15 + 1  # time after rules is self called

    def client_exit(self):
        exit()

    def turn_red(self, event):
        if start == True:
            event.widget["activeforeground"] = "red"

    def turn_green(self, event):
        if start == False:
            event.widget["activeforeground"] = "green"

    def turn_blue(self, event):
        event.widget["activeforeground"] = "blue"

    def start_game(self):
        global start
        start = True

    def stop_game(self):
        global start
        start = False

    def step_game(self):
        '''
        same as rules(), just not self called / called just once
        '''
        global start, generations
        start = False
        count_alive = 0
        alives = np.zeros((self.rows, self.cols), int)
        for i in range(self.rows):
            for j in range(self.cols):
                alives[i][j] = self.alive_nebour(i, j)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j]:
                    count_alive += 1
                if (self.grid[i][j] == 0 and alives[i][j] == 3) or (
                        self.grid[i][j] == 1 and alives[i][j] not in (2, 3)):
                    count_alive = self.cell_toggle_update(i, j, count_alive)

        generations += 1
        self.var3.set(str(generations))
        self.var4.set(count_alive)

    def reset_game(self, *event):
        global generations, start
        start = False
        generations = 0
        self.var1.set('clear')
        self.select_pattern()
        self.var3.set(str(generations))


############################


class Custom_Grid():
    '''
    for custom options
    can draw on current cloned grid in other window using mouse click
    clone it back
    so copied the current papa_grid array and then after updation, changed(not copy, original) it accordingly
    close the window and draw the changes

    rectangles are saved in a dict, responsive to button click using bind option
    ---
    save the grid as a user_pattern in a file
    these patterns can be opened using option menu 2
    then go
    '''

    def __init__(self, papa_grid):
        self.master = papa_grid
        self.newWindow = Toplevel(papa_grid.master)
        self.newWindow.resizable(0, 0)
        self.frame = Frame(self.newWindow)
        self.frame.pack()
        self.cur_grid = np.zeros((ROWS, COLS), int)

        for i in range(ROWS):
            for j in range(COLS):
                self.cur_grid[i][j] = papa_grid.grid[i][j]
        self.draw_gui()

    def draw_gui(self):
        self.cell_size = self.master.cell_size * 1.5
        self.canv = Canvas(self.frame, bg='black', relief=SUNKEN)
        self.canv_y = ROWS * self.cell_size
        self.canv_x = COLS * self.cell_size

        self.canv.config(width=self.canv_x, height=self.canv_y)
        self.canv.grid(row=0, column=0, rowspan=ROWS, columnspan=COLS)

        self.cells = {}
        for i in range(ROWS):
            for j in range(COLS):

                if self.cur_grid[i][j] == 1:
                    self.cells[(i, j)] = self.canv.create_rectangle(j * self.cell_size, i * self.cell_size,
                                                                    (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                                                                    fill='white')
                else:
                    self.cells[(i, j)] = self.canv.create_rectangle(j * self.cell_size, i * self.cell_size,
                                                                    (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                                                                    fill='gray')

                self.canv.tag_bind(self.cells[(i, j)], '<Button-1>', lambda event, i=i, j=j: self.toggle_cell(i, j))

        # buttons

        copy_only_button = Button(self.frame, text='Clone', command=self.copy_only)
        copy_only_button.grid(row=10, column=COLS)

        copy_save_button = Button(self.frame, text='Remember me', command=self.copy_save)
        copy_save_button.grid(row=15, column=COLS)

    def copy_only(self):
        for i in range(ROWS):
            for j in range(COLS):
                self.master.grid[i][j] = self.cur_grid[i][j]  # applying changes to the papa grid
        self.master.draw_grid()
        self.canv.delete(all)

        self.master.master.attributes("-topmost", True)
        self.newWindow.destroy()

    def copy_save(self):
        # work req #
        # test #
        mydict = {'a': 1, 'b': 2, 'c': 3}
        output = open('myfile.pkl', 'wb')
        pickle.dump(mydict, output)
        output.close()

        pkl_file = open('myfile.pkl', 'rb')
        mydict2 = pickle.load(pkl_file)
        pkl_file.close()

        print(mydict)
        print(mydict2)

        self.copy_only()

    def toggle_cell(self, i, j):
        val = self.cur_grid[i][j]
        if val == 0:
            self.canv.itemconfig(self.cells[(i, j)], fill='white')
            self.cur_grid[i][j] = 1
        else:
            self.canv.itemconfig(self.cells[(i, j)], fill='gray')
            self.cur_grid[i][j] = 0


root = Tk()

root.resizable(0, 0)

g1 = Grid(root)

g1.rules()

root.mainloop()

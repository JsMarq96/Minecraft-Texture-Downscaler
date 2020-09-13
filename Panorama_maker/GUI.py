from tkinter import Label, Entry, Button, Tk, filedialog, messagebox, END
from PIL import Image, ImageTk
from os import path
import time

'''
    GUI with tkinter for easier use without the command line
    by Juan S. Marquerie
'''

VERSION = '0.10'

def define_GUI(tk_window):
    # Window Config
    tk_window.title('Minecraft Panorama Utility v ' + VERSION)
    tk_window.geometry('500x200')

    # Labels
    label_folder_origin = Label(tk_window, text='Minecraft folder direction')
    label_folder_origin.grid(column=0, row=0)
    label_folder_origin = Label(tk_window, text='INSTRUCTIONS:')
    label_folder_origin.grid(column=3, row=0)
    label_folder_origin = Label(tk_window, text='First select your .minecraft folder')
    label_folder_origin.grid(column=3, row=1)
    label_folder_origin = Label(tk_window, text='Then, click the panorama and')
    label_folder_origin.grid(column=3, row=2)
    label_folder_origin = Label(tk_window, text='change to the minecraft window')
    label_folder_origin.grid(column=3, row=3)
    label_folder_origin = Label(tk_window, text='And wait for the timer to run out,')
    label_folder_origin.grid(column=3, row=4)
    label_folder_origin = Label(tk_window, text='and wait for the panoraming to be done!')
    label_folder_origin.grid(column=3, row=5)

    # Text Input
    minecraft_direction_input = Entry(tk_window, width=25)
    minecraft_direction_input.grid(column=0, row=1)

    # Button Events
    def launch_direction_search():
        selected_folder = filedialog.askdirectory()
        minecraft_direction_input.delete(0, END)
        minecraft_direction_input.insert(0,selected_folder)

    def panorama():
        from Panorama_maker import make_panorama_imgs
        button_resize.configure(state='disabled')
        tk_window.update()

        # Timer
        for i in range(4):
            time.sleep(1)
            button_resize.configure(text=str(i))
            tk_window.update()

        button_resize.configure(text='Panoraming...')
        tk_window.update()
        dir_txt = minecraft_direction_input.get()

        make_panorama_imgs(dir_txt)

        messagebox.showinfo('Minecraft Panorama Utility v ' + VERSION, 'Finished panoraming! Its stored on the background folder on the .minecraft folder')
        button_resize.configure(state='normal', text='Make panorama')
        tk_window.update()

    # Buttons
    button_search = Button(tk_window, text='Search', command=launch_direction_search)
    button_search.grid(column=1, row=1)
    button_resize = Button(tk_window, text='Make panorama', command=panorama)
    button_resize.grid(column=2, row=6)

'''
    Launch the GUI
'''
if __name__ == '__main__':
    window = Tk()
    define_GUI(window)
    window.mainloop()
import tkinter as tk
import superheros

def print_char_name():
    name = character.get()
    print(name)

def display_char_stats():
    name = character.get()
    stats = superheros.get_power_stats(name)
    name_label.configure(text=f"{name} Stats: {stats}")



bg_color = "#04d9d2"


window = tk.Tk()
window.title("Power Profiler")
window.geometry("550x450")
window.configure()



greeting = tk.Label(window, text="Welcome to the Power Profiler", font=('Times 24'), width=60)
greeting.pack()

ask = tk.Label(window, text="Please type in a character name to get their Power Profile: ")
ask.pack()

character = tk.Entry(window)
character.pack()

# print_button = tk.Button(window, text="Print Character Name", command=print_char_name)
# print_button.pack()

show_name_button = tk.Button(window, text=" Display Character Stats", command=display_char_stats)
show_name_button.pack()

name_label = tk.Label(window, text="Character Stats: ")
name_label.pack()


window.mainloop()
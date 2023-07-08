import tkinter as tk

def print_char_name():
    name = character.get()
    print(name)




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

print_button = tk.Button(window, text="Print Character Name", command=print_char_name)
print_button.pack()


window.mainloop()
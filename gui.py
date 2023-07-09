import tkinter as tk
import superheros
from PIL import ImageTk, Image

def print_char_name():
    name = character.get()
    print(name)

def display_char_stats():
    name = character.get()
    stats = superheros.get_power_stats(name)
    
    i = 0
    try:
        image_path = f"./character_images/{name}.jpg"
        character_image = Image.open(image_path)
    except:
        image_path = "./character_images/no-image.jpg"
        character_image = Image.open(image_path)
        
    character_image = character_image.resize((200, 200))
    character_photo = ImageTk.PhotoImage(character_image)
    character_image_label.configure(image=character_photo)
    character_image_label.image = character_photo
    
    for key, value in stats.items():
        if key == "response" or key == "id":
            continue
        key_label = tk.Label(stats_frame, text=key+":")
        key_label.grid(row=i, column=0, sticky='e')
        
        value_label = tk.Label(stats_frame, text=value)
        value_label.grid(row=i, column=1, sticky='w')
        
        i += 1





bg_color = "#04d9d2"


window = tk.Tk()
window.title("Power Profiler")
window.geometry("550x450")
window.configure()



greeting = tk.Label(window, text="Welcome to the Power Profiler", font=('Tekton Pro', 24, "bold"), width=60)
greeting.pack()

ask = tk.Label(window, text="Please type in a character name to get their Power Profile: ")
ask.pack()

character = tk.Entry(window)
character.pack()

# print_button = tk.Button(window, text="Print Character Name", command=print_char_name)
# print_button.pack()

show_name_button = tk.Button(window, text=" Display Character Stats", command=display_char_stats)
show_name_button.pack()

main_frame = tk.Frame(window)
main_frame.pack()


image_frame = tk.Frame(main_frame)
image_frame.pack(side="left", padx=10)

character_image_label = tk.Label(image_frame)
character_image_label.pack()

stats_frame = tk.Frame(main_frame)
stats_frame.pack(side="left", padx=10)

window.mainloop()
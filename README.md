# PowerProfiler

## How to run the application:

### inital steps

1. Clone the repository to your local computer

2. create an account with "https://superheroapi.com"

3. Once done, you should receive an API key.

4. Add your api key to the script (you can do this by either):
    - creating a cped.py file in the main directory and adding you key to a variable called TOKEN
    - or, insert your token directly into the variable called "key" in the "get_power_stats" function

### GUI

If you want to run your program within the gui, you will have to run the gui.py file on your local machine.

1. run this on your terminal

```
python3 gui.py
```
A user interface will deploy and it will ask for you to type in a name

The character list include 731 characters, a vast list, but does not include every character ever. If you want to know all the characters who are available, please see "heroList.py"

2. Type in a character name that appears on the character list

3. PowerStats should display next to an image of the character

4. If an image is not available, the interface will say so


## Project Overview

This is just a fun personal project to practice the uses of APIs and also get familiar with GUI projects. 

I hope to gain insight on best practices when it comes to using APIs; like security with tokens, different uses for calls (GET, POST, DEL, etc), and structuring my code when using an API. I also plan on using Azure DevOps platform to build and publish and artifact of the character builds. I believe going this extra step will help me with configuring and understanding end to end processes of software development.

The use of the GUI will be new to me. I have not had any projects that use GUIs, so I believe learning and understanding how the front-end interacts with the back-end will also help me in getting a deeper knowledge of how more robust applications operate.

As stated earlier, I plan to use Azure DevOps platform to build and test the application to have some automation involved. I will also utlize Azure KeyVault to store sensitive data and access that data through ADO to be able to connect to the API.

## Preparation

# Questions:

* How can I get information about a specific character?

* How to get the id mathcing the indentifying character?

* What information is presented in the API call and how should i parse it?

* How to display the character image and stats in the GUI?

* How do I iterate over the API response and display each power stat on the GUI.

## How it works

# The GUI

The application now has a GUI icorporated. Directions on how to use are listed at the top. i enjoyed this project and using the GUI. This was my first time having a project with an interface. It presented some challenges such as:

* incorporating the api script into the gui file and adding logic to add the data from the response to the gui

* fethcing the name that was given in the entry box and feeding it to the "get_power_stats" function

* displaying the image and the stats next to eachother, having to incorporate both the gird and pack functions so that the gui will format with the resizing of the window

Overall this was a great project for me to test the use of interfaces with a backend. I plan on trying different GUI libraries out too in future projects
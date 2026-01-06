# By transcrime
# GPL-3.0 license

import sys
import dearpygui
import dearpygui.dearpygui as window
import os
import subprocess

# Note this project is just for fun so keep working on it but it not priority

prefix = "https://github.com/" # this is no longer being used but keep it just in case

# secondary window 500x500
def clone_repo_callback(sender, data): # this def function will be activated when the button is clicked this because of callback=get_link_callback 
    with window.window(label="Secondary Window", width=500, height=500):
        window.add_text("This is the new window!")
        window.add_button(label="Close This", callback=lambda s: window.delete_item,)
        window.add_input_text(label="Insert your get link", tag="REPO_LINK")
        window.add_button(label="Submit", callback=get_link_callback)

def get_link_callback():
    user_input = window.get_value("REPO_LINK")                 
    print(f"User link: {user_input}")
    subprocess.run(["git", "clone", f"{user_input}"])
    cd_name_getting = os.path.splitext(os.path.basename(user_input))[0] # This splits the https:// and .git
    print(cd_name_getting)
   


def exit_callback():
 sys.exit() 


window.create_context()

# main window 900x900 
with window.window(label="Git GUI Application", width=900, height=900, no_move=True, no_resize=True):
    window.add_text("Welcome to the Git GUI Application!")
    
# There is only two buttons that do something the rest are just for show
    clone_button = window.add_button(label="Clone Repository", callback=clone_repo_callback)
   
    window.add_button(label="Commit Changes")
    window.add_button(label="Push to Remote")
    exit_button = window.add_button(label="exit", callback=exit_callback )
    
        
    


# I'm still learning this Library bear with me
window.create_viewport(title='Git GUI Application', width=900, height=900)
window.setup_dearpygui()
window.show_viewport()
window.start_dearpygui()
window.destroy_context()
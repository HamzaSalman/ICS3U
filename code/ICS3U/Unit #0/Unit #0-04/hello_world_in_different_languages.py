# Created by: Hamza Salman
# Created on: September 2016
# Created for: ICS3U
# This is the hello world program in differnt languages with buttons

import ui 

def hello_world_english_touch_up_inside(sender):
    view['hello_world_in_different_languages'].text = ('Hello, World!')
	
def hello_world_spanish_touch_up_inside(sender):
    view['hello_world_in_different_languages'].text = ('Hola, Mundo!')
	
def hello_world_french_touch_up_inside(sender):
    view['hello_world_in_different_languages'].text = ('Bonjour, Monde!')

view = ui.load_view()
view.present('full_screen')

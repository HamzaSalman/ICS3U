# Created by: Hamza Salman
# Course: ICS3U
# Created: September 2016
# This program is used to calculate the cost of a pizza

import ui

def calculate_button_touch_up_inside(sender):
    #this function calculates the cost of a pizza

    LABOUR = 0.75
    SHOP_RENT = 1.00
    HST = 1.13

    diameter = float(view['diameter_textfield'].text)

    price = (SHOP_RENT + LABOUR + 0.5 * diameter) * HST
    view['cost_label'].text = 'The cost is: ' + '${:,.2f}'.format(price);

view = ui.load_view()
view.present('full_screen')

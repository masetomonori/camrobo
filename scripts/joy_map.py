import json
import os

class JoyMap():

    button_A = 0
    button_B = 0
    button_X = 0
    button_Y = 0

    axis_cross_h = 0
    axis_cross_v = 0
    axis_stick_h_r = 0
    axis_stick_v_r = 0
    axis_stick_h_l = 0
    axis_stick_v_l = 0

    def __init__(self):
        dirname = os.path.dirname(__file__)
        with open(dirname + '/joy_config.json') as f:
            jsn = json.load(f)

            self.button_A = jsn["buttons"]["A"]
            self.button_B = jsn["buttons"]["B"]
            self.button_X = jsn["buttons"]["X"]
            self.button_Y = jsn["buttons"]["Y"]

            self.axis_cross_h   = jsn["axes"]["cross_h"]
            self.axis_cross_v   = jsn["axes"]["cross_v"]
            self.axis_stick_h_r = jsn["axes"]["stick_h_r"]
            self.axis_stick_v_r = jsn["axes"]["stick_v_r"]
            self.axis_stick_h_l = jsn["axes"]["stick_h_l"]
            self.axis_stick_v_l = jsn["axes"]["stick_v_l"]


#!/bin/bash -xve

sudo touch /dev/dc_GPIO_{06,13,20,21}
sudo chmod 666 /dev/dc_GPIO_{06,13,20,21}
#echo "0 0 0 0" | sudo tee /dev/rtlightsensor0



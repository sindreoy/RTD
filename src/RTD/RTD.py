#!/usr/bin/python
# -*- coding: ascii -*-
from __future__ import absolute_import, division, print_function  # v2.7 -> 3.5
"""

oooooooooooo       oooo oooo                    ooooo                 .o8
`888'     `8       `888 `888                    `888'                "888
 888       .ooooo.  888  888  .ooooo.  .oooo.o   888         .oooo.   888oooo.
 888oooo8 d88' `88b 888  888 d88' `88bd88(  "8   888        `P  )88b  d88' `88b
 888    " 888ooo888 888  888 888ooo888`"Y88b.    888         .oP"888  888   888
 888      888    .o 888  888 888    .oo.  )88b   888       od8(  888  888   888
o888o     `Y8bod8P'o888oo888o`Y8bod8P'8""888P'  o888ooooood8`Y888""8o `Y8bod8P'


@summary:      Felles lab GUI graphics parent classes
@author:       Sigve Karolius
@organization: Department of Chemical Engineering, NTNU, Norway
@contact:      sigveka@ntnu.no
@license:      Free (GPL.v3)
@requires:     Python 2.7.x or higher
@since:        18.06.2015
@version:      2.7
@todo 1.0:
@change:
@note:

"""

__author__  = "Sigve Karolius"
__license__ = "GPL.v3"
__date__    = "$Date: 2015-06-23 (Tue, 23 Jun 2015) $"

from adam_modules import Adam4117, Adam4019
from mac_motor import Mac050
from time import sleep
from FellesLab import MasterClass, Voltage, Pump


def main(GUI=False):

    module2 = Adam4117(
                base="Instrument", # "Dummy" OR "Instrument"
                portname = '/dev/ttyUSB0',
                slaveaddress = 6,
              )

    # module1 = Adam4117(portname='/dev/ttyUSB2',slaveaddress = 8)

    Framework = MasterClass()

    a = Pump(
          resource = Mac050(module2.serial, 1),
          resource_settings = {
             'label' : 'Pump',
             'unit' : '[rpm]',
             'sample_speed' : 2,
            'min_velocity' : 0,
            'max_velocity' : 4000,
            'min_speed': 0,
            'max_speed': 400,
            'min_acceleration' : 0,
            'max_acceleration' : 100,
          },
          data_processing = {
              'calibrationCurve' : lambda x: x, # Calibration curve
          },
          gui_configuration = {
             'plot' : False,
             'time_span' : 20, # seconds
             'color': 'red',
          },
     )
    sleep(0.1)

    b = Voltage(
          resource = module2,
          resource_settings = {
            'channel' : 3, # Configure module, set channel etc...
            'decimals' : 4,
         },
         meta_data = {
            'label' : 'Top',
            'unit' : '[V]',
            'sample_speed' : 0.1,
         },
         data_processing = {
             'calibrationCurve' : lambda x: x, # Calibration curve
         },
         gui_configuration = {
            'plot' : True,
            'time_span' : 20, # seconds
            'color': 'magenta',
         },
    )

    c = Voltage(
          resource = module2,
          resource_settings = {
            'channel' : 4, # Configure module, set channel etc...
            'decimals' : 4,
         },
         meta_data = {
            'label' : 'Bottom',
            'unit' : '[V]',
            'sample_speed' : 0.1,
         },
         data_processing = {
             'calibrationCurve' : lambda x: x, # Calibration curve
         },
         gui_configuration = {
            'plot' : True,
            'time_span' : 20, # seconds
            'color': 'cyan',
         },
    )

    if GUI:
        Framework.InitGUI()

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
if __name__ == "__main__":
    main(True)


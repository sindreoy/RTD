"""

oooooooooooo       oooo oooo                    ooooo                 .o8      
`888'     `8       `888 `888                    `888'                "888      
 888       .ooooo.  888  888  .ooooo.  .oooo.o   888         .oooo.   888oooo. 
 888oooo8 d88' `88b 888  888 d88' `88bd88(  "8   888        `P  )88b  d88' `88b
 888    " 888ooo888 888  888 888ooo888`"Y88b.    888         .oP"888  888   888
 888      888    .o 888  888 888    .oo.  )88b   888       od8(  888  888   888
o888o     `Y8bod8P'o888oo888o`Y8bod8P'8""888P'  o888ooooood8`Y888""8o `Y8bod8P'


@summary:
@author:       Sigve Karolius
@organization: Department of Chemical Engineering, NTNU, Norway
@contact:      sigveka@ntnu.no
@license:      Free (GPL.v3), although credit is appreciated  
@requires:     Python 2.7.x or higher
@since:        18.06.2015
@version:      2.7
@todo 1.0:     
@change:       
@note:         

"""

from os import getenv
from os.path import abspath, dirname, join
from glob import glob
# from distutils.core import setup, Extension
from setuptools import setup

args = {
  'name'        : 'RTD',
  'description' : 'RTD Experiment',
  'version'     : '0.1',
  'packages'    : [
    'RTD',
    'FellesLab',
    'adam_modules', 'adam_modules.utils',
    'mac_motor', 'mac_motor.emergencyStop',
  ],
  'package_dir'    : {
    'RTD'          : join('src','RTD'),
    'FellesLab'    : join('src','FellesLab'),
    'adam_modules' : join('src','adam_modules'),
    'adam_modules.utils' : join('src','adam_modules','utils'),
    'mac_motor'    : join('src','mac_motor'),
    'mac_motor.emergencyStop' : join('src','mac_motor','emergencyStop'),
  },
  'package_data' : {
  },
  'data_files' : [
    (join('RTD','bitmaps') ,       [join('data', 'img', 'desktop_rtd.png')]),
    (join('mac_motor','bitmaps') , [join('data', 'img', 'desktop_stop_motor.png')]),
  ],
  'include_package_data' : True,
  'install_requires' : [
   'minimalmodbus',
  ]
}

setup(**args)


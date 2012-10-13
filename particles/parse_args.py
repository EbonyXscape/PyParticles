# PyParticles : Particles simulation in python
# Copyright (C) 2012  Simone Riva
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import argparse
from particles.pypart_global import py_particle_version

def parse_args():
    desc = "PyParticles is a particle simulation tool box that support the most diffused numerical integration " 
    desc = desc + " and forces models "

    parser = argparse.ArgumentParser( description=desc , version="%(prog)s " + py_particle_version()  )


    parser.add_argument("-m", "--config_model",
        action="store_true",
        dest="config_model",
        help="Write out the model of a config file and exit")
    

    parser.add_argument(
        dest="path_name",
        nargs='?',
        default=None
        )
    
    return parser.parse_args()

############################################################################
# This module is a part of the Polyrot numerical package.  
#
# Copyright (C) 2023 Janosz Dewberry
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by the 
# Free Software Foundation, version 3.
#
# Polyrot is distributed in the hope that it will be useful, but WITHOUT ANY 
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more 
# details.
#
# You should have received a copy of the GNU General Public License along 
# with this program. If not, see http://www.gnu.org/licenses/.
############################################################################
# Module: helpers
# Brief: quality-of-life function definitions
############################################################################

from scipy.interpolate import splev,splrep

def terp(x0,y0,x):
    '''
        creates spline interpolator given y0(x0), and evaluates at new
        independent x
    '''
    return splev(x,splrep(x0,y0))
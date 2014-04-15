#!/usr/bin/env python
# ValkEye SIP Phone, vegpio.py, reads gpio values from procfs
# Ernesto Celis <developer@celisdelafuente.net>
# Nov. 2013
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA 
#

import os
import sys
from syslog import syslog as logger
from syslog import LOG_INFO as log_info
from syslog import LOG_ERR as log_err

INPUT = 0
OUTPUT = 1
#TODO PWM_OUTPUT = 2
PULLUP = 3
PULLDOWN = 4
PULLOFF = 5
#TODO CHECK = 6
#TODO GPIO_CLOCK = 7

LOW = 0
HIGH = 1

#TODO Make it dynamically load GPIO pins from /sys/class/gpio dir
GPIO_PATH = '/sys/class/gpio/'
VAL='/value'
DIR='/direction'

def _readPinValue(pin):
    with open(GPIO_PATH + pin + VAL, 'r') as f:
        for line in f:
            return line.rstrip('\n')

def digitalRead(pin):
    val = None
    try:
        val = _readPinValue(pin)
        if val is not None:
            return int(_readPinValue(pin))
    except:
        return None

def digitalWrite(pin, value):
    pass

def listen():
    #TODO Pass a list or dictionary of pins and iterate over it
    if digitalRead('gpio4_pg1') == 0:
        return "women"
    if digitalRead('gpio6_pg5') == 0:
        return "police"
    if digitalRead('gpio8_pg7') == 0:
        return "fire"
    if digitalRead('gpio9_pg9') == 0:
        return "cr"
    if digitalRead('gpio9_pg9') == 0:
        return "pc"
    #if digitalRead('gpio11_pg11') == 1:
        return "son"
    #elif digitalRead('gpio11_pg11') == 0:
        return "soff"





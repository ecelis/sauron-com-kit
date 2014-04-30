#!/usr/bin/env python
# ValkEye SIP Phone, vewiring.py
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
import syslog
import wiringpi2 as wp

HIGH = 1
LOW = 0

OUT_SPEAKER = 1

PIN_WOMEN = 23
PIN_POLICE = 19
PIN_CR = 13
PIN_FIRE = 15
PIN_SIREN = 14
PIN_PC = 22
PIN_SPEAKER = 48

DELAY = 50

wp.wiringPiSetup()

def listenButton():
    res = None
    pin_women = wp.digitalRead(PIN_WOMEN)
    pin_police = wp.digitalRead(PIN_POLICE)
    pin_cr = wp.digitalRead(PIN_CR)
    pin_fire = wp.digitalRead(PIN_FIRE)
    pin_siren = wp.digitalRead(PIN_SIREN)
    pin_pc = wp.digitalRead(PIN_PC)

    if pin_women == 0:
        res = "women"

    if pin_pc == 1:
        res = "son"
    else:
        res = "soff"

    if pin_police == 0:
        res = "police"

    if pin_cr == 0:
        res = "cr"

    if pin_fire == 0:
        res = "fire"

    if pin_siren == 0:
        res = "siren"

    return res



def delay():
    wp.delay(DELAY)


def speaker_on():
    wp.digitalWrite(PIN_SPEAKER, HIGH)
    return 1

def speaker_off():
    wp.digitalWrite(PIN_SPEAKER, LOW)
    return 0
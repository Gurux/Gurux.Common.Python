#
#  --------------------------------------------------------------------------
#   Gurux Ltd
#
#
#
#  Filename: $HeadURL$
#
#  Version: $Revision$,
#                $Date$
#                $Author$
#
#  Copyright (c) Gurux Ltd
#
# ---------------------------------------------------------------------------
#
#   DESCRIPTION
#
#  This file is a part of Gurux Device Framework.
#
#  Gurux Device Framework is Open Source software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2 of the License.
#  Gurux Device Framework is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  More information of Gurux products: http://www.gurux.org
#
#  This code is licensed under the GNU General Public License v2.
#  Full text may be retrieved at http://www.gnu.org/licenses/gpl-2.0.txt
# ---------------------------------------------------------------------------
import sys

#Maximum size of byte.
_MAX_BYTE_SIZE = 0xFF
_NIBBLE = 4
#Value of Hex A in decimal.
_HEX_A_DECIMAL_VALUE = 10

###Python 2 requires this
#pylint: disable=bad-option-value,old-style-class
class GXCommon:
    #pylint: disable=too-few-public-methods
    """General methods for communication."""

    def __init__(self, data=None, senderInfo=None):
        """
        Constructor.
        """

    @classmethod
    def getVersion(cls):
        """Is this version 2."""
        return sys.version_info

    @classmethod
    def isV2(cls):
        """Is this version 2."""
        return sys.version_info < (3, 0)

    @classmethod
    def toHex(cls, value):
        """Convert data to hex."""
        #Return empty string if array is empty.
        if not value:
            return ""
        __hexArray = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
        LOW_BYTE_PART = 0x0F
        hexChars = ""
        for it in value:
            hexChars += __hexArray[it >> _NIBBLE]
            hexChars += __hexArray[it & LOW_BYTE_PART]
            hexChars += ' '
        return hexChars

    #Convert char hex value to byte value.
    @classmethod
    def ___getValue(cls, c):
        #Id char.
        if c > '9':
            if c > 'Z':
                value = c.encode()[0] - 'a'.encode()[0]
            else:
                value = c.encode()[0] - 'A'.encode()[0]
            value += _HEX_A_DECIMAL_VALUE
        else:
            #If number.
            value = c.encode()[0] - '0'.encode()[0]
        return value

    @classmethod
    def hexToBytes(cls, value):
        ###Convert string to byte array.###
        buff = bytearray()
        lastValue = -1
        for ch in value:
            if '0' >= ch < 'g':
                if lastValue == -1:
                    lastValue = cls.___getValue(ch)
                elif lastValue != -1:
                    buff.append(lastValue << _NIBBLE | cls.___getValue(ch))
                    lastValue = -1
            elif lastValue != -1:
                buff.append(cls.___getValue(ch))
                lastValue = -1
        return buff

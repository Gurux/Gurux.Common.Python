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
import abc
from .ReceiveEventArgs import ReceiveEventArgs
from .MediaStateEventArgs import MediaStateEventArgs
from .PropertyChangedEventArgs import PropertyChangedEventArgs
from .TraceEventArgs import TraceEventArgs

#pylint: disable=no-self-argument
class IGXMediaListener(metaclass=abc.ABCMeta):
    """Media component will notify events throught this interface."""

    @abc.abstractmethod
    def onError(sender, ex):
        """
        Represents the method that will handle the error event of a Gurux
        component.

        sender :  The source of the event.
        ex : An Exception object that contains the event data.
        """

    @abc.abstractmethod
    def onReceived(sender, e: ReceiveEventArgs):
        """Media component sends received data through this method.

        sender : The source of the event.
        e : Event arguments.
        """

    @abc.abstractmethod
    def onMediaStateChange(sender, e: MediaStateEventArgs):
        """Media component sends notification, when its state changes.
        sender : The source of the event.
        e : Event arguments.
        """

    @abc.abstractmethod
    def onTrace(sender, e: TraceEventArgs):
        """Called when the Media is sending or receiving data.

        sender : The source of the event.
        e : Event arguments.
        """

    @abc.abstractmethod
    def onPropertyChanged(sender, e: PropertyChangedEventArgs):
        """
        Event is raised when a property is changed on a component.

        sender : The source of the event.
        e : Event arguments.
        """

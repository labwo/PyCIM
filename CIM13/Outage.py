#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13.Core import IdentifiedObject
from CIM13.Core import IrregularIntervalSchedule



from enthought.traits.api import Instance, List, Enum, Str, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


SwitchState = Enum("close", "open")

#------------------------------------------------------------------------------
#  "ClearanceTagType" class:
#------------------------------------------------------------------------------

class ClearanceTagType(IdentifiedObject):
    """ Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ClearanceTags = List(Instance("CIM13.Outage.ClearanceTag"))

    #--------------------------------------------------------------------------
    #  Begin "ClearanceTagType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "ClearanceTags",
                label="References"),
            dock="tab"),
        id="CIM13.Outage.ClearanceTagType",
        title="ClearanceTagType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ClearanceTagType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SwitchingOperation" class:
#------------------------------------------------------------------------------

class SwitchingOperation(IdentifiedObject):
    """ A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A switch may be operated by many schedules.
    Switches = List(Instance("CIM13.Wires.Switch"),
        desc="A switch may be operated by many schedules.")

    # An OutageSchedule may operate many switches.
    OutageSchedule = Instance("CIM13.Outage.OutageSchedule",
        desc="An OutageSchedule may operate many switches.",
        opposite="SwitchingOperations")

    # The switch position that shall result from this SwitchingOperation
    newState = SwitchState(desc="The switch position that shall result from this SwitchingOperation")

    # Time of operation in same units as OutageSchedule.xAxixUnits.
    operationTime = Str(desc="Time of operation in same units as OutageSchedule.xAxixUnits.")

    #--------------------------------------------------------------------------
    #  Begin "SwitchingOperation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "newState", "operationTime",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "Switches", "OutageSchedule",
                label="References"),
            dock="tab"),
        id="CIM13.Outage.SwitchingOperation",
        title="SwitchingOperation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchingOperation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageSchedule" class:
#------------------------------------------------------------------------------

class OutageSchedule(IrregularIntervalSchedule):
    """ The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An OutageSchedule may operate many switches.
    SwitchingOperations = List(Instance("CIM13.Outage.SwitchingOperation"),
        desc="An OutageSchedule may operate many switches.")

    # A power system resource may have an outage schedule
    PSR = Instance("CIM13.Core.PowerSystemResource",
        desc="A power system resource may have an outage schedule",
        opposite="OutageSchedule")

    #--------------------------------------------------------------------------
    #  Begin "OutageSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "TimePoints", "SwitchingOperations", "PSR",
                label="References"),
            dock="tab"),
        id="CIM13.Outage.OutageSchedule",
        title="OutageSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ClearanceTag" class:
#------------------------------------------------------------------------------

class ClearanceTag(IdentifiedObject):
    """ A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Conducting equipment may have multiple clearance tags for authorized field work
    ConductingEquipment = Instance("CIM13.Core.ConductingEquipment",
        desc="Conducting equipment may have multiple clearance tags for authorized field work",
        opposite="ClearanceTags")

    ClearanceTagType = Instance("CIM13.Outage.ClearanceTagType",
        opposite="ClearanceTags")

    # Description of the work to be performed
    workDescription = Str(desc="Description of the work to be performed")

    # The time at which the clearance tag is scheduled to be set.
    workStartTime = Str(desc="The time at which the clearance tag is scheduled to be set.")

    # The name of the person who is authorized to issue the tag
    authorityName = Str(desc="The name of the person who is authorized to issue the tag")

    # Set true if equipment must be deenergized
    deenergizeReqFlag = Bool(desc="Set true if equipment must be deenergized")

    # The time at which the clearance tag is scheduled to be removed
    workEndTime = Str(desc="The time at which the clearance tag is scheduled to be removed")

    # The time at which the clearance tag was issued
    tagIssueTime = Str(desc="The time at which the clearance tag was issued")

    # Set true if equipment must be grounded
    groundReqFlag = Bool(desc="Set true if equipment must be grounded")

    # Set true if equipment phasing must be checked
    phaseCheckReqFlag = Bool(desc="Set true if equipment phasing must be checked")

    #--------------------------------------------------------------------------
    #  Begin "ClearanceTag" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "workDescription", "workStartTime", "authorityName", "deenergizeReqFlag", "workEndTime", "tagIssueTime", "groundReqFlag", "phaseCheckReqFlag",
                label="Attributes", columns=1),
            VGroup("ContainedBy", "ModelingAuthoritySet", "ConductingEquipment", "ClearanceTagType",
                label="References"),
            dock="tab"),
        id="CIM13.Outage.ClearanceTag",
        title="ClearanceTag",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ClearanceTag" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------

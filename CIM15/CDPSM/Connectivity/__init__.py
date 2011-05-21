# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""The IEC 61968 subpackages of the CIM are developed, standardized and maintained by IEC TC57 Working Group 14: interfaces for distribution management (WG14). Currently, normative parts of the model support the needs of information exchange defined in IEC 61968-9 and in IEC 61968-13.
"""

from CIM15.CDPSM.Connectivity.Element import Element

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15?profile=http://iec.ch/TC57/2011/iec61968-13/CDPSM/Connectivity"
nsPrefix = "conn"

packageMap = {
    "Element": "CIM15.CDPSM.Connectivity",
    "Fuse": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "EnergyConsumer": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "Switch": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "Disconnector": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "ACLineSegment": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "SynchronousMachine": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "BusbarSection": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "LoadBreakSwitch": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "TransformerTank": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "GroundDisconnector": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "PowerTransformerEnd": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "Junction": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "SeriesCompensator": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "Breaker": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "TransformerTankEnd": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "Sectionaliser": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "DCLineSegment": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "Line": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "Conductor": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "PowerTransformer": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "Ground": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "TransformerEnd": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "ShuntCompensator": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "EnergySource": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "Jumper": "CIM15.CDPSM.Connectivity.IEC61970.Wires",
    "ShuntCompensatorPhase": "CIM15.CDPSM.Connectivity.IEC61970.WiresPhaseModel",
    "SwitchPhase": "CIM15.CDPSM.Connectivity.IEC61970.WiresPhaseModel",
    "Terminal": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "Bay": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "NameTypeAuthority": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "VoltageLevel": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "SubGeographicalRegion": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "PSRType": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "EquipmentContainer": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "ConductingEquipment": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "GeographicalRegion": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "NameType": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "Equipment": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "IdentifiedObject": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "ConnectivityNodeContainer": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "Substation": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "ConnectivityNode": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "Name": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "BaseVoltage": "CIM15.CDPSM.Connectivity.IEC61970.Core",
    "PowerSystemResource": "CIM15.CDPSM.Connectivity.IEC61970.Core",
}


class Length(float):
    """Unit of length.
    """
    pass

class Voltage(float):
    """Electrical voltage.
    """
    pass

class CIMTime(str):
    pass

class CIMDateTime(str):
    pass

class CIMDuration(str):
    pass

class CIMGYear(str):
    pass

class CIMDate(str):
    pass

class CIMGMonthDay(str):
    pass

class CIMGMonth(str):
    pass

class CIMGDay(str):
    pass

class CIMGYearMonth(str):
    pass

from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://iec.ch/TC57/"


class AbnormalOPcatKind(Enum):
    """Kinds of abnormal opertaion categories.

    Reference: IEEE1547-2018.

    :cvar catI: Category CAT_I.
    :cvar catII: Category CAT_II.
    :cvar catIII: Category CAT_III.
    """
    catI = "catI"
    catII = "catII"
    catIII = "catIII"


class AmiBillingReadyKind(Enum):
    """
    Lifecycle states of the metering installation at a usage point with respect
    to readiness for billing via advanced metering infrastructure reads.

    :cvar amiCapable: Usage point is equipped with an AMI capable meter
        that is not yet currently equipped with a communications module.
    :cvar amiDisabled: Usage point is equipped with an AMI capable
        meter; however, the AMI functionality has been disabled or is
        not being used.
    :cvar billingApproved: Usage point is equipped with an operating AMI
        capable meter and accuracy has been certified for billing
        purposes.
    :cvar enabled: Usage point is equipped with an AMI capable meter
        having communications capability.
    :cvar nonAmi: Usage point is equipped with a non AMI capable meter.
    :cvar nonMetered: Usage point is not currently equipped with a
        meter.
    :cvar operable: Usage point is equipped with an AMI capable meter
        that is functioning and communicating with the AMI network.
    """
    amiCapable = "amiCapable"
    amiDisabled = "amiDisabled"
    billingApproved = "billingApproved"
    enabled = "enabled"
    nonAmi = "nonAmi"
    nonMetered = "nonMetered"
    operable = "operable"


class CableConstructionKind(Enum):
    """
    Kind of cable construction.

    :cvar compacted: Compacted cable.
    :cvar compressed: Compressed cable.
    :cvar other: Other kind of cable construction.
    :cvar sector: Sector cable.
    :cvar segmental: Segmental cable.
    :cvar solid: Solid cable.
    :cvar stranded: Stranded cable.
    """
    compacted = "compacted"
    compressed = "compressed"
    other = "other"
    sector = "sector"
    segmental = "segmental"
    solid = "solid"
    stranded = "stranded"


class CableOuterJacketKind(Enum):
    """
    Kind of cable outer jacket.

    :cvar insulating: Insulating cable outer jacket.
    :cvar linearLowDensityPolyethylene: Linear low density polyethylene
        cable outer jacket.
    :cvar none: Cable has no outer jacket.
    :cvar other: Pther kind of cable outer jacket.
    :cvar polyethylene: Polyethylene cable outer jacket.
    :cvar pvc: PVC cable outer jacket.
    :cvar semiconducting: Semiconducting cable outer jacket.
    """
    insulating = "insulating"
    linearLowDensityPolyethylene = "linearLowDensityPolyethylene"
    none = "none"
    other = "other"
    polyethylene = "polyethylene"
    pvc = "pvc"
    semiconducting = "semiconducting"


class CableShieldMaterialKind(Enum):
    """
    Kind of cable shield material.

    :cvar aluminum: Aluminum cable shield.
    :cvar copper: Copper cable shield.
    :cvar lead: Lead cable shield.
    :cvar other: Other kind of cable shield material.
    :cvar steel: Steel cable shield.
    """
    aluminum = "aluminum"
    copper = "copper"
    lead = "lead"
    other = "other"
    steel = "steel"


class ConstantPowerFactorSettingKind(Enum):
    """The kinds of constant power factor setting.

    Reference: IEEE1547-2018.

    :cvar abs: ABS.
    :cvar inj: INJ.
    """
    abs = "abs"
    inj = "inj"


class ConverterControlMode(Enum):
    """
    :cvar constantPowerFactor: hold q/p constant
    :cvar constantReactivePower: Holds constant Q; may change both P and
        Q by dispatch commands
    :cvar dynamic: use association with DERIEEEType1
    """
    constantPowerFactor = "constantPowerFactor"
    constantReactivePower = "constantReactivePower"
    dynamic = "dynamic"


@dataclass
class CurveData:
    """Multi-purpose data points for defining a curve.

    The use of this generic class is discouraged if a more specific
    class  can be used to specify the x and y axis values along with
    their specific data types.

    :ivar xvalue: The data value of the X-axis variable,  depending on
        the X-axis units.
    :ivar y1value: The data value of the  first Y-axis variable,
        depending on the Y-axis units.
    :ivar y2value: The data value of the second Y-axis variable (if
        present), depending on the Y-axis units.
    :ivar y3value: The data value of the third Y-axis variable (if
        present), depending on the Y-axis units.
    :ivar Curve: The curve of  this curve data point.
    """
    xvalue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y1value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y2value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y3value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Curve: Optional["Curve"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


class CurveStyle(Enum):
    """
    Style or shape of curve.

    :cvar constantYValue: The Y-axis values are assumed constant until
        the next curve point and prior to the first curve point.
    :cvar straightLineYValues: The Y-axis values are assumed to be a
        straight line between values.  Also known as linear
        interpolation.
    """
    constantYValue = "constantYValue"
    straightLineYValues = "straightLineYValues"


@dataclass
class DERFunction:
    connectDisconnect: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    frequencyWattCurveFunction: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maxRealPowerLimiting: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rampRateControl: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reactivePowerDispatch: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    realPowerDispatch: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltageRegulation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltVarCurveFunction: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltWattCurveFunction: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceGroup: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


class DERParameterKind(Enum):
    activePower = "activePower"
    apparentPower = "apparentPower"
    decreasingRampRate = "decreasingRampRate"
    highFilterBiDirectionalRegulation = "highFilterBiDirectionalRegulation"
    highFilterDownRegulation = "highFilterDownRegulation"
    highFilterUpRegulation = "highFilterUpRegulation"
    increasingRampRate = "increasingRampRate"
    lowFilterBiDirectionalRegulation = "lowFilterBiDirectionalRegulation"
    lowFilterDownRegulation = "lowFilterDownRegulation"
    lowFilterUpRegulation = "lowFilterUpRegulation"
    reactivePower = "reactivePower"
    voltage = "voltage"


class DERUnitSymbol(Enum):
    """
    The units defined for usage in the CIM.

    :cvar A: Current in Ampere.
    :cvar Ah: Ampere-hours, Ampere-hours.
    :cvar As: Ampere seconds (A·s).
    :cvar Btu: Energy, British Thermal Unit.
    :cvar Hz: Frequency in Hertz (1/s).
    :cvar Q: Quantity power, Q.
    :cvar Qh: Quantity energy, Qh.
    :cvar V: Electric potential in Volt (W/A).
    :cvar VA: Apparent power in Volt Ampere (See also real power and
        reactive power.)
    :cvar VAh: Apparent energy in Volt Ampere hours.
    :cvar VAr: Reactive power in Volt Ampere reactive. The “reactive” or
        “imaginary” component of electrical power (VIsin(phi)). (See
        also real power and apparent power). Note: Different meter
        designs use different methods to arrive at their results. Some
        meters may compute reactive power as an arithmetic value, while
        others compute the value vectorially. The data consumer should
        determine the method in use and the suitability of the
        measurement for the intended purpose.
    :cvar VArh: Reactive energy in Volt Ampere reactive hours.
    :cvar VPerVA: Power factor, PF, the ratio of the active power to the
        apparent power. Note: The sign convention used for power factor
        will differ between IEC meters and EEI (ANSI) meters. It is
        assumed that the data consumers understand the type of meter
        being used and agree on the sign convention in use at any given
        utility.
    :cvar VPerVAr: Power factor, PF, the ratio of the active power to
        the apparent power. Note: The sign convention used for power
        factor will differ between IEC meters and EEI (ANSI) meters. It
        is assumed that the data consumers understand the type of meter
        being used and agree on the sign convention in use at any given
        utility.
    :cvar Vh: Volt-hour, Volt hours.
    :cvar Vs: Volt second (Ws/A).
    :cvar W: Real power in Watt (J/s). Electrical power may have real
        and reactive components. The real portion of electrical power
        (I²R or VIcos(phi)), is expressed in Watts. (See also apparent
        power and reactive power.)
    :cvar WPerA: Active power per current flow, watt per Ampere.
    :cvar WPers: Ramp rate in Watt per second.
    :cvar Wh: Real energy in Watt hours.
    :cvar deg: Plane angle in degrees.
    :cvar degC: Relative temperature in degrees Celsius. In the SI unit
        system the symbol is ºC. Electric charge is measured in coulomb
        that has the unit symbol C. To distinguish degree Celsius form
        coulomb the symbol used in the UML is degC. Reason for not using
        ºC is the special character º is difficult to manage in
        software.
    :cvar h: Time, hour = 60 min = 3600 s.
    :cvar min: Time, minute  = 60 s.
    :cvar ohm: Electric resistance in ohm (V/A).
    :cvar ohmPerm: Electric resistance per length in ohm per metre
        ((V/A)/m).
    :cvar ohmm: resistivity, Ohm metre, (rho).
    :cvar onePerHz: Reciprocal of frequency (1/Hz).
    :cvar s: Time in seconds.
    :cvar therm: Energy, Therm.
    """
    A = "A"
    Ah = "Ah"
    As = "As"
    Btu = "Btu"
    Hz = "Hz"
    Q = "Q"
    Qh = "Qh"
    V = "V"
    VA = "VA"
    VAh = "VAh"
    VAr = "VAr"
    VArh = "VArh"
    VPerVA = "VPerVA"
    VPerVAr = "VPerVAr"
    Vh = "Vh"
    Vs = "Vs"
    W = "W"
    WPerA = "WPerA"
    WPers = "WPers"
    Wh = "Wh"
    deg = "deg"
    degC = "degC"
    h = "h"
    min = "min"
    ohm = "ohm"
    ohmPerm = "ohmPerm"
    ohmm = "ohmm"
    onePerHz = "onePerHz"
    s = "s"
    therm = "therm"


@dataclass
class DateTimeInterval:
    """
    Interval between two date and time points.

    :ivar end: End date and time of this interval.
    :ivar start: Start date and time of this interval.
    """
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DynamicsFunctionBlock:
    """
    Abstract parent class for all Dynamics function blocks.

    :ivar enabled: Function block used indicator. true = use of function
        block is enabled false = use of function block is disabled.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceAction:
    """
    Action/command performed by an end device on a device other than the end
    device.

    :ivar command: Command text.
    :ivar duration: Amount of time the action of this control is to
        remain active.
    :ivar durationIndefinite: True if the action of this control is
        indefinite.
    :ivar startDateTime: Start date and time for action of this control.
    :ivar EndDeviceControl: End device control issuing this end device
        action.
    """
    command: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    durationIndefinite: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    startDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceControl: Optional["EndDeviceControl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceCapability:
    """
    Inherent capabilities of an end device (i.e., the functions it supports).

    :ivar autonomousDst: True if autonomous DST (daylight saving time)
        function is supported.
    :ivar communication: True if communication function is supported.
    :ivar connectDisconnect: True if connect and disconnect function is
        supported.
    :ivar demandResponse: True if demand response function is supported.
    :ivar electricMetering: True if electric metering function is
        supported.
    :ivar gasMetering: True if gas metering function is supported.
    :ivar metrology: True if metrology function is supported.
    :ivar onRequestRead: True if on request read function is supported.
    :ivar outageHistory: True if outage history function is supported.
    :ivar pressureCompensation: True if device performs pressure
        compensation for metered quantities.
    :ivar pricingInfo: True if pricing information is supported.
    :ivar pulseOutput: True if device produces pulse outputs.
    :ivar relaysProgramming: True if relays programming function is
        supported.
    :ivar reverseFlow: True if reverse flow function is supported.
    :ivar superCompressibilityCompensation: True if device performs
        super compressibility compensation for metered quantities.
    :ivar temperatureCompensation: True if device performs temperature
        compensation for metered quantities.
    :ivar textMessage: True if the displaying of text messages is
        supported.
    :ivar waterMetering: True if water metering function is supported.
    """
    autonomousDst: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    communication: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    connectDisconnect: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    demandResponse: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    electricMetering: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    gasMetering: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    metrology: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    onRequestRead: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    outageHistory: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pressureCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pricingInfo: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pulseOutput: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    relaysProgramming: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reverseFlow: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    superCompressibilityCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    temperatureCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    textMessage: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    waterMetering: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class FaultImpedance:
    """
    Impedance description for the fault.

    :ivar rGround: The resistance of the fault between phases and
        ground.
    :ivar rLineToLine: The resistance of the fault between phases.
    :ivar xGround: The reactance of the fault between phases and ground.
    :ivar xLineToLine: The reactance of the fault between phases.
    """
    rGround: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rLineToLine: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    xGround: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    xLineToLine: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


class FlowDirectionKind(Enum):
    """
    Kind of flow direction for reading/measured  values proper to some
    commodities such as, for example, energy, power, demand.

    :cvar forward: "Delivered," or "Imported" as defined 61968-2.
        Forward Active Energy is a positive kWh value as one would
        naturally expect to find as energy is supplied by the utility
        and consumed at the service. Forward Reactive Energy is a
        positive VArh value as one would naturally expect to find in the
        presence of inductive loading. In polyphase metering, the
        forward energy register is incremented when the sum of the phase
        energies is greater than zero: &amp;lt;img src="HTS_1.PNG"
        width="209" height="16" border="0" alt="graphic"/&amp;gt;
    :cvar lagging: Typically used to describe that a power factor is
        lagging the reference value. Note 1: When used to describe VA,
        “lagging” describes a form of measurement where reactive power
        is considered in all four quadrants, but real power is
        considered only in quadrants I and IV. Note 2: When used to
        describe power factor, the term “Lagging” implies that the PF is
        negative. The term “lagging” in this case takes the place of the
        negative sign. If a signed PF value is to be passed by the data
        producer, then the direction of flow enumeration zero (none)
        should be used in order to avoid the possibility of creating an
        expression that employs a double negative. The data consumer
        should be able to tell from the sign of the data if the PF is
        leading or lagging. This principle is analogous to the concept
        that “Reverse” energy is an implied negative value, and to
        publish a negative reverse value would be ambiguous. Note 3:
        Lagging power factors typically indicate inductive loading.
    :cvar leading: Typically used to describe that a power factor is
        leading the reference value. Note: Leading power factors
        typically indicate capacitive loading.
    :cvar net: |Forward| - |Reverse|, See 61968-2. Note: In some
        systems, the value passed as a “net” value could become
        negative. In other systems the value passed as a “net” value is
        always a positive number, and rolls-over and rolls-under as
        needed.
    :cvar none: Not Applicable (N/A)
    :cvar q1minusQ4: Q1 minus Q4
    :cvar q1plusQ2: Reactive positive quadrants. (The term “lagging” is
        preferred.)
    :cvar q1plusQ3: Quadrants 1 and 3
    :cvar q1plusQ4: Quadrants 1 and 4 usually represent forward active
        energy
    :cvar q2minusQ3: Q2 minus Q3
    :cvar q2plusQ3: Quadrants 2 and 3 usually represent reverse active
        energy
    :cvar q2plusQ4: Quadrants 2 and 4
    :cvar q3minusQ2: Q3 minus Q2
    :cvar q3plusQ4: Reactive negative quadrants. (The term “leading” is
        preferred.)
    :cvar quadrant1: Q1 only
    :cvar quadrant2: Q2 only
    :cvar quadrant3: Q3 only
    :cvar quadrant4: Q4 only
    :cvar reverse: Reverse Active Energy is equivalent to "Received," or
        "Exported" as defined in 61968-2. Reverse Active Energy is a
        positive kWh value as one would expect to find when energy is
        backfed by the service onto the utility network. Reverse
        Reactive Energy is a positive VArh value as one would expect to
        find in the presence of capacitive loading and a leading Power
        Factor. In polyphase metering, the reverse energy register is
        incremented when the sum of the phase energies is less than
        zero: &amp;lt;img src="HTS_1.PNG" width="209" height="16"
        border="0" alt="graphic"/&amp;gt; Note: The value passed as a
        reverse value is always a positive value. It is understood by
        the label “reverse” that it represents negative flow.
    :cvar total: |Forward| + |Reverse|, See 61968-2. The sum of the
        commodity in all quadrants Q1+Q2+Q3+Q4. In polyphase metering,
        the total energy register is incremented when the absolute value
        of the sum of the phase energies is greater than zero:
        &amp;lt;img src="HTS_1.PNG" width="217" height="16" border="0"
        alt="graphic"/&amp;gt;
    :cvar totalByPhase: In polyphase metering, the total by phase energy
        register is incremented when the sum of the absolute values of
        the phase energies is greater than zero: &amp;lt;img
        src="HTS_1.PNG" width="234" height="16" border="0"
        alt="graphic"/&amp;gt; In single phase metering, the formulas
        for “Total” and “Total by phase” collapse to the same
        expression. For communication purposes however, the “Total”
        enumeration should be used with single phase meter data.
    """
    forward = "forward"
    lagging = "lagging"
    leading = "leading"
    net = "net"
    none = "none"
    q1minusQ4 = "q1minusQ4"
    q1plusQ2 = "q1plusQ2"
    q1plusQ3 = "q1plusQ3"
    q1plusQ4 = "q1plusQ4"
    q2minusQ3 = "q2minusQ3"
    q2plusQ3 = "q2plusQ3"
    q2plusQ4 = "q2plusQ4"
    q3minusQ2 = "q3minusQ2"
    q3plusQ4 = "q3plusQ4"
    quadrant1 = "quadrant1"
    quadrant2 = "quadrant2"
    quadrant3 = "quadrant3"
    quadrant4 = "quadrant4"
    reverse = "reverse"
    total = "total"
    totalByPhase = "totalByPhase"


class HouseCooling(Enum):
    electric = "electric"
    heatPump = "heatPump"
    none = "none"


class HouseHeating(Enum):
    gas = "gas"
    heatPump = "heatPump"
    none = "none"
    resistance = "resistance"


class IEEE1547AbnormalPerfomanceCategory(Enum):
    CategoryI = "CategoryI"
    CategoryII = "CategoryII"
    CategoryIII = "CategoryIII"


@dataclass
class IEEE1547ControlSettings:
    constantPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    constantReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceIntentionalDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceMaxFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceMaxVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceMinFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceMinVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    frequencyDroopResponseTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    openLoopResponseTimeP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    overFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    overFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    timeConstantOpenLoop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    timeConstantReferenceVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    underFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    underFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltVarQ1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltVarQ2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltVarQ3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltVarQ4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltVarV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltVarV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltVarV3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltVarV4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltWattP1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltWattP2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltWattV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltWattV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wattVarP1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wattVarP2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wattVarP3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wattVarP4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wattVarQ1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wattVarQ2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wattVarQ3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wattVarQ4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerElectronicsConnections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RotatingMachines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


class IEEE1547IslandingCategory(Enum):
    """
    See clause 8.2.
    """
    BlackStart = "BlackStart"
    Capable = "Capable"
    Isochronous = "Isochronous"
    Uncategorized = "Uncategorized"


class IEEE1547NormalPerformanceCategory(Enum):
    CategoryA = "CategoryA"
    CategoryB = "CategoryB"


@dataclass
class IEEE1547TripSettings:
    OF1frequency: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OF1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OF2frequency: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OF2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OV1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OV1voltage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OV2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OV2voltage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UF1frequency: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UF1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UF2frequency: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UF2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UV1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UV1voltage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UV2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UV2voltage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerElectronicsConnections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RotatingMachines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Name:
    """The Name class provides the means to define any number of human readable
    names for an object.

    A name is &lt;b&gt;not&lt;/b&gt; to be used for defining inter-
    object relationships. For inter-object relationships instead use the
    object identification 'mRID'.

    :ivar name: Any free text that name the object.
    :ivar IdentifiedObject: Identified object that this name designates.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IdentifiedObject: Optional["IdentifiedObject"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


class NormalOPcatKind(Enum):
    """Kinds of normal operation categories.

    Reference: IEEE1547-2018.

    :cvar catA: Category CAT_A.
    :cvar catB: Category CAT_B.
    """
    catA = "catA"
    catB = "catB"


class OperationalLimitDirectionKind(Enum):
    """
    The direction attribute describes the side of  a limit that is a violation.

    :cvar absoluteValue: An absoluteValue limit means that a monitored
        absolute value above the limit value is a violation.
    :cvar high: High means that a monitored value above the limit value
        is a violation.   If applied to a terminal flow, the positive
        direction is into the terminal.
    :cvar low: Low means a monitored value below the limit is a
        violation.  If applied to a terminal flow, the positive
        direction is into the terminal.
    """
    absoluteValue = "absoluteValue"
    high = "high"
    low = "low"


class OrderedPhaseCodeKind(Enum):
    """In some use cases, the ordering of phases is important.

    The PhaseCode class does not represent order, but this class
    addresses such use cases. When two or more phases are present, the
    individual phases may occur in any order, but the neutral must
    always occur last. When only one phase and the neutral is present,
    that phase and the neutral may be re-ordered.
    """
    A = "A"
    AB = "AB"
    ABC = "ABC"
    ABCN = "ABCN"
    ABN = "ABN"
    AC = "AC"
    ACB = "ACB"
    ACBN = "ACBN"
    ACN = "ACN"
    AN = "AN"
    B = "B"
    BA = "BA"
    BAC = "BAC"
    BACN = "BACN"
    BAN = "BAN"
    BC = "BC"
    BCA = "BCA"
    BCAN = "BCAN"
    BCN = "BCN"
    BN = "BN"
    C = "C"
    CA = "CA"
    CAB = "CAB"
    CABN = "CABN"
    CAN = "CAN"
    CB = "CB"
    CBA = "CBA"
    CBAN = "CBAN"
    CBN = "CBN"
    CN = "CN"
    NA = "NA"
    NB = "NB"
    NC = "NC"
    Ns1 = "Ns1"
    Ns2 = "Ns2"
    X = "X"
    XN = "XN"
    XY = "XY"
    XYN = "XYN"
    none = "none"
    s1 = "s1"
    s12 = "s12"
    s12N = "s12N"
    s1N = "s1N"
    s2 = "s2"
    s21 = "s21"
    s21N = "s21N"
    s2N = "s2N"


class PhaseCode(Enum):
    """An unordered enumeration of phase identifiers.

    Allows designation of phases for both transmission and distribution
    equipment, circuits and loads.   The enumeration, by itself, does
    not describe how the phases are connected together or connected to
    ground.  Ground is not explicitly denoted as a phase. Residential
    and small commercial loads are often served from single-phase, or
    split-phase, secondary circuits. For example of s12N, phases 1 and 2
    refer to hot wires that are 180 degrees out of phase, while N refers
    to the neutral wire. Through single-phase transformer connections,
    these secondary circuits may be served from one or two of the
    primary phases A, B, and C. For three-phase loads, use the A, B, C
    phase codes instead of s12N.

    :cvar A: Phase A.
    :cvar AB: Phases A and B.
    :cvar ABC: Phases A, B, and C.
    :cvar ABCN: Phases A, B, C, and N.
    :cvar ABN: Phases A, B, and neutral.
    :cvar AC: Phases A and C.
    :cvar ACN: Phases A, C and neutral.
    :cvar AN: Phases A and neutral.
    :cvar B: Phase B.
    :cvar BC: Phases B and C.
    :cvar BCN: Phases B, C, and neutral.
    :cvar BN: Phases B and neutral.
    :cvar C: Phase C.
    :cvar CN: Phases C and neutral.
    :cvar N: Neutral phase.
    :cvar X: Unknown non-neutral phase.
    :cvar XN: Unknown non-neutral phase plus neutral.
    :cvar XY: Two unknown non-neutral phases.
    :cvar XYN: Two unknown non-neutral phases plus neutral.
    :cvar none: No phases specified.
    :cvar s1: Secondary phase 1.
    :cvar s12: Secondary phase 1 and 2.
    :cvar s12N: Secondary phases 1, 2, and neutral.
    :cvar s1N: Secondary phase 1 and neutral.
    :cvar s2: Secondary phase 2.
    :cvar s2N: Secondary phase 2 and neutral.
    """
    A = "A"
    AB = "AB"
    ABC = "ABC"
    ABCN = "ABCN"
    ABN = "ABN"
    AC = "AC"
    ACN = "ACN"
    AN = "AN"
    B = "B"
    BC = "BC"
    BCN = "BCN"
    BN = "BN"
    C = "C"
    CN = "CN"
    N = "N"
    X = "X"
    XN = "XN"
    XY = "XY"
    XYN = "XYN"
    none = "none"
    s1 = "s1"
    s12 = "s12"
    s12N = "s12N"
    s1N = "s1N"
    s2 = "s2"
    s2N = "s2N"


class PhaseConnectedFaultKind(Enum):
    """
    The type of fault connection among phases.

    :cvar lineOpen: The fault is when the conductor path is broken
        between two terminals. Additional coexisting faults may be
        required if the broken conductor also causes connections to
        grounds or other lines or phases.
    :cvar lineToGround: The fault connects the indicated phases to
        ground. The line to line fault impedance is not used and assumed
        infinite. The full ground impedance is connected between each
        phase specified in the fault and ground, but not between the
        phases.
    :cvar lineToLine: The fault connects the specified phases together
        without a connection to ground. The ground impedance of this
        fault is ignored. The line to line impedance is connected
        between each of the phases specified in the fault. For example
        three times for a three phase fault, one time for a two phase
        fault.  A single phase fault should not be specified.
    :cvar lineToLineToGround: The fault connects the indicated phases to
        ground and to each other. The line to line impedance is
        connected between each of the phases specified in the fault in a
        full mesh. For example three times for a three phase fault, one
        time for a two phase fault. A single phase fault should not be
        specified. The full ground impedance is connected between each
        phase specified in the fault and ground.
    """
    lineOpen = "lineOpen"
    lineToGround = "lineToGround"
    lineToLine = "lineToLine"
    lineToLineToGround = "lineToLineToGround"


class PhaseShuntConnectionKind(Enum):
    """
    The configuration of phase connections for a single terminal device such as
    a load or capacitor.

    :cvar D: Delta connection.
    :cvar G: Ground connection; use when explicit connection to ground
        needs to be expressed in combination with the phase code, such
        as for electrical wire/cable or for meters.
    :cvar I: Independent winding, for single-phase connections.
    :cvar Y: Wye connection.
    :cvar Yn: Wye, with neutral brought out for grounding.
    """
    D = "D"
    G = "G"
    I = "I"
    Y = "Y"
    Yn = "Yn"


@dataclass
class Priority:
    """
    Priority definition.

    :ivar justification: Justification for 'rank'.
    :ivar rank: Priority level; usually, lower number means high
        priority, but the details are provided in 'type'.
    :ivar type: Type describing 'rank'; e.g., high, emergency, etc.
    """
    justification: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rank: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


class RandomisationKind(Enum):
    """Kind of randomisation to be applied to control the timing of end device
    control commands and/or the definition of demand response and load control
    events.

    Value other than 'none' is typically used to mitigate potential
    deleterious effects of simultaneous operation of multiple devices.

    :cvar default: Randomisation of start and/or end times involving the
        operation of one or more devices is controlled by default
        settings for the device(s).
    :cvar end: End time of an event or control action affecting one or
        more devices is randomised to prevent simultaneous operation.
    :cvar none: Neither the start time nor the end time of an event or
        control action affecting one or more devices is randomised.
    :cvar start: Start time of an event or control action affecting one
        or more multiple devices is randomised.
    :cvar startAndEnd: Both the start time and the end time of an event
        or control action affecting one or more devices are randomised
        to prevent simultaneous operation.
    """
    default = "default"
    end = "end"
    none = "none"
    start = "start"
    startAndEnd = "startAndEnd"


@dataclass
class RegularTimePoint:
    """
    Time point for a schedule where the time between the consecutive points is
    constant.

    :ivar sequenceNumber: The position of the regular time point in the
        sequence. Note that time points don't have to be sequential,
        i.e. time points may be omitted. The actual time for a
        RegularTimePoint is computed by multiplying the associated
        regular interval schedule's time step with the regular time
        point sequence number and adding the associated schedules start
        time.
    :ivar value1: The first value at the time. The meaning of the value
        is defined by the derived type of the associated schedule.
    :ivar value2: The second value at the time. The meaning of the value
        is defined by the derived type of the associated schedule.
    :ivar IntervalSchedule: Regular interval schedule containing this
        time point.
    """
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IntervalSchedule: Optional["RegularIntervalSchedule"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


class RegulatingControlModeKind(Enum):
    """The kind of regulation model.

    For example regulating voltage, reactive power, active power, etc.

    :cvar activePower: Active power is specified.
    :cvar admittance: Admittance is specified.
    :cvar currentFlow: Current flow is specified.
    :cvar powerFactor: Power factor is specified.
    :cvar reactivePower: Reactive power is specified.
    :cvar temperature: Control switches on/off based on the local
        temperature (i.e., a thermostat).
    :cvar timeScheduled: Control switches on/off by time of day. The
        times may change on the weekend, or in different seasons.
    :cvar voltage: Voltage is specified.
    """
    activePower = "activePower"
    admittance = "admittance"
    currentFlow = "currentFlow"
    powerFactor = "powerFactor"
    reactivePower = "reactivePower"
    temperature = "temperature"
    timeScheduled = "timeScheduled"
    voltage = "voltage"


class RemoteSignalKind(Enum):
    """
    Type of input signal coming from remote bus.

    :cvar remoteBranchCurrentAmplitude: Input is branch current
        amplitude from remote terminal bus.
    :cvar remoteBusFrequency: Input is frequency from remote terminal
        bus.
    :cvar remoteBusFrequencyDeviation: Input is frequency deviation from
        remote terminal bus.
    :cvar remoteBusVoltage: Input is voltage from remote terminal bus.
    :cvar remoteBusVoltageAmplitude: Input is voltage amplitude from
        remote terminal bus.
    :cvar remoteBusVoltageAmplitudeDerivative: Input is branch current
        amplitude derivative from remote terminal bus.
    :cvar remoteBusVoltageFrequency: Input is voltage frequency from
        remote terminal bus.
    :cvar remoteBusVoltageFrequencyDeviation: Input is voltage frequency
        deviation from remote terminal bus.
    :cvar remotePuBusVoltageDerivative: Input is PU voltage derivative
        from remote terminal bus.
    """
    remoteBranchCurrentAmplitude = "remoteBranchCurrentAmplitude"
    remoteBusFrequency = "remoteBusFrequency"
    remoteBusFrequencyDeviation = "remoteBusFrequencyDeviation"
    remoteBusVoltage = "remoteBusVoltage"
    remoteBusVoltageAmplitude = "remoteBusVoltageAmplitude"
    remoteBusVoltageAmplitudeDerivative = "remoteBusVoltageAmplitudeDerivative"
    remoteBusVoltageFrequency = "remoteBusVoltageFrequency"
    remoteBusVoltageFrequencyDeviation = "remoteBusVoltageFrequencyDeviation"
    remotePuBusVoltageDerivative = "remotePuBusVoltageDerivative"


class SinglePhaseKind(Enum):
    """Enumeration of single phase identifiers.

    Allows designation of single phases for both transmission and
    distribution equipment, circuits and loads.

    :cvar A: Phase A.
    :cvar B: Phase B.
    :cvar C: Phase C.
    :cvar N: Neutral.
    :cvar s1: Secondary phase 1.
    :cvar s2: Secondary phase 2.
    """
    A = "A"
    B = "B"
    C = "C"
    N = "N"
    s1 = "s1"
    s2 = "s2"


@dataclass
class StateVariable:
    """
    An abstract class for state variables.
    """


@dataclass
class Status:
    """
    Current status information relevant to an entity.

    :ivar dateTime: Date and time for which status 'value' applies.
    :ivar reason: Reason code or explanation for why an object went to
        the current status 'value'.
    :ivar remark: Pertinent information regarding the current 'value',
        as free form text.
    :ivar value: Status value at 'dateTime'; prior status changes may
        have been kept in instances of activity records associated with
        the object to which this status applies.
    """
    dateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


class ThermostatControlMode(Enum):
    Cooling = "Cooling"
    Heating = "Heating"


class TimeIntervalKind(Enum):
    D = "D"
    M = "M"
    Y = "Y"
    h = "h"
    m_1 = "m"
    s = "s"


class UnitMultiplier(Enum):
    """The unit multipliers defined for the CIM.

    When applied to unit symbols, the unit symbol is treated as a
    derived unit. Regardless of the contents of the unit symbol text,
    the unit symbol shall be treated as if it were a single-character
    unit symbol. Unit symbols should not contain multipliers, and it
    should be left to the multiplier to define the multiple for an
    entire data type. For example, if a unit symbol is "A2Perh" and the
    multiplier is "k", then the value is k(A^2/h), and the multiplier
    applies to the entire final value, not to any individual part of the
    value. This can be conceptualized by substituting a derived unit
    symbol for the unit type. If one imagines that the symbol "Þ"
    represents the derived unit "A2Perh", then applying the multiplier
    "k" can be conceptualized simply as "kÞ". For example, the SI unit
    for mass is "kg" and not "g".  If the unit symbol is defined as
    "kg", then the multiplier is applied to "kg" as a whole and does not
    replace the "k" in front of the "g". In this case, the multiplier of
    "m" would be used with the unit symbol of "kg" to represent one
    gram.  As a text string, this violates the instructions in IEC
    80000-1. However, because the unit symbol in CIM is treated as a
    derived unit instead of as an SI unit, it makes more sense to
    conceptualize the "kg" as if it were replaced by one of the proposed
    replacements for the SI mass symbol. If one imagines that the "kg"
    were replaced by a symbol "Þ", then it is easier to conceptualize
    the multiplier "m" as creating the proper unit "mÞ", and not the
    forbidden unit "mkg".

    :cvar E: Exa 10**18.
    :cvar G: Giga 10**9.
    :cvar M: Mega 10**6.
    :cvar P: Peta 10**15
    :cvar T: Tera 10**12.
    :cvar Y: Yotta 10**24
    :cvar Z: Zetta 10**21
    :cvar a: atto 10**-18.
    :cvar c: Centi 10**-2.
    :cvar d: Deci 10**-1.
    :cvar da: deca 10**1.
    :cvar f: femto 10**-15.
    :cvar h: hecto 10**2.
    :cvar k: Kilo 10**3.
    :cvar m_1: Milli 10**-3.
    :cvar micro: Micro 10**-6.
    :cvar n: Nano 10**-9.
    :cvar none: No multiplier or equivalently multiply by 1.
    :cvar p_1: Pico 10**-12.
    :cvar y_1: yocto 10**-24.
    :cvar z_1: zepto 10**-21.
    """
    E = "E"
    G = "G"
    M = "M"
    P = "P"
    T = "T"
    Y = "Y"
    Z = "Z"
    a = "a"
    c = "c"
    d = "d"
    da = "da"
    f = "f"
    h = "h"
    k = "k"
    m_1 = "m"
    micro = "micro"
    n = "n"
    none = "none"
    p_1 = "p"
    y_1 = "y"
    z_1 = "z"


class UnitSymbol(Enum):
    """The derived units defined for usage in the CIM.

    In some cases, the derived unit is equal to an SI unit. Whenever
    possible, the standard derived symbol is used instead of the formula
    for the derived unit. For example, the unit symbol Farad is defined
    as "F" instead of "CPerV". In cases where a standard symbol does not
    exist for a derived unit, the formula for the unit is used as the
    unit symbol. For example, density does not have a standard symbol
    and so it is represented as "kgPerm3". With the exception of the
    "kg", which is an SI unit, the unit symbols do not contain
    multipliers and therefore represent the base derived unit to which a
    multiplier can be applied as a whole. Every unit symbol is treated
    as an unparseable text as if it were a single-letter symbol. The
    meaning of each unit symbol is defined by the accompanying
    descriptive text and not by the text contents of the unit symbol. To
    allow the widest possible range of serializations without requiring
    special character handling, several substitutions are made which
    deviate from the format described in IEC 80000-1. The division
    symbol "/" is replaced by the letters"Per". Exponents are written in
    plain text after the unit as "m3" instead of being formatted as in
    "m&lt;sup&gt;3&lt;/sup&gt;" or introducing a symbol as in "m^3". The
    degree symbol "°" is replaced with the letters "deg". Any
    clarification of the meaning for a substitution is included in the
    description for the unit symbol. Non-SI units are included in list
    of unit symbols to allow sources of data to be correctly labeled
    with their non-SI units (for example, a GPS sensor that is reporting
    numbers that represent feet instead of meters). This allows software
    to use the unit symbol information correctly convert and scale the
    raw data of those sources into SI-based units.

    :cvar A: Current in Ampere.
    :cvar A2: Ampere squared (A²).
    :cvar A2h: ampere-squared hour, Ampere-squared hour.
    :cvar A2s: Ampere squared time in square ampere (A²s).
    :cvar APerA: Current, Ratio of Amperages  Note: Users may need to
        supply a prefix such as ‘m’ to show rates such as ‘mA/A’.
    :cvar APerm: A/m, magnetic field strength, Ampere per metre.
    :cvar Ah: Ampere-hours, Ampere-hours.
    :cvar As: Ampere seconds (A·s).
    :cvar Bq: Radioactivity in Becquerel (1/s).
    :cvar Btu: Energy, British Thermal Unit.
    :cvar C: Electric charge in Coulomb (A·s).
    :cvar CPerkg: exposure (x rays), Coulomb per kilogram.
    :cvar CPerm2: surface charge density, Coulomb per square metre.
    :cvar CPerm3: electric charge density, Coulomb per cubic metre.
    :cvar F: Electric capacitance in Farad (C/V).
    :cvar FPerm: permittivity, Farad per metre.
    :cvar G: Magnetic flux density, Gauss (1 G = 10-4 T).
    :cvar Gy: Absorbed dose in Gray (J/kg).
    :cvar GyPers: absorbed dose rate, Gray per second.
    :cvar H: Electric inductance in Henry (Wb/A).
    :cvar HPerm: permeability, Henry per metre.
    :cvar Hz: Frequency in Hertz (1/s).
    :cvar HzPerHz: Frequency, Rate of frequency change  Note: Users may
        need to supply a prefix such as ‘m’ to show rates such as
        ‘mHz/Hz’.
    :cvar HzPers: Rate of change of frequency in Hertz per second.
    :cvar J: Energy in joule (N·m = C·V = W·s).
    :cvar JPerK: Heat capacity in Joule/Kelvin.
    :cvar JPerkg: Specific energy, Joule / kg.
    :cvar JPerkgK: Specific heat capacity, specific entropy, Joule per
        kilogram Kelvin.
    :cvar JPerm2: Insulation energy density, Joule per square metre or
        watt second per square metre.
    :cvar JPerm3: energy density, Joule per cubic metre.
    :cvar JPermol: molar energy, Joule per mole.
    :cvar JPermolK: molar entropy, molar heat capacity, Joule per mole
        kelvin.
    :cvar JPers: Energy rate joule per second (J/s),
    :cvar K: Temperature in Kelvin.
    :cvar KPers: Temperature change rate in Kelvin per second.
    :cvar M: Length, nautical mile (1 M = 1852 m).
    :cvar Mx: Magnetic flux, Maxwell (1 Mx = 10-8 Wb).
    :cvar N: Force in Newton (kg·m/s²).
    :cvar NPerm: Surface tension, Newton per metre.
    :cvar Nm: Moment of force, Newton metre.
    :cvar Oe: Magnetic field, Œrsted (1 Oe = (103/4p) A/m).
    :cvar Pa: Pressure in Pascal (N/m²). Note: the absolute or relative
        measurement of pressure is implied with this entry. See below
        for more explicit forms.
    :cvar PaPers: Pressure change rate in Pascal per second.
    :cvar Pas: Dynamic viscosity, Pascal second.
    :cvar Q: Quantity power, Q.
    :cvar Qh: Quantity energy, Qh.
    :cvar S: Conductance in Siemens.
    :cvar SPerm: Conductance per length (F/m).
    :cvar Sv: Dose equivalent in Sievert (J/kg).
    :cvar T: Magnetic flux density in Tesla (Wb/m2).
    :cvar V: Electric potential in Volt (W/A).
    :cvar V2: Volt squared (W²/A²).
    :cvar V2h: volt-squared hour, Volt-squared-hours.
    :cvar VA: Apparent power in Volt Ampere (See also real power and
        reactive power.)
    :cvar VAh: Apparent energy in Volt Ampere hours.
    :cvar VAr: Reactive power in Volt Ampere reactive. The “reactive” or
        “imaginary” component of electrical power (VIsin(phi)). (See
        also real power and apparent power). Note: Different meter
        designs use different methods to arrive at their results. Some
        meters may compute reactive power as an arithmetic value, while
        others compute the value vectorially. The data consumer should
        determine the method in use and the suitability of the
        measurement for the intended purpose.
    :cvar VArh: Reactive energy in Volt Ampere reactive hours.
    :cvar VPerHz: Magnetic flux in Volt per Hertz.
    :cvar VPerV: Voltage, Ratio of voltages Note: Users may need to
        supply a prefix such as ‘m’ to show rates such as ‘mV/V’.
    :cvar VPerVA: Power factor, PF, the ratio of the active power to the
        apparent power. Note: The sign convention used for power factor
        will differ between IEC meters and EEI (ANSI) meters. It is
        assumed that the data consumers understand the type of meter
        being used and agree on the sign convention in use at any given
        utility.
    :cvar VPerVAr: Power factor, PF, the ratio of the active power to
        the apparent power. Note: The sign convention used for power
        factor will differ between IEC meters and EEI (ANSI) meters. It
        is assumed that the data consumers understand the type of meter
        being used and agree on the sign convention in use at any given
        utility.
    :cvar VPerm: electric field strength, Volt per metre.
    :cvar Vh: Volt-hour, Volt hours.
    :cvar Vs: Volt second (Ws/A).
    :cvar W: Real power in Watt (J/s). Electrical power may have real
        and reactive components. The real portion of electrical power
        (I²R or VIcos(phi)), is expressed in Watts. (See also apparent
        power and reactive power.)
    :cvar WPerA: Active power per current flow, watt per Ampere.
    :cvar WPerW: Signal Strength, Ratio of power  Note: Users may need
        to supply a prefix such as ‘m’ to show rates such as ‘mW/W’.
    :cvar WPerm2: Heat flux density, irradiance, Watt per square metre.
    :cvar WPerm2sr: radiance, Watt per square metre steradian.
    :cvar WPermK: Thermal conductivity in Watt/metre Kelvin.
    :cvar WPers: Ramp rate in Watt per second.
    :cvar WPersr: Radiant intensity, Watt per steradian.
    :cvar Wb: Magnetic flux in Weber (V·s).
    :cvar Wh: Real energy in Watt hours.
    :cvar anglemin: Plane angle, minute.
    :cvar anglesec: Plane angle, second.
    :cvar bar: Pressure, bar (1 bar = 100 kPa).
    :cvar cd: Luminous intensity in candela.
    :cvar charPers: Data rate (baud) in characters per second.
    :cvar character: Number of characters.
    :cvar cosPhi: Power factor, dimensionless. Note 1: This definition
        of power factor only holds for balanced systems. See the
        alternative definition under code 153. Note 2 : Beware of
        differing sign conventions in use between the IEC and EEI. It is
        assumed that the data consumer understands the type of meter in
        use and the sign convention in use by the utility.
    :cvar count: Amount of substance, Counter value.
    :cvar d: Time, day = 24 h = 86400 s.
    :cvar dB: Sound pressure level in decibel. Note:  multiplier “d” is
        included in this unit symbol for compatibility with IEC
        61850-7-3.
    :cvar dBm: Power level (logrithmic ratio of signal strength , Bel-
        mW), normalized to 1mW. Note:  multiplier “d” is included in
        this unit symbol for compatibility with IEC 61850-7-3.
    :cvar deg: Plane angle in degrees.
    :cvar degC: Relative temperature in degrees Celsius. In the SI unit
        system the symbol is ºC. Electric charge is measured in coulomb
        that has the unit symbol C. To distinguish degree Celsius form
        coulomb the symbol used in the UML is degC. Reason for not using
        ºC is the special character º is difficult to manage in
        software.
    :cvar ft3: Volume, cubic foot.
    :cvar gPerg: Concentration, The ratio of the mass of a solute
        divided by the mass of  the solution. Note: Users may need use a
        prefix such a ‘µ’ to express a quantity such as ‘µg/g’.
    :cvar gal: Volume, US gallon (1 gal = 231 in3 = 128 fl ounce).
    :cvar h_1: Time, hour = 60 min = 3600 s.
    :cvar ha: Area, hectare.
    :cvar kat: Catalytic activity, katal = mol / s.
    :cvar katPerm3: catalytic activity concentration, katal per cubic
        metre.
    :cvar kg: Mass in kilogram.  Note: multiplier “k” is included in
        this unit symbol for compatibility with IEC 61850-7-3.
    :cvar kgPerJ: Weigh per energy in kilogram/joule (kg/J). Note:
        multiplier “k” is included in this unit symbol for compatibility
        with IEC 61850-7-3.
    :cvar kgPerm3: Density in kilogram/cubic metre (kg/m³). Note:
        multiplier “k” is included in this unit symbol for compatibility
        with IEC 61850-7-3.
    :cvar kgm: Moment of mass in kilogram metre (kg·m) (first moment of
        mass). Note: multiplier “k” is included in this unit symbol for
        compatibility with IEC 61850-7-3.
    :cvar kgm2: Moment of mass in kilogram square metre (kg·m²) (Second
        moment of mass, commonly called the moment of inertia). Note:
        multiplier “k” is included in this unit symbol for compatibility
        with IEC 61850-7-3.
    :cvar kn: Speed, knot (1 kn = 1852/3600) m/s.
    :cvar l: Volume, litre = dm3 = m3/1000.
    :cvar lPerh: Volumetric flow rate, litre per hour.
    :cvar lPerl: Concentration, The ratio of the volume of a solute
        divided by the volume of  the solution. Note: Users may need use
        a prefix such a ‘µ’ to express a quantity such as ‘µL/L’.
    :cvar lPers: Volumetric flow rate in litre per second.
    :cvar lm: Luminous flux in lumen (cd·sr).
    :cvar lx: Illuminance in lux (lm/m²).
    :cvar m_1: Length in meter.
    :cvar m2: Area in square metre (m²).
    :cvar m2Pers: Viscosity in metre square / second (m²/s).
    :cvar m3: Volume in cubic metre (m³).
    :cvar m3Compensated: Volume, cubic metre, with the value compensated
        for weather effects.
    :cvar m3Perh: Volumetric flow rate, cubic metre per hour.
    :cvar m3Perkg: Specific volume, cubic metre per kilogram, v.
    :cvar m3Pers: Volumetric flow rate in cubic metres per second
        (m³/s).
    :cvar m3Uncompensated: Volume, cubic metre, with the value
        uncompensated for weather effects.
    :cvar mPerm3: Fuel efficiency in metre per cubic metre (m/m³).
    :cvar mPers: Velocity in metre per second (m/s).
    :cvar mPers2: Acceleration in metre per second squared (m/s²).
    :cvar min: Time, minute  = 60 s.
    :cvar mmHg: Pressure, millimeter of mercury (1 mmHg is approximately
        133.3 Pa).
    :cvar mol: Amount of substance in mole.
    :cvar molPerkg: Concentration, Molality, the amount of solute in
        moles and the amount of solvent in kilograms.
    :cvar molPerm3: Concentration, The amount of substance
        concentration, (c), the amount of solvent in moles divided by
        the volume of solution in m³.
    :cvar molPermol: Concentration, Molar fraction (?), the ratio of the
        molar amount of a solute divided by the molar amount of the
        solution.
    :cvar none: Dimension less quantity, e.g. count, per unit, etc.
    :cvar ohm: Electric resistance in ohm (V/A).
    :cvar ohmPerm: Electric resistance per length in ohm per metre
        ((V/A)/m).
    :cvar ohmm: resistivity, Ohm metre, (rho).
    :cvar onePerHz: Reciprocal of frequency (1/Hz).
    :cvar onePerm: Wavenumber, reciprocal metre,  (1/m).
    :cvar ppm: Concentration in parts per million.
    :cvar rad: Plane angle in radian (m/m).
    :cvar radPers: Angular velocity in radians per second (rad/s).
    :cvar radPers2: Angular acceleration, radian per second squared.
    :cvar rev: Amount of rotation, Revolutions.
    :cvar rotPers: Rotations per second (1/s). See also Hz (1/s).
    :cvar s_1: Time in seconds.
    :cvar sPers: Time, Ratio of time Note: Users may need to supply a
        prefix such as ‘µ’ to show rates such as ‘µs/s’
    :cvar sr: Solid angle in steradian (m2/m2).
    :cvar therm: Energy, Therm.
    :cvar tonne: mass, “tonne” or “metric  ton” (1000 kg = 1 Mg).
    """
    A = "A"
    A2 = "A2"
    A2h = "A2h"
    A2s = "A2s"
    APerA = "APerA"
    APerm = "APerm"
    Ah = "Ah"
    As = "As"
    Bq = "Bq"
    Btu = "Btu"
    C = "C"
    CPerkg = "CPerkg"
    CPerm2 = "CPerm2"
    CPerm3 = "CPerm3"
    F = "F"
    FPerm = "FPerm"
    G = "G"
    Gy = "Gy"
    GyPers = "GyPers"
    H = "H"
    HPerm = "HPerm"
    Hz = "Hz"
    HzPerHz = "HzPerHz"
    HzPers = "HzPers"
    J = "J"
    JPerK = "JPerK"
    JPerkg = "JPerkg"
    JPerkgK = "JPerkgK"
    JPerm2 = "JPerm2"
    JPerm3 = "JPerm3"
    JPermol = "JPermol"
    JPermolK = "JPermolK"
    JPers = "JPers"
    K = "K"
    KPers = "KPers"
    M = "M"
    Mx = "Mx"
    N = "N"
    NPerm = "NPerm"
    Nm = "Nm"
    Oe = "Oe"
    Pa = "Pa"
    PaPers = "PaPers"
    Pas = "Pas"
    Q = "Q"
    Qh = "Qh"
    S = "S"
    SPerm = "SPerm"
    Sv = "Sv"
    T = "T"
    V = "V"
    V2 = "V2"
    V2h = "V2h"
    VA = "VA"
    VAh = "VAh"
    VAr = "VAr"
    VArh = "VArh"
    VPerHz = "VPerHz"
    VPerV = "VPerV"
    VPerVA = "VPerVA"
    VPerVAr = "VPerVAr"
    VPerm = "VPerm"
    Vh = "Vh"
    Vs = "Vs"
    W = "W"
    WPerA = "WPerA"
    WPerW = "WPerW"
    WPerm2 = "WPerm2"
    WPerm2sr = "WPerm2sr"
    WPermK = "WPermK"
    WPers = "WPers"
    WPersr = "WPersr"
    Wb = "Wb"
    Wh = "Wh"
    anglemin = "anglemin"
    anglesec = "anglesec"
    bar = "bar"
    cd = "cd"
    charPers = "charPers"
    character = "character"
    cosPhi = "cosPhi"
    count = "count"
    d = "d"
    dB = "dB"
    dBm = "dBm"
    deg = "deg"
    degC = "degC"
    ft3 = "ft3"
    gPerg = "gPerg"
    gal = "gal"
    h_1 = "h"
    ha = "ha"
    kat = "kat"
    katPerm3 = "katPerm3"
    kg = "kg"
    kgPerJ = "kgPerJ"
    kgPerm3 = "kgPerm3"
    kgm = "kgm"
    kgm2 = "kgm2"
    kn = "kn"
    l = "l"
    lPerh = "lPerh"
    lPerl = "lPerl"
    lPers = "lPers"
    lm = "lm"
    lx = "lx"
    m_1 = "m"
    m2 = "m2"
    m2Pers = "m2Pers"
    m3 = "m3"
    m3Compensated = "m3Compensated"
    m3Perh = "m3Perh"
    m3Perkg = "m3Perkg"
    m3Pers = "m3Pers"
    m3Uncompensated = "m3Uncompensated"
    mPerm3 = "mPerm3"
    mPers = "mPers"
    mPers2 = "mPers2"
    min = "min"
    mmHg = "mmHg"
    mol = "mol"
    molPerkg = "molPerkg"
    molPerm3 = "molPerm3"
    molPermol = "molPermol"
    none = "none"
    ohm = "ohm"
    ohmPerm = "ohmPerm"
    ohmm = "ohmm"
    onePerHz = "onePerHz"
    onePerm = "onePerm"
    ppm = "ppm"
    rad = "rad"
    radPers = "radPers"
    radPers2 = "radPers2"
    rev = "rev"
    rotPers = "rotPers"
    s_1 = "s"
    sPers = "sPers"
    sr = "sr"
    therm = "therm"
    tonne = "tonne"


class UsagePointConnectedKind(Enum):
    """
    State of the usage point with respect to connection to the network.

    :cvar connected: The usage point is connected to the network and
        able to receive or send the applicable commodity (electricity,
        gas, water, etc.).
    :cvar logicallyDisconnected: The usage point has been disconnected
        through operation of a disconnect function within the meter
        present at the usage point.  The usage point is unable to
        receive or send the applicable commodity (electricity, gas,
        water, etc.)  A logical disconnect can often be achieved without
        utilising a field crew.
    :cvar physicallyDisconnected: The usage point has been disconnected
        from the network at a point upstream of the meter. The usage
        point is unable to receive or send the applicable commodity
        (electricity, gas, water, etc.). A physical disconnect is often
        achieved by utilising a field crew.
    """
    connected = "connected"
    logicallyDisconnected = "logicallyDisconnected"
    physicallyDisconnected = "physicallyDisconnected"


@dataclass
class Version:
    """This is the version for a group of devices or objects.

    This could be used to track the version for any group of objects or
    devices over time. For example, for a DERGroup, the requesting
    system may want to get the details of a specific version of a
    DERGroup.

    :ivar date: date of this version
    :ivar major: major release level for this version
    :ivar minor: minor release level for this version
    :ivar revision: revision level for this version
    """
    date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    major: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    minor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    revision: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


class WindingConnection(Enum):
    """
    Winding connection type.

    :cvar A: Autotransformer common winding
    :cvar D: Delta
    :cvar I: Independent winding, for single-phase connections
    :cvar Y: Wye
    :cvar Yn: Wye, with neutral brought out for grounding.
    :cvar Z: ZigZag
    :cvar Zn: ZigZag, with neutral brought out for grounding.
    """
    A = "A"
    D = "D"
    I = "I"
    Y = "Y"
    Yn = "Yn"
    Z = "Z"
    Zn = "Zn"


class WireInsulationKind(Enum):
    """
    Kind of wire insulation.

    :cvar asbestosAndVarnishedCambric: Asbestos and varnished cambric
        wire insulation.
    :cvar beltedPilc: Belted pilc wire insulation.
    :cvar butyl: Butyl wire insulation.
    :cvar crosslinkedPolyethylene: Crosslinked polyethylene wire
        insulation.
    :cvar ethylenePropyleneRubber: Ethylene propylene rubber wire
        insulation.
    :cvar highMolecularWeightPolyethylene: High nolecular weight
        polyethylene wire insulation.
    :cvar highPressureFluidFilled: High pressure fluid filled wire
        insulation.
    :cvar lowCapacitanceRubber: Low capacitance rubber wire insulation.
    :cvar oilPaper: Oil paper wire insulation.
    :cvar other: Other kind of wire insulation.
    :cvar ozoneResistantRubber: Ozone resistant rubber wire insulation.
    :cvar rubber: Rubber wire insulation.
    :cvar siliconRubber: Silicon rubber wire insulation.
    :cvar treeResistantHighMolecularWeightPolyethylene: Tree resistant
        high molecular weight polyethylene wire insulation.
    :cvar treeRetardantCrosslinkedPolyethylene: Tree retardant
        crosslinked polyethylene wire insulation.
    :cvar unbeltedPilc: Unbelted pilc wire insulation.
    :cvar varnishedCambricCloth: Varnished cambric cloth wire
        insulation.
    :cvar varnishedDacronGlass: Varnished dacron glass wire insulation.
    """
    asbestosAndVarnishedCambric = "asbestosAndVarnishedCambric"
    beltedPilc = "beltedPilc"
    butyl = "butyl"
    crosslinkedPolyethylene = "crosslinkedPolyethylene"
    ethylenePropyleneRubber = "ethylenePropyleneRubber"
    highMolecularWeightPolyethylene = "highMolecularWeightPolyethylene"
    highPressureFluidFilled = "highPressureFluidFilled"
    lowCapacitanceRubber = "lowCapacitanceRubber"
    oilPaper = "oilPaper"
    other = "other"
    ozoneResistantRubber = "ozoneResistantRubber"
    rubber = "rubber"
    siliconRubber = "siliconRubber"
    treeResistantHighMolecularWeightPolyethylene = "treeResistantHighMolecularWeightPolyethylene"
    treeRetardantCrosslinkedPolyethylene = "treeRetardantCrosslinkedPolyethylene"
    unbeltedPilc = "unbeltedPilc"
    varnishedCambricCloth = "varnishedCambricCloth"
    varnishedDacronGlass = "varnishedDacronGlass"


class WireMaterialKind(Enum):
    """
    Kind of wire material.

    :cvar aaac: Aluminum-alloy conductor steel reinforced.
    :cvar acsr: Aluminum conductor steel reinforced.
    :cvar aluminum: Aluminum wire.
    :cvar aluminumAlloy: Aluminum-alloy wire.
    :cvar aluminumAlloySteel: Aluminum-alloy-steel wire.
    :cvar aluminumSteel: Aluminum-steel wire.
    :cvar copper: Copper wire.
    :cvar other: Other wire material.
    :cvar steel: Steel wire.
    """
    aaac = "aaac"
    acsr = "acsr"
    aluminum = "aluminum"
    aluminumAlloy = "aluminumAlloy"
    aluminumAlloySteel = "aluminumAlloySteel"
    aluminumSteel = "aluminumSteel"
    copper = "copper"
    other = "other"
    steel = "steel"


@dataclass
class DERDynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to DER dynamics models.

    :ivar PowerElectronicsConnection: Power electronics connection with
        which this DER dynamics model is associated.
    :ivar RemoteInputSignals:
    :ivar SynchronousMachine: Synchronous machine model with which this
        DER dynamics model is associated.
    """
    PowerElectronicsConnection: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RemoteInputSignals: List["RemoteInputSignal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SynchronousMachine: List["SynchronousMachine"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DispatchSchedule:
    """
    :ivar confidence:
    :ivar curveStyleKind: Used to specify whether the values over an
        interval are constant (constantYValue) or linearly interpolated
        (straightLineYValues)
    :ivar numberOfIntervals: Used to specify the number of intervals
        when requesting a forecast or a dispatch.
    :ivar startTime: The start time of the first interval in the
        dispatch schedule
    :ivar timeIntervalDuration: The length of time for each interval in
        the dispatch schedule.
    :ivar timeIntervalUnit: The unit of measure for the time axis of the
        dispatch schedule.
    :ivar DERCurveData:
    :ivar DERMonitorableParameter:
    """
    confidence: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveStyleKind: Optional[CurveStyle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    numberOfIntervals: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    startTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    timeIntervalDuration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    timeIntervalUnit: Optional[TimeIntervalKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERCurveData: List["DERCurveData"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERMonitorableParameter: Optional["DERMonitorableParameter"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class EndDeviceTiming:
    """
    Timing for the control actions of end devices.

    :ivar duration: Duration of the end device control action or the
        business event that is the subject of the end device control.
    :ivar durationIndefinite: True if 'duration' is indefinite.
    :ivar randomisation: Kind of randomisation to be applied to the end
        device control actions to be executed.
    :ivar interval: Start and end time of an interval during which end
        device control actions are to be executed.
    """
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    durationIndefinite: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    randomisation: Optional[RandomisationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class FloatQuantity:
    """
    Quantity with float value and associated unit information.
    """
    multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class IdentifiedObject:
    """
    This is a root class to provide common identification for all classes
    needing identification and naming attributes.

    :ivar mRID: Master resource identifier issued by a model authority.
        The mRID is unique within an exchange context. Global uniqueness
        is easily achieved by using a UUID,  as specified in RFC 4122,
        for the mRID. The use of UUID is strongly recommended. For
        CIMXML data files in RDF syntax conforming to IEC 61970-552
        Edition 1, the mRID is mapped to rdf:ID or rdf:about attributes
        that identify CIM object elements.
    :ivar aliasName: The aliasName is free text human readable name of
        the object alternative to IdentifiedObject.name. It may be non
        unique and may not correlate to a naming hierarchy. The
        attribute aliasName is retained because of backwards
        compatibility between CIM relases. It is however recommended to
        replace aliasName with the Name class as aliasName is planned
        for retirement at a future time.
    :ivar description: The description is a free human readable text
        describing or naming the object. It may be non unique and may
        not correlate to a naming hierarchy.
    :ivar name: The name is any free human readable and possibly non
        unique text naming the object.
    :ivar Names: All names of this identified object.
    """
    mRID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    aliasName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Names: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class StringQuantity:
    """
    Quantity with string value (when it is not important whether it is an
    integral or a floating point number) and associated unit information.
    """
    multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class SvPowerFlow(StateVariable):
    """State variable for power flow.

    Load convention is used for flow direction. This means flow out from
    the TopologicalNode into the equipment is positive.

    :ivar p: The active power flow. Load sign convention is used, i.e.
        positive sign means flow out from a TopologicalNode (bus) into
        the conducting equipment.
    :ivar phase: The individual phase of the flow.   If unspecified,
        then assumed to be balanced among phases.
    :ivar q: The reactive power flow. Load sign convention is used, i.e.
        positive sign means flow out from a TopologicalNode (bus) into
        the conducting equipment.
    :ivar Terminal: The terminal associated with the power flow state
        variable.
    """
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class SvShuntCompensatorSections(StateVariable):
    """
    State variable for the number of sections in service for a shunt
    compensator.

    :ivar phase: The terminal phase at which the connection is applied.
        If missing, the injection is assumed to be balanced among non-
        neutral phases.
    :ivar sections: The number of sections in service as a continous
        variable. To get integer value scale with
        ShuntCompensator.bPerSection.
    :ivar ShuntCompensator: The shunt compensator for which the state
        applies.
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sections: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ShuntCompensator: Optional["ShuntCompensator"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class SvStatus(StateVariable):
    """
    State variable for status.

    :ivar phase: The individual phase status.    If the attribute is
        unspecified, then three phase model is assumed.
    :ivar ConductingEquipment: The conducting equipment associated with
        the status state variable.
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ConductingEquipment: Optional["ConductingEquipment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class SvTapStep(StateVariable):
    """
    State variable for transformer tap step.

    :ivar position: The floating point tap position.   This is not the
        tap ratio, but rather the tap step position as defined by the
        related tap changer model and normally is constrained to be
        within the range of minimum and maximum tap positions.
    :ivar TapChanger: The tap changer associated with the tap step
        state.
    """
    position: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TapChanger: Optional["TapChanger"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class SvVoltage(StateVariable):
    """
    State variable for voltage.

    :ivar angle: The voltage angle of the topological node complex
        voltage with respect to system reference.
    :ivar phase: If specified the voltage is the line to ground voltage
        of the individual phase.   If unspecified, then the voltage is
        assumed balanced.
    :ivar v: The voltage magnitude at the topological node.
    :ivar ConnectivityNode:
    :ivar TopologicalNode: The topological node associated with the
        voltage state.
    """
    angle: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    v: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ConnectivityNode: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    TopologicalNode: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class BasicIntervalSchedule(IdentifiedObject):
    """
    Schedule of values at points in time.

    :ivar startTime: The time for the first time point.  The value can
        be a time of day, not a specific date.
    :ivar value1Multiplier: Multiplier for value1.
    :ivar value1Unit: Value1 units of measure.
    :ivar value2Multiplier: Multiplier for value2.
    :ivar value2Unit: Value2 units of measure.
    """
    startTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value1Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value1Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value2Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value2Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConstantReactivePowerSettings(IdentifiedObject):
    """Constant Reactive Power Settings.

    Reference: IEEE1547-2018.

    :ivar enabled: Constant reactive power mode select
        (CONST_Q_MODE_ENABLE). True means enabled. False means disabled.
        Typical value = false.
    :ivar reactivePower: Injecting reactive power setting (CONST_Q). Per
        unit value based on NP_Q_MAX_INJ. Negative signs should not be
        used but if present, indicates absorbing VAr based on
        NP_Q_MAX_ABS. Typical value = 0.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this
        constant reactive power settings  model.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class CoordinateSystem(IdentifiedObject):
    """
    Coordinate reference system.

    :ivar crsUrn: A Uniform Resource Name (URN) for the coordinate
        reference system (crs) used to define 'Location.PositionPoints'.
        An example would be the European Petroleum Survey Group (EPSG)
        code for a coordinate reference system, defined in URN under the
        Open Geospatial Consortium (OGC) namespace as:
        urn:ogc:def:uom:EPSG::XXXX, where XXXX is an EPSG code (a full
        list of codes can be found at the EPSG Registry web site
        http://www.epsg-registry.org/). To define the coordinate system
        as being WGS84 (latitude, longitude) using an EPSG OGC, this
        attribute would be urn:ogc:def:uom:EPSG::4236. A profile should
        limit this code to a set of allowed URNs agreed to by all
        sending and receiving parties.
    :ivar Locations: All locations described with position points in
        this coordinate system.
    """
    crsUrn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Locations: List["Location"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Curve(IdentifiedObject):
    """
    A multi-purpose curve or functional relationship between an independent
    variable (X-axis) and dependent (Y-axis) variables.

    :ivar curveStyle: The style or shape of the curve.
    :ivar xMultiplier: Multiplier for X-axis.
    :ivar xUnit: The X-axis units of measure.
    :ivar y1Multiplier: Multiplier for Y1-axis.
    :ivar y1Unit: The Y1-axis units of measure.
    :ivar y2Multiplier: Multiplier for Y2-axis.
    :ivar y2Unit: The Y2-axis units of measure.
    :ivar y3Multiplier: Multiplier for Y3-axis.
    :ivar y3Unit: The Y3-axis units of measure.
    :ivar CurveDatas: The point data values that define this curve.
    """
    curveStyle: Optional[CurveStyle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    xMultiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    xUnit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y1Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y1Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y2Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y2Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y3Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y3Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    CurveDatas: List[CurveData] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Customer(IdentifiedObject):
    """
    Organisation receiving services from service supplier.

    :ivar locale: Locale designating language to use in communications
        with this customer.
    :ivar pucNumber: (if applicable) Public utilities commission (PUC)
        identification number.
    :ivar specialNeed: True if customer organisation has special service
        needs such as life support, hospitals, etc.
    :ivar vip: (use 'priority' instead) True if this is an important
        customer. Importance is for matters different than those in
        'specialNeed' attribute.
    :ivar ConfigurationEvents: All configuration events created for this
        organisation role.
    :ivar EndDevices: All end devices of this customer.
    :ivar priority: Priority of the customer.
    :ivar status: Status of this customer.
    """
    locale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pucNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    specialNeed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    vip: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ConfigurationEvents: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDevices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    priority: Optional[Priority] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DERCurveData:
    intervalNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maxYValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minYValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    nominalYValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERMonitorableParameter: Optional["DERMonitorableParameter"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    DispatchSchedule: Optional[DispatchSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DERGroupDispatch(IdentifiedObject):
    EndDeviceGroup: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DERGroupForecast(IdentifiedObject):
    predictionCreationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceGroup: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class DERNameplateDataApplied(IdentifiedObject):
    """Capability related settings that may be changed (applied) at the time of
    commissioning or testing the DER.

    Settings in DERNameplateData are specified by the utility before
    commissioning, and usually not changed. Reference: IEEE 1547-2018
    and IEEE 1547.1-2020.

    :ivar acVnom: Voltage Base Nominal AC voltage rating in RMS Vac
        (NP_AC_V_NOM).
    :ivar apparentPowerChargeMax: Maximum apparent power charge rating
        in kilo Volt Amperes.  May differ from the apparent power
        maximum rating. (NP_APPARENT_POWER_CHARGE_MAX).
    :ivar overPF: Over-excited power factor (NP_OVER_PF).
    :ivar pMax: Active power rating in kilowatts at unity power factor
        (NP_P_MAX).
    :ivar pMaxCharge: Maximum active power charge rating in kilowatts
        (NP_P_MAX_CHARGE).
    :ivar pMaxOverPF: Active power rating in kilowatts at specified
        over-excited power factor (NP_P_MAX_OVER_PF).
    :ivar pMaxUnderPF: Active power rating in kilowatts at specified
        under-excited power factor (NP_P_MAX_UNDER_PF).
    :ivar qMaxAbs: Maximum absorbed reactive power rating in kilovolt-
        amperes reactive  (NP_Q_MAX_ABS).
    :ivar qMaxInj: Maximum injected reactive power rating in kilovolt-
        amperes reactive  (NP_Q_MAX_INJ).
    :ivar sMax: Maximum apparent power rating in kilovolt-amperes
        (NP_VA_MAX).
    :ivar underPF: Under-excited power factor (NP_UNDER_PF).
    :ivar DERNameplateData: The DER nameplate data to which this DER
        data is applied.
    """
    acVnom: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    apparentPowerChargeMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    overPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pMaxCharge: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pMaxOverPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pMaxUnderPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    qMaxAbs: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    qMaxInj: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    underPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERNameplateData: Optional["DERNameplateData"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class DayType(IdentifiedObject):
    """Group of similar days.

    For example it could be used to represent weekdays, weekend, or
    holidays.

    :ivar SeasonDayTypeSchedules: Schedules that use this DayType.
    """
    SeasonDayTypeSchedules: List["SeasonDayTypeSchedule"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceControlType(IdentifiedObject):
    """Detailed description for a control produced by an end device.

    Values in attributes allow for creation of recommended codes to be used for identifying end device controls as follows: &amp;lt;type&amp;gt;.&amp;lt;domain&amp;gt;.&amp;lt;subDomain&amp;gt;.&amp;lt;eventOrAction&amp;gt;.

    :ivar domain: High-level nature of the control.
    :ivar eventOrAction: The most specific part of this control type. It
        is mainly in the form of a verb that gives action to the control
        that just occurred.
    :ivar subDomain: More specific nature of the control, as a further
        sub-categorisation of 'domain'.
    :ivar type: Type of physical device from which the control was
        created. A value of zero (0) can be used when the source is
        unknown.
    :ivar EndDeviceControls: All end device controls of this type.
    """
    domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    eventOrAction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    subDomain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceControls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceEventDetail:
    """
    Name-value pair, specific to end device events.

    :ivar name: Name.
    :ivar EndDeviceEvent: End device owning this detail.
    :ivar value: Value, including unit information.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceEvent: Optional["EndDeviceEvent"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value: Optional[StringQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceEventType(IdentifiedObject):
    """Detailed description for an event produced by an end device.

    Values in attributes allow for creation of recommended codes to be used for identifying end device events as follows: &amp;lt;type&amp;gt;.&amp;lt;domain&amp;gt;.&amp;lt;subDomain&amp;gt;.&amp;lt;eventOrAction&amp;gt;.

    :ivar domain: High-level nature of the event. By properly
        classifying events by a small set of domain codes, a system can
        more easily run reports based on the types of events that have
        occurred or been received.
    :ivar eventOrAction: The most specific part of this event type. It
        is mainly in the form of a verb that gives action to the event
        that just occurred.
    :ivar subDomain: More specific nature of the event, as a further
        sub-categorisation of 'domain'.
    :ivar type: Type of physical device from which the event was
        created. A value of zero (0) can be used when the source is
        unknown.
    :ivar EndDeviceEvents: All end device events of this type.
    """
    domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    eventOrAction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    subDomain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceEvents: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class FaultCauseType(IdentifiedObject):
    """
    Type of cause of the fault.

    :ivar Faults: All faults with this cause type.
    """
    Faults: List["Fault"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class FrequencyDroopSettings(IdentifiedObject):
    """Frequency Droop Settings.

    Reference: IEEE1547-2018.

    :ivar dbof: Over frequency deadband offset from nominal frequency in
        Hz (PF_DBOF). Frequency values shall be reported to 3 decimal
        places. Typical value = 0,036.
    :ivar dbuf: Under frequency deadband offset from nominal frequency
        in Hz (PF_DBUF). Frequency values shall be reported to 3 decimal
        places. Typical value = 0,036.
    :ivar kof: Over frequency per unit frequency change corresponding to
        a 1 per unit power change (frequency droop) (PF_KOF). Typical
        value = 0,05.
    :ivar kuf: Under frequency per unit frequency change corresponding
        to a 1 per unit power change (frequency droop) (PF_KUF). Typical
        value = 0,05.
    :ivar olrt: Frequency droop open loop response time (PF_OLRT)
        (&gt;=0). The duration from a step change in control signal
        input until the output changes by 90% of its final change,
        before any overshoot. Typical value = 5.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this
        frequency droop settings model.
    """
    dbof: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dbuf: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    kof: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    kuf: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    olrt: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class FrequencyTripSettings(IdentifiedObject):
    """Frequency Trip Settings.

    Reference: IEEE1547-2018.

    :ivar of1TripF: Must trip frequency magnitude (OF1_TRIP_F).
        Frequency values shall be reported to 3 decimal places. Typical
        value = 61,2.
    :ivar of1TripT: Must trip duration (OF1_TRIP_T) (&gt;=0). Typical
        value = 300.
    :ivar of2TripF: Must trip frequency magnitude (OF2_TRIP_F).
        Frequency values shall be reported to 3 decimal places. Typical
        value = 62.
    :ivar of2TripT: Must trip duration (OF2_TRIP_T) (&gt;=0). Typical
        value = 0,16.
    :ivar uf1TripF: Must trip frequency magnitude (UF1_TRIP_F).
        Frequency values shall be reported to 3 decimal places. Typical
        value = 58,5.
    :ivar uf1TripT: Must trip duration (UF1_TRIP_T) (&gt;=0). Typical
        value = 300.
    :ivar uf2TripF: Must trip frequency magnitude (UF2_TRIP_F).
        Frequency values shall be reported to 3 decimal places. Typical
        value = 56,5.
    :ivar uf2TripT: Must trip duration (UF2_TRIP_T) (&gt;=0). Typical
        value = 0,16.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this
        frequency trip settings model.
    """
    of1TripF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    of1TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    of2TripF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    of2TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf1TripF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf1TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf2TripF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf2TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class GAPPS_CIM_export:
    IdentifiedObject: List[IdentifiedObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class GeographicalRegion(IdentifiedObject):
    """
    A geographical region of a power system network model.

    :ivar Regions: All sub-geograhpical regions within this geographical
        region.
    """
    Regions: List["SubGeographicalRegion"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class IOPoint(IdentifiedObject):
    """The class describe a measurement or control value.

    The purpose is to enable having attributes and associations common
    for measurement and control.
    """


@dataclass
class LoadResponseCharacteristic(IdentifiedObject):
    """Models the characteristic response of the load demand due to changes in
    system conditions such as voltage and frequency. This is not related to
    demand response. If LoadResponseCharacteristic.exponentModel is True, the
    voltage exponents are specified and used as to calculate:

    Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent
    Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent
    Where  * means "multiply" and ** is "raised to power of".

    :ivar exponentModel: Indicates the exponential voltage dependency
        model is to be used.   If false, the coefficient model is to be
        used. The exponential voltage dependency model consist of the
        attributes - pVoltageExponent - qVoltageExponent. The
        coefficient model consist of the attributes - pConstantImpedance
        - pConstantCurrent - pConstantPower - qConstantImpedance -
        qConstantCurrent - qConstantPower. The sum of
        pConstantImpedance, pConstantCurrent and pConstantPower shall
        equal 1. The sum of qConstantImpedance, qConstantCurrent and
        qConstantPower shall equal 1.
    :ivar pConstantCurrent: Portion of active power load modeled as
        constant current.
    :ivar pConstantImpedance: Portion of active power load modeled as
        constant impedance.
    :ivar pConstantPower: Portion of active power load modeled as
        constant power.
    :ivar pVoltageExponent: Exponent of per unit voltage effecting real
        power.
    :ivar qConstantCurrent: Portion of reactive power load modeled as
        constant current.
    :ivar qConstantImpedance: Portion of reactive power load modeled as
        constant impedance.
    :ivar qConstantPower: Portion of reactive power load modeled as
        constant power.
    :ivar qVoltageExponent: Exponent of per unit voltage effecting
        reactive power.
    :ivar EnergyConsumer: The set of loads that have the response
        characteristics.
    """
    exponentModel: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pConstantCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pConstantImpedance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pConstantPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pVoltageExponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    qConstantCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    qConstantImpedance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    qConstantPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    qVoltageExponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergyConsumer: List["EnergyConsumer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class MeterReading(IdentifiedObject):
    """
    Set of values obtained from the meter.

    :ivar EndDeviceEvents: All end device events associated with this
        set of measured values.
    :ivar Meter: Meter providing this reading.
    :ivar UsagePoint: Usage point from which this meter reading (set of
        values) has been obtained.
    """
    EndDeviceEvents: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Meter: Optional["Meter"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UsagePoint: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class MomentaryCessationSettings(IdentifiedObject):
    """Momentary Cessation Settings.

    Reference: IEEE1547-2018.

    :ivar hvrtT1: High-voltage momentary cessation time (MC_HVRT_T1)
        (&gt;=0). Typical value = 0.
    :ivar hvrtT2: High-voltage momentary cessation time (MC_HVRT_T2)
        (&gt;=0). Typical value = 13.
    :ivar hvrtV1: High-voltage momentary cessation voltage (MC_HVRT_V1).
        Per unit value based on NP_AC_V_NOM (voltage base). Typical
        value = 1,1.
    :ivar hvrtV2: High-voltage momentary cessation voltage (MC_HVRT_V2).
        Per unit value based on NP_AC_V_NOM (voltage base). Typical
        value = 1,2.
    :ivar lvrtT1: Low-voltage momentary cessation time (MC_LVRT_T1)
        (&gt;=0). Typical value = 0.
    :ivar lvrtT2: Low-voltage momentary cessation time (MC_LVRT_T2)
        (&gt;=0). Typical value = 2.
    :ivar lvrtV1: Low-voltage momentary cessation voltage (MC_LVRT_V1).
        Per unit value based on NP_AC_V_NOM (voltage base). Typical
        value = 0,5.
    :ivar lvrtV2: Low-voltage momentary cessation voltage (MC_LVRT_V2).
        Per unit value based on NP_AC_V_NOM (voltage base). Typical
        value = 0.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this
        momentary cessation settings model.
    """
    hvrtT1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hvrtT2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hvrtV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hvrtV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lvrtT1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lvrtT2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lvrtV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lvrtV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class OperationalLimitType(IdentifiedObject):
    """
    The operational meaning of a category of limits.

    :ivar acceptableDuration: The nominal acceptable duration of the
        limit.  Limits are commonly expressed in terms of the a time
        limit for which the limit is normally acceptable.   The actual
        acceptable duration of a specific limit may depend on other
        local factors such as temperature or wind speed.
    :ivar direction: The direction of the limit.
    :ivar OperationalLimit: The operational limits associated with this
        type of limit.
    """
    acceptableDuration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    direction: Optional[OperationalLimitDirectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OperationalLimit: List["OperationalLimit"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PerLengthLineParameter(IdentifiedObject):
    """
    Common type for per-length electrical catalogues describing line
    parameters.

    :ivar WireAssemblyInfo: A WireAssemblyInfo is used to compute the
        PerLengthParameter data in the Wires package
    """
    WireAssemblyInfo: Optional["WireAssemblyInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PowerLimitSettings(IdentifiedObject):
    """Power limit settings.

    Reference: IEEE1547-2018.

    :ivar enabled: Limit active power enable (AP_LIMIT_P_ENABLE). True
        means enabled. False means disabled. Typical value = false.
    :ivar pMax: Maximum active power setting (AP_MAX_P). Typical value =
        100.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this power
        limit settings model.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class RemoteInputSignal:
    """
    Supports connection to a terminal associated with a remote bus from which
    an input signal of a specific type is coming.

    :ivar remoteSignalType: Type of input signal.
    :ivar DERDynamics:
    :ivar Terminal:
    """
    remoteSignalType: Optional[RemoteSignalKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERDynamics: List[DERDynamics] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class ScheduledEvent(IdentifiedObject):
    """
    An event to trigger one or more activities, such as reading a meter,
    recalculating a bill, requesting work, when generating units must be
    scheduled for maintenance, when a transformer is scheduled to be
    refurbished, etc.

    :ivar duration: Duration of the scheduled event, for example, the
        time to ramp between values.
    :ivar type: Type of scheduled event.
    :ivar Assets:
    """
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Season(IdentifiedObject):
    """
    A specified time period of the year.

    :ivar endDate: Date season ends.
    :ivar startDate: Date season starts.
    :ivar SeasonDayTypeSchedules: Schedules that use this Season.
    """
    endDate: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    startDate: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SeasonDayTypeSchedules: List["SeasonDayTypeSchedule"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ServiceSettings(IdentifiedObject):
    """Service settings.

    Reference: IEEE1547-2018.

    :ivar delay: Minimum intentional delay before initiating Soft-Start
        (ES_DELAY) (&gt;=0). Typical value = 300.
    :ivar highFrequency: Frequency shall be equal to or less than
        default value. Frequency values shall be reported to 3 decimal
        places. (ES_F_HIGH). Typical value = 60,1.
    :ivar highVoltage: Per unit value based on NP_AC_V_NOM (voltage
        base). Voltage shall be equal to or less than default value.
        (ES_V_HIGH). Typical value = 1,05.
    :ivar lowFrequency: Frequency shall be equal to or greater than
        default value. Frequency values shall be reported to 3 decimal
        places. (ES_F_LOW). Typical value = 59,5.
    :ivar lowVoltage: Per unit value based on NP_AC_V_NOM (voltage
        base). Voltage shall be equal to or greater than default value.
        (ES_V_LOW). Typical value = 0,917.
    :ivar permitService: This function is activated by request from the
        Area Electric Power System (EPS) Operator (ES_PERMIT_SERVICE).
        True means enabled. False means deactivated. Typical value =
        true.
    :ivar rampRate: Enter service soft-start duration. Time from zero to
        100% NP_P_MAX (ES_RAMP_RATE) (&gt;=0). Typical value = 300.
    :ivar randomizedDelay: Enter service radomized delay is an optional
        feature in IEEE Std 1547-2018 (ES_RANDOMIZED_DELAY) (&gt;=0).
        Typical value = 300.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this
        service settings model.
    """
    delay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    highFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    highVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lowFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lowVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    permitService: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rampRate: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    randomizedDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class SvEstVoltage(SvVoltage):
    angleVariance: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    vVariance: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Estimate: Optional["Estimate"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ThermostatController(IdentifiedObject):
    """
    a price-responsive or bidding smart thermostat.

    :ivar aggregatorName: name of a market aggregator that collects bid
        curves for a higher-level market
    :ivar baseSetpoint: user's desired thermostat setpoint, including
        the effects of pre-programmed schedule
    :ivar controlMode:
    :ivar priceCap: maximum price per kwh that the controller will bid,
        regardless of the market's price cap
    :ivar rampHigh: slope of high-temperature bidding curve, $/degreeC
    :ivar rampLow: slope of low-temperature bidding curve, $/degreeC
    :ivar rangeHigh: maximum postive offset to the thermostat setpoint
    :ivar rangeLow: maximum negative offset to the thermostat setpoint
    :ivar useOverride:
    :ivar usePredictive:
    :ivar House:
    """
    aggregatorName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    baseSetpoint: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    controlMode: Optional[ThermostatControlMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    priceCap: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    rampHigh: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    rampLow: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    rangeHigh: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    rangeLow: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    useOverride: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    usePredictive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    House: Optional["House"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class TopologicalIsland(IdentifiedObject):
    """An electrically connected subset of the network. Topological islands can
    change as the current network state changes: e.g. due to.

    - disconnect switches or breakers change state in a SCADA/EMS
    - manual creation, change or deletion of topological nodes in a planning tool.

    :ivar TopologicalNodes: A topological node belongs to a topological
        island.
    """
    TopologicalNodes: List["TopologicalNode"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class TransformerCoreAdmittance(IdentifiedObject):
    """The transformer core admittance.

    Used to specify the core admittance of a transformer in a manner
    that can be shared among power transformers.

    :ivar b: Magnetizing branch susceptance (B mag).  The value can be
        positive or negative.
    :ivar b0: Zero sequence magnetizing branch susceptance.
    :ivar g: Magnetizing branch conductance (G mag).
    :ivar g0: Zero sequence magnetizing branch conductance.
    :ivar TransformerEnd: All transformer ends having this core
        admittance.
    :ivar TransformerEndInfo: Transformer end datasheet used to
        calculate this core admittance.
    """
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    b0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    g0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TransformerEnd: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TransformerEndInfo: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TransformerMeshImpedance(IdentifiedObject):
    """Transformer mesh impedance (Delta-model) between transformer ends.

    The typical case is that this class describes the impedance between
    two transformer ends pair-wise, i.e. the cardinalities at both
    tranformer end associations are 1. But in cases where two or more
    transformer ends are modeled the cardinalities are larger than 1.

    :ivar r: Resistance between the 'from' and the 'to' end, seen from
        the 'from' end.
    :ivar r0: Zero-sequence resistance between the 'from' and the 'to'
        end, seen from the 'from' end.
    :ivar x: Reactance between the 'from' and the 'to' end, seen from
        the 'from' end.
    :ivar x0: Zero-sequence reactance between the 'from' and the 'to'
        end, seen from the 'from' end.
    :ivar FromTransformerEnd: From end this mesh impedance is connected
        to. It determines the voltage reference.
    :ivar FromTransformerEndInfo: 'from' transformer end datasheet this
        mesh impedance is calculated from. It determines the voltage
        reference.
    :ivar ToTransformerEnd: All transformer ends this mesh impedance is
        connected to.
    :ivar ToTransformerEndInfos: All 'to' transformer end datasheets
        this mesh impedance for 'from' transformer end is calculated
        from.
    """
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    FromTransformerEnd: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    FromTransformerEndInfo: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ToTransformerEnd: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    ToTransformerEndInfos: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TransformerTest(IdentifiedObject):
    """
    Test result for transformer ends, such as short-circuit, open-circuit
    (excitation) or no-load test.

    :ivar basePower: Base power at which the tests are conducted,
        usually equal to the rateds of one of the involved transformer
        ends.
    :ivar temperature: Temperature at which the test is conducted.
    """
    basePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    temperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class UsagePointGroup(IdentifiedObject):
    """Abstraction for management of group communications within a two-way AMR
    system or the data for a group of related usage points.

    Commands can be issued to all of the usage points that belong to a
    usage point group using a defined group address and the underlying
    AMR communication infrastructure.

    :ivar type: Type of this group.
    :ivar DemandResponsePrograms: All demand response programs this
        usage point group is enrolled in.
    :ivar EndDeviceControls: All end device controls sending commands to
        this usage point group.
    :ivar UsagePoints: All usage points in this group.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DemandResponsePrograms: List["DemandResponseProgram"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceControls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltVarSettings(IdentifiedObject):
    """Volt Var Settings.

    Reference: IEEE1547-2018.

    :ivar curveQ1: VArs at V1. Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. (QV_CURVE_Q1). Typical value = 0,44.
    :ivar curveQ2: VArs at V2. Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. (QV_CURVE_Q2). Typical value = 0.
    :ivar curveQ3: VArs at V3. Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. (QV_CURVE_Q3). Typical value = 0.
    :ivar curveQ4: VArs at V4. Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. (QV_CURVE_Q4). Typical value = -0,44.
    :ivar curveV1: Undervoltage magnitude where VArs are at maximum. Per
        unit value based on NP_AC_V_NOM (voltage base) (QV_CURVE_V1).
        Typical value = 0,92.
    :ivar curveV2: Undervoltage magnitude where VArs are at minimum. Per
        unit value based on NP_AC_V_NOM (voltage base) (QV_CURVE_V2).
        Typical value = 0,98.
    :ivar curveV3: Overvoltage magnitude where VArs are at minimum. Per
        unit value based on NP_AC_V_NOM (voltage base) (QV_CURVE_V3).
        Typical value = 1,02.
    :ivar curveV4: Overvoltage magnitude where VArs are at minimum. Per
        unit value based on NP_AC_V_NOM (voltage base) (QV_CURVE_V4).
        Typical value = 1,08.
    :ivar enabled: Enables Volt-Var settings. It is specified by the
        area electric power system operator (QV_MODE_ENABLE). True means
        enabled. False meand disabled. Typical value = false.
    :ivar olrt: Volt-VAr open loop response time (QV_OLRT) (&gt;=0).
        Typical value = 5.
    :ivar vRef: Per unit value based on NP_AC_V_NOM (voltage base)
        (QV_VREF). Typical value = 1.
    :ivar vRefAutoModeEnabled: Enables Volt-Var settings auto mode. It
        is specified by the area electric power system operator
        (QV_VREF_AUTO_MODE). True means enabled. False meand disabled.
        Typical value = true.
    :ivar vRefOlrt: Vref time constant in seconds as specified by the
        area EPS operator (QV_VREF_OLRT) (&gt;=0).
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this volt
        var settings model.
    """
    curveQ1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveQ2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveQ3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveQ4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveV3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveV4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    olrt: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    vRef: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    vRefAutoModeEnabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    vRefOlrt: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltWattSettings(IdentifiedObject):
    """Volt Watt Settings.

    Reference: IEEE1547-2018.

    :ivar curveP1: Active power level at V1 (PV_CURVE_P1). Per unit
        value based on NP_P_MAX_CHARGE. Typical value = 1.
    :ivar curveP2gen: Minimum active power generating at V2
        (PV_CURVE_P2_GEN). The lesser of 0.2*Prated or Pmin. Per unit
        value based on NP_P_MAX. Typical value = Pmin.
    :ivar curveP2load: Applicable to DER which can generate and absorb
        active power (PV_CURVE_P2_LOAD). Per unit Value based on
        NP_P_MAX_CHARGE. Negative values indicate active power load.
        Indicates maximum active power absorption. Typical value = 0.
    :ivar curveV1: Upper start voltage for power reduction
        (PV_CURVE_V1). Per unit value based on NP_AC_V_NOM (voltage
        base). Typical value = 1,06.
    :ivar curveV2: Upper voltager for maximum power reduction
        (PV_CURVE_V2). Per unit value based on NP_AC_V_NOM (voltage
        base). Typical value = 1,1.
    :ivar enabled: Voltage-active power mode enable (PV_MODE_ENABLE).
        True means enabled. False means disabled. Typical value = false.
    :ivar olrt: P(V) open loop response time setting (PV_OLRT) (&gt;=0).
        Typical value = 10.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this volt
        watt settings model.
    """
    curveP1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveP2gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveP2load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    olrt: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltageTripSettings(IdentifiedObject):
    """Voltage Trip Settings.

    Reference: IEEE1547-2018.

    :ivar ov1TripT: Must trip duration (OV1_TRIP_T) (&gt;=0). Typical
        value = 13.
    :ivar ov1TripV: Must trip magnitude (OV1_TRIP_V). Per unit value
        based on NP_AC_V_NOM (voltage base). Typical value = 1,1.
    :ivar ov2TripT: Must trip duration (OV2_TRIP_T) (&gt;=0). Typical
        value = 0,16.
    :ivar ov2TripV: Must trip magnitude (OV2_TRIP_V). Per unit value
        based on NP_AC_V_NOM (voltage base). Typical value = 1,2.
    :ivar uv1TripT: Must trip duration (UV1_TRIP_T) (&gt;=0). Typical
        value = 21.
    :ivar uv1TripV: Must trip magnitude (UV1_TRIP_V). Per unit value
        based on NP_AC_V_NOM (voltage base). Typical value = 0,88.
    :ivar uv2TripT: Must trip duration (UV2_TRIP_T) (&gt;=0). Typical
        value = 2.
    :ivar uv2TripV: Must trip magnitude (UV2_TRIP_V). Per unit value
        based on NP_AC_V_NOM (voltage base). Typical value = 0,5.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this
        voltage trip settings model.
    """
    ov1TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov1TripV: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov2TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov2TripV: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv1TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv1TripV: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv2TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv2TripV: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WattVarSettings(IdentifiedObject):
    """Watt Var Settings.

    Reference: IEEE1547-2018.

    :ivar curveP1gen: Lower active power (generating) (QP_CURVE_P1_GEN).
        Per unit value based on NP_P_MAX. Typical value = 0,2.
    :ivar curveP1load: Lower active power (absorbing)
        (QP_CURVE_P1_LOAD). Per unit value based on NP_P_MAX_CHARGE.
        Typical value = -0,2.
    :ivar curveP2gen: Medium active power (generating)
        (QP_CURVE_P2_GEN). Per unit value based on NP_P_MAX. Typical
        value = 0,5.
    :ivar curveP2load: Medium active power (absorbing)
        (QP_CURVE_P2_LOAD). Per unit value based on NP_P_MAX_CHARGE.
        Typical value = -0,5.
    :ivar curveP3gen: Maximum active power (generating)
        (QP_CURVE_P3_GEN). Per unit value based on NP_P_MAX. Typical
        value = 1.
    :ivar curveP3load: Maximum active power (absorbing)
        (QP_CURVE_P3_LOAD). Per unit value based on NP_P_MAX_CHARGE.
        Typical value = -1.
    :ivar curveQ1gen: Lower reactive power while generating
        (QP_CURVE_Q1_GEN). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = 0.
    :ivar curveQ1load: Maximum reactive power while absorbing
        (QP_CURVE_Q1_LOAD). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = 0.
    :ivar curveQ2gen: Medium reactive power while generating
        (QP_CURVE_Q2_GEN). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = 0.
    :ivar curveQ2load: Medium reactive power while absorbing
        (QP_CURVE_Q2_LOAD). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr.. Typical value = 0.
    :ivar curveQ3gen: Maximum reactive power while generating
        (QP_CURVE_Q3_GEN). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = -0,44.
    :ivar curveQ3load: Lower reactive power while absorbing
        (QP_CURVE_Q3_LOAD). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = 0,44.
    :ivar enabled: This function is deactivated by request from the area
        electric power system operator (QP_MODE_ENABLE). True means
        enabled. False means disabled. Typical value = false.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this watt
        var settings model.
    """
    curveP1gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveP1load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveP2gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveP2load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveP3gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveP3load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveQ1gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveQ1load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveQ2gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveQ2load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveQ3gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curveQ3load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WirePosition(IdentifiedObject):
    """
    Identification, spacing and configuration of the wires of a conductor with
    respect to a structure.

    :ivar sequenceNumber: Numbering for wires on a WireSpacingInfo.
        Neutrals should be numbered last. Multiple circuits on the same
        pole, tower or right-of-way can be included with unique sequence
        numbers for the phases, and identical sequence numbers for any
        shared neutrals.
    :ivar xCoord: Signed horizontal distance from the wire at this
        position to a common reference point.
    :ivar yCoord: Signed vertical distance from the wire at this
        position: above ground (positive value) or burial depth below
        ground (negative value).
    :ivar WirePhaseInfo:
    :ivar WireSpacingInfo: Wire spacing data this wire position belongs
        to.
    """
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    xCoord: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    yCoord: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WirePhaseInfo: List["WirePhaseInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WireSpacingInfo: Optional["WireSpacingInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Control(IOPoint):
    """Control is used for supervisory/device control.

    It represents control outputs that are used to change the state in a
    process, e.g. close or open breaker, a set point value or a raise
    lower command.

    :ivar controlType: Specifies the type of Control, e.g.
        BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The
        ControlType.name shall be unique among all specified types and
        describe the type.
    :ivar timeStamp: The last time a control output was sent.
    :ivar unitMultiplier: The unit multiplier of the controlled
        quantity.
    :ivar unitSymbol: The unit of measure of the controlled quantity.
    :ivar PowerSystemResource: Regulating device governed by this
        control output.
    """
    controlType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    unitMultiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    unitSymbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerSystemResource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DERMonitorableParameter:
    DERParameter: Optional[DERParameterKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    flowDirection: Optional[FlowDirectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    yMultiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    yUnit: Optional[DERUnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    yUnitInstalledMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    yUnitInstalledMin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERCurveData: Optional[DERCurveData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DispatchSchedule: List[DispatchSchedule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceGroup: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DERNameplateData(IdentifiedObject):
    """DER nameplate data.

    Reference: IEEE1547-2018.

    :ivar abnormalOPcatKind: Abnormal performance Category
        (NP_ABNORMAL_OP_CAT).
    :ivar acVmax: AC voltage rating in RMS Volts (NP_AC_V_MAX).
    :ivar acVmin: AC voltage rating in RMS Volts (NP_AC_V_MIN).
    :ivar fwVer: FW Version (NP_FW_VER).
    :ivar manufacturer: Manufacturer (NP_MANUFACTURER).
    :ivar model: Model (NP_MODEL).
    :ivar normalOPcatKind: Normal performance capability
        (NP_NORMAL_OP_CAT).
    :ivar reactiveSusceptance: Reactive susceptance that remains
        connected to the Area EPS in the cease to energize and trip
        state (NP_REACTIVE_SUSCEPTANCE).
    :ivar serialNum: Serial number (NP_SERIAL_NUM).
    :ivar supportsConstPFmode:
    :ivar supportsConstQmode:
    :ivar supportsPFmode:
    :ivar supportsPVmode:
    :ivar supportsQPmode:
    :ivar supportsQVmode:
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this DER
        nameplate data model.
    :ivar DERNameplateDataApplied: The applied DER nameplate data.
    """
    abnormalOPcatKind: Optional[AbnormalOPcatKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    acVmax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    acVmin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    fwVer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normalOPcatKind: Optional[NormalOPcatKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reactiveSusceptance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    serialNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsConstPFmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supportsConstQmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supportsPFmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supportsPVmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supportsQPmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supportsQVmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERNameplateDataApplied: List[DERNameplateDataApplied] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class DemandResponseProgram(IdentifiedObject):
    """
    Demand response program.

    :ivar type: Type of demand response program; examples are CPP
        (critical-peak pricing), RTP (real-time pricing), DLC (direct
        load control), DBP (demand bidding program), BIP (base
        interruptible program). Note that possible types change a lot
        and it would be impossible to enumerate them all.
    :ivar EndDeviceGroups: All groups of end devices enrolled in this
        demand response program.
    :ivar UsagePointGroups: All usage point groups enrolled in this
        demand response program.
    :ivar validityInterval: Interval within which the program is valid.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceGroups: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UsagePointGroups: List[UsagePointGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    validityInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Estimate:
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SvEstVoltages: List[SvEstVoltage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Fault(IdentifiedObject):
    """
    Abnormal condition causing current flow through conducting equipment, such
    as caused by equipment failure or short circuits from objects not typically
    modeled (for example, a tree falling on a line).

    :ivar kind: The kind of phase fault.
    :ivar occurredDateTime: The date and time at which the fault
        occurred.
    :ivar phases: The phases participating in the fault. The fault
        connections into these phases are further specified by the type
        of fault.
    :ivar stopDateTime: Time when the fault is repaired. If not
        specified, the fault is temporary and will clear itself as soon
        as it's deenergized.
    :ivar FaultCauseTypes: All types of fault cause.
    :ivar FaultyEquipment: Equipment carrying this fault.
    :ivar impedance: Fault impedance. Its usage is described by 'kind'.
    :ivar Location:
    """
    kind: Optional[PhaseConnectedFaultKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    occurredDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    phases: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    stopDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    FaultCauseTypes: List[FaultCauseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    FaultyEquipment: Optional["Equipment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    impedance: Optional[FaultImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Location: Optional["Location"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class House(IdentifiedObject):
    """In GridLAB-D, a single-family residence with building envelope
    represented by the equivalent thermal parameter (ETP) model, heating,
    ventilating and air conditioning (HVAC), other appliances, lights and plug
    loads.

    In power flow, these house loads aggregate into ZIP loads. These
    house parameters are the minimal set required to consistently
    initialize or repeat a GridLAB-D simulation.
    """
    coolingSetpoint: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    coolingSystem: Optional[HouseCooling] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    floorArea: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    heatingSetpoint: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    heatingSystem: Optional[HouseHeating] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    hvacPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    numberOfStories: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    ServicePanel: Optional["EnergyConsumer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    ThermostatController: Optional[ThermostatController] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class NoLoadTest(TransformerTest):
    """No-load test results determine core admittance parameters.

    They include exciting current and core loss measurements from
    applying voltage to one winding. The excitation may be positive
    sequence or zero sequence. The test may be repeated at different
    voltages to measure saturation.

    :ivar energisedEndVoltage: Voltage applied to the winding (end)
        during test.
    :ivar excitingCurrent: Exciting current measured from a positive-
        sequence or single-phase excitation test.
    :ivar excitingCurrentZero: Exciting current measured from a zero-
        sequence open-circuit excitation test.
    :ivar loss: Losses measured from a positive-sequence or single-phase
        excitation test.
    :ivar lossZero: Losses measured from a zero-sequence excitation
        test.
    :ivar EnergisedEnd: Transformer end that current is applied to in
        this no-load test.
    """
    energisedEndVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    excitingCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    excitingCurrentZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    loss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lossZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergisedEnd: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class OpenCircuitTest(TransformerTest):
    """Open-circuit test results verify winding turn ratios and phase shifts.

    They include induced voltage and phase shift measurements on open-
    circuit windings, with voltage applied to the energised end. For
    three-phase windings, the excitation can be a positive sequence (the
    default) or a zero sequence.

    :ivar energisedEndStep: Tap step number for the energised end of the
        test pair.
    :ivar energisedEndVoltage: Voltage applied to the winding (end)
        during test.
    :ivar openEndStep: Tap step number for the open end of the test
        pair.
    :ivar openEndVoltage: Voltage measured at the open-circuited end,
        with the energised end set to rated voltage and all other ends
        open.
    :ivar phaseShift: Phase shift measured at the open end with the
        energised end set to rated voltage and all other ends open.
    :ivar EnergisedEnd: Transformer end that current is applied to in
        this open-circuit test.
    :ivar OpenEnd: Transformer end measured for induced voltage and
        angle in this open-circuit test.
    """
    energisedEndStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energisedEndVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    openEndStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    openEndVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phaseShift: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergisedEnd: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    OpenEnd: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class OperationalLimit(IdentifiedObject):
    """A value associated with a specific kind of limit.

    The sub class value attribute shall be positive. The sub class value
    attribute is inversely proportional to
    OperationalLimitType.acceptableDuration (acceptableDuration for
    short). A pair of value_x and acceptableDuration_x are related to
    each other as follows: if value_1 &amp;gt; value_2 &amp;gt; value_3
    &amp;gt;... then acceptableDuration_1 &amp;lt; acceptableDuration_2
    &amp;lt; acceptableDuration_3 &amp;lt; ... A value_x with
    direction="high" shall be greater than a value_y with
    direction="low".

    :ivar OperationalLimitSet:
    :ivar OperationalLimitType: The limit type associated with this
        limit.
    """
    OperationalLimitSet: Optional["OperationalLimitSet"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    OperationalLimitType: Optional[OperationalLimitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class OverfrequencyTripCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class OvervoltageTripCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PerLengthImpedance(PerLengthLineParameter):
    """
    Common type for per-length impedance electrical catalogues.

    :ivar ACLineSegments: All line segments described by this per-length
        impedance.
    """
    ACLineSegments: List["ACLineSegment"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class RegularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them is constant.

    :ivar endTime: The time for the last time point.  The value can be a
        time of day, not a specific date.
    :ivar timeStep: The time between each pair of subsequent regular
        time points in sequence order.
    :ivar TimePoints: The regular interval time point data values that
        define this schedule.
    """
    endTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    timeStep: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TimePoints: List[RegularTimePoint] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class ShortCircuitTest(TransformerTest):
    """Short-circuit test results determine mesh impedance parameters.

    They include load losses and leakage impedances. For three-phase
    windings, the excitation can be a positive sequence (the default) or
    a zero sequence. There shall be at least one grounded winding.

    :ivar energisedEndStep: Tap step number for the energised end of the
        test pair.
    :ivar groundedEndStep: Tap step number for the grounded end of the
        test pair.
    :ivar leakageImpedance: Leakage impedance measured from a positive-
        sequence or single-phase short-circuit test.
    :ivar leakageImpedanceZero: Leakage impedance measured from a zero-
        sequence short-circuit test.
    :ivar loss: Load losses from a positive-sequence or single-phase
        short-circuit test.
    :ivar lossZero: Load losses from a zero-sequence short-circuit test.
    :ivar EnergisedEnd: Transformer end that voltage is applied to in
        this short-circuit test. The test voltage is chosen to induce
        rated current in the energised end.
    :ivar GroundedEnds: All ends short-circuited in this short-circuit
        test.
    """
    energisedEndStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    groundedEndStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    leakageImpedance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    leakageImpedanceZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    loss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lossZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergisedEnd: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    GroundedEnds: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class SubGeographicalRegion(IdentifiedObject):
    """
    A subset of a geographical region of a power system network model.

    :ivar Region: The geographical region to which this sub-geographical
        region is within.
    :ivar Substations: The substations in this sub-geographical region.
    """
    Region: Optional[GeographicalRegion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Substations: List["Substation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TransformerEnd(IdentifiedObject):
    """A conducting connection point of a power transformer.

    It corresponds to a physical transformer winding terminal.  In
    earlier CIM versions, the TransformerWinding class served a similar
    purpose, but this class is more flexible because it associates to
    terminal but is not a specialization of ConductingEquipment.

    :ivar endNumber: Number for this transformer end, corresponding to
        the end's order in the power transformer vector group or phase
        angle clock number.  Highest voltage winding should be 1.  Each
        end within a power transformer should have a unique subsequent
        end number.   Note the transformer end number need not match the
        terminal sequence number.
    :ivar grounded: (for Yn and Zn connections) True if the neutral is
        solidly grounded.
    :ivar rground: (for Yn and Zn connections) Resistance part of
        neutral impedance where 'grounded' is true.
    :ivar xground: (for Yn and Zn connections) Reactive part of neutral
        impedance where 'grounded' is true.
    :ivar BaseVoltage: Base voltage of the transformer end.  This is
        essential for PU calculation.
    :ivar CoreAdmittance: Core admittance of this transformer end,
        representing magnetising current and core losses. The full
        values of the transformer should be supplied for one transformer
        end only.
    :ivar FromMeshImpedance: All mesh impedances between this 'to' and
        other 'from' transformer ends.
    :ivar PhaseTapChanger: Phase tap changer associated with this
        transformer end.
    :ivar RatioTapChanger: Ratio tap changer associated with this
        transformer end.
    :ivar Terminal: Terminal of the power transformer to which this
        transformer end belongs.
    :ivar ToMeshImpedance: All mesh impedances between this 'from' and
        other 'to' transformer ends.
    """
    endNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rground: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    xground: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    BaseVoltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    CoreAdmittance: Optional[TransformerCoreAdmittance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    FromMeshImpedance: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PhaseTapChanger: Optional["PhaseTapChanger"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RatioTapChanger: Optional["RatioTapChanger"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ToMeshImpedance: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class UnderfrequencyTripCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class UndervoltageTripCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltVarCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltWattCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WattVarCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class BaseVoltage(IdentifiedObject):
    """
    Defines a system base voltage which is referenced.

    :ivar nominalVoltage: The power system resource's base voltage.
    :ivar ConductingEquipment: All conducting equipment with this base
        voltage.  Use only when there is no voltage level container used
        and only one base voltage applies.  For example, not used for
        transformers.
    :ivar TopologicalNode: The topological nodes at the base voltage.
    :ivar TransformerEnds: Transformer ends at the base voltage.  This
        is essential for PU calculation.
    """
    nominalVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ConductingEquipment: List["ConductingEquipment"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TopologicalNode: List["TopologicalNode"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TransformerEnds: List[TransformerEnd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DERIEEEType1(DERDynamics):
    """DER model with behavior defined in IEEE 1547-2018.

    If DERDynamics.RemoteInputSignal is not provided, applicable
    voltages are measured at the Terminal of the associated
    PowerElectronicsConnection, SynchronousMachine, or
    AsynchronousMachine.  Otherwise, applicable voltages are measured at
    RemoteInputSignal.Terminal.  The applicable voltages are selected
    from all phase-to-phase, all phase-to-neutral, and all phase-to-
    ground voltages at the applicable Terminal, depending on grounding,
    wiring, and voltage level at the point of common coupling. The
    determination of grounding must account for the effect of any
    interconnection transformer, not just the associated
    PowerElectronicsConnection, SynchronousMachine, or
    AsynchronousMachine.  The VoltageTripSettings use the minimum (for
    uv) or maximum (for ov) applicable voltage.  The VoltVar and
    VoltWatt settings use the average applicable voltage.

    :ivar phaseToGroundApplicable: Indicates whether the DER uses phase-
        to-ground applicable voltages.
    :ivar phaseToNeutralApplicable: Indicates whether the DER uses
        phase-to-neutral applicable voltages.
    :ivar phaseToPhaseApplicable: Indicates whether the DER uses phase-
        to-phase applicable voltages.
    :ivar ConstantPowerFactorSettings: Constant power factor settings
        with which this DER IEEE type 1 model is associated.
    :ivar ConstantReactivePowerSettings: Constant reactive power
        settings with which this DER IEEE type 1 model is associated.
    :ivar DerNameplateData: DER nameplate data with which this DER IEEE
        type 1 model is associated.
    :ivar FrequencyDroopSettings: Frequency droop dettings with which
        this DER IEEE type 1 model is associated.
    :ivar FrequencyTripSettings: Frequency trip settings with which this
        DER IEEE type 1 model is associated.
    :ivar MomentaryCessationSettings: Momentary cessation settings with
        which this DER IEEE type 1 model is associated.
    :ivar PowerLimitSettings: Power limit settings with which this DER
        IEEE type 1 model is associated.
    :ivar ServiceSettings: Service settings with which this DER IEEE
        type 1 model is associated.
    :ivar VoltageTripSettings: Voltage trip settings with which this DER
        IEEE type 1 model is associated.
    :ivar VoltVarSettings: Volt var settings with which this DER IEEE
        type 1 model is associated.
    :ivar VoltWattSettings: Volt watt settings with which this DER IEEE
        type 1 model is associated.
    :ivar WattVarSettings: Watt var settings with which this DER IEEE
        type 1 model is associated.
    """
    phaseToGroundApplicable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    phaseToNeutralApplicable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    phaseToPhaseApplicable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    ConstantPowerFactorSettings: Optional["ConstantPowerFactorSettings"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ConstantReactivePowerSettings: Optional[ConstantReactivePowerSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DerNameplateData: Optional[DERNameplateData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    FrequencyDroopSettings: Optional[FrequencyDroopSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    FrequencyTripSettings: Optional[FrequencyTripSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    MomentaryCessationSettings: Optional[MomentaryCessationSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerLimitSettings: Optional[PowerLimitSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ServiceSettings: Optional[ServiceSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    VoltageTripSettings: Optional[VoltageTripSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    VoltVarSettings: Optional[VoltVarSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    VoltWattSettings: Optional[VoltWattSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WattVarSettings: Optional[WattVarSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EquipmentFault(Fault):
    """A fault applied at the terminal, external to the equipment.

    This class is not used to specify faults internal to the equipment.

    :ivar Terminal: The terminal connecting to the bus to which the
        fault is applied.
    """
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class IEEE1547Setting:
    constantPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    constantReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceIntentionalDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceMaxFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceMaxVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceMinFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enterServiceMinVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    frequencyDroopResponseTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    islandClearingTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    openLoopResponseTimeP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    overFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    overFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    timeConstantOpenLoop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    timeConstantReferenceVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    underFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    underFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OverfrequencyTripCurve: Optional[OverfrequencyTripCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OvervoltageTripCurve: Optional[OvervoltageTripCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerElectronicsConnections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RotatingMachines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UnderfrequencyTripCurve: Optional[UnderfrequencyTripCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UndervoltageTripCurve: Optional[UndervoltageTripCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    VoltVarCurve: Optional[VoltVarCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    VoltWattCurve: Optional[VoltWattCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WattVarCurve: Optional[WattVarCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Location(IdentifiedObject):
    """The place, scene, or point of something where someone or something has
    been, is, and/or will be at a given moment in time.

    It can be defined with one or more postition points (coordinates) in
    a given coordinate system.

    :ivar Assets: All assets at this location.
    :ivar CoordinateSystem: Coordinate system used to describe position
        points of this location.
    :ivar Fault:
    :ivar Measurements:
    :ivar PowerSystemResources: All power system resources at this
        location.
    """
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    CoordinateSystem: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Fault: List[Fault] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Measurements: List["Measurement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerSystemResources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PerLengthSequenceImpedance(PerLengthImpedance):
    """Sequence impedance and admittance parameters per unit length, for
    transposed lines of 1, 2, or 3 phases.

    For 1-phase lines, define x=x0=xself. For 2-phase lines, define
    x=xs-xm and x0=xs+xm.

    :ivar b0ch: Zero sequence shunt (charging) susceptance, per unit of
        length.
    :ivar bch: Positive sequence shunt (charging) susceptance, per unit
        of length.
    :ivar g0ch: Zero sequence shunt (charging) conductance, per unit of
        length.
    :ivar gch: Positive sequence shunt (charging) conductance, per unit
        of length.
    :ivar r: Positive sequence series resistance, per unit of length.
    :ivar r0: Zero sequence series resistance, per unit of length.
    :ivar x: Positive sequence series reactance, per unit of length.
    :ivar x0: Zero sequence series reactance, per unit of length.
    """
    b0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    bch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    g0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    gch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PowerTransformerEnd(TransformerEnd):
    """A PowerTransformerEnd is associated with each Terminal of a
    PowerTransformer.

    The impedance values r, r0, x, and x0 of a PowerTransformerEnd
    represents a star equivalent as follows 1) for a two Terminal
    PowerTransformer the high voltage (TransformerEnd.endNumber=1)
    PowerTransformerEnd has non zero values on r, r0, x, and x0 while
    the low voltage (TransformerEnd.endNumber=0) PowerTransformerEnd has
    zero values for r, r0, x, and x0. 2) for a three Terminal
    PowerTransformer the three PowerTransformerEnds represents a star
    equivalent with each leg in the star represented by r, r0, x, and x0
    values. 3) For a three Terminal transformer each PowerTransformerEnd
    shall have g, g0, b and b0 values corresponding the no load losses
    distributed on the three PowerTransformerEnds. The total no load
    loss shunt impedances may also be placed at one of the
    PowerTransformerEnds, preferably the end numbered 1, having the
    shunt values on end 1 is the preferred way. 4) for a
    PowerTransformer with more than three Terminals the
    PowerTransformerEnd impedance values cannot be used. Instead use the
    TransformerMeshImpedance or split the transformer into multiple
    PowerTransformers.

    :ivar connectionKind: Kind of connection.
    :ivar phaseAngleClock: Terminal voltage phase angle displacement
        where 360 degrees are represented with clock hours. The valid
        values are 0 to 11. For example, for the secondary side end of a
        transformer with vector group code of 'Dyn11', specify the
        connection kind as wye with neutral and specify the phase angle
        of the clock as 11.  The clock value of the transformer end
        number specified as 1, is assumed to be zero.  Note the
        transformer end number is not assumed to be the same as the
        terminal sequence number.
    :ivar r: Resistance (star-model) of the transformer end. The
        attribute shall be equal or greater than zero for non-equivalent
        transformers.
    :ivar ratedS: Normal apparent power rating. The attribute shall be a
        positive value. For a two-winding transformer the values for the
        high and low voltage sides shall be identical.
    :ivar ratedU: Rated voltage: phase-phase for three-phase windings,
        and either phase-phase or phase-neutral for single-phase
        windings. A high voltage side, as given by
        TransformerEnd.endNumber, shall have a ratedU that is greater or
        equal than ratedU for the lower voltage sides.
    :ivar PowerTransformer: The power transformer of this power
        transformer end.
    """
    connectionKind: Optional[WindingConnection] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phaseAngleClock: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerTransformer: Optional["PowerTransformer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """
    A time schedule covering a 24 hour period, with curve data for a specific
    type of season and day.

    :ivar DayType: DayType for the Schedule.
    :ivar Season: Season for the Schedule.
    """
    DayType: Optional[DayType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Season: Optional[Season] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TransformerTankEnd(TransformerEnd):
    """
    Transformer tank end represents an individual winding for unbalanced models
    or for transformer tanks connected into a bank (and bank is modelled with
    the PowerTransformer).

    :ivar orderedPhases: Identifies the phases present and the order of
        their connection on this winding (end) of the transformer. In
        some use cases, such as open-wye, open-delta transformers and
        single-phase, center-tap secondary transformers, the order of
        phase connection is important, so the OrderedPhaseCodeKind
        enumeration is used instead of PhaseCode.
    :ivar TransformerTank: Transformer this winding belongs to.
    """
    orderedPhases: Optional[OrderedPhaseCodeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TransformerTank: Optional["TransformerTank"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConstantPowerFactorSettings(IdentifiedObject):
    """Constant Power Factor Settings.

    Reference: IEEE1547-2018.

    :ivar constantPowerFactorExcitationKind: Under or over excited
        (CONST_PF_EXCITATION). Typical value
        =ConstantPowerFactorSettingKind.inj.
    :ivar enabled: Constant power factor mode select
        (CONST_PF_MODE_ENABLE). True means enabled. False means
        disabled. Typical value = true.
    :ivar powerFactor: Power factor setting (CONST_PF). Typical value =
        1.
    :ivar DERIEEEType1: DER IEEE type 1 model associated with this
        constant power factor settings model.
    """
    constantPowerFactorExcitationKind: Optional[ConstantPowerFactorSettingKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    powerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERIEEEType1: Optional[DERIEEEType1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PowerSystemResource(IdentifiedObject):
    """A power system resource can be an item of equipment such as a switch, an
    equipment container containing many individual items of equipment such as a
    substation, or an organisational entity such as sub-control area.

    Power system resources can have measurements associated.

    :ivar AssetDatasheet: Datasheet information for this power system
        resource.
    :ivar Assets: All assets represented by this power system resource.
        For example, multiple conductor assets are electrically modelled
        as a single AC line segment.
    :ivar Controls: The controller outputs used to actually govern a
        regulating device, e.g. the magnetization of a synchronous
        machine or capacitor bank breaker actuator.
    :ivar Location: Location of this power system resource.
    :ivar Measurements: The measurements associated with this power
        system resource.
    """
    AssetDatasheet: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Controls: List[Control] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Measurements: List["Measurement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class RegulationSchedule(SeasonDayTypeSchedule):
    """
    A pre-established pattern over time for a controlled variable, e.g., busbar
    voltage.

    :ivar RegulatingControl: Regulating controls that have this
        Schedule.
    :ivar VoltageControlZones: A VoltageControlZone may have a  voltage
        regulation schedule.
    """
    RegulatingControl: Optional["RegulatingControl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    VoltageControlZones: List["VoltageControlZone"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TapSchedule(SeasonDayTypeSchedule):
    """
    A pre-established pattern over time for a tap step.

    :ivar TapChanger: A TapSchedule is associated with a TapChanger.
    """
    TapChanger: Optional["TapChanger"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class TopologicalNode(IdentifiedObject):
    """For a detailed substation model a topological node is a set of
    connectivity nodes that, in the current network state, are connected
    together through any type of closed switches, including  jumpers.

    Topological nodes change as the current network state changes (i.e.,
    switches, breakers, etc. change state). For a planning model, switch
    statuses are not used to form topological nodes. Instead they are
    manually created or deleted in a model builder tool. Topological
    nodes maintained this way are also called "busses".

    :ivar pInjection: The active power injected into the bus at this
        location in addition to injections from equipment.  Positive
        sign means injection into the TopologicalNode (bus). Starting
        value for a steady state solution.
    :ivar qInjection: The reactive power injected into the bus at this
        location in addition to injections from equipment. Positive sign
        means injection into the TopologicalNode (bus). Starting value
        for a steady state solution.
    :ivar BaseVoltage: The base voltage of the topologocial node.
    :ivar ConnectivityNodeContainer: The connectivity node container to
        which the toplogical node belongs.
    :ivar ConnectivityNodes: The connectivity nodes combine together to
        form this topological node.  May depend on the current state of
        switches in the network.
    :ivar SvVoltage: The state voltage associated with the topological
        node.
    :ivar Terminal: The terminals associated with the topological node.
        This can be used as an alternative to the connectivity node path
        to terminal, thus making it unneccesary to model connectivity
        nodes in some cases.   Note that if connectivity nodes are in
        the model, this association would probably not be used as an
        input specification.
    :ivar TopologicalIsland: A topological node belongs to a topological
        island.
    """
    pInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    qInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    BaseVoltage: Optional[BaseVoltage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ConnectivityNodeContainer: Optional["ConnectivityNodeContainer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ConnectivityNodes: List["ConnectivityNode"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SvVoltage: List[SvVoltage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Terminal: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TopologicalIsland: Optional[TopologicalIsland] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class AssetInfo(IdentifiedObject):
    """Set of attributes of an asset, representing typical datasheet
    information of a physical device that can be instantiated and shared in
    different data exchange contexts:

    - as attributes of an asset instance (installed or in stock)
    - as attributes of an asset model (product by a manufacturer)
    - as attributes of a type asset (generic type of an asset as used in designs/extension planning).

    :ivar Assets: All assets described by this data.
    :ivar PowerSystemResources: All power system resources with this
        datasheet information.
    """
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerSystemResources: List[PowerSystemResource] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConnectivityNodeContainer(PowerSystemResource):
    """
    A base class for all objects that may contain connectivity nodes or
    topological nodes.

    :ivar ConnectivityNodes: Connectivity nodes which belong to this
        connectivity node container.
    :ivar TopologicalNode: The topological nodes which belong to this
        connectivity node container.
    """
    ConnectivityNodes: List["ConnectivityNode"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TopologicalNode: List[TopologicalNode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EnergyConsumerPhase(PowerSystemResource):
    """
    A single phase of an energy consumer.

    :ivar p: Active power of the load. Load sign convention is used,
        i.e. positive sign means flow out from a node. For voltage
        dependent loads the value is at rated voltage. Starting value
        for a steady state solution.
    :ivar phase: Phase of this energy consumer component.   If the
        energy consumer is wye connected, the connection is from the
        indicated phase to the central ground or neutral point.  If the
        energy consumer is delta connected, the phase indicates an
        energy consumer connected from the indicated phase to the next
        logical non-neutral phase.
    :ivar q: Reactive power of the load. Load sign convention is used,
        i.e. positive sign means flow out from a node. For voltage
        dependent loads the value is at rated voltage. Starting value
        for a steady state solution.
    :ivar EnergyConsumer: The energy consumer to which this phase
        belongs.
    """
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergyConsumer: Optional["EnergyConsumer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class EnergySourcePhase(PowerSystemResource):
    """
    Represents the single phase information of an unbalanced energy source.

    :ivar phase: Phase of this energy source component.   If the energy
        source wye connected, the connection is from the indicated phase
        to the central ground or neutral point.  If the energy source is
        delta connected, the phase indicates an energy source connected
        from the indicated phase to the next logical non-neutral phase.
    :ivar EnergySource: The energy sourceto which the phase belongs.
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergySource: Optional["EnergySource"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class PowerCutZone(PowerSystemResource):
    """
    An area or zone of the power system which is used for load shedding
    purposes.

    :ivar cutLevel1: First level (amount) of load to cut as a percentage
        of total zone load.
    :ivar cutLevel2: Second level (amount) of load to cut as a
        percentage of total zone load.
    :ivar EnergyConsumers: Energy consumer is assigned to the power cut
        zone.
    """
    cutLevel1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    cutLevel2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergyConsumers: List["EnergyConsumer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class PowerElectronicsConnectionPhase(PowerSystemResource):
    """
    :ivar p: Active power injection. Load sign convention is used, i.e.
        positive sign means flow into the equipment from the network.
    :ivar phase: Phase of this energy producer component.   If the
        energy producer is wye connected, the connection is from the
        indicated phase to the central ground or neutral point.  If the
        energy producer is delta connected, the phase indicates an
        energy producer connected from the indicated phase to the next
        logical non-neutral phase.
    :ivar q: Reactive power injection. Load sign convention is used,
        i.e. positive sign means flow into the equipment from the
        network.
    :ivar PowerElectronicsConnection:
    """
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerElectronicsConnection: Optional["PowerElectronicsConnection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class RegulatingControl(PowerSystemResource):
    """Specifies a set of equipment that works together to control a power
    system quantity such as voltage or flow.

    Remote bus voltage control is possible by specifying the controlled
    terminal located at some place remote from the controlling
    equipment. In case multiple equipment, possibly of different types,
    control same terminal there must be only one RegulatingControl at
    that terminal. The most specific subtype of RegulatingControl shall
    be used in case such equipment participate in the control, e.g.
    TapChangerControl for tap changers. For flow control  load sign
    convention is used, i.e. positive sign means flow out from a
    TopologicalNode (bus) into the conducting equipment.

    :ivar discrete: The regulation is performed in a discrete mode. This
        applies to equipment with discrete controls, e.g. tap changers
        and shunt compensators.
    :ivar enabled: The flag tells if regulation is enabled.
    :ivar mode: The regulating control mode presently available.  This
        specification allows for determining the kind of regulation
        without need for obtaining the units from a schedule.
    :ivar monitoredPhase: Phase voltage controlling this regulator,
        measured at regulator location.
    :ivar targetDeadband: This is a deadband used with discrete control
        to avoid excessive update of controls like tap changers and
        shunt compensator banks while regulating. The units of those
        appropriate for the mode.
    :ivar targetValue: The target value specified for case input.   This
        value can be used for the target value without the use of
        schedules. The value has the units appropriate to the mode
        attribute.
    :ivar RegulationSchedule: Schedule for this Regulating regulating
        control.
    :ivar Terminal: The terminal associated with this regulating
        control.  The terminal is associated instead of a node, since
        the terminal could connect into either a topological node (bus
        in bus-branch model) or a connectivity node (detailed switch
        model).  Sometimes it is useful to model regulation at a
        terminal of a bus bar object since the bus bar can be present in
        both a bus-branch model or a model with switch detail.
    """
    discrete: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    mode: Optional[RegulatingControlModeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    monitoredPhase: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    targetDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    targetValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RegulationSchedule: List[RegulationSchedule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ShuntCompensatorPhase(PowerSystemResource):
    """
    Single phase of a multi-phase shunt compensator when its attributes might
    be different per phase.

    :ivar maximumSections: The maximum number of sections that may be
        switched in for this phase.
    :ivar normalSections: For the capacitor phase, the normal number of
        sections switched in.
    :ivar phase: Phase of this shunt compensator component.   If the
        shunt compensator is wye connected, the connection is from the
        indicated phase to the central ground or neutral point.  If the
        shunt compensator is delta connected, the phase indicates a
        shunt compensator connected from the indicated phase to the next
        logical non-neutral phase.
    :ivar sections: Number of sections in use for this phase, when
        controlled independently from the other phases. If not provided,
        may default to the parent ShuntCompensator.sections value (see
        ShuntCompensator documentation for more details).
    :ivar ShuntCompensator: Shunt compensator of this shunt compensator
        phase.
    """
    maximumSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normalSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sections: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ShuntCompensator: Optional["ShuntCompensator"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class SvInjection(StateVariable):
    """The SvInjection is reporting the calculated bus injection minus the sum
    of the terminal flows.

    The terminal flow is positive out from the bus (load sign
    convention) and bus injection has positive flow into the bus.
    SvInjection may have the remainder after state estimation or slack
    after power flow calculation.

    :ivar phase: The terminal phase at which the connection is applied.
        If missing, the injection is assumed to be balanced among non-
        neutral phases.
    :ivar pInjection: The active power mismatch between calculated
        injection and initial injection.  Positive sign means injection
        into the TopologicalNode (bus).
    :ivar qInjection: The reactive power mismatch between calculated
        injection and initial injection.  Positive sign means injection
        into the TopologicalNode (bus).
    :ivar ConnectivityNode:
    :ivar TopologicalNode: The topological node associated with the flow
        injection state variable.
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    qInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ConnectivityNode: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    TopologicalNode: Optional[TopologicalNode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class TapChanger(PowerSystemResource):
    """
    Mechanism for changing transformer winding tap positions.

    :ivar controlEnabled: Specifies the regulation status of the
        equipment.  True is regulating, false is not regulating.
    :ivar ctRating:
    :ivar ctRatio:
    :ivar highStep: Highest possible tap step position, advance from
        neutral. The attribute shall be greater than lowStep.
    :ivar initialDelay: For an LTC, the delay for initial tap changer
        operation (first step change)
    :ivar lowStep: Lowest possible tap step position, retard from
        neutral
    :ivar ltcFlag: Specifies whether or not a TapChanger has load tap
        changing capabilities.
    :ivar neutralStep: The neutral tap step position for this winding.
        The attribute shall be equal or greater than lowStep and equal
        or less than highStep.
    :ivar neutralU: Voltage at which the winding operates at the neutral
        tap setting.
    :ivar normalStep: The tap step position used in "normal" network
        operation for this winding. For a "Fixed" tap changer indicates
        the current physical tap setting. The attribute shall be equal
        or greater than lowStep and equal or less than highStep.
    :ivar ptRatio:
    :ivar step: Tap changer position. Starting step for a steady state
        solution. Non integer values are allowed to support continuous
        tap variables. The reasons for continuous value are to support
        study cases where no discrete tap changers has yet been
        designed, a solutions where a narrow voltage band force the tap
        step to oscillate or accommodate for a continuous solution as
        input. The attribute shall be equal or greater than lowStep and
        equal or less than highStep.
    :ivar subsequentDelay: For an LTC, the delay for subsequent tap
        changer operation (second and later step changes)
    :ivar SvTapStep: The tap step state associated with the tap changer.
    :ivar TapChangerControl: The regulating control scheme in which this
        tap changer participates.
    :ivar TapSchedules: A TapChanger can have TapSchedules.
    """
    controlEnabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ctRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ctRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    highStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    initialDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lowStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ltcFlag: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutralStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutralU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normalStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ptRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    step: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    subsequentDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SvTapStep: Optional[SvTapStep] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TapChangerControl: Optional["TapChangerControl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TapSchedules: List[TapSchedule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltageControlZone(PowerSystemResource):
    """An area of the power system network which is defined for secondary
    voltage control purposes.

    A voltage control zone consists of a collection of substations with
    a designated bus bar section whose voltage will be controlled.

    :ivar BusbarSection: A VoltageControlZone is controlled by a
        designated BusbarSection.
    :ivar RegulationSchedule: A VoltageControlZone may have a  voltage
        regulation schedule.
    """
    BusbarSection: Optional["BusbarSection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    RegulationSchedule: Optional["RegulationSchedule"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Asset(IdentifiedObject):
    """Tangible resource of the utility, including power system equipment,
    various end devices, cabinets, buildings, etc.

    For electrical network equipment, the role of the asset is defined
    through PowerSystemResource and its subclasses, defined mainly in
    the Wires model (refer to IEC61970-301 and model package
    IEC61970::Wires). Asset description places emphasis on the physical
    characteristics of the equipment fulfilling that role.

    :ivar AssetInfo: Data applicable to this asset.
    :ivar Location: Location of this asset.
    :ivar Measurements:
    :ivar PowerSystemResources: All power system resources used to
        electrically model this asset. For example, transformer asset is
        electrically modelled with a transformer and its windings and
        tap changer.
    :ivar ScheduledEvents:
    """
    AssetInfo: Optional[AssetInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Measurements: List["Measurement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerSystemResources: List[PowerSystemResource] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ScheduledEvents: List[ScheduledEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class BusbarSectionInfo(AssetInfo):
    """
    Busbar section data.

    :ivar ratedCurrent: Rated current.
    :ivar ratedVoltage: Rated voltage.
    """
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConnectivityNode(IdentifiedObject):
    """
    Connectivity nodes are points where terminals of AC conducting equipment
    are connected together with zero impedance.

    :ivar ConnectivityNodeContainer: Container of this connectivity
        node.
    :ivar OperationalLimitSet:
    :ivar SvInjection:
    :ivar SvVoltage:
    :ivar Terminals: Terminals interconnected with zero impedance at a
        this connectivity node.
    :ivar TopologicalNode: The topological node to which this
        connectivity node is assigned.  May depend on the current state
        of switches in the network.
    """
    ConnectivityNodeContainer: Optional["ConnectivityNodeContainer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    OperationalLimitSet: List["OperationalLimitSet"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SvInjection: List[SvInjection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SvVoltage: Optional[SvVoltage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Terminals: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TopologicalNode: Optional[TopologicalNode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceInfo(AssetInfo):
    """
    End device data.

    :ivar isSolidState: If true, this is a solid state end device (as
        opposed to a mechanical or electromechanical device).
    :ivar phaseCount: Number of potential phases the end device
        supports, typically 0, 1 or 3.
    :ivar ratedCurrent: Rated current.
    :ivar ratedVoltage: Rated voltage.
    :ivar capability: Inherent capabilities of the device (i.e., the
        functions it supports).
    :ivar EndDevices: All end devices described with this data.
    """
    isSolidState: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phaseCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    capability: Optional[EndDeviceCapability] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDevices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EquipmentContainer(ConnectivityNodeContainer):
    """
    A modeling construct to provide a root class for containing equipment.

    :ivar AdditionalGroupedEquipment: The additonal contained equipment.
        The equipment belong to the equipment container. The equipment
        is contained in another equipment container, but also grouped
        with this equipment container.  Examples include when a switch
        contained in a substation is also desired to be grouped with a
        line contianer or when a switch is included in a secondary
        substation and also grouped in a feeder.
    :ivar Equipments: Contained equipment.
    """
    AdditionalGroupedEquipment: List["Equipment"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Equipments: List["Equipment"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class IEEE1547Info(AssetInfo):
    abnormalPerformanceCategory: Optional[IEEE1547AbnormalPerfomanceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    islandingCategory: Optional[IEEE1547IslandingCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maximumU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minimumU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normalPerformanceCategory: Optional[IEEE1547NormalPerformanceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    overExcitedPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedPatUnityPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedPcharge: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedPoverExcited: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedPunderExcited: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedQabsorbed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedQinjected: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedScharge: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    serialNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsDynamicReactiveCurrent: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsIEC61850: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsIEEE1815: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsIEEE20305: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsIslanding: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsSunSpecModBusEthernet: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsSunSpecModBusRS485: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsVoltWatt: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supportsWattVar: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    susceptanceCeaseToEnergize: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    underExcitedPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerElectronicsConnections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RotatingMachines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class LinearShuntCompensatorPhase(ShuntCompensatorPhase):
    """
    A per phase linear shunt compensator has banks or sections with equal
    admittance values.

    :ivar bPerSection: Susceptance per section of the phase if shunt
        compensator is wye connected.   Susceptance per section phase to
        phase if shunt compensator is delta connected.
    :ivar gPerSection: Conductance per section for this phase if shunt
        compensator is wye connected.  Conductance per section phase to
        phase if shunt compensator is delta connected.
    """
    bPerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    gPerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PhaseTapChanger(TapChanger):
    """A transformer phase shifting tap model that controls the phase angle
    difference across the power transformer and potentially the active power
    flow through the power transformer.

    This phase tap model may also impact the voltage magnitude.

    :ivar TransformerEnd: Transformer end to which this phase tap
        changer belongs.
    """
    TransformerEnd: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class PowerTransformerInfo(AssetInfo):
    """
    Set of power transformer data, from an equipment library.

    :ivar TransformerTankInfos: Data for all the tanks described by this
        power transformer data.
    """
    TransformerTankInfos: List["TransformerTankInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class RatioTapChanger(TapChanger):
    """
    A tap changer that changes the voltage ratio impacting the voltage
    magnitude but not the phase angle across the transformer.

    :ivar stepVoltageIncrement: Tap step increment, in per cent of
        neutral voltage, per step position. When the increment is
        negative, the voltage decreases when the tap step increases.
    :ivar TransformerEnd: Transformer end to which this ratio tap
        changer belongs.
    """
    stepVoltageIncrement: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TransformerEnd: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class ShuntCompensatorInfo(AssetInfo):
    """
    Properties of shunt capacitor, shunt reactor or switchable bank of shunt
    capacitor or reactor assets.

    :ivar maxPowerLoss: Maximum allowed apparent power loss.
    :ivar ratedCurrent: Rated current.
    :ivar ratedReactivePower: Rated reactive power.
    :ivar ratedVoltage: Rated voltage.
    """
    maxPowerLoss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class SwitchInfo(AssetInfo):
    """
    &amp;lt;was Switch data.&amp;gt; Switch datasheet information.

    :ivar breakingCapacity: The maximum fault current a breaking device
        can break safely under prescribed conditions of use.
    :ivar isSinglePhase: If true, it is a single phase switch.
    :ivar isUnganged: If true, the switch is not ganged (i.e., a switch
        phase may be operated separately from other phases).
    :ivar lowPressureAlarm: Gas or air pressure at or below which a low
        pressure alarm is generated.
    :ivar lowPressureLockOut: Gas or air pressure below which the
        breaker will not open.
    :ivar oilVolumePerTank: Volume of oil in each tank of bulk oil
        breaker.
    :ivar ratedCurrent: Rated current.
    :ivar ratedFrequency: Frequency for which switch is rated.
    :ivar ratedImpulseWithstandVoltage: Rated impulse withstand voltage,
        also known as BIL (Basic Impulse Level).
    :ivar ratedInterruptingTime: Switch rated interrupting time in
        seconds.
    :ivar ratedVoltage: Rated voltage.
    """
    breakingCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    isSinglePhase: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    isUnganged: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lowPressureAlarm: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lowPressureLockOut: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    oilVolumePerTank: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedImpulseWithstandVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedInterruptingTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TapChangerControl(RegulatingControl):
    """
    Describes behavior specific to tap changers, e.g. how the voltage at the
    end of a line varies with the load level and compensation of the voltage
    drop by tap adjustment.

    :ivar lineDropCompensation: If true, the line drop compensation is
        to be applied.
    :ivar lineDropR: Line drop compensator resistance setting for normal
        (forward) power flow.
    :ivar lineDropX: Line drop compensator reactance setting for normal
        (forward) power flow.
    :ivar maxLimitVoltage: Maximum allowed regulated voltage on the PT
        secondary, regardless of line drop compensation. Sometimes
        referred to as first-house protection.
    :ivar minLimitVoltage:
    :ivar reverseLineDropR: Line drop compensator resistance setting for
        reverse power flow.
    :ivar reverseLineDropX: Line drop compensator reactance setting for
        reverse power flow.
    :ivar TapChanger: The tap changers that participates in this
        regulating tap control scheme.
    """
    lineDropCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lineDropR: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lineDropX: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maxLimitVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minLimitVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reverseLineDropR: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reverseLineDropX: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TapChanger: List["TapChanger"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TapChangerInfo(AssetInfo):
    """
    Tap changer data.

    :ivar ctRating: Built-in current transformer primary rating.
    :ivar ctRatio: Built-in current transducer ratio.
    :ivar ptRatio: Built-in voltage transducer ratio.
    """
    ctRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ctRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ptRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TransformerEndInfo(AssetInfo):
    """
    Transformer end data.

    :ivar connectionKind: Kind of connection.
    :ivar emergencyS: Apparent power that the winding can carry under
        emergency conditions (also called long-term emergency power).
    :ivar endNumber: Number for this transformer end, corresponding to
        the end's order in the PowerTransformer.vectorGroup attribute.
        Highest voltage winding should be 1.
    :ivar insulationU: Basic insulation level voltage rating.
    :ivar phaseAngleClock: Winding phase angle where 360 degrees are
        represented with clock hours, so the valid values are {0, ...,
        11}. For example, to express the second winding in code 'Dyn11',
        set attributes as follows: 'endNumber'=2, 'connectionKind' = Yn
        and 'phaseAngleClock' = 11.
    :ivar r: DC resistance.
    :ivar ratedS: Normal apparent power rating.
    :ivar ratedU: Rated voltage: phase-phase for three-phase windings,
        and either phase-phase or phase-neutral for single-phase
        windings.
    :ivar shortTermS: Apparent power that this winding can carry for a
        short period of time (in emergency).
    :ivar CoreAdmittance: Core admittance calculated from this
        transformer end datasheet, representing magnetising current and
        core losses. The full values of the transformer should be
        supplied for one transformer end info only.
    :ivar EnergisedEndNoLoadTests: All no-load test measurements in
        which this transformer end was energised.
    :ivar EnergisedEndOpenCircuitTests: All open-circuit test
        measurements in which this transformer end was excited.
    :ivar EnergisedEndShortCircuitTests: All short-circuit test
        measurements in which this transformer end was energised.
    :ivar FromMeshImpedances: All mesh impedances between this 'to' and
        other 'from' transformer ends.
    :ivar GroundedEndShortCircuitTests: All short-circuit test
        measurements in which this transformer end was short-circuited.
    :ivar OpenEndOpenCircuitTests: All open-circuit test measurements in
        which this transformer end was not excited.
    :ivar ToMeshImpedances: All mesh impedances between this 'from' and
        other 'to' transformer ends.
    :ivar TransformerTankInfo: Transformer tank data that this end
        description is part of.
    """
    connectionKind: Optional[WindingConnection] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    emergencyS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    endNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    insulationU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phaseAngleClock: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    shortTermS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    CoreAdmittance: Optional["TransformerCoreAdmittance"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergisedEndNoLoadTests: List[NoLoadTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergisedEndOpenCircuitTests: List[OpenCircuitTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergisedEndShortCircuitTests: List[ShortCircuitTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    FromMeshImpedances: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    GroundedEndShortCircuitTests: List[ShortCircuitTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OpenEndOpenCircuitTests: List[OpenCircuitTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ToMeshImpedances: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TransformerTankInfo: Optional["TransformerTankInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class TransformerTankInfo(AssetInfo):
    """
    Set of transformer tank data, from an equipment library.

    :ivar PowerTransformerInfo: Power transformer data that this tank
        description is part of.
    :ivar TransformerEndInfos: Data for all the ends described by this
        transformer tank data.
    :ivar TransformerTanks:
    """
    PowerTransformerInfo: Optional["PowerTransformerInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    TransformerEndInfos: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    TransformerTanks: List["TransformerTank"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WireSpacingInfo(AssetInfo):
    """Wire spacing data that associates multiple wire positions with the line
    segment, and allows to calculate line segment impedances.

    Number of phases can be derived from the number of associated wire
    positions whose phase is not neutral.

    :ivar isCable: If true, this spacing data describes a cable.
    :ivar phaseWireCount: Number of wire sub-conductors in the
        symmetrical bundle (typically between 1 and 4).
    :ivar phaseWireSpacing: Distance between wire sub-conductors in a
        symmetrical bundle.
    :ivar ACLineSegments:
    :ivar WireAssemblyInfo:
    :ivar WirePositions: All positions of single wires (phase or
        neutral) making the conductor.
    """
    isCable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phaseWireCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phaseWireSpacing: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ACLineSegments: List["ACLineSegment"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WireAssemblyInfo: List["WireAssemblyInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WirePositions: List[WirePosition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class ActivityRecord(IdentifiedObject):
    """
    Records activity for an entity at a point in time; activity may be for an
    event that has already occurred or for a planned activity.

    :ivar createdDateTime: Date and time this activity record has been
        created (different from the 'status.dateTime', which is the time
        of a status change of the associated object, if applicable).
    :ivar type: Type of event resulting in this activity record.
    :ivar Assets: All assets for which this activity record has been
        created.
    """
    createdDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Assets: List[Asset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class AssetContainer(Asset):
    """
    Asset that is aggregation of other assets such as conductors, transformers,
    switchgear, land, fences, buildings, equipment, vehicles, etc.

    :ivar Assets: All assets within this container asset.
    """
    Assets: List[Asset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class AssetFunction(IdentifiedObject):
    """
    Function performed by an asset.

    :ivar configID: Configuration specified for this function.
    :ivar firmwareID: Firmware version.
    :ivar hardwareID: Hardware version.
    :ivar password: Password needed to access this function.
    :ivar programID: Name of program.
    :ivar Asset:
    """
    configID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    firmwareID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hardwareID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    programID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Asset: Optional[Asset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Feeder(EquipmentContainer):
    """A collection of equipment for organizational purposes, used for grouping
    distribution resources.

    The organization a feeder does not necessarily reflect connectivity
    or current operation state.

    :ivar NamingSecondarySubstation: The secondary substations that are
        normally energized from the feeder.  Used for naming purposes.
        Should be consistent with the other associations for energizing
        terminal specification and the feeder energization
        specification.
    :ivar NormalEnergizedSubstation: The substations that are normally
        energized by the feeder.
    :ivar NormalEnergizingSubstation: The substation that nominally
        energizes the feeder.  Also used for naming purposes.
    :ivar NormalHeadTerminal: The normal head terminal or terminals of
        the feeder.
    """
    NamingSecondarySubstation: List["Substation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    NormalEnergizedSubstation: List["Substation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    NormalEnergizingSubstation: Optional["Substation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    NormalHeadTerminal: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class Measurement(IdentifiedObject):
    """A Measurement represents any measured, calculated or non-measured non-
    calculated quantity. Any piece of equipment may contain Measurements, e.g.
    a substation may have temperature measurements and door open indications, a
    transformer may have oil temperature and tank pressure measurements, a bay
    may contain a number of power flow measurements and a Breaker may contain a
    switch status measurement.

    The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement.
    Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.
    If both a Terminal and PSR are associated, and the PSR is of type ConductingEquipment, the associated Terminal should belong to that ConductingEquipment instance.
    When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.

    :ivar measurementType: Specifies the type of measurement.  For
        example, this specifies if the measurement represents an indoor
        temperature, outdoor temperature, bus voltage, line flow, etc.
        When the measurementType is set to "Specialization", the type of
        Measurement is defined in more detail by the specialized class
        which inherits from Measurement.
    :ivar phases: Indicates to which phases the measurement applies and
        avoids the need to use 'measurementType' to also encode phase
        information (which would explode the types). The phase
        information in Measurement, along with 'measurementType' and
        'phases' uniquely defines a Measurement for a device, based on
        normal network phase. Their meaning will not change when the
        computed energizing phasing is changed due to jumpers or other
        reasons. If the attribute is missing three phases (ABC) shall be
        assumed.
    :ivar Asset:
    :ivar Locations:
    :ivar PowerSystemResource: The power system resource that contains
        the measurement.
    :ivar Terminal: One or more measurements may be associated with a
        terminal in the network.
    """
    measurementType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phases: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Asset: Optional[Asset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Locations: List[Location] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerSystemResource: Optional[PowerSystemResource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Terminal: Optional["ACDCTerminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class OperationalLimitSet(IdentifiedObject):
    """A set of limits associated with equipment.

    Sets of limits might apply to a specific temperature, or season for
    example. A set of limits may contain different severities of limit
    levels that would apply to the same equipment. The set may contain
    limits of different types such as apparent power and current limits
    or high and low voltage limits  that are logically applied together
    as a set.

    :ivar ConnectivityNode:
    :ivar Equipment: The equipment to which the limit set applies.
    :ivar OperationalLimitValue:
    :ivar Terminal:
    """
    ConnectivityNode: Optional[ConnectivityNode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Equipment: Optional["Equipment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OperationalLimitValue: List[OperationalLimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Terminal: Optional["ACDCTerminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Substation(EquipmentContainer):
    """
    A collection of equipment for purposes other than generation or
    utilization, through which electric energy in bulk is passed for the
    purposes of switching or modifying its characteristics.

    :ivar Region: The SubGeographicalRegion containing the substation.
    """
    Region: Optional[SubGeographicalRegion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WireAssemblyInfo(AssetInfo):
    """
    Describes the construction of a multi-conductor wire.
    """
    PerLengthLineParameter: List[PerLengthLineParameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WirePhaseInfo: List["WirePhaseInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WireSpacingInfo: Optional[WireSpacingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class ACDCTerminal(IdentifiedObject):
    """An electrical connection point (AC or DC) to a piece of conducting
    equipment.

    Terminals are connected at physical connection points called
    connectivity nodes.

    :ivar connected: The connected status is related to a bus-branch
        model and the topological node to terminal relation.  True
        implies the terminal is connected to the related topological
        node and false implies it is not. In a bus-branch model, the
        connected status is used to tell if equipment is disconnected
        without having to change the connectivity described by the
        topological node to terminal relation. A valid case is that
        conducting equipment can be connected in one end and open in the
        other. In particular for an AC line segment, where the reactive
        line charging can be significant, this is a relevant case.
    :ivar sequenceNumber: The orientation of the terminal connections
        for a multiple terminal conducting equipment.  The sequence
        numbering starts with 1 and additional terminals should follow
        in increasing order.   The first terminal is the "starting
        point" for a two terminal branch.
    :ivar Measurements: Measurements associated with this terminal
        defining  where the measurement is placed in the network
        topology.  It may be used, for instance, to capture the sensor
        position, such as a voltage transformer (PT) at a busbar or a
        current transformer (CT) at the bar between a breaker and an
        isolator.
    :ivar OperationalLimitSet:
    """
    connected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OperationalLimitSet: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceEvent(ActivityRecord):
    """
    Event detected by a device function associated with the end device.

    :ivar issuerID: Unique identifier of the business entity originating
        an end device control.
    :ivar issuerTrackingID: Identifier assigned by the initiator (e.g.
        retail electric provider) of an end device control action to
        uniquely identify the demand response event, text message, or
        other subject of the control action. Can be used when cancelling
        an event or text message request or to identify the originating
        event or text message in a consequential end device event.
    :ivar userID: (if user initiated) ID of user who initiated this end
        device event.
    :ivar EndDevice: End device that reported this end device event.
    :ivar EndDeviceEventDetails: All details of this end device event.
    :ivar EndDeviceEventType: Type of this end device event.
    :ivar MeterReading: Set of measured values to which this event
        applies.
    :ivar UsagePoint: Usage point for which this end device event is
        reported.
    """
    issuerID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    issuerTrackingID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    userID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDevice: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceEventDetails: List[EndDeviceEventDetail] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceEventType: Optional[EndDeviceEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    MeterReading: Optional[MeterReading] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UsagePoint: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceFunction(AssetFunction):
    """
    Function performed by an end device such as a meter, communication
    equipment, controllers, etc.

    :ivar enabled: True if the function is enabled.
    :ivar EndDevice: End device that performs this function.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDevice: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or
    mechanical.

    :ivar inService: If true, the equipment is in service.
    :ivar Faults: All faults on this equipment.
    :ivar OperationalLimitSet: The operational limit sets associated
        with this equipment.
    """
    inService: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Faults: List["Fault"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    OperationalLimitSet: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WirePhaseInfo:
    """
    :ivar phaseInfo:
    :ivar sequenceNumber: Numbering for wires on a WireSpacingInfo.
        Neutrals should be numbered last.
    :ivar WireAssemblyInfo:
    :ivar WireInfo:
    :ivar WirePosition:
    """
    phaseInfo: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WireAssemblyInfo: Optional[WireAssemblyInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    WireInfo: Optional["WireInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WirePosition: Optional[WirePosition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConductingEquipment(Equipment):
    """
    The parts of the AC power system that are designed to carry current or that
    are conductively connected through terminals.

    :ivar BaseVoltage: Base voltage of this conducting equipment.  Use
        only when there is no voltage level container used and only one
        base voltage applies.  For example, not used for transformers.
    :ivar SvStatus: The status state variable associated with this
        conducting equipment.
    :ivar Terminals: Conducting equipment have terminals that may be
        connected to other conducting equipment terminals via
        connectivity nodes or topological nodes.
    """
    BaseVoltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SvStatus: List[SvStatus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Terminals: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDevice(AssetContainer):
    """Asset container that performs one or more end device functions.

    One type of end device is a meter which can perform metering, load
    management, connect/disconnect, accounting functions, etc. Some end
    devices, such as ones monitoring and controlling air conditioners,
    refrigerators, pool pumps may be connected to a meter. All end
    devices may have communication capability defined by the associated
    communication function(s). An end device may be owned by a consumer,
    a service provider, utility or otherwise. There may be a related end
    device function that identifies a sensor or control point within a
    metering application or communications systems (e.g., water, gas,
    electricity). Some devices may use an optical port that conforms to
    the ANSI C12.18 standard for communications.

    :ivar amrSystem: Automated meter reading (AMR) or other
        communication system responsible for communications to this end
        device.
    :ivar installCode: Installation code.
    :ivar isPan: If true, this is a premises area network (PAN) device.
    :ivar isSmartInverter:
    :ivar isVirtual: If true, there is no physical device. As an
        example, a virtual meter can be defined to aggregate the
        consumption for two or more physical meters. Otherwise, this is
        a physical hardware device.
    :ivar timeZoneOffset: Time zone offset relative to GMT for the
        location of this end device.
    :ivar Customer: Customer owning this end device.
    :ivar DispatchablePowerCapability:
    :ivar EndDeviceControls: All end device controls sending commands to
        this end device.
    :ivar EndDeviceEvents: All events reported by this end device.
    :ivar EndDeviceFunctions: All end device functions this end device
        performs.
    :ivar EndDeviceGroups: All end device groups referring to this end
        device.
    :ivar EndDeviceInfo: End device data.
    :ivar UsagePoint: Usage point to which this end device belongs.
    """
    amrSystem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    installCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    isPan: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    isSmartInverter: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    isVirtual: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    timeZoneOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Customer: Optional[Customer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DispatchablePowerCapability: List["DispatchablePowerCapability"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceControls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceEvents: List[EndDeviceEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceFunctions: List[EndDeviceFunction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceGroups: Optional["EndDeviceGroup"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceInfo: Optional[EndDeviceInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UsagePoint: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PowerElectronicsUnit(Equipment):
    """
    A generating unit or battery or aggregation that connects to the AC network
    using power electronics rather than rotating machines.

    :ivar maxP: Maximum active power limit. This is the maximum
        (nameplate) limit for the unit.
    :ivar minP: Minimum active power limit. This is the minimum
        (nameplate) limit for the unit.
    :ivar PowerElectronicsConnection:
    """
    maxP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerElectronicsConnection: Optional["PowerElectronicsConnection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class Terminal(ACDCTerminal):
    """An AC electrical connection point to a piece of conducting equipment.

    Terminals are connected at physical connection points called
    connectivity nodes.

    :ivar ConductingEquipment: The conducting equipment of the terminal.
        Conducting equipment have  terminals that may be connected to
        other conducting equipment terminals via connectivity nodes or
        topological nodes.
    :ivar ConnectivityNode: The connectivity node to which this terminal
        connects with zero impedance.
    :ivar EquipmentFaults: The equipment faults at this terminal.
    :ivar NormalHeadFeeder: The feeder that this terminal normally
        feeds.  Only specifed for the terminals at head of feeders.
    :ivar RegulatingControl: The controls regulating this terminal.
    :ivar RemoteInputSignals:
    :ivar SvPowerFlow: The power flow state variable associated with the
        terminal.
    :ivar TopologicalNode: The topological node associated with the
        terminal.   This can be used as an alternative to the
        connectivity node path to topological node, thus making it
        unneccesary to model connectivity nodes in some cases.   Note
        that the if connectivity nodes are in the model, this
        association would probably not be used as an input
        specification.
    :ivar TransformerEnd: All transformer ends connected at this
        terminal.
    """
    ConductingEquipment: Optional["ConductingEquipment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    ConnectivityNode: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EquipmentFaults: List["EquipmentFault"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    NormalHeadFeeder: Optional["Feeder"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RegulatingControl: List["RegulatingControl"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RemoteInputSignals: List[RemoteInputSignal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SvPowerFlow: List[SvPowerFlow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TopologicalNode: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TransformerEnd: List[TransformerEnd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TransformerTank(Equipment):
    """An assembly of two or more coupled windings that transform electrical
    power between voltage levels.

    These windings are bound on a common core and place in the same
    tank. Transformer tank can be used to model both single-phase and
    3-phase transformers.

    :ivar PowerTransformer: Bank this transformer belongs to.
    :ivar TransformerTankEnds: All windings of this transformer.
    :ivar TransformerTankInfo:
    """
    PowerTransformer: Optional["PowerTransformer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TransformerTankEnds: List["TransformerTankEnd"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    TransformerTankInfo: Optional["TransformerTankInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class WireInfo(AssetInfo):
    """
    Wire data that can be specified per line segment phase, or for the line
    segment as a whole in case its phases all have the same wire
    characteristics.

    :ivar coreRadius: (if there is a different core material) Radius of
        the central core.
    :ivar coreStrandCount: (if used) Number of strands in the steel
        core.
    :ivar gmr: Geometric mean radius. If we replace the conductor by a
        thin walled tube of radius GMR, then its reactance is identical
        to the reactance of the actual conductor.
    :ivar insulated: True if conductor is insulated.
    :ivar insulationMaterial: (if insulated conductor) Material used for
        insulation.
    :ivar insulationThickness: (if insulated conductor) Thickness of the
        insulation.
    :ivar material: Conductor material.
    :ivar rAC25: AC resistance per unit length of the conductor at 25
        °C.
    :ivar rAC50: AC resistance per unit length of the conductor at 50
        °C.
    :ivar rAC75: AC resistance per unit length of the conductor at 75
        °C.
    :ivar radius: Outside radius of the wire.
    :ivar ratedCurrent: Current carrying capacity of the wire under
        stated thermal conditions.
    :ivar rDC20: DC resistance per unit length of the conductor at 20
        °C.
    :ivar sizeDescription: Describes the wire gauge or cross section
        (e.g., 4/0, #2, 336.5).
    :ivar strandCount: Number of strands in the conductor.
    :ivar ACLineSegmentPhases:
    :ivar WirePhaseInfo:
    """
    coreRadius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    coreStrandCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    gmr: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    insulated: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    insulationMaterial: Optional[WireInsulationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    insulationThickness: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    material: Optional[WireMaterialKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rAC25: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rAC50: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rAC75: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    radius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rDC20: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sizeDescription: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    strandCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ACLineSegmentPhases: List["ACLineSegmentPhase"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WirePhaseInfo: List[WirePhaseInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ACLineSegmentPhase(PowerSystemResource):
    """
    Represents a single wire of an alternating current line segment.

    :ivar phase: The phase connection of the wire at both ends.
    :ivar sequenceNumber: Number designation for this line segment
        phase. Each line segment phase within a line segment should have
        a unique sequence number. This is useful for unbalanced modeling
        to bind the mathematical model (PhaseImpedanceData of
        PerLengthPhaseImpedance) with the connectivity model (this
        class) and the physical model (WirePosition, WirePhaseInfo)
        without tight coupling. Multiple circuits on the same pole,
        tower or right-of-way can be included with unique sequence
        numbers for the phases, and identical sequence numbers for any
        shared neutrals.
    :ivar ACLineSegment: The line segment to which the phase belongs.
    :ivar WireInfo:
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ACLineSegment: Optional["ACLineSegment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    WireInfo: Optional[WireInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class CableInfo(WireInfo):
    """
    Cable data.

    :ivar constructionKind: Kind of construction of this cable.
    :ivar diameterOverCore: Diameter over the core, including any semi-
        con screen; should be the insulating layer's inside diameter.
    :ivar diameterOverInsulation: Diameter over the insulating layer,
        excluding outer screen.
    :ivar diameterOverJacket: Diameter over the outermost jacketing
        layer.
    :ivar diameterOverScreen: Diameter over the outer screen; should be
        the shield's inside diameter.
    :ivar isStrandFill: True if wire strands are extruded in a way to
        fill the voids in the cable.
    :ivar nominalTemperature: Maximum nominal design operating
        temperature.
    :ivar outerJacketKind: Kind of outer jacket of this cable.
    :ivar sheathAsNeutral: True if sheath / shield is used as a neutral
        (i.e., bonded).
    :ivar shieldMaterial: Material of the shield.
    """
    constructionKind: Optional[CableConstructionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    diameterOverCore: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    diameterOverInsulation: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    diameterOverJacket: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    diameterOverScreen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    isStrandFill: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    nominalTemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    outerJacketKind: Optional[CableOuterJacketKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sheathAsNeutral: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    shieldMaterial: Optional[CableShieldMaterialKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Conductor(ConductingEquipment):
    """
    Combination of conducting material with consistent electrical
    characteristics, building a single electrical system, used to carry current
    between points in the power system.

    :ivar length: Segment length for calculating line section
        capabilities
    """
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Connector(ConductingEquipment):
    """
    A conductor, or group of conductors, with negligible impedance, that serve
    to connect other conducting equipment within a single substation and are
    modelled with a single logical terminal.
    """


@dataclass
class DispatchablePowerCapability:
    """
    :ivar currentActivePower: Product of RMS value of the voltage and
        the RMS value of the in-phase component of the current
    :ivar currentApparentPower: Product of the RMS value of the voltage
        and the RMS value of the current
    :ivar currentReactivePower: Product of RMS value of the voltage and
        the RMS value of the quadrature component of the current
    :ivar maxActivePower: Product of RMS value of the voltage and the
        RMS value of the in-phase component of the current
    :ivar maxApparentPower: Product of the RMS value of the voltage and
        the RMS value of the current
    :ivar maxReactivePower: Product of RMS value of the voltage and the
        RMS value of the quadrature component of the current
    :ivar minActivePower: Product of RMS value of the voltage and the
        RMS value of the in-phase component of the current
    :ivar minApparentPower: Product of the RMS value of the voltage and
        the RMS value of the current
    :ivar minReactivePower: Product of RMS value of the voltage and the
        RMS value of the quadrature component of the current
    :ivar EndDevice:
    :ivar EndDeviceGroup:
    """
    currentActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    currentApparentPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    currentReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maxActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maxApparentPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maxReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minApparentPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDevice: Optional[EndDevice] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceGroup: Optional["EndDeviceGroup"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EnergyConnection(ConductingEquipment):
    pass


@dataclass
class Meter(EndDevice):
    """Physical asset that performs the metering role of the usage point.

    Used for measuring consumption and detection of events.

    :ivar MeterReadings: All meter readings provided by this meter.
    """
    MeterReadings: List["MeterReading"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class OverheadWireInfo(WireInfo):
    """
    Overhead wire data.
    """


@dataclass
class PowerTransformer(ConductingEquipment):
    """An electrical device consisting of  two or more coupled windings, with
    or without a magnetic core, for introducing mutual coupling between
    electric circuits.

    Transformers can be used to control voltage and phase shift (active
    power flow). A power transformer may be composed of separate
    transformer tanks that need not be identical. A power transformer
    can be modeled with or without tanks and is intended for use in both
    balanced and unbalanced representations.   A power transformer
    typically has two terminals, but may have one (grounding), three or
    more terminals. The inherited association
    ConductingEquipment.BaseVoltage should not be used.  The association
    from TransformerEnd to BaseVoltage should be used instead.

    :ivar vectorGroup: Vector group of the transformer for protective
        relaying, e.g., Dyn1. For unbalanced transformers, this may not
        be simply determined from the constituent winding connections
        and phase angle dispacements. The vectorGroup string consists of
        the following components in the order listed: high voltage
        winding connection, mid voltage winding connection (for three
        winding transformers), phase displacement clock number from 0 to
        11,  low voltage winding connection phase displacement clock
        number from 0 to 11.   The winding connections are D (delta), Y
        (wye), YN (wye with neutral), Z (zigzag), ZN (zigzag with
        neutral), A (auto transformer). Upper case means the high
        voltage, lower case mid or low. The high voltage winding always
        has clock postion 0 and is not included in the vector group
        string.  Some examples: YNy0 (two winding wye to wye with no
        phase displacement), YNd11 (two winding wye to delta with 330
        degrees phase displacement), YNyn0d5 (three winding transformer
        wye with neutral high voltgage, wye with neutral mid voltgage
        and no phase displacement, delta low voltage with 150 degrees
        displacement). Phase displacement is defined as the angular
        difference between the phasors representing the voltages between
        the neutral point (real or imaginary) and the corresponding
        terminals of two windings, a positive sequence voltage system
        being applied to the high-voltage terminals, following each
        other in alphabetical sequence if they are lettered, or in
        numerical sequence if they are numbered: the phasors are assumed
        to rotate in a counter-clockwise sense.
    :ivar PowerTransformerEnd: The ends of this power transformer.
    :ivar TransformerTanks: All transformers that belong to this bank.
    """
    vectorGroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerTransformerEnd: List["PowerTransformerEnd"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    TransformerTanks: List["TransformerTank"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Switch(ConductingEquipment):
    """A generic device designed to close, or open, or both, one or more
    electric circuits.

    All switches are two terminal devices including grounding switches.
    """


@dataclass
class ACLineSegment(Conductor):
    """A wire or combination of wires, with consistent electrical
    characteristics, building a single electrical system, used to carry
    alternating current between points in the power system.

    For symmetrical, transposed 3ph lines, it is sufficient to use
    attributes of the line segment, which describe impedances and
    admittances for the entire length of the segment.  Additionally
    impedances can be computed by using length and associated per length
    impedances. The BaseVoltage at the two ends of ACLineSegments in a
    Line shall have the same BaseVoltage.nominalVoltage. However,
    boundary lines  may have slightly different
    BaseVoltage.nominalVoltages and  variation is allowed. Larger
    voltage difference in general requires use of an equivalent branch.

    :ivar b0ch: Zero sequence shunt (charging) susceptance, uniformly
        distributed, of the entire line section.
    :ivar bch: Positive sequence shunt (charging) susceptance, uniformly
        distributed, of the entire line section.  This value represents
        the full charging over the full length of the line.
    :ivar g0ch: Zero sequence shunt (charging) conductance, uniformly
        distributed, of the entire line section.
    :ivar gch: Positive sequence shunt (charging) conductance, uniformly
        distributed, of the entire line section.
    :ivar r: Positive sequence series resistance of the entire line
        section.
    :ivar r0: Zero sequence series resistance of the entire line
        section.
    :ivar x: Positive sequence series reactance of the entire line
        section.
    :ivar x0: Zero sequence series reactance of the entire line section.
    :ivar ACLineSegmentPhases: The line segment phases which belong to
        the line segment.
    :ivar PerLengthImpedance: Per-length impedance of this line segment.
    :ivar WireSpacingInfo:
    """
    b0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    bch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    g0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    gch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ACLineSegmentPhases: List[ACLineSegmentPhase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PerLengthImpedance: Optional[PerLengthImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    WireSpacingInfo: Optional[WireSpacingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class BusbarSection(Connector):
    """A conductor, or group of conductors, with negligible impedance, that
    serve to connect other conducting equipment within a single substation.

    Voltage measurements are typically obtained from VoltageTransformers
    that are connected to busbar sections. A bus bar section may have
    many physical terminals but for analysis is modelled with exactly
    one logical terminal.

    :ivar ipMax: Maximum allowable peak short-circuit current of busbar
        (Ipmax in the IEC 60909-0). Mechanical limit of the busbar in
        the substation itself. Used for short circuit data exchange
        according to IEC 60909
    :ivar VoltageControlZone: A VoltageControlZone is controlled by a
        designated BusbarSection.
    """
    ipMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    VoltageControlZone: Optional["VoltageControlZone"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConcentricNeutralCableInfo(CableInfo):
    """
    Concentric neutral cable data.

    :ivar diameterOverNeutral: Diameter over the concentric neutral
        strands.
    :ivar neutralStrandCount: Number of concentric neutral strands.
    :ivar neutralStrandGmr: Geometric mean radius of the neutral strand.
    :ivar neutralStrandRadius: Outside radius of the neutral strand.
    :ivar neutralStrandRDC20: DC resistance per unit length of the
        neutral strand at 20 °C.
    """
    diameterOverNeutral: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutralStrandCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutralStrandGmr: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutralStrandRadius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutralStrandRDC20: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceGroup(IdentifiedObject):
    """Abstraction for management of group communications within a two-way AMR
    system or the data for a group of related end devices.

    Commands can be issued to all of the end devices that belong to the
    group using a defined group address and the underlying AMR
    communication infrastructure. A DERGroup and a PANDeviceGroup is an
    EndDeviceGroup.

    :ivar type: Type of this group.
    :ivar DemandResponsePrograms: All demand response programs this
        group of end devices is enrolled in.
    :ivar DERFunction:
    :ivar DERGroupDispatch:
    :ivar DERGroupForecast:
    :ivar DERMonitorableParameter:
    :ivar DispatchablePowerCapability:
    :ivar EndDeviceControls: All end device controls sending commands to
        this end device group.
    :ivar EndDevices: All end devices this end device group refers to.
    :ivar status:
    :ivar version:
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DemandResponsePrograms: List[DemandResponseProgram] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERFunction: Optional[DERFunction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERGroupDispatch: List[DERGroupDispatch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERGroupForecast: List[DERGroupForecast] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    DERMonitorableParameter: List[DERMonitorableParameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DispatchablePowerCapability: Optional[DispatchablePowerCapability] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceControls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDevices: List[EndDevice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EnergyConsumer(EnergyConnection):
    """Generic user of energy - a  point of consumption on the power system model.

    :ivar customerCount: Number of individual customers represented by
        this demand.
    :ivar grounded: Used for Yn and Zn connections. True if the neutral
        is solidly grounded.
    :ivar p: Active power of the load. Load sign convention is used,
        i.e. positive sign means flow out from a node. For voltage
        dependent loads the value is at rated voltage. Starting value
        for a steady state solution.
    :ivar phaseConnection: The type of phase connection, such as wye or
        delta.
    :ivar q: Reactive power of the load. Load sign convention is used,
        i.e. positive sign means flow out from a node. For voltage
        dependent loads the value is at rated voltage. Starting value
        for a steady state solution.
    :ivar EnergyConsumerPhase: The individual phase models for this
        energy consumer.
    :ivar House:
    :ivar LoadResponse: The load response characteristic of this load.
        If missing, this load is assumed to be constant power.
    :ivar PowerCutZone: The  energy consumer is assigned to this power
        cut zone.
    """
    customerCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phaseConnection: Optional[PhaseShuntConnectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergyConsumerPhase: List[EnergyConsumerPhase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    House: Optional[House] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    LoadResponse: Optional[LoadResponseCharacteristic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerCutZone: Optional[PowerCutZone] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EnergySource(EnergyConnection):
    """
    A generic equivalent for an energy supplier on a transmission or
    distribution voltage level.

    :ivar nominalVoltage: Phase-to-phase nominal voltage.
    :ivar r: Positive sequence Thevenin resistance.
    :ivar r0: Zero sequence Thevenin resistance.
    :ivar voltageAngle: Phase angle of a-phase open circuit.
    :ivar voltageMagnitude: Phase-to-phase open circuit voltage
        magnitude.
    :ivar x: Positive sequence Thevenin reactance.
    :ivar x0: Zero sequence Thevenin reactance.
    :ivar EnergySourcePhase: The individual phase information of the
        energy source.
    """
    nominalVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltageAngle: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltageMagnitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EnergySourcePhase: List[EnergySourcePhase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Fuse(Switch):
    """An overcurrent protective device with a circuit opening fusible part
    that is heated and severed by the passage of overcurrent through it.

    A fuse is considered a switching device because it breaks current.
    """


@dataclass
class ProtectedSwitch(Switch):
    """
    A ProtectedSwitch is a switching device that can be operated by
    ProtectionEquipment.
    """


@dataclass
class RegulatingCondEq(EnergyConnection):
    """
    A type of conducting equipment that can regulate a quantity (i.e. voltage
    or flow) at a specific point in the network.

    :ivar controlEnabled: Specifies the regulation status of the
        equipment.  True is regulating, false is not regulating.
    :ivar RegulatingControl: The regulating control scheme in which this
        equipment participates.
    """
    controlEnabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    RegulatingControl: Optional["RegulatingControl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Sectionaliser(Switch):
    """Automatic switch that will lock open to isolate a faulted section.

    It may, or may not, have load breaking capability. Its primary
    purpose is to provide fault sectionalising at locations where the
    fault current is either too high, or too low, for proper
    coordination of fuses.
    """


@dataclass
class TapeShieldCableInfo(CableInfo):
    """
    Tape shield cable data.

    :ivar tapeLap: Percentage of the tape shield width that overlaps in
        each wrap, typically 10% to 25%.
    :ivar tapeThickness: Thickness of the tape shield, before wrapping.
    """
    tapeLap: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    tapeThickness: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Breaker(ProtectedSwitch):
    """
    A mechanical switching device capable of making, carrying, and breaking
    currents under normal circuit conditions and also making, carrying for a
    specified time, and breaking currents under specified abnormal circuit
    conditions e.g.  those of short circuit.
    """


@dataclass
class EndDeviceControl(IdentifiedObject):
    """
    Instructs an end device (or an end device group) to perform a specified
    action.

    :ivar drProgramLevel: Level of a demand response program request,
        where 0=emergency. Note: Attribute is not defined on
        DemandResponseProgram as it is not its inherent property (it
        serves to control it).
    :ivar drProgramMandatory: Whether a demand response program request
        is mandatory. Note: Attribute is not defined on
        DemandResponseProgram as it is not its inherent property (it
        serves to control it).
    :ivar issuerID: Unique identifier of the business entity originating
        an end device control.
    :ivar issuerTrackingID: Identifier assigned by the initiator (e.g.
        retail electric provider) of an end device control action to
        uniquely identify the demand response event, text message, or
        other subject of the control action. Can be used when cancelling
        an event or text message request or to identify the originating
        event or text message in a consequential end device event.
    :ivar reason: Reason for the control action that allows to determine
        how to continue processing. For example, disconnect meter
        command may require different processing by the receiving system
        if it has been issued for a network-related reason (protection)
        or for a payment-related reason.
    :ivar EndDeviceAction: End device action issued by this end device
        control.
    :ivar EndDeviceControlType: Type of this end device control.
    :ivar EndDeviceGroups: All end device groups receiving commands from
        this end device control.
    :ivar EndDevices: All end devices receiving commands from this end
        device control.
    :ivar priceSignal: (if applicable) Price signal used as parameter
        for this end device control.
    :ivar primaryDeviceTiming: Timing for the control actions performed
        on the device identified in the end device control.
    :ivar scheduledInterval: (if control has scheduled duration) Date
        and time interval the control has been scheduled to execute
        within.
    :ivar secondaryDeviceTiming: Timing for the control actions
        performed by devices that are responding to event related
        information sent to the primary device indicated in the end
        device control.  For example, load control actions performed by
        a PAN device in response to demand response event information
        sent to a PAN gateway server.
    :ivar UsagePointGroups: All usage point groups receiving commands
        from this end device control.
    :ivar UsagePoints: All usage points receiving commands from this end
        device control.
    """
    drProgramLevel: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    drProgramMandatory: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    issuerID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    issuerTrackingID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceAction: Optional[EndDeviceAction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceControlType: Optional[EndDeviceControlType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    EndDeviceGroups: List[EndDeviceGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDevices: List[EndDevice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    priceSignal: Optional[FloatQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    primaryDeviceTiming: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    scheduledInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    secondaryDeviceTiming: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UsagePointGroups: List[UsagePointGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class LoadBreakSwitch(ProtectedSwitch):
    """
    A mechanical switching device capable of making, carrying, and breaking
    currents under normal operating conditions.
    """


@dataclass
class PowerElectronicsConnection(RegulatingCondEq):
    """
    A connection to the AC network for energy production or consumption that
    uses power electronics rather than rotating machines.

    :ivar inverterMode:
    :ivar maxIFault: Maximum fault current this device will contribute,
        in per-unit of rated current, before the converter protection
        will trip or bypass.
    :ivar maxQ: Maximum reactive power limit. This is the maximum
        (nameplate) limit for the unit.
    :ivar minQ: Minimum reactive power limit for the unit. This is the
        minimum (nameplate) limit for the unit.
    :ivar p: Active power injection. Load sign convention is used, i.e.
        positive sign means flow out from a node. Starting value for a
        steady state solution.
    :ivar q: Reactive power injection. Load sign convention is used,
        i.e. positive sign means flow out from a node. Starting value
        for a steady state solution.
    :ivar ratedS: Nameplate apparent power rating for the unit. The
        attribute shall have a positive value.
    :ivar ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It
        is primarily used for short circuit data exchange according to
        IEC 60909.
    :ivar DERDynamics: DER dynamics model associated with this power
        electronics connection model.
    :ivar IEEE1547ControlSettings:
    :ivar IEEE1547Info:
    :ivar IEEE1547Setting:
    :ivar IEEE1547TripSettings:
    :ivar PowerElectronicsConnectionPhases:
    :ivar PowerElectronicsUnit:
    """
    inverterMode: Optional[ConverterControlMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maxIFault: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maxQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    DERDynamics: Optional["DERDynamics"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IEEE1547ControlSettings: Optional[IEEE1547ControlSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IEEE1547Info: Optional["IEEE1547Info"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IEEE1547Setting: Optional[IEEE1547Setting] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IEEE1547TripSettings: Optional[IEEE1547TripSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerElectronicsConnectionPhases: List["PowerElectronicsConnectionPhase"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    PowerElectronicsUnit: List["PowerElectronicsUnit"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Recloser(ProtectedSwitch):
    """
    Pole-mounted fault interrupter with built-in phase and ground relays,
    current transformer (CT), and supplemental controls.
    """


@dataclass
class RotatingMachine(RegulatingCondEq):
    """
    A rotating machine which may be used as a generator or motor.

    :ivar p: Active power injection. Load sign convention is used, i.e.
        positive sign means flow out from a node. Starting value for a
        steady state solution.
    :ivar q: Reactive power injection. Load sign convention is used,
        i.e. positive sign means flow out from a node. Starting value
        for a steady state solution.
    :ivar ratedPowerFactor: Power factor (nameplate data). It is
        primarily used for short circuit data exchange according to IEC
        60909.
    :ivar ratedS: Nameplate apparent power rating for the unit. The
        attribute shall have a positive value.
    :ivar ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It
        is primarily used for short circuit data exchange according to
        IEC 60909.
    :ivar IEEE1547ControlSettings:
    :ivar IEEE1547Info:
    :ivar IEEE1547Setting:
    :ivar IEEE1547TripSettings:
    """
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IEEE1547ControlSettings: Optional["IEEE1547ControlSettings"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IEEE1547Info: Optional["IEEE1547Info"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IEEE1547Setting: Optional[IEEE1547Setting] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    IEEE1547TripSettings: Optional[IEEE1547TripSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ShuntCompensator(RegulatingCondEq):
    """A shunt capacitor or reactor or switchable bank of shunt capacitors or
    reactors.

    A section of a shunt compensator is an individual capacitor or
    reactor.  A negative value for reactivePerSection indicates that the
    compensator is a reactor. ShuntCompensator is a single terminal
    device.  Ground is implied.

    :ivar aVRDelay: Time delay required for the device to be connected
        or disconnected by automatic voltage regulation (AVR).
    :ivar grounded: Used for Yn and Zn connections. True if the neutral
        is solidly grounded.
    :ivar maximumSections: The maximum number of sections that may be
        switched in.
    :ivar nomU: The voltage at which the nominal reactive power may be
        calculated. This should normally be within 10% of the voltage at
        which the capacitor is connected to the network.
    :ivar normalSections: The normal number of sections switched in.
    :ivar phaseConnection: The type of phase connection, such as wye or
        delta.
    :ivar sections: Shunt compensator sections in use. Starting value
        for steady state solution. Non integer values are allowed to
        support continuous variables. The reasons for continuous value
        are to support study cases where no discrete shunt compensators
        has yet been designed, a solutions where a narrow voltage band
        force the sections to oscillate or accommodate for a continuous
        solution as input.
    :ivar ShuntCompensatorPhase: The individual phases models for the
        shunt compensator.
    :ivar SvShuntCompensatorSections: The state for the number of shunt
        compensator sections in service.
    """
    aVRDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    maximumSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    nomU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normalSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phaseConnection: Optional[PhaseShuntConnectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sections: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ShuntCompensatorPhase: List[ShuntCompensatorPhase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    SvShuntCompensatorSections: Optional[SvShuntCompensatorSections] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class LinearShuntCompensator(ShuntCompensator):
    """
    A linear shunt compensator has banks or sections with equal admittance
    values.

    :ivar b0PerSection: Zero sequence shunt (charging) susceptance per
        section
    :ivar bPerSection: Positive sequence shunt (charging) susceptance
        per section
    :ivar g0PerSection: Zero sequence shunt (charging) conductance per
        section
    :ivar gPerSection: Positive sequence shunt (charging) conductance
        per section
    """
    b0PerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    bPerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    g0PerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    gPerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class SynchronousMachine(RotatingMachine):
    """An electromechanical device that operates with shaft rotating
    synchronously with the network.

    It is a single machine operating either as a generator or
    synchronous condenser or pump.
    """


@dataclass
class UsagePoint(IdentifiedObject):
    """Logical or physical point in the network to which readings or events may
    be attributed.

    Used at the place where a physical or virtual meter may be located;
    however, it is not required that a meter be present.

    :ivar amiBillingReady: Tracks the lifecycle of the metering
        installation at a usage point with respect to readiness for
        billing via advanced metering infrastructure reads.
    :ivar checkBilling: True if as a result of an inspection or
        otherwise, there is a reason to suspect that a previous billing
        may have been performed with erroneous data. Value should be
        reset once this potential discrepancy has been resolved.
    :ivar connectionState: State of the usage point with respect to
        connection to the network.
    :ivar estimatedLoad: Estimated load.
    :ivar grounded: True if grounded.
    :ivar isSdp: If true, this usage point is a service delivery point,
        i.e., a usage point where the ownership of the service changes
        hands.
    :ivar isVirtual: If true, this usage point is virtual, i.e., no
        physical location exists in the network where a meter could be
        located to collect the meter readings. For example, one may
        define a virtual usage point to serve as an aggregation of usage
        for all of a company's premises distributed widely across the
        distribution territory. Otherwise, the usage point is physical,
        i.e., there is a logical point in the network where a meter
        could be located to collect meter readings.
    :ivar minimalUsageExpected: If true, minimal or zero usage is
        expected at this usage point for situations such as premises
        vacancy, logical or physical disconnect. It is used for readings
        validation and estimation.
    :ivar nominalServiceVoltage: Nominal service voltage.
    :ivar outageRegion: Outage region in which this usage point is
        located.
    :ivar phaseCode: Phase code. Number of wires and specific nominal
        phases can be deduced from enumeration literal values. For
        example, ABCN is three-phase, four-wire, s12n
        (splitSecondary12N) is single-phase, three-wire, and s1n and s2n
        are single-phase, two-wire.
    :ivar ratedCurrent: Current flow that this usage point is configured
        to deliver.
    :ivar ratedPower: Active power that this usage point is configured
        to deliver.
    :ivar readCycle: Cycle day on which the meter for this usage point
        will normally be read.  Usually correlated with the billing
        cycle.
    :ivar readRoute: Identifier of the route to which this usage point
        is assigned for purposes of meter reading. Typically used to
        configure hand held meter reading systems prior to collection of
        reads.
    :ivar serviceDeliveryRemark: Remarks about this usage point, for
        example the reason for it being rated with a non-nominal
        priority.
    :ivar servicePriority: Priority of service for this usage point.
        Note that usage points at the same service location can have
        different priorities.
    :ivar EndDeviceControls: All end device controls sending commands to
        this usage point.
    :ivar EndDeviceEvents: All end device events reported for this usage
        point.
    :ivar EndDevices: All end devices at this usage point.
    :ivar Equipments: All equipment connecting this usage point to the
        electrical grid.
    :ivar MeterReadings: All meter readings obtained from this usage
        point.
    """
    amiBillingReady: Optional[AmiBillingReadyKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    checkBilling: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    connectionState: Optional[UsagePointConnectedKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    estimatedLoad: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    isSdp: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    isVirtual: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minimalUsageExpected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    nominalServiceVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    outageRegion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phaseCode: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratedPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    readCycle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    readRoute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    serviceDeliveryRemark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    servicePriority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceControls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDeviceEvents: List[EndDeviceEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    EndDevices: List[EndDevice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    Equipments: List[Equipment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    MeterReadings: List[MeterReading] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConfigurationEvent(ActivityRecord):
    """
    Used to report details on creation, change or deletion of an entity or its
    configuration.

    :ivar effectiveDateTime: Date and time this event has or will become
        effective.
    :ivar modifiedBy: Source/initiator of modification.
    :ivar remark: Free text remarks.
    :ivar ChangedAsset: Asset whose change resulted in this
        configuration event.
    :ivar ChangedUsagePoint: Usage point whose change resulted in this
        configuration event.
    :ivar FaultCauseType:
    :ivar PowerSystemResource:
    """
    effectiveDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    modifiedBy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ChangedAsset: Optional[Asset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ChangedUsagePoint: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    FaultCauseType: Optional[FaultCauseType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    PowerSystemResource: Optional[PowerSystemResource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ReactiveCapabilityCurve(Curve):
    """Reactive power rating envelope versus the synchronous machine's active
    power, in both the generating and motoring modes.

    For each active power value there is a corresponding high and low
    reactive power limit  value. Typically there will be a separate
    curve for each coolant condition, such as hydrogen pressure.  The Y1
    axis values represent reactive minimum and the Y2 axis values
    represent reactive maximum.

    :ivar coolantTemperature: The machine's coolant temperature (e.g.,
        ambient air or stator circulating water).
    :ivar hydrogenPressure: The hydrogen coolant pressure
    :ivar InitiallyUsedBySynchronousMachines: Synchronous machines using
        this curve as default.
    :ivar SynchronousMachines: Synchronous machines using this curve.
    """
    coolantTemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hydrogenPressure: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    InitiallyUsedBySynchronousMachines: List[SynchronousMachine] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    SynchronousMachines: List[SynchronousMachine] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )

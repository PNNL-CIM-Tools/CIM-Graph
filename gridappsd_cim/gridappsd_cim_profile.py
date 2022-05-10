from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://iec.ch/TC57/"


class AbnormalOpcatKind(Enum):
    """Kinds of abnormal opertaion categories.

    Reference: IEEE1547-2018.

    :cvar CAT_I: Category CAT_I.
    :cvar CAT_II: Category CAT_II.
    :cvar CAT_III: Category CAT_III.
    """
    CAT_I = "catI"
    CAT_II = "catII"
    CAT_III = "catIII"


class AmiBillingReadyKind(Enum):
    """
    Lifecycle states of the metering installation at a usage point with respect
    to readiness for billing via advanced metering infrastructure reads.

    :cvar AMI_CAPABLE: Usage point is equipped with an AMI capable meter
        that is not yet currently equipped with a communications module.
    :cvar AMI_DISABLED: Usage point is equipped with an AMI capable
        meter; however, the AMI functionality has been disabled or is
        not being used.
    :cvar BILLING_APPROVED: Usage point is equipped with an operating
        AMI capable meter and accuracy has been certified for billing
        purposes.
    :cvar ENABLED: Usage point is equipped with an AMI capable meter
        having communications capability.
    :cvar NON_AMI: Usage point is equipped with a non AMI capable meter.
    :cvar NON_METERED: Usage point is not currently equipped with a
        meter.
    :cvar OPERABLE: Usage point is equipped with an AMI capable meter
        that is functioning and communicating with the AMI network.
    """
    AMI_CAPABLE = "amiCapable"
    AMI_DISABLED = "amiDisabled"
    BILLING_APPROVED = "billingApproved"
    ENABLED = "enabled"
    NON_AMI = "nonAmi"
    NON_METERED = "nonMetered"
    OPERABLE = "operable"


class CableConstructionKind(Enum):
    """
    Kind of cable construction.

    :cvar COMPACTED: Compacted cable.
    :cvar COMPRESSED: Compressed cable.
    :cvar OTHER: Other kind of cable construction.
    :cvar SECTOR: Sector cable.
    :cvar SEGMENTAL: Segmental cable.
    :cvar SOLID: Solid cable.
    :cvar STRANDED: Stranded cable.
    """
    COMPACTED = "compacted"
    COMPRESSED = "compressed"
    OTHER = "other"
    SECTOR = "sector"
    SEGMENTAL = "segmental"
    SOLID = "solid"
    STRANDED = "stranded"


class CableOuterJacketKind(Enum):
    """
    Kind of cable outer jacket.

    :cvar INSULATING: Insulating cable outer jacket.
    :cvar LINEAR_LOW_DENSITY_POLYETHYLENE: Linear low density
        polyethylene cable outer jacket.
    :cvar NONE: Cable has no outer jacket.
    :cvar OTHER: Pther kind of cable outer jacket.
    :cvar POLYETHYLENE: Polyethylene cable outer jacket.
    :cvar PVC: PVC cable outer jacket.
    :cvar SEMICONDUCTING: Semiconducting cable outer jacket.
    """
    INSULATING = "insulating"
    LINEAR_LOW_DENSITY_POLYETHYLENE = "linearLowDensityPolyethylene"
    NONE = "none"
    OTHER = "other"
    POLYETHYLENE = "polyethylene"
    PVC = "pvc"
    SEMICONDUCTING = "semiconducting"


class CableShieldMaterialKind(Enum):
    """
    Kind of cable shield material.

    :cvar ALUMINUM: Aluminum cable shield.
    :cvar COPPER: Copper cable shield.
    :cvar LEAD: Lead cable shield.
    :cvar OTHER: Other kind of cable shield material.
    :cvar STEEL: Steel cable shield.
    """
    ALUMINUM = "aluminum"
    COPPER = "copper"
    LEAD = "lead"
    OTHER = "other"
    STEEL = "steel"


class ConstantPowerFactorSettingKind(Enum):
    """The kinds of constant power factor setting.

    Reference: IEEE1547-2018.

    :cvar ABS: ABS.
    :cvar INJ: INJ.
    """
    ABS = "abs"
    INJ = "inj"


class ConverterControlMode(Enum):
    """
    :cvar CONSTANT_POWER_FACTOR: hold q/p constant
    :cvar CONSTANT_REACTIVE_POWER: Holds constant Q; may change both P
        and Q by dispatch commands
    :cvar DYNAMIC: use association with DERIEEEType1
    """
    CONSTANT_POWER_FACTOR = "constantPowerFactor"
    CONSTANT_REACTIVE_POWER = "constantReactivePower"
    DYNAMIC = "dynamic"


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
    :ivar curve: The curve of  this curve data point.
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
    curve: Optional["Curve"] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


class CurveStyle(Enum):
    """
    Style or shape of curve.

    :cvar CONSTANT_YVALUE: The Y-axis values are assumed constant until
        the next curve point and prior to the first curve point.
    :cvar STRAIGHT_LINE_YVALUES: The Y-axis values are assumed to be a
        straight line between values.  Also known as linear
        interpolation.
    """
    CONSTANT_YVALUE = "constantYValue"
    STRAIGHT_LINE_YVALUES = "straightLineYValues"


@dataclass
class Derfunction:
    class Meta:
        name = "DERFunction"

    connect_disconnect: Optional[bool] = field(
        default=None,
        metadata={
            "name": "connectDisconnect",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    frequency_watt_curve_function: Optional[bool] = field(
        default=None,
        metadata={
            "name": "frequencyWattCurveFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    max_real_power_limiting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "maxRealPowerLimiting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ramp_rate_control: Optional[bool] = field(
        default=None,
        metadata={
            "name": "rampRateControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reactive_power_dispatch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "reactivePowerDispatch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    real_power_dispatch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "realPowerDispatch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltage_regulation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "voltageRegulation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_curve_function: Optional[bool] = field(
        default=None,
        metadata={
            "name": "voltVarCurveFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_watt_curve_function: Optional[bool] = field(
        default=None,
        metadata={
            "name": "voltWattCurveFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_group: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


class DerparameterKind(Enum):
    ACTIVE_POWER = "activePower"
    APPARENT_POWER = "apparentPower"
    DECREASING_RAMP_RATE = "decreasingRampRate"
    HIGH_FILTER_BI_DIRECTIONAL_REGULATION = "highFilterBiDirectionalRegulation"
    HIGH_FILTER_DOWN_REGULATION = "highFilterDownRegulation"
    HIGH_FILTER_UP_REGULATION = "highFilterUpRegulation"
    INCREASING_RAMP_RATE = "increasingRampRate"
    LOW_FILTER_BI_DIRECTIONAL_REGULATION = "lowFilterBiDirectionalRegulation"
    LOW_FILTER_DOWN_REGULATION = "lowFilterDownRegulation"
    LOW_FILTER_UP_REGULATION = "lowFilterUpRegulation"
    REACTIVE_POWER = "reactivePower"
    VOLTAGE = "voltage"


class DerunitSymbol(Enum):
    """
    The units defined for usage in the CIM.

    :cvar A: Current in Ampere.
    :cvar AH: Ampere-hours, Ampere-hours.
    :cvar AS: Ampere seconds (A·s).
    :cvar BTU: Energy, British Thermal Unit.
    :cvar HZ: Frequency in Hertz (1/s).
    :cvar Q: Quantity power, Q.
    :cvar QH: Quantity energy, Qh.
    :cvar V: Electric potential in Volt (W/A).
    :cvar VA: Apparent power in Volt Ampere (See also real power and
        reactive power.)
    :cvar VAH: Apparent energy in Volt Ampere hours.
    :cvar VAR: Reactive power in Volt Ampere reactive. The “reactive” or
        “imaginary” component of electrical power (VIsin(phi)). (See
        also real power and apparent power). Note: Different meter
        designs use different methods to arrive at their results. Some
        meters may compute reactive power as an arithmetic value, while
        others compute the value vectorially. The data consumer should
        determine the method in use and the suitability of the
        measurement for the intended purpose.
    :cvar VARH: Reactive energy in Volt Ampere reactive hours.
    :cvar VPER_VA: Power factor, PF, the ratio of the active power to
        the apparent power. Note: The sign convention used for power
        factor will differ between IEC meters and EEI (ANSI) meters. It
        is assumed that the data consumers understand the type of meter
        being used and agree on the sign convention in use at any given
        utility.
    :cvar VPER_VAR: Power factor, PF, the ratio of the active power to
        the apparent power. Note: The sign convention used for power
        factor will differ between IEC meters and EEI (ANSI) meters. It
        is assumed that the data consumers understand the type of meter
        being used and agree on the sign convention in use at any given
        utility.
    :cvar VH: Volt-hour, Volt hours.
    :cvar VS: Volt second (Ws/A).
    :cvar W: Real power in Watt (J/s). Electrical power may have real
        and reactive components. The real portion of electrical power
        (I²R or VIcos(phi)), is expressed in Watts. (See also apparent
        power and reactive power.)
    :cvar WPER_A: Active power per current flow, watt per Ampere.
    :cvar WPERS: Ramp rate in Watt per second.
    :cvar WH: Real energy in Watt hours.
    :cvar DEG: Plane angle in degrees.
    :cvar DEG_C: Relative temperature in degrees Celsius. In the SI unit
        system the symbol is ºC. Electric charge is measured in coulomb
        that has the unit symbol C. To distinguish degree Celsius form
        coulomb the symbol used in the UML is degC. Reason for not using
        ºC is the special character º is difficult to manage in
        software.
    :cvar H: Time, hour = 60 min = 3600 s.
    :cvar MIN: Time, minute  = 60 s.
    :cvar OHM: Electric resistance in ohm (V/A).
    :cvar OHM_PERM: Electric resistance per length in ohm per metre
        ((V/A)/m).
    :cvar OHMM: resistivity, Ohm metre, (rho).
    :cvar ONE_PER_HZ: Reciprocal of frequency (1/Hz).
    :cvar S: Time in seconds.
    :cvar THERM: Energy, Therm.
    """
    A = "A"
    AH = "Ah"
    AS = "As"
    BTU = "Btu"
    HZ = "Hz"
    Q = "Q"
    QH = "Qh"
    V = "V"
    VA = "VA"
    VAH = "VAh"
    VAR = "VAr"
    VARH = "VArh"
    VPER_VA = "VPerVA"
    VPER_VAR = "VPerVAr"
    VH = "Vh"
    VS = "Vs"
    W = "W"
    WPER_A = "WPerA"
    WPERS = "WPers"
    WH = "Wh"
    DEG = "deg"
    DEG_C = "degC"
    H = "h"
    MIN = "min"
    OHM = "ohm"
    OHM_PERM = "ohmPerm"
    OHMM = "ohmm"
    ONE_PER_HZ = "onePerHz"
    S = "s"
    THERM = "therm"


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
    :ivar duration_indefinite: True if the action of this control is
        indefinite.
    :ivar start_date_time: Start date and time for action of this
        control.
    :ivar end_device_control: End device control issuing this end device
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
    duration_indefinite: Optional[bool] = field(
        default=None,
        metadata={
            "name": "durationIndefinite",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    start_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_control: Optional["EndDeviceControl"] = field(
        default=None,
        metadata={
            "name": "EndDeviceControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceCapability:
    """
    Inherent capabilities of an end device (i.e., the functions it supports).

    :ivar autonomous_dst: True if autonomous DST (daylight saving time)
        function is supported.
    :ivar communication: True if communication function is supported.
    :ivar connect_disconnect: True if connect and disconnect function is
        supported.
    :ivar demand_response: True if demand response function is
        supported.
    :ivar electric_metering: True if electric metering function is
        supported.
    :ivar gas_metering: True if gas metering function is supported.
    :ivar metrology: True if metrology function is supported.
    :ivar on_request_read: True if on request read function is
        supported.
    :ivar outage_history: True if outage history function is supported.
    :ivar pressure_compensation: True if device performs pressure
        compensation for metered quantities.
    :ivar pricing_info: True if pricing information is supported.
    :ivar pulse_output: True if device produces pulse outputs.
    :ivar relays_programming: True if relays programming function is
        supported.
    :ivar reverse_flow: True if reverse flow function is supported.
    :ivar super_compressibility_compensation: True if device performs
        super compressibility compensation for metered quantities.
    :ivar temperature_compensation: True if device performs temperature
        compensation for metered quantities.
    :ivar text_message: True if the displaying of text messages is
        supported.
    :ivar water_metering: True if water metering function is supported.
    """
    autonomous_dst: Optional[bool] = field(
        default=None,
        metadata={
            "name": "autonomousDst",
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
    connect_disconnect: Optional[bool] = field(
        default=None,
        metadata={
            "name": "connectDisconnect",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    demand_response: Optional[bool] = field(
        default=None,
        metadata={
            "name": "demandResponse",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    electric_metering: Optional[bool] = field(
        default=None,
        metadata={
            "name": "electricMetering",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    gas_metering: Optional[bool] = field(
        default=None,
        metadata={
            "name": "gasMetering",
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
    on_request_read: Optional[bool] = field(
        default=None,
        metadata={
            "name": "onRequestRead",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    outage_history: Optional[bool] = field(
        default=None,
        metadata={
            "name": "outageHistory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pressure_compensation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pressureCompensation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pricing_info: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pricingInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pulse_output: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pulseOutput",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    relays_programming: Optional[bool] = field(
        default=None,
        metadata={
            "name": "relaysProgramming",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reverse_flow: Optional[bool] = field(
        default=None,
        metadata={
            "name": "reverseFlow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    super_compressibility_compensation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "superCompressibilityCompensation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    temperature_compensation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "temperatureCompensation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    text_message: Optional[bool] = field(
        default=None,
        metadata={
            "name": "textMessage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    water_metering: Optional[bool] = field(
        default=None,
        metadata={
            "name": "waterMetering",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class FaultImpedance:
    """
    Impedance description for the fault.

    :ivar r_ground: The resistance of the fault between phases and
        ground.
    :ivar r_line_to_line: The resistance of the fault between phases.
    :ivar x_ground: The reactance of the fault between phases and
        ground.
    :ivar x_line_to_line: The reactance of the fault between phases.
    """
    r_ground: Optional[float] = field(
        default=None,
        metadata={
            "name": "rGround",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r_line_to_line: Optional[float] = field(
        default=None,
        metadata={
            "name": "rLineToLine",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x_ground: Optional[float] = field(
        default=None,
        metadata={
            "name": "xGround",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x_line_to_line: Optional[float] = field(
        default=None,
        metadata={
            "name": "xLineToLine",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


class FlowDirectionKind(Enum):
    """
    Kind of flow direction for reading/measured  values proper to some
    commodities such as, for example, energy, power, demand.

    :cvar FORWARD: "Delivered," or "Imported" as defined 61968-2.
        Forward Active Energy is a positive kWh value as one would
        naturally expect to find as energy is supplied by the utility
        and consumed at the service. Forward Reactive Energy is a
        positive VArh value as one would naturally expect to find in the
        presence of inductive loading. In polyphase metering, the
        forward energy register is incremented when the sum of the phase
        energies is greater than zero: &amp;lt;img src="HTS_1.PNG"
        width="209" height="16" border="0" alt="graphic"/&amp;gt;
    :cvar LAGGING: Typically used to describe that a power factor is
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
    :cvar LEADING: Typically used to describe that a power factor is
        leading the reference value. Note: Leading power factors
        typically indicate capacitive loading.
    :cvar NET: |Forward| - |Reverse|, See 61968-2. Note: In some
        systems, the value passed as a “net” value could become
        negative. In other systems the value passed as a “net” value is
        always a positive number, and rolls-over and rolls-under as
        needed.
    :cvar NONE: Not Applicable (N/A)
    :cvar Q1MINUS_Q4: Q1 minus Q4
    :cvar Q1PLUS_Q2: Reactive positive quadrants. (The term “lagging” is
        preferred.)
    :cvar Q1PLUS_Q3: Quadrants 1 and 3
    :cvar Q1PLUS_Q4: Quadrants 1 and 4 usually represent forward active
        energy
    :cvar Q2MINUS_Q3: Q2 minus Q3
    :cvar Q2PLUS_Q3: Quadrants 2 and 3 usually represent reverse active
        energy
    :cvar Q2PLUS_Q4: Quadrants 2 and 4
    :cvar Q3MINUS_Q2: Q3 minus Q2
    :cvar Q3PLUS_Q4: Reactive negative quadrants. (The term “leading” is
        preferred.)
    :cvar QUADRANT1: Q1 only
    :cvar QUADRANT2: Q2 only
    :cvar QUADRANT3: Q3 only
    :cvar QUADRANT4: Q4 only
    :cvar REVERSE: Reverse Active Energy is equivalent to "Received," or
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
    :cvar TOTAL: |Forward| + |Reverse|, See 61968-2. The sum of the
        commodity in all quadrants Q1+Q2+Q3+Q4. In polyphase metering,
        the total energy register is incremented when the absolute value
        of the sum of the phase energies is greater than zero:
        &amp;lt;img src="HTS_1.PNG" width="217" height="16" border="0"
        alt="graphic"/&amp;gt;
    :cvar TOTAL_BY_PHASE: In polyphase metering, the total by phase
        energy register is incremented when the sum of the absolute
        values of the phase energies is greater than zero: &amp;lt;img
        src="HTS_1.PNG" width="234" height="16" border="0"
        alt="graphic"/&amp;gt; In single phase metering, the formulas
        for “Total” and “Total by phase” collapse to the same
        expression. For communication purposes however, the “Total”
        enumeration should be used with single phase meter data.
    """
    FORWARD = "forward"
    LAGGING = "lagging"
    LEADING = "leading"
    NET = "net"
    NONE = "none"
    Q1MINUS_Q4 = "q1minusQ4"
    Q1PLUS_Q2 = "q1plusQ2"
    Q1PLUS_Q3 = "q1plusQ3"
    Q1PLUS_Q4 = "q1plusQ4"
    Q2MINUS_Q3 = "q2minusQ3"
    Q2PLUS_Q3 = "q2plusQ3"
    Q2PLUS_Q4 = "q2plusQ4"
    Q3MINUS_Q2 = "q3minusQ2"
    Q3PLUS_Q4 = "q3plusQ4"
    QUADRANT1 = "quadrant1"
    QUADRANT2 = "quadrant2"
    QUADRANT3 = "quadrant3"
    QUADRANT4 = "quadrant4"
    REVERSE = "reverse"
    TOTAL = "total"
    TOTAL_BY_PHASE = "totalByPhase"


class HouseCooling(Enum):
    ELECTRIC = "electric"
    HEAT_PUMP = "heatPump"
    NONE = "none"


class HouseHeating(Enum):
    GAS = "gas"
    HEAT_PUMP = "heatPump"
    NONE = "none"
    RESISTANCE = "resistance"


class Ieee1547AbnormalPerfomanceCategory(Enum):
    CATEGORY_I = "CategoryI"
    CATEGORY_II = "CategoryII"
    CATEGORY_III = "CategoryIII"


@dataclass
class Ieee1547ControlSettings:
    class Meta:
        name = "IEEE1547ControlSettings"

    constant_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "constantPowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    constant_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "constantReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_intentional_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceIntentionalDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_max_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMaxFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_max_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMaxVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_min_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMinFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_min_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMinVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    frequency_droop_response_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "frequencyDroopResponseTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    open_loop_response_time_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "openLoopResponseTimeP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    over_frequency_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "overFrequencyDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    over_frequency_droop: Optional[float] = field(
        default=None,
        metadata={
            "name": "overFrequencyDroop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_constant_open_loop: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeConstantOpenLoop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_constant_reference_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeConstantReferenceVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    under_frequency_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "underFrequencyDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    under_frequency_droop: Optional[float] = field(
        default=None,
        metadata={
            "name": "underFrequencyDroop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_q1: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarQ1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_q2: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarQ2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_q3: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarQ3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_q4: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarQ4",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_v1: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarV1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_v2: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarV2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_v3: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarV3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_v4: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarV4",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_watt_p1: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltWattP1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_watt_p2: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltWattP2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_watt_v1: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltWattV1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_watt_v2: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltWattV2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_p1: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarP1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_p2: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarP2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_p3: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarP3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_p4: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarP4",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_q1: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarQ1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_q2: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarQ2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_q3: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarQ3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_q4: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarQ4",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_electronics_connections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rotating_machines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "name": "RotatingMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


class Ieee1547IslandingCategory(Enum):
    """
    See clause 8.2.
    """
    BLACK_START = "BlackStart"
    CAPABLE = "Capable"
    ISOCHRONOUS = "Isochronous"
    UNCATEGORIZED = "Uncategorized"


class Ieee1547NormalPerformanceCategory(Enum):
    CATEGORY_A = "CategoryA"
    CATEGORY_B = "CategoryB"


@dataclass
class Ieee1547TripSettings:
    class Meta:
        name = "IEEE1547TripSettings"

    of1frequency: Optional[object] = field(
        default=None,
        metadata={
            "name": "OF1frequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    of1time: Optional[float] = field(
        default=None,
        metadata={
            "name": "OF1time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    of2frequency: Optional[object] = field(
        default=None,
        metadata={
            "name": "OF2frequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    of2time: Optional[float] = field(
        default=None,
        metadata={
            "name": "OF2time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov1time: Optional[float] = field(
        default=None,
        metadata={
            "name": "OV1time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov1voltage: Optional[object] = field(
        default=None,
        metadata={
            "name": "OV1voltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov2time: Optional[float] = field(
        default=None,
        metadata={
            "name": "OV2time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov2voltage: Optional[object] = field(
        default=None,
        metadata={
            "name": "OV2voltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf1frequency: Optional[object] = field(
        default=None,
        metadata={
            "name": "UF1frequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf1time: Optional[float] = field(
        default=None,
        metadata={
            "name": "UF1time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf2frequency: Optional[object] = field(
        default=None,
        metadata={
            "name": "UF2frequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf2time: Optional[float] = field(
        default=None,
        metadata={
            "name": "UF2time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv1time: Optional[float] = field(
        default=None,
        metadata={
            "name": "UV1time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv1voltage: Optional[object] = field(
        default=None,
        metadata={
            "name": "UV1voltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv2time: Optional[float] = field(
        default=None,
        metadata={
            "name": "UV2time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv2voltage: Optional[object] = field(
        default=None,
        metadata={
            "name": "UV2voltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_electronics_connections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rotating_machines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "name": "RotatingMachines",
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
    :ivar identified_object: Identified object that this name
        designates.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    identified_object: Optional["IdentifiedObject"] = field(
        default=None,
        metadata={
            "name": "IdentifiedObject",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


class NormalOpcatKind(Enum):
    """Kinds of normal operation categories.

    Reference: IEEE1547-2018.

    :cvar CAT_A: Category CAT_A.
    :cvar CAT_B: Category CAT_B.
    """
    CAT_A = "catA"
    CAT_B = "catB"


class OperationalLimitDirectionKind(Enum):
    """
    The direction attribute describes the side of  a limit that is a violation.

    :cvar ABSOLUTE_VALUE: An absoluteValue limit means that a monitored
        absolute value above the limit value is a violation.
    :cvar HIGH: High means that a monitored value above the limit value
        is a violation.   If applied to a terminal flow, the positive
        direction is into the terminal.
    :cvar LOW: Low means a monitored value below the limit is a
        violation.  If applied to a terminal flow, the positive
        direction is into the terminal.
    """
    ABSOLUTE_VALUE = "absoluteValue"
    HIGH = "high"
    LOW = "low"


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
    NS1 = "Ns1"
    NS2 = "Ns2"
    X = "X"
    XN = "XN"
    XY = "XY"
    XYN = "XYN"
    NONE = "none"
    S1 = "s1"
    S12 = "s12"
    S12_N = "s12N"
    S1_N = "s1N"
    S2 = "s2"
    S21 = "s21"
    S21_N = "s21N"
    S2_N = "s2N"


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
    :cvar NONE: No phases specified.
    :cvar S1: Secondary phase 1.
    :cvar S12: Secondary phase 1 and 2.
    :cvar S12_N: Secondary phases 1, 2, and neutral.
    :cvar S1_N: Secondary phase 1 and neutral.
    :cvar S2: Secondary phase 2.
    :cvar S2_N: Secondary phase 2 and neutral.
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
    NONE = "none"
    S1 = "s1"
    S12 = "s12"
    S12_N = "s12N"
    S1_N = "s1N"
    S2 = "s2"
    S2_N = "s2N"


class PhaseConnectedFaultKind(Enum):
    """
    The type of fault connection among phases.

    :cvar LINE_OPEN: The fault is when the conductor path is broken
        between two terminals. Additional coexisting faults may be
        required if the broken conductor also causes connections to
        grounds or other lines or phases.
    :cvar LINE_TO_GROUND: The fault connects the indicated phases to
        ground. The line to line fault impedance is not used and assumed
        infinite. The full ground impedance is connected between each
        phase specified in the fault and ground, but not between the
        phases.
    :cvar LINE_TO_LINE: The fault connects the specified phases together
        without a connection to ground. The ground impedance of this
        fault is ignored. The line to line impedance is connected
        between each of the phases specified in the fault. For example
        three times for a three phase fault, one time for a two phase
        fault.  A single phase fault should not be specified.
    :cvar LINE_TO_LINE_TO_GROUND: The fault connects the indicated
        phases to ground and to each other. The line to line impedance
        is connected between each of the phases specified in the fault
        in a full mesh. For example three times for a three phase fault,
        one time for a two phase fault. A single phase fault should not
        be specified. The full ground impedance is connected between
        each phase specified in the fault and ground.
    """
    LINE_OPEN = "lineOpen"
    LINE_TO_GROUND = "lineToGround"
    LINE_TO_LINE = "lineToLine"
    LINE_TO_LINE_TO_GROUND = "lineToLineToGround"


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
    :cvar YN: Wye, with neutral brought out for grounding.
    """
    D = "D"
    G = "G"
    I = "I"
    Y = "Y"
    YN = "Yn"


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

    :cvar DEFAULT: Randomisation of start and/or end times involving the
        operation of one or more devices is controlled by default
        settings for the device(s).
    :cvar END: End time of an event or control action affecting one or
        more devices is randomised to prevent simultaneous operation.
    :cvar NONE: Neither the start time nor the end time of an event or
        control action affecting one or more devices is randomised.
    :cvar START: Start time of an event or control action affecting one
        or more multiple devices is randomised.
    :cvar START_AND_END: Both the start time and the end time of an
        event or control action affecting one or more devices are
        randomised to prevent simultaneous operation.
    """
    DEFAULT = "default"
    END = "end"
    NONE = "none"
    START = "start"
    START_AND_END = "startAndEnd"


@dataclass
class RegularTimePoint:
    """
    Time point for a schedule where the time between the consecutive points is
    constant.

    :ivar sequence_number: The position of the regular time point in the
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
    :ivar interval_schedule: Regular interval schedule containing this
        time point.
    """
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
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
    interval_schedule: Optional["RegularIntervalSchedule"] = field(
        default=None,
        metadata={
            "name": "IntervalSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


class RegulatingControlModeKind(Enum):
    """The kind of regulation model.

    For example regulating voltage, reactive power, active power, etc.

    :cvar ACTIVE_POWER: Active power is specified.
    :cvar ADMITTANCE: Admittance is specified.
    :cvar CURRENT_FLOW: Current flow is specified.
    :cvar POWER_FACTOR: Power factor is specified.
    :cvar REACTIVE_POWER: Reactive power is specified.
    :cvar TEMPERATURE: Control switches on/off based on the local
        temperature (i.e., a thermostat).
    :cvar TIME_SCHEDULED: Control switches on/off by time of day. The
        times may change on the weekend, or in different seasons.
    :cvar VOLTAGE: Voltage is specified.
    """
    ACTIVE_POWER = "activePower"
    ADMITTANCE = "admittance"
    CURRENT_FLOW = "currentFlow"
    POWER_FACTOR = "powerFactor"
    REACTIVE_POWER = "reactivePower"
    TEMPERATURE = "temperature"
    TIME_SCHEDULED = "timeScheduled"
    VOLTAGE = "voltage"


class RemoteSignalKind(Enum):
    """
    Type of input signal coming from remote bus.

    :cvar REMOTE_BRANCH_CURRENT_AMPLITUDE: Input is branch current
        amplitude from remote terminal bus.
    :cvar REMOTE_BUS_FREQUENCY: Input is frequency from remote terminal
        bus.
    :cvar REMOTE_BUS_FREQUENCY_DEVIATION: Input is frequency deviation
        from remote terminal bus.
    :cvar REMOTE_BUS_VOLTAGE: Input is voltage from remote terminal bus.
    :cvar REMOTE_BUS_VOLTAGE_AMPLITUDE: Input is voltage amplitude from
        remote terminal bus.
    :cvar REMOTE_BUS_VOLTAGE_AMPLITUDE_DERIVATIVE: Input is branch
        current amplitude derivative from remote terminal bus.
    :cvar REMOTE_BUS_VOLTAGE_FREQUENCY: Input is voltage frequency from
        remote terminal bus.
    :cvar REMOTE_BUS_VOLTAGE_FREQUENCY_DEVIATION: Input is voltage
        frequency deviation from remote terminal bus.
    :cvar REMOTE_PU_BUS_VOLTAGE_DERIVATIVE: Input is PU voltage
        derivative from remote terminal bus.
    """
    REMOTE_BRANCH_CURRENT_AMPLITUDE = "remoteBranchCurrentAmplitude"
    REMOTE_BUS_FREQUENCY = "remoteBusFrequency"
    REMOTE_BUS_FREQUENCY_DEVIATION = "remoteBusFrequencyDeviation"
    REMOTE_BUS_VOLTAGE = "remoteBusVoltage"
    REMOTE_BUS_VOLTAGE_AMPLITUDE = "remoteBusVoltageAmplitude"
    REMOTE_BUS_VOLTAGE_AMPLITUDE_DERIVATIVE = "remoteBusVoltageAmplitudeDerivative"
    REMOTE_BUS_VOLTAGE_FREQUENCY = "remoteBusVoltageFrequency"
    REMOTE_BUS_VOLTAGE_FREQUENCY_DEVIATION = "remoteBusVoltageFrequencyDeviation"
    REMOTE_PU_BUS_VOLTAGE_DERIVATIVE = "remotePuBusVoltageDerivative"


class SinglePhaseKind(Enum):
    """Enumeration of single phase identifiers.

    Allows designation of single phases for both transmission and
    distribution equipment, circuits and loads.

    :cvar A: Phase A.
    :cvar B: Phase B.
    :cvar C: Phase C.
    :cvar N: Neutral.
    :cvar S1: Secondary phase 1.
    :cvar S2: Secondary phase 2.
    """
    A = "A"
    B = "B"
    C = "C"
    N = "N"
    S1 = "s1"
    S2 = "s2"


@dataclass
class StateVariable:
    """
    An abstract class for state variables.
    """


@dataclass
class Status:
    """
    Current status information relevant to an entity.

    :ivar date_time: Date and time for which status 'value' applies.
    :ivar reason: Reason code or explanation for why an object went to
        the current status 'value'.
    :ivar remark: Pertinent information regarding the current 'value',
        as free form text.
    :ivar value: Status value at 'dateTime'; prior status changes may
        have been kept in instances of activity records associated with
        the object to which this status applies.
    """
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dateTime",
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
    COOLING = "Cooling"
    HEATING = "Heating"


class TimeIntervalKind(Enum):
    D = "D"
    M = "M"
    Y = "Y"
    H = "h"
    M_1 = "m"
    S = "s"


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
    :cvar A: atto 10**-18.
    :cvar C: Centi 10**-2.
    :cvar D: Deci 10**-1.
    :cvar DA: deca 10**1.
    :cvar F: femto 10**-15.
    :cvar H: hecto 10**2.
    :cvar K: Kilo 10**3.
    :cvar M_1: Milli 10**-3.
    :cvar MICRO: Micro 10**-6.
    :cvar N: Nano 10**-9.
    :cvar NONE: No multiplier or equivalently multiply by 1.
    :cvar P_1: Pico 10**-12.
    :cvar Y_1: yocto 10**-24.
    :cvar Z_1: zepto 10**-21.
    """
    E = "E"
    G = "G"
    M = "M"
    P = "P"
    T = "T"
    Y = "Y"
    Z = "Z"
    A = "a"
    C = "c"
    D = "d"
    DA = "da"
    F = "f"
    H = "h"
    K = "k"
    M_1 = "m"
    MICRO = "micro"
    N = "n"
    NONE = "none"
    P_1 = "p"
    Y_1 = "y"
    Z_1 = "z"


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
    :cvar A2H: ampere-squared hour, Ampere-squared hour.
    :cvar A2S: Ampere squared time in square ampere (A²s).
    :cvar APER_A: Current, Ratio of Amperages  Note: Users may need to
        supply a prefix such as ‘m’ to show rates such as ‘mA/A’.
    :cvar APERM: A/m, magnetic field strength, Ampere per metre.
    :cvar AH: Ampere-hours, Ampere-hours.
    :cvar AS: Ampere seconds (A·s).
    :cvar BQ: Radioactivity in Becquerel (1/s).
    :cvar BTU: Energy, British Thermal Unit.
    :cvar C: Electric charge in Coulomb (A·s).
    :cvar CPERKG: exposure (x rays), Coulomb per kilogram.
    :cvar CPERM2: surface charge density, Coulomb per square metre.
    :cvar CPERM3: electric charge density, Coulomb per cubic metre.
    :cvar F: Electric capacitance in Farad (C/V).
    :cvar FPERM: permittivity, Farad per metre.
    :cvar G: Magnetic flux density, Gauss (1 G = 10-4 T).
    :cvar GY: Absorbed dose in Gray (J/kg).
    :cvar GY_PERS: absorbed dose rate, Gray per second.
    :cvar H: Electric inductance in Henry (Wb/A).
    :cvar HPERM: permeability, Henry per metre.
    :cvar HZ: Frequency in Hertz (1/s).
    :cvar HZ_PER_HZ: Frequency, Rate of frequency change  Note: Users
        may need to supply a prefix such as ‘m’ to show rates such as
        ‘mHz/Hz’.
    :cvar HZ_PERS: Rate of change of frequency in Hertz per second.
    :cvar J: Energy in joule (N·m = C·V = W·s).
    :cvar JPER_K: Heat capacity in Joule/Kelvin.
    :cvar JPERKG: Specific energy, Joule / kg.
    :cvar JPERKG_K: Specific heat capacity, specific entropy, Joule per
        kilogram Kelvin.
    :cvar JPERM2: Insulation energy density, Joule per square metre or
        watt second per square metre.
    :cvar JPERM3: energy density, Joule per cubic metre.
    :cvar JPERMOL: molar energy, Joule per mole.
    :cvar JPERMOL_K: molar entropy, molar heat capacity, Joule per mole
        kelvin.
    :cvar JPERS: Energy rate joule per second (J/s),
    :cvar K: Temperature in Kelvin.
    :cvar KPERS: Temperature change rate in Kelvin per second.
    :cvar M: Length, nautical mile (1 M = 1852 m).
    :cvar MX: Magnetic flux, Maxwell (1 Mx = 10-8 Wb).
    :cvar N: Force in Newton (kg·m/s²).
    :cvar NPERM: Surface tension, Newton per metre.
    :cvar NM: Moment of force, Newton metre.
    :cvar OE: Magnetic field, Œrsted (1 Oe = (103/4p) A/m).
    :cvar PA: Pressure in Pascal (N/m²). Note: the absolute or relative
        measurement of pressure is implied with this entry. See below
        for more explicit forms.
    :cvar PA_PERS: Pressure change rate in Pascal per second.
    :cvar PAS: Dynamic viscosity, Pascal second.
    :cvar Q: Quantity power, Q.
    :cvar QH: Quantity energy, Qh.
    :cvar S: Conductance in Siemens.
    :cvar SPERM: Conductance per length (F/m).
    :cvar SV: Dose equivalent in Sievert (J/kg).
    :cvar T: Magnetic flux density in Tesla (Wb/m2).
    :cvar V: Electric potential in Volt (W/A).
    :cvar V2: Volt squared (W²/A²).
    :cvar V2H: volt-squared hour, Volt-squared-hours.
    :cvar VA: Apparent power in Volt Ampere (See also real power and
        reactive power.)
    :cvar VAH: Apparent energy in Volt Ampere hours.
    :cvar VAR: Reactive power in Volt Ampere reactive. The “reactive” or
        “imaginary” component of electrical power (VIsin(phi)). (See
        also real power and apparent power). Note: Different meter
        designs use different methods to arrive at their results. Some
        meters may compute reactive power as an arithmetic value, while
        others compute the value vectorially. The data consumer should
        determine the method in use and the suitability of the
        measurement for the intended purpose.
    :cvar VARH: Reactive energy in Volt Ampere reactive hours.
    :cvar VPER_HZ: Magnetic flux in Volt per Hertz.
    :cvar VPER_V: Voltage, Ratio of voltages Note: Users may need to
        supply a prefix such as ‘m’ to show rates such as ‘mV/V’.
    :cvar VPER_VA: Power factor, PF, the ratio of the active power to
        the apparent power. Note: The sign convention used for power
        factor will differ between IEC meters and EEI (ANSI) meters. It
        is assumed that the data consumers understand the type of meter
        being used and agree on the sign convention in use at any given
        utility.
    :cvar VPER_VAR: Power factor, PF, the ratio of the active power to
        the apparent power. Note: The sign convention used for power
        factor will differ between IEC meters and EEI (ANSI) meters. It
        is assumed that the data consumers understand the type of meter
        being used and agree on the sign convention in use at any given
        utility.
    :cvar VPERM: electric field strength, Volt per metre.
    :cvar VH: Volt-hour, Volt hours.
    :cvar VS: Volt second (Ws/A).
    :cvar W: Real power in Watt (J/s). Electrical power may have real
        and reactive components. The real portion of electrical power
        (I²R or VIcos(phi)), is expressed in Watts. (See also apparent
        power and reactive power.)
    :cvar WPER_A: Active power per current flow, watt per Ampere.
    :cvar WPER_W: Signal Strength, Ratio of power  Note: Users may need
        to supply a prefix such as ‘m’ to show rates such as ‘mW/W’.
    :cvar WPERM2: Heat flux density, irradiance, Watt per square metre.
    :cvar WPERM2SR: radiance, Watt per square metre steradian.
    :cvar WPERM_K: Thermal conductivity in Watt/metre Kelvin.
    :cvar WPERS: Ramp rate in Watt per second.
    :cvar WPERSR: Radiant intensity, Watt per steradian.
    :cvar WB: Magnetic flux in Weber (V·s).
    :cvar WH: Real energy in Watt hours.
    :cvar ANGLEMIN: Plane angle, minute.
    :cvar ANGLESEC: Plane angle, second.
    :cvar BAR: Pressure, bar (1 bar = 100 kPa).
    :cvar CD: Luminous intensity in candela.
    :cvar CHAR_PERS: Data rate (baud) in characters per second.
    :cvar CHARACTER: Number of characters.
    :cvar COS_PHI: Power factor, dimensionless. Note 1: This definition
        of power factor only holds for balanced systems. See the
        alternative definition under code 153. Note 2 : Beware of
        differing sign conventions in use between the IEC and EEI. It is
        assumed that the data consumer understands the type of meter in
        use and the sign convention in use by the utility.
    :cvar COUNT: Amount of substance, Counter value.
    :cvar D: Time, day = 24 h = 86400 s.
    :cvar D_B: Sound pressure level in decibel. Note:  multiplier “d” is
        included in this unit symbol for compatibility with IEC
        61850-7-3.
    :cvar D_BM: Power level (logrithmic ratio of signal strength , Bel-
        mW), normalized to 1mW. Note:  multiplier “d” is included in
        this unit symbol for compatibility with IEC 61850-7-3.
    :cvar DEG: Plane angle in degrees.
    :cvar DEG_C: Relative temperature in degrees Celsius. In the SI unit
        system the symbol is ºC. Electric charge is measured in coulomb
        that has the unit symbol C. To distinguish degree Celsius form
        coulomb the symbol used in the UML is degC. Reason for not using
        ºC is the special character º is difficult to manage in
        software.
    :cvar FT3: Volume, cubic foot.
    :cvar G_PERG: Concentration, The ratio of the mass of a solute
        divided by the mass of  the solution. Note: Users may need use a
        prefix such a ‘µ’ to express a quantity such as ‘µg/g’.
    :cvar GAL: Volume, US gallon (1 gal = 231 in3 = 128 fl ounce).
    :cvar H_1: Time, hour = 60 min = 3600 s.
    :cvar HA: Area, hectare.
    :cvar KAT: Catalytic activity, katal = mol / s.
    :cvar KAT_PERM3: catalytic activity concentration, katal per cubic
        metre.
    :cvar KG: Mass in kilogram.  Note: multiplier “k” is included in
        this unit symbol for compatibility with IEC 61850-7-3.
    :cvar KG_PER_J: Weigh per energy in kilogram/joule (kg/J). Note:
        multiplier “k” is included in this unit symbol for compatibility
        with IEC 61850-7-3.
    :cvar KG_PERM3: Density in kilogram/cubic metre (kg/m³). Note:
        multiplier “k” is included in this unit symbol for compatibility
        with IEC 61850-7-3.
    :cvar KGM: Moment of mass in kilogram metre (kg·m) (first moment of
        mass). Note: multiplier “k” is included in this unit symbol for
        compatibility with IEC 61850-7-3.
    :cvar KGM2: Moment of mass in kilogram square metre (kg·m²) (Second
        moment of mass, commonly called the moment of inertia). Note:
        multiplier “k” is included in this unit symbol for compatibility
        with IEC 61850-7-3.
    :cvar KN: Speed, knot (1 kn = 1852/3600) m/s.
    :cvar L: Volume, litre = dm3 = m3/1000.
    :cvar L_PERH: Volumetric flow rate, litre per hour.
    :cvar L_PERL: Concentration, The ratio of the volume of a solute
        divided by the volume of  the solution. Note: Users may need use
        a prefix such a ‘µ’ to express a quantity such as ‘µL/L’.
    :cvar L_PERS: Volumetric flow rate in litre per second.
    :cvar LM: Luminous flux in lumen (cd·sr).
    :cvar LX: Illuminance in lux (lm/m²).
    :cvar M_1: Length in meter.
    :cvar M2: Area in square metre (m²).
    :cvar M2_PERS: Viscosity in metre square / second (m²/s).
    :cvar M3: Volume in cubic metre (m³).
    :cvar M3_COMPENSATED: Volume, cubic metre, with the value
        compensated for weather effects.
    :cvar M3_PERH: Volumetric flow rate, cubic metre per hour.
    :cvar M3_PERKG: Specific volume, cubic metre per kilogram, v.
    :cvar M3_PERS: Volumetric flow rate in cubic metres per second
        (m³/s).
    :cvar M3_UNCOMPENSATED: Volume, cubic metre, with the value
        uncompensated for weather effects.
    :cvar M_PERM3: Fuel efficiency in metre per cubic metre (m/m³).
    :cvar M_PERS: Velocity in metre per second (m/s).
    :cvar M_PERS2: Acceleration in metre per second squared (m/s²).
    :cvar MIN: Time, minute  = 60 s.
    :cvar MM_HG: Pressure, millimeter of mercury (1 mmHg is
        approximately 133.3 Pa).
    :cvar MOL: Amount of substance in mole.
    :cvar MOL_PERKG: Concentration, Molality, the amount of solute in
        moles and the amount of solvent in kilograms.
    :cvar MOL_PERM3: Concentration, The amount of substance
        concentration, (c), the amount of solvent in moles divided by
        the volume of solution in m³.
    :cvar MOL_PERMOL: Concentration, Molar fraction (?), the ratio of
        the molar amount of a solute divided by the molar amount of the
        solution.
    :cvar NONE: Dimension less quantity, e.g. count, per unit, etc.
    :cvar OHM: Electric resistance in ohm (V/A).
    :cvar OHM_PERM: Electric resistance per length in ohm per metre
        ((V/A)/m).
    :cvar OHMM: resistivity, Ohm metre, (rho).
    :cvar ONE_PER_HZ: Reciprocal of frequency (1/Hz).
    :cvar ONE_PERM: Wavenumber, reciprocal metre,  (1/m).
    :cvar PPM: Concentration in parts per million.
    :cvar RAD: Plane angle in radian (m/m).
    :cvar RAD_PERS: Angular velocity in radians per second (rad/s).
    :cvar RAD_PERS2: Angular acceleration, radian per second squared.
    :cvar REV: Amount of rotation, Revolutions.
    :cvar ROT_PERS: Rotations per second (1/s). See also Hz (1/s).
    :cvar S_1: Time in seconds.
    :cvar S_PERS: Time, Ratio of time Note: Users may need to supply a
        prefix such as ‘µ’ to show rates such as ‘µs/s’
    :cvar SR: Solid angle in steradian (m2/m2).
    :cvar THERM: Energy, Therm.
    :cvar TONNE: mass, “tonne” or “metric  ton” (1000 kg = 1 Mg).
    """
    A = "A"
    A2 = "A2"
    A2H = "A2h"
    A2S = "A2s"
    APER_A = "APerA"
    APERM = "APerm"
    AH = "Ah"
    AS = "As"
    BQ = "Bq"
    BTU = "Btu"
    C = "C"
    CPERKG = "CPerkg"
    CPERM2 = "CPerm2"
    CPERM3 = "CPerm3"
    F = "F"
    FPERM = "FPerm"
    G = "G"
    GY = "Gy"
    GY_PERS = "GyPers"
    H = "H"
    HPERM = "HPerm"
    HZ = "Hz"
    HZ_PER_HZ = "HzPerHz"
    HZ_PERS = "HzPers"
    J = "J"
    JPER_K = "JPerK"
    JPERKG = "JPerkg"
    JPERKG_K = "JPerkgK"
    JPERM2 = "JPerm2"
    JPERM3 = "JPerm3"
    JPERMOL = "JPermol"
    JPERMOL_K = "JPermolK"
    JPERS = "JPers"
    K = "K"
    KPERS = "KPers"
    M = "M"
    MX = "Mx"
    N = "N"
    NPERM = "NPerm"
    NM = "Nm"
    OE = "Oe"
    PA = "Pa"
    PA_PERS = "PaPers"
    PAS = "Pas"
    Q = "Q"
    QH = "Qh"
    S = "S"
    SPERM = "SPerm"
    SV = "Sv"
    T = "T"
    V = "V"
    V2 = "V2"
    V2H = "V2h"
    VA = "VA"
    VAH = "VAh"
    VAR = "VAr"
    VARH = "VArh"
    VPER_HZ = "VPerHz"
    VPER_V = "VPerV"
    VPER_VA = "VPerVA"
    VPER_VAR = "VPerVAr"
    VPERM = "VPerm"
    VH = "Vh"
    VS = "Vs"
    W = "W"
    WPER_A = "WPerA"
    WPER_W = "WPerW"
    WPERM2 = "WPerm2"
    WPERM2SR = "WPerm2sr"
    WPERM_K = "WPermK"
    WPERS = "WPers"
    WPERSR = "WPersr"
    WB = "Wb"
    WH = "Wh"
    ANGLEMIN = "anglemin"
    ANGLESEC = "anglesec"
    BAR = "bar"
    CD = "cd"
    CHAR_PERS = "charPers"
    CHARACTER = "character"
    COS_PHI = "cosPhi"
    COUNT = "count"
    D = "d"
    D_B = "dB"
    D_BM = "dBm"
    DEG = "deg"
    DEG_C = "degC"
    FT3 = "ft3"
    G_PERG = "gPerg"
    GAL = "gal"
    H_1 = "h"
    HA = "ha"
    KAT = "kat"
    KAT_PERM3 = "katPerm3"
    KG = "kg"
    KG_PER_J = "kgPerJ"
    KG_PERM3 = "kgPerm3"
    KGM = "kgm"
    KGM2 = "kgm2"
    KN = "kn"
    L = "l"
    L_PERH = "lPerh"
    L_PERL = "lPerl"
    L_PERS = "lPers"
    LM = "lm"
    LX = "lx"
    M_1 = "m"
    M2 = "m2"
    M2_PERS = "m2Pers"
    M3 = "m3"
    M3_COMPENSATED = "m3Compensated"
    M3_PERH = "m3Perh"
    M3_PERKG = "m3Perkg"
    M3_PERS = "m3Pers"
    M3_UNCOMPENSATED = "m3Uncompensated"
    M_PERM3 = "mPerm3"
    M_PERS = "mPers"
    M_PERS2 = "mPers2"
    MIN = "min"
    MM_HG = "mmHg"
    MOL = "mol"
    MOL_PERKG = "molPerkg"
    MOL_PERM3 = "molPerm3"
    MOL_PERMOL = "molPermol"
    NONE = "none"
    OHM = "ohm"
    OHM_PERM = "ohmPerm"
    OHMM = "ohmm"
    ONE_PER_HZ = "onePerHz"
    ONE_PERM = "onePerm"
    PPM = "ppm"
    RAD = "rad"
    RAD_PERS = "radPers"
    RAD_PERS2 = "radPers2"
    REV = "rev"
    ROT_PERS = "rotPers"
    S_1 = "s"
    S_PERS = "sPers"
    SR = "sr"
    THERM = "therm"
    TONNE = "tonne"


class UsagePointConnectedKind(Enum):
    """
    State of the usage point with respect to connection to the network.

    :cvar CONNECTED: The usage point is connected to the network and
        able to receive or send the applicable commodity (electricity,
        gas, water, etc.).
    :cvar LOGICALLY_DISCONNECTED: The usage point has been disconnected
        through operation of a disconnect function within the meter
        present at the usage point.  The usage point is unable to
        receive or send the applicable commodity (electricity, gas,
        water, etc.)  A logical disconnect can often be achieved without
        utilising a field crew.
    :cvar PHYSICALLY_DISCONNECTED: The usage point has been disconnected
        from the network at a point upstream of the meter. The usage
        point is unable to receive or send the applicable commodity
        (electricity, gas, water, etc.). A physical disconnect is often
        achieved by utilising a field crew.
    """
    CONNECTED = "connected"
    LOGICALLY_DISCONNECTED = "logicallyDisconnected"
    PHYSICALLY_DISCONNECTED = "physicallyDisconnected"


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
    :cvar YN: Wye, with neutral brought out for grounding.
    :cvar Z: ZigZag
    :cvar ZN: ZigZag, with neutral brought out for grounding.
    """
    A = "A"
    D = "D"
    I = "I"
    Y = "Y"
    YN = "Yn"
    Z = "Z"
    ZN = "Zn"


class WireInsulationKind(Enum):
    """
    Kind of wire insulation.

    :cvar ASBESTOS_AND_VARNISHED_CAMBRIC: Asbestos and varnished cambric
        wire insulation.
    :cvar BELTED_PILC: Belted pilc wire insulation.
    :cvar BUTYL: Butyl wire insulation.
    :cvar CROSSLINKED_POLYETHYLENE: Crosslinked polyethylene wire
        insulation.
    :cvar ETHYLENE_PROPYLENE_RUBBER: Ethylene propylene rubber wire
        insulation.
    :cvar HIGH_MOLECULAR_WEIGHT_POLYETHYLENE: High nolecular weight
        polyethylene wire insulation.
    :cvar HIGH_PRESSURE_FLUID_FILLED: High pressure fluid filled wire
        insulation.
    :cvar LOW_CAPACITANCE_RUBBER: Low capacitance rubber wire
        insulation.
    :cvar OIL_PAPER: Oil paper wire insulation.
    :cvar OTHER: Other kind of wire insulation.
    :cvar OZONE_RESISTANT_RUBBER: Ozone resistant rubber wire
        insulation.
    :cvar RUBBER: Rubber wire insulation.
    :cvar SILICON_RUBBER: Silicon rubber wire insulation.
    :cvar TREE_RESISTANT_HIGH_MOLECULAR_WEIGHT_POLYETHYLENE: Tree
        resistant high molecular weight polyethylene wire insulation.
    :cvar TREE_RETARDANT_CROSSLINKED_POLYETHYLENE: Tree retardant
        crosslinked polyethylene wire insulation.
    :cvar UNBELTED_PILC: Unbelted pilc wire insulation.
    :cvar VARNISHED_CAMBRIC_CLOTH: Varnished cambric cloth wire
        insulation.
    :cvar VARNISHED_DACRON_GLASS: Varnished dacron glass wire
        insulation.
    """
    ASBESTOS_AND_VARNISHED_CAMBRIC = "asbestosAndVarnishedCambric"
    BELTED_PILC = "beltedPilc"
    BUTYL = "butyl"
    CROSSLINKED_POLYETHYLENE = "crosslinkedPolyethylene"
    ETHYLENE_PROPYLENE_RUBBER = "ethylenePropyleneRubber"
    HIGH_MOLECULAR_WEIGHT_POLYETHYLENE = "highMolecularWeightPolyethylene"
    HIGH_PRESSURE_FLUID_FILLED = "highPressureFluidFilled"
    LOW_CAPACITANCE_RUBBER = "lowCapacitanceRubber"
    OIL_PAPER = "oilPaper"
    OTHER = "other"
    OZONE_RESISTANT_RUBBER = "ozoneResistantRubber"
    RUBBER = "rubber"
    SILICON_RUBBER = "siliconRubber"
    TREE_RESISTANT_HIGH_MOLECULAR_WEIGHT_POLYETHYLENE = "treeResistantHighMolecularWeightPolyethylene"
    TREE_RETARDANT_CROSSLINKED_POLYETHYLENE = "treeRetardantCrosslinkedPolyethylene"
    UNBELTED_PILC = "unbeltedPilc"
    VARNISHED_CAMBRIC_CLOTH = "varnishedCambricCloth"
    VARNISHED_DACRON_GLASS = "varnishedDacronGlass"


class WireMaterialKind(Enum):
    """
    Kind of wire material.

    :cvar AAAC: Aluminum-alloy conductor steel reinforced.
    :cvar ACSR: Aluminum conductor steel reinforced.
    :cvar ALUMINUM: Aluminum wire.
    :cvar ALUMINUM_ALLOY: Aluminum-alloy wire.
    :cvar ALUMINUM_ALLOY_STEEL: Aluminum-alloy-steel wire.
    :cvar ALUMINUM_STEEL: Aluminum-steel wire.
    :cvar COPPER: Copper wire.
    :cvar OTHER: Other wire material.
    :cvar STEEL: Steel wire.
    """
    AAAC = "aaac"
    ACSR = "acsr"
    ALUMINUM = "aluminum"
    ALUMINUM_ALLOY = "aluminumAlloy"
    ALUMINUM_ALLOY_STEEL = "aluminumAlloySteel"
    ALUMINUM_STEEL = "aluminumSteel"
    COPPER = "copper"
    OTHER = "other"
    STEEL = "steel"


@dataclass
class Derdynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to DER dynamics models.

    :ivar power_electronics_connection: Power electronics connection
        with which this DER dynamics model is associated.
    :ivar remote_input_signals:
    :ivar synchronous_machine: Synchronous machine model with which this
        DER dynamics model is associated.
    """
    class Meta:
        name = "DERDynamics"

    power_electronics_connection: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    remote_input_signals: List["RemoteInputSignal"] = field(
        default_factory=list,
        metadata={
            "name": "RemoteInputSignals",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    synchronous_machine: List["SynchronousMachine"] = field(
        default_factory=list,
        metadata={
            "name": "SynchronousMachine",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DispatchSchedule:
    """
    :ivar confidence:
    :ivar curve_style_kind: Used to specify whether the values over an
        interval are constant (constantYValue) or linearly interpolated
        (straightLineYValues)
    :ivar number_of_intervals: Used to specify the number of intervals
        when requesting a forecast or a dispatch.
    :ivar start_time: The start time of the first interval in the
        dispatch schedule
    :ivar time_interval_duration: The length of time for each interval
        in the dispatch schedule.
    :ivar time_interval_unit: The unit of measure for the time axis of
        the dispatch schedule.
    :ivar dercurve_data:
    :ivar dermonitorable_parameter:
    """
    confidence: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_style_kind: Optional[CurveStyle] = field(
        default=None,
        metadata={
            "name": "curveStyleKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    number_of_intervals: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfIntervals",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_interval_duration: Optional[int] = field(
        default=None,
        metadata={
            "name": "timeIntervalDuration",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    time_interval_unit: Optional[TimeIntervalKind] = field(
        default=None,
        metadata={
            "name": "timeIntervalUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dercurve_data: List["DercurveData"] = field(
        default_factory=list,
        metadata={
            "name": "DERCurveData",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dermonitorable_parameter: Optional["DermonitorableParameter"] = field(
        default=None,
        metadata={
            "name": "DERMonitorableParameter",
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
    :ivar duration_indefinite: True if 'duration' is indefinite.
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
    duration_indefinite: Optional[bool] = field(
        default=None,
        metadata={
            "name": "durationIndefinite",
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

    :ivar m_rid: Master resource identifier issued by a model authority.
        The mRID is unique within an exchange context. Global uniqueness
        is easily achieved by using a UUID,  as specified in RFC 4122,
        for the mRID. The use of UUID is strongly recommended. For
        CIMXML data files in RDF syntax conforming to IEC 61970-552
        Edition 1, the mRID is mapped to rdf:ID or rdf:about attributes
        that identify CIM object elements.
    :ivar alias_name: The aliasName is free text human readable name of
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
    :ivar names: All names of this identified object.
    """
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    alias_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "aliasName",
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
    names: List[Name] = field(
        default_factory=list,
        metadata={
            "name": "Names",
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
    :ivar terminal: The terminal associated with the power flow state
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
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
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
    :ivar shunt_compensator: The shunt compensator for which the state
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
    shunt_compensator: Optional["ShuntCompensator"] = field(
        default=None,
        metadata={
            "name": "ShuntCompensator",
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
    :ivar conducting_equipment: The conducting equipment associated with
        the status state variable.
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    conducting_equipment: Optional["ConductingEquipment"] = field(
        default=None,
        metadata={
            "name": "ConductingEquipment",
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
    :ivar tap_changer: The tap changer associated with the tap step
        state.
    """
    position: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    tap_changer: Optional["TapChanger"] = field(
        default=None,
        metadata={
            "name": "TapChanger",
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
    :ivar connectivity_node:
    :ivar topological_node: The topological node associated with the
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
    connectivity_node: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    topological_node: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class BasicIntervalSchedule(IdentifiedObject):
    """
    Schedule of values at points in time.

    :ivar start_time: The time for the first time point.  The value can
        be a time of day, not a specific date.
    :ivar value1_multiplier: Multiplier for value1.
    :ivar value1_unit: Value1 units of measure.
    :ivar value2_multiplier: Multiplier for value2.
    :ivar value2_unit: Value2 units of measure.
    """
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value1_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "value1Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value1_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "value1Unit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value2_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "value2Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    value2_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "value2Unit",
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
    :ivar reactive_power: Injecting reactive power setting (CONST_Q).
        Per unit value based on NP_Q_MAX_INJ. Negative signs should not
        be used but if present, indicates absorbing VAr based on
        NP_Q_MAX_ABS. Typical value = 0.
    :ivar derieeetype1: DER IEEE type 1 model associated with this
        constant reactive power settings  model.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "reactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class CoordinateSystem(IdentifiedObject):
    """
    Coordinate reference system.

    :ivar crs_urn: A Uniform Resource Name (URN) for the coordinate
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
    :ivar locations: All locations described with position points in
        this coordinate system.
    """
    crs_urn: Optional[str] = field(
        default=None,
        metadata={
            "name": "crsUrn",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    locations: List["Location"] = field(
        default_factory=list,
        metadata={
            "name": "Locations",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Curve(IdentifiedObject):
    """
    A multi-purpose curve or functional relationship between an independent
    variable (X-axis) and dependent (Y-axis) variables.

    :ivar curve_style: The style or shape of the curve.
    :ivar x_multiplier: Multiplier for X-axis.
    :ivar x_unit: The X-axis units of measure.
    :ivar y1_multiplier: Multiplier for Y1-axis.
    :ivar y1_unit: The Y1-axis units of measure.
    :ivar y2_multiplier: Multiplier for Y2-axis.
    :ivar y2_unit: The Y2-axis units of measure.
    :ivar y3_multiplier: Multiplier for Y3-axis.
    :ivar y3_unit: The Y3-axis units of measure.
    :ivar curve_datas: The point data values that define this curve.
    """
    curve_style: Optional[CurveStyle] = field(
        default=None,
        metadata={
            "name": "curveStyle",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "xMultiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "xUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y1_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "y1Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y1_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "y1Unit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y2_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "y2Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y2_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "y2Unit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y3_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "y3Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y3_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "y3Unit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_datas: List[CurveData] = field(
        default_factory=list,
        metadata={
            "name": "CurveDatas",
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
    :ivar puc_number: (if applicable) Public utilities commission (PUC)
        identification number.
    :ivar special_need: True if customer organisation has special
        service needs such as life support, hospitals, etc.
    :ivar vip: (use 'priority' instead) True if this is an important
        customer. Importance is for matters different than those in
        'specialNeed' attribute.
    :ivar configuration_events: All configuration events created for
        this organisation role.
    :ivar end_devices: All end devices of this customer.
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
    puc_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "pucNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    special_need: Optional[str] = field(
        default=None,
        metadata={
            "name": "specialNeed",
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
    configuration_events: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_devices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
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
class DercurveData:
    class Meta:
        name = "DERCurveData"

    interval_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "intervalNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    max_yvalue: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxYValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    min_yvalue: Optional[float] = field(
        default=None,
        metadata={
            "name": "minYValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    nominal_yvalue: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalYValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dermonitorable_parameter: Optional["DermonitorableParameter"] = field(
        default=None,
        metadata={
            "name": "DERMonitorableParameter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    dispatch_schedule: Optional[DispatchSchedule] = field(
        default=None,
        metadata={
            "name": "DispatchSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DergroupDispatch(IdentifiedObject):
    class Meta:
        name = "DERGroupDispatch"

    end_device_group: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DergroupForecast(IdentifiedObject):
    class Meta:
        name = "DERGroupForecast"

    prediction_creation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "predictionCreationDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_group: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class DernameplateDataApplied(IdentifiedObject):
    """Capability related settings that may be changed (applied) at the time of
    commissioning or testing the DER.

    Settings in DERNameplateData are specified by the utility before
    commissioning, and usually not changed. Reference: IEEE 1547-2018
    and IEEE 1547.1-2020.

    :ivar ac_vnom: Voltage Base Nominal AC voltage rating in RMS Vac
        (NP_AC_V_NOM).
    :ivar apparent_power_charge_max: Maximum apparent power charge
        rating in kilo Volt Amperes.  May differ from the apparent power
        maximum rating. (NP_APPARENT_POWER_CHARGE_MAX).
    :ivar over_pf: Over-excited power factor (NP_OVER_PF).
    :ivar p_max: Active power rating in kilowatts at unity power factor
        (NP_P_MAX).
    :ivar p_max_charge: Maximum active power charge rating in kilowatts
        (NP_P_MAX_CHARGE).
    :ivar p_max_over_pf: Active power rating in kilowatts at specified
        over-excited power factor (NP_P_MAX_OVER_PF).
    :ivar p_max_under_pf: Active power rating in kilowatts at specified
        under-excited power factor (NP_P_MAX_UNDER_PF).
    :ivar q_max_abs: Maximum absorbed reactive power rating in kilovolt-
        amperes reactive  (NP_Q_MAX_ABS).
    :ivar q_max_inj: Maximum injected reactive power rating in kilovolt-
        amperes reactive  (NP_Q_MAX_INJ).
    :ivar s_max: Maximum apparent power rating in kilovolt-amperes
        (NP_VA_MAX).
    :ivar under_pf: Under-excited power factor (NP_UNDER_PF).
    :ivar dernameplate_data: The DER nameplate data to which this DER
        data is applied.
    """
    class Meta:
        name = "DERNameplateDataApplied"

    ac_vnom: Optional[float] = field(
        default=None,
        metadata={
            "name": "acVnom",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    apparent_power_charge_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "apparentPowerChargeMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    over_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "overPF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "pMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_max_charge: Optional[float] = field(
        default=None,
        metadata={
            "name": "pMaxCharge",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_max_over_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "pMaxOverPF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_max_under_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "pMaxUnderPF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q_max_abs: Optional[float] = field(
        default=None,
        metadata={
            "name": "qMaxAbs",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q_max_inj: Optional[float] = field(
        default=None,
        metadata={
            "name": "qMaxInj",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    s_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "sMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    under_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "underPF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dernameplate_data: Optional["DernameplateData"] = field(
        default=None,
        metadata={
            "name": "DERNameplateData",
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

    :ivar season_day_type_schedules: Schedules that use this DayType.
    """
    season_day_type_schedules: List["SeasonDayTypeSchedule"] = field(
        default_factory=list,
        metadata={
            "name": "SeasonDayTypeSchedules",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceControlType(IdentifiedObject):
    """Detailed description for a control produced by an end device.

    Values in attributes allow for creation of recommended codes to be used for identifying end device controls as follows: &amp;lt;type&amp;gt;.&amp;lt;domain&amp;gt;.&amp;lt;subDomain&amp;gt;.&amp;lt;eventOrAction&amp;gt;.

    :ivar domain: High-level nature of the control.
    :ivar event_or_action: The most specific part of this control type.
        It is mainly in the form of a verb that gives action to the
        control that just occurred.
    :ivar sub_domain: More specific nature of the control, as a further
        sub-categorisation of 'domain'.
    :ivar type: Type of physical device from which the control was
        created. A value of zero (0) can be used when the source is
        unknown.
    :ivar end_device_controls: All end device controls of this type.
    """
    domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    event_or_action: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventOrAction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sub_domain: Optional[str] = field(
        default=None,
        metadata={
            "name": "subDomain",
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
    end_device_controls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceEventDetail:
    """
    Name-value pair, specific to end device events.

    :ivar name: Name.
    :ivar end_device_event: End device owning this detail.
    :ivar value: Value, including unit information.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_event: Optional["EndDeviceEvent"] = field(
        default=None,
        metadata={
            "name": "EndDeviceEvent",
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
    :ivar event_or_action: The most specific part of this event type. It
        is mainly in the form of a verb that gives action to the event
        that just occurred.
    :ivar sub_domain: More specific nature of the event, as a further
        sub-categorisation of 'domain'.
    :ivar type: Type of physical device from which the event was
        created. A value of zero (0) can be used when the source is
        unknown.
    :ivar end_device_events: All end device events of this type.
    """
    domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    event_or_action: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventOrAction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sub_domain: Optional[str] = field(
        default=None,
        metadata={
            "name": "subDomain",
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
    end_device_events: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class FaultCauseType(IdentifiedObject):
    """
    Type of cause of the fault.

    :ivar faults: All faults with this cause type.
    """
    faults: List["Fault"] = field(
        default_factory=list,
        metadata={
            "name": "Faults",
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
    :ivar derieeetype1: DER IEEE type 1 model associated with this
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
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class FrequencyTripSettings(IdentifiedObject):
    """Frequency Trip Settings.

    Reference: IEEE1547-2018.

    :ivar of1_trip_f: Must trip frequency magnitude (OF1_TRIP_F).
        Frequency values shall be reported to 3 decimal places. Typical
        value = 61,2.
    :ivar of1_trip_t: Must trip duration (OF1_TRIP_T) (&gt;=0). Typical
        value = 300.
    :ivar of2_trip_f: Must trip frequency magnitude (OF2_TRIP_F).
        Frequency values shall be reported to 3 decimal places. Typical
        value = 62.
    :ivar of2_trip_t: Must trip duration (OF2_TRIP_T) (&gt;=0). Typical
        value = 0,16.
    :ivar uf1_trip_f: Must trip frequency magnitude (UF1_TRIP_F).
        Frequency values shall be reported to 3 decimal places. Typical
        value = 58,5.
    :ivar uf1_trip_t: Must trip duration (UF1_TRIP_T) (&gt;=0). Typical
        value = 300.
    :ivar uf2_trip_f: Must trip frequency magnitude (UF2_TRIP_F).
        Frequency values shall be reported to 3 decimal places. Typical
        value = 56,5.
    :ivar uf2_trip_t: Must trip duration (UF2_TRIP_T) (&gt;=0). Typical
        value = 0,16.
    :ivar derieeetype1: DER IEEE type 1 model associated with this
        frequency trip settings model.
    """
    of1_trip_f: Optional[float] = field(
        default=None,
        metadata={
            "name": "of1TripF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    of1_trip_t: Optional[float] = field(
        default=None,
        metadata={
            "name": "of1TripT",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    of2_trip_f: Optional[float] = field(
        default=None,
        metadata={
            "name": "of2TripF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    of2_trip_t: Optional[float] = field(
        default=None,
        metadata={
            "name": "of2TripT",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf1_trip_f: Optional[float] = field(
        default=None,
        metadata={
            "name": "uf1TripF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf1_trip_t: Optional[float] = field(
        default=None,
        metadata={
            "name": "uf1TripT",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf2_trip_f: Optional[float] = field(
        default=None,
        metadata={
            "name": "uf2TripF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uf2_trip_t: Optional[float] = field(
        default=None,
        metadata={
            "name": "uf2TripT",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class GappsCimExport:
    class Meta:
        name = "GAPPS-CIM-export"
        namespace = "http://iec.ch/TC57/"

    identified_object: List[IdentifiedObject] = field(
        default_factory=list,
        metadata={
            "name": "IdentifiedObject",
            "type": "Element",
        }
    )


@dataclass
class GeographicalRegion(IdentifiedObject):
    """
    A geographical region of a power system network model.

    :ivar regions: All sub-geograhpical regions within this geographical
        region.
    """
    regions: List["SubGeographicalRegion"] = field(
        default_factory=list,
        metadata={
            "name": "Regions",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Iopoint(IdentifiedObject):
    """The class describe a measurement or control value.

    The purpose is to enable having attributes and associations common
    for measurement and control.
    """
    class Meta:
        name = "IOPoint"


@dataclass
class LoadResponseCharacteristic(IdentifiedObject):
    """Models the characteristic response of the load demand due to changes in
    system conditions such as voltage and frequency. This is not related to
    demand response. If LoadResponseCharacteristic.exponentModel is True, the
    voltage exponents are specified and used as to calculate:

    Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent
    Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent
    Where  * means "multiply" and ** is "raised to power of".

    :ivar exponent_model: Indicates the exponential voltage dependency
        model is to be used.   If false, the coefficient model is to be
        used. The exponential voltage dependency model consist of the
        attributes - pVoltageExponent - qVoltageExponent. The
        coefficient model consist of the attributes - pConstantImpedance
        - pConstantCurrent - pConstantPower - qConstantImpedance -
        qConstantCurrent - qConstantPower. The sum of
        pConstantImpedance, pConstantCurrent and pConstantPower shall
        equal 1. The sum of qConstantImpedance, qConstantCurrent and
        qConstantPower shall equal 1.
    :ivar p_constant_current: Portion of active power load modeled as
        constant current.
    :ivar p_constant_impedance: Portion of active power load modeled as
        constant impedance.
    :ivar p_constant_power: Portion of active power load modeled as
        constant power.
    :ivar p_voltage_exponent: Exponent of per unit voltage effecting
        real power.
    :ivar q_constant_current: Portion of reactive power load modeled as
        constant current.
    :ivar q_constant_impedance: Portion of reactive power load modeled
        as constant impedance.
    :ivar q_constant_power: Portion of reactive power load modeled as
        constant power.
    :ivar q_voltage_exponent: Exponent of per unit voltage effecting
        reactive power.
    :ivar energy_consumer: The set of loads that have the response
        characteristics.
    """
    exponent_model: Optional[bool] = field(
        default=None,
        metadata={
            "name": "exponentModel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_constant_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "pConstantCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_constant_impedance: Optional[float] = field(
        default=None,
        metadata={
            "name": "pConstantImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_constant_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "pConstantPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_voltage_exponent: Optional[float] = field(
        default=None,
        metadata={
            "name": "pVoltageExponent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q_constant_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "qConstantCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q_constant_impedance: Optional[float] = field(
        default=None,
        metadata={
            "name": "qConstantImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q_constant_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "qConstantPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q_voltage_exponent: Optional[float] = field(
        default=None,
        metadata={
            "name": "qVoltageExponent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energy_consumer: List["EnergyConsumer"] = field(
        default_factory=list,
        metadata={
            "name": "EnergyConsumer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class MeterReading(IdentifiedObject):
    """
    Set of values obtained from the meter.

    :ivar end_device_events: All end device events associated with this
        set of measured values.
    :ivar meter: Meter providing this reading.
    :ivar usage_point: Usage point from which this meter reading (set of
        values) has been obtained.
    """
    end_device_events: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    meter: Optional["Meter"] = field(
        default=None,
        metadata={
            "name": "Meter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    usage_point: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "name": "UsagePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class MomentaryCessationSettings(IdentifiedObject):
    """Momentary Cessation Settings.

    Reference: IEEE1547-2018.

    :ivar hvrt_t1: High-voltage momentary cessation time (MC_HVRT_T1)
        (&gt;=0). Typical value = 0.
    :ivar hvrt_t2: High-voltage momentary cessation time (MC_HVRT_T2)
        (&gt;=0). Typical value = 13.
    :ivar hvrt_v1: High-voltage momentary cessation voltage
        (MC_HVRT_V1). Per unit value based on NP_AC_V_NOM (voltage
        base). Typical value = 1,1.
    :ivar hvrt_v2: High-voltage momentary cessation voltage
        (MC_HVRT_V2). Per unit value based on NP_AC_V_NOM (voltage
        base). Typical value = 1,2.
    :ivar lvrt_t1: Low-voltage momentary cessation time (MC_LVRT_T1)
        (&gt;=0). Typical value = 0.
    :ivar lvrt_t2: Low-voltage momentary cessation time (MC_LVRT_T2)
        (&gt;=0). Typical value = 2.
    :ivar lvrt_v1: Low-voltage momentary cessation voltage (MC_LVRT_V1).
        Per unit value based on NP_AC_V_NOM (voltage base). Typical
        value = 0,5.
    :ivar lvrt_v2: Low-voltage momentary cessation voltage (MC_LVRT_V2).
        Per unit value based on NP_AC_V_NOM (voltage base). Typical
        value = 0.
    :ivar derieeetype1: DER IEEE type 1 model associated with this
        momentary cessation settings model.
    """
    hvrt_t1: Optional[float] = field(
        default=None,
        metadata={
            "name": "hvrtT1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hvrt_t2: Optional[float] = field(
        default=None,
        metadata={
            "name": "hvrtT2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hvrt_v1: Optional[float] = field(
        default=None,
        metadata={
            "name": "hvrtV1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hvrt_v2: Optional[float] = field(
        default=None,
        metadata={
            "name": "hvrtV2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lvrt_t1: Optional[float] = field(
        default=None,
        metadata={
            "name": "lvrtT1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lvrt_t2: Optional[float] = field(
        default=None,
        metadata={
            "name": "lvrtT2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lvrt_v1: Optional[float] = field(
        default=None,
        metadata={
            "name": "lvrtV1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    lvrt_v2: Optional[float] = field(
        default=None,
        metadata={
            "name": "lvrtV2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class OperationalLimitType(IdentifiedObject):
    """
    The operational meaning of a category of limits.

    :ivar acceptable_duration: The nominal acceptable duration of the
        limit.  Limits are commonly expressed in terms of the a time
        limit for which the limit is normally acceptable.   The actual
        acceptable duration of a specific limit may depend on other
        local factors such as temperature or wind speed.
    :ivar direction: The direction of the limit.
    :ivar operational_limit: The operational limits associated with this
        type of limit.
    """
    acceptable_duration: Optional[float] = field(
        default=None,
        metadata={
            "name": "acceptableDuration",
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
    operational_limit: List["OperationalLimit"] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PerLengthLineParameter(IdentifiedObject):
    """
    Common type for per-length electrical catalogues describing line
    parameters.

    :ivar wire_assembly_info: A WireAssemblyInfo is used to compute the
        PerLengthParameter data in the Wires package
    """
    wire_assembly_info: Optional["WireAssemblyInfo"] = field(
        default=None,
        metadata={
            "name": "WireAssemblyInfo",
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
    :ivar p_max: Maximum active power setting (AP_MAX_P). Typical value
        = 100.
    :ivar derieeetype1: DER IEEE type 1 model associated with this power
        limit settings model.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "pMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class RemoteInputSignal:
    """
    Supports connection to a terminal associated with a remote bus from which
    an input signal of a specific type is coming.

    :ivar remote_signal_type: Type of input signal.
    :ivar derdynamics:
    :ivar terminal:
    """
    remote_signal_type: Optional[RemoteSignalKind] = field(
        default=None,
        metadata={
            "name": "remoteSignalType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derdynamics: List[Derdynamics] = field(
        default_factory=list,
        metadata={
            "name": "DERDynamics",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
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
    :ivar assets:
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
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Season(IdentifiedObject):
    """
    A specified time period of the year.

    :ivar end_date: Date season ends.
    :ivar start_date: Date season starts.
    :ivar season_day_type_schedules: Schedules that use this Season.
    """
    end_date: Optional[object] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    start_date: Optional[object] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    season_day_type_schedules: List["SeasonDayTypeSchedule"] = field(
        default_factory=list,
        metadata={
            "name": "SeasonDayTypeSchedules",
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
    :ivar high_frequency: Frequency shall be equal to or less than
        default value. Frequency values shall be reported to 3 decimal
        places. (ES_F_HIGH). Typical value = 60,1.
    :ivar high_voltage: Per unit value based on NP_AC_V_NOM (voltage
        base). Voltage shall be equal to or less than default value.
        (ES_V_HIGH). Typical value = 1,05.
    :ivar low_frequency: Frequency shall be equal to or greater than
        default value. Frequency values shall be reported to 3 decimal
        places. (ES_F_LOW). Typical value = 59,5.
    :ivar low_voltage: Per unit value based on NP_AC_V_NOM (voltage
        base). Voltage shall be equal to or greater than default value.
        (ES_V_LOW). Typical value = 0,917.
    :ivar permit_service: This function is activated by request from the
        Area Electric Power System (EPS) Operator (ES_PERMIT_SERVICE).
        True means enabled. False means deactivated. Typical value =
        true.
    :ivar ramp_rate: Enter service soft-start duration. Time from zero
        to 100% NP_P_MAX (ES_RAMP_RATE) (&gt;=0). Typical value = 300.
    :ivar randomized_delay: Enter service radomized delay is an optional
        feature in IEEE Std 1547-2018 (ES_RANDOMIZED_DELAY) (&gt;=0).
        Typical value = 300.
    :ivar derieeetype1: DER IEEE type 1 model associated with this
        service settings model.
    """
    delay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    high_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "highFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    high_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "highVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    low_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    low_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    permit_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "permitService",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ramp_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "rampRate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    randomized_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "randomizedDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class SvEstVoltage(SvVoltage):
    angle_variance: Optional[object] = field(
        default=None,
        metadata={
            "name": "angleVariance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    v_variance: Optional[object] = field(
        default=None,
        metadata={
            "name": "vVariance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    estimate: Optional["Estimate"] = field(
        default=None,
        metadata={
            "name": "Estimate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ThermostatController(IdentifiedObject):
    """
    a price-responsive or bidding smart thermostat.

    :ivar aggregator_name: name of a market aggregator that collects bid
        curves for a higher-level market
    :ivar base_setpoint: user's desired thermostat setpoint, including
        the effects of pre-programmed schedule
    :ivar control_mode:
    :ivar price_cap: maximum price per kwh that the controller will bid,
        regardless of the market's price cap
    :ivar ramp_high: slope of high-temperature bidding curve, $/degreeC
    :ivar ramp_low: slope of low-temperature bidding curve, $/degreeC
    :ivar range_high: maximum postive offset to the thermostat setpoint
    :ivar range_low: maximum negative offset to the thermostat setpoint
    :ivar use_override:
    :ivar use_predictive:
    :ivar house:
    """
    aggregator_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "aggregatorName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    base_setpoint: Optional[float] = field(
        default=None,
        metadata={
            "name": "baseSetpoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    control_mode: Optional[ThermostatControlMode] = field(
        default=None,
        metadata={
            "name": "controlMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    price_cap: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "priceCap",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    ramp_high: Optional[float] = field(
        default=None,
        metadata={
            "name": "rampHigh",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    ramp_low: Optional[float] = field(
        default=None,
        metadata={
            "name": "rampLow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    range_high: Optional[float] = field(
        default=None,
        metadata={
            "name": "rangeHigh",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    range_low: Optional[float] = field(
        default=None,
        metadata={
            "name": "rangeLow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    use_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "useOverride",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    use_predictive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "usePredictive",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    house: Optional["House"] = field(
        default=None,
        metadata={
            "name": "House",
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

    :ivar topological_nodes: A topological node belongs to a topological
        island.
    """
    topological_nodes: List["TopologicalNode"] = field(
        default_factory=list,
        metadata={
            "name": "TopologicalNodes",
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
    :ivar transformer_end: All transformer ends having this core
        admittance.
    :ivar transformer_end_info: Transformer end datasheet used to
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
    transformer_end: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "name": "TransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    transformer_end_info: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "TransformerEndInfo",
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
    :ivar from_transformer_end: From end this mesh impedance is
        connected to. It determines the voltage reference.
    :ivar from_transformer_end_info: 'from' transformer end datasheet
        this mesh impedance is calculated from. It determines the
        voltage reference.
    :ivar to_transformer_end: All transformer ends this mesh impedance
        is connected to.
    :ivar to_transformer_end_infos: All 'to' transformer end datasheets
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
    from_transformer_end: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
            "name": "FromTransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    from_transformer_end_info: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "FromTransformerEndInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    to_transformer_end: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "name": "ToTransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    to_transformer_end_infos: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "name": "ToTransformerEndInfos",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TransformerTest(IdentifiedObject):
    """
    Test result for transformer ends, such as short-circuit, open-circuit
    (excitation) or no-load test.

    :ivar base_power: Base power at which the tests are conducted,
        usually equal to the rateds of one of the involved transformer
        ends.
    :ivar temperature: Temperature at which the test is conducted.
    """
    base_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "basePower",
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
    :ivar demand_response_programs: All demand response programs this
        usage point group is enrolled in.
    :ivar end_device_controls: All end device controls sending commands
        to this usage point group.
    :ivar usage_points: All usage points in this group.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    demand_response_programs: List["DemandResponseProgram"] = field(
        default_factory=list,
        metadata={
            "name": "DemandResponsePrograms",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_controls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltVarSettings(IdentifiedObject):
    """Volt Var Settings.

    Reference: IEEE1547-2018.

    :ivar curve_q1: VArs at V1. Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. (QV_CURVE_Q1). Typical value = 0,44.
    :ivar curve_q2: VArs at V2. Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. (QV_CURVE_Q2). Typical value = 0.
    :ivar curve_q3: VArs at V3. Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. (QV_CURVE_Q3). Typical value = 0.
    :ivar curve_q4: VArs at V4. Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. (QV_CURVE_Q4). Typical value = -0,44.
    :ivar curve_v1: Undervoltage magnitude where VArs are at maximum.
        Per unit value based on NP_AC_V_NOM (voltage base)
        (QV_CURVE_V1). Typical value = 0,92.
    :ivar curve_v2: Undervoltage magnitude where VArs are at minimum.
        Per unit value based on NP_AC_V_NOM (voltage base)
        (QV_CURVE_V2). Typical value = 0,98.
    :ivar curve_v3: Overvoltage magnitude where VArs are at minimum. Per
        unit value based on NP_AC_V_NOM (voltage base) (QV_CURVE_V3).
        Typical value = 1,02.
    :ivar curve_v4: Overvoltage magnitude where VArs are at minimum. Per
        unit value based on NP_AC_V_NOM (voltage base) (QV_CURVE_V4).
        Typical value = 1,08.
    :ivar enabled: Enables Volt-Var settings. It is specified by the
        area electric power system operator (QV_MODE_ENABLE). True means
        enabled. False meand disabled. Typical value = false.
    :ivar olrt: Volt-VAr open loop response time (QV_OLRT) (&gt;=0).
        Typical value = 5.
    :ivar v_ref: Per unit value based on NP_AC_V_NOM (voltage base)
        (QV_VREF). Typical value = 1.
    :ivar v_ref_auto_mode_enabled: Enables Volt-Var settings auto mode.
        It is specified by the area electric power system operator
        (QV_VREF_AUTO_MODE). True means enabled. False meand disabled.
        Typical value = true.
    :ivar v_ref_olrt: Vref time constant in seconds as specified by the
        area EPS operator (QV_VREF_OLRT) (&gt;=0).
    :ivar derieeetype1: DER IEEE type 1 model associated with this volt
        var settings model.
    """
    curve_q1: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_q2: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_q3: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_q4: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ4",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_v1: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveV1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_v2: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveV2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_v3: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveV3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_v4: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveV4",
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
    v_ref: Optional[float] = field(
        default=None,
        metadata={
            "name": "vRef",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    v_ref_auto_mode_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "vRefAutoModeEnabled",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    v_ref_olrt: Optional[float] = field(
        default=None,
        metadata={
            "name": "vRefOlrt",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltWattSettings(IdentifiedObject):
    """Volt Watt Settings.

    Reference: IEEE1547-2018.

    :ivar curve_p1: Active power level at V1 (PV_CURVE_P1). Per unit
        value based on NP_P_MAX_CHARGE. Typical value = 1.
    :ivar curve_p2gen: Minimum active power generating at V2
        (PV_CURVE_P2_GEN). The lesser of 0.2*Prated or Pmin. Per unit
        value based on NP_P_MAX. Typical value = Pmin.
    :ivar curve_p2load: Applicable to DER which can generate and absorb
        active power (PV_CURVE_P2_LOAD). Per unit Value based on
        NP_P_MAX_CHARGE. Negative values indicate active power load.
        Indicates maximum active power absorption. Typical value = 0.
    :ivar curve_v1: Upper start voltage for power reduction
        (PV_CURVE_V1). Per unit value based on NP_AC_V_NOM (voltage
        base). Typical value = 1,06.
    :ivar curve_v2: Upper voltager for maximum power reduction
        (PV_CURVE_V2). Per unit value based on NP_AC_V_NOM (voltage
        base). Typical value = 1,1.
    :ivar enabled: Voltage-active power mode enable (PV_MODE_ENABLE).
        True means enabled. False means disabled. Typical value = false.
    :ivar olrt: P(V) open loop response time setting (PV_OLRT) (&gt;=0).
        Typical value = 10.
    :ivar derieeetype1: DER IEEE type 1 model associated with this volt
        watt settings model.
    """
    curve_p1: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveP1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_p2gen: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveP2gen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_p2load: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveP2load",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_v1: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveV1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_v2: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveV2",
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
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltageTripSettings(IdentifiedObject):
    """Voltage Trip Settings.

    Reference: IEEE1547-2018.

    :ivar ov1_trip_t: Must trip duration (OV1_TRIP_T) (&gt;=0). Typical
        value = 13.
    :ivar ov1_trip_v: Must trip magnitude (OV1_TRIP_V). Per unit value
        based on NP_AC_V_NOM (voltage base). Typical value = 1,1.
    :ivar ov2_trip_t: Must trip duration (OV2_TRIP_T) (&gt;=0). Typical
        value = 0,16.
    :ivar ov2_trip_v: Must trip magnitude (OV2_TRIP_V). Per unit value
        based on NP_AC_V_NOM (voltage base). Typical value = 1,2.
    :ivar uv1_trip_t: Must trip duration (UV1_TRIP_T) (&gt;=0). Typical
        value = 21.
    :ivar uv1_trip_v: Must trip magnitude (UV1_TRIP_V). Per unit value
        based on NP_AC_V_NOM (voltage base). Typical value = 0,88.
    :ivar uv2_trip_t: Must trip duration (UV2_TRIP_T) (&gt;=0). Typical
        value = 2.
    :ivar uv2_trip_v: Must trip magnitude (UV2_TRIP_V). Per unit value
        based on NP_AC_V_NOM (voltage base). Typical value = 0,5.
    :ivar derieeetype1: DER IEEE type 1 model associated with this
        voltage trip settings model.
    """
    ov1_trip_t: Optional[float] = field(
        default=None,
        metadata={
            "name": "ov1TripT",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov1_trip_v: Optional[float] = field(
        default=None,
        metadata={
            "name": "ov1TripV",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov2_trip_t: Optional[float] = field(
        default=None,
        metadata={
            "name": "ov2TripT",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ov2_trip_v: Optional[float] = field(
        default=None,
        metadata={
            "name": "ov2TripV",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv1_trip_t: Optional[float] = field(
        default=None,
        metadata={
            "name": "uv1TripT",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv1_trip_v: Optional[float] = field(
        default=None,
        metadata={
            "name": "uv1TripV",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv2_trip_t: Optional[float] = field(
        default=None,
        metadata={
            "name": "uv2TripT",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    uv2_trip_v: Optional[float] = field(
        default=None,
        metadata={
            "name": "uv2TripV",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WattVarSettings(IdentifiedObject):
    """Watt Var Settings.

    Reference: IEEE1547-2018.

    :ivar curve_p1gen: Lower active power (generating)
        (QP_CURVE_P1_GEN). Per unit value based on NP_P_MAX. Typical
        value = 0,2.
    :ivar curve_p1load: Lower active power (absorbing)
        (QP_CURVE_P1_LOAD). Per unit value based on NP_P_MAX_CHARGE.
        Typical value = -0,2.
    :ivar curve_p2gen: Medium active power (generating)
        (QP_CURVE_P2_GEN). Per unit value based on NP_P_MAX. Typical
        value = 0,5.
    :ivar curve_p2load: Medium active power (absorbing)
        (QP_CURVE_P2_LOAD). Per unit value based on NP_P_MAX_CHARGE.
        Typical value = -0,5.
    :ivar curve_p3gen: Maximum active power (generating)
        (QP_CURVE_P3_GEN). Per unit value based on NP_P_MAX. Typical
        value = 1.
    :ivar curve_p3load: Maximum active power (absorbing)
        (QP_CURVE_P3_LOAD). Per unit value based on NP_P_MAX_CHARGE.
        Typical value = -1.
    :ivar curve_q1gen: Lower reactive power while generating
        (QP_CURVE_Q1_GEN). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = 0.
    :ivar curve_q1load: Maximum reactive power while absorbing
        (QP_CURVE_Q1_LOAD). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = 0.
    :ivar curve_q2gen: Medium reactive power while generating
        (QP_CURVE_Q2_GEN). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = 0.
    :ivar curve_q2load: Medium reactive power while absorbing
        (QP_CURVE_Q2_LOAD). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr.. Typical value = 0.
    :ivar curve_q3gen: Maximum reactive power while generating
        (QP_CURVE_Q3_GEN). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = -0,44.
    :ivar curve_q3load: Lower reactive power while absorbing
        (QP_CURVE_Q3_LOAD). Per unit value based on NP_Q_MAX_INJ or
        NP_Q_MAX_ABS. Negative signs should not be used but if present,
        indicates absorbing VAr. Typical value = 0,44.
    :ivar enabled: This function is deactivated by request from the area
        electric power system operator (QP_MODE_ENABLE). True means
        enabled. False means disabled. Typical value = false.
    :ivar derieeetype1: DER IEEE type 1 model associated with this watt
        var settings model.
    """
    curve_p1gen: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveP1gen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_p1load: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveP1load",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_p2gen: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveP2gen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_p2load: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveP2load",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_p3gen: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveP3gen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_p3load: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveP3load",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_q1gen: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ1gen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_q1load: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ1load",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_q2gen: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ2gen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_q2load: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ2load",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_q3gen: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ3gen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    curve_q3load: Optional[float] = field(
        default=None,
        metadata={
            "name": "curveQ3load",
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
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WirePosition(IdentifiedObject):
    """
    Identification, spacing and configuration of the wires of a conductor with
    respect to a structure.

    :ivar sequence_number: Numbering for wires on a WireSpacingInfo.
        Neutrals should be numbered last. Multiple circuits on the same
        pole, tower or right-of-way can be included with unique sequence
        numbers for the phases, and identical sequence numbers for any
        shared neutrals.
    :ivar x_coord: Signed horizontal distance from the wire at this
        position to a common reference point.
    :ivar y_coord: Signed vertical distance from the wire at this
        position: above ground (positive value) or burial depth below
        ground (negative value).
    :ivar wire_phase_info:
    :ivar wire_spacing_info: Wire spacing data this wire position
        belongs to.
    """
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    x_coord: Optional[float] = field(
        default=None,
        metadata={
            "name": "xCoord",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y_coord: Optional[float] = field(
        default=None,
        metadata={
            "name": "yCoord",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_phase_info: List["WirePhaseInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WirePhaseInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_spacing_info: Optional["WireSpacingInfo"] = field(
        default=None,
        metadata={
            "name": "WireSpacingInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Control(Iopoint):
    """Control is used for supervisory/device control.

    It represents control outputs that are used to change the state in a
    process, e.g. close or open breaker, a set point value or a raise
    lower command.

    :ivar control_type: Specifies the type of Control, e.g.
        BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The
        ControlType.name shall be unique among all specified types and
        describe the type.
    :ivar time_stamp: The last time a control output was sent.
    :ivar unit_multiplier: The unit multiplier of the controlled
        quantity.
    :ivar unit_symbol: The unit of measure of the controlled quantity.
    :ivar power_system_resource: Regulating device governed by this
        control output.
    """
    control_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "controlType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    unit_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "unitMultiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    unit_symbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "unitSymbol",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_system_resource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
            "name": "PowerSystemResource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DermonitorableParameter:
    class Meta:
        name = "DERMonitorableParameter"

    derparameter: Optional[DerparameterKind] = field(
        default=None,
        metadata={
            "name": "DERParameter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    flow_direction: Optional[FlowDirectionKind] = field(
        default=None,
        metadata={
            "name": "flowDirection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    y_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "yMultiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y_unit: Optional[DerunitSymbol] = field(
        default=None,
        metadata={
            "name": "yUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y_unit_installed_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "yUnitInstalledMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    y_unit_installed_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "yUnitInstalledMin",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dercurve_data: Optional[DercurveData] = field(
        default=None,
        metadata={
            "name": "DERCurveData",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dispatch_schedule: List[DispatchSchedule] = field(
        default_factory=list,
        metadata={
            "name": "DispatchSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_group: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class DernameplateData(IdentifiedObject):
    """DER nameplate data.

    Reference: IEEE1547-2018.

    :ivar abnormal_opcat_kind: Abnormal performance Category
        (NP_ABNORMAL_OP_CAT).
    :ivar ac_vmax: AC voltage rating in RMS Volts (NP_AC_V_MAX).
    :ivar ac_vmin: AC voltage rating in RMS Volts (NP_AC_V_MIN).
    :ivar fw_ver: FW Version (NP_FW_VER).
    :ivar manufacturer: Manufacturer (NP_MANUFACTURER).
    :ivar model: Model (NP_MODEL).
    :ivar normal_opcat_kind: Normal performance capability
        (NP_NORMAL_OP_CAT).
    :ivar reactive_susceptance: Reactive susceptance that remains
        connected to the Area EPS in the cease to energize and trip
        state (NP_REACTIVE_SUSCEPTANCE).
    :ivar serial_num: Serial number (NP_SERIAL_NUM).
    :ivar supports_const_pfmode:
    :ivar supports_const_qmode:
    :ivar supports_pfmode:
    :ivar supports_pvmode:
    :ivar supports_qpmode:
    :ivar supports_qvmode:
    :ivar derieeetype1: DER IEEE type 1 model associated with this DER
        nameplate data model.
    :ivar dernameplate_data_applied: The applied DER nameplate data.
    """
    class Meta:
        name = "DERNameplateData"

    abnormal_opcat_kind: Optional[AbnormalOpcatKind] = field(
        default=None,
        metadata={
            "name": "abnormalOPcatKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ac_vmax: Optional[float] = field(
        default=None,
        metadata={
            "name": "acVmax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ac_vmin: Optional[float] = field(
        default=None,
        metadata={
            "name": "acVmin",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    fw_ver: Optional[str] = field(
        default=None,
        metadata={
            "name": "fwVer",
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
    normal_opcat_kind: Optional[NormalOpcatKind] = field(
        default=None,
        metadata={
            "name": "normalOPcatKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reactive_susceptance: Optional[float] = field(
        default=None,
        metadata={
            "name": "reactiveSusceptance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    serial_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "serialNum",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_const_pfmode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsConstPFmode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supports_const_qmode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsConstQmode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supports_pfmode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsPFmode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supports_pvmode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsPVmode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supports_qpmode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsQPmode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    supports_qvmode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsQVmode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    derieeetype1: Optional["Derieeetype1"] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dernameplate_data_applied: List[DernameplateDataApplied] = field(
        default_factory=list,
        metadata={
            "name": "DERNameplateDataApplied",
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
    :ivar end_device_groups: All groups of end devices enrolled in this
        demand response program.
    :ivar usage_point_groups: All usage point groups enrolled in this
        demand response program.
    :ivar validity_interval: Interval within which the program is valid.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_groups: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    usage_point_groups: List[UsagePointGroup] = field(
        default_factory=list,
        metadata={
            "name": "UsagePointGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    validity_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "validityInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Estimate:
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sv_est_voltages: List[SvEstVoltage] = field(
        default_factory=list,
        metadata={
            "name": "SvEstVoltages",
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
    :ivar occurred_date_time: The date and time at which the fault
        occurred.
    :ivar phases: The phases participating in the fault. The fault
        connections into these phases are further specified by the type
        of fault.
    :ivar stop_date_time: Time when the fault is repaired. If not
        specified, the fault is temporary and will clear itself as soon
        as it's deenergized.
    :ivar fault_cause_types: All types of fault cause.
    :ivar faulty_equipment: Equipment carrying this fault.
    :ivar impedance: Fault impedance. Its usage is described by 'kind'.
    :ivar location:
    """
    kind: Optional[PhaseConnectedFaultKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    occurred_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "occurredDateTime",
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
    stop_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "stopDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    fault_cause_types: List[FaultCauseType] = field(
        default_factory=list,
        metadata={
            "name": "FaultCauseTypes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    faulty_equipment: Optional["Equipment"] = field(
        default=None,
        metadata={
            "name": "FaultyEquipment",
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
    location: Optional["Location"] = field(
        default=None,
        metadata={
            "name": "Location",
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
    cooling_setpoint: Optional[float] = field(
        default=None,
        metadata={
            "name": "coolingSetpoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    cooling_system: Optional[HouseCooling] = field(
        default=None,
        metadata={
            "name": "coolingSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    floor_area: Optional[float] = field(
        default=None,
        metadata={
            "name": "floorArea",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    heating_setpoint: Optional[float] = field(
        default=None,
        metadata={
            "name": "heatingSetpoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    heating_system: Optional[HouseHeating] = field(
        default=None,
        metadata={
            "name": "heatingSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    hvac_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "hvacPowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    number_of_stories: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfStories",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    service_panel: Optional["EnergyConsumer"] = field(
        default=None,
        metadata={
            "name": "ServicePanel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    thermostat_controller: Optional[ThermostatController] = field(
        default=None,
        metadata={
            "name": "ThermostatController",
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

    :ivar energised_end_voltage: Voltage applied to the winding (end)
        during test.
    :ivar exciting_current: Exciting current measured from a positive-
        sequence or single-phase excitation test.
    :ivar exciting_current_zero: Exciting current measured from a zero-
        sequence open-circuit excitation test.
    :ivar loss: Losses measured from a positive-sequence or single-phase
        excitation test.
    :ivar loss_zero: Losses measured from a zero-sequence excitation
        test.
    :ivar energised_end: Transformer end that current is applied to in
        this no-load test.
    """
    energised_end_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "energisedEndVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    exciting_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "excitingCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    exciting_current_zero: Optional[float] = field(
        default=None,
        metadata={
            "name": "excitingCurrentZero",
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
    loss_zero: Optional[float] = field(
        default=None,
        metadata={
            "name": "lossZero",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energised_end: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "EnergisedEnd",
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

    :ivar energised_end_step: Tap step number for the energised end of
        the test pair.
    :ivar energised_end_voltage: Voltage applied to the winding (end)
        during test.
    :ivar open_end_step: Tap step number for the open end of the test
        pair.
    :ivar open_end_voltage: Voltage measured at the open-circuited end,
        with the energised end set to rated voltage and all other ends
        open.
    :ivar phase_shift: Phase shift measured at the open end with the
        energised end set to rated voltage and all other ends open.
    :ivar energised_end: Transformer end that current is applied to in
        this open-circuit test.
    :ivar open_end: Transformer end measured for induced voltage and
        angle in this open-circuit test.
    """
    energised_end_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "energisedEndStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energised_end_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "energisedEndVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    open_end_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "openEndStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    open_end_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "openEndVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase_shift: Optional[float] = field(
        default=None,
        metadata={
            "name": "phaseShift",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energised_end: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "EnergisedEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    open_end: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "OpenEnd",
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

    :ivar operational_limit_set:
    :ivar operational_limit_type: The limit type associated with this
        limit.
    """
    operational_limit_set: Optional["OperationalLimitSet"] = field(
        default=None,
        metadata={
            "name": "OperationalLimitSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    operational_limit_type: Optional[OperationalLimitType] = field(
        default=None,
        metadata={
            "name": "OperationalLimitType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class OverfrequencyTripCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class OvervoltageTripCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PerLengthImpedance(PerLengthLineParameter):
    """
    Common type for per-length impedance electrical catalogues.

    :ivar acline_segments: All line segments described by this per-
        length impedance.
    """
    acline_segments: List["AclineSegment"] = field(
        default_factory=list,
        metadata={
            "name": "ACLineSegments",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class RegularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them is constant.

    :ivar end_time: The time for the last time point.  The value can be
        a time of day, not a specific date.
    :ivar time_step: The time between each pair of subsequent regular
        time points in sequence order.
    :ivar time_points: The regular interval time point data values that
        define this schedule.
    """
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_step: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_points: List[RegularTimePoint] = field(
        default_factory=list,
        metadata={
            "name": "TimePoints",
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

    :ivar energised_end_step: Tap step number for the energised end of
        the test pair.
    :ivar grounded_end_step: Tap step number for the grounded end of the
        test pair.
    :ivar leakage_impedance: Leakage impedance measured from a positive-
        sequence or single-phase short-circuit test.
    :ivar leakage_impedance_zero: Leakage impedance measured from a
        zero-sequence short-circuit test.
    :ivar loss: Load losses from a positive-sequence or single-phase
        short-circuit test.
    :ivar loss_zero: Load losses from a zero-sequence short-circuit
        test.
    :ivar energised_end: Transformer end that voltage is applied to in
        this short-circuit test. The test voltage is chosen to induce
        rated current in the energised end.
    :ivar grounded_ends: All ends short-circuited in this short-circuit
        test.
    """
    energised_end_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "energisedEndStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    grounded_end_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "groundedEndStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    leakage_impedance: Optional[float] = field(
        default=None,
        metadata={
            "name": "leakageImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    leakage_impedance_zero: Optional[float] = field(
        default=None,
        metadata={
            "name": "leakageImpedanceZero",
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
    loss_zero: Optional[float] = field(
        default=None,
        metadata={
            "name": "lossZero",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energised_end: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "EnergisedEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    grounded_ends: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "name": "GroundedEnds",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )


@dataclass
class SubGeographicalRegion(IdentifiedObject):
    """
    A subset of a geographical region of a power system network model.

    :ivar region: The geographical region to which this sub-geographical
        region is within.
    :ivar substations: The substations in this sub-geographical region.
    """
    region: Optional[GeographicalRegion] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    substations: List["Substation"] = field(
        default_factory=list,
        metadata={
            "name": "Substations",
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

    :ivar end_number: Number for this transformer end, corresponding to
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
    :ivar base_voltage: Base voltage of the transformer end.  This is
        essential for PU calculation.
    :ivar core_admittance: Core admittance of this transformer end,
        representing magnetising current and core losses. The full
        values of the transformer should be supplied for one transformer
        end only.
    :ivar from_mesh_impedance: All mesh impedances between this 'to' and
        other 'from' transformer ends.
    :ivar phase_tap_changer: Phase tap changer associated with this
        transformer end.
    :ivar ratio_tap_changer: Ratio tap changer associated with this
        transformer end.
    :ivar terminal: Terminal of the power transformer to which this
        transformer end belongs.
    :ivar to_mesh_impedance: All mesh impedances between this 'from' and
        other 'to' transformer ends.
    """
    end_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "endNumber",
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
    base_voltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "name": "BaseVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    core_admittance: Optional[TransformerCoreAdmittance] = field(
        default=None,
        metadata={
            "name": "CoreAdmittance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    from_mesh_impedance: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "name": "FromMeshImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase_tap_changer: Optional["PhaseTapChanger"] = field(
        default=None,
        metadata={
            "name": "PhaseTapChanger",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ratio_tap_changer: Optional["RatioTapChanger"] = field(
        default=None,
        metadata={
            "name": "RatioTapChanger",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    to_mesh_impedance: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "name": "ToMeshImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class UnderfrequencyTripCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class UndervoltageTripCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltVarCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class VoltWattCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WattVarCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class BaseVoltage(IdentifiedObject):
    """
    Defines a system base voltage which is referenced.

    :ivar nominal_voltage: The power system resource's base voltage.
    :ivar conducting_equipment: All conducting equipment with this base
        voltage.  Use only when there is no voltage level container used
        and only one base voltage applies.  For example, not used for
        transformers.
    :ivar topological_node: The topological nodes at the base voltage.
    :ivar transformer_ends: Transformer ends at the base voltage.  This
        is essential for PU calculation.
    """
    nominal_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    conducting_equipment: List["ConductingEquipment"] = field(
        default_factory=list,
        metadata={
            "name": "ConductingEquipment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    topological_node: List["TopologicalNode"] = field(
        default_factory=list,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    transformer_ends: List[TransformerEnd] = field(
        default_factory=list,
        metadata={
            "name": "TransformerEnds",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Derieeetype1(Derdynamics):
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

    :ivar phase_to_ground_applicable: Indicates whether the DER uses
        phase-to-ground applicable voltages.
    :ivar phase_to_neutral_applicable: Indicates whether the DER uses
        phase-to-neutral applicable voltages.
    :ivar phase_to_phase_applicable: Indicates whether the DER uses
        phase-to-phase applicable voltages.
    :ivar constant_power_factor_settings: Constant power factor settings
        with which this DER IEEE type 1 model is associated.
    :ivar constant_reactive_power_settings: Constant reactive power
        settings with which this DER IEEE type 1 model is associated.
    :ivar der_nameplate_data: DER nameplate data with which this DER
        IEEE type 1 model is associated.
    :ivar frequency_droop_settings: Frequency droop dettings with which
        this DER IEEE type 1 model is associated.
    :ivar frequency_trip_settings: Frequency trip settings with which
        this DER IEEE type 1 model is associated.
    :ivar momentary_cessation_settings: Momentary cessation settings
        with which this DER IEEE type 1 model is associated.
    :ivar power_limit_settings: Power limit settings with which this DER
        IEEE type 1 model is associated.
    :ivar service_settings: Service settings with which this DER IEEE
        type 1 model is associated.
    :ivar voltage_trip_settings: Voltage trip settings with which this
        DER IEEE type 1 model is associated.
    :ivar volt_var_settings: Volt var settings with which this DER IEEE
        type 1 model is associated.
    :ivar volt_watt_settings: Volt watt settings with which this DER
        IEEE type 1 model is associated.
    :ivar watt_var_settings: Watt var settings with which this DER IEEE
        type 1 model is associated.
    """
    class Meta:
        name = "DERIEEEType1"

    phase_to_ground_applicable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "phaseToGroundApplicable",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    phase_to_neutral_applicable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "phaseToNeutralApplicable",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    phase_to_phase_applicable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "phaseToPhaseApplicable",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    constant_power_factor_settings: Optional["ConstantPowerFactorSettings"] = field(
        default=None,
        metadata={
            "name": "ConstantPowerFactorSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    constant_reactive_power_settings: Optional[ConstantReactivePowerSettings] = field(
        default=None,
        metadata={
            "name": "ConstantReactivePowerSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    der_nameplate_data: Optional[DernameplateData] = field(
        default=None,
        metadata={
            "name": "DerNameplateData",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    frequency_droop_settings: Optional[FrequencyDroopSettings] = field(
        default=None,
        metadata={
            "name": "FrequencyDroopSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    frequency_trip_settings: Optional[FrequencyTripSettings] = field(
        default=None,
        metadata={
            "name": "FrequencyTripSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    momentary_cessation_settings: Optional[MomentaryCessationSettings] = field(
        default=None,
        metadata={
            "name": "MomentaryCessationSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_limit_settings: Optional[PowerLimitSettings] = field(
        default=None,
        metadata={
            "name": "PowerLimitSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    service_settings: Optional[ServiceSettings] = field(
        default=None,
        metadata={
            "name": "ServiceSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltage_trip_settings: Optional[VoltageTripSettings] = field(
        default=None,
        metadata={
            "name": "VoltageTripSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_settings: Optional[VoltVarSettings] = field(
        default=None,
        metadata={
            "name": "VoltVarSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_watt_settings: Optional[VoltWattSettings] = field(
        default=None,
        metadata={
            "name": "VoltWattSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_settings: Optional[WattVarSettings] = field(
        default=None,
        metadata={
            "name": "WattVarSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EquipmentFault(Fault):
    """A fault applied at the terminal, external to the equipment.

    This class is not used to specify faults internal to the equipment.

    :ivar terminal: The terminal connecting to the bus to which the
        fault is applied.
    """
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Ieee1547Setting:
    class Meta:
        name = "IEEE1547Setting"

    constant_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "constantPowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    constant_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "constantReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_intentional_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceIntentionalDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_max_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMaxFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_max_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMaxVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_min_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMinFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    enter_service_min_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMinVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    frequency_droop_response_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "frequencyDroopResponseTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    island_clearing_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "islandClearingTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    open_loop_response_time_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "openLoopResponseTimeP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    over_frequency_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "overFrequencyDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    over_frequency_droop: Optional[float] = field(
        default=None,
        metadata={
            "name": "overFrequencyDroop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_constant_open_loop: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeConstantOpenLoop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_constant_reference_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeConstantReferenceVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    under_frequency_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "underFrequencyDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    under_frequency_droop: Optional[float] = field(
        default=None,
        metadata={
            "name": "underFrequencyDroop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    overfrequency_trip_curve: Optional[OverfrequencyTripCurve] = field(
        default=None,
        metadata={
            "name": "OverfrequencyTripCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    overvoltage_trip_curve: Optional[OvervoltageTripCurve] = field(
        default=None,
        metadata={
            "name": "OvervoltageTripCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_electronics_connections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rotating_machines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "name": "RotatingMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    underfrequency_trip_curve: Optional[UnderfrequencyTripCurve] = field(
        default=None,
        metadata={
            "name": "UnderfrequencyTripCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    undervoltage_trip_curve: Optional[UndervoltageTripCurve] = field(
        default=None,
        metadata={
            "name": "UndervoltageTripCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_var_curve: Optional[VoltVarCurve] = field(
        default=None,
        metadata={
            "name": "VoltVarCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    volt_watt_curve: Optional[VoltWattCurve] = field(
        default=None,
        metadata={
            "name": "VoltWattCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    watt_var_curve: Optional[WattVarCurve] = field(
        default=None,
        metadata={
            "name": "WattVarCurve",
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

    :ivar assets: All assets at this location.
    :ivar coordinate_system: Coordinate system used to describe position
        points of this location.
    :ivar fault:
    :ivar measurements:
    :ivar power_system_resources: All power system resources at this
        location.
    """
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "CoordinateSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    fault: List[Fault] = field(
        default_factory=list,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    measurements: List["Measurement"] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_system_resources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "name": "PowerSystemResources",
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

    :ivar connection_kind: Kind of connection.
    :ivar phase_angle_clock: Terminal voltage phase angle displacement
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
    :ivar rated_s: Normal apparent power rating. The attribute shall be
        a positive value. For a two-winding transformer the values for
        the high and low voltage sides shall be identical.
    :ivar rated_u: Rated voltage: phase-phase for three-phase windings,
        and either phase-phase or phase-neutral for single-phase
        windings. A high voltage side, as given by
        TransformerEnd.endNumber, shall have a ratedU that is greater or
        equal than ratedU for the lower voltage sides.
    :ivar power_transformer: The power transformer of this power
        transformer end.
    """
    connection_kind: Optional[WindingConnection] = field(
        default=None,
        metadata={
            "name": "connectionKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase_angle_clock: Optional[int] = field(
        default=None,
        metadata={
            "name": "phaseAngleClock",
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
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_transformer: Optional["PowerTransformer"] = field(
        default=None,
        metadata={
            "name": "PowerTransformer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """
    A time schedule covering a 24 hour period, with curve data for a specific
    type of season and day.

    :ivar day_type: DayType for the Schedule.
    :ivar season: Season for the Schedule.
    """
    day_type: Optional[DayType] = field(
        default=None,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    season: Optional[Season] = field(
        default=None,
        metadata={
            "name": "Season",
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

    :ivar ordered_phases: Identifies the phases present and the order of
        their connection on this winding (end) of the transformer. In
        some use cases, such as open-wye, open-delta transformers and
        single-phase, center-tap secondary transformers, the order of
        phase connection is important, so the OrderedPhaseCodeKind
        enumeration is used instead of PhaseCode.
    :ivar transformer_tank: Transformer this winding belongs to.
    """
    ordered_phases: Optional[OrderedPhaseCodeKind] = field(
        default=None,
        metadata={
            "name": "orderedPhases",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    transformer_tank: Optional["TransformerTank"] = field(
        default=None,
        metadata={
            "name": "TransformerTank",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConstantPowerFactorSettings(IdentifiedObject):
    """Constant Power Factor Settings.

    Reference: IEEE1547-2018.

    :ivar constant_power_factor_excitation_kind: Under or over excited
        (CONST_PF_EXCITATION). Typical value
        =ConstantPowerFactorSettingKind.inj.
    :ivar enabled: Constant power factor mode select
        (CONST_PF_MODE_ENABLE). True means enabled. False means
        disabled. Typical value = true.
    :ivar power_factor: Power factor setting (CONST_PF). Typical value =
        1.
    :ivar derieeetype1: DER IEEE type 1 model associated with this
        constant power factor settings model.
    """
    constant_power_factor_excitation_kind: Optional[ConstantPowerFactorSettingKind] = field(
        default=None,
        metadata={
            "name": "constantPowerFactorExcitationKind",
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
    power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "powerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derieeetype1: Optional[Derieeetype1] = field(
        default=None,
        metadata={
            "name": "DERIEEEType1",
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

    :ivar asset_datasheet: Datasheet information for this power system
        resource.
    :ivar assets: All assets represented by this power system resource.
        For example, multiple conductor assets are electrically modelled
        as a single AC line segment.
    :ivar controls: The controller outputs used to actually govern a
        regulating device, e.g. the magnetization of a synchronous
        machine or capacitor bank breaker actuator.
    :ivar location: Location of this power system resource.
    :ivar measurements: The measurements associated with this power
        system resource.
    """
    asset_datasheet: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "name": "AssetDatasheet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    controls: List[Control] = field(
        default_factory=list,
        metadata={
            "name": "Controls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    measurements: List["Measurement"] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class RegulationSchedule(SeasonDayTypeSchedule):
    """
    A pre-established pattern over time for a controlled variable, e.g., busbar
    voltage.

    :ivar regulating_control: Regulating controls that have this
        Schedule.
    :ivar voltage_control_zones: A VoltageControlZone may have a
        voltage regulation schedule.
    """
    regulating_control: Optional["RegulatingControl"] = field(
        default=None,
        metadata={
            "name": "RegulatingControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    voltage_control_zones: List["VoltageControlZone"] = field(
        default_factory=list,
        metadata={
            "name": "VoltageControlZones",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TapSchedule(SeasonDayTypeSchedule):
    """
    A pre-established pattern over time for a tap step.

    :ivar tap_changer: A TapSchedule is associated with a TapChanger.
    """
    tap_changer: Optional["TapChanger"] = field(
        default=None,
        metadata={
            "name": "TapChanger",
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

    :ivar p_injection: The active power injected into the bus at this
        location in addition to injections from equipment.  Positive
        sign means injection into the TopologicalNode (bus). Starting
        value for a steady state solution.
    :ivar q_injection: The reactive power injected into the bus at this
        location in addition to injections from equipment. Positive sign
        means injection into the TopologicalNode (bus). Starting value
        for a steady state solution.
    :ivar base_voltage: The base voltage of the topologocial node.
    :ivar connectivity_node_container: The connectivity node container
        to which the toplogical node belongs.
    :ivar connectivity_nodes: The connectivity nodes combine together to
        form this topological node.  May depend on the current state of
        switches in the network.
    :ivar sv_voltage: The state voltage associated with the topological
        node.
    :ivar terminal: The terminals associated with the topological node.
        This can be used as an alternative to the connectivity node path
        to terminal, thus making it unneccesary to model connectivity
        nodes in some cases.   Note that if connectivity nodes are in
        the model, this association would probably not be used as an
        input specification.
    :ivar topological_island: A topological node belongs to a
        topological island.
    """
    p_injection: Optional[float] = field(
        default=None,
        metadata={
            "name": "pInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q_injection: Optional[float] = field(
        default=None,
        metadata={
            "name": "qInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    base_voltage: Optional[BaseVoltage] = field(
        default=None,
        metadata={
            "name": "BaseVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    connectivity_node_container: Optional["ConnectivityNodeContainer"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNodeContainer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    connectivity_nodes: List["ConnectivityNode"] = field(
        default_factory=list,
        metadata={
            "name": "ConnectivityNodes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sv_voltage: List[SvVoltage] = field(
        default_factory=list,
        metadata={
            "name": "SvVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    terminal: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    topological_island: Optional[TopologicalIsland] = field(
        default=None,
        metadata={
            "name": "TopologicalIsland",
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

    :ivar assets: All assets described by this data.
    :ivar power_system_resources: All power system resources with this
        datasheet information.
    """
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_system_resources: List[PowerSystemResource] = field(
        default_factory=list,
        metadata={
            "name": "PowerSystemResources",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConnectivityNodeContainer(PowerSystemResource):
    """
    A base class for all objects that may contain connectivity nodes or
    topological nodes.

    :ivar connectivity_nodes: Connectivity nodes which belong to this
        connectivity node container.
    :ivar topological_node: The topological nodes which belong to this
        connectivity node container.
    """
    connectivity_nodes: List["ConnectivityNode"] = field(
        default_factory=list,
        metadata={
            "name": "ConnectivityNodes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    topological_node: List[TopologicalNode] = field(
        default_factory=list,
        metadata={
            "name": "TopologicalNode",
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
    :ivar energy_consumer: The energy consumer to which this phase
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
    energy_consumer: Optional["EnergyConsumer"] = field(
        default=None,
        metadata={
            "name": "EnergyConsumer",
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
    :ivar energy_source: The energy sourceto which the phase belongs.
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energy_source: Optional["EnergySource"] = field(
        default=None,
        metadata={
            "name": "EnergySource",
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

    :ivar cut_level1: First level (amount) of load to cut as a
        percentage of total zone load.
    :ivar cut_level2: Second level (amount) of load to cut as a
        percentage of total zone load.
    :ivar energy_consumers: Energy consumer is assigned to the power cut
        zone.
    """
    cut_level1: Optional[float] = field(
        default=None,
        metadata={
            "name": "cutLevel1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    cut_level2: Optional[float] = field(
        default=None,
        metadata={
            "name": "cutLevel2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energy_consumers: List["EnergyConsumer"] = field(
        default_factory=list,
        metadata={
            "name": "EnergyConsumers",
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
    :ivar power_electronics_connection:
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
    power_electronics_connection: Optional["PowerElectronicsConnection"] = field(
        default=None,
        metadata={
            "name": "PowerElectronicsConnection",
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
    :ivar monitored_phase: Phase voltage controlling this regulator,
        measured at regulator location.
    :ivar target_deadband: This is a deadband used with discrete control
        to avoid excessive update of controls like tap changers and
        shunt compensator banks while regulating. The units of those
        appropriate for the mode.
    :ivar target_value: The target value specified for case input.
        This value can be used for the target value without the use of
        schedules. The value has the units appropriate to the mode
        attribute.
    :ivar regulation_schedule: Schedule for this Regulating regulating
        control.
    :ivar terminal: The terminal associated with this regulating
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
    monitored_phase: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "name": "monitoredPhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    target_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "targetDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    target_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "targetValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    regulation_schedule: List[RegulationSchedule] = field(
        default_factory=list,
        metadata={
            "name": "RegulationSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ShuntCompensatorPhase(PowerSystemResource):
    """
    Single phase of a multi-phase shunt compensator when its attributes might
    be different per phase.

    :ivar maximum_sections: The maximum number of sections that may be
        switched in for this phase.
    :ivar normal_sections: For the capacitor phase, the normal number of
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
    :ivar shunt_compensator: Shunt compensator of this shunt compensator
        phase.
    """
    maximum_sections: Optional[int] = field(
        default=None,
        metadata={
            "name": "maximumSections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normal_sections: Optional[int] = field(
        default=None,
        metadata={
            "name": "normalSections",
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
    shunt_compensator: Optional["ShuntCompensator"] = field(
        default=None,
        metadata={
            "name": "ShuntCompensator",
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
    :ivar p_injection: The active power mismatch between calculated
        injection and initial injection.  Positive sign means injection
        into the TopologicalNode (bus).
    :ivar q_injection: The reactive power mismatch between calculated
        injection and initial injection.  Positive sign means injection
        into the TopologicalNode (bus).
    :ivar connectivity_node:
    :ivar topological_node: The topological node associated with the
        flow injection state variable.
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    p_injection: Optional[float] = field(
        default=None,
        metadata={
            "name": "pInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    q_injection: Optional[float] = field(
        default=None,
        metadata={
            "name": "qInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    connectivity_node: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    topological_node: Optional[TopologicalNode] = field(
        default=None,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class TapChanger(PowerSystemResource):
    """
    Mechanism for changing transformer winding tap positions.

    :ivar control_enabled: Specifies the regulation status of the
        equipment.  True is regulating, false is not regulating.
    :ivar ct_rating:
    :ivar ct_ratio:
    :ivar high_step: Highest possible tap step position, advance from
        neutral. The attribute shall be greater than lowStep.
    :ivar initial_delay: For an LTC, the delay for initial tap changer
        operation (first step change)
    :ivar low_step: Lowest possible tap step position, retard from
        neutral
    :ivar ltc_flag: Specifies whether or not a TapChanger has load tap
        changing capabilities.
    :ivar neutral_step: The neutral tap step position for this winding.
        The attribute shall be equal or greater than lowStep and equal
        or less than highStep.
    :ivar neutral_u: Voltage at which the winding operates at the
        neutral tap setting.
    :ivar normal_step: The tap step position used in "normal" network
        operation for this winding. For a "Fixed" tap changer indicates
        the current physical tap setting. The attribute shall be equal
        or greater than lowStep and equal or less than highStep.
    :ivar pt_ratio:
    :ivar step: Tap changer position. Starting step for a steady state
        solution. Non integer values are allowed to support continuous
        tap variables. The reasons for continuous value are to support
        study cases where no discrete tap changers has yet been
        designed, a solutions where a narrow voltage band force the tap
        step to oscillate or accommodate for a continuous solution as
        input. The attribute shall be equal or greater than lowStep and
        equal or less than highStep.
    :ivar subsequent_delay: For an LTC, the delay for subsequent tap
        changer operation (second and later step changes)
    :ivar sv_tap_step: The tap step state associated with the tap
        changer.
    :ivar tap_changer_control: The regulating control scheme in which
        this tap changer participates.
    :ivar tap_schedules: A TapChanger can have TapSchedules.
    """
    control_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "controlEnabled",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ct_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "ctRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ct_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "ctRatio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    high_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "highStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    initial_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "initialDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    low_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "lowStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ltc_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ltcFlag",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutral_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "neutralStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutral_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "neutralU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normal_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "normalStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pt_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "ptRatio",
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
    subsequent_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "subsequentDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sv_tap_step: Optional[SvTapStep] = field(
        default=None,
        metadata={
            "name": "SvTapStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    tap_changer_control: Optional["TapChangerControl"] = field(
        default=None,
        metadata={
            "name": "TapChangerControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    tap_schedules: List[TapSchedule] = field(
        default_factory=list,
        metadata={
            "name": "TapSchedules",
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

    :ivar busbar_section: A VoltageControlZone is controlled by a
        designated BusbarSection.
    :ivar regulation_schedule: A VoltageControlZone may have a  voltage
        regulation schedule.
    """
    busbar_section: Optional["BusbarSection"] = field(
        default=None,
        metadata={
            "name": "BusbarSection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    regulation_schedule: Optional["RegulationSchedule"] = field(
        default=None,
        metadata={
            "name": "RegulationSchedule",
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

    :ivar asset_info: Data applicable to this asset.
    :ivar location: Location of this asset.
    :ivar measurements:
    :ivar power_system_resources: All power system resources used to
        electrically model this asset. For example, transformer asset is
        electrically modelled with a transformer and its windings and
        tap changer.
    :ivar scheduled_events:
    """
    asset_info: Optional[AssetInfo] = field(
        default=None,
        metadata={
            "name": "AssetInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    measurements: List["Measurement"] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_system_resources: List[PowerSystemResource] = field(
        default_factory=list,
        metadata={
            "name": "PowerSystemResources",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    scheduled_events: List[ScheduledEvent] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class BusbarSectionInfo(AssetInfo):
    """
    Busbar section data.

    :ivar rated_current: Rated current.
    :ivar rated_voltage: Rated voltage.
    """
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConnectivityNode(IdentifiedObject):
    """
    Connectivity nodes are points where terminals of AC conducting equipment
    are connected together with zero impedance.

    :ivar connectivity_node_container: Container of this connectivity
        node.
    :ivar operational_limit_set:
    :ivar sv_injection:
    :ivar sv_voltage:
    :ivar terminals: Terminals interconnected with zero impedance at a
        this connectivity node.
    :ivar topological_node: The topological node to which this
        connectivity node is assigned.  May depend on the current state
        of switches in the network.
    """
    connectivity_node_container: Optional["ConnectivityNodeContainer"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNodeContainer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    operational_limit_set: List["OperationalLimitSet"] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimitSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sv_injection: List[SvInjection] = field(
        default_factory=list,
        metadata={
            "name": "SvInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sv_voltage: Optional[SvVoltage] = field(
        default=None,
        metadata={
            "name": "SvVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    terminals: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "name": "Terminals",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    topological_node: Optional[TopologicalNode] = field(
        default=None,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceInfo(AssetInfo):
    """
    End device data.

    :ivar is_solid_state: If true, this is a solid state end device (as
        opposed to a mechanical or electromechanical device).
    :ivar phase_count: Number of potential phases the end device
        supports, typically 0, 1 or 3.
    :ivar rated_current: Rated current.
    :ivar rated_voltage: Rated voltage.
    :ivar capability: Inherent capabilities of the device (i.e., the
        functions it supports).
    :ivar end_devices: All end devices described with this data.
    """
    is_solid_state: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSolidState",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "phaseCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
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
    end_devices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EquipmentContainer(ConnectivityNodeContainer):
    """
    A modeling construct to provide a root class for containing equipment.

    :ivar additional_grouped_equipment: The additonal contained
        equipment.  The equipment belong to the equipment container. The
        equipment is contained in another equipment container, but also
        grouped with this equipment container.  Examples include when a
        switch contained in a substation is also desired to be grouped
        with a line contianer or when a switch is included in a
        secondary substation and also grouped in a feeder.
    :ivar equipments: Contained equipment.
    """
    additional_grouped_equipment: List["Equipment"] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalGroupedEquipment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    equipments: List["Equipment"] = field(
        default_factory=list,
        metadata={
            "name": "Equipments",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Ieee1547Info(AssetInfo):
    class Meta:
        name = "IEEE1547Info"

    abnormal_performance_category: Optional[Ieee1547AbnormalPerfomanceCategory] = field(
        default=None,
        metadata={
            "name": "abnormalPerformanceCategory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    islanding_category: Optional[Ieee1547IslandingCategory] = field(
        default=None,
        metadata={
            "name": "islandingCategory",
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
    maximum_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minimum_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumU",
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
    normal_performance_category: Optional[Ieee1547NormalPerformanceCategory] = field(
        default=None,
        metadata={
            "name": "normalPerformanceCategory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    over_excited_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "overExcitedPF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_pat_unity_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPatUnityPF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_pcharge: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPcharge",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_pover_excited: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPoverExcited",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_punder_excited: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPunderExcited",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_qabsorbed: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedQabsorbed",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_qinjected: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedQinjected",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_scharge: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedScharge",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "serialNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_dynamic_reactive_current: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsDynamicReactiveCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_iec61850: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsIEC61850",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_ieee1815: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsIEEE1815",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_ieee20305: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsIEEE20305",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_islanding: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsIslanding",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_sun_spec_mod_bus_ethernet: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsSunSpecModBusEthernet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_sun_spec_mod_bus_rs485: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsSunSpecModBusRS485",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_volt_watt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsVoltWatt",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    supports_watt_var: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsWattVar",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    susceptance_cease_to_energize: Optional[float] = field(
        default=None,
        metadata={
            "name": "susceptanceCeaseToEnergize",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    under_excited_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "underExcitedPF",
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
    power_electronics_connections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rotating_machines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "name": "RotatingMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class LinearShuntCompensatorPhase(ShuntCompensatorPhase):
    """
    A per phase linear shunt compensator has banks or sections with equal
    admittance values.

    :ivar b_per_section: Susceptance per section of the phase if shunt
        compensator is wye connected.   Susceptance per section phase to
        phase if shunt compensator is delta connected.
    :ivar g_per_section: Conductance per section for this phase if shunt
        compensator is wye connected.  Conductance per section phase to
        phase if shunt compensator is delta connected.
    """
    b_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "bPerSection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    g_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "gPerSection",
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

    :ivar transformer_end: Transformer end to which this phase tap
        changer belongs.
    """
    transformer_end: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
            "name": "TransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class PowerTransformerInfo(AssetInfo):
    """
    Set of power transformer data, from an equipment library.

    :ivar transformer_tank_infos: Data for all the tanks described by
        this power transformer data.
    """
    transformer_tank_infos: List["TransformerTankInfo"] = field(
        default_factory=list,
        metadata={
            "name": "TransformerTankInfos",
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

    :ivar step_voltage_increment: Tap step increment, in per cent of
        neutral voltage, per step position. When the increment is
        negative, the voltage decreases when the tap step increases.
    :ivar transformer_end: Transformer end to which this ratio tap
        changer belongs.
    """
    step_voltage_increment: Optional[float] = field(
        default=None,
        metadata={
            "name": "stepVoltageIncrement",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    transformer_end: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
            "name": "TransformerEnd",
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

    :ivar max_power_loss: Maximum allowed apparent power loss.
    :ivar rated_current: Rated current.
    :ivar rated_reactive_power: Rated reactive power.
    :ivar rated_voltage: Rated voltage.
    """
    max_power_loss: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxPowerLoss",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class SwitchInfo(AssetInfo):
    """
    &amp;lt;was Switch data.&amp;gt; Switch datasheet information.

    :ivar breaking_capacity: The maximum fault current a breaking device
        can break safely under prescribed conditions of use.
    :ivar is_single_phase: If true, it is a single phase switch.
    :ivar is_unganged: If true, the switch is not ganged (i.e., a switch
        phase may be operated separately from other phases).
    :ivar low_pressure_alarm: Gas or air pressure at or below which a
        low pressure alarm is generated.
    :ivar low_pressure_lock_out: Gas or air pressure below which the
        breaker will not open.
    :ivar oil_volume_per_tank: Volume of oil in each tank of bulk oil
        breaker.
    :ivar rated_current: Rated current.
    :ivar rated_frequency: Frequency for which switch is rated.
    :ivar rated_impulse_withstand_voltage: Rated impulse withstand
        voltage, also known as BIL (Basic Impulse Level).
    :ivar rated_interrupting_time: Switch rated interrupting time in
        seconds.
    :ivar rated_voltage: Rated voltage.
    """
    breaking_capacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "breakingCapacity",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    is_single_phase: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSinglePhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    is_unganged: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isUnganged",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    low_pressure_alarm: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowPressureAlarm",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    low_pressure_lock_out: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowPressureLockOut",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    oil_volume_per_tank: Optional[float] = field(
        default=None,
        metadata={
            "name": "oilVolumePerTank",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_impulse_withstand_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedImpulseWithstandVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_interrupting_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedInterruptingTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
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

    :ivar line_drop_compensation: If true, the line drop compensation is
        to be applied.
    :ivar line_drop_r: Line drop compensator resistance setting for
        normal (forward) power flow.
    :ivar line_drop_x: Line drop compensator reactance setting for
        normal (forward) power flow.
    :ivar max_limit_voltage: Maximum allowed regulated voltage on the PT
        secondary, regardless of line drop compensation. Sometimes
        referred to as first-house protection.
    :ivar min_limit_voltage:
    :ivar reverse_line_drop_r: Line drop compensator resistance setting
        for reverse power flow.
    :ivar reverse_line_drop_x: Line drop compensator reactance setting
        for reverse power flow.
    :ivar tap_changer: The tap changers that participates in this
        regulating tap control scheme.
    """
    line_drop_compensation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "lineDropCompensation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    line_drop_r: Optional[float] = field(
        default=None,
        metadata={
            "name": "lineDropR",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    line_drop_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "lineDropX",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    max_limit_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxLimitVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    min_limit_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "minLimitVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reverse_line_drop_r: Optional[float] = field(
        default=None,
        metadata={
            "name": "reverseLineDropR",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    reverse_line_drop_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "reverseLineDropX",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    tap_changer: List["TapChanger"] = field(
        default_factory=list,
        metadata={
            "name": "TapChanger",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TapChangerInfo(AssetInfo):
    """
    Tap changer data.

    :ivar ct_rating: Built-in current transformer primary rating.
    :ivar ct_ratio: Built-in current transducer ratio.
    :ivar pt_ratio: Built-in voltage transducer ratio.
    """
    ct_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "ctRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ct_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "ctRatio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    pt_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "ptRatio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class TransformerEndInfo(AssetInfo):
    """
    Transformer end data.

    :ivar connection_kind: Kind of connection.
    :ivar emergency_s: Apparent power that the winding can carry under
        emergency conditions (also called long-term emergency power).
    :ivar end_number: Number for this transformer end, corresponding to
        the end's order in the PowerTransformer.vectorGroup attribute.
        Highest voltage winding should be 1.
    :ivar insulation_u: Basic insulation level voltage rating.
    :ivar phase_angle_clock: Winding phase angle where 360 degrees are
        represented with clock hours, so the valid values are {0, ...,
        11}. For example, to express the second winding in code 'Dyn11',
        set attributes as follows: 'endNumber'=2, 'connectionKind' = Yn
        and 'phaseAngleClock' = 11.
    :ivar r: DC resistance.
    :ivar rated_s: Normal apparent power rating.
    :ivar rated_u: Rated voltage: phase-phase for three-phase windings,
        and either phase-phase or phase-neutral for single-phase
        windings.
    :ivar short_term_s: Apparent power that this winding can carry for a
        short period of time (in emergency).
    :ivar core_admittance: Core admittance calculated from this
        transformer end datasheet, representing magnetising current and
        core losses. The full values of the transformer should be
        supplied for one transformer end info only.
    :ivar energised_end_no_load_tests: All no-load test measurements in
        which this transformer end was energised.
    :ivar energised_end_open_circuit_tests: All open-circuit test
        measurements in which this transformer end was excited.
    :ivar energised_end_short_circuit_tests: All short-circuit test
        measurements in which this transformer end was energised.
    :ivar from_mesh_impedances: All mesh impedances between this 'to'
        and other 'from' transformer ends.
    :ivar grounded_end_short_circuit_tests: All short-circuit test
        measurements in which this transformer end was short-circuited.
    :ivar open_end_open_circuit_tests: All open-circuit test
        measurements in which this transformer end was not excited.
    :ivar to_mesh_impedances: All mesh impedances between this 'from'
        and other 'to' transformer ends.
    :ivar transformer_tank_info: Transformer tank data that this end
        description is part of.
    """
    connection_kind: Optional[WindingConnection] = field(
        default=None,
        metadata={
            "name": "connectionKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    emergency_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "emergencyS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "endNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    insulation_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "insulationU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase_angle_clock: Optional[int] = field(
        default=None,
        metadata={
            "name": "phaseAngleClock",
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
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    short_term_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "shortTermS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    core_admittance: Optional["TransformerCoreAdmittance"] = field(
        default=None,
        metadata={
            "name": "CoreAdmittance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energised_end_no_load_tests: List[NoLoadTest] = field(
        default_factory=list,
        metadata={
            "name": "EnergisedEndNoLoadTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energised_end_open_circuit_tests: List[OpenCircuitTest] = field(
        default_factory=list,
        metadata={
            "name": "EnergisedEndOpenCircuitTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    energised_end_short_circuit_tests: List[ShortCircuitTest] = field(
        default_factory=list,
        metadata={
            "name": "EnergisedEndShortCircuitTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    from_mesh_impedances: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "name": "FromMeshImpedances",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    grounded_end_short_circuit_tests: List[ShortCircuitTest] = field(
        default_factory=list,
        metadata={
            "name": "GroundedEndShortCircuitTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    open_end_open_circuit_tests: List[OpenCircuitTest] = field(
        default_factory=list,
        metadata={
            "name": "OpenEndOpenCircuitTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    to_mesh_impedances: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "name": "ToMeshImpedances",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    transformer_tank_info: Optional["TransformerTankInfo"] = field(
        default=None,
        metadata={
            "name": "TransformerTankInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class TransformerTankInfo(AssetInfo):
    """
    Set of transformer tank data, from an equipment library.

    :ivar power_transformer_info: Power transformer data that this tank
        description is part of.
    :ivar transformer_end_infos: Data for all the ends described by this
        transformer tank data.
    :ivar transformer_tanks:
    """
    power_transformer_info: Optional["PowerTransformerInfo"] = field(
        default=None,
        metadata={
            "name": "PowerTransformerInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    transformer_end_infos: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "name": "TransformerEndInfos",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    transformer_tanks: List["TransformerTank"] = field(
        default_factory=list,
        metadata={
            "name": "TransformerTanks",
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

    :ivar is_cable: If true, this spacing data describes a cable.
    :ivar phase_wire_count: Number of wire sub-conductors in the
        symmetrical bundle (typically between 1 and 4).
    :ivar phase_wire_spacing: Distance between wire sub-conductors in a
        symmetrical bundle.
    :ivar acline_segments:
    :ivar wire_assembly_info:
    :ivar wire_positions: All positions of single wires (phase or
        neutral) making the conductor.
    """
    is_cable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isCable",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase_wire_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "phaseWireCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase_wire_spacing: Optional[float] = field(
        default=None,
        metadata={
            "name": "phaseWireSpacing",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    acline_segments: List["AclineSegment"] = field(
        default_factory=list,
        metadata={
            "name": "ACLineSegments",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_assembly_info: List["WireAssemblyInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WireAssemblyInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_positions: List[WirePosition] = field(
        default_factory=list,
        metadata={
            "name": "WirePositions",
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

    :ivar created_date_time: Date and time this activity record has been
        created (different from the 'status.dateTime', which is the time
        of a status change of the associated object, if applicable).
    :ivar type: Type of event resulting in this activity record.
    :ivar assets: All assets for which this activity record has been
        created.
    """
    created_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
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
    assets: List[Asset] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class AssetContainer(Asset):
    """
    Asset that is aggregation of other assets such as conductors, transformers,
    switchgear, land, fences, buildings, equipment, vehicles, etc.

    :ivar assets: All assets within this container asset.
    """
    assets: List[Asset] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class AssetFunction(IdentifiedObject):
    """
    Function performed by an asset.

    :ivar config_id: Configuration specified for this function.
    :ivar firmware_id: Firmware version.
    :ivar hardware_id: Hardware version.
    :ivar password: Password needed to access this function.
    :ivar program_id: Name of program.
    :ivar asset:
    """
    config_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "configID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    firmware_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "firmwareID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hardware_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "hardwareID",
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
    program_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "programID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    asset: Optional[Asset] = field(
        default=None,
        metadata={
            "name": "Asset",
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

    :ivar naming_secondary_substation: The secondary substations that
        are normally energized from the feeder.  Used for naming
        purposes.   Should be consistent with the other associations for
        energizing terminal specification and the feeder energization
        specification.
    :ivar normal_energized_substation: The substations that are normally
        energized by the feeder.
    :ivar normal_energizing_substation: The substation that nominally
        energizes the feeder.  Also used for naming purposes.
    :ivar normal_head_terminal: The normal head terminal or terminals of
        the feeder.
    """
    naming_secondary_substation: List["Substation"] = field(
        default_factory=list,
        metadata={
            "name": "NamingSecondarySubstation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normal_energized_substation: List["Substation"] = field(
        default_factory=list,
        metadata={
            "name": "NormalEnergizedSubstation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normal_energizing_substation: Optional["Substation"] = field(
        default=None,
        metadata={
            "name": "NormalEnergizingSubstation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normal_head_terminal: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "name": "NormalHeadTerminal",
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

    :ivar measurement_type: Specifies the type of measurement.  For
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
    :ivar asset:
    :ivar locations:
    :ivar power_system_resource: The power system resource that contains
        the measurement.
    :ivar terminal: One or more measurements may be associated with a
        terminal in the network.
    """
    measurement_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementType",
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
    asset: Optional[Asset] = field(
        default=None,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    locations: List[Location] = field(
        default_factory=list,
        metadata={
            "name": "Locations",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_system_resource: Optional[PowerSystemResource] = field(
        default=None,
        metadata={
            "name": "PowerSystemResource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    terminal: Optional["Acdcterminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
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

    :ivar connectivity_node:
    :ivar equipment: The equipment to which the limit set applies.
    :ivar operational_limit_value:
    :ivar terminal:
    """
    connectivity_node: Optional[ConnectivityNode] = field(
        default=None,
        metadata={
            "name": "ConnectivityNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    equipment: Optional["Equipment"] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    operational_limit_value: List[OperationalLimit] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimitValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    terminal: Optional["Acdcterminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
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

    :ivar region: The SubGeographicalRegion containing the substation.
    """
    region: Optional[SubGeographicalRegion] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WireAssemblyInfo(AssetInfo):
    """
    Describes the construction of a multi-conductor wire.
    """
    per_length_line_parameter: List[PerLengthLineParameter] = field(
        default_factory=list,
        metadata={
            "name": "PerLengthLineParameter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_phase_info: List["WirePhaseInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WirePhaseInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_spacing_info: Optional[WireSpacingInfo] = field(
        default=None,
        metadata={
            "name": "WireSpacingInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class Acdcterminal(IdentifiedObject):
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
    :ivar sequence_number: The orientation of the terminal connections
        for a multiple terminal conducting equipment.  The sequence
        numbering starts with 1 and additional terminals should follow
        in increasing order.   The first terminal is the "starting
        point" for a two terminal branch.
    :ivar measurements: Measurements associated with this terminal
        defining  where the measurement is placed in the network
        topology.  It may be used, for instance, to capture the sensor
        position, such as a voltage transformer (PT) at a busbar or a
        current transformer (CT) at the bar between a breaker and an
        isolator.
    :ivar operational_limit_set:
    """
    class Meta:
        name = "ACDCTerminal"

    connected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    operational_limit_set: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimitSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EndDeviceEvent(ActivityRecord):
    """
    Event detected by a device function associated with the end device.

    :ivar issuer_id: Unique identifier of the business entity
        originating an end device control.
    :ivar issuer_tracking_id: Identifier assigned by the initiator (e.g.
        retail electric provider) of an end device control action to
        uniquely identify the demand response event, text message, or
        other subject of the control action. Can be used when cancelling
        an event or text message request or to identify the originating
        event or text message in a consequential end device event.
    :ivar user_id: (if user initiated) ID of user who initiated this end
        device event.
    :ivar end_device: End device that reported this end device event.
    :ivar end_device_event_details: All details of this end device
        event.
    :ivar end_device_event_type: Type of this end device event.
    :ivar meter_reading: Set of measured values to which this event
        applies.
    :ivar usage_point: Usage point for which this end device event is
        reported.
    """
    issuer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    issuer_tracking_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerTrackingID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "userID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "name": "EndDevice",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_event_details: List[EndDeviceEventDetail] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEventDetails",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_event_type: Optional[EndDeviceEventType] = field(
        default=None,
        metadata={
            "name": "EndDeviceEventType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    meter_reading: Optional[MeterReading] = field(
        default=None,
        metadata={
            "name": "MeterReading",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    usage_point: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "name": "UsagePoint",
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
    :ivar end_device: End device that performs this function.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "name": "EndDevice",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or
    mechanical.

    :ivar in_service: If true, the equipment is in service.
    :ivar faults: All faults on this equipment.
    :ivar operational_limit_set: The operational limit sets associated
        with this equipment.
    """
    in_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inService",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    faults: List["Fault"] = field(
        default_factory=list,
        metadata={
            "name": "Faults",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    operational_limit_set: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimitSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class WirePhaseInfo:
    """
    :ivar phase_info:
    :ivar sequence_number: Numbering for wires on a WireSpacingInfo.
        Neutrals should be numbered last.
    :ivar wire_assembly_info:
    :ivar wire_info:
    :ivar wire_position:
    """
    phase_info: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "name": "phaseInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_assembly_info: Optional[WireAssemblyInfo] = field(
        default=None,
        metadata={
            "name": "WireAssemblyInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    wire_info: Optional["WireInfo"] = field(
        default=None,
        metadata={
            "name": "WireInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_position: Optional[WirePosition] = field(
        default=None,
        metadata={
            "name": "WirePosition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConductingEquipment(Equipment):
    """
    The parts of the AC power system that are designed to carry current or that
    are conductively connected through terminals.

    :ivar base_voltage: Base voltage of this conducting equipment.  Use
        only when there is no voltage level container used and only one
        base voltage applies.  For example, not used for transformers.
    :ivar sv_status: The status state variable associated with this
        conducting equipment.
    :ivar terminals: Conducting equipment have terminals that may be
        connected to other conducting equipment terminals via
        connectivity nodes or topological nodes.
    """
    base_voltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "name": "BaseVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sv_status: List[SvStatus] = field(
        default_factory=list,
        metadata={
            "name": "SvStatus",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    terminals: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "name": "Terminals",
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

    :ivar amr_system: Automated meter reading (AMR) or other
        communication system responsible for communications to this end
        device.
    :ivar install_code: Installation code.
    :ivar is_pan: If true, this is a premises area network (PAN) device.
    :ivar is_smart_inverter:
    :ivar is_virtual: If true, there is no physical device. As an
        example, a virtual meter can be defined to aggregate the
        consumption for two or more physical meters. Otherwise, this is
        a physical hardware device.
    :ivar time_zone_offset: Time zone offset relative to GMT for the
        location of this end device.
    :ivar customer: Customer owning this end device.
    :ivar dispatchable_power_capability:
    :ivar end_device_controls: All end device controls sending commands
        to this end device.
    :ivar end_device_events: All events reported by this end device.
    :ivar end_device_functions: All end device functions this end device
        performs.
    :ivar end_device_groups: All end device groups referring to this end
        device.
    :ivar end_device_info: End device data.
    :ivar usage_point: Usage point to which this end device belongs.
    """
    amr_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "amrSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    install_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "installCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    is_pan: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPan",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    is_smart_inverter: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSmartInverter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    is_virtual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isVirtual",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    time_zone_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeZoneOffset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    customer: Optional[Customer] = field(
        default=None,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dispatchable_power_capability: List["DispatchablePowerCapability"] = field(
        default_factory=list,
        metadata={
            "name": "DispatchablePowerCapability",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_controls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_events: List[EndDeviceEvent] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_functions: List[EndDeviceFunction] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceFunctions",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_groups: Optional["EndDeviceGroup"] = field(
        default=None,
        metadata={
            "name": "EndDeviceGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_info: Optional[EndDeviceInfo] = field(
        default=None,
        metadata={
            "name": "EndDeviceInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    usage_point: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "name": "UsagePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class PowerElectronicsUnit(Equipment):
    """
    A generating unit or battery or aggregation that connects to the AC network
    using power electronics rather than rotating machines.

    :ivar max_p: Maximum active power limit. This is the maximum
        (nameplate) limit for the unit.
    :ivar min_p: Minimum active power limit. This is the minimum
        (nameplate) limit for the unit.
    :ivar power_electronics_connection:
    """
    max_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    min_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "minP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_electronics_connection: Optional["PowerElectronicsConnection"] = field(
        default=None,
        metadata={
            "name": "PowerElectronicsConnection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )


@dataclass
class Terminal(Acdcterminal):
    """An AC electrical connection point to a piece of conducting equipment.

    Terminals are connected at physical connection points called
    connectivity nodes.

    :ivar conducting_equipment: The conducting equipment of the
        terminal.  Conducting equipment have  terminals that may be
        connected to other conducting equipment terminals via
        connectivity nodes or topological nodes.
    :ivar connectivity_node: The connectivity node to which this
        terminal connects with zero impedance.
    :ivar equipment_faults: The equipment faults at this terminal.
    :ivar normal_head_feeder: The feeder that this terminal normally
        feeds.  Only specifed for the terminals at head of feeders.
    :ivar regulating_control: The controls regulating this terminal.
    :ivar remote_input_signals:
    :ivar sv_power_flow: The power flow state variable associated with
        the terminal.
    :ivar topological_node: The topological node associated with the
        terminal.   This can be used as an alternative to the
        connectivity node path to topological node, thus making it
        unneccesary to model connectivity nodes in some cases.   Note
        that the if connectivity nodes are in the model, this
        association would probably not be used as an input
        specification.
    :ivar transformer_end: All transformer ends connected at this
        terminal.
    """
    conducting_equipment: Optional["ConductingEquipment"] = field(
        default=None,
        metadata={
            "name": "ConductingEquipment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    connectivity_node: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    equipment_faults: List["EquipmentFault"] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentFaults",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normal_head_feeder: Optional["Feeder"] = field(
        default=None,
        metadata={
            "name": "NormalHeadFeeder",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    regulating_control: List["RegulatingControl"] = field(
        default_factory=list,
        metadata={
            "name": "RegulatingControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    remote_input_signals: List[RemoteInputSignal] = field(
        default_factory=list,
        metadata={
            "name": "RemoteInputSignals",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sv_power_flow: List[SvPowerFlow] = field(
        default_factory=list,
        metadata={
            "name": "SvPowerFlow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    topological_node: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    transformer_end: List[TransformerEnd] = field(
        default_factory=list,
        metadata={
            "name": "TransformerEnd",
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

    :ivar power_transformer: Bank this transformer belongs to.
    :ivar transformer_tank_ends: All windings of this transformer.
    :ivar transformer_tank_info:
    """
    power_transformer: Optional["PowerTransformer"] = field(
        default=None,
        metadata={
            "name": "PowerTransformer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    transformer_tank_ends: List["TransformerTankEnd"] = field(
        default_factory=list,
        metadata={
            "name": "TransformerTankEnds",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    transformer_tank_info: Optional["TransformerTankInfo"] = field(
        default=None,
        metadata={
            "name": "TransformerTankInfo",
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

    :ivar core_radius: (if there is a different core material) Radius of
        the central core.
    :ivar core_strand_count: (if used) Number of strands in the steel
        core.
    :ivar gmr: Geometric mean radius. If we replace the conductor by a
        thin walled tube of radius GMR, then its reactance is identical
        to the reactance of the actual conductor.
    :ivar insulated: True if conductor is insulated.
    :ivar insulation_material: (if insulated conductor) Material used
        for insulation.
    :ivar insulation_thickness: (if insulated conductor) Thickness of
        the insulation.
    :ivar material: Conductor material.
    :ivar r_ac25: AC resistance per unit length of the conductor at 25
        °C.
    :ivar r_ac50: AC resistance per unit length of the conductor at 50
        °C.
    :ivar r_ac75: AC resistance per unit length of the conductor at 75
        °C.
    :ivar radius: Outside radius of the wire.
    :ivar rated_current: Current carrying capacity of the wire under
        stated thermal conditions.
    :ivar r_dc20: DC resistance per unit length of the conductor at 20
        °C.
    :ivar size_description: Describes the wire gauge or cross section
        (e.g., 4/0, #2, 336.5).
    :ivar strand_count: Number of strands in the conductor.
    :ivar acline_segment_phases:
    :ivar wire_phase_info:
    """
    core_radius: Optional[float] = field(
        default=None,
        metadata={
            "name": "coreRadius",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    core_strand_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "coreStrandCount",
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
    insulation_material: Optional[WireInsulationKind] = field(
        default=None,
        metadata={
            "name": "insulationMaterial",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    insulation_thickness: Optional[float] = field(
        default=None,
        metadata={
            "name": "insulationThickness",
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
    r_ac25: Optional[float] = field(
        default=None,
        metadata={
            "name": "rAC25",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r_ac50: Optional[float] = field(
        default=None,
        metadata={
            "name": "rAC50",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r_ac75: Optional[float] = field(
        default=None,
        metadata={
            "name": "rAC75",
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
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    r_dc20: Optional[float] = field(
        default=None,
        metadata={
            "name": "rDC20",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    size_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "sizeDescription",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    strand_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "strandCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    acline_segment_phases: List["AclineSegmentPhase"] = field(
        default_factory=list,
        metadata={
            "name": "ACLineSegmentPhases",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_phase_info: List[WirePhaseInfo] = field(
        default_factory=list,
        metadata={
            "name": "WirePhaseInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class AclineSegmentPhase(PowerSystemResource):
    """
    Represents a single wire of an alternating current line segment.

    :ivar phase: The phase connection of the wire at both ends.
    :ivar sequence_number: Number designation for this line segment
        phase. Each line segment phase within a line segment should have
        a unique sequence number. This is useful for unbalanced modeling
        to bind the mathematical model (PhaseImpedanceData of
        PerLengthPhaseImpedance) with the connectivity model (this
        class) and the physical model (WirePosition, WirePhaseInfo)
        without tight coupling. Multiple circuits on the same pole,
        tower or right-of-way can be included with unique sequence
        numbers for the phases, and identical sequence numbers for any
        shared neutrals.
    :ivar acline_segment: The line segment to which the phase belongs.
    :ivar wire_info:
    """
    class Meta:
        name = "ACLineSegmentPhase"

    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    acline_segment: Optional["AclineSegment"] = field(
        default=None,
        metadata={
            "name": "ACLineSegment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    wire_info: Optional[WireInfo] = field(
        default=None,
        metadata={
            "name": "WireInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class CableInfo(WireInfo):
    """
    Cable data.

    :ivar construction_kind: Kind of construction of this cable.
    :ivar diameter_over_core: Diameter over the core, including any
        semi-con screen; should be the insulating layer's inside
        diameter.
    :ivar diameter_over_insulation: Diameter over the insulating layer,
        excluding outer screen.
    :ivar diameter_over_jacket: Diameter over the outermost jacketing
        layer.
    :ivar diameter_over_screen: Diameter over the outer screen; should
        be the shield's inside diameter.
    :ivar is_strand_fill: True if wire strands are extruded in a way to
        fill the voids in the cable.
    :ivar nominal_temperature: Maximum nominal design operating
        temperature.
    :ivar outer_jacket_kind: Kind of outer jacket of this cable.
    :ivar sheath_as_neutral: True if sheath / shield is used as a
        neutral (i.e., bonded).
    :ivar shield_material: Material of the shield.
    """
    construction_kind: Optional[CableConstructionKind] = field(
        default=None,
        metadata={
            "name": "constructionKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    diameter_over_core: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverCore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    diameter_over_insulation: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverInsulation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    diameter_over_jacket: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverJacket",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    diameter_over_screen: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverScreen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    is_strand_fill: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isStrandFill",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    nominal_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalTemperature",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    outer_jacket_kind: Optional[CableOuterJacketKind] = field(
        default=None,
        metadata={
            "name": "outerJacketKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sheath_as_neutral: Optional[bool] = field(
        default=None,
        metadata={
            "name": "sheathAsNeutral",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    shield_material: Optional[CableShieldMaterialKind] = field(
        default=None,
        metadata={
            "name": "shieldMaterial",
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
    :ivar current_active_power: Product of RMS value of the voltage and
        the RMS value of the in-phase component of the current
    :ivar current_apparent_power: Product of the RMS value of the
        voltage and the RMS value of the current
    :ivar current_reactive_power: Product of RMS value of the voltage
        and the RMS value of the quadrature component of the current
    :ivar max_active_power: Product of RMS value of the voltage and the
        RMS value of the in-phase component of the current
    :ivar max_apparent_power: Product of the RMS value of the voltage
        and the RMS value of the current
    :ivar max_reactive_power: Product of RMS value of the voltage and
        the RMS value of the quadrature component of the current
    :ivar min_active_power: Product of RMS value of the voltage and the
        RMS value of the in-phase component of the current
    :ivar min_apparent_power: Product of the RMS value of the voltage
        and the RMS value of the current
    :ivar min_reactive_power: Product of RMS value of the voltage and
        the RMS value of the quadrature component of the current
    :ivar end_device:
    :ivar end_device_group:
    """
    current_active_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "currentActivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    current_apparent_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "currentApparentPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    current_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "currentReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    max_active_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxActivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    max_apparent_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxApparentPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    max_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    min_active_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "minActivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    min_apparent_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "minApparentPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    min_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "minReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device: Optional[EndDevice] = field(
        default=None,
        metadata={
            "name": "EndDevice",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_group: Optional["EndDeviceGroup"] = field(
        default=None,
        metadata={
            "name": "EndDeviceGroup",
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

    :ivar meter_readings: All meter readings provided by this meter.
    """
    meter_readings: List["MeterReading"] = field(
        default_factory=list,
        metadata={
            "name": "MeterReadings",
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

    :ivar vector_group: Vector group of the transformer for protective
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
    :ivar power_transformer_end: The ends of this power transformer.
    :ivar transformer_tanks: All transformers that belong to this bank.
    """
    vector_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "vectorGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_transformer_end: List["PowerTransformerEnd"] = field(
        default_factory=list,
        metadata={
            "name": "PowerTransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    transformer_tanks: List["TransformerTank"] = field(
        default_factory=list,
        metadata={
            "name": "TransformerTanks",
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
class AclineSegment(Conductor):
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
    :ivar acline_segment_phases: The line segment phases which belong to
        the line segment.
    :ivar per_length_impedance: Per-length impedance of this line
        segment.
    :ivar wire_spacing_info:
    """
    class Meta:
        name = "ACLineSegment"

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
    acline_segment_phases: List[AclineSegmentPhase] = field(
        default_factory=list,
        metadata={
            "name": "ACLineSegmentPhases",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    per_length_impedance: Optional[PerLengthImpedance] = field(
        default=None,
        metadata={
            "name": "PerLengthImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    wire_spacing_info: Optional[WireSpacingInfo] = field(
        default=None,
        metadata={
            "name": "WireSpacingInfo",
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

    :ivar ip_max: Maximum allowable peak short-circuit current of busbar
        (Ipmax in the IEC 60909-0). Mechanical limit of the busbar in
        the substation itself. Used for short circuit data exchange
        according to IEC 60909
    :ivar voltage_control_zone: A VoltageControlZone is controlled by a
        designated BusbarSection.
    """
    ip_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "ipMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltage_control_zone: Optional["VoltageControlZone"] = field(
        default=None,
        metadata={
            "name": "VoltageControlZone",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConcentricNeutralCableInfo(CableInfo):
    """
    Concentric neutral cable data.

    :ivar diameter_over_neutral: Diameter over the concentric neutral
        strands.
    :ivar neutral_strand_count: Number of concentric neutral strands.
    :ivar neutral_strand_gmr: Geometric mean radius of the neutral
        strand.
    :ivar neutral_strand_radius: Outside radius of the neutral strand.
    :ivar neutral_strand_rdc20: DC resistance per unit length of the
        neutral strand at 20 °C.
    """
    diameter_over_neutral: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverNeutral",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutral_strand_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "neutralStrandCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutral_strand_gmr: Optional[float] = field(
        default=None,
        metadata={
            "name": "neutralStrandGmr",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutral_strand_radius: Optional[float] = field(
        default=None,
        metadata={
            "name": "neutralStrandRadius",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    neutral_strand_rdc20: Optional[float] = field(
        default=None,
        metadata={
            "name": "neutralStrandRDC20",
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
    :ivar demand_response_programs: All demand response programs this
        group of end devices is enrolled in.
    :ivar derfunction:
    :ivar dergroup_dispatch:
    :ivar dergroup_forecast:
    :ivar dermonitorable_parameter:
    :ivar dispatchable_power_capability:
    :ivar end_device_controls: All end device controls sending commands
        to this end device group.
    :ivar end_devices: All end devices this end device group refers to.
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
    demand_response_programs: List[DemandResponseProgram] = field(
        default_factory=list,
        metadata={
            "name": "DemandResponsePrograms",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derfunction: Optional[Derfunction] = field(
        default=None,
        metadata={
            "name": "DERFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dergroup_dispatch: List[DergroupDispatch] = field(
        default_factory=list,
        metadata={
            "name": "DERGroupDispatch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dergroup_forecast: List[DergroupForecast] = field(
        default_factory=list,
        metadata={
            "name": "DERGroupForecast",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    dermonitorable_parameter: List[DermonitorableParameter] = field(
        default_factory=list,
        metadata={
            "name": "DERMonitorableParameter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dispatchable_power_capability: Optional[DispatchablePowerCapability] = field(
        default=None,
        metadata={
            "name": "DispatchablePowerCapability",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_controls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_devices: List[EndDevice] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
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

    :ivar customer_count: Number of individual customers represented by
        this demand.
    :ivar grounded: Used for Yn and Zn connections. True if the neutral
        is solidly grounded.
    :ivar p: Active power of the load. Load sign convention is used,
        i.e. positive sign means flow out from a node. For voltage
        dependent loads the value is at rated voltage. Starting value
        for a steady state solution.
    :ivar phase_connection: The type of phase connection, such as wye or
        delta.
    :ivar q: Reactive power of the load. Load sign convention is used,
        i.e. positive sign means flow out from a node. For voltage
        dependent loads the value is at rated voltage. Starting value
        for a steady state solution.
    :ivar energy_consumer_phase: The individual phase models for this
        energy consumer.
    :ivar house:
    :ivar load_response: The load response characteristic of this load.
        If missing, this load is assumed to be constant power.
    :ivar power_cut_zone: The  energy consumer is assigned to this power
        cut zone.
    """
    customer_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "customerCount",
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
    phase_connection: Optional[PhaseShuntConnectionKind] = field(
        default=None,
        metadata={
            "name": "phaseConnection",
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
    energy_consumer_phase: List[EnergyConsumerPhase] = field(
        default_factory=list,
        metadata={
            "name": "EnergyConsumerPhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    house: Optional[House] = field(
        default=None,
        metadata={
            "name": "House",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    load_response: Optional[LoadResponseCharacteristic] = field(
        default=None,
        metadata={
            "name": "LoadResponse",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_cut_zone: Optional[PowerCutZone] = field(
        default=None,
        metadata={
            "name": "PowerCutZone",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class EnergySource(EnergyConnection):
    """
    A generic equivalent for an energy supplier on a transmission or
    distribution voltage level.

    :ivar nominal_voltage: Phase-to-phase nominal voltage.
    :ivar r: Positive sequence Thevenin resistance.
    :ivar r0: Zero sequence Thevenin resistance.
    :ivar voltage_angle: Phase angle of a-phase open circuit.
    :ivar voltage_magnitude: Phase-to-phase open circuit voltage
        magnitude.
    :ivar x: Positive sequence Thevenin reactance.
    :ivar x0: Zero sequence Thevenin reactance.
    :ivar energy_source_phase: The individual phase information of the
        energy source.
    """
    nominal_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalVoltage",
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
    voltage_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltageAngle",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    voltage_magnitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltageMagnitude",
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
    energy_source_phase: List[EnergySourcePhase] = field(
        default_factory=list,
        metadata={
            "name": "EnergySourcePhase",
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

    :ivar control_enabled: Specifies the regulation status of the
        equipment.  True is regulating, false is not regulating.
    :ivar regulating_control: The regulating control scheme in which
        this equipment participates.
    """
    control_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "controlEnabled",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    regulating_control: Optional["RegulatingControl"] = field(
        default=None,
        metadata={
            "name": "RegulatingControl",
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

    :ivar tape_lap: Percentage of the tape shield width that overlaps in
        each wrap, typically 10% to 25%.
    :ivar tape_thickness: Thickness of the tape shield, before wrapping.
    """
    tape_lap: Optional[float] = field(
        default=None,
        metadata={
            "name": "tapeLap",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    tape_thickness: Optional[float] = field(
        default=None,
        metadata={
            "name": "tapeThickness",
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

    :ivar dr_program_level: Level of a demand response program request,
        where 0=emergency. Note: Attribute is not defined on
        DemandResponseProgram as it is not its inherent property (it
        serves to control it).
    :ivar dr_program_mandatory: Whether a demand response program
        request is mandatory. Note: Attribute is not defined on
        DemandResponseProgram as it is not its inherent property (it
        serves to control it).
    :ivar issuer_id: Unique identifier of the business entity
        originating an end device control.
    :ivar issuer_tracking_id: Identifier assigned by the initiator (e.g.
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
    :ivar end_device_action: End device action issued by this end device
        control.
    :ivar end_device_control_type: Type of this end device control.
    :ivar end_device_groups: All end device groups receiving commands
        from this end device control.
    :ivar end_devices: All end devices receiving commands from this end
        device control.
    :ivar price_signal: (if applicable) Price signal used as parameter
        for this end device control.
    :ivar primary_device_timing: Timing for the control actions
        performed on the device identified in the end device control.
    :ivar scheduled_interval: (if control has scheduled duration) Date
        and time interval the control has been scheduled to execute
        within.
    :ivar secondary_device_timing: Timing for the control actions
        performed by devices that are responding to event related
        information sent to the primary device indicated in the end
        device control.  For example, load control actions performed by
        a PAN device in response to demand response event information
        sent to a PAN gateway server.
    :ivar usage_point_groups: All usage point groups receiving commands
        from this end device control.
    :ivar usage_points: All usage points receiving commands from this
        end device control.
    """
    dr_program_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "drProgramLevel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    dr_program_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "drProgramMandatory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    issuer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    issuer_tracking_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerTrackingID",
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
    end_device_action: Optional[EndDeviceAction] = field(
        default=None,
        metadata={
            "name": "EndDeviceAction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_control_type: Optional[EndDeviceControlType] = field(
        default=None,
        metadata={
            "name": "EndDeviceControlType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    end_device_groups: List[EndDeviceGroup] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_devices: List[EndDevice] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    price_signal: Optional[FloatQuantity] = field(
        default=None,
        metadata={
            "name": "priceSignal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    primary_device_timing: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "name": "primaryDeviceTiming",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    scheduled_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "scheduledInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    secondary_device_timing: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "name": "secondaryDeviceTiming",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    usage_point_groups: List[UsagePointGroup] = field(
        default_factory=list,
        metadata={
            "name": "UsagePointGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
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

    :ivar inverter_mode:
    :ivar max_ifault: Maximum fault current this device will contribute,
        in per-unit of rated current, before the converter protection
        will trip or bypass.
    :ivar max_q: Maximum reactive power limit. This is the maximum
        (nameplate) limit for the unit.
    :ivar min_q: Minimum reactive power limit for the unit. This is the
        minimum (nameplate) limit for the unit.
    :ivar p: Active power injection. Load sign convention is used, i.e.
        positive sign means flow out from a node. Starting value for a
        steady state solution.
    :ivar q: Reactive power injection. Load sign convention is used,
        i.e. positive sign means flow out from a node. Starting value
        for a steady state solution.
    :ivar rated_s: Nameplate apparent power rating for the unit. The
        attribute shall have a positive value.
    :ivar rated_u: Rated voltage (nameplate data, Ur in IEC 60909-0). It
        is primarily used for short circuit data exchange according to
        IEC 60909.
    :ivar derdynamics: DER dynamics model associated with this power
        electronics connection model.
    :ivar ieee1547_control_settings:
    :ivar ieee1547_info:
    :ivar ieee1547_setting:
    :ivar ieee1547_trip_settings:
    :ivar power_electronics_connection_phases:
    :ivar power_electronics_unit:
    """
    inverter_mode: Optional[ConverterControlMode] = field(
        default=None,
        metadata={
            "name": "inverterMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    max_ifault: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxIFault",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    max_q: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxQ",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    min_q: Optional[float] = field(
        default=None,
        metadata={
            "name": "minQ",
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
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    derdynamics: Optional["Derdynamics"] = field(
        default=None,
        metadata={
            "name": "DERDynamics",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ieee1547_control_settings: Optional[Ieee1547ControlSettings] = field(
        default=None,
        metadata={
            "name": "IEEE1547ControlSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ieee1547_info: Optional["Ieee1547Info"] = field(
        default=None,
        metadata={
            "name": "IEEE1547Info",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ieee1547_setting: Optional[Ieee1547Setting] = field(
        default=None,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ieee1547_trip_settings: Optional[Ieee1547TripSettings] = field(
        default=None,
        metadata={
            "name": "IEEE1547TripSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_electronics_connection_phases: List["PowerElectronicsConnectionPhase"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnectionPhases",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    power_electronics_unit: List["PowerElectronicsUnit"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsUnit",
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
    :ivar rated_power_factor: Power factor (nameplate data). It is
        primarily used for short circuit data exchange according to IEC
        60909.
    :ivar rated_s: Nameplate apparent power rating for the unit. The
        attribute shall have a positive value.
    :ivar rated_u: Rated voltage (nameplate data, Ur in IEC 60909-0). It
        is primarily used for short circuit data exchange according to
        IEC 60909.
    :ivar ieee1547_control_settings:
    :ivar ieee1547_info:
    :ivar ieee1547_setting:
    :ivar ieee1547_trip_settings:
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
    rated_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ieee1547_control_settings: Optional["Ieee1547ControlSettings"] = field(
        default=None,
        metadata={
            "name": "IEEE1547ControlSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ieee1547_info: Optional["Ieee1547Info"] = field(
        default=None,
        metadata={
            "name": "IEEE1547Info",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ieee1547_setting: Optional[Ieee1547Setting] = field(
        default=None,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    ieee1547_trip_settings: Optional[Ieee1547TripSettings] = field(
        default=None,
        metadata={
            "name": "IEEE1547TripSettings",
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

    :ivar a_vrdelay: Time delay required for the device to be connected
        or disconnected by automatic voltage regulation (AVR).
    :ivar grounded: Used for Yn and Zn connections. True if the neutral
        is solidly grounded.
    :ivar maximum_sections: The maximum number of sections that may be
        switched in.
    :ivar nom_u: The voltage at which the nominal reactive power may be
        calculated. This should normally be within 10% of the voltage at
        which the capacitor is connected to the network.
    :ivar normal_sections: The normal number of sections switched in.
    :ivar phase_connection: The type of phase connection, such as wye or
        delta.
    :ivar sections: Shunt compensator sections in use. Starting value
        for steady state solution. Non integer values are allowed to
        support continuous variables. The reasons for continuous value
        are to support study cases where no discrete shunt compensators
        has yet been designed, a solutions where a narrow voltage band
        force the sections to oscillate or accommodate for a continuous
        solution as input.
    :ivar shunt_compensator_phase: The individual phases models for the
        shunt compensator.
    :ivar sv_shunt_compensator_sections: The state for the number of
        shunt compensator sections in service.
    """
    a_vrdelay: Optional[float] = field(
        default=None,
        metadata={
            "name": "aVRDelay",
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
    maximum_sections: Optional[int] = field(
        default=None,
        metadata={
            "name": "maximumSections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    nom_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "nomU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    normal_sections: Optional[int] = field(
        default=None,
        metadata={
            "name": "normalSections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase_connection: Optional[PhaseShuntConnectionKind] = field(
        default=None,
        metadata={
            "name": "phaseConnection",
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
    shunt_compensator_phase: List[ShuntCompensatorPhase] = field(
        default_factory=list,
        metadata={
            "name": "ShuntCompensatorPhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    sv_shunt_compensator_sections: Optional[SvShuntCompensatorSections] = field(
        default=None,
        metadata={
            "name": "SvShuntCompensatorSections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class LinearShuntCompensator(ShuntCompensator):
    """
    A linear shunt compensator has banks or sections with equal admittance
    values.

    :ivar b0_per_section: Zero sequence shunt (charging) susceptance per
        section
    :ivar b_per_section: Positive sequence shunt (charging) susceptance
        per section
    :ivar g0_per_section: Zero sequence shunt (charging) conductance per
        section
    :ivar g_per_section: Positive sequence shunt (charging) conductance
        per section
    """
    b0_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "b0PerSection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    b_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "bPerSection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    g0_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "g0PerSection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    g_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "gPerSection",
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

    :ivar ami_billing_ready: Tracks the lifecycle of the metering
        installation at a usage point with respect to readiness for
        billing via advanced metering infrastructure reads.
    :ivar check_billing: True if as a result of an inspection or
        otherwise, there is a reason to suspect that a previous billing
        may have been performed with erroneous data. Value should be
        reset once this potential discrepancy has been resolved.
    :ivar connection_state: State of the usage point with respect to
        connection to the network.
    :ivar estimated_load: Estimated load.
    :ivar grounded: True if grounded.
    :ivar is_sdp: If true, this usage point is a service delivery point,
        i.e., a usage point where the ownership of the service changes
        hands.
    :ivar is_virtual: If true, this usage point is virtual, i.e., no
        physical location exists in the network where a meter could be
        located to collect the meter readings. For example, one may
        define a virtual usage point to serve as an aggregation of usage
        for all of a company's premises distributed widely across the
        distribution territory. Otherwise, the usage point is physical,
        i.e., there is a logical point in the network where a meter
        could be located to collect meter readings.
    :ivar minimal_usage_expected: If true, minimal or zero usage is
        expected at this usage point for situations such as premises
        vacancy, logical or physical disconnect. It is used for readings
        validation and estimation.
    :ivar nominal_service_voltage: Nominal service voltage.
    :ivar outage_region: Outage region in which this usage point is
        located.
    :ivar phase_code: Phase code. Number of wires and specific nominal
        phases can be deduced from enumeration literal values. For
        example, ABCN is three-phase, four-wire, s12n
        (splitSecondary12N) is single-phase, three-wire, and s1n and s2n
        are single-phase, two-wire.
    :ivar rated_current: Current flow that this usage point is
        configured to deliver.
    :ivar rated_power: Active power that this usage point is configured
        to deliver.
    :ivar read_cycle: Cycle day on which the meter for this usage point
        will normally be read.  Usually correlated with the billing
        cycle.
    :ivar read_route: Identifier of the route to which this usage point
        is assigned for purposes of meter reading. Typically used to
        configure hand held meter reading systems prior to collection of
        reads.
    :ivar service_delivery_remark: Remarks about this usage point, for
        example the reason for it being rated with a non-nominal
        priority.
    :ivar service_priority: Priority of service for this usage point.
        Note that usage points at the same service location can have
        different priorities.
    :ivar end_device_controls: All end device controls sending commands
        to this usage point.
    :ivar end_device_events: All end device events reported for this
        usage point.
    :ivar end_devices: All end devices at this usage point.
    :ivar equipments: All equipment connecting this usage point to the
        electrical grid.
    :ivar meter_readings: All meter readings obtained from this usage
        point.
    """
    ami_billing_ready: Optional[AmiBillingReadyKind] = field(
        default=None,
        metadata={
            "name": "amiBillingReady",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    check_billing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "checkBilling",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    connection_state: Optional[UsagePointConnectedKind] = field(
        default=None,
        metadata={
            "name": "connectionState",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    estimated_load: Optional[float] = field(
        default=None,
        metadata={
            "name": "estimatedLoad",
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
    is_sdp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSdp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    is_virtual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isVirtual",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    minimal_usage_expected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "minimalUsageExpected",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    nominal_service_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalServiceVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    outage_region: Optional[str] = field(
        default=None,
        metadata={
            "name": "outageRegion",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    phase_code: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "name": "phaseCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    rated_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    read_cycle: Optional[str] = field(
        default=None,
        metadata={
            "name": "readCycle",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    read_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "readRoute",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    service_delivery_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceDeliveryRemark",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    service_priority: Optional[str] = field(
        default=None,
        metadata={
            "name": "servicePriority",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_controls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_device_events: List[EndDeviceEvent] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    end_devices: List[EndDevice] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    equipments: List[Equipment] = field(
        default_factory=list,
        metadata={
            "name": "Equipments",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    meter_readings: List[MeterReading] = field(
        default_factory=list,
        metadata={
            "name": "MeterReadings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )


@dataclass
class ConfigurationEvent(ActivityRecord):
    """
    Used to report details on creation, change or deletion of an entity or its
    configuration.

    :ivar effective_date_time: Date and time this event has or will
        become effective.
    :ivar modified_by: Source/initiator of modification.
    :ivar remark: Free text remarks.
    :ivar changed_asset: Asset whose change resulted in this
        configuration event.
    :ivar changed_usage_point: Usage point whose change resulted in this
        configuration event.
    :ivar fault_cause_type:
    :ivar power_system_resource:
    """
    effective_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "effectiveDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    modified_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "modifiedBy",
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
    changed_asset: Optional[Asset] = field(
        default=None,
        metadata={
            "name": "ChangedAsset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    changed_usage_point: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "name": "ChangedUsagePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    fault_cause_type: Optional[FaultCauseType] = field(
        default=None,
        metadata={
            "name": "FaultCauseType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "required": True,
        }
    )
    power_system_resource: Optional[PowerSystemResource] = field(
        default=None,
        metadata={
            "name": "PowerSystemResource",
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

    :ivar coolant_temperature: The machine's coolant temperature (e.g.,
        ambient air or stator circulating water).
    :ivar hydrogen_pressure: The hydrogen coolant pressure
    :ivar initially_used_by_synchronous_machines: Synchronous machines
        using this curve as default.
    :ivar synchronous_machines: Synchronous machines using this curve.
    """
    coolant_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "coolantTemperature",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    hydrogen_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "hydrogenPressure",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
        }
    )
    initially_used_by_synchronous_machines: List[SynchronousMachine] = field(
        default_factory=list,
        metadata={
            "name": "InitiallyUsedBySynchronousMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )
    synchronous_machines: List[SynchronousMachine] = field(
        default_factory=list,
        metadata={
            "name": "SynchronousMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/",
            "min_occurs": 1,
        }
    )

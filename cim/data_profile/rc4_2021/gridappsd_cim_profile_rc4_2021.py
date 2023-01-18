from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime

__NAMESPACE__ = "http://iec.ch/TC57/CIM100#"


class AstmstandardEditionKind(Enum):
    """
    List of editions of ASTM standards.
    """
    VALUE_00_2005 = "00(2005)"
    VALUE_00_2005_E1 = "00(2005)e1"
    VALUE_00_2010 = "00(2010)"
    VALUE_01 = "01"
    VALUE_01A_2007 = "01a(2007)"
    VALUE_01E1 = "01e1"
    VALUE_02 = "02"
    VALUE_02_2007 = "02(2007)"
    VALUE_02_2008 = "02(2008)"
    VALUE_02_2009 = "02(2009)"
    VALUE_02_2012 = "02(2012)"
    VALUE_02_2014 = "02(2014)"
    VALUE_02A = "02a"
    VALUE_02B = "02b"
    VALUE_02E1 = "02e1"
    VALUE_03 = "03"
    VALUE_03_2008 = "03(2008)"
    VALUE_03_2014 = "03(2014)"
    VALUE_03A = "03a"
    VALUE_04 = "04"
    VALUE_04A = "04a"
    VALUE_04AE1 = "04ae1"
    VALUE_04E1 = "04e1"
    VALUE_04E2 = "04e2"
    VALUE_05 = "05"
    VALUE_05_2010 = "05(2010)"
    VALUE_05A = "05a"
    VALUE_05A_2010 = "05a(2010)"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_07_2013 = "07(2013)"
    VALUE_08 = "08"
    VALUE_08E1 = "08e1"
    VALUE_09 = "09"
    VALUE_09_2013 = "09(2013)"
    VALUE_10 = "10"
    VALUE_10A = "10a"
    VALUE_11 = "11"
    VALUE_11A = "11a"
    VALUE_12 = "12"
    VALUE_12A = "12a"
    VALUE_12B = "12b"
    VALUE_13 = "13"
    VALUE_13E1 = "13e1"
    VALUE_14 = "14"
    VALUE_14A = "14a"
    VALUE_14E1 = "14e1"
    VALUE_14E2 = "14e2"
    VALUE_15 = "15"
    VALUE_15A = "15a"
    VALUE_65 = "65"
    VALUE_71 = "71"
    VALUE_74 = "74"
    VALUE_80E1 = "80e1"
    VALUE_82 = "82"
    VALUE_83_1996_E1 = "83(1996)e1"
    VALUE_85 = "85"
    VALUE_85_1990_E1 = "85(1990)e1"
    VALUE_87_1995 = "87(1995)"
    VALUE_87E1 = "87e1"
    VALUE_88 = "88"
    VALUE_90E1 = "90e1"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_94 = "94"
    VALUE_94_1999 = "94(1999)"
    VALUE_94_2004 = "94(2004)"
    VALUE_94_2010 = "94(2010)"
    VALUE_94E1 = "94e1"
    VALUE_95 = "95"
    VALUE_95_2000_E1 = "95(2000)e1"
    VALUE_96 = "96"
    VALUE_96_2002_E1 = "96(2002)e1"
    VALUE_96A = "96a"
    VALUE_96E1 = "96e1"
    VALUE_97 = "97"
    VALUE_97_2002 = "97(2002)"
    VALUE_97_2003 = "97(2003)"
    VALUE_97_2008 = "97(2008)"
    VALUE_97A = "97a"
    VALUE_97A_2004 = "97a(2004)"
    VALUE_98 = "98"
    VALUE_98A = "98a"
    VALUE_99 = "99"
    VALUE_99_2004_E1 = "99(2004)e1"
    VALUE_99_2005 = "99(2005)"
    VALUE_99_2009 = "99(2009)"
    VALUE_99A = "99a"
    VALUE_99A_2004 = "99a(2004)"
    VALUE_99E1 = "99e1"
    VALUE_99E2 = "99e2"
    NONE = "none"
    UNKNOWN = "unknown"


class AstmstandardKind(Enum):
    """
    List of ASTM standards.

    :cvar D1169: Standard Test Method for Specific Resistance
        (Resistivity) of Electrical Insulating Liquids.
    :cvar D1275: Standard Test Method for Corrosive Sulfur in Electrical
        Insulating Oils.
    :cvar D1298: Standard Test Method for Density, Relative Density, or
        API Gravity of Crude Petroleum and Liquid Petroleum Products by
        Hydrometer Method  -or- Standard Test Method for Density,
        Relative Density (Specific Gravity), or API Gravity of Crude
        Petroleum and Liquid Petroleum Products by Hydrometer Method.
    :cvar D149: Standard Test Method for Dielectric Breakdown Voltage
        and Dielectric Strength of Solid Electrical Insulating Materials
        at Commercial Power Frequencies.
    :cvar D1500: Standard Test Method for ASTM Color of Petroleum
        Products (ASTM Color Scale).
    :cvar D1524: Standard Test Method for Visual Examination of Used
        Electrical Insulating Oils of Petroleum Origin in the Field.
    :cvar D1533: Standard Test Method for Water in Insulating Liquids by
        Coulometric Karl Fischer Titration.
    :cvar D1816: Standard Test Method for Dielectric Breakdown Voltage
        of Insulating Liquids Using VDE Electrodes.
    :cvar D2029: Standard Test Methods for Water Vapor Content of
        Electrical Insulating Gases by Measurement of Dew Point.
    :cvar D2112: Standard Test Method for Oxidation Stability of
        Inhibited Mineral Insulating Oil by Pressure Vessel.
    :cvar D2129: Standard Test Method for Color of Clear Electrical
        Insulating Liquids (Platinum-Cobalt Scale).
    :cvar D2140: Standard Practice for Calculating Carbon-Type
        Composition of Insulating Oils of Petroleum Origin  -or-
        Standard Test Method for Carbon-Type Composition of Insulating
        Oils of Petroleum Origin.
    :cvar D2144: Standard Practices for Examination of Electrical
        Insulating Oils by Infrared Absorption  -or- Standard Test
        Methods for Examination of Electrical Insulating Oils by
        Infrared Absorption.
    :cvar D2668: Standard Test Method for 2,6-di-tert-Butyl- p-Cresol
        and 2,6-di-tert-Butyl Phenol in Electrical Insulating Oil by
        Infrared Absorption  -or- Standard Test Method for
        2,6-Ditertiary-Butyl Para Cresol and 2,6-Ditertiary-Butyl Phenol
        in Electrical Insulating Oil by Infrared Absorption.
    :cvar D3612: Standard Test Method for Analysis of Gases Dissolved in
        Electrical Insulating Oil by Gas Chromatography.
    :cvar D4052: Standard Test Method for Density, Relative Density, and
        API Gravity of Liquids by Digital Density Meter  -or- Standard
        Test Method for Density and Relative Density of Liquids by
        Digital Density Meter.
    :cvar D4059: Standard Test Method for Analysis of Polychlorinated
        Biphenyls in Insulating Liquids by Gas Chromatography.
    :cvar D4230: Standard Test Method of Measuring Humidity with Cooled-
        Surface Condensation (Dew-Point) Hygrometer.
    :cvar D4243: Standard Test Method for Measurement of Average
        Viscometric Degree of Polymerization of New and Aged Electrical
        Papers and Boards.
    :cvar D445: Standard Test Method for Kinematic Viscosity of
        Transparent and Opaque Liquids (and Calculation of Dynamic
        Viscosity)  -or- Standard Method Of Test For Viscosity Of
        Transparent And Opaque Liquids (Kinematic And Dynamic
        Viscosities).
    :cvar D4768: Standard Test Method for Analysis of 2,6-Ditertiary-
        Butyl Para-Cresol and 2,6-Ditertiary-Butyl Phenol in Insulating
        Liquids by Gas Chromatography.
    :cvar D5837: Standard Test Method for Furanic Compounds in
        Electrical Insulating Liquids by High-Performance Liquid
        Chromatography (HPLC).
    :cvar D5853: Standard Test Method for Pour Point of Crude Oils.
    :cvar D5949: Standard Test Method for Pour Point of Petroleum
        Products (Automatic Pressure Pulsing Method).
    :cvar D5950: Standard Test Method for Pour Point of Petroleum
        Products (Automatic Tilt Method).
    :cvar D5985: Standard Test Method for Pour Point of Petroleum
        Products (Rotational Method).
    :cvar D6304: Standard Test Method for Determination of Water in
        Petroleum Products, Lubricating Oils, and Additives by
        Coulometric Karl Fischer Titration.
    :cvar D6749: Standard Test Method for Pour Point of Petroleum
        Products (Automatic Air Pressure Method).
    :cvar D6786: Standard Test Method for Particle Count in Mineral
        Insulating Oil Using Automatic Optical Particle Counters.
    :cvar D6892: Standard Test Method for Pour Point of Petroleum
        Products (Robotic Tilt Method).
    :cvar D7151: Standard Test Method for Determination of Elements in
        Insulating Oils by Inductively Coupled Plasma Atomic Emission
        Spectrometry (ICP-AES).
    :cvar D7346: Standard Test Method for No Flow Point and Pour Point
        of Petroleum Products and Liquid Fuels  -or- Standard Test
        Method for No Flow Point and Pour Point of Petroleum Products
        -or- Standard Test Method for No Flow Point of Petroleum
        Products.
    :cvar D828: Standard Test Method for Tensile Properties of Paper and
        Paperboard Using Constant-Rate-of-Elongation Apparatus
        (Withdrawn 2009).
    :cvar D877: Standard Test Method for Dielectric Breakdown Voltage of
        Insulating Liquids Using Disk Electrodes.
    :cvar D877_D877_M: Standard Test Method for Dielectric Breakdown
        Voltage of Insulating Liquids Using Disk Electrodes.
    :cvar D92: Standard Test Method for Flash and Fire Points by
        Cleveland Open Cup Tester  -or- Standard Test Method for Flash
        and Fire Points by Cleveland Open Cup.
    :cvar D924: Standard Test Method for Dissipation Factor (or Power
        Factor) and Relative Permittivity (Dielectric Constant) of
        Electrical Insulating Liquids.
    :cvar D93: Standard Test Methods for Flash Point by Pensky-Martens
        Closed Cup Tester  -or- Standard Test Method for Flash Point by
        Pensky-Martens Closed Tester  -or- Standard Method Of Test For
        Flash Point by Pensky-Martens Closed Tester.
    :cvar D97: Standard Test Method for Pour Point of Petroleum Products
        -or- Standard Test Method for Pour Point of Petroleum Oils.
    :cvar D974: Standard Test Method for Acid and Base Number by Color-
        Indicator Titration.
    """
    D1169 = "D1169"
    D1275 = "D1275"
    D1298 = "D1298"
    D149 = "D149"
    D1500 = "D1500"
    D1524 = "D1524"
    D1533 = "D1533"
    D1816 = "D1816"
    D2029 = "D2029"
    D2112 = "D2112"
    D2129 = "D2129"
    D2140 = "D2140"
    D2144 = "D2144"
    D2668 = "D2668"
    D3612 = "D3612"
    D4052 = "D4052"
    D4059 = "D4059"
    D4230 = "D4230"
    D4243 = "D4243"
    D445 = "D445"
    D4768 = "D4768"
    D5837 = "D5837"
    D5853 = "D5853"
    D5949 = "D5949"
    D5950 = "D5950"
    D5985 = "D5985"
    D6304 = "D6304"
    D6749 = "D6749"
    D6786 = "D6786"
    D6892 = "D6892"
    D7151 = "D7151"
    D7346 = "D7346"
    D828 = "D828"
    D877 = "D877"
    D877_D877_M = "D877/D877M"
    D92 = "D92"
    D924 = "D924"
    D93 = "D93"
    D97 = "D97"
    D974 = "D974"


@dataclass
class AcceptanceTest:
    """
    Acceptance test for assets.

    :ivar date_time: Date and time the asset was last tested using the
        'type' of test and yielding the current status in 'success'
        attribute.
    :ivar success: True if asset has passed acceptance test and may be
        placed in or is in service. It is set to false if asset is
        removed from service and is required to be tested again before
        being placed back in service, possibly in a new location. Since
        asset may go through multiple tests during its lifecycle, the
        date of each acceptance test may be recorded in
        'Asset.ActivityRecord.status.dateTime'.
    :ivar type: Type of test or group of tests that was conducted on
        'dateTime'.
    """
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AccountNotification:
    """
    Notifications for move-in, move-out, delinquencies, etc.
    """
    customer_notification_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerNotificationType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    method_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "methodType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_account: Optional["CustomerAccount"] = field(
        default=None,
        metadata={
            "name": "CustomerAccount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


class AccumulationKind(Enum):
    """
    Kind of accumulation behaviour for read / measured values from individual
    end points.

    :cvar BOUNDED_QUANTITY: A time-independent cumulative quantity much
        like a 'bulkQuantity' or a 'latchingQuantity', except that the
        accumulation stops at the maximum or minimum values. When the
        maximum is reached, any additional positive accumulation is
        discarded, but negative accumulation may be accepted (thus
        lowering the counter.) Likewise, when the negative bound is
        reached, any additional negative accumulation is discarded, but
        positive accumulation is accepted (thus increasing the counter.)
    :cvar BULK_QUANTITY: A value from a register which represents the
        bulk quantity of a commodity. This quantity is computed as the
        integral of the commodity usage rate. This value is typically
        used as the basis for the dial reading at the meter, and as a
        result, will roll over upon reaching a maximum dial value. Note
        1: With the metering system, the roll-over behaviour typically
        implies a roll-under behavior so that the value presented is
        always a positive value (e.g. unsigned integer or positive
        decimal.) However, when communicating data between enterprise
        applications a negative value might occur in a case such as net
        metering. Note 2: A 'bulkQuantity' refers primarily to the dial
        reading and not the consumption over a specific period of time.
    :cvar CONTINUOUS_CUMULATIVE: The sum of the previous billing period
        values and the present period value. Note:
        'continuousCumulative' is commonly used in conjunction with
        'demand', and it  would represent the cumulative sum of the
        previous billing period maximum demand values (as occurring with
        each demand reset) summed with the present period maximum demand
        value (which has yet to be reset.)
    :cvar CUMULATIVE: The sum of the previous billing period values.
        Note: 'cumulative' is commonly used in conjunction with
        ï¿½demand.ï¿½ Each demand reset causes the maximum demand value
        for the present billing period (since the last demand reset) to
        accumulate as an accumulative total of all maximum demands. So
        instead of 'zeroing' the demand register, a demand reset has the
        effect of adding the present maximum demand to this accumulating
        total.
    :cvar DELTA_DATA: The difference between the value at the end of the
        prescribed interval and the beginning of the interval. This is
        used for incremental interval data. Note: One common application
        would be for load profile data, another use might be to report
        the number of events within an interval (such as the number of
        equipment energisations within the specified period of time.)
    :cvar INDICATING: As if a needle is swung out on the meter face to a
        value to indicate the current value. Note: An 'indicating' value
        is typically measured over hundreds of milliseconds or greater,
        or may imply a ï¿½pusherï¿½ mechanism to capture a value.
        Compare this to 'instantaneous' which is measured over a shorter
        period of time.
    :cvar INSTANTANEOUS: Typically measured over the fastest period of
        time allowed by the definition of the metric (usually
        milliseconds or tens of milliseconds.) Note: 'instantaneous' was
        moved to attribute #3 in Ed.2 of IEC 61968-9, from attribute #1
        in Ed.1 of IEC 61968-9.
    :cvar LATCHING_QUANTITY: When this description is applied to a
        metered value, it implies that the value is a time-independent
        cumulative quantity much like a 'bulkQuantity', except that it
        latches upon the maximum value upon reaching that value. Any
        additional accumulation (positive or negative) is discarded
        until a reset occurs. Note: A 'latchingQuantity' may also occur
        in the downward direction ï¿½ upon reaching a minimum value. The
        terms 'maximum' or 'minimum' (for 'aggregate') will usually be
        included when this type of accumulation behaviour is present.
        When this description is applied to an encoded value (UOM=
        'Code'), it implies that the value has one or more bits which
        are latching. The condition that caused the bit to be set may
        have long since evaporated. In either case, the timestamp that
        accompanies the value may not coincide with the moment the value
        was initially set. In both cases a system will need to perform
        an operation to clear the latched value.
    :cvar NONE: Not applicable, or implied by the unit of measure.
    :cvar SUMMATION: A form of accumulation which is selective with
        respect to time. Note : 'summation' could be considered a
        specialisation of 'bulkQuantity' as it selectively accumulates
        pulses over a timing pattern (while 'bulkQuantity' accumulates
        pulses all of the time).
    :cvar TIME_DELAY: A form of computation which introduces a time
        delay characteristic to the data value.
    """
    BOUNDED_QUANTITY = "boundedQuantity"
    BULK_QUANTITY = "bulkQuantity"
    CONTINUOUS_CUMULATIVE = "continuousCumulative"
    CUMULATIVE = "cumulative"
    DELTA_DATA = "deltaData"
    INDICATING = "indicating"
    INSTANTANEOUS = "instantaneous"
    LATCHING_QUANTITY = "latchingQuantity"
    NONE = "none"
    SUMMATION = "summation"
    TIME_DELAY = "timeDelay"


class AggregateKind(Enum):
    """
    Kind of aggregation for read / measured values from multiple end points.

    :cvar AVERAGE: The value represents average.
    :cvar EXCESS: The value represents an amount over which a threshold
        was exceeded.
    :cvar FIFTH_MAXIMUM: The fifth highest value observed.
    :cvar FOURTH_MAXIMUM: The fourth highest value observed.
    :cvar HIGH_THRESHOLD: The value represents a programmed high
        threshold.
    :cvar LOW_THRESHOLD: The value represents a programmed low
        threshold.
    :cvar MAXIMUM: The highest value observed.
    :cvar MINIMUM: The smallest value observed.
    :cvar NOMINAL: The nominal value.
    :cvar NONE: Not applicable.
    :cvar NORMAL: The normal value.
    :cvar SECOND_MAXIMUM: The second highest value observed.
    :cvar SECOND_MINIMUM: The second smallest value observed.
    :cvar SUM: The accumulated sum.
    :cvar THIRD_MAXIMUM: The third highest value observed.
    """
    AVERAGE = "average"
    EXCESS = "excess"
    FIFTH_MAXIMUM = "fifthMaximum"
    FOURTH_MAXIMUM = "fourthMaximum"
    HIGH_THRESHOLD = "highThreshold"
    LOW_THRESHOLD = "lowThreshold"
    MAXIMUM = "maximum"
    MINIMUM = "minimum"
    NOMINAL = "nominal"
    NONE = "none"
    NORMAL = "normal"
    SECOND_MAXIMUM = "secondMaximum"
    SECOND_MINIMUM = "secondMinimum"
    SUM = "sum"
    THIRD_MAXIMUM = "thirdMaximum"


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


class AnalyticKind(Enum):
    """
    Possible kinds of analytics.
    """
    AGING_ANALYTIC = "agingAnalytic"
    FAULT_ANALYTIC = "faultAnalytic"
    HEALTH_ANALYTIC = "healthAnalytic"
    OTHER = "other"
    REPLACEMENT_ANALYTIC = "replacementAnalytic"
    RISK_ANALYTIC = "riskAnalytic"


class AssetFailureClassification(Enum):
    DEFECT = "defect"
    MAJOR = "major"
    MAJOR_NEEDS_REPLACEMENT = "majorNeedsReplacement"
    MINOR = "minor"


class AssetFailureMode(Enum):
    """What asset has failed to be able to do.

    Reason for breaker failure.
    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    FAIL_TO_CARRY_LOAD = "failToCarryLoad"
    FAIL_TO_CLOSE = "failToClose"
    FAIL_TO_INTERRUPT = "failToInterrupt"
    FAIL_TO_OPEN = "failToOpen"
    FAIL_TO_PROVIDE_INSULATION_LEVEL = "failToProvideInsulationLevel"


class AssetGroupKind(Enum):
    """
    Possible kinds of asset groups.

    :cvar ANALYSIS_GROUP:
    :cvar COMPLIANCE_GROUP:
    :cvar FUNCTIONAL_GROUP: assets grouped together for a particular
        function - such as a group of feeders.
    :cvar INVENTORY_GROUP:
    :cvar OTHER:
    """
    ANALYSIS_GROUP = "analysisGroup"
    COMPLIANCE_GROUP = "complianceGroup"
    FUNCTIONAL_GROUP = "functionalGroup"
    INVENTORY_GROUP = "inventoryGroup"
    OTHER = "other"


class AssetHazardKind(Enum):
    """Type of hazard that is posed to asset in this location.

    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).

    :cvar AMBIENT_TEMP_ABOVE38: Subject to ambient temperature above 38
        ï¿½C.
    :cvar AMBIENT_TEMP_BELOW_MINUS12: Subject to ambient temperature of
        below -12 ï¿½C.
    :cvar CHILDREN_AT_PLAY: Children play in area (stray kite/ball
        hazard).
    :cvar FISHING_AREA: Fishing in area (fishing pole/line hazard).
    :cvar OTHER: If other, look at type field for more information.
    :cvar VEGETATION: Vegetation growing below asset that may cause
        problem.
    """
    AMBIENT_TEMP_ABOVE38 = "ambientTempAbove38"
    AMBIENT_TEMP_BELOW_MINUS12 = "ambientTempBelowMinus12"
    CHILDREN_AT_PLAY = "childrenAtPlay"
    FISHING_AREA = "fishingArea"
    OTHER = "other"
    VEGETATION = "vegetation"


class AssetKind(Enum):
    """
    :cvar BREAKER_AIR_BLAST_BREAKER:
    :cvar BREAKER_BULK_OIL_BREAKER:
    :cvar BREAKER_INSULATING_STACK_ASSEMBLY:
    :cvar BREAKER_MINIMUM_OIL_BREAKER:
    :cvar BREAKER_SF6_DEAD_TANK_BREAKER:
    :cvar BREAKER_SF6_LIVE_TANK_BREAKER:
    :cvar BREAKER_TANK_ASSEMBLY:
    :cvar OTHER: Other type of Asset. The type attribute may provide
        more details in this case.
    :cvar TRANSFORMER:
    :cvar TRANSFORMER_TANK:
    """
    BREAKER_AIR_BLAST_BREAKER = "breakerAirBlastBreaker"
    BREAKER_BULK_OIL_BREAKER = "breakerBulkOilBreaker"
    BREAKER_INSULATING_STACK_ASSEMBLY = "breakerInsulatingStackAssembly"
    BREAKER_MINIMUM_OIL_BREAKER = "breakerMinimumOilBreaker"
    BREAKER_SF6_DEAD_TANK_BREAKER = "breakerSF6DeadTankBreaker"
    BREAKER_SF6_LIVE_TANK_BREAKER = "breakerSF6LiveTankBreaker"
    BREAKER_TANK_ASSEMBLY = "breakerTankAssembly"
    OTHER = "other"
    TRANSFORMER = "transformer"
    TRANSFORMER_TANK = "transformerTank"


class AssetModelUsageKind(Enum):
    """
    Usage for an asset model.

    :cvar CUSTOMER_SUBSTATION: Asset model is intended for use in
        customer substation.
    :cvar DISTRIBUTION_OVERHEAD: Asset model is intended for use in
        distribution overhead network.
    :cvar DISTRIBUTION_UNDERGROUND: Asset model is intended for use in
        underground distribution network.
    :cvar OTHER: Other kind of asset model usage.
    :cvar STREETLIGHT: Asset model is intended for use as streetlight.
    :cvar SUBSTATION: Asset model is intended for use in substation.
    :cvar TRANSMISSION: Asset model is intended for use in transmission
        network.
    :cvar UNKNOWN: Usage of the asset model is unknown.
    """
    CUSTOMER_SUBSTATION = "customerSubstation"
    DISTRIBUTION_OVERHEAD = "distributionOverhead"
    DISTRIBUTION_UNDERGROUND = "distributionUnderground"
    OTHER = "other"
    STREETLIGHT = "streetlight"
    SUBSTATION = "substation"
    TRANSMISSION = "transmission"
    UNKNOWN = "unknown"


class AsynchronousMachineKind(Enum):
    """
    Kind of Asynchronous Machine.

    :cvar GENERATOR: The Asynchronous Machine is a generator.
    :cvar MOTOR: The Asynchronous Machine is a motor.
    """
    GENERATOR = "generator"
    MOTOR = "motor"


class AtmosphericAnalogKind(Enum):
    """
    Kinds of analogs measuring an atmospheric condition.

    :cvar ALBEDO:
    :cvar AMBIENT_TEMPERATURE: The temperature measured b&lt;font
        color="#0f0f0f"&gt;y a thermometer exposed to the air in a place
        sheltered from direct solar radiation. &lt;/font&gt;Also known
        as "dry bulb" because&lt;font color="#0f0f0f"&gt; the air
        temperature is indicated by a thermometer not
        affecte&lt;/font&gt;d by the moisture of the air.
    :cvar ATMOSPHERIC_PRESSURE:
    :cvar CEILING:
    :cvar DEW_POINT: The temperature to which air must be cooled at
        constant pressure and constant water-vapor content in order for
        saturation to occur. In other words, it is the temperature at
        which water vapor starts to condense out of the air.
    :cvar HEAT_INDEX: The temperature of how hot it "feels like" for a
        given combination of warm air temperature and relative humidity.
    :cvar HORIZONTAL_VISIBILITY:
    :cvar HUMIDITY:
    :cvar ICE:
    :cvar ILLUMINANCE_DIFFUSE_HORIZONTAL:
    :cvar ILLUMINANCE_DIRECT_NORMAL:
    :cvar ILLUMINANCE_GLOBAL_HORIZONTAL:
    :cvar IRRADIANCE_DIFFUSE_HORIZONAL:
    :cvar IRRADIANCE_DIRECT_NORMAL:
    :cvar IRRADIANCE_EXTRA_TERRESTRIAL_HORIZONTAL:
    :cvar IRRADIANCE_EXTRA_TERRESTRIAL_VERTICAL:
    :cvar IRRADIANCE_GLOBAL_HORIZONTAL:
    :cvar LUMINANCE_ZENITH:
    :cvar PRECIPITATION:
    :cvar RAIN:
    :cvar SKY_COVERAGE_OPAQUE:
    :cvar SKY_COVERAGE_TOTAL:
    :cvar SNOW: Snow amount over a specified period of time.
    :cvar VERTICAL_VISIBILITY:
    :cvar WIND_CHILL: The temperature of how cold it "feels like" based
        on the rate of heat loss from exposed skin caused by the effects
        of wind and cold temperatures.
    :cvar WIND_SPEED_GUST: Maximum instantaneous wind speed in the 10
        minute period preceding a moment in time so long as more than 10
        knots of difference has been exhibited between peaks and lulls
        during that 10 minute time period. 0 value means no gusts during
        preceding 10 minute period.
    :cvar WIND_SPEED_INSTANTANEOUS: Wind speed at a moment in time.
    :cvar WIND_SPEED_PEAK: Peak instantaneous wind speed in the 60
        minutes preceding a moment in time as long as peak speed greater
        than 25 knots. 0 value means speed did not exceed 25 knots
        during preceding 60 minutes.
    :cvar WIND_SPEED_SUSTAINED: Average instantaneous wind speed over
        the 2-minute time period preceding a moment in time.
    """
    ALBEDO = "albedo"
    AMBIENT_TEMPERATURE = "ambientTemperature"
    ATMOSPHERIC_PRESSURE = "atmosphericPressure"
    CEILING = "ceiling"
    DEW_POINT = "dewPoint"
    HEAT_INDEX = "heatIndex"
    HORIZONTAL_VISIBILITY = "horizontalVisibility"
    HUMIDITY = "humidity"
    ICE = "ice"
    ILLUMINANCE_DIFFUSE_HORIZONTAL = "illuminanceDiffuseHorizontal"
    ILLUMINANCE_DIRECT_NORMAL = "illuminanceDirectNormal"
    ILLUMINANCE_GLOBAL_HORIZONTAL = "illuminanceGlobalHorizontal"
    IRRADIANCE_DIFFUSE_HORIZONAL = "irradianceDiffuseHorizonal"
    IRRADIANCE_DIRECT_NORMAL = "irradianceDirectNormal"
    IRRADIANCE_EXTRA_TERRESTRIAL_HORIZONTAL = "irradianceExtraTerrestrialHorizontal"
    IRRADIANCE_EXTRA_TERRESTRIAL_VERTICAL = "irradianceExtraTerrestrialVertical"
    IRRADIANCE_GLOBAL_HORIZONTAL = "irradianceGlobalHorizontal"
    LUMINANCE_ZENITH = "luminanceZenith"
    PRECIPITATION = "precipitation"
    RAIN = "rain"
    SKY_COVERAGE_OPAQUE = "skyCoverageOpaque"
    SKY_COVERAGE_TOTAL = "skyCoverageTotal"
    SNOW = "snow"
    VERTICAL_VISIBILITY = "verticalVisibility"
    WIND_CHILL = "windChill"
    WIND_SPEED_GUST = "windSpeedGust"
    WIND_SPEED_INSTANTANEOUS = "windSpeedInstantaneous"
    WIND_SPEED_PEAK = "windSpeedPeak"
    WIND_SPEED_SUSTAINED = "windSpeedSustained"


class BatteryState(Enum):
    """
    :cvar CHARGING: storedE is increasing
    :cvar DISCHARGING: storedE is decreasing
    :cvar EMPTY: unable to Discharge, and not Charging
    :cvar FULL: unable to Charge, and not Discharging
    :cvar WAITING: neither Charging nor Discharging, but able to do so
    """
    CHARGING = "Charging"
    DISCHARGING = "Discharging"
    EMPTY = "Empty"
    FULL = "Full"
    WAITING = "Waiting"


class BreakerApplicationKind(Enum):
    """Classifications of network roles in which breakers can be deployed.

    The classifications are intended to reflect both criticality of breaker in network operations and typical usage experienced by breaker.
    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    BUS_BREAKER = "busBreaker"
    BUS_TIE_BREAKER = "busTieBreaker"
    CAPACITOR_OR_REACTOR_BANK_BREAKER = "capacitorOrReactorBankBreaker"
    FEEDER_BREAKER = "feederBreaker"
    OTHER = "other"
    SPARE = "spare"
    STEP_UP_TRANSFORMER_BREAKER_FOSSIL = "stepUpTransformerBreakerFossil"
    STEP_UP_TRANSFORMER_BREAKER_HYDRO = "stepUpTransformerBreakerHydro"
    STEP_UP_TRANSFORMER_BREAKER_NUCLEAR = "stepUpTransformerBreakerNuclear"
    STEP_UP_TRANSFORMER_BREAKER_PUMPED_STORAGE = "stepUpTransformerBreakerPumpedStorage"
    SUBSTATION_TRANSFORMER_BREAKER = "substationTransformerBreaker"
    TRANSMISSION_FLOW_GATE_LINE_BREAKER = "transmissionFlowGateLineBreaker"
    TRANSMISSION_LINE_BREAKER = "transmissionLineBreaker"
    TRANSMISSION_TIE_LINE_BREAKER = "transmissionTieLineBreaker"


class BreakerConfiguration(Enum):
    """
    Switching arrangement for bay.

    :cvar BREAKER_AND_AHALF: Breaker and a half.
    :cvar DOUBLE_BREAKER: Double breaker.
    :cvar NO_BREAKER: No breaker.
    :cvar SINGLE_BREAKER: Single breaker.
    """
    BREAKER_AND_AHALF = "breakerAndAHalf"
    DOUBLE_BREAKER = "doubleBreaker"
    NO_BREAKER = "noBreaker"
    SINGLE_BREAKER = "singleBreaker"


class BreakerFailureReasonKind(Enum):
    """Reason for breaker failure.

    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    SF6_BLAST_VALVE_FAILURE = "SF6BlastValveFailure"
    SF6_PUFFER_FAILURE = "SF6PufferFailure"
    BLAST_VALVE_FAILURE = "blastValveFailure"
    BUSHING_FAILURE = "bushingFailure"
    CLOSE_COIL_OPEN_SHORTED_FAILED = "closeCoilOpenShortedFailed"
    CONTAMINATED_AIR = "contaminatedAir"
    CONTAMINATED_ARC_CHUTES = "contaminatedArcChutes"
    CONTAMINATED_GAS = "contaminatedGas"
    CONTAMINATED_GAS_AIR = "contaminatedGasAir"
    CONTROL_CIRCUIT_FAILURE = "controlCircuitFailure"
    DEGRADED_LUBRICATION = "degradedLubrication"
    EXTERNAL_OR_INTERNAL_CONTAMINATION = "externalOrInternalContamination"
    HIGH_PRESSURE_AIR_PLANT = "highPressureAirPlant"
    HIGH_RESISTANCE_LOAD_PATH = "highResistanceLoadPath"
    HIGH_RESISTANCE_PATH = "highResistancePath"
    INTERRUPTER_CONTACT_FAILURE = "interrupterContactFailure"
    INTERRUPTER_FAILURE = "interrupterFailure"
    LINKAGE_FAILURE = "linkageFailure"
    LOSS_OF_OIL = "lossOfOil"
    LOSS_OF_VACUUM = "lossOfVacuum"
    LOW_GAS_PRESSURE = "lowGasPressure"
    MECHANISM_FAILURE = "mechanismFailure"
    MECHANISM_OR_LINKAGE_FAILURE = "mechanismOrLinkageFailure"
    OIL_RELATED_FAILURE = "oilRelatedFailure"
    POOR_OIL_QUALITY = "poorOilQuality"
    RACKING_MECHANISM_FAILURE = "rackingMechanismFailure"
    RESISTOR_FAILURE = "resistorFailure"
    RESISTOR_GRADING_CAPACITOR_FAILURE = "resistorGradingCapacitorFailure"
    SOLID_DIELECTRIC_FAILURE = "solidDielectricFailure"
    STORED_ENERGY_FAILURE = "storedEnergyFailure"
    TRIP_COIL_OPEN_SHORTED_FAILED = "tripCoilOpenShortedFailed"


class BusbarConfiguration(Enum):
    """
    Busbar layout for bay.

    :cvar DOUBLE_BUS: Double bus.
    :cvar MAIN_WITH_TRANSFER: Main bus with transfer bus.
    :cvar RING_BUS: Ring bus.
    :cvar SINGLE_BUS: Single bus.
    """
    DOUBLE_BUS = "doubleBus"
    MAIN_WITH_TRANSFER = "mainWithTransfer"
    RING_BUS = "ringBus"
    SINGLE_BUS = "singleBus"


class BushingInsulationKind(Enum):
    """
    Insulation kind for bushings.

    :cvar COMPOUND:
    :cvar OIL_IMPREGNATED_PAPER: &amp;lt;was paperoil&amp;gt;.
    :cvar OTHER:
    :cvar RESIN_BONDED_PAPER:
    :cvar RESIN_IMPREGNATED_PAPER:
    :cvar SOLID_PORCELAIN:
    """
    COMPOUND = "compound"
    OIL_IMPREGNATED_PAPER = "oilImpregnatedPaper"
    OTHER = "other"
    RESIN_BONDED_PAPER = "resinBondedPaper"
    RESIN_IMPREGNATED_PAPER = "resinImpregnatedPaper"
    SOLID_PORCELAIN = "solidPorcelain"


class CigrestandardEditionKind(Enum):
    """
    List of editions for CIGRE standards.
    """
    VALUE_2000 = "2000"
    NONE = "none"
    UNKNOWN = "unknown"


class CigrestandardKind(Enum):
    """
    List of CIGRE standards.

    :cvar TB_170: CIGRE Technical Brochure 170 Static Electrification in
        Power Transformers.
    """
    TB_170 = "TB 170"


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


class CloudKind(Enum):
    ALTO_CUMULUS = "altoCumulus"
    ALTO_STRATUS = "altoStratus"
    CIRRO_CUMULUS = "cirroCumulus"
    CIRRO_STRATUS = "cirroStratus"
    CIRRUS = "cirrus"
    CUMULO_NIMBUS = "cumuloNimbus"
    CUMULUS = "cumulus"
    NIMBO_STRATUS = "nimboStratus"
    OTHER = "other"
    STRATO_CUMULUS = "stratoCumulus"
    STRATUS = "stratus"
    TOWERING_CUMULUS = "toweringCumulus"


class ComDirectionKind(Enum):
    """
    Kind of communication direction.

    :cvar BI_DIRECTIONAL: Communication with the device is bi-
        directional.
    :cvar FROM_DEVICE: Communication is from device.
    :cvar TO_DEVICE: Communication is to device.
    """
    BI_DIRECTIONAL = "biDirectional"
    FROM_DEVICE = "fromDevice"
    TO_DEVICE = "toDevice"


class ComTechnologyKind(Enum):
    """
    Kind of communication technology.

    :cvar CELLULAR: Communicates using a public cellular radio network.
        A specific variant of 'rf'.
    :cvar ETHERNET: Communicates using one or more of a family of frame-
        based computer networking technologies conforming to the IEEE
        802.3 standard.
    :cvar HOME_PLUG: Communicates using power line communication
        technologies conforming to the standards established by the
        HomePlug Powerline Alliance. A specific variant of 'plc'.
    :cvar PAGER: Communicates using a public one-way or two-way radio-
        based paging network. A specific variant of 'rf'.
    :cvar PHONE: Communicates using a basic, wireline telephone system.
    :cvar PLC: Communicates using power line communication technologies.
    :cvar RF: Communicates using private or public radio-based
        technology.
    :cvar RF_MESH: Communicates using a mesh radio technology. A
        specific variant of 'rf'.
    :cvar ZIGBEE: Communicates using radio communication technologies
        conforming to the standards established by the ZigBee. A
        specific variant of 'rf'.
    """
    CELLULAR = "cellular"
    ETHERNET = "ethernet"
    HOME_PLUG = "homePlug"
    PAGER = "pager"
    PHONE = "phone"
    PLC = "plc"
    RF = "rf"
    RF_MESH = "rfMesh"
    ZIGBEE = "zigbee"


class CommodityKind(Enum):
    """
    Kind of commodity being measured.

    :cvar AIR:
    :cvar CARBON:
    :cvar CH4: Methane CH&lt;sub&gt;4&lt;/sub&gt;
    :cvar CO2: Carbon Dioxide CO&lt;sub&gt;2&lt;/sub&gt;
    :cvar COMMUNICATION: A measurement of the communication
        infrastructure itself.
    :cvar COOLING_FLUID: The cool fluid returns warmer than when it was
        sent. The heat conveyed may be metered.
    :cvar ELECTRICITY_PRIMARY_METERED: It is possible for a meter to be
        outfitted with an external VT and/or CT. The meter might not be
        aware of these devices, and the display not compensate for their
        presence. Ultimately, when these scalars are applied, the value
        that represents the service value is called the ï¿½primary
        meteredï¿½ value. The ï¿½indexï¿½ in sub-category 3 mirrors
        those of sub-category 0.
    :cvar ELECTRICITY_SECONDARY_METERED: All types of metered
        quantities. This type of reading comes from the meter and
        represents a ï¿½secondaryï¿½ metered value.
    :cvar HCH: Hexachlorocyclohexane HCH
    :cvar HEATING_FLUID: This fluid is likely in liquid form. It is not
        necessarily water or water based. The warm fluid returns cooler
        than when it was sent. The heat conveyed may be metered.
    :cvar INSULATIVE_GAS: (SF&lt;sub&gt;6&lt;/sub&gt; is found
        separately below.)
    :cvar INSULATIVE_OIL:
    :cvar INTERNET: Internet service
    :cvar NATURAL_GAS:
    :cvar NONE: Not Applicable
    :cvar NONPOTABLE_WATER: Reclaimed water ï¿½ possibly used for
        irrigation but not sufficiently treated to be considered safe
        for drinking.
    :cvar NOX: Nitrous Oxides NO&lt;sub&gt;X&lt;/sub&gt;
    :cvar PFC: Perfluorocarbons PFC
    :cvar POTABLE_WATER: Drinkable water
    :cvar PROPANE:
    :cvar REFUSE: trash
    :cvar SF6: Sulfurhexafluoride SF&lt;sub&gt;6&lt;/sub&gt;
    :cvar SO2: Sulfur Dioxide SO&lt;sub&gt;2&lt;/sub&gt;
    :cvar STEAM: Water in steam form, usually used for heating.
    :cvar TV_LICENCE: Television
    :cvar WASTE_WATER: (Sewerage)
    """
    AIR = "air"
    CARBON = "carbon"
    CH4 = "ch4"
    CO2 = "co2"
    COMMUNICATION = "communication"
    COOLING_FLUID = "coolingFluid"
    ELECTRICITY_PRIMARY_METERED = "electricityPrimaryMetered"
    ELECTRICITY_SECONDARY_METERED = "electricitySecondaryMetered"
    HCH = "hch"
    HEATING_FLUID = "heatingFluid"
    INSULATIVE_GAS = "insulativeGas"
    INSULATIVE_OIL = "insulativeOil"
    INTERNET = "internet"
    NATURAL_GAS = "naturalGas"
    NONE = "none"
    NONPOTABLE_WATER = "nonpotableWater"
    NOX = "nox"
    PFC = "pfc"
    POTABLE_WATER = "potableWater"
    PROPANE = "propane"
    REFUSE = "refuse"
    SF6 = "sf6"
    SO2 = "so2"
    STEAM = "steam"
    TV_LICENCE = "tvLicence"
    WASTE_WATER = "wasteWater"


@dataclass
class ControlledAppliance:
    """
    Appliance controlled with a PAN device control.

    :ivar is_electric_vehicle: True if the appliance is an electric
        vehicle.
    :ivar is_exterior_lighting: True if the appliance is exterior
        lighting.
    :ivar is_generation_system: True if the appliance is a generation
        system.
    :ivar is_hvac_compressor_or_furnace: True if the appliance is HVAC
        compressor or furnace.
    :ivar is_interior_lighting: True if the appliance is interior
        lighting.
    :ivar is_irrigation_pump: True if the appliance is an irrigation
        pump.
    :ivar is_managed_commercial_industrial_load: True if the appliance
        is managed commercial or industrial load.
    :ivar is_pool_pump_spa_jacuzzi: True if the appliance is a pool,
        pump, spa or jacuzzi.
    :ivar is_simple_misc_load: True if the appliance is a simple
        miscellaneous load.
    :ivar is_smart_appliance: True if the appliance is a smart
        appliance.
    :ivar is_strip_and_baseboard_heater: True if the appliance is a stip
        or baseboard heater.
    :ivar is_water_heater: True if the appliance is a water heater.
    """
    is_electric_vehicle: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isElectricVehicle",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_exterior_lighting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isExteriorLighting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_generation_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isGenerationSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_hvac_compressor_or_furnace: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isHvacCompressorOrFurnace",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_interior_lighting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isInteriorLighting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_irrigation_pump: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isIrrigationPump",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_managed_commercial_industrial_load: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isManagedCommercialIndustrialLoad",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_pool_pump_spa_jacuzzi: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPoolPumpSpaJacuzzi",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_simple_misc_load: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSimpleMiscLoad",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_smart_appliance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSmartAppliance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_strip_and_baseboard_heater: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isStripAndBaseboardHeater",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_water_heater: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isWaterHeater",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class CorporateStandardKind(Enum):
    """
    Kind of corporate standard.

    :cvar EXPERIMENTAL: Asset model is used experimentally.
    :cvar OTHER: Other kind of corporate standard for the asset model.
    :cvar STANDARD: Asset model is used as corporate standard.
    :cvar UNDER_EVALUATION: Asset model usage is under evaluation.
    """
    EXPERIMENTAL = "experimental"
    OTHER = "other"
    STANDARD = "standard"
    UNDER_EVALUATION = "underEvaluation"


class CoverageCodeKind(Enum):
    """
    Kinds of weather condition coverage.
    """
    BRIEF = "brief"
    FREQUENT = "frequent"
    INTERMITTANT = "intermittant"
    ISOLATED = "isolated"
    NUMEROUS = "numerous"
    OCCASIONAL = "occasional"
    PARTLY = "partly"
    PATCHY = "patchy"
    PERIODS_OF = "periodsOf"
    SCATTERED = "scattered"
    WIDESPREAD = "widespread"


class CrewStatusKind(Enum):
    """
    the enumerated values for the dispatch status.

    :cvar ARRIVED: Indicates that one or more crews have arrived at the
        work site
    :cvar ASSIGNED: Indicates that one or more crews have been assigned
        to the work
    :cvar AWAITING_CREW_ASSIGNMENT: Indicates that the work is awaiting
        one or more crews to be assigned
    :cvar ENROUTE: Indicates that one or more crews are traveling to the
        work site(s)
    :cvar FIELD_COMPLETE: Indicates that the work at one or more work
        sites has been completed
    """
    ARRIVED = "arrived"
    ASSIGNED = "assigned"
    AWAITING_CREW_ASSIGNMENT = "awaitingCrewAssignment"
    ENROUTE = "enroute"
    FIELD_COMPLETE = "fieldComplete"


class Currency(Enum):
    """Monetary currencies.

    ISO 4217 standard including 3-character currency code.

    :cvar AED: United Arab Emirates dirham.
    :cvar AFN: Afghan afghani.
    :cvar ALL: Albanian lek.
    :cvar AMD: Armenian dram.
    :cvar ANG: Netherlands Antillean guilder.
    :cvar AOA: Angolan kwanza.
    :cvar ARS: Argentine peso.
    :cvar AUD: Australian dollar.
    :cvar AWG: Aruban florin.
    :cvar AZN: Azerbaijani manat.
    :cvar BAM: Bosnia and Herzegovina convertible mark.
    :cvar BBD: Barbados dollar.
    :cvar BDT: Bangladeshi taka.
    :cvar BGN: Bulgarian lev.
    :cvar BHD: Bahraini dinar.
    :cvar BIF: Burundian franc.
    :cvar BMD: Bermudian dollar (customarily known as Bermuda dollar).
    :cvar BND: Brunei dollar.
    :cvar BOB: Boliviano.
    :cvar BOV: Bolivian Mvdol (funds code).
    :cvar BRL: Brazilian real.
    :cvar BSD: Bahamian dollar.
    :cvar BTN: Bhutanese ngultrum.
    :cvar BWP: Botswana pula.
    :cvar BYR: Belarusian ruble.
    :cvar BZD: Belize dollar.
    :cvar CAD: Canadian dollar
    :cvar CDF: Congolese franc.
    :cvar CHF: Swiss franc.
    :cvar CLF: Unidad de Fomento (funds code), Chile.
    :cvar CLP: Chilean peso.
    :cvar CNY: Chinese yuan.
    :cvar COP: Colombian peso.
    :cvar COU: Unidad de Valor Real.
    :cvar CRC: Costa Rican colon.
    :cvar CUC: Cuban convertible peso.
    :cvar CUP: Cuban peso.
    :cvar CVE: Cape Verde escudo.
    :cvar CZK: Czech koruna.
    :cvar DJF: Djiboutian franc.
    :cvar DKK: Danish krone.
    :cvar DOP: Dominican peso.
    :cvar DZD: Algerian dinar.
    :cvar EEK: Estonian kroon.
    :cvar EGP: Egyptian pound.
    :cvar ERN: Eritrean nakfa.
    :cvar ETB: Ethiopian birr.
    :cvar EUR: Euro.
    :cvar FJD: Fiji dollar.
    :cvar FKP: Falkland Islands pound.
    :cvar GBP: Pound sterling.
    :cvar GEL: Georgian lari.
    :cvar GHS: Ghanaian cedi.
    :cvar GIP: Gibraltar pound.
    :cvar GMD: Gambian dalasi.
    :cvar GNF: Guinean franc.
    :cvar GTQ: Guatemalan quetzal.
    :cvar GYD: Guyanese dollar.
    :cvar HKD: Hong Kong dollar.
    :cvar HNL: Honduran lempira.
    :cvar HRK: Croatian kuna.
    :cvar HTG: Haitian gourde.
    :cvar HUF: Hungarian forint.
    :cvar IDR: Indonesian rupiah.
    :cvar ILS: Israeli new sheqel.
    :cvar INR: Indian rupee.
    :cvar IQD: Iraqi dinar.
    :cvar IRR: Iranian rial.
    :cvar ISK: Icelandic krï¿½na.
    :cvar JMD: Jamaican dollar.
    :cvar JOD: Jordanian dinar.
    :cvar JPY: Japanese yen.
    :cvar KES: Kenyan shilling.
    :cvar KGS: Kyrgyzstani som.
    :cvar KHR: Cambodian riel.
    :cvar KMF: Comoro franc.
    :cvar KPW: North Korean won.
    :cvar KRW: South Korean won.
    :cvar KWD: Kuwaiti dinar.
    :cvar KYD: Cayman Islands dollar.
    :cvar KZT: Kazakhstani tenge.
    :cvar LAK: Lao kip.
    :cvar LBP: Lebanese pound.
    :cvar LKR: Sri Lanka rupee.
    :cvar LRD: Liberian dollar.
    :cvar LSL: Lesotho loti.
    :cvar LTL: Lithuanian litas.
    :cvar LVL: Latvian lats.
    :cvar LYD: Libyan dinar.
    :cvar MAD: Moroccan dirham.
    :cvar MDL: Moldovan leu.
    :cvar MGA: Malagasy ariary.
    :cvar MKD: Macedonian denar.
    :cvar MMK: Myanma kyat.
    :cvar MNT: Mongolian tugrik.
    :cvar MOP: Macanese pataca.
    :cvar MRO: Mauritanian ouguiya.
    :cvar MUR: Mauritian rupee.
    :cvar MVR: Maldivian rufiyaa.
    :cvar MWK: Malawian kwacha.
    :cvar MXN: Mexican peso.
    :cvar MYR: Malaysian ringgit.
    :cvar MZN: Mozambican metical.
    :cvar NAD: Namibian dollar.
    :cvar NGN: Nigerian naira.
    :cvar NIO: Cordoba oro.
    :cvar NOK: Norwegian krone.
    :cvar NPR: Nepalese rupee.
    :cvar NZD: New Zealand dollar.
    :cvar OMR: Omani rial.
    :cvar PAB: Panamanian balboa.
    :cvar PEN: Peruvian nuevo sol.
    :cvar PGK: Papua New Guinean kina.
    :cvar PHP: Philippine peso.
    :cvar PKR: Pakistani rupee.
    :cvar PLN: Polish zloty.
    :cvar PYG: Paraguayan guaranï¿½.
    :cvar QAR: Qatari rial.
    :cvar RON: Romanian new leu.
    :cvar RSD: Serbian dinar.
    :cvar RUB: Russian rouble.
    :cvar RWF: Rwandan franc.
    :cvar SAR: Saudi riyal.
    :cvar SBD: Solomon Islands dollar.
    :cvar SCR: Seychelles rupee.
    :cvar SDG: Sudanese pound.
    :cvar SEK: Swedish krona/kronor.
    :cvar SGD: Singapore dollar.
    :cvar SHP: Saint Helena pound.
    :cvar SLL: Sierra Leonean leone.
    :cvar SOS: Somali shilling.
    :cvar SRD: Surinamese dollar.
    :cvar STD: Sï¿½o Tomï¿½ and Prï¿½ncipe dobra.
    :cvar SYP: Syrian pound.
    :cvar SZL: Lilangeni.
    :cvar THB: Thai baht.
    :cvar TJS: Tajikistani somoni.
    :cvar TMT: Turkmenistani manat.
    :cvar TND: Tunisian dinar.
    :cvar TOP: Tongan pa?anga.
    :cvar TRY: Turkish lira.
    :cvar TTD: Trinidad and Tobago dollar.
    :cvar TWD: New Taiwan dollar.
    :cvar TZS: Tanzanian shilling.
    :cvar UAH: Ukrainian hryvnia.
    :cvar UGX: Ugandan shilling.
    :cvar USD: United States dollar.
    :cvar UYU: Uruguayan peso.
    :cvar UZS: Uzbekistan som.
    :cvar VEF: Venezuelan bolï¿½var fuerte.
    :cvar VND: Vietnamese Dong.
    :cvar VUV: Vanuatu vatu.
    :cvar WST: Samoan tala.
    :cvar XAF: CFA franc BEAC.
    :cvar XCD: East Caribbean dollar.
    :cvar XOF: CFA Franc BCEAO.
    :cvar XPF: CFP franc.
    :cvar YER: Yemeni rial.
    :cvar ZAR: South African rand.
    :cvar ZMK: Zambian kwacha.
    :cvar ZWL: Zimbabwe dollar.
    """
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHF = "CHF"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EEK = "EEK"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    STD = "STD"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XCD = "XCD"
    XOF = "XOF"
    XPF = "XPF"
    YER = "YER"
    ZAR = "ZAR"
    ZMK = "ZMK"
    ZWL = "ZWL"


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y1value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y2value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y3value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    curve: Optional["Curve"] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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


class CustomerKind(Enum):
    """
    Kind of customer.

    :cvar COMMERCIAL_INDUSTRIAL: Commercial industrial customer.
    :cvar ENERGY_SERVICE_SCHEDULER: Customer as energy service
        scheduler.
    :cvar ENERGY_SERVICE_SUPPLIER: Customer as energy service supplier.
    :cvar ENTERPRISE:
    :cvar INTERNAL_USE: Internal use customer.
    :cvar OTHER: Other kind of customer.
    :cvar PUMPING_LOAD: Pumping load customer.
    :cvar REGIONAL_OPERATOR:
    :cvar RESIDENTIAL: Residential customer.
    :cvar RESIDENTIAL_AND_COMMERCIAL: Residential and commercial
        customer.
    :cvar RESIDENTIAL_AND_STREETLIGHT: Residential and streetlight
        customer.
    :cvar RESIDENTIAL_FARM_SERVICE: Residential farm service customer.
    :cvar RESIDENTIAL_STREETLIGHT_OTHERS: Residential streetlight or
        other related customer.
    :cvar SUBSIDIARY:
    :cvar WIND_MACHINE: Wind machine customer.
    """
    COMMERCIAL_INDUSTRIAL = "commercialIndustrial"
    ENERGY_SERVICE_SCHEDULER = "energyServiceScheduler"
    ENERGY_SERVICE_SUPPLIER = "energyServiceSupplier"
    ENTERPRISE = "enterprise"
    INTERNAL_USE = "internalUse"
    OTHER = "other"
    PUMPING_LOAD = "pumpingLoad"
    REGIONAL_OPERATOR = "regionalOperator"
    RESIDENTIAL = "residential"
    RESIDENTIAL_AND_COMMERCIAL = "residentialAndCommercial"
    RESIDENTIAL_AND_STREETLIGHT = "residentialAndStreetlight"
    RESIDENTIAL_FARM_SERVICE = "residentialFarmService"
    RESIDENTIAL_STREETLIGHT_OTHERS = "residentialStreetlightOthers"
    SUBSIDIARY = "subsidiary"
    WIND_MACHINE = "windMachine"


@dataclass
class Derfunction:
    class Meta:
        name = "DERFunction"

    connect_disconnect: Optional[bool] = field(
        default=None,
        metadata={
            "name": "connectDisconnect",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    frequency_watt_curve_function: Optional[bool] = field(
        default=None,
        metadata={
            "name": "frequencyWattCurveFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_real_power_limiting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "maxRealPowerLimiting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ramp_rate_control: Optional[bool] = field(
        default=None,
        metadata={
            "name": "rampRateControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reactive_power_dispatch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "reactivePowerDispatch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    real_power_dispatch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "realPowerDispatch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltage_regulation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "voltageRegulation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_curve_function: Optional[bool] = field(
        default=None,
        metadata={
            "name": "voltVarCurveFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_watt_curve_function: Optional[bool] = field(
        default=None,
        metadata={
            "name": "voltWattCurveFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_group: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :cvar AS: Ampere seconds (Aï¿½s).
    :cvar BTU: Energy, British Thermal Unit.
    :cvar HZ: Frequency in Hertz (1/s).
    :cvar Q: Quantity power, Q.
    :cvar QH: Quantity energy, Qh.
    :cvar V: Electric potential in Volt (W/A).
    :cvar VA: Apparent power in Volt Ampere (See also real power and
        reactive power.)
    :cvar VAH: Apparent energy in Volt Ampere hours.
    :cvar VAR: Reactive power in Volt Ampere reactive. The
        ï¿½reactiveï¿½ or ï¿½imaginaryï¿½ component of electrical power
        (VIsin(phi)). (See also real power and apparent power). Note:
        Different meter designs use different methods to arrive at their
        results. Some meters may compute reactive power as an arithmetic
        value, while others compute the value vectorially. The data
        consumer should determine the method in use and the suitability
        of the measurement for the intended purpose.
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
        (Iï¿½R or VIcos(phi)), is expressed in Watts. (See also apparent
        power and reactive power.)
    :cvar WPER_A: Active power per current flow, watt per Ampere.
    :cvar WPERS: Ramp rate in Watt per second.
    :cvar WH: Real energy in Watt hours.
    :cvar DEG: Plane angle in degrees.
    :cvar DEG_C: Relative temperature in degrees Celsius. In the SI unit
        system the symbol is ï¿½C. Electric charge is measured in
        coulomb that has the unit symbol C. To distinguish degree
        Celsius form coulomb the symbol used in the UML is degC. Reason
        for not using ï¿½C is the special character ï¿½ is difficult to
        manage in software.
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


class DinstandardEditionKind(Enum):
    """
    List of editions for DIN standards.
    """
    VALUE_1985 = "1985"
    NONE = "none"
    UNKNOWN = "unknown"


class DinstandardKind(Enum):
    """
    List of DIN standards.

    :cvar VALUE_51353: Testing of insulating oils; detection of
        corrosive sulfur; silver strip test.
    """
    VALUE_51353 = "51353"


@dataclass
class DateInterval:
    """
    Interval between two dates.
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class DecimalQuantity:
    pass


@dataclass
class DeploymentDate:
    """Dates for deployment events of an asset.

    May have multiple deployment type dates for this device and a
    compound type allows a query to return multiple dates.

    :ivar in_service_date: Date and time asset most recently put in
        service.
    :ivar installed_date: Date and time asset most recently installed.
    :ivar not_yet_installed_date: Date and time of asset deployment
        transition to not yet installed.
    :ivar out_of_service_date: Date and time asset most recently taken
        out of service.
    :ivar removed_date: Date and time asset most recently removed.
    """
    in_service_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "inServiceDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    installed_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "installedDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    not_yet_installed_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "notYetInstalledDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    out_of_service_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "outOfServiceDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    removed_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "removedDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class DeploymentStateKind(Enum):
    """
    Possible states of asset deployment.
    """
    IN_SERVICE = "inService"
    INSTALLED = "installed"
    NOT_YET_INSTALLED = "notYetInstalled"
    OUT_OF_SERVICE = "outOfService"
    REMOVED = "removed"


class DobleStandardEditionKind(Enum):
    """
    List of editions for Doble standards.
    """
    NONE = "none"
    UNKNOWN = "unknown"


class DobleStandardKind(Enum):
    """
    List of Doble standards.

    :cvar METHANOL: Doble test for methanol.
    """
    METHANOL = "methanol"


class EpastandardEditionKind(Enum):
    """
    List of editions for EPA standards.
    """
    A = "A"
    NONE = "none"
    UNKNOWN = "unknown"


class EpastandardKind(Enum):
    """
    List of EPA standards.

    :cvar VALUE_8082: Polychlorinated Biphenyls (PCBs) by Gas
        Chromatography.
    """
    VALUE_8082 = "8082"


@dataclass
class ElectronicAddress:
    """
    Electronic address information.

    :ivar email1: Primary email address.
    :ivar email2: Alternate email address.
    :ivar lan: Address on local area network.
    :ivar mac: MAC (Media Access Control) address.
    :ivar password: Password needed to log in.
    :ivar radio: Radio address.
    :ivar user_id: User ID needed to log in, which can be for an
        individual person, an organisation, a location, etc.
    :ivar web: World wide web address.
    """
    email1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    email2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lan: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    radio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "userID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    web: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class EmissionType(Enum):
    """
    The type of emission.

    :cvar CARBON_DIOXIDE: Carbon diaoxide.
    :cvar CARBON_DISULFIDE: Carbon disulfide.
    :cvar CHLORINE: Clorine.
    :cvar HYDROGEN_SULFIDE: Hydrogen sulfide.
    :cvar NITROGEN_OXIDE: Nitrogen oxide.
    :cvar SULFUR_DIOXIDE: Sulfer dioxide.
    """
    CARBON_DIOXIDE = "carbonDioxide"
    CARBON_DISULFIDE = "carbonDisulfide"
    CHLORINE = "chlorine"
    HYDROGEN_SULFIDE = "hydrogenSulfide"
    NITROGEN_OXIDE = "nitrogenOxide"
    SULFUR_DIOXIDE = "sulfurDioxide"


class EmissionValueSource(Enum):
    """
    The source of the emission value.

    :cvar CALCULATED: Calculated.
    :cvar MEASURED: Measured.
    """
    CALCULATED = "calculated"
    MEASURED = "measured"


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    duration_indefinite: Optional[bool] = field(
        default=None,
        metadata={
            "name": "durationIndefinite",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    start_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_control: Optional["EndDeviceControl"] = field(
        default=None,
        metadata={
            "name": "EndDeviceControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    communication: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    connect_disconnect: Optional[bool] = field(
        default=None,
        metadata={
            "name": "connectDisconnect",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    demand_response: Optional[bool] = field(
        default=None,
        metadata={
            "name": "demandResponse",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    electric_metering: Optional[bool] = field(
        default=None,
        metadata={
            "name": "electricMetering",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gas_metering: Optional[bool] = field(
        default=None,
        metadata={
            "name": "gasMetering",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    metrology: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    on_request_read: Optional[bool] = field(
        default=None,
        metadata={
            "name": "onRequestRead",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    outage_history: Optional[bool] = field(
        default=None,
        metadata={
            "name": "outageHistory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pressure_compensation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pressureCompensation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pricing_info: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pricingInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pulse_output: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pulseOutput",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    relays_programming: Optional[bool] = field(
        default=None,
        metadata={
            "name": "relaysProgramming",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reverse_flow: Optional[bool] = field(
        default=None,
        metadata={
            "name": "reverseFlow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    super_compressibility_compensation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "superCompressibilityCompensation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    temperature_compensation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "temperatureCompensation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    text_message: Optional[bool] = field(
        default=None,
        metadata={
            "name": "textMessage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    water_metering: Optional[bool] = field(
        default=None,
        metadata={
            "name": "waterMetering",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class EndDeviceFunctionKind(Enum):
    """
    Kind of end device function.

    :cvar AUTONOMOUS_DST: Autonomous application of daylight saving time
        (DST).
    :cvar DEMAND_RESPONSE: Demand response functions.
    :cvar ELECTRIC_METERING: Electricity metering.
    :cvar GAS_METERING: Gas metering.
    :cvar METROLOGY: Presentation of metered values to a user or another
        system (always a function of a meter, but might not be supported
        by a load control unit).
    :cvar ON_REQUEST_READ: On-request reads.
    :cvar OUTAGE_HISTORY: Reporting historical power interruption data.
    :cvar RELAYS_PROGRAMMING: Support for one or more relays that may be
        programmable in the meter (and tied to TOU, time pulse, load
        control or other functions).
    :cvar REVERSE_FLOW: Detection and monitoring of reverse flow.
    :cvar WATER_METERING: Water metering.
    """
    AUTONOMOUS_DST = "autonomousDst"
    DEMAND_RESPONSE = "demandResponse"
    ELECTRIC_METERING = "electricMetering"
    GAS_METERING = "gasMetering"
    METROLOGY = "metrology"
    ON_REQUEST_READ = "onRequestRead"
    OUTAGE_HISTORY = "outageHistory"
    RELAYS_PROGRAMMING = "relaysProgramming"
    REVERSE_FLOW = "reverseFlow"
    WATER_METERING = "waterMetering"


@dataclass
class ExtensionItem:
    ext_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "extName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ext_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "extType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ext_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "extValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class Fscale(Enum):
    """Fujita scale (referred to as EF-scale starting in 2007) for tornado
    damage.

    A set of wind estimates (not measurements) based on damage. It uses three-second gusts estimated at the point of damage based on a judgment of 8 levels of damage to 28 indicators. These estimates vary with height and exposure.
    Note: The 3 second gust is not the same wind as in standard surface observations.
    Enumerations based on NOAA conventions.

    :cvar FIVE: Over 200 mph 3-second gust.
    :cvar FOUR: 166-200 mph 3-second gust.
    :cvar MINUS_NINE: Unknown.
    :cvar ONE: 86-110 mph 3-second gust.
    :cvar THREE: 136-165 mph 3-second gust.
    :cvar TWO: 111-135 mph 3-second gust.
    :cvar ZERO: 65-85 mph 3-second gust.
    """
    FIVE = "five"
    FOUR = "four"
    MINUS_NINE = "minusNine"
    ONE = "one"
    THREE = "three"
    TWO = "two"
    ZERO = "zero"


class FacilityKind(Enum):
    """
    Types of facilities at which an asset can be deployed.
    """
    DISTRIBUTION_POLE_TOP = "distributionPoleTop"
    SUBSTATION_DISTRIBUTION = "substationDistribution"
    SUBSTATION_FOSSIL_PLANT = "substationFossilPlant"
    SUBSTATION_HYDRO_PLANT = "substationHydroPlant"
    SUBSTATION_NUCLEAR_PLANT = "substationNuclearPlant"
    SUBSTATION_SUB_TRANSMISSION = "substationSubTransmission"
    SUBSTATION_TRANSMISSION = "substationTransmission"


class FailureIsolationMethodKind(Enum):
    """
    How the failure has been isolated.
    """
    BREAKER_OPERATION = "breakerOperation"
    BURNED_IN_THE_CLEAR = "burnedInTheClear"
    FUSE = "fuse"
    MANUALLY_ISOLATED = "manuallyIsolated"
    OTHER = "other"


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r_line_to_line: Optional[float] = field(
        default=None,
        metadata={
            "name": "rLineToLine",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_ground: Optional[float] = field(
        default=None,
        metadata={
            "name": "xGround",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_line_to_line: Optional[float] = field(
        default=None,
        metadata={
            "name": "xLineToLine",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
        ï¿½laggingï¿½ describes a form of measurement where reactive
        power is considered in all four quadrants, but real power is
        considered only in quadrants I and IV. Note 2: When used to
        describe power factor, the term ï¿½Laggingï¿½ implies that the
        PF is negative. The term ï¿½laggingï¿½ in this case takes the
        place of the negative sign. If a signed PF value is to be passed
        by the data producer, then the direction of flow enumeration
        zero (none) should be used in order to avoid the possibility of
        creating an expression that employs a double negative. The data
        consumer should be able to tell from the sign of the data if the
        PF is leading or lagging. This principle is analogous to the
        concept that ï¿½Reverseï¿½ energy is an implied negative value,
        and to publish a negative reverse value would be ambiguous. Note
        3: Lagging power factors typically indicate inductive loading.
    :cvar LEADING: Typically used to describe that a power factor is
        leading the reference value. Note: Leading power factors
        typically indicate capacitive loading.
    :cvar NET: |Forward| - |Reverse|, See 61968-2. Note: In some
        systems, the value passed as a ï¿½netï¿½ value could become
        negative. In other systems the value passed as a ï¿½netï¿½ value
        is always a positive number, and rolls-over and rolls-under as
        needed.
    :cvar NONE: Not Applicable (N/A)
    :cvar Q1MINUS_Q4: Q1 minus Q4
    :cvar Q1PLUS_Q2: Reactive positive quadrants. (The term
        ï¿½laggingï¿½ is preferred.)
    :cvar Q1PLUS_Q3: Quadrants 1 and 3
    :cvar Q1PLUS_Q4: Quadrants 1 and 4 usually represent forward active
        energy
    :cvar Q2MINUS_Q3: Q2 minus Q3
    :cvar Q2PLUS_Q3: Quadrants 2 and 3 usually represent reverse active
        energy
    :cvar Q2PLUS_Q4: Quadrants 2 and 4
    :cvar Q3MINUS_Q2: Q3 minus Q2
    :cvar Q3PLUS_Q4: Reactive negative quadrants. (The term
        ï¿½leadingï¿½ is preferred.)
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
        the label ï¿½reverseï¿½ that it represents negative flow.
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
        for ï¿½Totalï¿½ and ï¿½Total by phaseï¿½ collapse to the same
        expression. For communication purposes however, the ï¿½Totalï¿½
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


class FuelType(Enum):
    """
    Type of fuel.

    :cvar COAL: Generic coal, not including lignite type.
    :cvar GAS: Natural gas.
    :cvar HARD_COAL: Hard coal
    :cvar LIGNITE: The fuel is lignite coal.  Note that this is a
        special type of coal, so the other enum of coal is reserved for
        hard coal types or if the exact type of coal is not known.
    :cvar OIL: Oil.
    :cvar OIL_SHALE: Oil Shale
    """
    COAL = "coal"
    GAS = "gas"
    HARD_COAL = "hardCoal"
    LIGNITE = "lignite"
    OIL = "oil"
    OIL_SHALE = "oilShale"


class GeosphericAnalogKind(Enum):
    """
    Kinds of analogs measuring a geospheric condition.

    :cvar LIGHTNING_DENSITY: Flash rate in
        strikes/hour/km&lt;sup&gt;2&lt;/sup&gt;.
    :cvar SEISMIC_EAST_WEST:
    :cvar SEISMIC_NORTH_SOUTH:
    :cvar SEISMIC_VERTICAL:
    :cvar SNOW_PACK_DEPTH:
    :cvar TEMPERATURE:
    """
    LIGHTNING_DENSITY = "lightningDensity"
    SEISMIC_EAST_WEST = "seismicEastWest"
    SEISMIC_NORTH_SOUTH = "seismicNorthSouth"
    SEISMIC_VERTICAL = "seismicVertical"
    SNOW_PACK_DEPTH = "snowPackDepth"
    TEMPERATURE = "temperature"


class HouseCooling(Enum):
    ELECTRIC = "electric"
    HEAT_PUMP = "heatPump"
    NONE = "none"


class HouseHeating(Enum):
    GAS = "gas"
    HEAT_PUMP = "heatPump"
    NONE = "none"
    RESISTANCE = "resistance"


class HydroEnergyConversionKind(Enum):
    """
    Specifies the capability of the hydro generating unit to convert energy as
    a generator or pump.

    :cvar GENERATOR: Able to generate power, but not able to pump water
        for energy storage.
    :cvar PUMP_AND_GENERATOR: Able to both generate power and pump water
        for energy storage.
    """
    GENERATOR = "generator"
    PUMP_AND_GENERATOR = "pumpAndGenerator"


class HydroPlantStorageKind(Enum):
    """
    The type of hydro power plant.

    :cvar PUMPED_STORAGE: Pumped storage.
    :cvar RUN_OF_RIVER: Run of river.
    :cvar STORAGE: Storage.
    """
    PUMPED_STORAGE = "pumpedStorage"
    RUN_OF_RIVER = "runOfRiver"
    STORAGE = "storage"


class HydrosphericAnalogKind(Enum):
    """
    Kinds of analogs measuring a hydrospheric condition.
    """
    FLOOD_LEVEL = "floodLevel"
    STORM_SURGE_HEIGHT = "stormSurgeHeight"
    SURFACE_TEMPERATURE = "surfaceTemperature"
    WATER_TEMPERATURE = "waterTemperature"
    WAVE_HEIGHT = "waveHeight"


@dataclass
class Iec61970Cimversion:
    """
    This is the IEC 61970 CIM version number assigned to this UML model.
    """
    class Meta:
        name = "IEC61970CIMVersion"


class IecstandardEditionKind(Enum):
    """
    List of editions for IEC standards.
    """
    VALUE_1963 = "1963"
    VALUE_1967 = "1967"
    VALUE_1973 = "1973"
    VALUE_1974 = "1974"
    VALUE_1977 = "1977"
    VALUE_1978 = "1978"
    VALUE_1979 = "1979"
    VALUE_1985 = "1985"
    VALUE_1989 = "1989"
    VALUE_1992 = "1992"
    VALUE_1992_AMD1_2004 = "1992/AMD1:2004"
    VALUE_1992_COR1_1992 = "1992/COR1:1992"
    VALUE_1993 = "1993"
    VALUE_1995 = "1995"
    VALUE_1997 = "1997"
    VALUE_1998 = "1998"
    VALUE_2004 = "2004"
    VALUE_2004_AMD1_2007 = "2004/AMD1:2007"
    VALUE_2004_AMD1_2007_CSV = "2004/AMD1:2007CSV"
    VALUE_2005 = "2005"
    VALUE_2007 = "2007"
    VALUE_2008 = "2008"
    VALUE_2010 = "2010"
    VALUE_2011 = "2011"
    VALUE_2012 = "2012"
    VALUE_2013 = "2013"
    VALUE_2013_COR_2013 = "2013/COR:2013"
    NONE = "none"
    UNKNOWN = "unknown"


class IecstandardKind(Enum):
    """
    List of IEC standards.

    :cvar VALUE_60156: Insulating liquids - Determination of the
        breakdown voltage at power frequency - Test method.
    :cvar VALUE_60243_1: Electric strength of insulating materials -
        Test methods - Part 1: Tests at power frequencies.
    :cvar VALUE_60243_2: Electric strength of insulating materials -
        Test methods - Part 2: Additional requirements for tests using
        direct voltage.
    :cvar VALUE_60243_3: Electric strength of insulating materials -
        Test methods - Part 3: Additional requirements for 1,2/50 ï¿½s
        impulse tests.
    :cvar VALUE_60247: Insulating liquids - Measurement of relative
        permittivity, dielectric dissipation factor (tan d) and d.c.
        resistivity  -or- Measurement of relative permittivity,
        dielectric dissipation factor and d.c. resistivity of insulating
        liquids  -or- Recommended test cells for measuring the
        resistivity of insulating liquids and methods of cleaning the
        cells.
    :cvar VALUE_60422: Mineral insulating oils in electrical equipment -
        Supervision and maintenance guidance.
    :cvar VALUE_60450: Measurement of the average viscometric degree of
        polymerization of new and aged cellulosic electrically
        insulating materials.
    :cvar VALUE_60567: Oil-filled electrical equipment - Sampling of
        gases and analysis of free and dissolved gasses - Guidance  -or-
        Oil-filled electrical equipment - Sampling of gases and of oil
        for analysis of free and dissolved gases - Guidance  -or- Guide
        for the sampling of gases and of oil form oil-filled electrical
        equipment and for the analysis of free and dissolved gases.
    :cvar VALUE_60666: Detection and determination of specified
        additives in mineral insulating oils  -or- Detection and
        determination of specified anti-oxidant additives in insulating
        oils.
    :cvar VALUE_60814: Insulating liquids - Oil-impregnated paper and
        pressboard - Determination of water by automatic coulometric
        Karl Fischer titration.
    :cvar VALUE_60970: Insulating liquids - Methods for counting and
        sizing particles  -or- Methods for counting and sizing particles
        in insulating liquids.
    :cvar VALUE_60997:
    :cvar VALUE_61125: Unused hydrocarbon based insulating liquids -
        Test methods for evaluating the oxidation stability.
    :cvar VALUE_61198: Mineral insulating oils - Methods for the
        determination of 2-furfural and related compounds.
    :cvar VALUE_61619: Insulating liquids - Contamination by
        polychlorinated biphenyls (PCBs) - Method of determination by
        capillary column gas chromatography.
    :cvar VALUE_61868: Mineral insulating oils ï¿½ Determination of
        kinematic viscosity at very low temperatures.
    :cvar VALUE_62535: Insulating liquids ï¿½ Test method for detection
        of potentially corrosive sulphur in used and unused insulating
        oil.
    :cvar VALUE_62697_1: Test methods for quantitative determination of
        corrosive sulfur compounds in unused and used insulating liquids
        - Part 1: Test method for quantitative determination of
        dibenzyldisulfide (DBDS).
    :cvar VALUE_62770: Fluids for electrotechnical applications ï¿½
        Unused natural esters for transformers and similar electrical
        equipment.
    """
    VALUE_60156 = "60156"
    VALUE_60243_1 = "60243-1"
    VALUE_60243_2 = "60243-2"
    VALUE_60243_3 = "60243-3"
    VALUE_60247 = "60247"
    VALUE_60422 = "60422"
    VALUE_60450 = "60450"
    VALUE_60567 = "60567"
    VALUE_60666 = "60666"
    VALUE_60814 = "60814"
    VALUE_60970 = "60970"
    VALUE_60997 = "60997"
    VALUE_61125 = "61125"
    VALUE_61198 = "61198"
    VALUE_61619 = "61619"
    VALUE_61868 = "61868"
    VALUE_62535 = "62535"
    VALUE_62697_1 = "62697-1"
    VALUE_62770 = "62770"


class Ieee1547AbnormalPerfomanceCategory(Enum):
    CATEGORY_I = "CategoryI"
    CATEGORY_II = "CategoryII"
    CATEGORY_III = "CategoryIII"


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    of1time: Optional[float] = field(
        default=None,
        metadata={
            "name": "OF1time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    of2frequency: Optional[object] = field(
        default=None,
        metadata={
            "name": "OF2frequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    of2time: Optional[float] = field(
        default=None,
        metadata={
            "name": "OF2time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ov1time: Optional[float] = field(
        default=None,
        metadata={
            "name": "OV1time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ov1voltage: Optional[object] = field(
        default=None,
        metadata={
            "name": "OV1voltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ov2time: Optional[float] = field(
        default=None,
        metadata={
            "name": "OV2time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ov2voltage: Optional[object] = field(
        default=None,
        metadata={
            "name": "OV2voltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    uf1frequency: Optional[object] = field(
        default=None,
        metadata={
            "name": "UF1frequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    uf1time: Optional[float] = field(
        default=None,
        metadata={
            "name": "UF1time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    uf2frequency: Optional[object] = field(
        default=None,
        metadata={
            "name": "UF2frequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    uf2time: Optional[float] = field(
        default=None,
        metadata={
            "name": "UF2time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    uv1time: Optional[float] = field(
        default=None,
        metadata={
            "name": "UV1time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    uv1voltage: Optional[object] = field(
        default=None,
        metadata={
            "name": "UV1voltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    uv2time: Optional[float] = field(
        default=None,
        metadata={
            "name": "UV2time",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    uv2voltage: Optional[object] = field(
        default=None,
        metadata={
            "name": "UV2voltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_electronics_connections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rotating_machines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "name": "RotatingMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class IeeestandardEditionKind(Enum):
    """
    List of editions for IEEE standards.
    """
    VALUE_1978 = "1978"
    VALUE_1995 = "1995"
    NONE = "none"
    UNKNOWN = "unknown"


class IeeestandardKind(Enum):
    """
    List of IEEE standards.

    :cvar VALUE_62: IEEE Guide for Diagnostic Field Testing of Electric
        Power Apparatus - Part 1: Oil Filled Power Transformers,
        Regulators, and Reactors -or- IEEE Guide for Field Testing Power
        Apparatus Insulation.
    """
    VALUE_62 = "62"


class IsostandardEditionKind(Enum):
    """
    List of editions for ISO standards.
    """
    VALUE_1973 = "1973"
    VALUE_1974 = "1974"
    VALUE_1976 = "1976"
    VALUE_1983 = "1983"
    VALUE_1985 = "1985"
    VALUE_1988 = "1988"
    VALUE_1992 = "1992"
    VALUE_1993 = "1993"
    VALUE_1994 = "1994"
    VALUE_1994_COR1_1997 = "1994/Cor1:1997"
    VALUE_1998 = "1998"
    VALUE_2000 = "2000"
    VALUE_2002 = "2002"
    VALUE_2005 = "2005"
    VALUE_2008 = "2008"
    NONE = "none"
    UNKNOWN = "unknown"


class IsostandardKind(Enum):
    """
    List of ISO standards.

    :cvar VALUE_1924: Paper and board -- Determination of tensile
        strength.
    :cvar VALUE_1924_1: Paper and board -- Determination of tensile
        properties -- Part 1: Constant rate of loading method.
    :cvar VALUE_1924_2: Paper and board -- Determination of tensile
        properties -- Part 2: Constant rate of elongation method (20
        mm/min)  -or- Paper and board -- Determination of tensile
        properties -- Part 2: Constant rate of elongation method.
    :cvar VALUE_1924_3: Paper and board -- Determination of tensile
        properties -- Part 3: Constant rate of elongation method (100
        mm/min).
    :cvar VALUE_2592: Determination of flash and fire points --
        Cleveland open cup method (copied directly from ASTM D92).
    :cvar VALUE_2719: Determination of flash point -- Pensky-Martens
        closed cup method (copied directly from ASTM D93)  -or-
        Petroleum products and lubricants -- Determination of flash
        point -- Pensky-Martens closed cup method (copied directly from
        ASTM D93)  -or- Petroleum products -- Determination of flash
        point -- Pensky-Martens closed cup method (copied directly from
        ASTM D93).
    :cvar VALUE_3016: Petroleum products -- Determination of pour point
        -or- Petroleum oils -- Determination of pour point.
    :cvar VALUE_3104: Petroleum products -- Transparent and opaque
        liquids -- Determination of kinematic viscosity and calculation
        of dynamic viscosity.
    :cvar VALUE_3675: Crude petroleum and liquid petroleum products --
        Laboratory determination of density -- Hydrometer method  -or-
        Crude petroleum and liquid petroleum products -- Laboratory
        determination of density or relative density -- Hydrometer
        method.
    """
    VALUE_1924 = "1924"
    VALUE_1924_1 = "1924-1"
    VALUE_1924_2 = "1924-2"
    VALUE_1924_3 = "1924-3"
    VALUE_2592 = "2592"
    VALUE_2719 = "2719"
    VALUE_3016 = "3016"
    VALUE_3104 = "3104"
    VALUE_3675 = "3675"


@dataclass
class InUseDate:
    """Dates associated with asset 'in use' status.

    May have multiple in use dates for this device and a compound type
    allows a query to return multiple dates.

    :ivar in_use_date: Date asset was most recently put in use.
    :ivar not_ready_for_use_date: Date of most recent asset transition
        to not ready for use state.
    :ivar ready_for_use_date: Date of most recent asset transition to
        ready for use state.
    """
    in_use_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "inUseDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    not_ready_for_use_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "notReadyForUseDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ready_for_use_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "readyForUseDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class IntensityCodeKind(Enum):
    """
    Kinds of weather condition intensity.
    """
    HEAVY = "heavy"
    LIGHT = "light"
    VERY_HEAVY = "veryHeavy"
    VERY_LIGHT = "veryLight"


class InterruptingMediumKind(Enum):
    AIR_BLAST = "airBlast"
    AIR_MAGNETIC = "airMagnetic"
    BULK_OIL = "bulkOil"
    GAS_SINGLE_PRESSURE = "gasSinglePressure"
    GAS_TWO_PRESSURE = "gasTwoPressure"
    MINIMUM_OIL = "minimumOil"
    VACUUM = "vacuum"


@dataclass
class IrregularTimePoint:
    """
    TimePoints for a schedule where the time between the points varies.

    :ivar time: The time is relative to the schedule starting time.
    :ivar value1: The first value at the time. The meaning of the value
        is defined by the derived type of the associated schedule.
    :ivar value2: The second value at the time. The meaning of the value
        is defined by the derived type of the associated schedule.
    :ivar interval_schedule: An IrregularTimePoint belongs to an
        IrregularIntervalSchedule.
    """
    time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    interval_schedule: Optional["IrregularIntervalSchedule"] = field(
        default=None,
        metadata={
            "name": "IntervalSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


class LaborelecStandardEditionKind(Enum):
    """
    List of editions for Laborelec standards.
    """
    NONE = "none"
    UNKNOWN = "unknown"


class LaborelecStandardKind(Enum):
    """
    List of Laborelec standards.

    :cvar METHANOL: Laborelec test for methanol.
    """
    METHANOL = "methanol"


@dataclass
class LifecycleDate:
    """Dates for asset lifecycle state changes.

    May have multiple lifecycle dates for this device and a compound
    type allows a query to return multiple dates.

    :ivar installation_date: Date current installation was completed,
        which may not be the same as the in-service date. Asset may have
        been installed at other locations previously. Ignored if asset
        is (1) not currently installed (e.g., stored in a depot) or (2)
        not intended to be installed (e.g., vehicle, tool).
    :ivar manufactured_date: Date the asset was manufactured.
    :ivar purchase_date: Date the asset was purchased. Note that even
        though an asset may have been purchased, it may not have been
        received into inventory at the time of purchase.
    :ivar received_date: Date the asset was received and first placed
        into inventory.
    :ivar removal_date: Date when the asset was last removed from
        service. Ignored if (1) not intended to be in service, or (2)
        currently in service.
    :ivar retired_date: Date the asset is permanently retired from
        service and may be scheduled for disposal. Ignored if asset is
        (1) currently in service, or (2) permanently removed from
        service.
    """
    installation_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "installationDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    manufactured_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "manufacturedDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    purchase_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "purchaseDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    received_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "receivedDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    removal_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "removalDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    retired_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "retiredDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class LocationKind(Enum):
    """
    :cvar CENTER: The center of a phenomenon. Will typically be used
        with a Location with a single PositionPoint instance.
    :cvar EXTENT: The area or line of a phenomenon, not the center. Will
        typically be used with a Location with multiple PositionPoint
        instances.
    :cvar PRIMARY: Primary area to which an environmental alert applies.
    :cvar SECONDARY: Secondary area to which an environmental alert
        applies.
    """
    CENTER = "center"
    EXTENT = "extent"
    PRIMARY = "primary"
    SECONDARY = "secondary"


class MacroPeriodKind(Enum):
    """
    Kind of macro period for calculations on read / measured values.

    :cvar BILLING_PERIOD: Captured during the billing period starting at
        midnight of the first day of the billing period (as defined by
        the billing cycle day). If during the current billing period, it
        specifies a period from the start of the current billing period
        until "now".
    :cvar DAILY: Daily period starting at midnight. If for the current
        day, this specifies the time from midnight to "now".
    :cvar MONTHLY: Monthly period starting at midnight on the first day
        of the month. If within the current month, this specifies the
        period from the start of the month until "now."
    :cvar NONE: Not applicable.
    :cvar SEASONAL: A season of time spanning multiple months. E.g.
        "Summer," "Spring," "Fall," and "Winter" based cycle. If within
        the current season, it specifies the period from the start of
        the current season until "now."
    :cvar SPECIFIED_PERIOD: For the period defined by the start and end
        of the TimePeriod element in the message.
    :cvar WEEKLY: Weekly period starting at midnight on the first day of
        the week and ending the instant before midnight the last day of
        the week. If within the current week, it specifies the period
        from the start of the week until "now."
    """
    BILLING_PERIOD = "billingPeriod"
    DAILY = "daily"
    MONTHLY = "monthly"
    NONE = "none"
    SEASONAL = "seasonal"
    SPECIFIED_PERIOD = "specifiedPeriod"
    WEEKLY = "weekly"


class MeasurementKind(Enum):
    """
    Kind of read / measured value.

    :cvar ALARM:
    :cvar AP_TITLE:
    :cvar APPARENT_POWER_FACTOR:
    :cvar APPLICATION_CONTEXT:
    :cvar ASSET_NUMBER:
    :cvar AUDIBLE_VOLUME: Sound
    :cvar BANDWIDTH:
    :cvar BATTERY_CARRYOVER:
    :cvar BATTERY_VOLTAGE:
    :cvar BILL_CARRYOVER: Customerï¿½s bill for the (Currency)
    :cvar BILL_LAST_PERIOD: Customerï¿½s bill for the previous billing
        period (Currency)
    :cvar BILL_TO_DATE: Customerï¿½s bill, as known thus far within the
        present billing period (Currency)
    :cvar BROADCAST_ADDRESS:
    :cvar CONNECTION_FEE: Monthly fee for connection to commodity.
    :cvar CURRENCY: funds
    :cvar CURRENT:
    :cvar CURRENT_ANGLE:
    :cvar CURRENT_IMBALANCE:
    :cvar DATA_OVERFLOW_ALARM:
    :cvar DATE:
    :cvar DEMAND:
    :cvar DEMAND_LIMIT:
    :cvar DEMAND_RESET: Usually expressed as a count as part of a
        billing cycle
    :cvar DEVICE_ADDRESS_TYPE1:
    :cvar DEVICE_ADDRESS_TYPE2:
    :cvar DEVICE_ADDRESS_TYPE3:
    :cvar DEVICE_ADDRESS_TYPE4:
    :cvar DEVICE_CLASS:
    :cvar DIAGNOSTIC:
    :cvar DISTANCE:
    :cvar DISTORTION_POWER_FACTOR:
    :cvar DISTORTION_VOLT_AMP:
    :cvar ELECTRONIC_SERIAL_NUMBER:
    :cvar EMERGENCY_LIMIT:
    :cvar ENCODER_TAMPER:
    :cvar END_DEVICE_ID:
    :cvar ENERGIZATION:
    :cvar ENERGIZATION_LOAD_SIDE:
    :cvar ENERGY:
    :cvar FAN:
    :cvar FREQUENCY:
    :cvar FREQUENCY_EXCURSION: Usually expressed as a ï¿½countï¿½
    :cvar FUND: Dup with ï¿½currencyï¿½
    :cvar GROUP_ADDRESS_TYPE1:
    :cvar GROUP_ADDRESS_TYPE2:
    :cvar GROUP_ADDRESS_TYPE3:
    :cvar GROUP_ADDRESS_TYPE4:
    :cvar IEEE1366_ASAI:
    :cvar IEEE1366_ASIDI:
    :cvar IEEE1366_ASIFI:
    :cvar IEEE1366_CAIDI:
    :cvar IEEE1366_CAIFI:
    :cvar IEEE1366_CEMIN:
    :cvar IEEE1366_CEMSMIN:
    :cvar IEEE1366_CTAIDI:
    :cvar IEEE1366_MAIFI:
    :cvar IEEE1366_MAIFIE:
    :cvar IEEE1366_MOMENTARY_INTERRUPTION:
    :cvar IEEE1366_MOMENTARY_INTERRUPTION_EVENT:
    :cvar IEEE1366_SAIDI:
    :cvar IEEE1366_SAIFI:
    :cvar IEEE1366_SUSTAINED_INTERRUPTION:
    :cvar INTERRUPTION_BEHAVIOUR:
    :cvar INVERSION_TAMPER:
    :cvar IP_ADDRESS:
    :cvar LINE_LOSS:
    :cvar LOAD_INTERRUPT:
    :cvar LOAD_SHED:
    :cvar LOSS:
    :cvar MAC_ADDRESS:
    :cvar MAINTENANCE:
    :cvar MFG_ASSIGNED_CONFIGURATION_ID:
    :cvar MFG_ASSIGNED_PHYSICAL_SERIAL_NUMBER:
    :cvar MFG_ASSIGNED_PRODUCT_NUMBER:
    :cvar MFG_ASSIGNED_UNIQUE_COMMUNICATION_ADDRESS:
    :cvar MULTI_CAST_ADDRESS:
    :cvar NEGATIVE_SEQUENCE:
    :cvar NONE: Not Applicable
    :cvar ONE_WAY_ADDRESS:
    :cvar PHASOR_POWER_FACTOR:
    :cvar PHASOR_REACTIVE_POWER:
    :cvar PHYSICAL_TAMPER:
    :cvar POSITIVE_SEQUENCE:
    :cvar POWER:
    :cvar POWER_FACTOR:
    :cvar POWER_LOSS_TAMPER:
    :cvar POWER_OUTAGE:
    :cvar POWER_QUALITY:
    :cvar POWER_RESTORATION:
    :cvar PROGRAMMED:
    :cvar PUSHBUTTON:
    :cvar QUANTITY_POWER:
    :cvar RELAY_ACTIVATION:
    :cvar RELAY_CYCLE: Usually expressed as a count
    :cvar REMOVAL_TAMPER:
    :cvar REPROGRAMMING_TAMPER:
    :cvar REVERSE_ROTATION_TAMPER:
    :cvar SAG: or Voltage Dip
    :cvar SIGNAL_STRENGTH:
    :cvar SIGNALTO_NOISE_RATIO: Moved here from Attribute #9 UOM
    :cvar SWELL:
    :cvar SWITCH_ARMED:
    :cvar SWITCH_DISABLED:
    :cvar SWITCH_POSITION:
    :cvar TAMPER:
    :cvar TAP_POSITION:
    :cvar TARIFF_RATE:
    :cvar TEMPERATURE:
    :cvar TOTAL_HARMONIC_DISTORTION:
    :cvar TRANSFORMER_LOSS:
    :cvar TWO_WAY_ADDRESS:
    :cvar UNIPEDE_VOLTAGE_DIP10TO15:
    :cvar UNIPEDE_VOLTAGE_DIP15TO30:
    :cvar UNIPEDE_VOLTAGE_DIP30TO60:
    :cvar UNIPEDE_VOLTAGE_DIP60TO90:
    :cvar UNIPEDE_VOLTAGE_DIP90TO100:
    :cvar VOLTAGE:
    :cvar VOLTAGE_ANGLE:
    :cvar VOLTAGE_EXCURSION:
    :cvar VOLTAGE_IMBALANCE:
    :cvar VOLUME: Clarified  from Ed. 1. to indicate fluid volume
    :cvar VOLUMETRIC_FLOW:
    :cvar WATCHDOG_TIMEOUT:
    :cvar ZERO_FLOW_DURATION:
    :cvar ZERO_SEQUENCE:
    """
    ALARM = "alarm"
    AP_TITLE = "apTitle"
    APPARENT_POWER_FACTOR = "apparentPowerFactor"
    APPLICATION_CONTEXT = "applicationContext"
    ASSET_NUMBER = "assetNumber"
    AUDIBLE_VOLUME = "audibleVolume"
    BANDWIDTH = "bandwidth"
    BATTERY_CARRYOVER = "batteryCarryover"
    BATTERY_VOLTAGE = "batteryVoltage"
    BILL_CARRYOVER = "billCarryover"
    BILL_LAST_PERIOD = "billLastPeriod"
    BILL_TO_DATE = "billToDate"
    BROADCAST_ADDRESS = "broadcastAddress"
    CONNECTION_FEE = "connectionFee"
    CURRENCY = "currency"
    CURRENT = "current"
    CURRENT_ANGLE = "currentAngle"
    CURRENT_IMBALANCE = "currentImbalance"
    DATA_OVERFLOW_ALARM = "dataOverflowAlarm"
    DATE = "date"
    DEMAND = "demand"
    DEMAND_LIMIT = "demandLimit"
    DEMAND_RESET = "demandReset"
    DEVICE_ADDRESS_TYPE1 = "deviceAddressType1"
    DEVICE_ADDRESS_TYPE2 = "deviceAddressType2"
    DEVICE_ADDRESS_TYPE3 = "deviceAddressType3"
    DEVICE_ADDRESS_TYPE4 = "deviceAddressType4"
    DEVICE_CLASS = "deviceClass"
    DIAGNOSTIC = "diagnostic"
    DISTANCE = "distance"
    DISTORTION_POWER_FACTOR = "distortionPowerFactor"
    DISTORTION_VOLT_AMP = "distortionVoltAmp"
    ELECTRONIC_SERIAL_NUMBER = "electronicSerialNumber"
    EMERGENCY_LIMIT = "emergencyLimit"
    ENCODER_TAMPER = "encoderTamper"
    END_DEVICE_ID = "endDeviceID"
    ENERGIZATION = "energization"
    ENERGIZATION_LOAD_SIDE = "energizationLoadSide"
    ENERGY = "energy"
    FAN = "fan"
    FREQUENCY = "frequency"
    FREQUENCY_EXCURSION = "frequencyExcursion"
    FUND = "fund"
    GROUP_ADDRESS_TYPE1 = "groupAddressType1"
    GROUP_ADDRESS_TYPE2 = "groupAddressType2"
    GROUP_ADDRESS_TYPE3 = "groupAddressType3"
    GROUP_ADDRESS_TYPE4 = "groupAddressType4"
    IEEE1366_ASAI = "ieee1366ASAI"
    IEEE1366_ASIDI = "ieee1366ASIDI"
    IEEE1366_ASIFI = "ieee1366ASIFI"
    IEEE1366_CAIDI = "ieee1366CAIDI"
    IEEE1366_CAIFI = "ieee1366CAIFI"
    IEEE1366_CEMIN = "ieee1366CEMIn"
    IEEE1366_CEMSMIN = "ieee1366CEMSMIn"
    IEEE1366_CTAIDI = "ieee1366CTAIDI"
    IEEE1366_MAIFI = "ieee1366MAIFI"
    IEEE1366_MAIFIE = "ieee1366MAIFIe"
    IEEE1366_MOMENTARY_INTERRUPTION = "ieee1366MomentaryInterruption"
    IEEE1366_MOMENTARY_INTERRUPTION_EVENT = "ieee1366MomentaryInterruptionEvent"
    IEEE1366_SAIDI = "ieee1366SAIDI"
    IEEE1366_SAIFI = "ieee1366SAIFI"
    IEEE1366_SUSTAINED_INTERRUPTION = "ieee1366SustainedInterruption"
    INTERRUPTION_BEHAVIOUR = "interruptionBehaviour"
    INVERSION_TAMPER = "inversionTamper"
    IP_ADDRESS = "ipAddress"
    LINE_LOSS = "lineLoss"
    LOAD_INTERRUPT = "loadInterrupt"
    LOAD_SHED = "loadShed"
    LOSS = "loss"
    MAC_ADDRESS = "macAddress"
    MAINTENANCE = "maintenance"
    MFG_ASSIGNED_CONFIGURATION_ID = "mfgAssignedConfigurationID"
    MFG_ASSIGNED_PHYSICAL_SERIAL_NUMBER = "mfgAssignedPhysicalSerialNumber"
    MFG_ASSIGNED_PRODUCT_NUMBER = "mfgAssignedProductNumber"
    MFG_ASSIGNED_UNIQUE_COMMUNICATION_ADDRESS = "mfgAssignedUniqueCommunicationAddress"
    MULTI_CAST_ADDRESS = "multiCastAddress"
    NEGATIVE_SEQUENCE = "negativeSequence"
    NONE = "none"
    ONE_WAY_ADDRESS = "oneWayAddress"
    PHASOR_POWER_FACTOR = "phasorPowerFactor"
    PHASOR_REACTIVE_POWER = "phasorReactivePower"
    PHYSICAL_TAMPER = "physicalTamper"
    POSITIVE_SEQUENCE = "positiveSequence"
    POWER = "power"
    POWER_FACTOR = "powerFactor"
    POWER_LOSS_TAMPER = "powerLossTamper"
    POWER_OUTAGE = "powerOutage"
    POWER_QUALITY = "powerQuality"
    POWER_RESTORATION = "powerRestoration"
    PROGRAMMED = "programmed"
    PUSHBUTTON = "pushbutton"
    QUANTITY_POWER = "quantityPower"
    RELAY_ACTIVATION = "relayActivation"
    RELAY_CYCLE = "relayCycle"
    REMOVAL_TAMPER = "removalTamper"
    REPROGRAMMING_TAMPER = "reprogrammingTamper"
    REVERSE_ROTATION_TAMPER = "reverseRotationTamper"
    SAG = "sag"
    SIGNAL_STRENGTH = "signalStrength"
    SIGNALTO_NOISE_RATIO = "signaltoNoiseRatio"
    SWELL = "swell"
    SWITCH_ARMED = "switchArmed"
    SWITCH_DISABLED = "switchDisabled"
    SWITCH_POSITION = "switchPosition"
    TAMPER = "tamper"
    TAP_POSITION = "tapPosition"
    TARIFF_RATE = "tariffRate"
    TEMPERATURE = "temperature"
    TOTAL_HARMONIC_DISTORTION = "totalHarmonicDistortion"
    TRANSFORMER_LOSS = "transformerLoss"
    TWO_WAY_ADDRESS = "twoWayAddress"
    UNIPEDE_VOLTAGE_DIP10TO15 = "unipedeVoltageDip10to15"
    UNIPEDE_VOLTAGE_DIP15TO30 = "unipedeVoltageDip15to30"
    UNIPEDE_VOLTAGE_DIP30TO60 = "unipedeVoltageDip30to60"
    UNIPEDE_VOLTAGE_DIP60TO90 = "unipedeVoltageDip60to90"
    UNIPEDE_VOLTAGE_DIP90TO100 = "unipedeVoltageDip90to100"
    VOLTAGE = "voltage"
    VOLTAGE_ANGLE = "voltageAngle"
    VOLTAGE_EXCURSION = "voltageExcursion"
    VOLTAGE_IMBALANCE = "voltageImbalance"
    VOLUME = "volume"
    VOLUMETRIC_FLOW = "volumetricFlow"
    WATCHDOG_TIMEOUT = "watchdogTimeout"
    ZERO_FLOW_DURATION = "zeroFlowDuration"
    ZERO_SEQUENCE = "zeroSequence"


class MeasuringPeriodKind(Enum):
    """
    Kind of period for reading / measuring values.

    :cvar FIFTEEN_MINUTE: 15-minute
    :cvar FIVE_MINUTE: 5-minute
    :cvar FIXED_BLOCK10_MIN: 10-minute Fixed Block
    :cvar FIXED_BLOCK15_MIN: 15-minute Fixed Block
    :cvar FIXED_BLOCK1_MIN: 1-minute Fixed Block
    :cvar FIXED_BLOCK20_MIN: 20-minute Fixed Block
    :cvar FIXED_BLOCK30_MIN: 30-minute Fixed Block
    :cvar FIXED_BLOCK5_MIN: 5-minute Fixed Block
    :cvar FIXED_BLOCK60_MIN: 60-minute Fixed Block
    :cvar NONE: Not applicable.
    :cvar ONE_MINUTE: 1-minute
    :cvar PRESENT: Within the present period of time
    :cvar PREVIOUS: Shifted within the previous monthly cycle and data
        set
    :cvar ROLLING_BLOCK10_MIN_INTVL1_MIN_SUB_INTVL: 10-minute Rolling
        Block with 1-minute sub-intervals
    :cvar ROLLING_BLOCK10_MIN_INTVL2_MIN_SUB_INTVL: 10-minute Rolling
        Block with 2-minute sub-intervals
    :cvar ROLLING_BLOCK10_MIN_INTVL5_MIN_SUB_INTVL: 10-minute Rolling
        Block with 5-minute sub-intervals
    :cvar ROLLING_BLOCK15_MIN_INTVL1_MIN_SUB_INTVL: 15-minute Rolling
        Block with 1-minute sub-intervals
    :cvar ROLLING_BLOCK15_MIN_INTVL3_MIN_SUB_INTVL: 15-minute Rolling
        Block with 3-minute sub-intervals
    :cvar ROLLING_BLOCK15_MIN_INTVL5_MIN_SUB_INTVL: 15-minute Rolling
        Block with 5-minute sub-intervals
    :cvar ROLLING_BLOCK30_MIN_INTVL10_MIN_SUB_INTVL: 30-minute Rolling
        Block with 10-minute sub-intervals
    :cvar ROLLING_BLOCK30_MIN_INTVL15_MIN_SUB_INTVL: 30-minute Rolling
        Block with 15-minute sub-intervals
    :cvar ROLLING_BLOCK30_MIN_INTVL2_MIN_SUB_INTVL: 30-minute Rolling
        Block with 2-minute sub-intervals
    :cvar ROLLING_BLOCK30_MIN_INTVL3_MIN_SUB_INTVL: 30-minute Rolling
        Block with 3-minute sub-intervals
    :cvar ROLLING_BLOCK30_MIN_INTVL5_MIN_SUB_INTVL: 30-minute Rolling
        Block with 5-minute sub-intervals.
    :cvar ROLLING_BLOCK30_MIN_INTVL6_MIN_SUB_INTVL: 30-minute Rolling
        Block with 6-minute sub-intervals
    :cvar ROLLING_BLOCK5_MIN_INTVL1_MIN_SUB_INTVL: 5-minute Rolling
        Block with 1-minute sub-intervals
    :cvar ROLLING_BLOCK60_MIN_INTVL10_MIN_SUB_INTVL: 60-minute Rolling
        Block with 10-minute sub-intervals
    :cvar ROLLING_BLOCK60_MIN_INTVL12_MIN_SUB_INTVL: 60-minute Rolling
        Block with 12-minute sub-intervals
    :cvar ROLLING_BLOCK60_MIN_INTVL15_MIN_SUB_INTVL: 60-minute Rolling
        Block with 15-minute sub-intervals
    :cvar ROLLING_BLOCK60_MIN_INTVL20_MIN_SUB_INTVL: 60-minute Rolling
        Block with 20-minute sub-intervals
    :cvar ROLLING_BLOCK60_MIN_INTVL30_MIN_SUB_INTVL: 60-minute Rolling
        Block with 30-minute sub-intervals
    :cvar ROLLING_BLOCK60_MIN_INTVL4_MIN_SUB_INTVL: 60-minute Rolling
        Block with 4-minute sub-intervals
    :cvar ROLLING_BLOCK60_MIN_INTVL5_MIN_SUB_INTVL: 60-minute Rolling
        Block with 5-minute sub-intervals
    :cvar ROLLING_BLOCK60_MIN_INTVL6_MIN_SUB_INTVL: 60-minute Rolling
        Block with 6-minute sub-intervals
    :cvar SIXTY_MINUTE: 60-minute
    :cvar TEN_MINUTE: 10-minute
    :cvar THIRTY_MINUTE: 30-minute
    :cvar THREE_MINUTE: 3-minute
    :cvar TWENTY_MINUTE: 20-minute interval
    :cvar TWENTYFOUR_HOUR: 24-hour
    :cvar TWO_MINUTE: 2-minute
    """
    FIFTEEN_MINUTE = "fifteenMinute"
    FIVE_MINUTE = "fiveMinute"
    FIXED_BLOCK10_MIN = "fixedBlock10Min"
    FIXED_BLOCK15_MIN = "fixedBlock15Min"
    FIXED_BLOCK1_MIN = "fixedBlock1Min"
    FIXED_BLOCK20_MIN = "fixedBlock20Min"
    FIXED_BLOCK30_MIN = "fixedBlock30Min"
    FIXED_BLOCK5_MIN = "fixedBlock5Min"
    FIXED_BLOCK60_MIN = "fixedBlock60Min"
    NONE = "none"
    ONE_MINUTE = "oneMinute"
    PRESENT = "present"
    PREVIOUS = "previous"
    ROLLING_BLOCK10_MIN_INTVL1_MIN_SUB_INTVL = "rollingBlock10MinIntvl1MinSubIntvl"
    ROLLING_BLOCK10_MIN_INTVL2_MIN_SUB_INTVL = "rollingBlock10MinIntvl2MinSubIntvl"
    ROLLING_BLOCK10_MIN_INTVL5_MIN_SUB_INTVL = "rollingBlock10MinIntvl5MinSubIntvl"
    ROLLING_BLOCK15_MIN_INTVL1_MIN_SUB_INTVL = "rollingBlock15MinIntvl1MinSubIntvl"
    ROLLING_BLOCK15_MIN_INTVL3_MIN_SUB_INTVL = "rollingBlock15MinIntvl3MinSubIntvl"
    ROLLING_BLOCK15_MIN_INTVL5_MIN_SUB_INTVL = "rollingBlock15MinIntvl5MinSubIntvl"
    ROLLING_BLOCK30_MIN_INTVL10_MIN_SUB_INTVL = "rollingBlock30MinIntvl10MinSubIntvl"
    ROLLING_BLOCK30_MIN_INTVL15_MIN_SUB_INTVL = "rollingBlock30MinIntvl15MinSubIntvl"
    ROLLING_BLOCK30_MIN_INTVL2_MIN_SUB_INTVL = "rollingBlock30MinIntvl2MinSubIntvl"
    ROLLING_BLOCK30_MIN_INTVL3_MIN_SUB_INTVL = "rollingBlock30MinIntvl3MinSubIntvl"
    ROLLING_BLOCK30_MIN_INTVL5_MIN_SUB_INTVL = "rollingBlock30MinIntvl5MinSubIntvl"
    ROLLING_BLOCK30_MIN_INTVL6_MIN_SUB_INTVL = "rollingBlock30MinIntvl6MinSubIntvl"
    ROLLING_BLOCK5_MIN_INTVL1_MIN_SUB_INTVL = "rollingBlock5MinIntvl1MinSubIntvl"
    ROLLING_BLOCK60_MIN_INTVL10_MIN_SUB_INTVL = "rollingBlock60MinIntvl10MinSubIntvl"
    ROLLING_BLOCK60_MIN_INTVL12_MIN_SUB_INTVL = "rollingBlock60MinIntvl12MinSubIntvl"
    ROLLING_BLOCK60_MIN_INTVL15_MIN_SUB_INTVL = "rollingBlock60MinIntvl15MinSubIntvl"
    ROLLING_BLOCK60_MIN_INTVL20_MIN_SUB_INTVL = "rollingBlock60MinIntvl20MinSubIntvl"
    ROLLING_BLOCK60_MIN_INTVL30_MIN_SUB_INTVL = "rollingBlock60MinIntvl30MinSubIntvl"
    ROLLING_BLOCK60_MIN_INTVL4_MIN_SUB_INTVL = "rollingBlock60MinIntvl4MinSubIntvl"
    ROLLING_BLOCK60_MIN_INTVL5_MIN_SUB_INTVL = "rollingBlock60MinIntvl5MinSubIntvl"
    ROLLING_BLOCK60_MIN_INTVL6_MIN_SUB_INTVL = "rollingBlock60MinIntvl6MinSubIntvl"
    SIXTY_MINUTE = "sixtyMinute"
    TEN_MINUTE = "tenMinute"
    THIRTY_MINUTE = "thirtyMinute"
    THREE_MINUTE = "threeMinute"
    TWENTY_MINUTE = "twentyMinute"
    TWENTYFOUR_HOUR = "twentyfourHour"
    TWO_MINUTE = "twoMinute"


class MediumKind(Enum):
    """
    Kind of medium.
    """
    SF6 = "SF6"
    SF6_CF4 = "SF6CF4"
    SF6_N2 = "SF6N2"
    AIR = "air"
    GAS = "gas"
    LIQUID = "liquid"
    MINERAL_OIL = "mineralOil"
    SOLID = "solid"


class MeterMultiplierKind(Enum):
    """
    Kind of meter multiplier.

    :cvar CT_RATIO: Current transformer ratio used to convert associated
        quantities to real measurements.
    :cvar K_E: Test constant.
    :cvar K_H: Meter kh (watthour) constant. The number of watthours
        that must be applied to the meter to cause one disk revolution
        for an electromechanical meter or the number of watthours
        represented by one increment pulse for an electronic meter.
    :cvar K_R: Register multiplier. The number to multiply the register
        reading by in order to get kWh.
    :cvar PT_RATIO: Potential transformer ratio used to convert
        associated quantities to real measurements.
    :cvar TRANSFORMER_RATIO: Product of the CT ratio and PT ratio.
    """
    CT_RATIO = "ctRatio"
    K_E = "kE"
    K_H = "kH"
    K_R = "kR"
    PT_RATIO = "ptRatio"
    TRANSFORMER_RATIO = "transformerRatio"


@dataclass
class MeterWorkTask:
    """
    Work task involving meters.

    :ivar meter: Meter on which this non-replacement work task is
        performed.
    :ivar old_meter: Old meter replaced by this work task.
    :ivar usage_point: Usage point to which this meter service work task
        applies.
    """
    meter: Optional["Meter"] = field(
        default=None,
        metadata={
            "name": "Meter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    old_meter: Optional["Meter"] = field(
        default=None,
        metadata={
            "name": "OldMeter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_point: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "name": "UsagePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class MonthDayInterval:
    """
    Interval between two times specified as mont and date.
    """


@dataclass
class NameTypeAuthority:
    """
    Authority responsible for creation and management of names of a given type;
    typically an organization or an enterprise system.

    :ivar description: Description of the name type authority.
    :ivar name: Name of the name type authority.
    :ivar name_types: All name types managed by this authority.
    """
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    name_types: List["NameType"] = field(
        default_factory=list,
        metadata={
            "name": "NameTypes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class NonlinearShuntCompensatorPhasePoint:
    """
    A per phase non linear shunt compensator bank or section admittance value.

    :ivar b: Positive sequence shunt (charging) susceptance per section
    :ivar g: Positive sequence shunt (charging) conductance per section
    :ivar section_number: The number of the section.
    :ivar nonlinear_shunt_compensator_phase:
    """
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    section_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sectionNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nonlinear_shunt_compensator_phase: Optional["NonlinearShuntCompensatorPhase"] = field(
        default=None,
        metadata={
            "name": "NonlinearShuntCompensatorPhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class NonlinearShuntCompensatorPoint:
    """
    A non linear shunt compensator bank or section admittance value.

    :ivar b: Positive sequence shunt (charging) susceptance per section
    :ivar b0: Zero sequence shunt (charging) susceptance per section
    :ivar g: Positive sequence shunt (charging) conductance per section
    :ivar g0: Zero sequence shunt (charging) conductance per section
    :ivar section_number: The number of the section.
    :ivar nonlinear_shunt_compensator:
    """
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    b0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    section_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sectionNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nonlinear_shunt_compensator: Optional["NonlinearShuntCompensator"] = field(
        default=None,
        metadata={
            "name": "NonlinearShuntCompensator",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


class NotificationTriggerKind(Enum):
    """
    Kind of trigger to notify customer.

    :cvar ETR_CHANGE: Notify customer if estimated restoration time
        changes.
    :cvar INFORM_DISPATCHED: Notify customer that a crew has been
        dispatched to investigate the problem.
    :cvar INITIAL_ETR: Notify customer for the first time that estimated
        restoration time is available.
    :cvar POWER_OUT: Notify customer of planned outage.
    :cvar POWER_RESTORED: Notify customer when power has been restored.
    """
    ETR_CHANGE = "etrChange"
    INFORM_DISPATCHED = "informDispatched"
    INITIAL_ETR = "initialEtr"
    POWER_OUT = "powerOut"
    POWER_RESTORED = "powerRestored"


class OilSampleLocation(Enum):
    OIL_DRAINAGE_DEVICE = "oilDrainageDevice"
    OIL_SAMPLE_VALVE = "oilSampleValve"
    OTHER = "other"


class OilTemperatureSource(Enum):
    INFRARED_GUN = "infraredGun"
    OTHER = "other"
    TOP_OIL_TEMPERATURE_GAUGE = "topOilTemperatureGauge"


class OperatingMechanismKind(Enum):
    CAPACITOR_TRIP = "capacitorTrip"
    HYDRAULIC = "hydraulic"
    PNEUDRAULIC = "pneudraulic"
    PNEUMATIC = "pneumatic"
    SOLENOID = "solenoid"
    SPRING = "spring"
    SPRING_HAND_CRANK = "springHandCrank"
    SPRING_HYDRAULIC = "springHydraulic"
    SPRING_MOTOR = "springMotor"


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


@dataclass
class OverfrequencyTripCurveData:
    f: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    t: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OvervoltageTripCurveData:
    t: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    v: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class PnnltroubleCallKind(Enum):
    LINE_DOWN = "lineDown"
    POWER_ON = "powerOn"
    POWER_OUT = "powerOut"


@dataclass
class PanPricingDetail:
    """
    Detail for a single price command/action.

    :ivar alternate_cost_delivered: Alternative measure of the cost of
        the energy consumed. An example might be the emissions of CO2
        for each kWh of electricity consumed providing a measure of the
        environmental cost.
    :ivar alternate_cost_unit: Cost unit for the alternate cost
        delivered field. One example is kg of CO2 per unit of measure.
    :ivar current_time_date: Current time as determined by a PAN device.
    :ivar generation_price: Price of the commodity measured in base unit
        of currency per 'unitOfMeasure'.
    :ivar generation_price_ratio: Ratio of 'generationPrice' to the
        "normal" price chosen by the commodity provider.
    :ivar price: Price of the commodity measured in base unit of
        currency per 'unitOfMeasure'.
    :ivar price_ratio: Ratio of 'price' to the "normal" price chosen by
        the commodity provider.
    :ivar price_tier: Pricing tier as chosen by the commodity provider.
    :ivar price_tier_count: Maximum number of price tiers available.
    :ivar price_tier_label: Label for price tier.
    :ivar rate_label: Label of the current billing rate specified by
        commodity provider.
    :ivar register_tier: Register tier accumulating usage information.
    :ivar unit_of_measure: Defines commodity as well as its base unit of
        measure.
    :ivar pan_pricing: PAN pricing command/action issuing this price
        detail.
    """
    alternate_cost_delivered: Optional[float] = field(
        default=None,
        metadata={
            "name": "alternateCostDelivered",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    alternate_cost_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "alternateCostUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    current_time_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "currentTimeDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    generation_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "generationPrice",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    generation_price_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "generationPriceRatio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    price_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "priceRatio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    price_tier: Optional[int] = field(
        default=None,
        metadata={
            "name": "priceTier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    price_tier_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "priceTierCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    price_tier_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "priceTierLabel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rate_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "rateLabel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    register_tier: Optional[str] = field(
        default=None,
        metadata={
            "name": "registerTier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unit_of_measure: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitOfMeasure",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pan_pricing: Optional["PanPricing"] = field(
        default=None,
        metadata={
            "name": "PanPricing",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class PetersenCoilModeKind(Enum):
    """
    The mode of operation for a Petersen coil.

    :cvar AUTOMATIC_POSITIONING: Automatic positioning.
    :cvar FIXED: Fixed position.
    :cvar MANUAL: Manual positioning.
    """
    AUTOMATIC_POSITIONING = "automaticPositioning"
    FIXED = "fixed"
    MANUAL = "manual"


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


@dataclass
class PhaseImpedanceData:
    """Impedance and conductance matrix element values.

    The diagonal elements are described by the elements having the same
    toPhase and fromPhase value and the off diagonal elements have
    different toPhase and fromPhase values. The matrix can also be
    stored in symmetric lower triangular format using the row and column
    attributes, which map to ACLineSegmentPhase.sequenceNumber.

    :ivar b: Susceptance matrix element value, per length of unit.
    :ivar column: This matrix element's column number, in the range 1 to
        row. Only the lower triangle needs to be stored. Neutrals should
        be numbered last.  Multiple circuits on the same pole, tower or
        right-of-way can be included with unique sequence numbers for
        the phases, and identical sequence numbers for any shared
        neutrals. This solumn number matches
        ACLineSegmentPhase.sequenceNumber, WirePosition.sequenceNumber
        and WirePhaseInfo.sequenceNumber as applicable..
    :ivar g: Conductance matrix element value, per length of unit.
    :ivar r: Resistance matrix element value, per length of unit.
    :ivar row: This matrix element's row number, in the range 1 to
        PerLengthPhaseImpedance.conductorCount. Only the lower triangle
        needs to be stored. Neutrals should be numbered last.  Multiple
        circuits on the same pole, tower or right-of-way can be included
        with unique sequence numbers for the phases, and identical
        sequence numbers for any shared neutrals. This row number
        matches ACLineSegmentPhase.sequenceNumber,
        WirePosition.sequenceNumber and WirePhaseInfo.sequenceNumber as
        applicable..
    :ivar x: Reactance matrix element value, per length of unit.
    :ivar phase_impedance: Conductor phase impedance to which this data
        belongs.
    """
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    column: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    row: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_impedance: Optional["PerLengthPhaseImpedance"] = field(
        default=None,
        metadata={
            "name": "PhaseImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
class PositionPoint:
    """Set of spatial coordinates that determine a point, defined in the
    coordinate system specified in 'Location.CoordinateSystem'.

    Use a single position point instance to desribe a point-oriented location. Use a sequence of position points to describe a line-oriented object (physical location of non-point oriented objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case, have first and last position point with the same values).

    :ivar group_number: Zero-relative sequence number of this group
        within a series of points; used when there is a need to express
        disjoint groups of points that are considered to be part of a
        single location.
    :ivar sequence_number: Zero-relative sequence number of this point
        within a series of points.
    :ivar x_position: X axis position.
    :ivar y_position: Y axis position.
    :ivar z_position: (if applicable) Z axis position.
    :ivar location: Location described by this position point.
    """
    group_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "groupNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPosition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "yPosition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    z_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "zPosition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    location: Optional["Location"] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rank: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class ProcedureKind(Enum):
    """
    Kind of procedure.

    :cvar DIAGNOSIS: Diagnosis procedure.
    :cvar INSPECTION: Inspection procedure.
    :cvar MAINTENANCE: Maintenance procedure.
    :cvar OTHER: Other procedure.
    :cvar TEST: Test procedure.
    """
    DIAGNOSIS = "diagnosis"
    INSPECTION = "inspection"
    MAINTENANCE = "maintenance"
    OTHER = "other"
    TEST = "test"


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
class RationalNumber:
    """Rational number = 'numerator' / 'denominator'.

    :ivar denominator: Denominator. Value 1 indicates the number is a
        simple integer.
    :ivar numerator: Numerator.
    """
    denominator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ReadingInterharmonic:
    """
    Interharmonics are represented as a rational number 'numerator' /
    'denominator', and harmonics are represented using the same mechanism and
    identified by 'denominator'=1.

    :ivar denominator: Interharmonic denominator. Value 0 means not
        applicable. Value 2 is used in combination with 'numerator'=1 to
        represent interharmonic 1/2. Finally, value 1 indicates the
        harmonic of the order specified with 'numerator'.
    :ivar numerator: Interharmonic numerator. Value 0 means not
        applicable. Value 1 is used in combination with 'denominator'=2
        to represent interharmonic 1/2, and with 'denominator'=1 it
        represents fundamental frequency. Finally, values greater than 1
        indicate the harmonic of that order (e.g., 'numerator'=5 is the
        fifth harmonic).
    """
    denominator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class ReadingReasonKind(Enum):
    """
    Reason for the reading being taken.

    :cvar BILLING: Reading(s) taken or to be taken in response to a
        billing-related inquiry by a customer or other party. A variant
        of 'inquiry'.
    :cvar DEMAND_RESET: Reading(s) taken or to be taken in conjunction
        with the resetting of one or more demand registers in a meter.
    :cvar INQUIRY: Reading(s) taken or to be taken in response to an
        inquiry by a customer or other party.
    :cvar INSTALLATION: Reading(s) taken or to be taken in conjunction
        with installation of a meter.
    :cvar LOAD_MANAGEMENT: Reading(s) taken or to be taken to support
        management of loads on distribution networks or devices.
    :cvar LOAD_RESEARCH: Reading(s) taken or to be taken to support
        research and analysis of loads on distribution networks or
        devices.
    :cvar MOVE_IN: Reading(s) taken or to be taken in conjunction with a
        customer move-in event.
    :cvar MOVE_OUT: Reading(s) taken or to be taken in conjunction with
        a customer move-out event.
    :cvar OTHER: Reading(s) taken or to be taken for some other reason
        or purpose.
    :cvar REMOVAL: Reading(s) taken or to be taken in conjunction with
        removal of a meter.
    :cvar SERVICE_CONNECT: Reading(s) taken or to be taken in
        conjunction with a connection or re-connection of service.
    :cvar SERVICE_DISCONNECT: Reading(s) taken or to be taken in
        conjunction with a disconnection of service.
    """
    BILLING = "billing"
    DEMAND_RESET = "demandReset"
    INQUIRY = "inquiry"
    INSTALLATION = "installation"
    LOAD_MANAGEMENT = "loadManagement"
    LOAD_RESEARCH = "loadResearch"
    MOVE_IN = "moveIn"
    MOVE_OUT = "moveOut"
    OTHER = "other"
    REMOVAL = "removal"
    SERVICE_CONNECT = "serviceConnect"
    SERVICE_DISCONNECT = "serviceDisconnect"


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    interval_schedule: Optional["RegularIntervalSchedule"] = field(
        default=None,
        metadata={
            "name": "IntervalSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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


class RelativeDisplacementKind(Enum):
    """
    The types of relative displacement.
    """
    CENTRE_EARTH = "centreEarth"
    GROUND = "ground"
    SEA_LEVEL = "seaLevel"


class ReportingMethodKind(Enum):
    """
    Method by which information is gathered from station.

    :cvar AUTOMATED: Station automatically reports.
    :cvar MANUAL: Station must be physically visited to gather
        observations.
    :cvar QUERIED: Station must be queried to obtain observations.
    """
    AUTOMATED = "automated"
    MANUAL = "manual"
    QUERIED = "queried"


class RevenueKind(Enum):
    """
    Accounting classification of the type of revenue collected for the customer
    agreement, typically used to break down accounts for revenue accounting.

    :cvar COMMERCIAL: Commercial revenue.
    :cvar INDUSTRIAL: Industrial revenue.
    :cvar IRRIGATION: Irrigation revenue.
    :cvar NON_RESIDENTIAL: Non-residential revenue.
    :cvar OTHER: Other revenue kind.
    :cvar RESIDENTIAL: Residential revenue.
    :cvar STREET_LIGHT: Streetlight revenue.
    """
    COMMERCIAL = "commercial"
    INDUSTRIAL = "industrial"
    IRRIGATION = "irrigation"
    NON_RESIDENTIAL = "nonResidential"
    OTHER = "other"
    RESIDENTIAL = "residential"
    STREET_LIGHT = "streetLight"


class RiskScoreKind(Enum):
    CUSTOMER_RISK = "customerRisk"
    FINANCIAL_RISK = "financialRisk"
    SAFETY_RISK = "safetyRisk"


class SvccontrolMode(Enum):
    """
    Static VAr Compensator control mode.
    """
    REACTIVE_POWER = "reactivePower"
    VOLTAGE = "voltage"


class SampleContainerType(Enum):
    GLASS_CAN = "glassCan"
    METAL_CAN = "metalCan"
    SYRINGE = "syringe"


class ScaleKind(Enum):
    EXPONENTIAL = "exponential"
    LINEAR = "linear"


class SealConditionKind(Enum):
    """
    Kind of seal condition.

    :cvar BROKEN: Seal is broken.
    :cvar LOCKED: Seal is locked.
    :cvar MISSING: Seal is missing.
    :cvar OPEN: Seal is open.
    :cvar OTHER: Other kind of seal condition.
    """
    BROKEN = "broken"
    LOCKED = "locked"
    MISSING = "missing"
    OPEN = "open"
    OTHER = "other"


class SealKind(Enum):
    """
    Kind of seal.

    :cvar LEAD: Lead seal.
    :cvar LOCK: Lock seal.
    :cvar OTHER: Other kind of seal.
    :cvar STEEL: Steel seal.
    """
    LEAD = "lead"
    LOCK = "lock"
    OTHER = "other"
    STEEL = "steel"


class ServiceKind(Enum):
    """
    Kind of service.

    :cvar AIR: Air service.
    :cvar ELECTRICITY: Electricity service.
    :cvar GAS: Gas service.
    :cvar HEAT: Heat service.
    :cvar HEATING_FLUID: Heating fluid service.
    :cvar INTERNET: Internet service.
    :cvar NATURAL_GAS: Natural gas service.
    :cvar OTHER: Other kind of service.
    :cvar PROPANE: Propane service.
    :cvar RATES: Rates (e.g. tax, charge, toll, duty, tariff, etc.)
        service.
    :cvar REFUSE: Refuse (waster) service.
    :cvar SEWERAGE: Sewerage service.
    :cvar STEAM: Steam service.
    :cvar TIME: Time service.
    :cvar TV_LICENCE: TV license service.
    :cvar WATER: Water service.
    """
    AIR = "air"
    ELECTRICITY = "electricity"
    GAS = "gas"
    HEAT = "heat"
    HEATING_FLUID = "heatingFluid"
    INTERNET = "internet"
    NATURAL_GAS = "naturalGas"
    OTHER = "other"
    PROPANE = "propane"
    RATES = "rates"
    REFUSE = "refuse"
    SEWERAGE = "sewerage"
    STEAM = "steam"
    TIME = "time"
    TV_LICENCE = "tvLicence"
    WATER = "water"


@dataclass
class ServiceLocation:
    """
    A real estate location, commonly referred to as premises.

    :ivar access_method: Method for the service person to access this
        service location. For example, a description of where to obtain
        a key if the facility is unmanned and secured.
    :ivar needs_inspection: True if inspection is needed of facilities
        at this service location. This could be requested by a customer,
        due to suspected tampering, environmental concerns (e.g., a fire
        in the vicinity), or to correct incompatible data.
    :ivar site_access_problem: Problems previously encountered when
        visiting or performing work on this location. Examples include:
        bad dog, violent customer, verbally abusive occupant,
        obstructions, safety hazards, etc.
    :ivar customer_agreements: All customer agreements regulating this
        service location.
    :ivar end_devices: All end devices that measure the service
        delivered to this service location.
    :ivar trouble_ticket:
    :ivar usage_points: All usage points delivering service (of the same
        type) to this service location.
    """
    access_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "accessMethod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    needs_inspection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "needsInspection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    site_access_problem: Optional[str] = field(
        default=None,
        metadata={
            "name": "siteAccessProblem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_agreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAgreements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_devices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    trouble_ticket: List["TroubleTicket"] = field(
        default_factory=list,
        metadata={
            "name": "TroubleTicket",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class ServiceMultiplierKind(Enum):
    """
    Kind of service multiplier.

    :cvar CT_RATIO: Current transformer ratio used to convert associated
        quantities to real measurements.
    :cvar PT_RATIO: Voltage transformer ratio used to convert associated
        quantities to real measurements.
    :cvar TRANSFORMER_RATIO: Product of the CT ratio and PT ratio.
    """
    CT_RATIO = "ctRatio"
    PT_RATIO = "ptRatio"
    TRANSFORMER_RATIO = "transformerRatio"


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


class SmartInverterMode(Enum):
    """
    :cvar CONSTANT_PF:
    :cvar CONSTANT_PQ: Required to dispatch P and Q
    :cvar LOAD_FOLLOWING: For batteries
    :cvar VOLT_VAR: Default IEEE 1547-2018
    :cvar VOLT_WATT: Default IEEE 1547-2018
    """
    CONSTANT_PF = "constantPF"
    CONSTANT_PQ = "constantPQ"
    LOAD_FOLLOWING = "loadFollowing"
    VOLT_VAR = "voltVar"
    VOLT_WATT = "voltWatt"


class SpaceAnalogKind(Enum):
    """
    Kinds of analogs measuring a space condition.
    """
    MAGNETIC_FIELD_DIRECTION = "magneticFieldDirection"
    MAGNETIC_FIELD_STRENGTH = "magneticFieldStrength"


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class StreetDetail:
    """
    Street details, in the context of address.

    :ivar address_general: First line of a free form address or some
        additional address information (for example a mail stop).
    :ivar address_general2: (if applicable) Second line of a free form
        address.
    :ivar address_general3: (if applicable) Third line of a free form
        address.
    :ivar building_name: (if applicable) In certain cases the physical
        location of the place of interest does not have a direct point
        of entry from the street, but may be located inside a larger
        structure such as a building, complex, office block, apartment,
        etc.
    :ivar code: (if applicable) Utilities often make use of external
        reference systems, such as those of the town-planner's
        department or surveyor general's mapping system, that allocate
        global reference codes to streets.
    :ivar name: Name of the street.
    :ivar number: Designator of the specific location on the street.
    :ivar prefix: Prefix to the street name. For example: North, South,
        East, West.
    :ivar suffix: Suffix to the street name. For example: North, South,
        East, West.
    :ivar suite_number: Number of the apartment or suite.
    :ivar type: Type of street. Examples include: street, circle,
        boulevard, avenue, road, drive, etc.
    :ivar within_town_limits: True if this street is within the legal
        geographical boundaries of the specified town (default).
    """
    address_general: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    address_general2: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    address_general3: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    building_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "buildingName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    suite_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "suiteNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    within_town_limits: Optional[bool] = field(
        default=None,
        metadata={
            "name": "withinTownLimits",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class SynchronousMachineKind(Enum):
    """
    Synchronous machine type.
    """
    CONDENSER = "condenser"
    GENERATOR = "generator"
    GENERATOR_OR_CONDENSER = "generatorOrCondenser"
    GENERATOR_OR_CONDENSER_OR_MOTOR = "generatorOrCondenserOrMotor"
    GENERATOR_OR_MOTOR = "generatorOrMotor"
    MOTOR = "motor"
    MOTOR_OR_CONDENSER = "motorOrCondenser"


class SynchronousMachineOperatingMode(Enum):
    """
    Synchronous machine operating mode.
    """
    CONDENSER = "condenser"
    GENERATOR = "generator"
    MOTOR = "motor"


class TappistandardEditionKind(Enum):
    """
    List of editions for TAPPI standards.
    """
    VALUE_2009 = "2009"
    NONE = "none"
    UNKNOWN = "unknown"


class TappistandardKind(Enum):
    """
    List of TAPPI  standards.

    :cvar T494: Tensile properties of paper and paperboard(using
        constant rate of elongation apparatus), Test Method TAPPI/ANSI T
        494 om-13.
    """
    T494 = "T494"


@dataclass
class TapChangerTablePoint:
    """
    :ivar b: The magnetizing branch susceptance deviation in percent of
        nominal value. The actual susceptance is calculated as follows:
        calculated magnetizing susceptance = b(nominal) * (1 + b(from
        this class)/100).   The b(nominal) is defined as the static
        magnetizing susceptance on the associated power transformer end
        or ends.  This model assumes the star impedance (pi model) form.
    :ivar g: The magnetizing branch conductance deviation in percent of
        nominal value. The actual conductance is calculated as follows:
        calculated magnetizing conductance = g(nominal) * (1 + g(from
        this class)/100).   The g(nominal) is defined as the static
        magnetizing conductance on the associated power transformer end
        or ends.  This model assumes the star impedance (pi model) form.
    :ivar r: The resistance deviation in percent of nominal value. The
        actual reactance is calculated as follows: calculated resistance
        = r(nominal) * (1 + r(from this class)/100).   The r(nominal) is
        defined as the static resistance on the associated power
        transformer end or ends.  This model assumes the star impedance
        (pi model) form.
    :ivar ratio: The voltage at the tap step divided by rated voltage of
        the transformer end having the tap changer. Hence this is a
        value close to one. For example, if the ratio at step 1 is 1.01,
        and the rated voltage of the transformer end is 110kV, then the
        voltage obtained by setting the tap changer to step 1 to is
        111.1kV.
    :ivar step: The tap step.
    :ivar x: The series reactance deviation in percent of nominal value.
        The actual reactance is calculated as follows: calculated
        reactance = x(nominal) * (1 + x(from this class)/100).   The
        x(nominal) is defined as the static series reactance on the
        associated power transformer end or ends.  This model assumes
        the star impedance (pi model) form.
    """
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    step: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class TelephoneNumber:
    """
    Telephone number.

    :ivar area_code: (if applicable) Area or region code.
    :ivar city_code: City code.
    :ivar country_code: Country code.
    :ivar dial_out: (if applicable) Dial out code, for instance to call
        outside an enterprise.
    :ivar extension: (if applicable) Extension for this telephone
        number.
    :ivar international_prefix: (if applicable) Prefix used when calling
        an international number.
    :ivar itu_phone: Phone number according to ITU E.164.
    :ivar local_number: Main (local) part of this telephone number.
    """
    area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "areaCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "cityCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "countryCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dial_out: Optional[str] = field(
        default=None,
        metadata={
            "name": "dialOut",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    international_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "internationalPrefix",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    itu_phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "ituPhone",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    local_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "localNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class TestKind(Enum):
    """
    The test applied to determine if the condition is met.
    """
    EQUAL_TO = "equalTo"
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL_TO = "greaterThanOrEqualTo"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL_TO = "lessThanOrEqualTo"


class TestMethod(Enum):
    """
    :cvar VALUE_60567_BY_DISPLACEMENT:
    :cvar VALUE_60567_BY_PARTITION:
    :cvar VALUE_60567_BY_VACUUM:
    :cvar VALUE_60970_AUTOMATIC: Automatic method.
    :cvar VALUE_60970_MANUAL1: Manual method 1.
    :cvar VALUE_60970_MANUAL2: Manual method 2.
    :cvar VALUE_61125_A:
    :cvar VALUE_61125_B:
    :cvar VALUE_61125_C:
    :cvar VALUE_62270_ANNEX_A:
    :cvar VALUE_62535_ANNEX_A:
    :cvar VALUE_62535_MAIN:
    :cvar D1275_A:
    :cvar D1275_B:
    :cvar D3612_A:
    :cvar D3612_B:
    :cvar D3612_C:
    """
    VALUE_60567_BY_DISPLACEMENT = "60567ByDisplacement"
    VALUE_60567_BY_PARTITION = "60567ByPartition"
    VALUE_60567_BY_VACUUM = "60567ByVacuum"
    VALUE_60970_AUTOMATIC = "60970Automatic"
    VALUE_60970_MANUAL1 = "60970Manual1"
    VALUE_60970_MANUAL2 = "60970Manual2"
    VALUE_61125_A = "61125A"
    VALUE_61125_B = "61125B"
    VALUE_61125_C = "61125C"
    VALUE_62270_ANNEX_A = "62270AnnexA"
    VALUE_62535_ANNEX_A = "62535AnnexA"
    VALUE_62535_MAIN = "62535Main"
    D1275_A = "D1275A"
    D1275_B = "D1275B"
    D3612_A = "D3612A"
    D3612_B = "D3612B"
    D3612_C = "D3612C"


class TestReason(Enum):
    POST_OIL_TREATMENT = "postOilTreatment"
    POST_OPERATION_FAULT = "postOperationFault"
    POST_REPAIR = "postRepair"
    ROUTINE = "routine"


class TestVariantKind(Enum):
    """
    :cvar VALUE_0_C: Testing done at temperature of 0ï¿½C.
    :cvar VALUE_100_C: Testing done at temperature of  100ï¿½C.
    :cvar VALUE_164HOURS: Measurements taken at 164 hours.
    :cvar VALUE_1MM: Specimen of 1 mm thickness used in testing.
    :cvar VALUE_25_C: Testing done at temperature of  25ï¿½C.
    :cvar VALUE_2MM: Specimen of 2 mm thickness used in testing.
    :cvar VALUE_30_C: Testing done at temperature of 30ï¿½C.
    :cvar VALUE_40_C: Testing done at temperature of 40ï¿½C.
    :cvar VALUE_72HOURS: Measurements taken at 72 hours.
    :cvar MINUS30_C: Testing done at temperature of -30ï¿½C.
    :cvar MINUS40_C: Testing done at temperature of -40ï¿½C.
    """
    VALUE_0_C = "0C"
    VALUE_100_C = "100C"
    VALUE_164HOURS = "164hours"
    VALUE_1MM = "1mm"
    VALUE_25_C = "25C"
    VALUE_2MM = "2mm"
    VALUE_30_C = "30C"
    VALUE_40_C = "40C"
    VALUE_72HOURS = "72hours"
    MINUS30_C = "minus30C"
    MINUS40_C = "minus40C"


class ThermostatControlMode(Enum):
    COOLING = "Cooling"
    HEATING = "Heating"


@dataclass
class TimeInterval:
    """
    Interval between two times.

    :ivar end: End time of this interval.
    :ivar start: Start time of this interval.
    """
    end: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    start: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class TimeIntervalKind(Enum):
    D = "D"
    M = "M"
    Y = "Y"
    H = "h"
    M_1 = "m"
    S = "s"


@dataclass
class TownDetail:
    """
    Town details, in the context of address.

    :ivar code: Town code.
    :ivar country: Name of the country.
    :ivar name: Town name.
    :ivar section: Town section. For example, it is common for there to
        be 36 sections per township.
    :ivar state_or_province: Name of the state or province.
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    section: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    state_or_province: Optional[str] = field(
        default=None,
        metadata={
            "name": "stateOrProvince",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class TransformerApplicationKind(Enum):
    """Classifications of network roles in which transformers can be deployed.

    The classifications are intended to reflect both criticality of transformer in network operations and typical usage experienced by transformer.
    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    DISTRIBUTION = "distribution"
    GENERATOR_STEP_UP = "generatorStepUp"
    TRANSMISSION_BUS_TO_BUS = "transmissionBusToBus"
    TRANSMISSION_BUS_TO_DISTRIBUTION = "transmissionBusToDistribution"


class TransformerFailureReasonKind(Enum):
    """Reason for transformer failure.

    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    BUSHING_FAILURE = "bushingFailure"
    LOSS_OF_OIL = "lossOfOil"
    OIL_RELATED_FAILURE = "oilRelatedFailure"
    POOR_OIL_QUALITY = "poorOilQuality"


class TransmissionModeKind(Enum):
    """
    Transmission mode for end device display controls, applicable to premises
    area network (PAN) devices.

    :cvar ANONYMOUS: Message transmission mode whereby messages or
        commands are broadcast to unspecified devices listening for such
        communications.
    :cvar BOTH: Message transmission mode whereby messages or commands
        are sent by both 'normal' and 'anonymous' methods.
    :cvar NORMAL: Message transmission mode whereby messages or commands
        are sent to specific devices.
    """
    ANONYMOUS = "anonymous"
    BOTH = "both"
    NORMAL = "normal"


class TroubleReportingKind(Enum):
    """
    Kind of trouble reporting.

    :cvar CALL: Trouble call received by customer service
        representative.
    :cvar EMAIL: Trouble reported by email.
    :cvar IVR: Trouble reported through interactive voice response
        system.
    :cvar LETTER: Trouble reported by letter.
    :cvar OTHER: Trouble reported by other means.
    """
    CALL = "call"
    EMAIL = "email"
    IVR = "ivr"
    LETTER = "letter"
    OTHER = "other"


class UkministryOfDefenceStandardEditionKind(Enum):
    """
    List of editions for UK Ministry of Defence standards.
    """
    ISSUE_1 = "Issue 1"
    NONE = "none"
    UNKNOWN = "unknown"


class UkministryofDefenceStandardKind(Enum):
    """
    List of UK Ministry of Defence standards.

    :cvar VALUE_05_50_PART_65: Ministry of Defence, Defence Standard
        05-50 (Part 65)/Issue 1 METHODS FOR TESTING FUELS, LUBRICANTS
        AND ASSOCIATED PRODUCTS.
    """
    VALUE_05_50_PART_65 = "05-50 (Part 65)"


@dataclass
class UnderfrequencyTripCurveData:
    f: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    t: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class UndervoltageTripCurveData:
    t: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    v: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


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
    symbol for the unit type. If one imagines that the symbol "ï¿½"
    represents the derived unit "A2Perh", then applying the multiplier
    "k" can be conceptualized simply as "kï¿½". For example, the SI unit
    for mass is "kg" and not "g".  If the unit symbol is defined as
    "kg", then the multiplier is applied to "kg" as a whole and does not
    replace the "k" in front of the "g". In this case, the multiplier of
    "m" would be used with the unit symbol of "kg" to represent one
    gram.  As a text string, this violates the instructions in IEC
    80000-1. However, because the unit symbol in CIM is treated as a
    derived unit instead of as an SI unit, it makes more sense to
    conceptualize the "kg" as if it were replaced by one of the proposed
    replacements for the SI mass symbol. If one imagines that the "kg"
    were replaced by a symbol "ï¿½", then it is easier to conceptualize
    the multiplier "m" as creating the proper unit "mï¿½", and not the
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
    degree symbol "ï¿½" is replaced with the letters "deg". Any
    clarification of the meaning for a substitution is included in the
    description for the unit symbol. Non-SI units are included in list
    of unit symbols to allow sources of data to be correctly labeled
    with their non-SI units (for example, a GPS sensor that is reporting
    numbers that represent feet instead of meters). This allows software
    to use the unit symbol information correctly convert and scale the
    raw data of those sources into SI-based units.

    :cvar A: Current in Ampere.
    :cvar A2: Ampere squared (Aï¿½).
    :cvar A2H: ampere-squared hour, Ampere-squared hour.
    :cvar A2S: Ampere squared time in square ampere (Aï¿½s).
    :cvar APER_A: Current, Ratio of Amperages  Note: Users may need to
        supply a prefix such as ï¿½mï¿½ to show rates such as
        ï¿½mA/Aï¿½.
    :cvar APERM: A/m, magnetic field strength, Ampere per metre.
    :cvar AH: Ampere-hours, Ampere-hours.
    :cvar AS: Ampere seconds (Aï¿½s).
    :cvar BQ: Radioactivity in Becquerel (1/s).
    :cvar BTU: Energy, British Thermal Unit.
    :cvar C: Electric charge in Coulomb (Aï¿½s).
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
        may need to supply a prefix such as ï¿½mï¿½ to show rates such
        as ï¿½mHz/Hzï¿½.
    :cvar HZ_PERS: Rate of change of frequency in Hertz per second.
    :cvar J: Energy in joule (Nï¿½m = Cï¿½V = Wï¿½s).
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
    :cvar N: Force in Newton (kgï¿½m/sï¿½).
    :cvar NPERM: Surface tension, Newton per metre.
    :cvar NM: Moment of force, Newton metre.
    :cvar OE: Magnetic field, ï¿½rsted (1 Oe = (103/4p) A/m).
    :cvar PA: Pressure in Pascal (N/mï¿½). Note: the absolute or
        relative measurement of pressure is implied with this entry. See
        below for more explicit forms.
    :cvar PA_PERS: Pressure change rate in Pascal per second.
    :cvar PAS: Dynamic viscosity, Pascal second.
    :cvar Q: Quantity power, Q.
    :cvar QH: Quantity energy, Qh.
    :cvar S: Conductance in Siemens.
    :cvar SPERM: Conductance per length (F/m).
    :cvar SV: Dose equivalent in Sievert (J/kg).
    :cvar T: Magnetic flux density in Tesla (Wb/m2).
    :cvar V: Electric potential in Volt (W/A).
    :cvar V2: Volt squared (Wï¿½/Aï¿½).
    :cvar V2H: volt-squared hour, Volt-squared-hours.
    :cvar VA: Apparent power in Volt Ampere (See also real power and
        reactive power.)
    :cvar VAH: Apparent energy in Volt Ampere hours.
    :cvar VAR: Reactive power in Volt Ampere reactive. The
        ï¿½reactiveï¿½ or ï¿½imaginaryï¿½ component of electrical power
        (VIsin(phi)). (See also real power and apparent power). Note:
        Different meter designs use different methods to arrive at their
        results. Some meters may compute reactive power as an arithmetic
        value, while others compute the value vectorially. The data
        consumer should determine the method in use and the suitability
        of the measurement for the intended purpose.
    :cvar VARH: Reactive energy in Volt Ampere reactive hours.
    :cvar VPER_HZ: Magnetic flux in Volt per Hertz.
    :cvar VPER_V: Voltage, Ratio of voltages Note: Users may need to
        supply a prefix such as ï¿½mï¿½ to show rates such as
        ï¿½mV/Vï¿½.
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
        (Iï¿½R or VIcos(phi)), is expressed in Watts. (See also apparent
        power and reactive power.)
    :cvar WPER_A: Active power per current flow, watt per Ampere.
    :cvar WPER_W: Signal Strength, Ratio of power  Note: Users may need
        to supply a prefix such as ï¿½mï¿½ to show rates such as
        ï¿½mW/Wï¿½.
    :cvar WPERM2: Heat flux density, irradiance, Watt per square metre.
    :cvar WPERM2SR: radiance, Watt per square metre steradian.
    :cvar WPERM_K: Thermal conductivity in Watt/metre Kelvin.
    :cvar WPERS: Ramp rate in Watt per second.
    :cvar WPERSR: Radiant intensity, Watt per steradian.
    :cvar WB: Magnetic flux in Weber (Vï¿½s).
    :cvar WH: Real energy in Watt hours.
    :cvar ANGLEMIN: Plane angle, minute.
    :cvar ANGLESEC: Plane angle, second.
    :cvar BAR: Pressure, bar (1 bar = 100 kPa).
    :cvar CD: Luminous intensity in candela.
    :cvar CHAR_PERS: Data rate (baud) in characters per second.
    :cvar CHARACTER: Number of characters.
    :cvar COS_PHI: Power factor, dimensionless. Note 1: This definition
        of power factor only holds for balanced systems. See the
        alternative definition under code 153. Note 2ï¿½: Beware of
        differing sign conventions in use between the IEC and EEI. It is
        assumed that the data consumer understands the type of meter in
        use and the sign convention in use by the utility.
    :cvar COUNT: Amount of substance, Counter value.
    :cvar D: Time, day = 24 h = 86400 s.
    :cvar D_B: Sound pressure level in decibel. Note:  multiplier
        ï¿½dï¿½ is included in this unit symbol for compatibility with
        IEC 61850-7-3.
    :cvar D_BM: Power level (logrithmic ratio of signal strength , Bel-
        mW), normalized to 1mW. Note:  multiplier ï¿½dï¿½ is included in
        this unit symbol for compatibility with IEC 61850-7-3.
    :cvar DEG: Plane angle in degrees.
    :cvar DEG_C: Relative temperature in degrees Celsius. In the SI unit
        system the symbol is ï¿½C. Electric charge is measured in
        coulomb that has the unit symbol C. To distinguish degree
        Celsius form coulomb the symbol used in the UML is degC. Reason
        for not using ï¿½C is the special character ï¿½ is difficult to
        manage in software.
    :cvar FT3: Volume, cubic foot.
    :cvar G_PERG: Concentration, The ratio of the mass of a solute
        divided by the mass of  the solution. Note: Users may need use a
        prefix such a ï¿½ï¿½ï¿½ to express a quantity such as
        ï¿½ï¿½g/gï¿½.
    :cvar GAL: Volume, US gallon (1 gal = 231 in3 = 128 fl ounce).
    :cvar H_1: Time, hour = 60 min = 3600 s.
    :cvar HA: Area, hectare.
    :cvar KAT: Catalytic activity, katal = mol / s.
    :cvar KAT_PERM3: catalytic activity concentration, katal per cubic
        metre.
    :cvar KG: Mass in kilogram.  Note: multiplier ï¿½kï¿½ is included in
        this unit symbol for compatibility with IEC 61850-7-3.
    :cvar KG_PER_J: Weigh per energy in kilogram/joule (kg/J). Note:
        multiplier ï¿½kï¿½ is included in this unit symbol for
        compatibility with IEC 61850-7-3.
    :cvar KG_PERM3: Density in kilogram/cubic metre (kg/mï¿½). Note:
        multiplier ï¿½kï¿½ is included in this unit symbol for
        compatibility with IEC 61850-7-3.
    :cvar KGM: Moment of mass in kilogram metre (kgï¿½m) (first moment
        of mass). Note: multiplier ï¿½kï¿½ is included in this unit
        symbol for compatibility with IEC 61850-7-3.
    :cvar KGM2: Moment of mass in kilogram square metre (kgï¿½mï¿½)
        (Second moment of mass, commonly called the moment of inertia).
        Note: multiplier ï¿½kï¿½ is included in this unit symbol for
        compatibility with IEC 61850-7-3.
    :cvar KN: Speed, knot (1 kn = 1852/3600) m/s.
    :cvar L: Volume, litre = dm3 = m3/1000.
    :cvar L_PERH: Volumetric flow rate, litre per hour.
    :cvar L_PERL: Concentration, The ratio of the volume of a solute
        divided by the volume of  the solution. Note: Users may need use
        a prefix such a ï¿½ï¿½ï¿½ to express a quantity such as
        ï¿½ï¿½L/Lï¿½.
    :cvar L_PERS: Volumetric flow rate in litre per second.
    :cvar LM: Luminous flux in lumen (cdï¿½sr).
    :cvar LX: Illuminance in lux (lm/mï¿½).
    :cvar M_1: Length in meter.
    :cvar M2: Area in square metre (mï¿½).
    :cvar M2_PERS: Viscosity in metre square / second (mï¿½/s).
    :cvar M3: Volume in cubic metre (mï¿½).
    :cvar M3_COMPENSATED: Volume, cubic metre, with the value
        compensated for weather effects.
    :cvar M3_PERH: Volumetric flow rate, cubic metre per hour.
    :cvar M3_PERKG: Specific volume, cubic metre per kilogram, v.
    :cvar M3_PERS: Volumetric flow rate in cubic metres per second
        (mï¿½/s).
    :cvar M3_UNCOMPENSATED: Volume, cubic metre, with the value
        uncompensated for weather effects.
    :cvar M_PERM3: Fuel efficiency in metre per cubic metre (m/mï¿½).
    :cvar M_PERS: Velocity in metre per second (m/s).
    :cvar M_PERS2: Acceleration in metre per second squared (m/sï¿½).
    :cvar MIN: Time, minute  = 60 s.
    :cvar MM_HG: Pressure, millimeter of mercury (1 mmHg is
        approximately 133.3 Pa).
    :cvar MOL: Amount of substance in mole.
    :cvar MOL_PERKG: Concentration, Molality, the amount of solute in
        moles and the amount of solvent in kilograms.
    :cvar MOL_PERM3: Concentration, The amount of substance
        concentration, (c), the amount of solvent in moles divided by
        the volume of solution in mï¿½.
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
        prefix such as ï¿½ï¿½ï¿½ to show rates such as ï¿½ï¿½s/sï¿½
    :cvar SR: Solid angle in steradian (m2/m2).
    :cvar THERM: Energy, Therm.
    :cvar TONNE: mass, ï¿½tonneï¿½ or ï¿½metric  tonï¿½ (1000 kg = 1
        Mg).
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


class Validity(Enum):
    """
    Validity for MeasurementValue.

    :cvar GOOD: The value is marked good if no abnormal condition of the
        acquisition function or the information source is detected.
    :cvar INVALID: The value is marked invalid when a supervision
        function recognises abnormal conditions of the acquisition
        function or the information source (missing or non-operating
        updating devices). The value is not defined under this
        condition. The mark invalid is used to indicate to the client
        that the value may be incorrect and shall not be used.
    :cvar QUESTIONABLE: The value is marked questionable if a
        supervision function detects an abnormal behaviour, however the
        value could still be valid. The client is responsible for
        determining whether or not values marked "questionable" should
        be used.
    """
    GOOD = "GOOD"
    INVALID = "INVALID"
    QUESTIONABLE = "QUESTIONABLE"


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    major: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    revision: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VoltVarCurveData:
    q: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    v: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VoltWattCurveData:
    p: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    v: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class WepstandardEditionKind(Enum):
    """
    List of editions for WEP standards.
    """
    NONE = "none"
    UNKNOWN = "unknown"


class WepstandardKind(Enum):
    """
    List of WEP standards.

    :cvar VALUE_12_1254_E: Westinghouse Engineering Procedure 12,1254E.
    """
    VALUE_12_1254_E = "12, 1254E"


@dataclass
class WattVarCurveData:
    p: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class WeatherCodeKind(Enum):
    """
    Kinds of weather conditions.

    :cvar BLOWING_DUST: "BD" weather code ("Blowing Dust").
    :cvar BLOWING_SAND: "BN" weather code ("Blowing Sand").
    :cvar BLOWING_SNOW: "BS" weather code ("Blowing Snow").
    :cvar CLOUDY:
    :cvar DRIZZLE: "L" weather code ("Drizzle").
    :cvar FOG: "F weather code ("Fog
    :cvar FREEZING_DRIZZLE: "ZL" weather code ("Freezing Drizzle").
    :cvar FREEZING_RAIN: "ZR" weather code ("Freezing Rain").
    :cvar FREEZING_SPRAY: "ZF" weather code ("Freezing Spray").
    :cvar FROST: "FR" weather code ("Frost").
    :cvar HAIL: "A" weather code ("Hail").
    :cvar HAZE: "H" weather code ("Haze").
    :cvar ICE_CRYSTALS: "IC" weather code ("Ice Crystals").
    :cvar ICE_FOG: "IF" weather code ("Ice Fog").
    :cvar MIST: "BR" weather code ("Mist"),
    :cvar RAIN: "R" weather code ("Rain").
    :cvar RAIN_SHOWERS: "RW" weather code ("Rain Showers").
    :cvar RAIN_SNOW_MIX: "RS" weather code ("Rain/Snow Mix").
    :cvar SLEET: "IP" weather code ("Ice Pellets/Sleet").
    :cvar SMOKE: "K" weather code ("Smoke").
    :cvar SNOW: "S" weather code ("Snow").
    :cvar SNOW_SHOWERS: "SW" weather code ("Snow Showers").
    :cvar SNOW_SLEET_MIX: "SI" weather code ("Snow/Sleet Mix").
    :cvar SUNNY:
    :cvar THUNDER_STORMS: "T" weather code ("Thunder Storms").
    :cvar VOLCANIC_ASH: "VA" weather code ("Volcanic Ash").
    :cvar WATER_SPOUTS: "WP" weather code ("Water Spouts")
    :cvar WINTRY_MIX: "WS" weather code ("Wintry Mix").
    """
    BLOWING_DUST = "blowingDust"
    BLOWING_SAND = "blowingSand"
    BLOWING_SNOW = "blowingSnow"
    CLOUDY = "cloudy"
    DRIZZLE = "drizzle"
    FOG = "fog"
    FREEZING_DRIZZLE = "freezingDrizzle"
    FREEZING_RAIN = "freezingRain"
    FREEZING_SPRAY = "freezingSpray"
    FROST = "frost"
    HAIL = "hail"
    HAZE = "haze"
    ICE_CRYSTALS = "iceCrystals"
    ICE_FOG = "iceFog"
    MIST = "mist"
    RAIN = "rain"
    RAIN_SHOWERS = "rainShowers"
    RAIN_SNOW_MIX = "rainSnowMix"
    SLEET = "sleet"
    SMOKE = "smoke"
    SNOW = "snow"
    SNOW_SHOWERS = "snowShowers"
    SNOW_SLEET_MIX = "snowSleetMix"
    SUNNY = "sunny"
    THUNDER_STORMS = "thunderStorms"
    VOLCANIC_ASH = "volcanicAsh"
    WATER_SPOUTS = "waterSpouts"
    WINTRY_MIX = "wintryMix"


class WindGenUnitKind(Enum):
    """
    Kind of wind generating unit.

    :cvar OFFSHORE: The wind generating unit is located offshore.
    :cvar ONSHORE: The wind generating unit is located onshore.
    """
    OFFSHORE = "offshore"
    ONSHORE = "onshore"


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


class WireUsageKind(Enum):
    """
    Kind of wire usage.

    :cvar DISTRIBUTION: Wire is used in medium voltage network.
    :cvar OTHER: Other kind of wire usage.
    :cvar SECONDARY: Wire is used in low voltage circuit.
    :cvar TRANSMISSION: Wire is used in extra-high voltage or high
        voltage network.
    """
    DISTRIBUTION = "distribution"
    OTHER = "other"
    SECONDARY = "secondary"
    TRANSMISSION = "transmission"


@dataclass
class Astmstandard:
    """
    Standard published by ASTM (ASTM International).

    :ivar standard_edition: Edition of ASTM standard.
    :ivar standard_number: ASTM standard number.
    """
    class Meta:
        name = "ASTMStandard"

    standard_edition: Optional[AstmstandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[AstmstandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Cigrestandard:
    """
    Standard published by CIGRE (Council on Large Electric Systems).

    :ivar standard_edition: Edition of CIGRE standard.
    :ivar standard_number: CIGRE standard number.
    """
    class Meta:
        name = "CIGREStandard"

    standard_edition: Optional[CigrestandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[CigrestandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Dinstandard:
    """
    Standard published by DIN (German Institute of Standards).

    :ivar standard_edition: Edition of DIN standard.
    :ivar standard_number: DIN standard number.
    """
    class Meta:
        name = "DINStandard"

    standard_edition: Optional[DinstandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[DinstandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    curve_style_kind: Optional[CurveStyle] = field(
        default=None,
        metadata={
            "name": "curveStyleKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    number_of_intervals: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfIntervals",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_interval_duration: Optional[int] = field(
        default=None,
        metadata={
            "name": "timeIntervalDuration",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    time_interval_unit: Optional[TimeIntervalKind] = field(
        default=None,
        metadata={
            "name": "timeIntervalUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dercurve_data: List["DercurveData"] = field(
        default_factory=list,
        metadata={
            "name": "DERCurveData",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dermonitorable_parameter: Optional["DermonitorableParameter"] = field(
        default=None,
        metadata={
            "name": "DERMonitorableParameter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class DobleStandard:
    """
    Standard published by Doble.

    :ivar standard_edition: Edition of Doble standard.
    :ivar standard_number: Doble standard number.
    """
    standard_edition: Optional[DobleStandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[DobleStandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Epastandard:
    """
    Standard published by EPA (United States Environmental Protection Agency).

    :ivar standard_edition: Edition of EPA standard.
    :ivar standard_number: EPA standard number.
    """
    class Meta:
        name = "EPAStandard"

    standard_edition: Optional[EpastandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[EpastandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    duration_indefinite: Optional[bool] = field(
        default=None,
        metadata={
            "name": "durationIndefinite",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    randomisation: Optional[RandomisationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ExtensionsList:
    extensions_item: Optional[ExtensionItem] = field(
        default=None,
        metadata={
            "name": "extensionsItem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FieldDispatchStep:
    """
    Details of the step in the field dispatch history.

    :ivar dispatch_status: The status of one or more crews dispatched to
        perform field work at one or more work sites
    :ivar occurred_date_time: The date and time at which the dispatch
        status occurred.
    :ivar remarks: freeform comments related to the dispatch to perform
        field work.
    :ivar sequence_number: The sequence number of the field dispatch
        step within the field dispatch history.  Begins with 1 and
        increments up.
    :ivar field_dispatch_history:
    """
    dispatch_status: Optional[CrewStatusKind] = field(
        default=None,
        metadata={
            "name": "dispatchStatus",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    occurred_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "occurredDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    field_dispatch_history: Optional["FieldDispatchHistory"] = field(
        default=None,
        metadata={
            "name": "FieldDispatchHistory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Iecstandard:
    """
    Standard published by IEC (International Electrotechnical Commission).

    :ivar standard_edition: Edition of IEC standard.
    :ivar standard_number: IEC standard number.
    """
    class Meta:
        name = "IECStandard"

    standard_edition: Optional[IecstandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[IecstandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Ieeestandard:
    """
    Standard published by IEEE (Institute of Electrical and Electronics
    Engineers).

    :ivar standard_edition: Edition of IEEE standard.
    :ivar standard_number: IEEE standard number.
    """
    class Meta:
        name = "IEEEStandard"

    standard_edition: Optional[IeeestandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[IeeestandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Isostandard:
    """
    Standard published by ISO (International Organization for Standardization).

    :ivar standard_edition: Edition of ISO standard.
    :ivar standard_number: ISO standard number.
    """
    class Meta:
        name = "ISOStandard"

    standard_edition: Optional[IsostandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[IsostandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class IntegerQuantity:
    """
    Quantity with integer value and associated unit information.
    """
    multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class LaborelecStandard:
    """
    Standard published by Laborelec.

    :ivar standard_edition: Edition of Laborelec standard.
    :ivar standard_number: Laborelec standard number.
    """
    standard_edition: Optional[LaborelecStandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[LaborelecStandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class NameType:
    """Type of name.

    Possible values for attribute 'name' are implementation dependent
    but standard profiles may specify types. An enterprise may have
    multiple IT systems each having its own local name for the same
    object, e.g. a planning system may have different names from an EMS.
    An object may also have different names within the same IT system,
    e.g. localName as defined in CIM version 14. The definition from
    CIM14 is: The localName is a human readable name of the object. It
    is a free text name local to a node in a naming hierarchy similar to
    a file directory structure. A power system related naming hierarchy
    may be: Substation, VoltageLevel, Equipment etc. Children of the
    same parent in such a hierarchy have names that typically are unique
    among them.

    :ivar description: Description of the name type.
    :ivar name: Name of the name type.
    :ivar names: All names of this type.
    :ivar name_type_authority: Authority responsible for managing names
        of this type.
    """
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    names: List["Name"] = field(
        default_factory=list,
        metadata={
            "name": "Names",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    name_type_authority: Optional[NameTypeAuthority] = field(
        default=None,
        metadata={
            "name": "NameTypeAuthority",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PanDemandResponse(EndDeviceAction):
    """
    PAN control used to issue action/command to PAN devices during a demand
    response/load control event.

    :ivar avg_load_adjustment: Used to define a maximum energy usage
        limit as a percentage of the client implementations specific
        average energy usage. The load adjustment percentage is added to
        100% creating a percentage limit applied to the client
        implementations specific average energy usage. A -10% load
        adjustment percentage will establish an energy usage limit equal
        to 90% of the client implementations specific average energy
        usage. Each load adjustment percentage is referenced to the
        client implementations specific average energy usage. There are
        no cumulative effects. The range of this field is -100% to +100%
        with a resolution of 1. A -100% value equals a total load shed.
        A +100% value will limit the energy usage to the client
        implementations specific average energy usage.
    :ivar cancel_control_mode: Encoding of cancel control.
    :ivar cancel_date_time: Timestamp when a canceling of the event is
        scheduled to start.
    :ivar cancel_now: If true, a canceling of the event should start
        immediately.
    :ivar cooling_offset: Requested offset to apply to the normal
        cooling setpoint at the time of the start of the event. It
        represents a temperature change that will be applied to the
        associated cooling set point. The temperature offsets will be
        calculated per the local temperature in the thermostat. The
        calculated temperature will be interpreted as the number of
        degrees to be added to the cooling set point. Sequential demand
        response events are not cumulative. The offset shall be applied
        to the normal setpoint.
    :ivar cooling_setpoint: Requested cooling set point. Temperature set
        point is typically defined and calculated based on local
        temperature.
    :ivar criticality_level: Level of criticality for the action of this
        control. The action taken by load control devices for an event
        can be solely based on this value, or in combination with other
        load control event fields supported by the device.
    :ivar duty_cycle: Maximum "on" state duty cycle as a percentage of
        time. For example, if the value is 80, the device would be in an
        "on" state for 80% of the time for the duration of the action.
    :ivar enrollment_group: Provides a mechanism to direct load control
        actions to groups of PAN devices. It can be used in conjunction
        with the PAN device types.
    :ivar heating_offset: Requested offset to apply to the normal
        heating setpoint at the time of the start of the event. It
        represents a temperature change that will be applied to the
        associated heating set point. The temperature offsets will be
        calculated per the local temperature in the thermostat. The
        calculated temperature will be interpreted as the number of
        degrees to be subtracted from the heating set point. Sequential
        demand response events are not cumulative. The offset shall be
        applied to the normal setpoint.
    :ivar heating_setpoint: Requested heating set point. Temperature set
        point is typically defined and calculated based on local
        temperature.
    :ivar appliance: Appliance being controlled.
    """
    avg_load_adjustment: Optional[float] = field(
        default=None,
        metadata={
            "name": "avgLoadAdjustment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cancel_control_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "cancelControlMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cancel_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "cancelDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cancel_now: Optional[bool] = field(
        default=None,
        metadata={
            "name": "cancelNow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cooling_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "coolingOffset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cooling_setpoint: Optional[float] = field(
        default=None,
        metadata={
            "name": "coolingSetpoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    criticality_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "criticalityLevel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    duty_cycle: Optional[float] = field(
        default=None,
        metadata={
            "name": "dutyCycle",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enrollment_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "enrollmentGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heating_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "heatingOffset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heating_setpoint: Optional[float] = field(
        default=None,
        metadata={
            "name": "heatingSetpoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    appliance: Optional[ControlledAppliance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PanDisplay(EndDeviceAction):
    """
    PAN action/command used to issue the displaying of text messages on PAN
    devices.

    :ivar confirmation_required: If true, the requesting entity (e.g.
        retail electric provider) requires confirmation of the
        successful display of the text message.
    :ivar priority: Priority associated with the text message to be
        displayed.
    :ivar text_message: Text to be displayed by a PAN device.
    :ivar transmission_mode: Transmission mode to be used for this PAN
        display control.
    """
    confirmation_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "confirmationRequired",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    text_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "textMessage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transmission_mode: Optional[TransmissionModeKind] = field(
        default=None,
        metadata={
            "name": "transmissionMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PanPricing(EndDeviceAction):
    """
    PAN action/command used to issue pricing information to a PAN device.

    :ivar provider_id: Unique identifier for the commodity provider.
    :ivar pan_pricing_details: All pricing details issued by this PAN
        pricing command/action.
    """
    provider_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "providerID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pan_pricing_details: List[PanPricingDetail] = field(
        default_factory=list,
        metadata={
            "name": "PanPricingDetails",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhaseTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the phase tap changer tabular curve.

    :ivar angle: The angle difference in degrees. A positive value
        indicates a positive phase shift from the winding where the tap
        is located to the other winding (for a two-winding transformer).
    :ivar phase_tap_changer_table: The table of this point.
    """
    angle: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_tap_changer_table: Optional["PhaseTapChangerTable"] = field(
        default=None,
        metadata={
            "name": "PhaseTapChangerTable",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Quality61850:
    """
    Quality flags in this class are as defined in IEC 61850, except for
    estimatorReplaced, which has been included in this class for convenience.

    :ivar bad_reference: Measurement value may be incorrect due to a
        reference being out of calibration.
    :ivar estimator_replaced: Value has been replaced by State
        Estimator. estimatorReplaced is not an IEC61850 quality bit but
        has been put in this class for convenience.
    :ivar failure: This identifier indicates that a supervision function
        has detected an internal or external failure, e.g. communication
        failure.
    :ivar old_data: Measurement value is old and possibly invalid, as it
        has not been successfully updated during a specified time
        interval.
    :ivar operator_blocked: Measurement value is blocked and hence
        unavailable for transmission.
    :ivar oscillatory: To prevent some overload of the communication it
        is sensible to detect and suppress oscillating (fast changing)
        binary inputs. If a signal changes in a defined time (tosc)
        twice in the same direction (from 0 to 1 or from 1 to 0) then
        oscillation is detected and the detail quality identifier
        "oscillatory" is set. If it is detected a configured numbers of
        transient changes could be passed by. In this time the validity
        status "questionable" is set. If after this defined numbers of
        changes the signal is still in the oscillating state the value
        shall be set either to the opposite state of the previous stable
        value or to a defined default value. In this case the validity
        status "questionable" is reset and "invalid" is set as long as
        the signal is oscillating. If it is configured such that no
        transient changes should be passed by then the validity status
        "invalid" is set immediately in addition to the detail quality
        identifier "oscillatory" (used for status information only).
    :ivar out_of_range: Measurement value is beyond a predefined range
        of value.
    :ivar over_flow: Measurement value is beyond the capability of being
        represented properly. For example, a counter value overflows
        from maximum count back to a value of zero.
    :ivar suspect: A correlation function has detected that the value is
        not consitent with other values. Typically set by a network
        State Estimator.
    :ivar test: Measurement value is transmitted for test purposes.
    :ivar validity: Validity of the measurement value.
    """
    bad_reference: Optional[bool] = field(
        default=None,
        metadata={
            "name": "badReference",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    estimator_replaced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "estimatorReplaced",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failure: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    old_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oldData",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operator_blocked: Optional[bool] = field(
        default=None,
        metadata={
            "name": "operatorBlocked",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    oscillatory: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    out_of_range: Optional[bool] = field(
        default=None,
        metadata={
            "name": "outOfRange",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    over_flow: Optional[bool] = field(
        default=None,
        metadata={
            "name": "overFlow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    suspect: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class RatioTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the ratio tap changer tabular curve.

    :ivar ratio_tap_changer_table: Table of this point.
    """
    ratio_tap_changer_table: Optional["RatioTapChangerTable"] = field(
        default=None,
        metadata={
            "name": "RatioTapChangerTable",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class RelativeDisplacement:
    """
    Vertical displacement relative to either sealevel, ground or the centre of
    the earth.
    """
    displacement: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    kind: Optional[RelativeDisplacementKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ReportingCapability:
    """&lt;font color="#0f0f0f"&gt;Definition of one set of reporting
    capabilities for this monitoring station.

    The associated EnvironmentalValueSets describe the maximum range of
    possible environmental values the station is capable of returning
    via relationships with non-populated AnalogValue child instances.
    This attribute is intended primarily to assist a utility in managing
    its stations. &lt;/font&gt;

    :ivar reporting_interval_period: Number of units of time making up
        reporting period.
    :ivar reporting_method: Indicates how the weather station reports
        observations.
    :ivar environmental_analog: One of the environmental value sets
        expressing one of the reporting capabilities.
    """
    reporting_interval_period: Optional[int] = field(
        default=None,
        metadata={
            "name": "reportingIntervalPeriod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reporting_method: Optional[ReportingMethodKind] = field(
        default=None,
        metadata={
            "name": "reportingMethod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_analog: List["EnvironmentalAnalog"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalAnalog",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class StreetAddress:
    """
    General purpose street and postal address information.

    :ivar po_box: Post office box.
    :ivar postal_code: Postal code for the address.
    :ivar status: Status of this address.
    :ivar street_detail: Street detail.
    :ivar town_detail: Town detail.
    """
    po_box: Optional[str] = field(
        default=None,
        metadata={
            "name": "poBox",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    street_detail: Optional[StreetDetail] = field(
        default=None,
        metadata={
            "name": "streetDetail",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    town_detail: Optional[TownDetail] = field(
        default=None,
        metadata={
            "name": "townDetail",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sections: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shunt_compensator: Optional["ShuntCompensator"] = field(
        default=None,
        metadata={
            "name": "ShuntCompensator",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SvStatus(StateVariable):
    """
    State variable for status.

    :ivar in_service: The in service status as a result of topology
        processing.
    :ivar phase: The individual phase status.    If the attribute is
        unspecified, then three phase model is assumed.
    :ivar conducting_equipment: The conducting equipment associated with
        the status state variable.
    """
    in_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inService",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    conducting_equipment: Optional["ConductingEquipment"] = field(
        default=None,
        metadata={
            "name": "ConductingEquipment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SvSwitch(StateVariable):
    """
    State variable for switch.

    :ivar open: The attribute tells if the computed state of the switch
        is considered open.
    :ivar phase: The terminal phase at which the connection is applied.
        If missing, the injection is assumed to be balanced among non-
        neutral phases.
    :ivar switch: The switch associated with the switch state.
    """
    open: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    switch: Optional["Switch"] = field(
        default=None,
        metadata={
            "name": "Switch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tap_changer: Optional["TapChanger"] = field(
        default=None,
        metadata={
            "name": "TapChanger",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    v: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    connectivity_node: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    topological_node: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Tappistandard:
    """
    Standard published by TAPPI.

    :ivar standard_edition: Edition of TAPPI standard.
    :ivar standard_number: TAPPI standard number.
    """
    class Meta:
        name = "TAPPIStandard"

    standard_edition: Optional[TappistandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[TappistandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class UkministryOfDefenceStandard:
    """
    Standard published by United Kingdom Ministry of Defence.

    :ivar standard_edition: Edition of UK Ministry of Defence standard.
    :ivar standard_number: UK Ministry of Defence standard number.
    """
    class Meta:
        name = "UKMinistryOfDefenceStandard"

    standard_edition: Optional[UkministryOfDefenceStandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[UkministryofDefenceStandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Wepstandard:
    """Standard published by Westinghouse - a WEP (Westinghouse Engineering Procedure).

    :ivar standard_edition: Edition of WEP standard.
    :ivar standard_number: WEP standard number.
    """
    class Meta:
        name = "WEPStandard"

    standard_edition: Optional[WepstandardEditionKind] = field(
        default=None,
        metadata={
            "name": "standardEdition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    standard_number: Optional[WepstandardKind] = field(
        default=None,
        metadata={
            "name": "standardNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_yvalue: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxYValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_yvalue: Optional[float] = field(
        default=None,
        metadata={
            "name": "minYValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominal_yvalue: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalYValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dermonitorable_parameter: Optional["DermonitorableParameter"] = field(
        default=None,
        metadata={
            "name": "DERMonitorableParameter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dispatch_schedule: Optional[DispatchSchedule] = field(
        default=None,
        metadata={
            "name": "DispatchSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_event: Optional["EndDeviceEvent"] = field(
        default=None,
        metadata={
            "name": "EndDeviceEvent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[StringQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class MeasurementValueQuality(Quality61850):
    """Measurement quality flags.

    Bits 0-10 are defined for substation automation in draft IEC 61850
    part 7-3. Bits 11-15 are reserved for future expansion by that
    document. Bits 16-31 are reserved for EMS applications.

    :ivar measurement_value: A MeasurementValue has a
        MeasurementValueQuality associated with it.
    """
    measurement_value: Optional["MeasurementValue"] = field(
        default=None,
        metadata={
            "name": "MeasurementValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar name_type: Type of this name.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    identified_object: Optional["IdentifiedObject"] = field(
        default=None,
        metadata={
            "name": "IdentifiedObject",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    name_type: Optional[NameType] = field(
        default=None,
        metadata={
            "name": "NameType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SvEstVoltage(SvVoltage):
    angle_variance: Optional[object] = field(
        default=None,
        metadata={
            "name": "angleVariance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    v_variance: Optional[object] = field(
        default=None,
        metadata={
            "name": "vVariance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    estimate: Optional["Estimate"] = field(
        default=None,
        metadata={
            "name": "Estimate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class UserAttribute:
    """
    Generic name-value pair class, with optional sequence number and units for
    value; can be used to model parts of information exchange when concrete
    types are not known in advance.

    :ivar name: Name of an attribute.
    :ivar sequence_number: Sequence number for this attribute in a list
        of attributes.
    :ivar procedure_data_sets:
    :ivar value: Value of an attribute, including unit information.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    procedure_data_sets: List["ProcedureDataSet"] = field(
        default_factory=list,
        metadata={
            "name": "ProcedureDataSets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[StringQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    flow_direction: Optional[FlowDirectionKind] = field(
        default=None,
        metadata={
            "name": "flowDirection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    y_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "yMultiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y_unit: Optional[DerunitSymbol] = field(
        default=None,
        metadata={
            "name": "yUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y_unit_installed_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "yUnitInstalledMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y_unit_installed_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "yUnitInstalledMin",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dercurve_data: Optional[DercurveData] = field(
        default=None,
        metadata={
            "name": "DERCurveData",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dispatch_schedule: List[DispatchSchedule] = field(
        default_factory=list,
        metadata={
            "name": "DispatchSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_group: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Estimate:
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_est_voltages: List[SvEstVoltage] = field(
        default_factory=list,
        metadata={
            "name": "SvEstVoltages",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    alias_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "aliasName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    names: List[Name] = field(
        default_factory=list,
        metadata={
            "name": "Names",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Appointment(IdentifiedObject):
    """
    Meeting time and location.

    :ivar call_ahead: True if requested to call customer when someone is
        about to arrive at their premises.
    :ivar meeting_interval: Date and time reserved for appointment.
    :ivar persons: All persons for this appointment.
    """
    call_ahead: Optional[bool] = field(
        default=None,
        metadata={
            "name": "callAhead",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meeting_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "meetingInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    persons: List["PersonRole"] = field(
        default_factory=list,
        metadata={
            "name": "Persons",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetDeployment(IdentifiedObject):
    """
    Deployment of asset deployment in a power system resource role.

    :ivar breaker_application: Type of network role breaker is playing
        in this deployment (applies to breaker assets only).
    :ivar deployment_state: Current deployment state of asset.
    :ivar facility_kind: Kind of facility (like substation or pole or
        building or plant or service center) at which asset deployed.
    :ivar likelihood_of_failure: Likelihood of asset failure on a scale
        of 1(low) to 100 (high).
    :ivar transformer_application: Type of network role transformer is
        playing in this deployment (applies to transformer assets only).
    :ivar asset: Asset in this deployment.
    :ivar base_voltage: Base voltage of this network asset deployment.
    :ivar deployment_date: Dates of asset deployment.
    """
    breaker_application: Optional[BreakerApplicationKind] = field(
        default=None,
        metadata={
            "name": "breakerApplication",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    deployment_state: Optional[DeploymentStateKind] = field(
        default=None,
        metadata={
            "name": "deploymentState",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    facility_kind: Optional[FacilityKind] = field(
        default=None,
        metadata={
            "name": "facilityKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    likelihood_of_failure: Optional[int] = field(
        default=None,
        metadata={
            "name": "likelihoodOfFailure",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_application: Optional[TransformerApplicationKind] = field(
        default=None,
        metadata={
            "name": "transformerApplication",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    base_voltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "name": "BaseVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    deployment_date: Optional[DeploymentDate] = field(
        default=None,
        metadata={
            "name": "deploymentDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    firmware_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "firmwareID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hardware_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "hardwareID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    program_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "programID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BaseFrequency(IdentifiedObject):
    """The class describe a base frequency for a power system network.

    In case of multiple power networks with different frequencies, e.g.
    50 or 60 Hertz each network will have it's own base frequency class.
    Hence it is assumed that power system objects having different base
    frequencies appear in separate documents where each document has a
    single base frequency instance.

    :ivar frequency: The base frequency.
    """
    frequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BasePower(IdentifiedObject):
    """
    The BasePower class defines the base power used in the per unit
    calculations.

    :ivar base_power: Value used as base power.
    """
    base_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "basePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value1_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "value1Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value1_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "value1Unit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value2_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "value2Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value2_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "value2Unit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BranchGroup(IdentifiedObject):
    """A group of branch terminals whose directed flow summation is to be
    monitored.

    A branch group need not form a cutset of the network.

    :ivar maximum_active_power: The maximum active power flow.
    :ivar maximum_reactive_power: The maximum reactive power flow.
    :ivar minimum_active_power: The minimum active power flow.
    :ivar minimum_reactive_power: The minimum reactive power flow.
    :ivar monitor_active_power: Monitor the active power flow.
    :ivar monitor_reactive_power: Monitor the reactive power flow.
    :ivar branch_group_terminal:
    """
    maximum_active_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumActivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maximum_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimum_active_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumActivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimum_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    monitor_active_power: Optional[bool] = field(
        default=None,
        metadata={
            "name": "monitorActivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    monitor_reactive_power: Optional[bool] = field(
        default=None,
        metadata={
            "name": "monitorReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    branch_group_terminal: List["BranchGroupTerminal"] = field(
        default_factory=list,
        metadata={
            "name": "BranchGroupTerminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CimGridAppsDRc42021:
    class Meta:
        name = "CIM_GridAPPS-D_RC4_2021"
        namespace = "http://iec.ch/TC57/CIM100#"

    identified_object: List[IdentifiedObject] = field(
        default_factory=list,
        metadata={
            "name": "IdentifiedObject",
            "type": "Element",
        }
    )


@dataclass
class CatalogAssetType(IdentifiedObject):
    """
    assets that may be used for planning, work or design purposes.

    :ivar estimated_unit_cost: Estimated unit cost (or cost per unit
        length) of this type of asset. It does not include labor to
        install, construct or configure it.
    :ivar kind:
    :ivar stock_item: True if item is a stock item (default).
    :ivar type:
    :ivar asset_info:
    :ivar product_asset_model:
    :ivar quantity: The value, unit of measure, and multiplier for the
        quantity.
    """
    estimated_unit_cost: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "estimatedUnitCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    kind: Optional[AssetKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    stock_item: Optional[bool] = field(
        default=None,
        metadata={
            "name": "stockItem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_info: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "name": "AssetInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    product_asset_model: List["ProductAssetModel"] = field(
        default_factory=list,
        metadata={
            "name": "ProductAssetModel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    quantity: Optional[StringQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    locations: List["Location"] = field(
        default_factory=list,
        metadata={
            "name": "Locations",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CrewType(IdentifiedObject):
    """Custom description of the type of crew.

    This may be used to determine the type of work the crew can be
    assigned to. Examples include repair, tree trimming, switching, etc.

    :ivar crews: All crews of this type.
    """
    crews: List["Crew"] = field(
        default_factory=list,
        metadata={
            "name": "Crews",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "xMultiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "xUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y1_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "y1Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y1_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "y1Unit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y2_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "y2Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y2_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "y2Unit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y3_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "y3Multiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y3_unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "y3Unit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    curve_datas: List[CurveData] = field(
        default_factory=list,
        metadata={
            "name": "CurveDatas",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_group: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Document(IdentifiedObject):
    """Parent class for different groupings of information collected and
    managed as a part of a business process.

    It will frequently contain references to other objects, such as
    assets, people and power system resources.

    :ivar author_name: Name of the author of this document.
    :ivar comment: Free text comment.
    :ivar created_date_time: Date and time that this document was
        created.
    :ivar last_modified_date_time: Date and time this document was last
        modified. Documents may potentially be modified many times
        during their lifetime.
    :ivar revision_number: Revision number for this document.
    :ivar subject: Document subject.
    :ivar title: Document title.
    :ivar type: Utility-specific classification of this document,
        according to its corporate standards, practices, and existing IT
        systems (e.g., for management of assets, maintenance, work,
        outage, customers, etc.).
    :ivar approver: Approver of this document.
    :ivar author: Author of this document.
    :ivar configuration_events: All configuration events created for
        this document.
    :ivar doc_status: Status of this document. For status of subject
        matter this document represents (e.g., Agreement, Work), use
        'status' attribute. Example values for 'docStatus.status' are
        draft, approved, cancelled, etc.
    :ivar editor: Editor of this document.
    :ivar electronic_address: Electronic address.
    :ivar issuer: Issuer of this document.
    :ivar status: Status of subject matter (e.g., Agreement, Work) this
        document represents. For status of the document itself, use
        'docStatus' attribute.
    """
    author_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "authorName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    created_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    last_modified_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastModifiedDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    subject: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    approver: Optional["Approver"] = field(
        default=None,
        metadata={
            "name": "Approver",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    author: Optional["Author"] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    configuration_events: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    doc_status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "docStatus",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    editor: Optional["Editor"] = field(
        default=None,
        metadata={
            "name": "Editor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    electronic_address: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "name": "electronicAddress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    issuer: Optional["Issuer"] = field(
        default=None,
        metadata={
            "name": "Issuer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    event_or_action: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventOrAction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sub_domain: Optional[str] = field(
        default=None,
        metadata={
            "name": "subDomain",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_controls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    event_or_action: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventOrAction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sub_domain: Optional[str] = field(
        default=None,
        metadata={
            "name": "subDomain",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_events: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnergyArea(IdentifiedObject):
    """Describes an area having energy production or consumption.

    Specializations are intended to support the load allocation function
    as typically required in energy management systems or planning
    studies to allocate hypothesized load levels to individual load
    points for power flow analysis.  Often the energy area can be linked
    to both measured and forecast load levels.
    """


@dataclass
class FaultCauseType(IdentifiedObject):
    """
    Type of cause of the fault.

    :ivar configuration_event:
    :ivar faults: All faults with this cause type.
    """
    configuration_event: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    faults: List["Fault"] = field(
        default_factory=list,
        metadata={
            "name": "Faults",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FieldDispatchHistory(IdentifiedObject):
    """
    The history of field dispatch statuses for this work.
    """
    crew: Optional["Crew"] = field(
        default=None,
        metadata={
            "name": "Crew",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    field_dispatch_step: List[FieldDispatchStep] = field(
        default_factory=list,
        metadata={
            "name": "FieldDispatchStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FinancialInfo(IdentifiedObject):
    """Various current financial properties associated with a particular asset.

    Historical properties may be determined by ActivityRecords
    associated with the asset.

    :ivar account: The account to which this actual material item is
        charged.
    :ivar actual_purchase_cost: The actual purchase cost of this
        particular asset.
    :ivar cost_description: Description of the cost.
    :ivar cost_type: Type of cost to which this Material Item belongs.
    :ivar financial_value: Value of asset as of 'valueDateTime'.
    :ivar plant_transfer_date_time: Date and time asset's financial
        value was put in plant for regulatory accounting purposes (e.g.,
        for rate base calculations). This is sometime referred to as the
        "in-service date".
    :ivar purchase_date_time: Date and time asset was purchased.
    :ivar purchase_order_number: Purchase order identifier.
    :ivar value_date_time: Date and time at which the financial value
        was last established.
    :ivar warranty_end_date_time: Date and time warranty on asset
        expires.
    :ivar asset:
    :ivar quantity: The quantity of the asset if per unit length, for
        example conductor.
    """
    account: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    actual_purchase_cost: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "actualPurchaseCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cost_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "costDescription",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cost_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "costType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    financial_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "financialValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    plant_transfer_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "plantTransferDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    purchase_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "purchaseDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    purchase_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "purchaseOrderNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "valueDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    warranty_end_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "warrantyEndDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    quantity: Optional[IntegerQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Hazard(IdentifiedObject):
    """
    An object or a condition that is a danger for causing loss or perils to an
    asset and/or people.

    :ivar type: Type of this hazard.
    :ivar status: Status of this hazard.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
class Limit(IdentifiedObject):
    """Specifies one limit value for a Measurement.

    A Measurement typically has several limits that are kept together by
    the LimitSet class. The actual meaning and use of a Limit instance
    (i.e., if it is an alarm or warning limit or if it is a high or low
    limit) is not captured in the Limit class. However the name of a
    Limit instance may indicate both meaning and use.
    """
    procedures: List["Procedure"] = field(
        default_factory=list,
        metadata={
            "name": "Procedures",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class LimitSet(IdentifiedObject):
    """Specifies a set of Limits that are associated with a Measurement.

    A Measurement may have several LimitSets corresponding to seasonal
    or other changing conditions. The condition is captured in the name
    and description attributes. The same LimitSet may be used for
    several Measurements. In particular percentage limits are used this
    way.

    :ivar is_percentage_limits: Tells if the limit values are in
        percentage of normalValue or the specified Unit for Measurements
        and Controls.
    """
    is_percentage_limits: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPercentageLimits",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    p_constant_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "pConstantCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    p_constant_impedance: Optional[float] = field(
        default=None,
        metadata={
            "name": "pConstantImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    p_constant_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "pConstantPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    p_voltage_exponent: Optional[float] = field(
        default=None,
        metadata={
            "name": "pVoltageExponent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q_constant_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "qConstantCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q_constant_impedance: Optional[float] = field(
        default=None,
        metadata={
            "name": "qConstantImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q_constant_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "qConstantPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q_voltage_exponent: Optional[float] = field(
        default=None,
        metadata={
            "name": "qVoltageExponent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energy_consumer: List["EnergyConsumer"] = field(
        default_factory=list,
        metadata={
            "name": "EnergyConsumer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class MeasurementValueSource(IdentifiedObject):
    """MeasurementValueSource describes the alternative sources updating a
    MeasurementValue.

    User conventions for how to use the MeasurementValueSource
    attributes are described in the introduction to IEC 61970-301.

    :ivar measurement_values: The MeasurementValues updated by the
        source.
    """
    measurement_values: List["MeasurementValue"] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementValues",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Medium(IdentifiedObject):
    """
    A substance that either (1) provides the means of transmission of a force
    or effect, such as hydraulic fluid, or (2) is used for a surrounding or
    enveloping substance, such as oil in a transformer or circuit breaker.

    :ivar kind: Kind of this medium.
    :ivar volume_spec: The volume of the medium specified for this
        application. Note that the actual volume is a type of
        measurement associated witht the asset.
    :ivar asset:
    """
    kind: Optional[MediumKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volume_spec: Optional[float] = field(
        default=None,
        metadata={
            "name": "volumeSpec",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class MeterMultiplier(IdentifiedObject):
    """
    Multiplier applied at the meter.

    :ivar kind: Kind of multiplier.
    :ivar value: Multiplier value.
    :ivar meter: Meter applying this multiplier.
    """
    kind: Optional[MeterMultiplierKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter: Optional["Meter"] = field(
        default=None,
        metadata={
            "name": "Meter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class MetrologyRequirement(IdentifiedObject):
    """
    A specification of the metering requirements for a particular point within
    a network.

    :ivar reason: Reason for this metrology requirement being specified.
    :ivar reading_types: All reading types required to be collected by
        this metrology requirement.
    :ivar usage_points: All usage points having this metrology
        requirement.
    """
    reason: Optional[ReadingReasonKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reading_types: List["ReadingType"] = field(
        default_factory=list,
        metadata={
            "name": "ReadingTypes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class MutualCoupling(IdentifiedObject):
    """
    This class represents the zero sequence line mutual coupling.

    :ivar b0ch: Zero sequence mutual coupling shunt (charging)
        susceptance, uniformly distributed, of the entire line section.
    :ivar distance11: Distance to the start of the coupled region from
        the first line's terminal having sequence number equal to 1.
    :ivar distance12: Distance to the end of the coupled region from the
        first line's terminal with sequence number equal to 1.
    :ivar distance21: Distance to the start of coupled region from the
        second line's terminal with sequence number equal to 1.
    :ivar distance22: Distance to the end of coupled region from the
        second line's terminal with sequence number equal to 1.
    :ivar g0ch: Zero sequence mutual coupling shunt (charging)
        conductance, uniformly distributed, of the entire line section.
    :ivar r0: Zero sequence branch-to-branch mutual impedance coupling,
        resistance.
    :ivar x0: Zero sequence branch-to-branch mutual impedance coupling,
        reactance.
    :ivar first_terminal: The starting terminal for the calculation of
        distances along the first branch of the mutual coupling.
        Normally MutualCoupling would only be used for terminals of AC
        line segments.  The first and second terminals of a mutual
        coupling should point to different AC line segments.
    :ivar second_terminal: The starting terminal for the calculation of
        distances along the second branch of the mutual coupling.
    """
    b0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    distance11: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    distance12: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    distance21: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    distance22: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    first_terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "First_Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    second_terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Second_Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class NamedPhenomenon(IdentifiedObject):
    """
    Supports designating multiple environmental phenomenon (in different
    Observations or Forecasts) as all related to the same identified phenomenon
    (a specific hurricane or tornado or flood, or example).

    :ivar environmental_phenomenon: An occurence of an environmental
        phenomenon associated with this identified phenomenon.
    """
    environmental_phenomenon: List["EnvironmentalPhenomenon"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalPhenomenon",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OperatingParticipant(IdentifiedObject):
    """An operator of multiple power system resource objects.

    Note multple operating participants may operate the same power
    system resource object.   This can be used for modeling jointly
    owned units where each owner operates as a contractual share.

    :ivar operating_share: The operating shares of this operating
        participant.  An operating participant can be resused for any
        number of power system resources.
    """
    operating_share: List["OperatingShare"] = field(
        default_factory=list,
        metadata={
            "name": "OperatingShare",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    direction: Optional[OperationalLimitDirectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operational_limit: List["OperationalLimit"] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Organisation(IdentifiedObject):
    """
    Organisation that might have roles as utility, contractor, supplier,
    manufacturer, customer, etc.

    :ivar electronic_address: Electronic address.
    :ivar parent_organisation: Parent organisation of this organisation.
    :ivar phone1: Phone number.
    :ivar phone2: Additional phone number.
    :ivar postal_address: Postal address, potentially different than
        'streetAddress' (e.g., another city).
    :ivar roles: All roles of this organisation.
    :ivar street_address: Street address.
    """
    electronic_address: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "name": "electronicAddress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    parent_organisation: Optional["ParentOrganization"] = field(
        default=None,
        metadata={
            "name": "ParentOrganisation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phone1: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phone2: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    postal_address: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "name": "postalAddress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    roles: List["OrganisationRole"] = field(
        default_factory=list,
        metadata={
            "name": "Roles",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    street_address: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "name": "streetAddress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Psrtype(IdentifiedObject):
    """Classifying instances of the same class, e.g. overhead and underground
    ACLineSegments.

    This classification mechanism is intended to provide flexibility
    outside the scope of this standard, i.e. provide customisation that
    is non standard.

    :ivar power_system_resources: Power system resources classified with
        this power system resource type.
    """
    class Meta:
        name = "PSRType"

    power_system_resources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "name": "PowerSystemResources",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Person(IdentifiedObject):
    """
    General purpose information for name and other information to contact
    people.

    :ivar first_name: Person's first name.
    :ivar last_name: Person's last (family, sir) name.
    :ivar m_name: Middle name(s) or initial(s).
    :ivar prefix: A prefix or title for the person's name, such as Miss,
        Mister, Doctor, etc.
    :ivar special_need: Special service needs for the person (contact)
        are described; examples include life support, etc.
    :ivar suffix: A suffix for the person's name, such as II, III, etc.
    :ivar electronic_address: Electronic address.
    :ivar landline_phone: Landline phone number.
    :ivar mobile_phone: Mobile phone number.
    :ivar roles: All roles of this person.
    """
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    m_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "mName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    special_need: Optional[str] = field(
        default=None,
        metadata={
            "name": "specialNeed",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    electronic_address: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "name": "electronicAddress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    landline_phone: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "name": "landlinePhone",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mobile_phone: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "name": "mobilePhone",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    roles: List["PersonRole"] = field(
        default_factory=list,
        metadata={
            "name": "Roles",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class RatioTapChangerTable(IdentifiedObject):
    """
    Describes a curve for how the voltage magnitude and impedance varies with
    the tap step.

    :ivar ratio_tap_changer: The ratio tap changer of this tap ratio
        table.
    :ivar ratio_tap_changer_table_point: Points of this table.
    """
    ratio_tap_changer: List["RatioTapChanger"] = field(
        default_factory=list,
        metadata={
            "name": "RatioTapChanger",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratio_tap_changer_table_point: List[RatioTapChangerTablePoint] = field(
        default_factory=list,
        metadata={
            "name": "RatioTapChangerTablePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class ReadingQualityType(IdentifiedObject):
    """Detailed description for a quality of a reading value, produced by an
    end device or a system.

    Values in attributes allow for creation of the recommended codes to be used for identifying reading value quality codes as follows: &amp;lt;systemId&amp;gt;.&amp;lt;category&amp;gt;.&amp;lt;subCategory&amp;gt;.

    :ivar category: High-level nature of the reading value quality.
    :ivar sub_category: More specific nature of the reading value
        quality, as a further sub-categorisation of 'category'.
    :ivar system_id: Identification of the system which has declared the
        issue with the data or provided commentary on the data.
    :ivar reading_qualities: All reading qualities of this type.
    """
    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sub_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "subCategory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "systemId",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reading_qualities: List["ReadingQuality"] = field(
        default_factory=list,
        metadata={
            "name": "ReadingQualities",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ReportingSuperGroup(IdentifiedObject):
    """
    A reporting super group, groups reporting groups for a higher level report.
    """
    reporting_group: List["ReportingGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ReportingGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class RightOfWay(IdentifiedObject):
    parallel_line_segments: List["ParallelLineSegment"] = field(
        default_factory=list,
        metadata={
            "name": "ParallelLineSegments",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class Seal(IdentifiedObject):
    """
    Physically controls access to AssetContainers.

    :ivar applied_date_time: Date and time this seal has been applied.
    :ivar condition: Condition of seal.
    :ivar kind: Kind of seal.
    :ivar seal_number: (reserved word) Seal number.
    :ivar asset_container: Asset container to which this seal is
        applied.
    """
    applied_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "appliedDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    condition: Optional[SealConditionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    kind: Optional[SealKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    seal_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "sealNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_container: Optional["AssetContainer"] = field(
        default=None,
        metadata={
            "name": "AssetContainer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    start_date: Optional[object] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    season_day_type_schedules: List["SeasonDayTypeSchedule"] = field(
        default_factory=list,
        metadata={
            "name": "SeasonDayTypeSchedules",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ServiceCategory(IdentifiedObject):
    """
    Category of service provided to the customer.

    :ivar kind: Kind of service.
    :ivar configuration_events: All configuration events created for
        this service category.
    :ivar customer_agreements: All customer agreements with this service
        category.
    :ivar pricing_structures: All pricing structures applicable to this
        service category.
    :ivar usage_points: All usage points that deliver this category of
        service.
    """
    kind: Optional[ServiceKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    configuration_events: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_agreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAgreements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pricing_structures: List["PricingStructure"] = field(
        default_factory=list,
        metadata={
            "name": "PricingStructures",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ServiceMultiplier(IdentifiedObject):
    """
    Multiplier applied at the usage point.

    :ivar kind: Kind of multiplier.
    :ivar value: Multiplier value.
    :ivar usage_point: Usage point applying this multiplier.
    """
    kind: Optional[ServiceMultiplierKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_point: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "name": "UsagePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class SwitchOperationSummary(IdentifiedObject):
    """
    Up-to-date, of-record summary of switch operation information, distilled
    from a variety of sources (real-time data or real-time data historian,
    field inspections, etc.) of use to asset health analytics.

    :ivar lifetime_fault_operations: Total breaker fault operations to
        date.
    :ivar lifetime_motor_starts: Total motor starts to date.
    :ivar lifetime_total_operations: Total breaker operations to date
        (including fault and non-fault).
    :ivar most_recent_fault_operation_date: Date of most recent breaker
        fault operation.
    :ivar most_recent_motor_start_date: Date of most recent motor start.
    :ivar most_recent_operation_date: Date of most recent breaker
        operation (fault or non-fault).
    :ivar breaker: Breaker asset to which this operation information
        applies.
    """
    lifetime_fault_operations: Optional[int] = field(
        default=None,
        metadata={
            "name": "lifetimeFaultOperations",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lifetime_motor_starts: Optional[int] = field(
        default=None,
        metadata={
            "name": "lifetimeMotorStarts",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lifetime_total_operations: Optional[int] = field(
        default=None,
        metadata={
            "name": "lifetimeTotalOperations",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    most_recent_fault_operation_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "mostRecentFaultOperationDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    most_recent_motor_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "mostRecentMotorStartDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    most_recent_operation_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "mostRecentOperationDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    breaker: Optional["Asset"] = field(
        default=None,
        metadata={
            "name": "Breaker",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TestStandard(IdentifiedObject):
    """
    The precise standard used in executing a lab test, including the standard,
    and standard version, test method and variant, if needed.

    :ivar test_method: Identification of test method used if multiple
        methods specified by test standard.
    :ivar test_variant: Identification of variant of test method or
        standard if one is specified by the standard.
    :ivar test_standard_astm: Which ASTM standard used to determine
        analog value result. Applies only if ASTM standard used.
    :ivar test_standard_cigre: Which CIGRE standard used to determine
        analog value result. Applies only if CIGRE standard used.
    :ivar test_standard_din: Which DIN standard used to determine analog
        value result. Applies only if DIN standard used.
    :ivar test_standard_doble: Which Doble standard used to determine
        analog value result. Applies only if Doble standard used.
    :ivar test_standard_epa: Which EPA standard used to determine analog
        value result. Applies only if EPA standard used.
    :ivar test_standard_iec: Which IEC standard used to determine analog
        value result. Applies only if IEC standard used.
    :ivar test_standard_ieee: Which IEEE standard used to determine
        analog value result. Applies only if IEEE standard used.
    :ivar test_standard_iso: Which ISO standard used to determine analog
        value result. Applies only if ISO standard used.
    :ivar test_standard_laborelec: Which Laborelec standard used to
        determine analog value result. Applies only if Laborelec
        standard used.
    :ivar test_standard_tappi: Which TAPPI standard used to determine
        analog value result. Applies only if TAPPI standard used.
    :ivar test_standard_ukministry_of_defence: Which UK Ministry of
        Defence standard used to determine analog value result. Applies
        only if UK Ministry of Defence standard used.
    :ivar test_standard_wep: Which WEP standard used to determine analog
        value result. Applies only if WEP standard used.
    """
    test_method: Optional[TestMethod] = field(
        default=None,
        metadata={
            "name": "testMethod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_variant: Optional[TestVariantKind] = field(
        default=None,
        metadata={
            "name": "testVariant",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_astm: Optional[Astmstandard] = field(
        default=None,
        metadata={
            "name": "testStandardASTM",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_cigre: Optional[Cigrestandard] = field(
        default=None,
        metadata={
            "name": "testStandardCIGRE",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_din: Optional[Dinstandard] = field(
        default=None,
        metadata={
            "name": "testStandardDIN",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_doble: Optional[DobleStandard] = field(
        default=None,
        metadata={
            "name": "testStandardDoble",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_epa: Optional[Epastandard] = field(
        default=None,
        metadata={
            "name": "testStandardEPA",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_iec: Optional[Iecstandard] = field(
        default=None,
        metadata={
            "name": "testStandardIEC",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_ieee: Optional[Ieeestandard] = field(
        default=None,
        metadata={
            "name": "testStandardIEEE",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_iso: Optional[Isostandard] = field(
        default=None,
        metadata={
            "name": "testStandardISO",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_laborelec: Optional[LaborelecStandard] = field(
        default=None,
        metadata={
            "name": "testStandardLaborelec",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_tappi: Optional[Tappistandard] = field(
        default=None,
        metadata={
            "name": "testStandardTAPPI",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_ukministry_of_defence: Optional[UkministryOfDefenceStandard] = field(
        default=None,
        metadata={
            "name": "testStandardUKMinistryOfDefence",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_standard_wep: Optional[Wepstandard] = field(
        default=None,
        metadata={
            "name": "testStandardWEP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    base_setpoint: Optional[float] = field(
        default=None,
        metadata={
            "name": "baseSetpoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    control_mode: Optional[ThermostatControlMode] = field(
        default=None,
        metadata={
            "name": "controlMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    price_cap: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "priceCap",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ramp_high: Optional[float] = field(
        default=None,
        metadata={
            "name": "rampHigh",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ramp_low: Optional[float] = field(
        default=None,
        metadata={
            "name": "rampLow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    range_high: Optional[float] = field(
        default=None,
        metadata={
            "name": "rangeHigh",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    range_low: Optional[float] = field(
        default=None,
        metadata={
            "name": "rangeLow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    use_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "useOverride",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    use_predictive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "usePredictive",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    house: Optional["House"] = field(
        default=None,
        metadata={
            "name": "House",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TopologicalIsland(IdentifiedObject):
    """An electrically connected subset of the network. Topological islands can
    change as the current network state changes: e.g. due to.

    - disconnect switches or breakers change state in a SCADA/EMS
    - manual creation, change or deletion of topological nodes in a planning tool.

    :ivar angle_ref_topological_node: The angle reference for the
        island.   Normally there is one TopologicalNode that is selected
        as the angle reference for each island.   Other reference
        schemes exist, so the association is typically optional.
    :ivar topological_nodes: A topological node belongs to a topological
        island.
    """
    angle_ref_topological_node: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "name": "AngleRefTopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    topological_nodes: List["TopologicalNode"] = field(
        default_factory=list,
        metadata={
            "name": "TopologicalNodes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    b0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_end: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "name": "TransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_end_info: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "TransformerEndInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    from_transformer_end: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
            "name": "FromTransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    from_transformer_end_info: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "FromTransformerEndInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    to_transformer_end: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "name": "ToTransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    to_transformer_end_infos: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "name": "ToTransformerEndInfos",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class TransformerStarImpedance(IdentifiedObject):
    """Transformer star impedance (Pi-model) that accurately reflects impedance
    for transformers with 2 or 3 windings.

    For transformers with 4 or more windings, you must use
    TransformerMeshImpedance class. For transmission networks use
    PowerTransformerEnd impedances (r, r0, x, x0, b, b0, g and g0).

    :ivar r: Resistance of the transformer end.
    :ivar r0: Zero sequence series resistance of the transformer end.
    :ivar x: Positive sequence series reactance of the transformer end.
    :ivar x0: Zero sequence series reactance of the transformer end.
    :ivar transformer_end: All transformer ends having this star
        impedance.
    :ivar transformer_end_info: Transformer end datasheet used to
        calculate this transformer star impedance.
    """
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_end: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "name": "TransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_end_info: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "TransformerEndInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    temperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ValueToAlias(IdentifiedObject):
    """
    Describes the translation of one particular value into a name, e.g. 1 as
    "Open".

    :ivar value: The value that is mapped.
    :ivar value_alias_set: The ValueAliasSet having the ValueToAlias
        mappings.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value_alias_set: Optional["ValueAliasSet"] = field(
        default=None,
        metadata={
            "name": "ValueAliasSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_coord: Optional[float] = field(
        default=None,
        metadata={
            "name": "xCoord",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y_coord: Optional[float] = field(
        default=None,
        metadata={
            "name": "yCoord",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_phase_info: List["WirePhaseInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WirePhaseInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_spacing_info: Optional["WireSpacingInfo"] = field(
        default=None,
        metadata={
            "name": "WireSpacingInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AccumulatorLimit(Limit):
    """
    Limit values for Accumulator measurements.

    :ivar value: The value to supervise against. The value is positive.
    :ivar limit_set: The set of limits.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    limit_set: Optional["AccumulatorLimitSet"] = field(
        default=None,
        metadata={
            "name": "LimitSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Agreement(Document):
    """Formal agreement between two parties defining the terms and conditions
    for a set of services.

    The specifics of the services are, in turn, defined via one or more
    service agreements.

    :ivar sign_date: Date this agreement was consummated among
        associated persons and/or organisations.
    :ivar validity_interval: Date and time interval this agreement is
        valid (from going into effect to termination).
    """
    sign_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "signDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    validity_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "validityInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AnalogLimit(Limit):
    """
    Limit values for Analog measurements.

    :ivar value: The value to supervise against.
    :ivar limit_set: The set of limits.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    limit_set: Optional["AnalogLimitSet"] = field(
        default=None,
        metadata={
            "name": "LimitSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class AssetGroup(Document):
    """
    A grouping of assets created for a purpose such as fleet analytics,
    inventory or compliance management.

    :ivar kind: Kind of asset group this asset group is.
    :ivar analytic:
    :ivar analytic_score:
    :ivar asset:
    """
    kind: Optional[AssetGroupKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    analytic: List["Analytic"] = field(
        default_factory=list,
        metadata={
            "name": "Analytic",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    analytic_score: List["AnalyticScore"] = field(
        default_factory=list,
        metadata={
            "name": "AnalyticScore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetLocationHazard(Hazard):
    """Potential hazard related to the location of an asset.

    Examples are trees growing under overhead power lines, a park being
    located by a substation (i.e., children climb fence to recover a
    ball), a lake near an overhead distribution line (fishing pole/line
    contacting power lines), dangerous neighbour, etc.

    :ivar kind: Kind of hazard.
    :ivar locations: The location of this hazard.
    """
    kind: Optional[AssetHazardKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    locations: List["Location"] = field(
        default_factory=list,
        metadata={
            "name": "Locations",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BranchGroupTerminal:
    """
    A specific directed terminal flow for a branch group.

    :ivar positive_flow_in: The flow into the terminal is summed if set
        true.   The flow out of the terminanl is summed if set false.
    :ivar branch_group:
    :ivar terminal: The terminal to be summed.
    """
    positive_flow_in: Optional[bool] = field(
        default=None,
        metadata={
            "name": "positiveFlowIn",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    branch_group: Optional[BranchGroup] = field(
        default=None,
        metadata={
            "name": "BranchGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar operation_in_progress: Indicates that a client is currently
        sending control commands that has not completed.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operation_in_progress: Optional[bool] = field(
        default=None,
        metadata={
            "name": "operationInProgress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unit_multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "name": "unitMultiplier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unit_symbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "unitSymbol",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_system_resource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
            "name": "PowerSystemResource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Crew(IdentifiedObject):
    """
    Group of people with specific skills, tools, and vehicles.

    :ivar crew_members: All members of this crew.
    :ivar crew_type: Type of this crew.
    :ivar field_dispatch_history:
    :ivar location:
    :ivar status: Status of this crew.
    """
    crew_members: List["CrewMember"] = field(
        default_factory=list,
        metadata={
            "name": "CrewMembers",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    crew_type: Optional[CrewType] = field(
        default=None,
        metadata={
            "name": "CrewType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    field_dispatch_history: List[FieldDispatchHistory] = field(
        default_factory=list,
        metadata={
            "name": "FieldDispatchHistory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    location: Optional["Location"] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CustomerAccount(Document):
    """Assignment of a group of products and services purchased by the customer
    through a customer agreement, used as a mechanism for customer billing and
    payment.

    It contains common information from the various types of customer
    agreements to create billings (invoices) for a customer and receive
    payment.

    :ivar billing_cycle: Cycle day on which the associated customer
        account will normally be billed, used to determine when to
        produce the billing.
    :ivar budget_bill: Budget bill code.
    :ivar last_bill_amount: The last amount that will be billed to the
        customer prior to shut off of the account.
    :ivar account_notification:
    :ivar customer: Customer owning this account.
    :ivar customer_agreements: All agreements for this customer account.
    """
    billing_cycle: Optional[str] = field(
        default=None,
        metadata={
            "name": "billingCycle",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    budget_bill: Optional[str] = field(
        default=None,
        metadata={
            "name": "budgetBill",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    last_bill_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lastBillAmount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    account_notification: List[AccountNotification] = field(
        default_factory=list,
        metadata={
            "name": "AccountNotification",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer: Optional["Customer"] = field(
        default=None,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    customer_agreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAgreements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EmissionAccount(Curve):
    """Accounts for tracking emissions usage and credits for thermal generating
    units.

    A unit may have zero or more emission accounts, and will typically
    have one for tracking usage and one for tracking credits.

    :ivar emission_type: The type of emission, for example sulfur
        dioxide (SO2). The y1AxisUnits of the curve contains the unit of
        measure (e.g. kg) and the emissionType is the type of emission
        (e.g. sulfer dioxide).
    :ivar emission_value_source: The source of the emission value.
    :ivar thermal_generating_unit: A thermal generating unit may have
        one or more emission allowance accounts.
    """
    emission_type: Optional[EmissionType] = field(
        default=None,
        metadata={
            "name": "emissionType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    emission_value_source: Optional[EmissionValueSource] = field(
        default=None,
        metadata={
            "name": "emissionValueSource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    thermal_generating_unit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EmissionCurve(Curve):
    """Relationship between the unit's emission rate in units of mass per hour
    (Y-axis) and output active power (X-axis) for a given type of emission.

    This curve applies when only one type of fuel is being burned.

    :ivar emission_content: The emission content per quantity of fuel
        burned.
    :ivar emission_type: The type of emission, which also gives the
        production rate measurement unit. The y1AxisUnits of the curve
        contains the unit of measure (e.g. kg) and the emissionType is
        the type of emission (e.g. sulfer dioxide).
    :ivar is_net_gross_p: Flag is set to true when output is expressed
        in net active power.
    :ivar thermal_generating_unit: A thermal generating unit may have
        one or more emission curves.
    """
    emission_content: Optional[float] = field(
        default=None,
        metadata={
            "name": "emissionContent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    emission_type: Optional[EmissionType] = field(
        default=None,
        metadata={
            "name": "emissionType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_net_gross_p: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isNetGrossP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    thermal_generating_unit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dr_program_mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "drProgramMandatory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    issuer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    issuer_tracking_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerTrackingID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_action: Optional[EndDeviceAction] = field(
        default=None,
        metadata={
            "name": "EndDeviceAction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_control_type: Optional[EndDeviceControlType] = field(
        default=None,
        metadata={
            "name": "EndDeviceControlType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    end_device_groups: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_devices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    price_signal: Optional[FloatQuantity] = field(
        default=None,
        metadata={
            "name": "priceSignal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    primary_device_timing: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "name": "primaryDeviceTiming",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scheduled_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "scheduledInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    secondary_device_timing: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "name": "secondaryDeviceTiming",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_point_groups: List["UsagePointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePointGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EndDeviceFunction(AssetFunction):
    """
    Function performed by an end device such as a meter, communication
    equipment, controllers, etc.

    :ivar enabled: True if the function is enabled.
    :ivar end_device: End device that performs this function.
    :ivar registers: All registers for quantities metered by this end
        device function.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "name": "EndDevice",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    registers: List["Register"] = field(
        default_factory=list,
        metadata={
            "name": "Registers",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalPhenomenon(IdentifiedObject):
    """The actual or forecast occurrence of an environmental phenomenon at a
    specific point in time (or during a specific time interval) that may have
    both a center and area/line location.

    Named events (like Hurricane Andrew or the ash cloud associated with
    the St. Helens eruption) are intended to be modeled using an
    instance of IdentifiedPhenomenon (where the event name is recorded)
    related with one or more EnvironmentalPhenomenon instances in one or
    more Observations or Forecasts) which describe the event over time.

    :ivar environmental_information:
    :ivar environmental_location_kind: Location of relevance to this
        environmental phenomenon.
    :ivar named_phenomenon: The identified phenomenon to which this
        environmental phenomenon is associated.
    :ivar phenomenon_classification:
    :ivar time_interval: The timestamp of the phenomenon as a single
        point or time interval.
    """
    environmental_information: List["EnvironmentalInformation"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalInformation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    environmental_location_kind: List["EnvironmentalLocationType"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalLocationKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    named_phenomenon: Optional[NamedPhenomenon] = field(
        default=None,
        metadata={
            "name": "NamedPhenomenon",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phenomenon_classification: Optional["PhenomenonClassification"] = field(
        default=None,
        metadata={
            "name": "PhenomenonClassification",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    occurred_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "occurredDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phases: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    stop_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "stopDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fault_cause_types: List[FaultCauseType] = field(
        default_factory=list,
        metadata={
            "name": "FaultCauseTypes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    faulty_equipment: Optional["Equipment"] = field(
        default=None,
        metadata={
            "name": "FaultyEquipment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    impedance: Optional[FaultImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    location: Optional["Location"] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FuelAllocationSchedule(Curve):
    """
    The amount of fuel of a given type which is allocated for consumption over
    a specified period of time.

    :ivar fuel_allocation_end_date: The end time and date of the fuel
        allocation schedule.
    :ivar fuel_allocation_start_date: The start time and date of the
        fuel allocation schedule.
    :ivar fuel_type: The type of fuel, which also indicates the
        corresponding measurement unit.
    :ivar max_fuel_allocation: The maximum amount fuel that is allocated
        for consumption for the scheduled time period.
    :ivar min_fuel_allocation: The minimum amount fuel that is allocated
        for consumption for the scheduled time period, e.g., based on a
        "take-or-pay" contract.
    :ivar fossil_fuel: A fuel allocation schedule must have a fossil
        fuel.
    :ivar thermal_generating_unit: A thermal generating unit may have
        one or more fuel allocation schedules.
    """
    fuel_allocation_end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "fuelAllocationEndDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_allocation_start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "fuelAllocationStartDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_type: Optional[FuelType] = field(
        default=None,
        metadata={
            "name": "fuelType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_fuel_allocation: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxFuelAllocation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_fuel_allocation: Optional[float] = field(
        default=None,
        metadata={
            "name": "minFuelAllocation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fossil_fuel: Optional["FossilFuel"] = field(
        default=None,
        metadata={
            "name": "FossilFuel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    thermal_generating_unit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class GenUnitOpCostCurve(Curve):
    """Relationship between unit operating cost (Y-axis) and unit output active
    power (X-axis).

    The operating cost curve for thermal units is derived from heat
    input and fuel costs. The operating cost curve for hydro units is
    derived from water flow rates and equivalent water costs.

    :ivar is_net_gross_p: Flag is set to true when output is expressed
        in net active power.
    :ivar generating_unit: A generating unit may have one or more cost
        curves, depending upon fuel mixture and fuel cost.
    """
    is_net_gross_p: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isNetGrossP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    generating_unit: Optional["GeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "GeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class GrossToNetActivePowerCurve(Curve):
    """Relationship between the generating unit's gross active power output on
    the X-axis (measured at the terminals of the machine(s)) and the generating
    unit's net active power output on the Y-axis (based on utility-defined
    measurements at the power station).

    Station service loads, when modeled, should be treated as non-
    conforming bus loads. There may be more than one curve, depending on
    the auxiliary equipment that is in service.

    :ivar generating_unit: A generating unit may have a gross active
        power to net active power curve, describing the losses and
        auxiliary power requirements of the unit.
    """
    generating_unit: Optional["GeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "GeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class HeatInputCurve(Curve):
    """Relationship between unit heat input in energy per time for main fuel
    (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active
    power (X-axis).

    The quantity of main fuel used to sustain generation at this output
    level is prorated for throttling between definition points. The
    quantity of supplemental fuel used at this output level is fixed and
    not prorated.

    :ivar aux_power_mult: Power output - auxiliary power multiplier
        adjustment factor.
    :ivar aux_power_offset: Power output - auxiliary power offset
        adjustment factor.
    :ivar heat_input_eff: Heat input - efficiency multiplier adjustment
        factor.
    :ivar heat_input_offset: Heat input - offset adjustment factor.
    :ivar is_net_gross_p: Flag is set to true when output is expressed
        in net active power.
    :ivar thermal_generating_unit: A thermal generating unit may have a
        heat input curve.
    """
    aux_power_mult: Optional[float] = field(
        default=None,
        metadata={
            "name": "auxPowerMult",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    aux_power_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "auxPowerOffset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heat_input_eff: Optional[float] = field(
        default=None,
        metadata={
            "name": "heatInputEff",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heat_input_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "heatInputOffset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_net_gross_p: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isNetGrossP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    thermal_generating_unit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class HeatRateCurve(Curve):
    """Relationship between unit heat rate per active power (Y-axis) and  unit
    output (X-axis).

    The heat input is from all fuels.

    :ivar is_net_gross_p: Flag is set to true when output is expressed
        in net active power.
    :ivar thermal_generating_unit: A thermal generating unit may have a
        heat rate curve.
    """
    is_net_gross_p: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isNetGrossP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    thermal_generating_unit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    cooling_system: Optional[HouseCooling] = field(
        default=None,
        metadata={
            "name": "coolingSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    floor_area: Optional[float] = field(
        default=None,
        metadata={
            "name": "floorArea",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    heating_setpoint: Optional[float] = field(
        default=None,
        metadata={
            "name": "heatingSetpoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    heating_system: Optional[HouseHeating] = field(
        default=None,
        metadata={
            "name": "heatingSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hvac_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "hvacPowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    number_of_stories: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfStories",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    service_panel: Optional["EnergyConsumer"] = field(
        default=None,
        metadata={
            "name": "ServicePanel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    thermostat_controller: Optional[ThermostatController] = field(
        default=None,
        metadata={
            "name": "ThermostatController",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class HydroGeneratingEfficiencyCurve(Curve):
    """Relationship between unit efficiency in percent and unit output active
    power for a given net head in meters.

    The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ
    Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant)
    For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.

    :ivar hydro_generating_unit: A hydro generating unit has an
        efficiency curve.
    """
    hydro_generating_unit: Optional["HydroGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "HydroGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IncidentHazard(Hazard):
    """Hazardous situation associated with an incident.

    Examples are line down, gas leak, fire, etc.

    :ivar trouble_ticket: Trouble ticket associated with this hazard.
    """
    trouble_ticket: Optional["TroubleTicket"] = field(
        default=None,
        metadata={
            "name": "TroubleTicket",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class IncrementalHeatRateCurve(Curve):
    """Relationship between unit incremental heat rate in (delta energy/time)
    per (delta active power) and unit output in active power.

    The IHR curve represents the slope of the HeatInputCurve. Note that
    the "incremental heat rate" and the "heat rate" have the same
    engineering units.

    :ivar is_net_gross_p: Flag is set to true when output is expressed
        in net active power.
    :ivar thermal_generating_unit: A thermal generating unit may have an
        incremental heat rate curve.
    """
    is_net_gross_p: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isNetGrossP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    thermal_generating_unit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IrregularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them varies.

    :ivar time_points: The point data values that define a curve.
    """
    time_points: List[IrregularTimePoint] = field(
        default_factory=list,
        metadata={
            "name": "TimePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class LevelVsVolumeCurve(Curve):
    """Relationship between reservoir volume and reservoir level.

    The  volume is at the y-axis and the reservoir level at the x-axis.

    :ivar reservoir: A reservoir may have a level versus volume
        relationship.
    """
    reservoir: Optional["Reservoir"] = field(
        default=None,
        metadata={
            "name": "Reservoir",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class LoadArea(EnergyArea):
    """
    The class is the root or first level in a hierarchical structure for
    grouping of loads for the purpose of load flow load scaling.

    :ivar sub_load_areas: The SubLoadAreas in the LoadArea.
    """
    sub_load_areas: List["SubLoadArea"] = field(
        default_factory=list,
        metadata={
            "name": "SubLoadAreas",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class MeasurementValue(Iopoint):
    """The current state for a measurement.

    A state value is an instance of a measurement from a specific
    source. Measurements can be associated with many state values, each
    representing a different source for the measurement.

    :ivar sensor_accuracy: The limit, expressed as a percentage of the
        sensor maximum, that errors will not exceed when the sensor is
        used under  reference conditions.
    :ivar time_stamp: The time when the value was last updated
    :ivar measurement_value_quality: A MeasurementValue has a
        MeasurementValueQuality associated with it.
    :ivar measurement_value_source: A reference to the type of source
        that updates the MeasurementValue, e.g. SCADA, CCLink, manual,
        etc. User conventions for the names of sources are contained in
        the introduction to IEC 61970-301.
    :ivar procedure_data_set:
    """
    sensor_accuracy: Optional[float] = field(
        default=None,
        metadata={
            "name": "sensorAccuracy",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurement_value_quality: Optional[MeasurementValueQuality] = field(
        default=None,
        metadata={
            "name": "MeasurementValueQuality",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurement_value_source: Optional[MeasurementValueSource] = field(
        default=None,
        metadata={
            "name": "MeasurementValueSource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    procedure_data_set: List["ProcedureDataSet"] = field(
        default_factory=list,
        metadata={
            "name": "ProcedureDataSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    exciting_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "excitingCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    exciting_current_zero: Optional[float] = field(
        default=None,
        metadata={
            "name": "excitingCurrentZero",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    loss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    loss_zero: Optional[float] = field(
        default=None,
        metadata={
            "name": "lossZero",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energised_end: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "EnergisedEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energised_end_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "energisedEndVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    open_end_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "openEndStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    open_end_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "openEndVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_shift: Optional[float] = field(
        default=None,
        metadata={
            "name": "phaseShift",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energised_end: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "EnergisedEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    open_end: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "OpenEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class OperatingShare:
    """
    Specifies the operations contract relationship between a power system
    resource and a contract participant.

    :ivar percentage: Percentage operational ownership between the pair
        (power system resource and operatging participant) associated
        with this share. The total percentage ownership for a power
        system resource should add to 100%.
    :ivar operating_participant: The operating participant having this
        share with the associated power system resource.
    :ivar power_system_resource: The power system resource to which the
        share applies.
    """
    percentage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operating_participant: Optional[OperatingParticipant] = field(
        default=None,
        metadata={
            "name": "OperatingParticipant",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    power_system_resource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
            "name": "PowerSystemResource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    operational_limit_type: Optional[OperationalLimitType] = field(
        default=None,
        metadata={
            "name": "OperationalLimitType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OrganisationRole(IdentifiedObject):
    """
    Identifies a way in which an organisation may participate in the utility
    enterprise (e.g., customer, manufacturer, etc).

    :ivar configuration_events: All configuration events created for
        this organisation role.
    :ivar organisation: Organisation having this role.
    """
    configuration_events: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    organisation: Optional[Organisation] = field(
        default=None,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OverfrequencyTripCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OvervoltageTripCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ParallelLineSegment(IdentifiedObject):
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    acline_segment: Optional["AclineSegment"] = field(
        default=None,
        metadata={
            "name": "ACLineSegment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    right_of_way: Optional[RightOfWay] = field(
        default=None,
        metadata={
            "name": "RightOfWay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ParentOrganization(Organisation):
    """
    :ivar organisation: Organisation that is part of this parent
        organisation.
    """
    organisation: List["Organisation"] = field(
        default_factory=list,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PenstockLossCurve(Curve):
    """Relationship between penstock head loss (in meters) and  total discharge
    through the penstock (in cubic meters per second).

    One or more turbines may be connected to the same penstock.

    :ivar hydro_generating_unit: A hydro generating unit has a penstock
        loss curve.
    """
    hydro_generating_unit: Optional["HydroGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "HydroGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PersonRole(IdentifiedObject):
    """
    :ivar appointments: All appointments for this person.
    :ivar configuration_events: All configuration events created for
        this person role.
    :ivar person: Person having this role.
    """
    appointments: List[Appointment] = field(
        default_factory=list,
        metadata={
            "name": "Appointments",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    configuration_events: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    person: Optional[Person] = field(
        default=None,
        metadata={
            "name": "Person",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ReadingQuality:
    """Quality of a specific reading value or interval reading value.

    Note that more than one quality may be applicable to a given
    reading. Typically not used unless problems or unusual conditions
    occur (i.e., quality for each reading is assumed to be good unless
    stated otherwise in associated reading quality type). It can also be
    used with the corresponding reading quality type to indicate that
    the validation has been performed and succeeded.

    :ivar comment: Elaboration on the quality code.
    :ivar source: System acting as the source of the quality code.
    :ivar time_stamp: Date and time at which the quality code was
        assigned or ascertained.
    :ivar reading: Reading value to which this quality applies.
    :ivar reading_quality_type: Type of this reading quality.
    """
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reading: Optional["BaseReading"] = field(
        default=None,
        metadata={
            "name": "Reading",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reading_quality_type: Optional[ReadingQualityType] = field(
        default=None,
        metadata={
            "name": "ReadingQualityType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_step: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_points: List[RegularTimePoint] = field(
        default_factory=list,
        metadata={
            "name": "TimePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    grounded_end_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "groundedEndStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    leakage_impedance: Optional[float] = field(
        default=None,
        metadata={
            "name": "leakageImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    leakage_impedance_zero: Optional[float] = field(
        default=None,
        metadata={
            "name": "leakageImpedanceZero",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    loss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    loss_zero: Optional[float] = field(
        default=None,
        metadata={
            "name": "lossZero",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energised_end: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "name": "EnergisedEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    grounded_ends: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "name": "GroundedEnds",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class ShutdownCurve(Curve):
    """
    Relationship between the rate in gross active power/minute (Y-axis) at
    which a unit should be shutdown and its present gross MW output (X-axis).

    :ivar shutdown_cost: Fixed shutdown cost.
    :ivar shutdown_date: The date and time of the most recent generating
        unit shutdown.
    :ivar thermal_generating_unit: A thermal generating unit may have a
        shutdown curve.
    """
    shutdown_cost: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "shutdownCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shutdown_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "shutdownDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    thermal_generating_unit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class StartIgnFuelCurve(Curve):
    """
    The quantity of ignition fuel (Y-axis) used to restart and repay the
    auxiliary power consumed versus the number of hours (X-axis) the unit was
    off line.

    :ivar ignition_fuel_type: Type of ignition fuel.
    :ivar startup_model: The unit's startup model may have a startup
        ignition fuel curve.
    """
    ignition_fuel_type: Optional[FuelType] = field(
        default=None,
        metadata={
            "name": "ignitionFuelType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startup_model: Optional["StartupModel"] = field(
        default=None,
        metadata={
            "name": "StartupModel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class StartMainFuelCurve(Curve):
    """
    The quantity of main fuel (Y-axis) used to restart and repay the auxiliary
    power consumed versus the number of hours (X-axis) the unit was off line.

    :ivar main_fuel_type: Type of main fuel.
    :ivar startup_model: The unit's startup model may have a startup
        main fuel curve.
    """
    main_fuel_type: Optional[FuelType] = field(
        default=None,
        metadata={
            "name": "mainFuelType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startup_model: Optional["StartupModel"] = field(
        default=None,
        metadata={
            "name": "StartupModel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class StartRampCurve(Curve):
    """
    Rate in gross active power/minute (Y-axis) at which a unit can be loaded
    versus the number of hours (X-axis) the unit was off line.

    :ivar hot_standby_ramp: The startup ramp rate in gross for a unit
        that is on hot standby.
    :ivar startup_model: The unit's startup model may have a startup
        ramp curve.
    """
    hot_standby_ramp: Optional[float] = field(
        default=None,
        metadata={
            "name": "hotStandbyRamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startup_model: Optional["StartupModel"] = field(
        default=None,
        metadata={
            "name": "StartupModel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SubGeographicalRegion(IdentifiedObject):
    """
    A subset of a geographical region of a power system network model.

    :ivar lines: The lines within the sub-geographical region.
    :ivar region: The geographical region to which this sub-geographical
        region is within.
    :ivar substations: The substations in this sub-geographical region.
    """
    lines: List["Line"] = field(
        default_factory=list,
        metadata={
            "name": "Lines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    region: Optional[GeographicalRegion] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    substations: List["Substation"] = field(
        default_factory=list,
        metadata={
            "name": "Substations",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class TailbayLossCurve(Curve):
    """Relationship between tailbay head loss hight (y-axis) and the total
    discharge into the power station's tailbay volume per time unit (x-axis) .

    There could be more than one curve depending on the level of the
    tailbay reservoir or river level.

    :ivar hydro_generating_unit: A hydro generating unit has a tailbay
        loss curve.
    """
    hydro_generating_unit: Optional["HydroGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "HydroGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TargetLevelSchedule(Curve):
    """Reservoir water level targets from advanced studies or "rule curves".

    Typically in one hour increments for up to 10 days.

    :ivar high_level_limit: High target level limit, above which the
        reservoir operation will be penalized.
    :ivar low_level_limit: Low target level limit, below which the
        reservoir operation will be penalized.
    :ivar reservoir: A reservoir may have a water level target schedule.
    """
    high_level_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "highLevelLimit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    low_level_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowLevelLimit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reservoir: Optional["Reservoir"] = field(
        default=None,
        metadata={
            "name": "Reservoir",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Tariff(Document):
    """Document, approved by the responsible regulatory agency, listing the
    terms and conditions, including a schedule of prices, under which utility
    services will be provided.

    It has a unique number within the state or province. For rate
    schedules it is frequently allocated by the affiliated Public
    utilities commission (PUC).

    :ivar end_date: (if tariff became inactive) Date tariff was
        terminated.
    :ivar start_date: Date tariff was activated.
    :ivar pricing_structures: All pricing structures using this tariff.
    """
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pricing_structures: List["PricingStructure"] = field(
        default_factory=list,
        metadata={
            "name": "PricingStructures",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class TimeSchedule(Document):
    """Description of anything that changes through time.

    Time schedule is used to perform a single-valued function of time.
    Use inherited 'type' attribute to give additional information on
    this schedule, such as: periodic (hourly, daily, weekly, monthly,
    etc.), day of the month, by date, calendar (specific times and
    dates).

    :ivar disabled: True if this schedule is deactivated (disabled).
    :ivar offset: The offset from midnight (i.e., 0 h, 0 min, 0 s) for
        the periodic time points to begin. For example, for an interval
        meter that is set up for five minute intervals
        ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would
        result in scheduled events to read the meter executing at 2 min,
        7 min, 12 min, 17 min, 22 min, 27 min, 32 min, 37 min, 42 min,
        47 min, 52 min, and 57 min past each hour.
    :ivar recurrence_pattern: Interval at which the scheduled action
        repeats (e.g., first Monday of every month, last day of the
        month, etc.).
    :ivar recurrence_period: Duration between time points, from the
        beginning of one period to the beginning of the next period.
        Note that a device like a meter may have multiple interval
        periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min).
    :ivar schedule_interval: Schedule date and time interval.
    :ivar time_points: Sequence of time points belonging to this time
        schedule.
    """
    disabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    offset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    recurrence_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "recurrencePattern",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    recurrence_period: Optional[float] = field(
        default=None,
        metadata={
            "name": "recurrencePeriod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    schedule_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "scheduleInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_points: List["TimePoint"] = field(
        default_factory=list,
        metadata={
            "name": "TimePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar star_impedance: (accurate for 2- or 3-winding transformers
        only) Pi-model impedances of this transformer end. By
        convention, for a two winding transformer, the full values of
        the transformer should be entered on the high voltage end
        (endNumber=1).
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rground: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xground: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    base_voltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "name": "BaseVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    core_admittance: Optional[TransformerCoreAdmittance] = field(
        default=None,
        metadata={
            "name": "CoreAdmittance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    from_mesh_impedance: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "name": "FromMeshImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_tap_changer: Optional["PhaseTapChanger"] = field(
        default=None,
        metadata={
            "name": "PhaseTapChanger",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratio_tap_changer: Optional["RatioTapChanger"] = field(
        default=None,
        metadata={
            "name": "RatioTapChanger",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    star_impedance: Optional[TransformerStarImpedance] = field(
        default=None,
        metadata={
            "name": "StarImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    to_mesh_impedance: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "name": "ToMeshImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class UnderfrequencyTripCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class UndervoltageTripCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VoltVarCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VoltWattCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class WattVarCurve(Curve):
    ieee1547_setting: List["Ieee1547Setting"] = field(
        default_factory=list,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AccumulatorLimitSet(LimitSet):
    """
    An AccumulatorLimitSet specifies a set of Limits that are associated with
    an Accumulator measurement.

    :ivar limits: The limit values used for supervision of Measurements.
    :ivar measurements: The Measurements using the LimitSet.
    """
    limits: List[AccumulatorLimit] = field(
        default_factory=list,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    measurements: List["Accumulator"] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AccumulatorReset(Control):
    """
    This command reset the counter value to zero.

    :ivar accumulator_value: The accumulator value that is reset by the
        command.
    """
    accumulator_value: Optional["AccumulatorValue"] = field(
        default=None,
        metadata={
            "name": "AccumulatorValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ActivePowerLimit(OperationalLimit):
    """
    Limit on active power flow.

    :ivar normal_value: The normal value of active power limit.
    :ivar value: Value of active power limit.
    """
    normal_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "normalValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AnalogControl(Control):
    """
    An analog control used for supervisory control.

    :ivar max_value: Normal value range maximum for any of the
        Control.value. Used for scaling, e.g. in bar graphs.
    :ivar min_value: Normal value range minimum for any of the
        Control.value. Used for scaling, e.g. in bar graphs.
    :ivar analog_value: The MeasurementValue that is controlled.
    """
    max_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "minValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    analog_value: Optional["AnalogValue"] = field(
        default=None,
        metadata={
            "name": "AnalogValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class AnalogLimitSet(LimitSet):
    """
    An AnalogLimitSet specifies a set of Limits that are associated with an
    Analog measurement.

    :ivar limits: The limit values used for supervision of Measurements.
    :ivar measurements: The Measurements using the LimitSet.
    """
    limits: List[AnalogLimit] = field(
        default_factory=list,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurements: List["Analog"] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AnalyticScore(IdentifiedObject):
    """An indicative scoring by an analytic that can be used to characterize
    the health of or the risk associated with one or more assets.

    The analytic score reflects the results of an execution of an
    analytic against an asset or group of assets.

    :ivar calculation_date_time: Timestamp of when the score was
        calculated.
    :ivar effective_date_time: Date-time for when the score applies.
    :ivar value: Asset health score value.
    :ivar analytic:
    :ivar asset:
    :ivar asset_aggregate_score:
    :ivar asset_group:
    """
    calculation_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "calculationDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    effective_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "effectiveDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    analytic: Optional["Analytic"] = field(
        default=None,
        metadata={
            "name": "Analytic",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_aggregate_score: Optional["AggregateScore"] = field(
        default=None,
        metadata={
            "name": "AssetAggregateScore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_group: Optional[AssetGroup] = field(
        default=None,
        metadata={
            "name": "AssetGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ApparentPowerLimit(OperationalLimit):
    """
    Apparent power limit.

    :ivar normal_value: The normal apparent power limit.
    :ivar value: The apparent power limit.
    """
    normal_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "normalValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetOrganisationRole(OrganisationRole):
    """
    Role an organisation plays with respect to asset.

    :ivar assets: All assets for this organisation role.
    """
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AtmosphericPhenomenon(EnvironmentalPhenomenon):
    """
    An atmospheric phenomenon with a base and altitude providing the vertical
    coverage (combined with the Location to provide three dimensional space)

    :ivar direction: The direction the phenomenon is moving.
    :ivar max_coverage: The maximum percentage coverage
    :ivar min_coverage: The minimum percentage coverage
    :ivar speed: The speed of the phenomenon
    :ivar altitude: The maximum altitude of the phenomenon.
    :ivar base: The base altitude of the phenomenon.
    """
    direction: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_coverage: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxCoverage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_coverage: Optional[float] = field(
        default=None,
        metadata={
            "name": "minCoverage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    speed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    altitude: Optional[RelativeDisplacement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    base: Optional[RelativeDisplacement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BaseReading(MeasurementValue):
    """Common representation for reading values.

    Note that a reading value may have multiple qualities, as produced
    by various systems ('ReadingQuality.source').

    :ivar reported_date_time: (used only when there are detailed
        auditing requirements) Date and time at which the reading was
        first delivered to the metering system.
    :ivar source: System that originally supplied the reading (e.g.,
        customer, AMI system, handheld reading system, another
        enterprise system, etc.).
    :ivar value: Value of this reading.
    :ivar reading_qualities: All qualities of this reading.
    :ivar time_period: Start and end of the period for those readings
        whose type has a time attribute such as 'billing', seasonal' or
        'forTheSpecifiedPeriod'.
    """
    reported_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "reportedDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reading_qualities: List[ReadingQuality] = field(
        default_factory=list,
        metadata={
            "name": "ReadingQualities",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timePeriod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar network_asset_deployment: A network asset deployment at this
        base voltage level.
    :ivar topological_node: The topological nodes at the base voltage.
    :ivar transformer_ends: Transformer ends at the base voltage.  This
        is essential for PU calculation.
    :ivar voltage_level: The voltage levels having this base voltage.
    """
    nominal_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    conducting_equipment: List["ConductingEquipment"] = field(
        default_factory=list,
        metadata={
            "name": "ConductingEquipment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    network_asset_deployment: List[AssetDeployment] = field(
        default_factory=list,
        metadata={
            "name": "NetworkAssetDeployment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    topological_node: List["TopologicalNode"] = field(
        default_factory=list,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_ends: List[TransformerEnd] = field(
        default_factory=list,
        metadata={
            "name": "TransformerEnds",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltage_level: List["VoltageLevel"] = field(
        default_factory=list,
        metadata={
            "name": "VoltageLevel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CurrentLimit(OperationalLimit):
    """
    Operational limit on current.

    :ivar normal_value: The normal value for limit on current flow.
    :ivar value: Limit on current flow.
    """
    normal_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "normalValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class DocumentPersonRole(PersonRole):
    """
    Person role with respect to documents.
    """


@dataclass
class EnvironmentalDataProvider(OrganisationRole):
    """Entity providing environmental data.

    Could be an observed weather data provider, an entity providing
    forecasts, an authority providing alerts, etc.

    :ivar environmental_alert: Alert issued by this environmental data
        provider.
    :ivar environmental_information: Environmental information provided
        by this environmental data provider.
    """
    environmental_alert: List["EnvironmentalAlert"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalAlert",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_information: List["EnvironmentalInformation"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalInformation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalLocationType:
    """Kind of environmental location.

    Used when an environmental alert or phenomenon has multiple
    locations associated with it.

    :ivar kind: The kind of location. Typical values might be center,
        extent, primary, secondary, etc.
    :ivar environmental_alert: Environmental alert applying to location
        of this type.
    :ivar environmental_phenomenon: Environmental phenomenon for which
        this location is of relevance.
    :ivar location: Location of this instance of ths kind of
        environmental location.
    """
    kind: Optional[LocationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_alert: List["EnvironmentalAlert"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalAlert",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_phenomenon: List[EnvironmentalPhenomenon] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalPhenomenon",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    location: Optional["Location"] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FossilFuel(IdentifiedObject):
    """The fossil fuel consumed by the non-nuclear thermal generating unit.

    For example, coal, oil, gas, etc.   This a the specific fuels that
    the generating unit can consume.

    :ivar fossil_fuel_type: The type of fossil fuel, such as coal, oil,
        or gas.
    :ivar fuel_cost: The cost in terms of heat value for the given type
        of fuel.
    :ivar fuel_dispatch_cost: The cost of fuel used for economic
        dispatching which includes: fuel cost, transportation cost,  and
        incremental maintenance cost.
    :ivar fuel_eff_factor: The efficiency factor for the fuel (per unit)
        in terms of the effective energy absorbed.
    :ivar fuel_handling_cost: Handling and processing cost associated
        with this fuel.
    :ivar fuel_heat_content: The amount of heat per weight (or volume)
        of the given type of fuel.
    :ivar fuel_mixture: Relative amount of the given type of fuel, when
        multiple fuels are being consumed.
    :ivar fuel_sulfur: The fuel's fraction of pollution credit per unit
        of heat content.
    :ivar high_breakpoint_p: The active power output level of the unit
        at which the given type of fuel is switched on. This fuel (e.g.,
        oil) is sometimes used to supplement the base fuel (e.g., coal)
        at high active power output levels.
    :ivar low_breakpoint_p: The active power output level of the unit at
        which the given type of fuel is switched off. This fuel (e.g.,
        oil) is sometimes used to stabilize the base fuel (e.g., coal)
        at low active power output levels.
    :ivar fuel_allocation_schedules: A fuel allocation schedule must
        have a fossil fuel.
    :ivar thermal_generating_unit: A thermal generating unit may have
        one or more fossil fuels.
    """
    fossil_fuel_type: Optional[FuelType] = field(
        default=None,
        metadata={
            "name": "fossilFuelType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_cost: Optional[float] = field(
        default=None,
        metadata={
            "name": "fuelCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_dispatch_cost: Optional[float] = field(
        default=None,
        metadata={
            "name": "fuelDispatchCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_eff_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "fuelEffFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_handling_cost: Optional[float] = field(
        default=None,
        metadata={
            "name": "fuelHandlingCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_heat_content: Optional[float] = field(
        default=None,
        metadata={
            "name": "fuelHeatContent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_mixture: Optional[float] = field(
        default=None,
        metadata={
            "name": "fuelMixture",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_sulfur: Optional[float] = field(
        default=None,
        metadata={
            "name": "fuelSulfur",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    high_breakpoint_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "highBreakpointP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    low_breakpoint_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowBreakpointP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_allocation_schedules: List[FuelAllocationSchedule] = field(
        default_factory=list,
        metadata={
            "name": "FuelAllocationSchedules",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    thermal_generating_unit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class GenUnitOpSchedule(RegularIntervalSchedule):
    """The generating unit's Operator-approved current operating schedule (or
    plan), typically produced with the aid of unit commitment type analyses.

    The X-axis represents absolute time. The Y1-axis represents the
    status (0=off-line and unavailable: 1=available: 2=must run: 3=must
    run at fixed power value: etc.). The Y2-axis represents the must run
    fixed power value where required.

    :ivar generating_unit: A generating unit may have an operating
        schedule, indicating the planned operation of the unit.
    """
    generating_unit: Optional["GeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "GeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class GeosphericPhenomenon(EnvironmentalPhenomenon):
    """
    A geospheric phenomenon.
    """


@dataclass
class HydroPumpOpSchedule(RegularIntervalSchedule):
    """
    The hydro pump's Operator-approved current operating schedule (or plan),
    typically produced with the aid of unit commitment type analyses.The unit's
    operating schedule status is typically given as: (0=unavailable)
    (1=avilable to startup or shutdown)  (2=must pump).

    :ivar hydro_pump: The hydro pump has a pumping schedule over time,
        indicating when pumping is to occur.
    """
    hydro_pump: Optional["HydroPump"] = field(
        default=None,
        metadata={
            "name": "HydroPump",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class HydrosphericPhenomenon(EnvironmentalPhenomenon):
    """
    A hydrospheric phenomenon.
    """


@dataclass
class Ieee1547Setting:
    class Meta:
        name = "IEEE1547Setting"

    constant_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "constantPowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    constant_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "constantReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_intentional_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceIntentionalDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_max_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMaxFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_max_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMaxVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_min_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMinFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_min_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMinVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    frequency_droop_response_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "frequencyDroopResponseTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    island_clearing_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "islandClearingTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    open_loop_response_time_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "openLoopResponseTimeP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    over_frequency_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "overFrequencyDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    over_frequency_droop: Optional[float] = field(
        default=None,
        metadata={
            "name": "overFrequencyDroop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_constant_open_loop: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeConstantOpenLoop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_constant_reference_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeConstantReferenceVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    under_frequency_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "underFrequencyDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    under_frequency_droop: Optional[float] = field(
        default=None,
        metadata={
            "name": "underFrequencyDroop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overfrequency_trip_curve: Optional[OverfrequencyTripCurve] = field(
        default=None,
        metadata={
            "name": "OverfrequencyTripCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overvoltage_trip_curve: Optional[OvervoltageTripCurve] = field(
        default=None,
        metadata={
            "name": "OvervoltageTripCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_electronics_connections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rotating_machines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "name": "RotatingMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    underfrequency_trip_curve: Optional[UnderfrequencyTripCurve] = field(
        default=None,
        metadata={
            "name": "UnderfrequencyTripCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    undervoltage_trip_curve: Optional[UndervoltageTripCurve] = field(
        default=None,
        metadata={
            "name": "UndervoltageTripCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_curve: Optional[VoltVarCurve] = field(
        default=None,
        metadata={
            "name": "VoltVarCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_watt_curve: Optional[VoltWattCurve] = field(
        default=None,
        metadata={
            "name": "VoltWattCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    watt_var_curve: Optional[WattVarCurve] = field(
        default=None,
        metadata={
            "name": "WattVarCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class InflowForecast(RegularIntervalSchedule):
    """Natural water inflow to a reservoir, usually forecasted from predicted
    rain and snowmelt.

    Typically in one hour increments for up to 10 days. The forecast is
    given in average cubic meters per second over the time increment.

    :ivar reservoir: A reservoir may have a "natural" inflow forecast.
    """
    reservoir: Optional["Reservoir"] = field(
        default=None,
        metadata={
            "name": "Reservoir",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class LineFault(Fault):
    """
    A fault that occurs on an AC line segment at some point along the length.

    :ivar length_from_terminal1: The length to the place where the fault
        is located starting from terminal with sequence number 1 of the
        faulted line segment.
    :ivar acline_segment: The line segment of this line fault.
    """
    length_from_terminal1: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthFromTerminal1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    acline_segment: Optional["AclineSegment"] = field(
        default=None,
        metadata={
            "name": "ACLineSegment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Manufacturer(OrganisationRole):
    """
    Organisation that manufactures asset products.

    :ivar product_asset_models: All asset models by this manufacturer.
    """
    product_asset_models: List["ProductAssetModel"] = field(
        default_factory=list,
        metadata={
            "name": "ProductAssetModels",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OperationPersonRole(PersonRole):
    """
    Person role in the context of utility operations.
    """


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
    connectivity_node: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    equipment: Optional["Equipment"] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operational_limit_value: List[OperationalLimit] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimitValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminal: Optional["Acdcterminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PerLengthPhaseImpedance(PerLengthImpedance):
    """
    Impedance and admittance parameters per unit length for n-wire unbalanced
    lines, in matrix form.

    :ivar conductor_count: Number of phase, neutral, and other wires
        retained. Constrains the number of matrix elements and the phase
        codes that can be used with this matrix.
    :ivar phase_impedance_data: All data that belong to this conductor
        phase impedance.
    """
    conductor_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "conductorCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_impedance_data: List[PhaseImpedanceData] = field(
        default_factory=list,
        metadata={
            "name": "PhaseImpedanceData",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    bch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_angle_clock: Optional[int] = field(
        default=None,
        metadata={
            "name": "phaseAngleClock",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_transformer: Optional["PowerTransformer"] = field(
        default=None,
        metadata={
            "name": "PowerTransformer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PricingStructure(Document):
    """Grouping of pricing components and prices used in the creation of
    customer charges and the eligibility criteria under which these terms may
    be offered to a customer.

    The reasons for grouping include state, customer classification,
    site characteristics, classification (i.e. fee price structure,
    deposit price structure, electric service price structure, etc.) and
    accounting requirements.

    :ivar code: Unique user-allocated key for this pricing structure,
        used by company representatives to identify the correct price
        structure for allocating to a customer. For rate schedules it is
        often prefixed by a state code.
    :ivar daily_ceiling_usage: Absolute maximum valid non-demand usage
        quantity used in validating a customer's billed non-demand
        usage.
    :ivar daily_estimated_usage: Used in place of actual computed
        estimated average when history of usage is not available, and
        typically manually entered by customer accounting.
    :ivar daily_floor_usage: Absolute minimum valid non-demand usage
        quantity used in validating a customer's billed non-demand
        usage.
    :ivar revenue_kind: (accounting) Kind of revenue, often used to
        determine the grace period allowed, before collection actions
        are taken on a customer (grace periods vary between revenue
        classes).
    :ivar tax_exemption: True if this pricing structure is not taxable.
    :ivar customer_agreements: All customer agreements with this pricing
        structure.
    :ivar service_category: Service category to which this pricing
        structure applies.
    :ivar tariffs: All tariffs used by this pricing structure.
    :ivar usage_points: All service delivery points (with prepayment
        meter running as a stand-alone device, with no CustomerAgreement
        or Customer) to which this pricing structure applies.
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    daily_ceiling_usage: Optional[int] = field(
        default=None,
        metadata={
            "name": "dailyCeilingUsage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    daily_estimated_usage: Optional[int] = field(
        default=None,
        metadata={
            "name": "dailyEstimatedUsage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    daily_floor_usage: Optional[int] = field(
        default=None,
        metadata={
            "name": "dailyFloorUsage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    revenue_kind: Optional[RevenueKind] = field(
        default=None,
        metadata={
            "name": "revenueKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tax_exemption: Optional[bool] = field(
        default=None,
        metadata={
            "name": "taxExemption",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_agreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAgreements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_category: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "name": "ServiceCategory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    tariffs: List[Tariff] = field(
        default_factory=list,
        metadata={
            "name": "Tariffs",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ProcedureDataSet(Document):
    """A data set recorded each time a procedure is executed.

    Observed results are captured in associated measurement values
    and/or values for properties relevant to the type of procedure
    performed.

    :ivar completed_date_time: Date and time procedure was completed.
    :ivar asset: Asset to which this procedure data set applies.
    :ivar measurement_value:
    :ivar procedure: Procedure capturing this data set.
    :ivar properties: UserAttributes used to specify further properties
        of this procedure data set. Use 'name' to specify what kind of
        property it is, and 'value.value' attribute for the actual
        value.
    """
    completed_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "completedDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurement_value: List[MeasurementValue] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    procedure: Optional["Procedure"] = field(
        default=None,
        metadata={
            "name": "Procedure",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    properties: List[UserAttribute] = field(
        default_factory=list,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Register(IdentifiedObject):
    """
    A device that indicates or records units of the commodity or other quantity
    measured.

    :ivar is_virtual: If true, the data it produces is  calculated or
        measured by a device other than a physical end device/meter.
        Otherwise, any data streams it produces are measured by the
        hardware of the end device/meter itself.
    :ivar left_digit_count: Number of digits (dials on a mechanical
        meter) to the left of the decimal place; default is normally 5.
    :ivar right_digit_count: Number of digits (dials on a mechanical
        meter) to the right of the decimal place.
    :ivar tou_tier_name: Name used for the time of use tier (also known
        as bin or bucket).  For example, "peak", "off-peak", "TOU
        Category A", etc.
    :ivar channels: All channels that collect/report values from this
        register.
    :ivar end_device_function: End device function metering quantities
        displayed by this register.
    :ivar tou_tier: Clock time interval for register to beging/cease
        accumulating time of usage (e.g., start at 8:00 am, stop at 5:00
        pm).
    """
    is_virtual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isVirtual",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    left_digit_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "leftDigitCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    right_digit_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "rightDigitCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tou_tier_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "touTierName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    channels: List["Channel"] = field(
        default_factory=list,
        metadata={
            "name": "Channels",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_function: Optional[EndDeviceFunction] = field(
        default=None,
        metadata={
            "name": "EndDeviceFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tou_tier: Optional[TimeInterval] = field(
        default=None,
        metadata={
            "name": "touTier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    season: Optional[Season] = field(
        default=None,
        metadata={
            "name": "Season",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class SimpleEndDeviceFunction(EndDeviceFunction):
    """Simple end device function distinguished by 'kind'.

    Use this class for instances that cannot be represented by another
    end device function specialisations.

    :ivar kind: Kind of this function.
    """
    kind: Optional[EndDeviceFunctionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class SpacePhenomenon(EnvironmentalPhenomenon):
    """
    An extra-terrestrial phenomenon.
    """


@dataclass
class StartupModel(IdentifiedObject):
    """
    Unit start up characteristics depending on how long the unit has been off
    line.

    :ivar fixed_maint_cost: Fixed maintenance cost.
    :ivar hot_standby_heat: The amount of heat input per time uint
        required for hot standby operation.
    :ivar incremental_maint_cost: Incremental maintenance cost.
    :ivar minimum_down_time: The minimum number of hours the unit must
        be down before restart.
    :ivar minimum_run_time: The minimum number of hours the unit must be
        operating before being allowed to shut down.
    :ivar risk_factor_cost: The opportunity cost associated with the
        return in monetary unit. This represents the restart's "share"
        of the unit depreciation and risk of an event which would damage
        the unit.
    :ivar startup_cost: Total miscellaneous start up costs.
    :ivar startup_date: The date and time of the most recent generating
        unit startup.
    :ivar startup_priority: Startup priority within control area where
        lower numbers indicate higher priorities.  More than one unit in
        an area may be assigned the same priority.
    :ivar stby_aux_p: The unit's auxiliary active power consumption to
        maintain standby mode.
    :ivar start_ign_fuel_curve: The unit's startup model may have a
        startup ignition fuel curve.
    :ivar start_main_fuel_curve: The unit's startup model may have a
        startup main fuel curve.
    :ivar start_ramp_curve: The unit's startup model may have a startup
        ramp curve.
    :ivar thermal_generating_unit: A thermal generating unit may have a
        startup model.
    """
    fixed_maint_cost: Optional[float] = field(
        default=None,
        metadata={
            "name": "fixedMaintCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hot_standby_heat: Optional[float] = field(
        default=None,
        metadata={
            "name": "hotStandbyHeat",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    incremental_maint_cost: Optional[float] = field(
        default=None,
        metadata={
            "name": "incrementalMaintCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimum_down_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumDownTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimum_run_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumRunTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    risk_factor_cost: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "riskFactorCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startup_cost: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "startupCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startup_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startupDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startup_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "startupPriority",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    stby_aux_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "stbyAuxP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    start_ign_fuel_curve: Optional[StartIgnFuelCurve] = field(
        default=None,
        metadata={
            "name": "StartIgnFuelCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    start_main_fuel_curve: Optional[StartMainFuelCurve] = field(
        default=None,
        metadata={
            "name": "StartMainFuelCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    start_ramp_curve: Optional[StartRampCurve] = field(
        default=None,
        metadata={
            "name": "StartRampCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    thermal_generating_unit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SteamSendoutSchedule(RegularIntervalSchedule):
    """
    The cogeneration plant's steam sendout schedule in volume per time unit.

    :ivar cogeneration_plant: A cogeneration plant has a steam sendout
        schedule.
    """
    cogeneration_plant: Optional["CogenerationPlant"] = field(
        default=None,
        metadata={
            "name": "CogenerationPlant",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class StringMeasurementValue(MeasurementValue):
    """
    StringMeasurementValue represents a measurement value of type string.

    :ivar value: The value to supervise.
    :ivar string_measurement: Measurement to which this value is
        connected.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    string_measurement: Optional["StringMeasurement"] = field(
        default=None,
        metadata={
            "name": "StringMeasurement",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SubLoadArea(EnergyArea):
    """
    The class is the second level in a hierarchical structure for grouping of
    loads for the purpose of load flow load scaling.

    :ivar load_area: The LoadArea where the SubLoadArea belongs.
    :ivar load_groups: The Loadgroups in the SubLoadArea.
    """
    load_area: Optional[LoadArea] = field(
        default=None,
        metadata={
            "name": "LoadArea",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    load_groups: List["LoadGroup"] = field(
        default_factory=list,
        metadata={
            "name": "LoadGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class TimePoint(IdentifiedObject):
    """
    A point in time within a sequence of points in time relative to a time
    schedule.

    :ivar date_time: Absolute date and time for this time point. For
        calendar-based time point, it is typically manually entered,
        while for interval-based or sequence-based time point it is
        derived.
    :ivar relative_time_interval: (if interval-based) A point in time
        relative to scheduled start time in
        'TimeSchedule.scheduleInterval.start'.
    :ivar sequence_number: (if sequence-based) Relative sequence number
        for this time point.
    :ivar status: Status of this time point.
    :ivar time_schedule: Time schedule owning this time point.
    :ivar window: Interval defining the window of time that this time
        point is valid (for example, seasonal, only on weekends, not on
        weekends, only 8:00 am to 5:00 pm, etc.).
    """
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    relative_time_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "relativeTimeInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_schedule: Optional[TimeSchedule] = field(
        default=None,
        metadata={
            "name": "TimeSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    window: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class TransformerTankEnd(TransformerEnd):
    """
    Transformer tank end represents an individual winding for unbalanced models
    or for transformer tanks connected into a bank (and bank is modelled with
    the PowerTransformer).

    :ivar phases: Describes the phases carried by a conducting
        equipment.
    :ivar transformer_tank: Transformer this winding belongs to.
    """
    phases: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_tank: Optional["TransformerTank"] = field(
        default=None,
        metadata={
            "name": "TransformerTank",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class TroubleTicket(Document):
    """
    :ivar date_time_of_report: Date and time the trouble has been
        reported.
    :ivar first_responder_status: Indicates whether the first responder
        such as police, fire department etc.has been notified and
        whether they are on site or en route.
    :ivar multiple_premises: Set to true if the outage report indicated
        that other neighbors are also out of power.
    :ivar reporting_kind: Indicates how the customer reported trouble.
    :ivar resolved_date_time: Date and time this trouble ticket has been
        resolved.
    :ivar trouble_code: Trouble code (e.g., power down, flickering
        lights, partial power, etc).
    :ivar trouble_kind:
    :ivar customer: Customer for whom this trouble ticket is relevant.
    :ivar incident_hazard: All hazards reported with this trouble
        ticket.
    :ivar notification: Notification for this trouble ticket.
    :ivar service_location:
    """
    date_time_of_report: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dateTimeOfReport",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    first_responder_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstResponderStatus",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    multiple_premises: Optional[bool] = field(
        default=None,
        metadata={
            "name": "multiplePremises",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reporting_kind: Optional[TroubleReportingKind] = field(
        default=None,
        metadata={
            "name": "reportingKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    resolved_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "resolvedDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    trouble_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "troubleCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    trouble_kind: Optional[PnnltroubleCallKind] = field(
        default=None,
        metadata={
            "name": "troubleKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer: Optional["Customer"] = field(
        default=None,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    incident_hazard: List[IncidentHazard] = field(
        default_factory=list,
        metadata={
            "name": "IncidentHazard",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    notification: Optional["CustomerNotification"] = field(
        default=None,
        metadata={
            "name": "Notification",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_location: Optional[ServiceLocation] = field(
        default=None,
        metadata={
            "name": "ServiceLocation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    demand_response_programs: List["DemandResponseProgram"] = field(
        default_factory=list,
        metadata={
            "name": "DemandResponsePrograms",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_controls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VoltageLimit(OperationalLimit):
    """
    Operational limit applied to voltage.

    :ivar normal_value: The normal limit on voltage. High or low limit
        nature of the limit depends upon the properties of the
        operational limit type.
    :ivar value: Limit on voltage. High or low limit nature of the limit
        depends upon the properties of the operational limit type.
    """
    normal_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "normalValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AccumulatorValue(MeasurementValue):
    """
    AccumulatorValue represents an accumulated (counted) MeasurementValue.

    :ivar value: The value to supervise. The value is positive.
    :ivar accumulator: Measurement to which this value is connected.
    :ivar accumulator_reset: The command that reset the accumulator
        value.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    accumulator: Optional["Accumulator"] = field(
        default=None,
        metadata={
            "name": "Accumulator",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    accumulator_reset: Optional[AccumulatorReset] = field(
        default=None,
        metadata={
            "name": "AccumulatorReset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AggregateScore(AnalyticScore):
    """
    An aggregated indicative scoring by an analytic, which is based on other
    analytic scores, that can be used to characterize the health of or the risk
    associated with one or more assets.
    """
    analytic_score: List["AnalyticScore"] = field(
        default_factory=list,
        metadata={
            "name": "AnalyticScore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class AnalogValue(MeasurementValue):
    """
    AnalogValue represents an analog MeasurementValue.

    :ivar value: The value to supervise.
    :ivar analog: Measurement to which this value is connected.
    :ivar analog_control: The Control variable associated with the
        MeasurementValue.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    analog: Optional["Analog"] = field(
        default=None,
        metadata={
            "name": "Analog",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    analog_control: Optional[AnalogControl] = field(
        default=None,
        metadata={
            "name": "AnalogControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Approver(DocumentPersonRole):
    """
    Person who accepted/signed or rejected the document.

    :ivar documents: All documents for this approver.
    """
    documents: List["Document"] = field(
        default_factory=list,
        metadata={
            "name": "Documents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetOwner(AssetOrganisationRole):
    """
    Owner of the asset.

    :ivar ownerships: All ownerships of this owner.
    """
    ownerships: List["Ownership"] = field(
        default_factory=list,
        metadata={
            "name": "Ownerships",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetTestSampleTaker(AssetOrganisationRole):
    """
    :ivar specimen: Specimen taken by this sample taker.
    """
    specimen: List["Specimen"] = field(
        default_factory=list,
        metadata={
            "name": "Specimen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetUser(AssetOrganisationRole):
    """
    Organisation that is a user of the asset.
    """


@dataclass
class Author(DocumentPersonRole):
    """
    Person who created document or activity record.

    :ivar activity_records: All activity records with this author.
    :ivar documents: All documents of this this author.
    """
    activity_records: List["ActivityRecord"] = field(
        default_factory=list,
        metadata={
            "name": "ActivityRecords",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    documents: List[Document] = field(
        default_factory=list,
        metadata={
            "name": "Documents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Channel(IdentifiedObject):
    """A single path for the collection or reporting of register values over a
    period of time.

    For example, a register which measures forward energy can have two
    channels, one providing bulk quantity readings and the other
    providing interval readings of a fixed interval size.

    :ivar is_virtual: If true, the data is being calculated by an
        enterprise system rather than metered directly.
    :ivar reading_type: Reading type for register values
        reported/collected by this channel.
    :ivar register: Register whose values are collected/reported by this
        channel.
    """
    is_virtual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isVirtual",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reading_type: Optional["ReadingType"] = field(
        default=None,
        metadata={
            "name": "ReadingType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    register: Optional[Register] = field(
        default=None,
        metadata={
            "name": "Register",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CloudCondition(AtmosphericPhenomenon):
    """
    A classified cloud phenomenon with a type.

    :ivar kind: The type of the cloud as defined by the CloudKind
        enumeration.
    """
    kind: Optional[CloudKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ConformLoadSchedule(SeasonDayTypeSchedule):
    """A curve of load  versus time (X-axis) showing the active power values
    (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered.

    This curve represents a typical pattern of load over the time period
    for a given day type and season.

    :ivar conform_load_group: The ConformLoadGroup where the
        ConformLoadSchedule belongs.
    """
    conform_load_group: Optional["ConformLoadGroup"] = field(
        default=None,
        metadata={
            "name": "ConformLoadGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class CrewMember(OperationPersonRole):
    """
    Member of a crew.

    :ivar crew: Crew to which this crew member belongs.
    """
    crew: Optional["Crew"] = field(
        default=None,
        metadata={
            "name": "Crew",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CustomerNotification:
    """
    Conditions for notifying the customer about the changes in the status of
    their service (e.g., outage restore, estimated restoration time, tariff or
    service level change, etc.)

    :ivar contact_type: Type of contact (e.g., phone, email, etc.).
    :ivar contact_value: Value of contact type (e.g., phone number,
        email address, etc.).
    :ivar earliest_date_time_to_call: Earliest date time to call the
        customer.
    :ivar latest_date_time_to_call: Latest date time to call the
        customer.
    :ivar trigger: Trigger for this notification.
    :ivar customer: Customer requiring this notification.
    :ivar trouble_tickets: All trouble tickets with this notification.
    """
    contact_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    contact_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    earliest_date_time_to_call: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "earliestDateTimeToCall",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    latest_date_time_to_call: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "latestDateTimeToCall",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    trigger: Optional[NotificationTriggerKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer: Optional["Customer"] = field(
        default=None,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    trouble_tickets: List[TroubleTicket] = field(
        default_factory=list,
        metadata={
            "name": "TroubleTickets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Cyclone(AtmosphericPhenomenon):
    """
    A cyclone (or tropical cyclone), a rapidly-rotating storm system
    characterized by a low-pressure center, strong winds, and a spiral
    arrangement of thunderstorms that produce heavy rain.

    :ivar central_pressure: The central pressure of the cyclone during
        the time interval.
    :ivar max_surface_wind_speed: The maximum surface wind speed of the
        cyclone during the time interval.
    :ivar wind_force: Wind Force as classified on the Beaufort Scale
        (0-12) during the time interval.
    """
    central_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "centralPressure",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_surface_wind_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxSurfaceWindSpeed",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wind_force: Optional[int] = field(
        default=None,
        metadata={
            "name": "windForce",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar customer_agreements: All customer agreements through which the
        customer is enrolled in this demand response program.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_agreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAgreements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_groups: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_point_groups: List[UsagePointGroup] = field(
        default_factory=list,
        metadata={
            "name": "UsagePointGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    validity_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "validityInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class DiagnosisDataSet(ProcedureDataSet):
    """The result of a problem (typically an asset failure) diagnosis.

    Contains complete information like what might be received from a lab
    doing forensic analysis of a failed asset.

    :ivar effect: Effect of problem.
    :ivar failure_mode: Failuer mode, for example: Failure to Insulate;
        Failure to conduct; Failure to contain oil; Failure to provide
        ground plane; Other.
    :ivar final_cause: Cause of problem determined during diagnosis.
    :ivar final_code: Code for diagnosed probem type.
    :ivar final_origin: Origin of problem determined during diagnosis.
    :ivar final_remark: Remarks pertaining to findings during problem
        diagnosis.
    :ivar phase_code: Phase(s) diagnosed.
    :ivar preliminary_code: Code for problem type determined during
        preliminary assessment.
    :ivar preliminary_date_time: Date and time preliminary assessment of
        problem was performed.
    :ivar preliminary_remark: Remarks pertaining to preliminary
        assessment of problem.
    :ivar root_cause: Root cause of problem determined during diagnosis.
    :ivar root_origin: Root origin of problem determined during
        diagnosis.
    :ivar root_remark: Remarks pertaining to root cause findings during
        problem diagnosis.
    """
    effect: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failure_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "failureMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    final_cause: Optional[str] = field(
        default=None,
        metadata={
            "name": "finalCause",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    final_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "finalCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    final_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "finalOrigin",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    final_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "finalRemark",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_code: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "name": "phaseCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    preliminary_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "preliminaryCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    preliminary_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "preliminaryDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    preliminary_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "preliminaryRemark",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    root_cause: Optional[str] = field(
        default=None,
        metadata={
            "name": "rootCause",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    root_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "rootOrigin",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    root_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "rootRemark",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Earthquake(GeosphericPhenomenon):
    """
    An earthquake.

    :ivar intensity: The intensity of the earthquake as defined by the
        Modified Mercalli Intensity (MMI) scale. Possible values are
        1-12, corresponding to I-XII.
    :ivar magnitude: The magnitude of the earthquake as defined on the
        Moment Magnitude (M&lt;sub&gt;w&lt;/sub&gt;) scale, which
        measures the size of earthquakes in terms of the energy
        released. Must be greater than zero.
    :ivar focal_depth: The depth below the earth's surface of the
        earthquake's focal point.
    """
    intensity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    magnitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    focal_depth: Optional[RelativeDisplacement] = field(
        default=None,
        metadata={
            "name": "focalDepth",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Editor(DocumentPersonRole):
    """
    Person who modified the document.

    :ivar documents: All documents for this editor.
    """
    documents: List["Document"] = field(
        default_factory=list,
        metadata={
            "name": "Documents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalCodedValue(StringMeasurementValue):
    """An environmental value described using a coded value.

    A triplicate of enumerated values representing intensity, coverage,
    type of weather is used. These may be concatenated into the string
    value.

    :ivar coverage_kind: Code representing the coverage of the weather
        condition during the time interval.
    :ivar intensity_kind: Code representing the intensity of the weather
        condition during the time interval.
    :ivar probability_percent: Probability of weather condition
        occurring during the time interval expressed as a percentage.
        Applicable only when weather condition is related to a forecast
        (not an observation).
    :ivar weather_kind: Code representing the type of weather condition
        during the time interval.
    """
    coverage_kind: Optional[CoverageCodeKind] = field(
        default=None,
        metadata={
            "name": "coverageKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    intensity_kind: Optional[IntensityCodeKind] = field(
        default=None,
        metadata={
            "name": "intensityKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    probability_percent: Optional[float] = field(
        default=None,
        metadata={
            "name": "probabilityPercent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    weather_kind: Optional[WeatherCodeKind] = field(
        default=None,
        metadata={
            "name": "weatherKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Fire(GeosphericPhenomenon):
    """
    A fire, often uncontrolled, covering an area of land which typically
    contains combustible vegetation.
    """


@dataclass
class Flood(HydrosphericPhenomenon):
    """A flood, an overflowing of a large amount of water beyond its normal
    confines, esp.

    over what is normally dry land.
    """


@dataclass
class InspectionDataSet(ProcedureDataSet):
    """
    Documents the result of one inspection, for a given attribute of an asset.

    :ivar location_condition: Description of the conditions of the
        location where the asset resides.
    :ivar according_to_schedules:
    """
    location_condition: Optional[str] = field(
        default=None,
        metadata={
            "name": "locationCondition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    according_to_schedules: List["ScheduledEventData"] = field(
        default_factory=list,
        metadata={
            "name": "AccordingToSchedules",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class IntervalReading(BaseReading):
    """Data captured at regular intervals of time.

    Interval data could be captured as incremental data, absolute data, or relative data. The source for the data is usually a tariff quantity or an engineering quantity. Data is typically captured in time-tagged, uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min.
    Note: Interval Data is sometimes also called "Interval Data Readings" (IDR).

    :ivar interval_blocks: All blocks containing this interval reading.
    """
    interval_blocks: List["IntervalBlock"] = field(
        default_factory=list,
        metadata={
            "name": "IntervalBlocks",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Issuer(DocumentPersonRole):
    """
    Person who issued the document and is responsible for its content.

    :ivar documents: All documents for this issuer.
    """
    documents: List["Document"] = field(
        default_factory=list,
        metadata={
            "name": "Documents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Landslide(GeosphericPhenomenon):
    """
    A landslide, a large mass of rocks and earth that suddenly and quickly
    moves down the side of a mountain or hill.
    """


@dataclass
class LightningStrike(GeosphericPhenomenon):
    """
    A cloud-to-ground lightning strike at a particular location.

    :ivar error_ellipse_confidence: Likelihood that strike fell within
        errorEllipse.
    :ivar error_ellipse_major_semi_axis: Length of major semi-axis
        (longest radius) of the error ellipse.
    :ivar error_ellipse_minor_semi_axis: Length of minor semi-axis
        (shortest radius) of the error ellipse.
    :ivar error_ellipse_orientation: The orientation of the major semi-
        axis in degrees from True North.
    :ivar negative_polarity: The polarity of the strike, with T meaning
        negative. About 90% of all lightning strokes are negative
        strokes, meaning that they were initiated by a large
        concentration of negative charge in the cloud-base; this tends
        to induce an area of positive charge on the ground.
    :ivar peak_amplitude: Peak current of strike.
    """
    error_ellipse_confidence: Optional[float] = field(
        default=None,
        metadata={
            "name": "errorEllipseConfidence",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    error_ellipse_major_semi_axis: Optional[float] = field(
        default=None,
        metadata={
            "name": "errorEllipseMajorSemiAxis",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    error_ellipse_minor_semi_axis: Optional[float] = field(
        default=None,
        metadata={
            "name": "errorEllipseMinorSemiAxis",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    error_ellipse_orientation: Optional[float] = field(
        default=None,
        metadata={
            "name": "errorEllipseOrientation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    negative_polarity: Optional[bool] = field(
        default=None,
        metadata={
            "name": "negativePolarity",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    peak_amplitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "peakAmplitude",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class LoadGroup(IdentifiedObject):
    """
    The class is the third level in a hierarchical structure for grouping of
    loads for the purpose of load flow load scaling.

    :ivar sub_load_area: The SubLoadArea where the Loadgroup belongs.
    """
    sub_load_area: Optional[SubLoadArea] = field(
        default=None,
        metadata={
            "name": "SubLoadArea",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class MagneticStorm(SpacePhenomenon):
    """
    A magnetic storm, a temporary disturbance of the earth's magnetic field,
    induced by radiation and streams of charged particles from the sun.

    :ivar change_dst: Change in the disturbance  - storm time (Dst)
        index. The size of a geomagnetic storm is classified as: -
        moderate ( -50 nT &amp;gt;minimum of Dst &amp;gt; -100 nT) -
        intense (-100 nT &amp;gt; minimum Dst &amp;gt; -250 nT) or -
        super-storm ( minimum of Dst &amp;lt; -250 nT).
    """
    change_dst: Optional[float] = field(
        default=None,
        metadata={
            "name": "changeDst",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Maintainer(AssetOrganisationRole):
    """
    Organisation that maintains assets.
    """


@dataclass
class MaintenanceDataSet(ProcedureDataSet):
    """
    The result of a maintenance activity, a type of Procedure, for a given
    attribute of an asset.

    :ivar condition_after: Condition of asset just following maintenance
        procedure.
    :ivar condition_before: Description of the condition of the asset
        just prior to maintenance being performed.
    :ivar maint_code: Code for the type of maintenance performed.
    """
    condition_after: Optional[str] = field(
        default=None,
        metadata={
            "name": "conditionAfter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    condition_before: Optional[str] = field(
        default=None,
        metadata={
            "name": "conditionBefore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maint_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "maintCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """
    An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves)
    versus time (X-axis) for non-conforming loads, e.g., large industrial load
    or power station service (where modeled).

    :ivar non_conform_load_group: The NonConformLoadGroup where the
        NonConformLoadSchedule belongs.
    """
    non_conform_load_group: Optional["NonConformLoadGroup"] = field(
        default=None,
        metadata={
            "name": "NonConformLoadGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Operator(OperationPersonRole):
    """
    Control room operator.
    """


@dataclass
class Procedure(Document):
    """
    Documented procedure for various types of work or work tasks on assets.

    :ivar instruction: Textual description of this procedure.
    :ivar kind: Kind of procedure.
    :ivar sequence_number: Sequence number in a sequence of procedures
        being performed.
    :ivar assets: All assets to which this procedure applies.
    :ivar limits:
    :ivar measurements: Document containing this measurement.
    :ivar procedure_data_sets: All data sets captured by this procedure.
    """
    instruction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    kind: Optional[ProcedureKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    limits: List[Limit] = field(
        default_factory=list,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurements: List["Measurement"] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    procedure_data_sets: List[ProcedureDataSet] = field(
        default_factory=list,
        metadata={
            "name": "ProcedureDataSets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ProductAssetModel(IdentifiedObject):
    """
    Asset model by a specific manufacturer.

    :ivar catalogue_number: Catalogue number for asset model.
    :ivar corporate_standard_kind: Kind of corporate standard for this
        asset model.
    :ivar drawing_number: Drawing number for asset model.
    :ivar instruction_manual: Reference manual or instruction book for
        this asset model.
    :ivar model_number: Manufacturer's model number.
    :ivar model_version: Version number for product model, which
        indicates vintage of the product.
    :ivar overall_length: Overall length of this asset model.
    :ivar style_number: Style number of asset model.
    :ivar usage_kind: Intended usage for this asset model.
    :ivar asset: An asset of this model.
    :ivar asset_info:
    :ivar catalog_asset_type:
    :ivar manufacturer: Manufacturer of this asset model.
    """
    catalogue_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "catalogueNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    corporate_standard_kind: Optional[CorporateStandardKind] = field(
        default=None,
        metadata={
            "name": "corporateStandardKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    drawing_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "drawingNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    instruction_manual: Optional[str] = field(
        default=None,
        metadata={
            "name": "instructionManual",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    model_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    model_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelVersion",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overall_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "overallLength",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    style_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "styleNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_kind: Optional[AssetModelUsageKind] = field(
        default=None,
        metadata={
            "name": "usageKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_info: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "name": "AssetInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    catalog_asset_type: Optional[CatalogAssetType] = field(
        default=None,
        metadata={
            "name": "CatalogAssetType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    manufacturer: Optional[Manufacturer] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class RaiseLowerCommand(AnalogControl):
    """An analog control that increase or decrease a set point value with
    pulses.

    Unless otherwise specified, one pulse moves the set point by one.

    :ivar value_alias_set: The ValueAliasSet used for translation of a
        Control value to a name.
    """
    value_alias_set: Optional["ValueAliasSet"] = field(
        default=None,
        metadata={
            "name": "ValueAliasSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Reading(BaseReading):
    """Specific value measured by a meter or other asset, or calculated by a
    system.

    Each Reading is associated with a specific ReadingType.

    :ivar reason: Reason for this reading being taken.
    :ivar meter_readings: All meter readings (sets of values) containing
        this reading value.
    :ivar reading_type: Type information for this reading value.
    """
    reason: Optional[ReadingReasonKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter_readings: List["MeterReading"] = field(
        default_factory=list,
        metadata={
            "name": "MeterReadings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reading_type: Optional["ReadingType"] = field(
        default=None,
        metadata={
            "name": "ReadingType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltage_control_zones: List["VoltageControlZone"] = field(
        default_factory=list,
        metadata={
            "name": "VoltageControlZones",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class SetPoint(AnalogControl):
    """
    An analog control that issue a set point value.

    :ivar normal_value: Normal value for Control.value e.g. used for
        percentage scaling.
    :ivar value: The value representing the actuator output.
    """
    normal_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "normalValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class SwitchSchedule(SeasonDayTypeSchedule):
    """A schedule of switch positions.

    If RegularTimePoint.value1 is 0, the switch is open.  If 1, the
    switch is closed.

    :ivar switch: A SwitchSchedule is associated with a Switch.
    """
    switch: Optional["Switch"] = field(
        default=None,
        metadata={
            "name": "Switch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TestDataSet(ProcedureDataSet):
    """
    Test results, usually obtained by a lab or other independent organisation.

    :ivar conclusion: Conclusion drawn from test results.
    :ivar specimen_id: Identifier of specimen used in inspection or
        test.
    :ivar specimen_to_lab_date_time: Date and time the specimen was
        received by the lab.
    """
    conclusion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimen_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "specimenID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimen_to_lab_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "specimenToLabDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar angle_ref_topological_island: The island for which the node is
        an angle reference.   Normally there is one angle reference node
        for each island.
    :ivar base_voltage: The base voltage of the topologocial node.
    :ivar bus_name_marker: BusnameMarkers that may refer to a pre
        defined TopologicalNode.
    :ivar connectivity_node_container: The connectivity node container
        to which the toplogical node belongs.
    :ivar connectivity_nodes: The connectivity nodes combine together to
        form this topological node.  May depend on the current state of
        switches in the network.
    :ivar reporting_group: The reporting group to which the topological
        node belongs.
    :ivar sv_injection: The injection flows state variables associated
        with the topological node.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q_injection: Optional[float] = field(
        default=None,
        metadata={
            "name": "qInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    angle_ref_topological_island: Optional[TopologicalIsland] = field(
        default=None,
        metadata={
            "name": "AngleRefTopologicalIsland",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    base_voltage: Optional[BaseVoltage] = field(
        default=None,
        metadata={
            "name": "BaseVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    bus_name_marker: List["BusNameMarker"] = field(
        default_factory=list,
        metadata={
            "name": "BusNameMarker",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    connectivity_node_container: Optional["ConnectivityNodeContainer"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNodeContainer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    connectivity_nodes: List["ConnectivityNode"] = field(
        default_factory=list,
        metadata={
            "name": "ConnectivityNodes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reporting_group: Optional["ReportingGroup"] = field(
        default=None,
        metadata={
            "name": "ReportingGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_injection: List["SvInjection"] = field(
        default_factory=list,
        metadata={
            "name": "SvInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_voltage: List[SvVoltage] = field(
        default_factory=list,
        metadata={
            "name": "SvVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminal: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    topological_island: Optional[TopologicalIsland] = field(
        default=None,
        metadata={
            "name": "TopologicalIsland",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Tornado(AtmosphericPhenomenon):
    """
    A tornado, a violent destructive whirling wind accompanied by a funnel-
    shaped cloud that progresses in a narrow path over the land.

    :ivar f_scale: Fujita scale (referred to as EF-scale starting in
        2007) for the tornado.
    :ivar width: Width of the tornado during the time interval.
    """
    f_scale: Optional[Fscale] = field(
        default=None,
        metadata={
            "name": "fScale",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Tsunami(HydrosphericPhenomenon):
    """
    A tsunami (tidal wave), a long high sea wave caused by an earthquake,
    submarine landslide, or other disturbance.

    :ivar intensity: Tsunami intensity on the Papadopoulos-Imamura
        tsunami intensity scale. Possible values are 1-12, corresponding
        to I-XII.
    :ivar magnitude: Tsunami magnitude in the Tsunami Magnitude Scale
        (Mt).  Is greater than zero.
    """
    intensity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    magnitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VolcanicAshCloud(AtmosphericPhenomenon):
    """
    An ash cloud formed as a result of a volcanic eruption.

    :ivar density: Particulate density of the ash cloud during the time
        interval.
    :ivar particle_size: The diameter of the particles during the time
        interval.
    """
    density: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    particle_size: Optional[float] = field(
        default=None,
        metadata={
            "name": "particleSize",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Whirlpool(HydrosphericPhenomenon):
    """
    A whirlpool, a rapidly rotating mass of water in a river or sea into which
    objects may be drawn, typically caused by the meeting of conflicting
    currents.
    """


@dataclass
class ActivityRecord(IdentifiedObject):
    """
    Records activity for an entity at a point in time; activity may be for an
    event that has already occurred or for a planned activity.

    :ivar created_date_time: Date and time this activity record has been
        created (different from the 'status.dateTime', which is the time
        of a status change of the associated object, if applicable).
    :ivar reason: Reason for event resulting in this activity record,
        typically supplied when user initiated.
    :ivar severity: Severity level of event resulting in this activity
        record.
    :ivar type: Type of event resulting in this activity record.
    :ivar assets: All assets for which this activity record has been
        created.
    :ivar author: Author of this activity record.
    :ivar status: Information on consequence of event resulting in this
        activity record.
    """
    created_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    severity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    author: Optional[Author] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ConformLoadGroup(LoadGroup):
    """
    A group of loads conforming to an allocation pattern.

    :ivar conform_load_schedules: The ConformLoadSchedules in the
        ConformLoadGroup.
    :ivar energy_consumers: Conform loads assigned to this
        ConformLoadGroup.
    """
    conform_load_schedules: List[ConformLoadSchedule] = field(
        default_factory=list,
        metadata={
            "name": "ConformLoadSchedules",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    energy_consumers: List["ConformLoad"] = field(
        default_factory=list,
        metadata={
            "name": "EnergyConsumers",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Customer(OrganisationRole):
    """
    Organisation receiving services from service supplier.

    :ivar kind: Kind of customer.
    :ivar locale: Locale designating language to use in communications
        with this customer.
    :ivar puc_number: (if applicable) Public utilities commission (PUC)
        identification number.
    :ivar special_need: True if customer organisation has special
        service needs such as life support, hospitals, etc.
    :ivar vip: (use 'priority' instead) True if this is an important
        customer. Importance is for matters different than those in
        'specialNeed' attribute.
    :ivar customer_accounts: All accounts of this customer.
    :ivar customer_agreements: All agreements of this customer.
    :ivar customer_notifications: All notifications required by this
        customer.
    :ivar end_devices: All end devices of this customer.
    :ivar priority: Priority of the customer.
    :ivar status: Status of this customer.
    :ivar trouble_tickets: All trouble tickets for this customer.
    """
    kind: Optional[CustomerKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    locale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    puc_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "pucNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    special_need: Optional[str] = field(
        default=None,
        metadata={
            "name": "specialNeed",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    vip: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_accounts: List[CustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccounts",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_agreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAgreements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_notifications: List[CustomerNotification] = field(
        default_factory=list,
        metadata={
            "name": "CustomerNotifications",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_devices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    priority: Optional[Priority] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    trouble_tickets: List[TroubleTicket] = field(
        default_factory=list,
        metadata={
            "name": "TroubleTickets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    demand_response_programs: List[DemandResponseProgram] = field(
        default_factory=list,
        metadata={
            "name": "DemandResponsePrograms",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    derfunction: Optional[Derfunction] = field(
        default=None,
        metadata={
            "name": "DERFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dergroup_dispatch: List[DergroupDispatch] = field(
        default_factory=list,
        metadata={
            "name": "DERGroupDispatch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dergroup_forecast: List[DergroupForecast] = field(
        default_factory=list,
        metadata={
            "name": "DERGroupForecast",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    dermonitorable_parameter: List[DermonitorableParameter] = field(
        default_factory=list,
        metadata={
            "name": "DERMonitorableParameter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dispatchable_power_capability: Optional["DispatchablePowerCapability"] = field(
        default=None,
        metadata={
            "name": "DispatchablePowerCapability",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_controls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_devices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Hurricane(Cyclone):
    """
    A hurricane, a subtype of cyclone occurring in the North Atlantic Ocean or
    North-eastern Pacific Ocean whose intensity is measured using the Saffir-
    Simpson Hurricane Scale.

    :ivar category: The hurricane's category during the time interval,
        using Saffir-Simpson Hurricane Wind Scale, a 1 to 5 rating based
        on a hurricane's sustained wind speed.
    """
    category: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar procedures: Measurements are specified in types of documents,
        such as procedures.
    :ivar terminal: One or more measurements may be associated with a
        terminal in the network.
    """
    measurement_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phases: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    locations: List["Location"] = field(
        default_factory=list,
        metadata={
            "name": "Locations",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_system_resource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
            "name": "PowerSystemResource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    procedures: List[Procedure] = field(
        default_factory=list,
        metadata={
            "name": "Procedures",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminal: Optional["Acdcterminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class NonConformLoadGroup(LoadGroup):
    """
    Loads that do not follow a daily and seasonal load variation pattern.

    :ivar energy_consumers: Conform loads assigned to this
        ConformLoadGroup.
    :ivar non_conform_load_schedules: The NonConformLoadSchedules in the
        NonConformLoadGroup.
    """
    energy_consumers: List["NonConformLoad"] = field(
        default_factory=list,
        metadata={
            "name": "EnergyConsumers",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    non_conform_load_schedules: List[NonConformLoadSchedule] = field(
        default_factory=list,
        metadata={
            "name": "NonConformLoadSchedules",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class Ownership(IdentifiedObject):
    """
    Ownership of e.g. asset.

    :ivar share: Share of this ownership.
    :ivar asset: Asset that is object of this ownership.
    :ivar asset_owner: Asset owner that is subject in this ownership.
    """
    share: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_owner: Optional[AssetOwner] = field(
        default=None,
        metadata={
            "name": "AssetOwner",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ReadingType(IdentifiedObject):
    """Detailed description for a type of a reading value.

    Values in attributes allow for the creation of recommended codes to be used for identifying reading value types as follows: &amp;lt;macroPeriod&amp;gt;.&amp;lt;aggregate&amp;gt;.&amp;lt;measuringPeriod&amp;gt;.&amp;lt;accumulation&amp;gt;.&amp;lt;flowDirection&amp;gt;.&amp;lt;commodity&amp;gt;.&amp;lt;measurementKind&amp;gt;.&amp;lt;interharmonic.numerator&amp;gt;.&amp;lt;interharmonic.denominator&amp;gt;.&amp;lt;argument.numerator&amp;gt;.&amp;lt;argument.denominator&amp;gt;.&amp;lt;tou&amp;gt;.&amp;lt;cpp&amp;gt;.&amp;lt;consumptionTier&amp;gt;.&amp;lt;phases&amp;gt;.&amp;lt;multiplier&amp;gt;.&amp;lt;unit&amp;gt;.&amp;lt;currency&amp;gt;.

    :ivar accumulation: Accumulation behaviour of a reading over time,
        usually 'measuringPeriod', to be used with individual endpoints
        (as opposed to 'macroPeriod' and 'aggregate' that are used to
        describe aggregations of data from individual endpoints).
    :ivar aggregate: Salient attribute of the reading data aggregated
        from individual endpoints. This is mainly used to define a
        mathematical operation carried out over 'macroPeriod', but may
        also be used to describe an attribute of the data when the
        'macroPeriod' is not defined.
    :ivar commodity: Commodity being measured.
    :ivar consumption_tier: In case of common flat-rate pricing for
        power, in which all purchases are at a given rate,
        'consumptionTier'=0. Otherwise, the value indicates the
        consumption tier, which can be used in conjunction with TOU or
        CPP pricing. Consumption tier pricing refers to the method of
        billing in which a certain "block" of energy is purchased/sold
        at one price, after which the next block of energy is purchased
        at another price, and so on, all throughout a defined period. At
        the start of the defined period, consumption is initially zero,
        and any usage is measured against the first consumption tier
        ('consumptionTier'=1). If this block of energy is consumed
        before the end of the period, energy consumption moves to be
        reconed against the second consumption tier
        ('consumptionTier'=2), and so on. At the end of the defined
        period, the consumption accumulator is reset, and usage within
        the 'consumptionTier'=1 restarts.
    :ivar cpp: Critical peak period (CPP) bucket the reading value is
        attributed to. Value 0 means not applicable. Even though CPP is
        usually considered a specialised form of time of use 'tou', this
        attribute is defined explicitly for flexibility.
    :ivar currency: Metering-specific currency.
    :ivar flow_direction: Flow direction for a reading where the
        direction of flow of the commodity is important (for electricity
        measurements this includes current, energy, power, and demand).
    :ivar macro_period: Time period of interest that reflects how the
        reading is viewed or captured over a long period of time.
    :ivar measurement_kind: Identifies "what" is being measured, as
        refinement of 'commodity'. When combined with 'unit', it
        provides detail to the unit of measure. For example, 'energy'
        with a unit of measure of 'kWh' indicates to the user that
        active energy is being measured, while with 'kVAh' or 'kVArh',
        it indicates apparent energy and reactive energy, respectively.
        'power' can be combined in a similar way with various power
        units of measure: Distortion power ('distortionVoltAmperes')
        with 'kVA' is different from 'power' with 'kVA'.
    :ivar measuring_period: Time attribute inherent or fundamental to
        the reading value (as opposed to 'macroPeriod' that supplies an
        "adjective" to describe aspects of a time period with regard to
        the measurement). It refers to the way the value was originally
        measured and not to the frequency at which it is reported or
        presented. For example, an hourly interval of consumption data
        would have value 'hourly' as an attribute. However in the case
        of an hourly sampled voltage value, the meterReadings schema
        would carry the 'hourly' interval size information. It is common
        for meters to report demand in a form that is measured over the
        course of a portion of an hour, while enterprise applications
        however commonly assume the demand (in kW or kVAr) normalised to
        1 hour. The system that receives readings directly from the
        meter therefore shall perform this transformation before
        publishing readings for use by the other enterprise systems. The
        scalar used is chosen based on the block size (not any sub-
        interval size).
    :ivar multiplier: Metering-specific multiplier.
    :ivar phases: Metering-specific phase code.
    :ivar tou: Time of use (TOU) bucket the reading value is attributed
        to. Value 0 means not applicable.
    :ivar unit: Metering-specific unit.
    :ivar argument: Argument used to introduce numbers into the unit of
        measure description where they are needed (e.g., 4 where the
        measure needs an argument such as CEMI(n=4)). Most arguments
        used in practice however will be integers (i.e.,
        'denominator'=1). Value 0 in 'numerator' and 'denominator' means
        not applicable.
    :ivar channel: Channel reporting/collecting register values with
        this type information.
    :ivar interharmonic: Indication of a "harmonic" or "interharmonic"
        basis for the measurement. Value 0 in 'numerator' and
        'denominator' means not applicable.
    :ivar interval_blocks: All blocks containing interval reading values
        with this type information.
    :ivar metrology_requirements: All metrology requirements that
        require this reading type to be collected.
    :ivar pending_calculation: Pending calculation that produced this
        reading type.
    :ivar readings: All reading values with this type information.
    """
    accumulation: Optional[AccumulationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    aggregate: Optional[AggregateKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    commodity: Optional[CommodityKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    consumption_tier: Optional[int] = field(
        default=None,
        metadata={
            "name": "consumptionTier",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cpp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    flow_direction: Optional[FlowDirectionKind] = field(
        default=None,
        metadata={
            "name": "flowDirection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    macro_period: Optional[MacroPeriodKind] = field(
        default=None,
        metadata={
            "name": "macroPeriod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurement_kind: Optional[MeasurementKind] = field(
        default=None,
        metadata={
            "name": "measurementKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measuring_period: Optional[MeasuringPeriodKind] = field(
        default=None,
        metadata={
            "name": "measuringPeriod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phases: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tou: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    argument: Optional[RationalNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    channel: Optional[Channel] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    interharmonic: Optional[ReadingInterharmonic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    interval_blocks: List["IntervalBlock"] = field(
        default_factory=list,
        metadata={
            "name": "IntervalBlocks",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    metrology_requirements: List[MetrologyRequirement] = field(
        default_factory=list,
        metadata={
            "name": "MetrologyRequirements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pending_calculation: Optional["PendingCalculation"] = field(
        default=None,
        metadata={
            "name": "PendingCalculation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    readings: List[Reading] = field(
        default_factory=list,
        metadata={
            "name": "Readings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class RiskScore(AggregateScore):
    """
    Score that is indicative of the risk associated with one or more assets.

    :ivar kind: The risk kind, such as CustomerRisk, FinancialRisk,
        SafetyRisk, etc.
    :ivar asset_health_score: Individual health score associated with
        this risk score.
    """
    kind: Optional[RiskScoreKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_health_score: List["HealthScore"] = field(
        default_factory=list,
        metadata={
            "name": "AssetHealthScore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ScheduledEventData:
    """
    Schedule parameters for an activity that is to occur, is occurring, or has
    completed.

    :ivar estimated_window: Estimated date and time for activity
        execution (with earliest possibility of activity initiation and
        latest possibility of activity completion).
    :ivar inspection_data_set:
    :ivar requested_window: Requested date and time interval for
        activity execution.
    :ivar scheduled_events: All scheduled events with this
        specification.
    :ivar status:
    """
    estimated_window: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "estimatedWindow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    inspection_data_set: Optional[InspectionDataSet] = field(
        default=None,
        metadata={
            "name": "InspectionDataSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    requested_window: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "requestedWindow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scheduled_events: List["ScheduledEvent"] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Specimen(IdentifiedObject):
    """
    Sample or specimen of a material (fluid or solid).

    :ivar ambient_temperature_at_sampling: Operating ambient temperature
        (in ï¿½C).
    :ivar humidity_at_sampling: Operating ambient humidity (in percent).
    :ivar specimen_id: Identifier of specimen used in inspection or
        test.
    :ivar specimen_sample_date_time: Date and time sample specimen
        taken.
    :ivar specimen_to_lab_date_time: Date and time the specimen was
        received by the lab.
    :ivar asset_test_sample_taker: Test sampler taker who gathered this
        specimen.
    :ivar lab_test_data_set: Results from lab testing done on specimen.
    """
    ambient_temperature_at_sampling: Optional[float] = field(
        default=None,
        metadata={
            "name": "ambientTemperatureAtSampling",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    humidity_at_sampling: Optional[float] = field(
        default=None,
        metadata={
            "name": "humidityAtSampling",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimen_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "specimenID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimen_sample_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "specimenSampleDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimen_to_lab_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "specimenToLabDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_test_sample_taker: Optional[AssetTestSampleTaker] = field(
        default=None,
        metadata={
            "name": "AssetTestSampleTaker",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lab_test_data_set: List["LabTestDataSet"] = field(
        default_factory=list,
        metadata={
            "name": "LabTestDataSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    p_injection: Optional[float] = field(
        default=None,
        metadata={
            "name": "pInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q_injection: Optional[float] = field(
        default=None,
        metadata={
            "name": "qInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    connectivity_node: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    topological_node: Optional[TopologicalNode] = field(
        default=None,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TropicalCycloneAustralia(Cyclone):
    """
    A tropical cyclone, a subtype of cyclone that forms to the east of 90ï¿½E
    in the Southern Hemisphere whose intensity is measured by the Australian
    tropical cyclone intensity scale.

    :ivar category: Strength of tropical cyclone during the time
        interval, based on Australian Bureau of Meteorology Category
        System where: 1 - tropical cyclone, with typical gusts over flat
        land 90-125 km/h 2 - tropical cyclone, with typical gusts over
        flat land 125-164 km/h 3 - severe tropical cyclone, with typical
        gusts over flat land 165-224 km/h 4 - severe tropical cyclone,
        with typical gusts over flat land 225-279 km/h 5 - severe
        tropical cyclone, with typical gusts over flat land greater
        than 280 km/h.
    """
    category: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ValueAliasSet(IdentifiedObject):
    """Describes the translation of a set of values into a name and is
    intendend to facilitate cusom translations.

    Each ValueAliasSet has a name, description etc. A specific
    Measurement may represent a discrete state like Open, Closed,
    Intermediate etc. This requires a translation from the
    MeasurementValue.value number to a string, e.g. 0-&amp;gt;"Invalid",
    1-&amp;gt;"Open", 2-&amp;gt;"Closed", 3-&amp;gt;"Intermediate". Each
    ValueToAlias member in ValueAliasSet.Value describe a mapping for
    one particular value to a name.

    :ivar commands: The Commands using the set for translation.
    :ivar discretes: The Measurements using the set for translation.
    :ivar raise_lower_commands: The Commands using the set for
        translation.
    :ivar values: The ValueToAlias mappings included in the set.
    """
    commands: List["Command"] = field(
        default_factory=list,
        metadata={
            "name": "Commands",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    discretes: List["Discrete"] = field(
        default_factory=list,
        metadata={
            "name": "Discretes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    raise_lower_commands: List[RaiseLowerCommand] = field(
        default_factory=list,
        metadata={
            "name": "RaiseLowerCommands",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    values: List[ValueToAlias] = field(
        default_factory=list,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class Accumulator(Measurement):
    """
    Accumulator represents an accumulated (counted) Measurement, e.g. an energy
    value.

    :ivar max_value: Normal value range maximum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar accumulator_values: The values connected to this measurement.
    :ivar limit_sets: A measurement may have zero or more limit ranges
        defined for it.
    """
    max_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    accumulator_values: List[AccumulatorValue] = field(
        default_factory=list,
        metadata={
            "name": "AccumulatorValues",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    limit_sets: List[AccumulatorLimitSet] = field(
        default_factory=list,
        metadata={
            "name": "LimitSets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Analog(Measurement):
    """
    Analog represents an analog Measurement.

    :ivar max_value: Normal value range maximum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar min_value: Normal value range minimum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar normal_value: Normal measurement value, e.g., used for
        percentage calculations.
    :ivar positive_flow_in: If true then this measurement is an active
        power, reactive power or current with the convention that a
        positive value measured at the Terminal means power is flowing
        into the related PowerSystemResource.
    :ivar analog_values: The values connected to this measurement.
    :ivar limit_sets: A measurement may have zero or more limit ranges
        defined for it.
    """
    max_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "minValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "normalValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    positive_flow_in: Optional[bool] = field(
        default=None,
        metadata={
            "name": "positiveFlowIn",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    analog_values: List[AnalogValue] = field(
        default_factory=list,
        metadata={
            "name": "AnalogValues",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    limit_sets: List[AnalogLimitSet] = field(
        default_factory=list,
        metadata={
            "name": "LimitSets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetHealthEvent(ActivityRecord):
    """An asset health-related event that is created by an analytic.

    The event is a record of a change in asset health.

    :ivar action_recommendation: Recommendation for action.
    :ivar action_timeline: Time horizon for action.
    :ivar effective_date_time: The date and time when the event is
        effective.
    :ivar analytic:
    """
    action_recommendation: Optional[str] = field(
        default=None,
        metadata={
            "name": "actionRecommendation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    action_timeline: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "actionTimeline",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    effective_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "effectiveDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    analytic: Optional["Analytic"] = field(
        default=None,
        metadata={
            "name": "Analytic",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    operational_limit_set: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimitSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_injection: List[SvInjection] = field(
        default_factory=list,
        metadata={
            "name": "SvInjection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_voltage: Optional[SvVoltage] = field(
        default=None,
        metadata={
            "name": "SvVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminals: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "name": "Terminals",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    topological_node: Optional[TopologicalNode] = field(
        default=None,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Discrete(Measurement):
    """
    Discrete represents a discrete Measurement, i.e. a Measurement representing
    discrete values, e.g. a Breaker position.

    :ivar max_value: Normal value range maximum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar min_value: Normal value range minimum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar normal_value: Normal measurement value, e.g., used for
        percentage calculations.
    :ivar discrete_values: The values connected to this measurement.
    :ivar value_alias_set: The ValueAliasSet used for translation of a
        MeasurementValue.value to a name.
    """
    max_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "minValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "normalValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    discrete_values: List["DiscreteValue"] = field(
        default_factory=list,
        metadata={
            "name": "DiscreteValues",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value_alias_set: Optional[ValueAliasSet] = field(
        default=None,
        metadata={
            "name": "ValueAliasSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    current_apparent_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "currentApparentPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    current_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "currentReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_active_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxActivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_apparent_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxApparentPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_active_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "minActivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_apparent_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "minApparentPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "minReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "name": "EndDevice",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_group: Optional[EndDeviceGroup] = field(
        default=None,
        metadata={
            "name": "EndDeviceGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FailureEvent(ActivityRecord):
    """An event where an asset has failed to perform its functions within
    specified parameters.

    This class is intended to reflect the failure itself. Additional
    information resulting from forensic analysis could be captured by a
    diagnosis data set.

    :ivar breaker_failure_reason: Reason for breaker failure.
    :ivar corporate_code: Code for asset failure.
    :ivar failure_classification: Classification of failure.
    :ivar failure_date_time: Time and date of asset failure.
    :ivar failure_isolation_method: How the asset failure was isolated
        from the system.
    :ivar failure_mode: What asset failed to be able to do.
    :ivar fault_locating_method: The method used for locating the
        faulted part of the asset. For example, cable options include:
        Cap Discharge-Thumping, Bridge Method, Visual Inspection, Other.
    :ivar location: Failure location on an object.
    :ivar root_cause: Root cause of asset failure.
    :ivar transformer_failure_reason: Reason for transformer failure.
    """
    breaker_failure_reason: Optional[BreakerFailureReasonKind] = field(
        default=None,
        metadata={
            "name": "breakerFailureReason",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    corporate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "corporateCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failure_classification: Optional[AssetFailureClassification] = field(
        default=None,
        metadata={
            "name": "failureClassification",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failure_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "failureDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failure_isolation_method: Optional[FailureIsolationMethodKind] = field(
        default=None,
        metadata={
            "name": "failureIsolationMethod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failure_mode: Optional[AssetFailureMode] = field(
        default=None,
        metadata={
            "name": "failureMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fault_locating_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "faultLocatingMethod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    root_cause: Optional[str] = field(
        default=None,
        metadata={
            "name": "rootCause",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_failure_reason: Optional[TransformerFailureReasonKind] = field(
        default=None,
        metadata={
            "name": "transformerFailureReason",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class HealthScore(AggregateScore):
    """
    Score that is indicative of the health of one or more assets.

    :ivar asset_risk_score: Risk score with which this health score is
        associated.
    """
    asset_risk_score: Optional[RiskScore] = field(
        default=None,
        metadata={
            "name": "AssetRiskScore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class LabTestDataSet(ProcedureDataSet):
    """
    Results of testing done by a lab.

    :ivar conclusion: Conclusion drawn from test results.
    :ivar conclusion_confidence: Description of confidence in
        conclusion.
    :ivar reason_for_test: Reason for performing test.
    :ivar test_equipment_id: Identity of lab equipment used to perform
        test.
    :ivar asset_test_lab: Test lab which produced this set of lab test
        results.
    :ivar specimen: Specimen on which lab testing done in determining
        results.
    """
    conclusion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    conclusion_confidence: Optional[str] = field(
        default=None,
        metadata={
            "name": "conclusionConfidence",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reason_for_test: Optional[TestReason] = field(
        default=None,
        metadata={
            "name": "reasonForTest",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test_equipment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "testEquipmentID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_test_lab: Optional["AssetTestLab"] = field(
        default=None,
        metadata={
            "name": "AssetTestLab",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimen: Optional[Specimen] = field(
        default=None,
        metadata={
            "name": "Specimen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Location(IdentifiedObject):
    """The place, scene, or point of something where someone or something has
    been, is, and/or will be at a given moment in time.

    It can be defined with one or more postition points (coordinates) in
    a given coordinate system.

    :ivar direction: (if applicable) Direction that allows field crews
        to quickly find a given asset. For a given location, such as a
        street address, this is the relative direction in which to find
        the asset. For example, a streetlight may be located at the 'NW'
        (northwest) corner of the customer's site, or a usage point may
        be located on the second floor of an apartment building.
    :ivar geo_info_reference: (if applicable) Reference to geographical
        information source, often external to the utility.
    :ivar type: Classification by utility's corporate standards and
        practices, relative to the location itself (e.g., geographical,
        functional accounting, etc., not a given property that happens
        to exist at that location).
    :ivar assets: All assets at this location.
    :ivar configuration_events: All configuration events created for
        this location.
    :ivar coordinate_system: Coordinate system used to describe position
        points of this location.
    :ivar crew:
    :ivar electronic_address: Electronic address.
    :ivar environmental_location_kind: Kind of environmental location
        which this location is.
    :ivar fault:
    :ivar hazards: All asset hazards at this location.
    :ivar main_address: Main address of the location.
    :ivar measurements:
    :ivar phone1: Phone number.
    :ivar phone2: Additional phone number.
    :ivar position_points: Sequence of position points describing this
        location, expressed in coordinate system
        'Location.CoordinateSystem'.
    :ivar power_system_resources: All power system resources at this
        location.
    :ivar secondary_address: Secondary address of the location. For
        example, PO Box address may have different ZIP code than that in
        the 'mainAddress'.
    :ivar status: Status of this location.
    """
    direction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    geo_info_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "geoInfoReference",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    configuration_events: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "CoordinateSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    crew: List[Crew] = field(
        default_factory=list,
        metadata={
            "name": "Crew",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    electronic_address: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "name": "electronicAddress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_location_kind: List[EnvironmentalLocationType] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalLocationKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fault: List[Fault] = field(
        default_factory=list,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hazards: List[AssetLocationHazard] = field(
        default_factory=list,
        metadata={
            "name": "Hazards",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    main_address: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "name": "mainAddress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phone1: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phone2: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    position_points: List[PositionPoint] = field(
        default_factory=list,
        metadata={
            "name": "PositionPoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_system_resources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "name": "PowerSystemResources",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    secondary_address: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "name": "secondaryAddress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OilSpecimen(Specimen):
    oil_sample_taken_from: Optional[OilSampleLocation] = field(
        default=None,
        metadata={
            "name": "oilSampleTakenFrom",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    oil_sample_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "oilSampleTemperature",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    oil_temperature_source: Optional[OilTemperatureSource] = field(
        default=None,
        metadata={
            "name": "oilTemperatureSource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sample_container: Optional[SampleContainerType] = field(
        default=None,
        metadata={
            "name": "sampleContainer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PendingCalculation:
    """When present, a scalar conversion that needs to be applied to every
    IntervalReading.value contained in IntervalBlock.

    This conversion results in a new associated ReadingType, reflecting
    the true dimensions of IntervalReading values after the conversion.

    :ivar multiply_before_add: Whether scalars should be applied before
        adding the 'offset'.
    :ivar offset: (if applicable) Offset to be added as well as
        multiplication using scalars.
    :ivar scalar_denominator: (if scalar is rational number) When
        'IntervalReading.value' is multiplied by 'scalarNumerator' and
        divided by this value, it causes a unit of measure conversion to
        occur, resulting in the 'ReadingType.unit'.
    :ivar scalar_float: (if scalar is floating number) When multiplied
        with 'IntervalReading.value', it causes a unit of measure
        conversion to occur, according to the 'ReadingType.unit'.
    :ivar scalar_numerator: (if scalar is integer or rational number)
        When the scalar is a simple integer, and this attribute is
        presented alone and multiplied with 'IntervalReading.value', it
        causes a unit of measure conversion to occur, resulting in the
        'ReadingType.unit'. It is never used in conjunction with
        'scalarFloat', only with 'scalarDenominator'.
    :ivar interval_blocks: All blocks of interval reading values to
        which this pending conversion applies.
    :ivar reading_type: Reading type resulting from this pending
        conversion.
    """
    multiply_before_add: Optional[bool] = field(
        default=None,
        metadata={
            "name": "multiplyBeforeAdd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scalar_denominator: Optional[int] = field(
        default=None,
        metadata={
            "name": "scalarDenominator",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scalar_float: Optional[float] = field(
        default=None,
        metadata={
            "name": "scalarFloat",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scalar_numerator: Optional[int] = field(
        default=None,
        metadata={
            "name": "scalarNumerator",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    interval_blocks: List["IntervalBlock"] = field(
        default_factory=list,
        metadata={
            "name": "IntervalBlocks",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reading_type: Optional[ReadingType] = field(
        default=None,
        metadata={
            "name": "ReadingType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar scheduled_event_data: Specification for this scheduled event.
    :ivar status:
    """
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scheduled_event_data: Optional[ScheduledEventData] = field(
        default=None,
        metadata={
            "name": "ScheduledEventData",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class StringMeasurement(Measurement):
    """
    StringMeasurement represents a measurement with values of type string.

    :ivar string_measurement_values: The values connected to this
        measurement.
    """
    string_measurement_values: List[StringMeasurementValue] = field(
        default_factory=list,
        metadata={
            "name": "StringMeasurementValues",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Analytic(Document):
    """
    An algorithm or calculation for making an assessment about an asset or
    asset grouping for lifecycle decision making.

    :ivar best_value: Value that indicates best possible numeric value.
    :ivar kind: Kind of analytic this analytic is.
    :ivar scale_kind: The scoring scale kind.
    :ivar worst_value: Value that indicates worst possible numeric
        value.
    :ivar analytic_score:
    :ivar asset:
    :ivar asset_group:
    :ivar asset_health_event:
    """
    best_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "bestValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    kind: Optional[AnalyticKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    scale_kind: Optional[ScaleKind] = field(
        default=None,
        metadata={
            "name": "scaleKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    worst_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "worstValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    analytic_score: List[AnalyticScore] = field(
        default_factory=list,
        metadata={
            "name": "AnalyticScore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Asset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_group: List[AssetGroup] = field(
        default_factory=list,
        metadata={
            "name": "AssetGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_health_event: List[AssetHealthEvent] = field(
        default_factory=list,
        metadata={
            "name": "AssetHealthEvent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetTestLab(AssetOrganisationRole):
    """
    Test lab that performs various types of testing related to assets.

    :ivar lab_test_data_set: A set of lab test results produced by this
        test lab.
    """
    lab_test_data_set: List[LabTestDataSet] = field(
        default_factory=list,
        metadata={
            "name": "LabTestDataSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class DiscreteValue(MeasurementValue):
    """
    DiscreteValue represents a discrete MeasurementValue.

    :ivar value: The value to supervise.
    :ivar command: The Control variable associated with the
        MeasurementValue.
    :ivar discrete: Measurement to which this value is connected.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    command: Optional["Command"] = field(
        default=None,
        metadata={
            "name": "Command",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    discrete: Optional[Discrete] = field(
        default=None,
        metadata={
            "name": "Discrete",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EnvironmentalStringMeasurement(StringMeasurement):
    """
    String measurement of relevance in the environmental domain.

    :ivar classification_condition: Classification condition which this
        string measurement helps define.
    :ivar environmental_information: Observation or forecast with which
        this environmental string is associated.
    """
    classification_condition: Optional["ClassificationCondition"] = field(
        default=None,
        metadata={
            "name": "ClassificationCondition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_information: Optional["EnvironmentalInformation"] = field(
        default=None,
        metadata={
            "name": "EnvironmentalInformation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class IntervalBlock:
    """Time sequence of readings of the same reading type.

    Contained interval readings may need conversion through the
    application of an offset and a scalar defined in associated pending.

    :ivar interval_readings: Interval reading contained in this block.
    :ivar meter_reading: Meter reading containing this interval block.
    :ivar pending_calculation: Pending calculation to apply to interval
        reading values contained by this block (after which the
        resulting reading type is different than the original because it
        reflects the conversion result).
    :ivar reading_type: Type information for interval reading values
        contained in this block.
    """
    interval_readings: List[IntervalReading] = field(
        default_factory=list,
        metadata={
            "name": "IntervalReadings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter_reading: Optional["MeterReading"] = field(
        default=None,
        metadata={
            "name": "MeterReading",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pending_calculation: Optional[PendingCalculation] = field(
        default=None,
        metadata={
            "name": "PendingCalculation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reading_type: Optional[ReadingType] = field(
        default=None,
        metadata={
            "name": "ReadingType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class UsagePointLocation(Location):
    """
    Location of an individual usage point.

    :ivar access_method: Method for the service person to access this
        usage point location. For example, a description of where to
        obtain a key if the facility is unmanned and secured.
    :ivar remark: Remarks about this location.
    :ivar site_access_problem: Problems previously encountered when
        visiting or performing work at this location. Examples include:
        bad dog, violent customer, verbally abusive occupant,
        obstructions, safety hazards, etc.
    :ivar usage_points: All usage points at this location.
    """
    access_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "accessMethod",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    site_access_problem: Optional[str] = field(
        default=None,
        metadata={
            "name": "siteAccessProblem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Command(Control):
    """
    A Command is a discrete control used for supervisory control.

    :ivar normal_value: Normal value for Control.value e.g. used for
        percentage scaling.
    :ivar value: The value representing the actuator output.
    :ivar discrete_value: The MeasurementValue that is controlled.
    :ivar value_alias_set: The ValueAliasSet used for translation of a
        Control value to a name.
    """
    normal_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "normalValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    discrete_value: Optional[DiscreteValue] = field(
        default=None,
        metadata={
            "name": "DiscreteValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value_alias_set: Optional[ValueAliasSet] = field(
        default=None,
        metadata={
            "name": "ValueAliasSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalInformation(IdentifiedObject):
    """
    Abstract class (with concrete child classes of Observation and Forecast)
    that groups phenomenon and/or environmental value sets.

    :ivar created: The timestamp of when the forecast was created
    :ivar environmental_analog: Environmental analog associated with
        this observation or forecast.
    :ivar environmental_data_provider: Environmental data provider
        supplying this environmental information.
    :ivar environmental_phenomenon:
    :ivar environmental_string_measurement: Environmental string
        measurement associated with this forecast or observation.
    """
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_analog: List["EnvironmentalAnalog"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalAnalog",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_data_provider: Optional[EnvironmentalDataProvider] = field(
        default=None,
        metadata={
            "name": "EnvironmentalDataProvider",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_phenomenon: List[EnvironmentalPhenomenon] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalPhenomenon",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_string_measurement: List[EnvironmentalStringMeasurement] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalStringMeasurement",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class MeterReading(IdentifiedObject):
    """
    Set of values obtained from the meter.

    :ivar is_coincident_trigger: If true, this meter reading is the
        meter reading for which other coincident meter readings are
        requested or provided.
    :ivar customer_agreement: (could be deprecated in the future)
        Customer agreement for this meter reading.
    :ivar end_device_events: All end device events associated with this
        set of measured values.
    :ivar interval_blocks: All interval blocks contained in this meter
        reading.
    :ivar meter: Meter providing this reading.
    :ivar readings: All reading values contained within this meter
        reading.
    :ivar usage_point: Usage point from which this meter reading (set of
        values) has been obtained.
    :ivar values_interval: Date and time interval of the data items
        contained within this meter reading.
    """
    is_coincident_trigger: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isCoincidentTrigger",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_agreement: Optional["CustomerAgreement"] = field(
        default=None,
        metadata={
            "name": "CustomerAgreement",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_events: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    interval_blocks: List[IntervalBlock] = field(
        default_factory=list,
        metadata={
            "name": "IntervalBlocks",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter: Optional["Meter"] = field(
        default=None,
        metadata={
            "name": "Meter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    readings: List[Reading] = field(
        default_factory=list,
        metadata={
            "name": "Readings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_point: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "name": "UsagePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    values_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "valuesInterval",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CustomerAgreement(Agreement):
    """Agreement between the customer and the service supplier to pay for
    service at a specific service location.

    It records certain billing information about the type of service
    provided at the service location and is used during charge creation
    to determine the type of service.

    :ivar is_pre_pay: If true, the customer is a pre-pay customer for
        the specified service.
    :ivar load_mgmt: Load management code.
    :ivar shut_off_date_time: Final date and time the service will be
        billed to the previous customer.
    :ivar customer: Customer for this agreement.
    :ivar customer_account: Customer account owning this agreement.
    :ivar demand_response_programs: All demand response programs the
        customer is enrolled in through this customer agreement.
    :ivar meter_readings: (could be deprecated in the future) All meter
        readings for this customer agreement.
    :ivar pricing_structures: All pricing structures applicable to this
        customer agreement.
    :ivar service_category: Service category for this agreement.
    :ivar service_locations: All service locations regulated by this
        customer agreement.
    :ivar usage_points: All service delivery points regulated by this
        customer agreement.
    """
    is_pre_pay: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPrePay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    load_mgmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "loadMgmt",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shut_off_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "shutOffDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer: Optional[Customer] = field(
        default=None,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    customer_account: Optional[CustomerAccount] = field(
        default=None,
        metadata={
            "name": "CustomerAccount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    demand_response_programs: List[DemandResponseProgram] = field(
        default_factory=list,
        metadata={
            "name": "DemandResponsePrograms",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter_readings: List[MeterReading] = field(
        default_factory=list,
        metadata={
            "name": "MeterReadings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pricing_structures: List[PricingStructure] = field(
        default_factory=list,
        metadata={
            "name": "PricingStructures",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_category: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "name": "ServiceCategory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_locations: List[ServiceLocation] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLocations",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_points: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class DiscreteCommand(Command):
    pass


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    issuer_tracking_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerTrackingID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "userID",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "name": "EndDevice",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_event_details: List[EndDeviceEventDetail] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEventDetails",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_event_type: Optional[EndDeviceEventType] = field(
        default=None,
        metadata={
            "name": "EndDeviceEventType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    meter_reading: Optional[MeterReading] = field(
        default=None,
        metadata={
            "name": "MeterReading",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_point: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "name": "UsagePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalAnalog(Analog):
    """
    Analog measurement of relevance in the environmental domain.

    :ivar classification_condition: Classification condition which this
        analog helps define.
    :ivar environmental_information: Observation or forecast with which
        this environmental analog measurement is associated.
    :ivar reporting_capability: The reporting capability this
        environmental value set helps define.
    """
    classification_condition: Optional["ClassificationCondition"] = field(
        default=None,
        metadata={
            "name": "ClassificationCondition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_information: Optional[EnvironmentalInformation] = field(
        default=None,
        metadata={
            "name": "EnvironmentalInformation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reporting_capability: Optional[ReportingCapability] = field(
        default=None,
        metadata={
            "name": "ReportingCapability",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Forecast(EnvironmentalInformation):
    """
    A forecast group of value sets and/or phenomena.

    :ivar valid_for: The interval for which the forecast is valid.  For
        example, a forecast issued now for tomorrow might be valid for
        the next 2 hours.
    """
    valid_for: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "validFor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Observation(EnvironmentalInformation):
    """
    Observed (actual non-forecast) values sets and/or phenomena.
    """
    environmental_event: List["EnvironmentalEvent"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalEvent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AtmosphericAnalog(EnvironmentalAnalog):
    """
    Analog measuring an atmospheric condition.

    :ivar kind: Kind of atmospheric analog.
    """
    kind: Optional[AtmosphericAnalogKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ClassificationCondition(IdentifiedObject):
    """
    A classification condition used to define preconditions that must be met by
    a phenomena classification.

    :ivar duration: The duration of the of the condition in seconds
    :ivar test: The test applied to the value.
    :ivar environmental_analog: Analog which contributes to the
        definition of this classification condition.
    :ivar environmental_string_measurement: String measurement which
        contributes to the definition of this classification condition.
    :ivar phenomenon_classification: Phenomenon classification to which
        this condition relates.
    """
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    test: Optional[TestKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_analog: List[EnvironmentalAnalog] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalAnalog",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_string_measurement: List[EnvironmentalStringMeasurement] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalStringMeasurement",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phenomenon_classification: Optional["PhenomenonClassification"] = field(
        default=None,
        metadata={
            "name": "PhenomenonClassification",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalEvent(ActivityRecord):
    """
    An environmental event tied to an observation that will be recorded against
    or affect one or more assets.
    """
    observation: List[Observation] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class GeosphericAnalog(EnvironmentalAnalog):
    """
    Analog measuring a geospheric condition.

    :ivar kind: Kind of geospheric analog.
    """
    kind: Optional[GeosphericAnalogKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class HydrosphericAnalog(EnvironmentalAnalog):
    """
    Analog measuring a hydrospheric condition.

    :ivar kind: Kind of hydrospheric analog.
    """
    kind: Optional[HydrosphericAnalogKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class SpaceAnalog(EnvironmentalAnalog):
    """
    Analog measuring a space (extra-terrestrial) condition.

    :ivar kind: Kind of space analog.
    """
    kind: Optional[SpaceAnalogKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


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
    :ivar configuration_events: All configuration events created for
        this usage point.
    :ivar customer_agreement: Customer agreement regulating this service
        delivery point.
    :ivar end_device_controls: All end device controls sending commands
        to this usage point.
    :ivar end_device_events: All end device events reported for this
        usage point.
    :ivar end_devices: All end devices at this usage point.
    :ivar equipments: All equipment connecting this usage point to the
        electrical grid.
    :ivar meter_readings: All meter readings obtained from this usage
        point.
    :ivar meter_service_work_tasks: All meter service work tasks at this
        usage point.
    :ivar metrology_requirements: All metrology requirements for this
        usage point.
    :ivar pricing_structures: All pricing structures applicable to this
        service delivery point (with prepayment meter running as a
        stand-alone device, with no CustomerAgreement or Customer).
    :ivar service_category: Service category delivered by this usage
        point.
    :ivar service_location: Service location where the service delivered
        by this usage point is consumed.
    :ivar service_multipliers: All multipliers applied at this usage
        point.
    :ivar usage_point_groups: All groups to which this usage point
        belongs.
    :ivar usage_point_location: Location of this usage point.
    """
    ami_billing_ready: Optional[AmiBillingReadyKind] = field(
        default=None,
        metadata={
            "name": "amiBillingReady",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    check_billing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "checkBilling",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    connection_state: Optional[UsagePointConnectedKind] = field(
        default=None,
        metadata={
            "name": "connectionState",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    estimated_load: Optional[float] = field(
        default=None,
        metadata={
            "name": "estimatedLoad",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_sdp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSdp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_virtual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isVirtual",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimal_usage_expected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "minimalUsageExpected",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominal_service_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalServiceVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    outage_region: Optional[str] = field(
        default=None,
        metadata={
            "name": "outageRegion",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_code: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "name": "phaseCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    read_cycle: Optional[str] = field(
        default=None,
        metadata={
            "name": "readCycle",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    read_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "readRoute",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_delivery_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceDeliveryRemark",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_priority: Optional[str] = field(
        default=None,
        metadata={
            "name": "servicePriority",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    configuration_events: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer_agreement: Optional[CustomerAgreement] = field(
        default=None,
        metadata={
            "name": "CustomerAgreement",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_controls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_events: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_devices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    equipments: List["Equipment"] = field(
        default_factory=list,
        metadata={
            "name": "Equipments",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter_readings: List[MeterReading] = field(
        default_factory=list,
        metadata={
            "name": "MeterReadings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter_service_work_tasks: List[MeterWorkTask] = field(
        default_factory=list,
        metadata={
            "name": "MeterServiceWorkTasks",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    metrology_requirements: List[MetrologyRequirement] = field(
        default_factory=list,
        metadata={
            "name": "MetrologyRequirements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pricing_structures: List[PricingStructure] = field(
        default_factory=list,
        metadata={
            "name": "PricingStructures",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_category: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "name": "ServiceCategory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_location: Optional[ServiceLocation] = field(
        default=None,
        metadata={
            "name": "ServiceLocation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_multipliers: List[ServiceMultiplier] = field(
        default_factory=list,
        metadata={
            "name": "ServiceMultipliers",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_point_groups: List[UsagePointGroup] = field(
        default_factory=list,
        metadata={
            "name": "UsagePointGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_point_location: Optional["UsagePointLocation"] = field(
        default=None,
        metadata={
            "name": "UsagePointLocation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar changed_document: Document whose change resulted in this
        configuration event.
    :ivar changed_location: Location whose change resulted in this
        configuration event.
    :ivar changed_organisation_role: Organisation role whose change
        resulted in this configuration event.
    :ivar changed_person_role: Person role whose change resulted in this
        configuration event.
    :ivar changed_service_category: Service category whose change
        resulted in this configuration event.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    modified_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "modifiedBy",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    changed_asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "name": "ChangedAsset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    changed_document: Optional[Document] = field(
        default=None,
        metadata={
            "name": "ChangedDocument",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    changed_location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "ChangedLocation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    changed_organisation_role: Optional[OrganisationRole] = field(
        default=None,
        metadata={
            "name": "ChangedOrganisationRole",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    changed_person_role: Optional["PersonRole"] = field(
        default=None,
        metadata={
            "name": "ChangedPersonRole",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    changed_service_category: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "name": "ChangedServiceCategory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    changed_usage_point: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "name": "ChangedUsagePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fault_cause_type: Optional[FaultCauseType] = field(
        default=None,
        metadata={
            "name": "FaultCauseType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    power_system_resource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
            "name": "PowerSystemResource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhenomenonClassification(IdentifiedObject):
    """
    A pre-defined phenomenon classification as defined by a particular
    authority.

    :ivar classification_condition: Condition contributing to the
        classification of this phenomenon.
    :ivar environmental_data_authority: Authority defining this
        environmental phenomenon.
    :ivar environmental_phenomenon:
    """
    classification_condition: List[ClassificationCondition] = field(
        default_factory=list,
        metadata={
            "name": "ClassificationCondition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_data_authority: Optional["EnvironmentalDataAuthority"] = field(
        default=None,
        metadata={
            "name": "EnvironmentalDataAuthority",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_phenomenon: List[EnvironmentalPhenomenon] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalPhenomenon",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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

    :ivar activity_records: All activity records created for this asset.
    :ivar analytic:
    :ivar analytic_score:
    :ivar asset_container: Container of this asset.
    :ivar asset_deployment: This asset's deployment.
    :ivar asset_function:
    :ivar asset_group:
    :ivar asset_info: Data applicable to this asset.
    :ivar breaker_operation: Breaker operation information for this
        breaker.
    :ivar configuration_events: All configuration events created for
        this asset.
    :ivar financial_info:
    :ivar location: Location of this asset.
    :ivar measurements:
    :ivar medium:
    :ivar organisation_roles: All roles an organisation plays for this
        asset.
    :ivar ownerships: All ownerships of this asset.
    :ivar power_system_resources: All power system resources used to
        electrically model this asset. For example, transformer asset is
        electrically modelled with a transformer and its windings and
        tap changer.
    :ivar procedure_data_set: Procedure data set that applies to this
        asset.
    :ivar procedures: All procedures applicable to this asset.
    :ivar product_asset_model: The model of this asset.
    :ivar scheduled_events:
    """
    activity_records: List[ActivityRecord] = field(
        default_factory=list,
        metadata={
            "name": "ActivityRecords",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    analytic: List[Analytic] = field(
        default_factory=list,
        metadata={
            "name": "Analytic",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    analytic_score: List[AnalyticScore] = field(
        default_factory=list,
        metadata={
            "name": "AnalyticScore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_container: Optional["AssetContainer"] = field(
        default=None,
        metadata={
            "name": "AssetContainer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_deployment: Optional[AssetDeployment] = field(
        default=None,
        metadata={
            "name": "AssetDeployment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_function: List[AssetFunction] = field(
        default_factory=list,
        metadata={
            "name": "AssetFunction",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_group: List[AssetGroup] = field(
        default_factory=list,
        metadata={
            "name": "AssetGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    asset_info: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "name": "AssetInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    breaker_operation: Optional[SwitchOperationSummary] = field(
        default=None,
        metadata={
            "name": "BreakerOperation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    configuration_events: List[ConfigurationEvent] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    financial_info: Optional[FinancialInfo] = field(
        default=None,
        metadata={
            "name": "FinancialInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    medium: List[Medium] = field(
        default_factory=list,
        metadata={
            "name": "Medium",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    organisation_roles: List[AssetOrganisationRole] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationRoles",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ownerships: List[Ownership] = field(
        default_factory=list,
        metadata={
            "name": "Ownerships",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_system_resources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "name": "PowerSystemResources",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    procedure_data_set: List[ProcedureDataSet] = field(
        default_factory=list,
        metadata={
            "name": "ProcedureDataSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    procedures: List[Procedure] = field(
        default_factory=list,
        metadata={
            "name": "Procedures",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    product_asset_model: Optional[ProductAssetModel] = field(
        default=None,
        metadata={
            "name": "ProductAssetModel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scheduled_events: List[ScheduledEvent] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalDataAuthority(OrganisationRole):
    """
    An entity defining classifications or categories of environmental
    information, like phenomena or alerts.

    :ivar alert_type_list: A specific version of a list of alerts
        published by this environmental data authority.
    :ivar phenomenon_classification: Phenomenon classification defined
        by this environmental data authority.
    """
    alert_type_list: List["AlertTypeList"] = field(
        default_factory=list,
        metadata={
            "name": "AlertTypeList",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phenomenon_classification: List[PhenomenonClassification] = field(
        default_factory=list,
        metadata={
            "name": "PhenomenonClassification",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AlertTypeList(IdentifiedObject):
    """A named list of alert types.

    Note:  the name of the list is reflected in the .name attribute (inherited from IdentifiedObject).

    :ivar version: The version of the named list of alert types.
    :ivar environmental_alert: An alert whose type is drawn from this
        alert type list.
    :ivar environmental_data_authority: The environmental data authority
        responsible for publishing this list of alert types.
    """
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_alert: List["EnvironmentalAlert"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalAlert",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_data_authority: Optional[EnvironmentalDataAuthority] = field(
        default=None,
        metadata={
            "name": "EnvironmentalDataAuthority",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetContainer(Asset):
    """
    Asset that is aggregation of other assets such as conductors, transformers,
    switchgear, land, fences, buildings, equipment, vehicles, etc.

    :ivar assets: All assets within this container asset.
    :ivar seals: All seals applied to this asset container.
    """
    assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    seals: List[Seal] = field(
        default_factory=list,
        metadata={
            "name": "Seals",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar catalog_asset_type:
    :ivar power_system_resources: All power system resources with this
        datasheet information.
    :ivar product_asset_model:
    """
    assets: List[Asset] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    catalog_asset_type: Optional[CatalogAssetType] = field(
        default=None,
        metadata={
            "name": "CatalogAssetType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_system_resources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "name": "PowerSystemResources",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    product_asset_model: Optional[ProductAssetModel] = field(
        default=None,
        metadata={
            "name": "ProductAssetModel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Bushing(Asset):
    """
    Bushing asset.

    :ivar fixed_contact: Fixed contact of interrupter to which this
        bushing is attached.
    :ivar moving_contact: Moving contact of interrupter to which this
        bushing is attached.
    :ivar terminal:
    """
    fixed_contact: Optional["InterrupterUnit"] = field(
        default=None,
        metadata={
            "name": "FixedContact",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    moving_contact: Optional["InterrupterUnit"] = field(
        default=None,
        metadata={
            "name": "MovingContact",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ComMedia(Asset):
    """
    Communication media such as fibre optic cable, power-line, telephone, etc.
    """


@dataclass
class ComModule(Asset):
    """An asset having communications capabilities that can be paired with a
    meter or other end device to provide the device with communication ability,
    through associated communication function.

    An end device that has communications capabilities through embedded
    hardware can use that function directly (without the communication
    module), or combine embedded communication function with additional
    communication functions provided through an external communication
    module (e.g. zigbee).

    :ivar amr_system: Automated meter reading (AMR) system communicating
        with this com module.
    :ivar supports_autonomous_dst: If true, autonomous daylight saving
        time (DST) function is supported.
    :ivar time_zone_offset: Time zone offset relative to GMT for the
        location of this com module.
    :ivar com_functions: All functions this communication module
        performs.
    """
    amr_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "amrSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_autonomous_dst: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsAutonomousDst",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_zone_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeZoneOffset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    com_functions: List["ComFunction"] = field(
        default_factory=list,
        metadata={
            "name": "ComFunctions",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Factsdevice(Asset):
    """
    FACTS device asset.
    """
    class Meta:
        name = "FACTSDevice"


@dataclass
class InterrupterUnit(Asset):
    """Breaker interrupter.

    Some interrupters have one fixed and one moving contact, some have 2
    fixed contacts, some 2 moving contacts. An interrupter will have
    relationships with 2 bushings and those relationships may be any
    combination of the FixedContact and MovingContact associations.

    :ivar bushing: Bushing(s) to which the fixed contact(s) of this
        interrupter is(are) attached. Some interrupters have one fixed
        and one moving contact, some have 2 fixed contacts, some 2
        moving contacts. An interrupter will have relationships with 2
        bushings and those relationships may be any combination of the
        FixedContact and MovingContact associations.
    :ivar operating_mechanism: Breaker mechanism controlling this
        interrupter.
    """
    bushing: List["Bushing"] = field(
        default_factory=list,
        metadata={
            "name": "Bushing",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operating_mechanism: Optional["OperatingMechanism"] = field(
        default=None,
        metadata={
            "name": "OperatingMechanism",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Joint(Asset):
    """Joint connects two or more cables.

    It includes the portion of cable under wipes, welds, or other seals.

    :ivar insulation: The type of insulation around the joint,
        classified according to the utility's asset management standards
        and practices.
    """
    insulation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OperatingMechanism(Asset):
    """
    Breaker mechanism.

    :ivar interrupter_unit: Interrupter controlled by this mechanism.
    """
    interrupter_unit: List["InterrupterUnit"] = field(
        default_factory=list,
        metadata={
            "name": "InterrupterUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Streetlight(Asset):
    """
    Streetlight asset.

    :ivar arm_length: Length of arm. Note that a new light may be placed
        on an existing arm.
    :ivar light_rating: Power rating of light.
    """
    arm_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "armLength",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    light_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "lightRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class StructureSupport(Asset):
    """
    Support for structure assets.

    :ivar anchor_rod_count: (if anchor) Number of rods used.
    :ivar anchor_rod_length: (if anchor) Length of rod used.
    :ivar direction: Direction of this support structure.
    :ivar length: Length of this support structure.
    :ivar size: Size of this support structure.
    :ivar secured_structure:
    """
    anchor_rod_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "anchorRodCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    anchor_rod_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "anchorRodLength",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    direction: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    size: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    secured_structure: Optional["Structure"] = field(
        default=None,
        metadata={
            "name": "SecuredStructure",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BushingInfo(AssetInfo):
    """
    Bushing datasheet information.

    :ivar c1_capacitance: Factory measured capacitance, measured between
        the power factor tap and the bushing conductor.
    :ivar c1_power_factor: Factory measured insulation power factor,
        measured between the power factor tap and the bushing conductor.
    :ivar c2_capacitance: Factory measured capacitance measured between
        the power factor tap and ground.
    :ivar c2_power_factor: Factory measured insulation power factor,
        measured between the power factor tap and ground.
    :ivar insulation_kind: Kind of insulation.
    :ivar rated_current: Rated current for bushing as installed.
    :ivar rated_impulse_withstand_voltage: Rated impulse withstand
        voltage, also known as BIL (Basic Impulse Level).
    :ivar rated_line_to_ground_voltage: Rated line-to-ground voltage.
        Also referred to as U&lt;sub&gt;y&lt;/sub&gt; on bushing
        nameplate.
    :ivar rated_voltage: Rated voltage. Can be referred to as
        U&lt;sub&gt;m&lt;/sub&gt;, system voltage or class on bushing
        nameplate.
    """
    c1_capacitance: Optional[float] = field(
        default=None,
        metadata={
            "name": "c1Capacitance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    c1_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "c1PowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    c2_capacitance: Optional[float] = field(
        default=None,
        metadata={
            "name": "c2Capacitance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    c2_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "c2PowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    insulation_kind: Optional[BushingInsulationKind] = field(
        default=None,
        metadata={
            "name": "insulationKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_impulse_withstand_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedImpulseWithstandVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_line_to_ground_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedLineToGroundVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Cabinet(AssetContainer):
    """
    Enclosure that offers protection to the equipment it contains and/or safety
    to people/animals outside it.
    """


@dataclass
class ComFunction(EndDeviceFunction):
    """
    Communication function of communication equipment or a device such as a
    meter.

    :ivar amr_address: Communication ID number (e.g. serial number, IP
        address, telephone number, etc.) of the AMR module which serves
        this meter.
    :ivar amr_router: Communication ID number (e.g. port number, serial
        number, data collector ID, etc.) of the parent device associated
        to this AMR module.
    :ivar direction: Kind of communication direction.
    :ivar technology: Kind of communication technology.
    :ivar com_module: Module performing this communication function.
    """
    amr_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "amrAddress",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    amr_router: Optional[str] = field(
        default=None,
        metadata={
            "name": "amrRouter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    direction: Optional[ComDirectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    technology: Optional[ComTechnologyKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    com_module: Optional[ComModule] = field(
        default=None,
        metadata={
            "name": "ComModule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class DuctBank(AssetContainer):
    """
    A duct contains individual wires in the layout as specified with associated
    wire spacing instances; number of them gives the number of conductors in
    this duct.

    :ivar circuit_count: Number of circuits in duct bank. Refer to
        associations between a duct (ConductorAsset) and an
        ACLineSegment to understand which circuits are in which ducts.
    :ivar wire_spacing_infos:
    """
    circuit_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "circuitCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_spacing_infos: List["WireSpacingInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WireSpacingInfos",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar service_location: Service location whose service delivery is
        measured by this end device.
    :ivar usage_point: Usage point to which this end device belongs.
    """
    amr_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "amrSystem",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    install_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "installCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_pan: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPan",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_smart_inverter: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSmartInverter",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_virtual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isVirtual",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_zone_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeZoneOffset",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    customer: Optional["Customer"] = field(
        default=None,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dispatchable_power_capability: List[DispatchablePowerCapability] = field(
        default_factory=list,
        metadata={
            "name": "DispatchablePowerCapability",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_controls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceControls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_events: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceEvents",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_functions: List[EndDeviceFunction] = field(
        default_factory=list,
        metadata={
            "name": "EndDeviceFunctions",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_groups: Optional[EndDeviceGroup] = field(
        default=None,
        metadata={
            "name": "EndDeviceGroups",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_device_info: Optional["EndDeviceInfo"] = field(
        default=None,
        metadata={
            "name": "EndDeviceInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    service_location: Optional["ServiceLocation"] = field(
        default=None,
        metadata={
            "name": "ServiceLocation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_point: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "name": "UsagePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "phaseCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    capability: Optional[EndDeviceCapability] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_devices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "name": "EndDevices",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalAlert(ActivityRecord):
    """
    An environmental alert issued by a provider or system.

    :ivar alert_type: The type of the issued alert which is drawn from
        the specified alert type list.
    :ivar cancelled_date_time: Time and date alert cancelled. Used only
        if alert is cancelled before it expires.
    :ivar headline: An abbreviated textual description of the alert
        issued. Note: the full text of the alert appears in the
        .description attribute (inherited from IdentifiedObject).
    :ivar alert_type_list: The list of alert types from which the type
        of this alert is drawn.
    :ivar environmental_data_provider: Environmental data provider for
        this alert.
    :ivar environmental_location_kind: Type of location to which this
        environmental alert applies.
    :ivar in_effect: The interval for which this weather alert is in
        effect.
    """
    alert_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cancelled_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "cancelledDateTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    headline: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    alert_type_list: Optional[AlertTypeList] = field(
        default=None,
        metadata={
            "name": "AlertTypeList",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    environmental_data_provider: Optional[EnvironmentalDataProvider] = field(
        default=None,
        metadata={
            "name": "EnvironmentalDataProvider",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    environmental_location_kind: List["EnvironmentalLocationType"] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalLocationKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    in_effect: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "inEffect",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Facility(AssetContainer):
    """
    A facility may contain buildings, storage facilities, switching facilities,
    power generation, manufacturing facilities, maintenance facilities, etc.

    :ivar kind: Kind of this facility.
    """
    kind: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    islanding_category: Optional[Ieee1547IslandingCategory] = field(
        default=None,
        metadata={
            "name": "islandingCategory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maximum_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimum_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_performance_category: Optional[Ieee1547NormalPerformanceCategory] = field(
        default=None,
        metadata={
            "name": "normalPerformanceCategory",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    over_excited_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "overExcitedPF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_pat_unity_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPatUnityPF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_pcharge: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPcharge",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_pover_excited: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPoverExcited",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_punder_excited: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPunderExcited",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_qabsorbed: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedQabsorbed",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_qinjected: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedQinjected",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_scharge: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedScharge",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "serialNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_dynamic_reactive_current: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsDynamicReactiveCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_iec61850: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsIEC61850",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_ieee1815: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsIEEE1815",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_ieee20305: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsIEEE20305",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_islanding: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsIslanding",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_sun_spec_mod_bus_ethernet: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsSunSpecModBusEthernet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_sun_spec_mod_bus_rs485: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsSunSpecModBusRS485",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_volt_watt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsVoltWatt",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supports_watt_var: Optional[bool] = field(
        default=None,
        metadata={
            "name": "supportsWattVar",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    susceptance_cease_to_energize: Optional[float] = field(
        default=None,
        metadata={
            "name": "susceptanceCeaseToEnergize",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    under_excited_pf: Optional[float] = field(
        default=None,
        metadata={
            "name": "underExcitedPF",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_electronics_connections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rotating_machines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "name": "RotatingMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class InterrupterUnitInfo(AssetInfo):
    """
    :ivar interrupting_medium: Interrupting medium.
    """
    interrupting_medium: Optional[InterruptingMediumKind] = field(
        default=None,
        metadata={
            "name": "interruptingMedium",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OperatingMechanismInfo(AssetInfo):
    """
    Breaker operating mechanism datasheet information.

    :ivar close_amps: Close current (nominal).
    :ivar close_voltage: Close voltage in volts DC.
    :ivar mechanism_kind: Kind of breaker operating mechanism.
    :ivar motor_run_current: Rated motor run current in amps.
    :ivar motor_start_current: Rated motor start current in amps.
    :ivar motor_voltage: Nominal motor voltage in volts DC.
    :ivar trip_amps: Trip current (nominal).
    :ivar trip_voltage: Trip voltage in volts DC.
    """
    close_amps: Optional[float] = field(
        default=None,
        metadata={
            "name": "closeAmps",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    close_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "closeVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mechanism_kind: Optional[OperatingMechanismKind] = field(
        default=None,
        metadata={
            "name": "mechanismKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    motor_run_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "motorRunCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    motor_start_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "motorStartCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    motor_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "motorVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    trip_amps: Optional[float] = field(
        default=None,
        metadata={
            "name": "tripAmps",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    trip_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "tripVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar configuration_event:
    :ivar controls: The controller outputs used to actually govern a
        regulating device, e.g. the magnetization of a synchronous
        machine or capacitor bank breaker actuator.
    :ivar location: Location of this power system resource.
    :ivar measurements: The measurements associated with this power
        system resource.
    :ivar operating_share: The operating shares of this power system
        resource.
    :ivar psrtype: Custom classification for this power system resource.
    :ivar reporting_group: Reporting groups to which this power system
        resource belongs.
    """
    asset_datasheet: Optional[AssetInfo] = field(
        default=None,
        metadata={
            "name": "AssetDatasheet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    assets: List[Asset] = field(
        default_factory=list,
        metadata={
            "name": "Assets",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    configuration_event: List[ConfigurationEvent] = field(
        default_factory=list,
        metadata={
            "name": "ConfigurationEvent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    controls: List[Control] = field(
        default_factory=list,
        metadata={
            "name": "Controls",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operating_share: List[OperatingShare] = field(
        default_factory=list,
        metadata={
            "name": "OperatingShare",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    psrtype: Optional[Psrtype] = field(
        default=None,
        metadata={
            "name": "PSRType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reporting_group: List["ReportingGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ReportingGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Structure(AssetContainer):
    """Construction holding assets such as conductors, transformers,
    switchgear, etc.

    Where applicable, number of conductors can be derived from the
    number of associated wire spacing instances.

    :ivar fumigant_applied_date: Date fumigant was last applied.
    :ivar fumigant_name: Name of fumigant.
    :ivar height: Visible height of structure above ground level for
        overhead construction (e.g., Pole or Tower) or below ground
        level for an underground vault, manhole, etc. Refer to
        associated DimensionPropertiesInfo for other types of
        dimensions.
    :ivar rated_voltage: Maximum rated voltage of the equipment that can
        be mounted on/contained within the structure.
    :ivar remove_weed: True if weeds are to be removed around asset.
    :ivar weed_removed_date: Date weed were last removed.
    :ivar structure_supports:
    :ivar wire_spacing_infos:
    """
    fumigant_applied_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "fumigantAppliedDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fumigant_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fumigantName",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    remove_weed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "removeWeed",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    weed_removed_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "weedRemovedDate",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    structure_supports: List[StructureSupport] = field(
        default_factory=list,
        metadata={
            "name": "StructureSupports",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_spacing_infos: List["WireSpacingInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WireSpacingInfos",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_single_phase: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSinglePhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_unganged: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isUnganged",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    low_pressure_alarm: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowPressureAlarm",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    low_pressure_lock_out: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowPressureLockOut",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    oil_volume_per_tank: Optional[float] = field(
        default=None,
        metadata={
            "name": "oilVolumePerTank",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_impulse_withstand_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedImpulseWithstandVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_interrupting_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedInterruptingTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ct_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "ctRatio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pt_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "ptRatio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar transformer_star_impedance: Transformer star impedance
        calculated from this transformer end datasheet.
    :ivar transformer_tank_info: Transformer tank data that this end
        description is part of.
    """
    connection_kind: Optional[WindingConnection] = field(
        default=None,
        metadata={
            "name": "connectionKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    emergency_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "emergencyS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    end_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "endNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    insulation_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "insulationU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_angle_clock: Optional[int] = field(
        default=None,
        metadata={
            "name": "phaseAngleClock",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    short_term_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "shortTermS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    core_admittance: Optional["TransformerCoreAdmittance"] = field(
        default=None,
        metadata={
            "name": "CoreAdmittance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energised_end_no_load_tests: List[NoLoadTest] = field(
        default_factory=list,
        metadata={
            "name": "EnergisedEndNoLoadTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energised_end_open_circuit_tests: List[OpenCircuitTest] = field(
        default_factory=list,
        metadata={
            "name": "EnergisedEndOpenCircuitTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energised_end_short_circuit_tests: List[ShortCircuitTest] = field(
        default_factory=list,
        metadata={
            "name": "EnergisedEndShortCircuitTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    from_mesh_impedances: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "name": "FromMeshImpedances",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    grounded_end_short_circuit_tests: List[ShortCircuitTest] = field(
        default_factory=list,
        metadata={
            "name": "GroundedEndShortCircuitTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    open_end_open_circuit_tests: List[OpenCircuitTest] = field(
        default_factory=list,
        metadata={
            "name": "OpenEndOpenCircuitTests",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    to_mesh_impedances: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "name": "ToMeshImpedances",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_star_impedance: Optional[TransformerStarImpedance] = field(
        default=None,
        metadata={
            "name": "TransformerStarImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_tank_info: Optional["TransformerTankInfo"] = field(
        default=None,
        metadata={
            "name": "TransformerTankInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    """
    power_transformer_info: Optional["PowerTransformerInfo"] = field(
        default=None,
        metadata={
            "name": "PowerTransformerInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    transformer_end_infos: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "name": "TransformerEndInfos",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class CogenerationPlant(PowerSystemResource):
    """A set of thermal generating units for the production of electrical
    energy and process steam (usually from the output of the steam turbines).

    The steam sendout is typically used for industrial purposes or for
    municipal heating and cooling.

    :ivar cogen_hpsendout_rating: The high pressure steam sendout.
    :ivar cogen_hpsteam_rating: The high pressure steam rating.
    :ivar cogen_lpsendout_rating: The low pressure steam sendout.
    :ivar cogen_lpsteam_rating: The low pressure steam rating.
    :ivar rated_p: The rated output active power of the cogeneration
        plant.
    :ivar steam_sendout_schedule: A cogeneration plant has a steam
        sendout schedule.
    :ivar thermal_generating_units: A thermal generating unit may be a
        member of a cogeneration plant.
    """
    cogen_hpsendout_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "cogenHPSendoutRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cogen_hpsteam_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "cogenHPSteamRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cogen_lpsendout_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "cogenLPSendoutRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cogen_lpsteam_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "cogenLPSteamRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    steam_sendout_schedule: Optional[SteamSendoutSchedule] = field(
        default=None,
        metadata={
            "name": "SteamSendoutSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    thermal_generating_units: List["ThermalGeneratingUnit"] = field(
        default_factory=list,
        metadata={
            "name": "ThermalGeneratingUnits",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CombinedCyclePlant(PowerSystemResource):
    """
    A set of combustion turbines and steam turbines where the exhaust heat from
    the combustion turbines is recovered to make steam for the steam turbines,
    resulting in greater overall plant efficiency.

    :ivar comb_cycle_plant_rating: The combined cycle plant's active
        power output rating.
    :ivar thermal_generating_units: A thermal generating unit may be a
        member of a combined cycle plant.
    """
    comb_cycle_plant_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "combCyclePlantRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    thermal_generating_units: List["ThermalGeneratingUnit"] = field(
        default_factory=list,
        metadata={
            "name": "ThermalGeneratingUnits",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    connectivity_nodes: List[ConnectivityNode] = field(
        default_factory=list,
        metadata={
            "name": "ConnectivityNodes",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    topological_node: List[TopologicalNode] = field(
        default_factory=list,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energy_consumer: Optional["EnergyConsumer"] = field(
        default=None,
        metadata={
            "name": "EnergyConsumer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energy_source: Optional["EnergySource"] = field(
        default=None,
        metadata={
            "name": "EnergySource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or
    mechanical.

    :ivar aggregate: The single instance of equipment represents
        multiple pieces of equipment that have been modeled together as
        an aggregate.  Examples would be power transformers or
        synchronous machines operating in parallel modeled as a single
        aggregate power transformer or aggregate synchronous machine.
        This is not to be used to indicate equipment that is part of a
        group of interdependent equipment produced by a network
        production program.
    :ivar in_service: If true, the equipment is in service.
    :ivar network_analysis_enabled: The equipment is enabled to
        participate in network analysis.  If unspecified, the value is
        assumed to be true.
    :ivar normally_in_service: If true, the equipment is normally in
        service.
    :ivar additional_equipment_container: Additional equipment container
        beyond the primary equipment container.  The equipment is
        contained in another equipment container, but also grouped with
        this equipment container.
    :ivar equipment_container: Container of this equipment.
    :ivar faults: All faults on this equipment.
    :ivar operational_limit_set: The operational limit sets associated
        with this equipment.
    :ivar usage_points: All usage points connected to the electrical
        grid through this equipment.
    """
    aggregate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    in_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inService",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    network_analysis_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "networkAnalysisEnabled",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normally_in_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "normallyInService",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    additional_equipment_container: List["EquipmentContainer"] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalEquipmentContainer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    equipment_container: Optional["EquipmentContainer"] = field(
        default=None,
        metadata={
            "name": "EquipmentContainer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    faults: List["Fault"] = field(
        default_factory=list,
        metadata={
            "name": "Faults",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operational_limit_set: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimitSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage_points: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "name": "UsagePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Meter(EndDevice):
    """Physical asset that performs the metering role of the usage point.

    Used for measuring consumption and detection of events.

    :ivar form_number: Meter form designation per ANSI C12.10 or other
        applicable standard. An alphanumeric designation denoting the
        circuit arrangement for which the meter is applicable and its
        specific terminal arrangement.
    :ivar meter_multipliers: All multipliers applied at this meter.
    :ivar meter_readings: All meter readings provided by this meter.
    :ivar meter_replacement_work_tasks: All work tasks on replacement of
        this old meter.
    :ivar meter_service_work_task: All non-replacement work tasks on
        this meter.
    """
    form_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "formNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter_multipliers: List[MeterMultiplier] = field(
        default_factory=list,
        metadata={
            "name": "MeterMultipliers",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter_readings: List["MeterReading"] = field(
        default_factory=list,
        metadata={
            "name": "MeterReadings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter_replacement_work_tasks: List[MeterWorkTask] = field(
        default_factory=list,
        metadata={
            "name": "MeterReplacementWorkTasks",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meter_service_work_task: List[MeterWorkTask] = field(
        default_factory=list,
        metadata={
            "name": "MeterServiceWorkTask",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cut_level2: Optional[float] = field(
        default=None,
        metadata={
            "name": "cutLevel2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energy_consumers: List["EnergyConsumer"] = field(
        default_factory=list,
        metadata={
            "name": "EnergyConsumers",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_electronics_connection: Optional["PowerElectronicsConnection"] = field(
        default=None,
        metadata={
            "name": "PowerElectronicsConnection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar regulating_cond_eq: The equipment that participates in this
        regulating control scheme.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mode: Optional[RegulatingControlModeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    monitored_phase: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "name": "monitoredPhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    target_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "targetDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    target_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "targetValue",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    regulating_cond_eq: List["RegulatingCondEq"] = field(
        default_factory=list,
        metadata={
            "name": "RegulatingCondEq",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    regulation_schedule: List[RegulationSchedule] = field(
        default_factory=list,
        metadata={
            "name": "RegulationSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ReportingGroup(IdentifiedObject):
    """
    A reporting group is used for various ad-hoc groupings used for reporting.

    :ivar bus_name_marker: The bus name markers that belong to this
        reporting group.
    :ivar power_system_resource: Power system resources which belong to
        this reporting group.
    :ivar reporting_super_group:
    :ivar topological_node: The topological nodes that belong to the
        reporting group.
    """
    bus_name_marker: List["BusNameMarker"] = field(
        default_factory=list,
        metadata={
            "name": "BusNameMarker",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_system_resource: List[PowerSystemResource] = field(
        default_factory=list,
        metadata={
            "name": "PowerSystemResource",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reporting_super_group: Optional[ReportingSuperGroup] = field(
        default=None,
        metadata={
            "name": "ReportingSuperGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    topological_node: List[TopologicalNode] = field(
        default_factory=list,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Reservoir(PowerSystemResource):
    """A water storage facility within a hydro system, including: ponds, lakes,
    lagoons, and rivers.

    The storage is usually behind some type of dam.

    :ivar active_storage_capacity: Storage volume between the full
        supply level and the normal minimum operating level.
    :ivar energy_storage_rating: The reservoir's energy storage rating
        in energy for given head conditions.
    :ivar full_supply_level: Full supply level, above which water will
        spill. This can be the spillway crest level or the top of closed
        gates.
    :ivar gross_capacity: Total capacity of reservoir.
    :ivar normal_min_operate_level: Normal minimum operating level below
        which the penstocks will draw air.
    :ivar river_outlet_works: River outlet works for riparian right
        releases or other purposes.
    :ivar spill_travel_delay: The spillway water travel delay to the
        next downstream reservoir.
    :ivar spillway_capacity: The flow capacity of the spillway in cubic
        meters per second.
    :ivar spillway_crest_length: The length of the spillway crest.
    :ivar spillway_crest_level: Spillway crest level above which water
        will spill.
    :ivar spill_way_gate_type: Type of spillway gate, including
        parameters.
    :ivar hydro_power_plants: Generators discharge water to or pumps are
        supplied water from a downstream reservoir.
    :ivar inflow_forecasts: A reservoir may have a "natural" inflow
        forecast.
    :ivar level_vs_volume_curves: A reservoir may have a level versus
        volume relationship.
    :ivar spills_from_reservoir: A reservoir may spill into a downstream
        reservoir.
    :ivar target_level_schedule: A reservoir may have a water level
        target schedule.
    :ivar upstream_from_hydro_power_plants: Generators are supplied
        water from or pumps discharge water to an upstream reservoir.
    """
    active_storage_capacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "activeStorageCapacity",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energy_storage_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "energyStorageRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    full_supply_level: Optional[float] = field(
        default=None,
        metadata={
            "name": "fullSupplyLevel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gross_capacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "grossCapacity",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_min_operate_level: Optional[float] = field(
        default=None,
        metadata={
            "name": "normalMinOperateLevel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    river_outlet_works: Optional[str] = field(
        default=None,
        metadata={
            "name": "riverOutletWorks",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spill_travel_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "spillTravelDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spillway_capacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "spillwayCapacity",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spillway_crest_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "spillwayCrestLength",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spillway_crest_level: Optional[float] = field(
        default=None,
        metadata={
            "name": "spillwayCrestLevel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spill_way_gate_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "spillWayGateType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydro_power_plants: List["HydroPowerPlant"] = field(
        default_factory=list,
        metadata={
            "name": "HydroPowerPlants",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    inflow_forecasts: List[InflowForecast] = field(
        default_factory=list,
        metadata={
            "name": "InflowForecasts",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    level_vs_volume_curves: List[LevelVsVolumeCurve] = field(
        default_factory=list,
        metadata={
            "name": "LevelVsVolumeCurves",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spills_from_reservoir: Optional["Reservoir"] = field(
        default=None,
        metadata={
            "name": "SpillsFromReservoir",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    target_level_schedule: Optional[TargetLevelSchedule] = field(
        default=None,
        metadata={
            "name": "TargetLevelSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    upstream_from_hydro_power_plants: List["HydroPowerPlant"] = field(
        default_factory=list,
        metadata={
            "name": "UpstreamFromHydroPowerPlants",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_sections: Optional[int] = field(
        default=None,
        metadata={
            "name": "normalSections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sections: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shunt_compensator: Optional["ShuntCompensator"] = field(
        default=None,
        metadata={
            "name": "ShuntCompensator",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SwitchPhase(PowerSystemResource):
    """
    Single phase of a multi-phase switch when its attributes might be different
    per phase.

    :ivar closed: The attribute tells if the switch is considered closed
        when used as input to topology processing.
    :ivar normal_open: Used in cases when no Measurement for the status
        value is present. If the SwitchPhase has a status measurement
        the Discrete.normalValue is expected to match with this value.
    :ivar phase_side1: Phase of this SwitchPhase on the side with
        terminal sequence number equal 1. Should be a phase contained in
        that terminal&amp;rsquo;s phases attribute.
    :ivar phase_side2: Phase of this SwitchPhase on the side with
        terminal sequence number equal 2.  Should be a phase contained
        in that terminal&amp;rsquo;s Terminal.phases attribute.
    :ivar rated_current: Rated current through this phase, if different
        from the others.
    :ivar switch: The switch of the switch phase.
    """
    closed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_open: Optional[bool] = field(
        default=None,
        metadata={
            "name": "normalOpen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_side1: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "name": "phaseSide1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_side2: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "name": "phaseSide2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    switch: Optional["Switch"] = field(
        default=None,
        metadata={
            "name": "Switch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TapChanger(PowerSystemResource):
    """
    Mechanism for changing transformer winding tap positions.

    :ivar control_enabled: Specifies the regulation status of the
        equipment.  True is regulating, false is not regulating.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    high_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "highStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    initial_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "initialDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    low_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "lowStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ltc_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ltcFlag",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutral_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "neutralStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutral_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "neutralU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "normalStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    step: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    subsequent_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "subsequentDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_tap_step: Optional[SvTapStep] = field(
        default=None,
        metadata={
            "name": "SvTapStep",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tap_changer_control: Optional["TapChangerControl"] = field(
        default=None,
        metadata={
            "name": "TapChangerControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tap_schedules: List[TapSchedule] = field(
        default_factory=list,
        metadata={
            "name": "TapSchedules",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    regulation_schedule: Optional["RegulationSchedule"] = field(
        default=None,
        metadata={
            "name": "RegulationSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar usage: Usage of the associated wires.
    :ivar acline_segments:
    :ivar duct_bank:
    :ivar structures:
    :ivar wire_assembly_info:
    :ivar wire_positions: All positions of single wires (phase or
        neutral) making the conductor.
    """
    is_cable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isCable",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_wire_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "phaseWireCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_wire_spacing: Optional[float] = field(
        default=None,
        metadata={
            "name": "phaseWireSpacing",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usage: Optional[WireUsageKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    acline_segments: List["AclineSegment"] = field(
        default_factory=list,
        metadata={
            "name": "ACLineSegments",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    duct_bank: Optional[DuctBank] = field(
        default=None,
        metadata={
            "name": "DuctBank",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    structures: List[Structure] = field(
        default_factory=list,
        metadata={
            "name": "Structures",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_assembly_info: List["WireAssemblyInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WireAssemblyInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_positions: List[WirePosition] = field(
        default_factory=list,
        metadata={
            "name": "WirePositions",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class BusNameMarker(IdentifiedObject):
    """Used to apply user standard names to topology buses.

    Typically used for "bus/branch" case generation. Associated with one
    or more terminals that are normally connected with the bus name.
    The associated terminals are normally connected by non-retained
    switches. For a ring bus station configuration, all busbar terminals
    in the ring are typically associated.   For a breaker and a half
    scheme, both busbars would normally be associated.  For a ring bus,
    all busbars would normally be associated.  For a "straight" busbar
    configuration, normally only the main terminal at the busbar would
    be associated.

    :ivar priority: Priority of bus name marker for use as topology bus
        name.  Use 0 for don t care.  Use 1 for highest priority.  Use 2
        as priority is less than 1 and so on.
    :ivar reporting_group: The reporting group to which this bus name
        marker belongs.
    :ivar terminal: The terminals associated with this bus name marker.
    :ivar topological_node: A user defined topological node that was
        originally defined in a planning model not yet having topology
        described by ConnectivityNodes. Once ConnectivityNodes has been
        created they may linked to user defined ToplogicalNdes using
        BusNameMarkers.
    """
    priority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reporting_group: Optional[ReportingGroup] = field(
        default=None,
        metadata={
            "name": "ReportingGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminal: List["Acdcterminal"] = field(
        default_factory=list,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    topological_node: Optional[TopologicalNode] = field(
        default=None,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CompositeSwitch(Equipment):
    """A model of a set of individual Switches normally enclosed within the
    same cabinet and possibly with interlocks that restrict the combination of
    switch positions.

    These are typically found in medium voltage distribution networks. A
    CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-
    mounted switchgear, with primitive internal devices such as an
    internal bus-bar plus 3 or 4 internal switches each of which may
    individually be open or closed. A CompositeSwitch and a set of
    contained Switches can also be used to represent a multi-position
    switch e.g. a switch that can connect a circuit to Ground, Open or
    Busbar.

    :ivar composite_switch_type: An alphanumeric code that can be used
        as a reference to extra information such as the description of
        the interlocking scheme if any.
    :ivar switches: Switches contained in this Composite switch.
    """
    composite_switch_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "compositeSwitchType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    switches: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switches",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_status: List[SvStatus] = field(
        default_factory=list,
        metadata={
            "name": "SvStatus",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    terminals: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "name": "Terminals",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    equipments: List["Equipment"] = field(
        default_factory=list,
        metadata={
            "name": "Equipments",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class HydroPowerPlant(PowerSystemResource):
    """A hydro power station which can generate or pump.

    When generating, the generator turbines receive water from an upper
    reservoir. When pumping, the pumps receive their water from a lower
    reservoir.

    :ivar discharge_travel_delay: Water travel delay from tailbay to
        next downstream hydro power station.
    :ivar gen_rated_p: The hydro plant's generating rating active power
        for rated head conditions.
    :ivar hydro_plant_storage_type: The type of hydro power plant water
        storage.
    :ivar penstock_type: Type and configuration of hydro plant
        penstock(s).
    :ivar plant_discharge_capacity: Total plant discharge capacity.
    :ivar plant_rated_head: The plant's rated gross head.
    :ivar pump_rated_p: The hydro plant's pumping rating active power
        for rated head conditions.
    :ivar surge_tank_code: A code describing the type (or absence) of
        surge tank that is associated with the hydro power plant.
    :ivar surge_tank_crest_level: The level at which the surge tank
        spills.
    :ivar gen_source_pump_discharge_reservoir: Generators are supplied
        water from or pumps discharge water to an upstream reservoir.
    :ivar hydro_generating_units: The hydro generating unit belongs to a
        hydro power plant.
    :ivar hydro_pumps: The hydro pump may be a member of a pumped
        storage plant or a pump for distributing water.
    :ivar reservoir: Generators discharge water to or pumps are supplied
        water from a downstream reservoir.
    """
    discharge_travel_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "dischargeTravelDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gen_rated_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "genRatedP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydro_plant_storage_type: Optional[HydroPlantStorageKind] = field(
        default=None,
        metadata={
            "name": "hydroPlantStorageType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    penstock_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "penstockType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    plant_discharge_capacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "plantDischargeCapacity",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    plant_rated_head: Optional[float] = field(
        default=None,
        metadata={
            "name": "plantRatedHead",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pump_rated_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "pumpRatedP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    surge_tank_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "surgeTankCode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    surge_tank_crest_level: Optional[float] = field(
        default=None,
        metadata={
            "name": "surgeTankCrestLevel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gen_source_pump_discharge_reservoir: Optional[Reservoir] = field(
        default=None,
        metadata={
            "name": "GenSourcePumpDischargeReservoir",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hydro_generating_units: List["HydroGeneratingUnit"] = field(
        default_factory=list,
        metadata={
            "name": "HydroGeneratingUnits",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydro_pumps: List["HydroPump"] = field(
        default_factory=list,
        metadata={
            "name": "HydroPumps",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reservoir: Optional[Reservoir] = field(
        default=None,
        metadata={
            "name": "Reservoir",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "gPerSection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class NonlinearShuntCompensatorPhase(ShuntCompensatorPhase):
    """
    A per phase non linear shunt compensator has bank or section admittance
    values that differs.
    """
    nonlinear_shunt_compensator_phase_points: List[NonlinearShuntCompensatorPhasePoint] = field(
        default_factory=list,
        metadata={
            "name": "NonlinearShuntCompensatorPhasePoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "minP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_electronics_connection: Optional["PowerElectronicsConnection"] = field(
        default=None,
        metadata={
            "name": "PowerElectronicsConnection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar ratio_tap_changer_table: The tap ratio table for this ratio
        tap changer.
    :ivar transformer_end: Transformer end to which this ratio tap
        changer belongs.
    """
    step_voltage_increment: Optional[float] = field(
        default=None,
        metadata={
            "name": "stepVoltageIncrement",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratio_tap_changer_table: Optional[RatioTapChangerTable] = field(
        default=None,
        metadata={
            "name": "RatioTapChangerTable",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_end: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
            "name": "TransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TapChangerControl(RegulatingControl):
    """
    Describes behavior specific to tap changers, e.g. how the voltage at the
    end of a line varies with the load level and compensation of the voltage
    drop by tap adjustment.

    :ivar limit_voltage: Maximum allowed regulated voltage on the PT
        secondary, regardless of line drop compensation. Sometimes
        referred to as first-house protection.
    :ivar line_drop_compensation: If true, the line drop compensation is
        to be applied.
    :ivar line_drop_r: Line drop compensator resistance setting for
        normal (forward) power flow.
    :ivar line_drop_x: Line drop compensator reactance setting for
        normal (forward) power flow.
    :ivar reverse_line_drop_r: Line drop compensator resistance setting
        for reverse power flow.
    :ivar reverse_line_drop_x: Line drop compensator reactance setting
        for reverse power flow.
    :ivar tap_changer: The tap changers that participates in this
        regulating tap control scheme.
    """
    limit_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "limitVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    line_drop_compensation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "lineDropCompensation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    line_drop_r: Optional[float] = field(
        default=None,
        metadata={
            "name": "lineDropR",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    line_drop_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "lineDropX",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reverse_line_drop_r: Optional[float] = field(
        default=None,
        metadata={
            "name": "reverseLineDropR",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reverse_line_drop_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "reverseLineDropX",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tap_changer: List["TapChanger"] = field(
        default_factory=list,
        metadata={
            "name": "TapChanger",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    """
    power_transformer: Optional["PowerTransformer"] = field(
        default=None,
        metadata={
            "name": "PowerTransformer",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_tank_ends: List[TransformerTankEnd] = field(
        default_factory=list,
        metadata={
            "name": "TransformerTankEnds",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_phase_info: List["WirePhaseInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WirePhaseInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_spacing_info: Optional[WireSpacingInfo] = field(
        default=None,
        metadata={
            "name": "WireSpacingInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar bus_name_marker: The bus name marker used to name the bus
        (topological node).
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    bus_name_marker: Optional[BusNameMarker] = field(
        default=None,
        metadata={
            "name": "BusNameMarker",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operational_limit_set: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "name": "OperationalLimitSet",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BatteryUnit(PowerElectronicsUnit):
    """
    An electrochemical energy storage device.

    :ivar battery_state: indicates whether the battery is charging,
        discharging or idle
    :ivar rated_e: full energy storage capacity of the battery
    :ivar stored_e: amount of energy currently stored; no more than
        ratedE
    """
    battery_state: Optional[BatteryState] = field(
        default=None,
        metadata={
            "name": "batteryState",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_e: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedE",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    stored_e: Optional[float] = field(
        default=None,
        metadata={
            "name": "storedE",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Bay(EquipmentContainer):
    """A collection of power system resources (within a given substation)
    including conducting equipment, protection relays, measurements, and
    telemetry.

    A bay typically represents a physical grouping related to
    modularization of equipment.

    :ivar bay_energy_meas_flag: Indicates the presence/absence of energy
        measurements.
    :ivar bay_power_meas_flag: Indicates the presence/absence of
        active/reactive power measurements.
    :ivar breaker_configuration: Breaker configuration.
    :ivar bus_bar_configuration: Bus bar configuration.
    :ivar substation: Substation containing the bay.
    :ivar voltage_level: The voltage level containing this bay.
    """
    bay_energy_meas_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "bayEnergyMeasFlag",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    bay_power_meas_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "bayPowerMeasFlag",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    breaker_configuration: Optional[BreakerConfiguration] = field(
        default=None,
        metadata={
            "name": "breakerConfiguration",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    bus_bar_configuration: Optional[BusbarConfiguration] = field(
        default=None,
        metadata={
            "name": "busBarConfiguration",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    substation: Optional["Substation"] = field(
        default=None,
        metadata={
            "name": "Substation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltage_level: Optional["VoltageLevel"] = field(
        default=None,
        metadata={
            "name": "VoltageLevel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Clamp(ConductingEquipment):
    """A Clamp is a galvanic connection at a line segment where other equipment
    is connected.

    A Clamp does not cut the line segment. A Clamp is
    ConductingEquipment and has one Terminal with an associated
    ConnectivityNode. Any other ConductingEquipment can be connected to
    the Clamp ConnectivityNode.

    :ivar length_from_terminal1: The length to the place where the clamp
        is located starting from side one of the line segment, i.e. the
        line segment terminal with sequence number equal to 1.
    :ivar acline_segment: The line segment to which the clamp is
        connected.
    """
    length_from_terminal1: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthFromTerminal1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    acline_segment: Optional["AclineSegment"] = field(
        default=None,
        metadata={
            "name": "ACLineSegment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
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
class EarthFaultCompensator(ConductingEquipment):
    """A conducting equipment used to represent a connection to ground which is
    typically used to compensate earth faults..

    An earth fault compensator device modeled with a single terminal
    implies a second terminal solidly connected to ground.  If two
    terminals are modeled, the ground is not assumed and normal
    connection rules apply.

    :ivar r: Nominal resistance of device.
    """
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnergyConnection(ConductingEquipment):
    pass


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_energized_substation: List["Substation"] = field(
        default_factory=list,
        metadata={
            "name": "NormalEnergizedSubstation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_energizing_substation: Optional["Substation"] = field(
        default=None,
        metadata={
            "name": "NormalEnergizingSubstation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_head_terminal: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "name": "NormalHeadTerminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class Ground(ConductingEquipment):
    """A point where the system is grounded used for connecting conducting
    equipment to ground.

    The power system model can have any number of grounds.
    """


@dataclass
class HydroPump(Equipment):
    """
    A synchronous motor-driven pump, typically associated with a pumped storage
    plant.

    :ivar pump_disch_at_max_head: The pumping discharge under maximum
        head conditions, usually at full gate.
    :ivar pump_disch_at_min_head: The pumping discharge under minimum
        head conditions, usually at full gate.
    :ivar pump_power_at_max_head: The pumping power under maximum head
        conditions, usually at full gate.
    :ivar pump_power_at_min_head: The pumping power under minimum head
        conditions, usually at full gate.
    :ivar hydro_power_plant: The hydro pump may be a member of a pumped
        storage plant or a pump for distributing water.
    :ivar hydro_pump_op_schedule: The hydro pump has a pumping schedule
        over time, indicating when pumping is to occur.
    :ivar rotating_machine: The synchronous machine drives the turbine
        which moves the water from a low elevation to a higher
        elevation. The direction of machine rotation for pumping may or
        may not be the same as for generating.
    """
    pump_disch_at_max_head: Optional[float] = field(
        default=None,
        metadata={
            "name": "pumpDischAtMaxHead",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pump_disch_at_min_head: Optional[float] = field(
        default=None,
        metadata={
            "name": "pumpDischAtMinHead",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pump_power_at_max_head: Optional[float] = field(
        default=None,
        metadata={
            "name": "pumpPowerAtMaxHead",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pump_power_at_min_head: Optional[float] = field(
        default=None,
        metadata={
            "name": "pumpPowerAtMinHead",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydro_power_plant: Optional[HydroPowerPlant] = field(
        default=None,
        metadata={
            "name": "HydroPowerPlant",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydro_pump_op_schedule: Optional[HydroPumpOpSchedule] = field(
        default=None,
        metadata={
            "name": "HydroPumpOpSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rotating_machine: Optional["RotatingMachine"] = field(
        default=None,
        metadata={
            "name": "RotatingMachine",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Line(EquipmentContainer):
    """
    Contains equipment beyond a substation belonging to a power transmission
    line.

    :ivar region: The sub-geographical region of the line.
    """
    region: Optional["SubGeographicalRegion"] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhaseTapChangerLinear(PhaseTapChanger):
    """Describes a tap changer with a linear relation between the tap step and
    the phase angle difference across the transformer.

    This is a mathematical model that is an approximation of a real
    phase tap changer. The phase angle is computed as
    stepPhaseShitfIncrement times the tap position. The secondary side
    voltage magnitude is the same as at the primary side.

    :ivar step_phase_shift_increment: Phase shift per step position. A
        positive value indicates a positive phase shift from the winding
        where the tap is located to the other winding (for a two-winding
        transformer). The actual phase shift increment might be more
        accurately computed from the symmetrical or asymmetrical models
        or a tap step table lookup if those are available.
    :ivar x_max: The reactance depend on the tap position according to a
        "u" shaped curve. The maximum reactance (xMax) appear at the low
        and high tap positions.
    :ivar x_min: The reactance depend on the tap position according to a
        "u" shaped curve. The minimum reactance (xMin) appear at the mid
        tap position.
    """
    step_phase_shift_increment: Optional[float] = field(
        default=None,
        metadata={
            "name": "stepPhaseShiftIncrement",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "xMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "xMin",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhaseTapChangerNonLinear(PhaseTapChanger):
    """The non-linear phase tap changer describes the non-linear behavior of a
    phase tap changer.

    This is a base class for the symmetrical and asymmetrical phase tap
    changer models. The details of these models can be found in the IEC
    61970-301 document.

    :ivar voltage_step_increment: The voltage step increment on the out
        of phase winding specified in percent of neutral voltage of the
        tap changer. When the increment is negative, the voltage
        decreases when the tap step increases.
    :ivar x_max: The reactance depend on the tap position according to a
        "u" shaped curve. The maximum reactance (xMax) appear at the low
        and high tap positions.
    :ivar x_min: The reactance depend on the tap position according to a
        "u" shaped curve. The minimum reactance (xMin) appear at the mid
        tap position.
    """
    voltage_step_increment: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltageStepIncrement",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "xMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "xMin",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhaseTapChangerTabular(PhaseTapChanger):
    """
    :ivar phase_tap_changer_table: The phase tap changer table for this
        phase tap changer.
    """
    phase_tap_changer_table: Optional["PhaseTapChangerTable"] = field(
        default=None,
        metadata={
            "name": "PhaseTapChangerTable",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhotoVoltaicUnit(PowerElectronicsUnit):
    """
    A photovoltaic device or an aggregation of such devices.
    """


@dataclass
class Plant(EquipmentContainer):
    """
    A Plant is a collection of equipment for purposes of generation.
    """


@dataclass
class PowerElectronicsWindUnit(PowerElectronicsUnit):
    """
    A wind generating unit that connects to the AC network with power
    electronics rather than rotating machines or an aggregation of such units.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_transformer_end: List[PowerTransformerEnd] = field(
        default_factory=list,
        metadata={
            "name": "PowerTransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_tanks: List[TransformerTank] = field(
        default_factory=list,
        metadata={
            "name": "TransformerTanks",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class SeriesCompensator(ConductingEquipment):
    """A Series Compensator is a series capacitor or reactor or an AC
    transmission line without charging susceptance.

    It is a two terminal device.

    :ivar r: Positive sequence resistance.
    :ivar r0: Zero sequence resistance.
    :ivar varistor_present: Describe if a metal oxide varistor (mov) for
        over voltage protection is configured at the series compensator.
    :ivar varistor_rated_current: The maximum current the varistor is
        designed to handle at specified duration.
    :ivar varistor_voltage_threshold: The dc voltage at which the
        varistor start conducting.
    :ivar x: Positive sequence reactance.
    :ivar x0: Zero sequence reactance.
    """
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    varistor_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "varistorPresent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    varistor_rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "varistorRatedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    varistor_voltage_threshold: Optional[float] = field(
        default=None,
        metadata={
            "name": "varistorVoltageThreshold",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Substation(EquipmentContainer):
    """
    A collection of equipment for purposes other than generation or
    utilization, through which electric energy in bulk is passed for the
    purposes of switching or modifying its characteristics.

    :ivar bays: Bays contained in the substation.
    :ivar naming_feeder: The primary feeder that normally energizes the
        secondary substation. Used for naming purposes.  Either this
        association or the substation to subgeographical region should
        be used for hiearchical containment specification.
    :ivar normal_energized_feeder: The normal energized feeders of the
        substation. Also used for naming purposes.
    :ivar normal_energizing_feeder: The feeders that potentially
        energize  the downstream substation.  Should be consistent with
        the associations that describe the naming hiearchy.
    :ivar region: The SubGeographicalRegion containing the substation.
    :ivar voltage_levels: The voltage levels within this substation.
    """
    bays: List["Bay"] = field(
        default_factory=list,
        metadata={
            "name": "Bays",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    naming_feeder: Optional["Feeder"] = field(
        default=None,
        metadata={
            "name": "NamingFeeder",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_energized_feeder: List["Feeder"] = field(
        default_factory=list,
        metadata={
            "name": "NormalEnergizedFeeder",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_energizing_feeder: List["Feeder"] = field(
        default_factory=list,
        metadata={
            "name": "NormalEnergizingFeeder",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    region: Optional[SubGeographicalRegion] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltage_levels: List["VoltageLevel"] = field(
        default_factory=list,
        metadata={
            "name": "VoltageLevels",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Switch(ConductingEquipment):
    """A generic device designed to close, or open, or both, one or more
    electric circuits.

    All switches are two terminal devices including grounding switches.

    :ivar normal_open: The attribute is used in cases when no
        Measurement for the status value is present. If the Switch has a
        status measurement the Discrete.normalValue is expected to match
        with the Switch.normalOpen.
    :ivar open: The attribute tells if the switch is considered open
        when used as input to topology processing.
    :ivar rated_current: The maximum continuous current carrying
        capacity in amps governed by the device material and
        construction.
    :ivar retained: Branch is retained in a bus branch model.  The flow
        through retained switches will normally be calculated in power
        flow.
    :ivar composite_switch: Composite switch to which this Switch
        belongs.
    :ivar sv_switch: The switch state associated with the switch.
    :ivar switch_phase: The individual switch phases for the switch.
    :ivar switch_schedules: A Switch can be associated with
        SwitchSchedules.
    """
    normal_open: Optional[bool] = field(
        default=None,
        metadata={
            "name": "normalOpen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    open: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    retained: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    composite_switch: Optional[CompositeSwitch] = field(
        default=None,
        metadata={
            "name": "CompositeSwitch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_switch: List[SvSwitch] = field(
        default_factory=list,
        metadata={
            "name": "SvSwitch",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    switch_phase: List[SwitchPhase] = field(
        default_factory=list,
        metadata={
            "name": "SwitchPhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    switch_schedules: List[SwitchSchedule] = field(
        default_factory=list,
        metadata={
            "name": "SwitchSchedules",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VoltageLevel(EquipmentContainer):
    """A collection of equipment at one common system voltage forming a
    switchgear.

    The equipment typically consist of breakers, busbars,
    instrumentation, control, regulation and protection devices as well
    as assemblies of all these.

    :ivar high_voltage_limit: The bus bar's high voltage limit
    :ivar low_voltage_limit: The bus bar's low voltage limit
    :ivar base_voltage: The base voltage used for all equipment within
        the voltage level.
    :ivar bays: The bays within this voltage level.
    :ivar substation: The substation of the voltage level.
    """
    high_voltage_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "highVoltageLimit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    low_voltage_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowVoltageLimit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    base_voltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "name": "BaseVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    bays: List["Bay"] = field(
        default_factory=list,
        metadata={
            "name": "Bays",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    substation: Optional["Substation"] = field(
        default=None,
        metadata={
            "name": "Substation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_assembly_info: Optional[WireAssemblyInfo] = field(
        default=None,
        metadata={
            "name": "WireAssemblyInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wire_info: Optional["WireInfo"] = field(
        default=None,
        metadata={
            "name": "WireInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_position: Optional[WirePosition] = field(
        default=None,
        metadata={
            "name": "WirePosition",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltage_control_zone: Optional["VoltageControlZone"] = field(
        default=None,
        metadata={
            "name": "VoltageControlZone",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Cut(Switch):
    """A cut separates a line segment into two parts.

    The cut appears as a switch inserted between these two parts and
    connects them together. As the cut is normally open there is no
    galvanic connection between the two line segment parts. But it is
    possible to close the cut to get galvanic connection. The cut
    terminals are oriented towards the line segment terminals with the
    same sequence number. Hence the cut terminal with sequence number
    equal to 1 is oriented to the line segment's terminal with sequence
    number equal to 1. The cut terminals also act as connection points
    for jumpers and other equipment, e.g. a mobile generator. To enable
    this, connectivity nodes are placed at the cut terminals. Once the
    connectivity nodes are in place any conducting equipment can be
    connected at them.

    :ivar length_from_terminal1: The length to the place where the cut
        is located starting from side one of the cut line segment, i.e.
        the line segment Terminal with sequenceNumber equal to 1.
    :ivar acline_segment: The line segment to which the cut is applied.
    """
    length_from_terminal1: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthFromTerminal1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    acline_segment: Optional["AclineSegment"] = field(
        default=None,
        metadata={
            "name": "ACLineSegment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Disconnector(Switch):
    """A manually operated or motor operated mechanical switching device used
    for changing the connections in a circuit, or for isolating a circuit or
    equipment from a source of power.

    It is required to open or close circuits when negligible current is
    broken or made.
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_connection: Optional[PhaseShuntConnectionKind] = field(
        default=None,
        metadata={
            "name": "phaseConnection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energy_consumer_phase: List[EnergyConsumerPhase] = field(
        default_factory=list,
        metadata={
            "name": "EnergyConsumerPhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    house: Optional[House] = field(
        default=None,
        metadata={
            "name": "House",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    load_response: Optional[LoadResponseCharacteristic] = field(
        default=None,
        metadata={
            "name": "LoadResponse",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_cut_zone: Optional[PowerCutZone] = field(
        default=None,
        metadata={
            "name": "PowerCutZone",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltage_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltageAngle",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltage_magnitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltageMagnitude",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energy_source_phase: List[EnergySourcePhase] = field(
        default_factory=list,
        metadata={
            "name": "EnergySourcePhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Fuse(Switch):
    """An overcurrent protective device with a circuit opening fusible part
    that is heated and severed by the passage of overcurrent through it.

    A fuse is considered a switching device because it breaks current.
    """


@dataclass
class GroundDisconnector(Switch):
    """
    A manually operated or motor operated mechanical switching device used for
    isolating a circuit or equipment from ground.
    """


@dataclass
class GroundingImpedance(EarthFaultCompensator):
    """
    A fixed impedance device used for grounding.

    :ivar x: Reactance of device.
    """
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Jumper(Switch):
    """A short section of conductor with negligible impedance which can be
    manually removed and replaced if the circuit is de-energized.

    Note that zero-impedance branches can potentially be modeled by
    other equipment types.
    """


@dataclass
class Junction(Connector):
    """
    A point where one or more conducting equipments are connected with zero
    resistance.
    """


@dataclass
class PetersenCoil(EarthFaultCompensator):
    """
    A tunable impedance device normally used to offset line charging during
    single line faults in an ungrounded section of network.

    :ivar mode: The mode of operation of the Petersen coil.
    :ivar nominal_u: The nominal voltage for which the coil is designed.
    :ivar offset_current: The offset current that the Petersen coil
        controller is operating from the resonant point.  This is
        normally a fixed amount for which the controller is configured
        and could be positive or negative.  Typically 0 to 60 Amperes
        depending on voltage and resonance conditions.
    :ivar position_current: The control current used to control the
        Petersen coil also known as the position current.  Typically in
        the range of 20-200mA.
    :ivar x_ground_max: The maximum reactance.
    :ivar x_ground_min: The minimum reactance.
    :ivar x_ground_nominal: The nominal reactance.  This is the
        operating point (normally over compensation) that is defined
        based on the resonance point in the healthy network condition.
        The impedance is calculated based on nominal voltage divided by
        position current.
    """
    mode: Optional[PetersenCoilModeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominal_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    offset_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "offsetCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    position_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "positionCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_ground_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "xGroundMax",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_ground_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "xGroundMin",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x_ground_nominal: Optional[float] = field(
        default=None,
        metadata={
            "name": "xGroundNominal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    """Describes the tap model for an asymmetrical phase shifting transformer
    in which the difference voltage vector adds to the primary side voltage.

    The angle between the primary side voltage and the difference
    voltage is named the winding connection angle. The phase shift
    depends on both the difference voltage magnitude and the winding
    connection angle.

    :ivar winding_connection_angle: The phase angle between the in-phase
        winding and the out-of -phase winding used for creating phase
        shift. The out-of-phase winding produces what is known as the
        difference voltage.  Setting this angle to 90 degrees is not the
        same as a symmetrical transformer.
    """
    winding_connection_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "windingConnectionAngle",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhaseTapChangerSymmetrical(PhaseTapChangerNonLinear):
    """Describes a symmetrical phase shifting transformer tap model in which
    the secondary side voltage magnitude is the same as at the primary side.

    The difference voltage magnitude is the base in an equal-sided
    triangle where the sides corresponds to the primary and secondary
    voltages. The phase angle difference corresponds to the top angle
    and can be expressed as twice the arctangent of half the total
    difference voltage.
    """


@dataclass
class PhaseTapChangerTable(IdentifiedObject):
    """
    Describes a tabular curve for how the phase angle difference and impedance
    varies with the tap step.

    :ivar phase_tap_changer_table_point: The points of this table.
    :ivar phase_tap_changer_tabular: The phase tap changers to which
        this phase tap table applies.
    """
    phase_tap_changer_table_point: List[PhaseTapChangerTablePoint] = field(
        default_factory=list,
        metadata={
            "name": "PhaseTapChangerTablePoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    phase_tap_changer_tabular: List[PhaseTapChangerTabular] = field(
        default_factory=list,
        metadata={
            "name": "PhaseTapChangerTabular",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ProtectedSwitch(Switch):
    """
    A ProtectedSwitch is a switching device that can be operated by
    ProtectionEquipment.

    :ivar breaking_capacity: The maximum fault current a breaking device
        can break safely under prescribed conditions of use.
    """
    breaking_capacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "breakingCapacity",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    regulating_control: Optional["RegulatingControl"] = field(
        default=None,
        metadata={
            "name": "RegulatingControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
class Terminal(Acdcterminal):
    """An AC electrical connection point to a piece of conducting equipment.

    Terminals are connected at physical connection points called
    connectivity nodes.

    :ivar branch_group_terminal: The directed branch group terminals for
        which this terminal is monitored.
    :ivar bushing:
    :ivar conducting_equipment: The conducting equipment of the
        terminal.  Conducting equipment have  terminals that may be
        connected to other conducting equipment terminals via
        connectivity nodes or topological nodes.
    :ivar connectivity_node: The connectivity node to which this
        terminal connects with zero impedance.
    :ivar equipment_faults: The equipment faults at this terminal.
    :ivar has_first_mutual_coupling: Mutual couplings associated with
        the branch as the first branch.
    :ivar has_second_mutual_coupling: Mutual couplings with the branch
        associated as the first branch.
    :ivar normal_head_feeder: The feeder that this terminal normally
        feeds.  Only specifed for the terminals at head of feeders.
    :ivar regulating_control: The controls regulating this terminal.
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
    branch_group_terminal: List[BranchGroupTerminal] = field(
        default_factory=list,
        metadata={
            "name": "BranchGroupTerminal",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    bushing: Optional["Bushing"] = field(
        default=None,
        metadata={
            "name": "Bushing",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    conducting_equipment: Optional["ConductingEquipment"] = field(
        default=None,
        metadata={
            "name": "ConductingEquipment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    connectivity_node: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "name": "ConnectivityNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    equipment_faults: List["EquipmentFault"] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentFaults",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    has_first_mutual_coupling: List[MutualCoupling] = field(
        default_factory=list,
        metadata={
            "name": "HasFirstMutualCoupling",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    has_second_mutual_coupling: List[MutualCoupling] = field(
        default_factory=list,
        metadata={
            "name": "HasSecondMutualCoupling",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_head_feeder: Optional["Feeder"] = field(
        default=None,
        metadata={
            "name": "NormalHeadFeeder",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    regulating_control: List["RegulatingControl"] = field(
        default_factory=list,
        metadata={
            "name": "RegulatingControl",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_power_flow: List[SvPowerFlow] = field(
        default_factory=list,
        metadata={
            "name": "SvPowerFlow",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    topological_node: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "name": "TopologicalNode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformer_end: List[TransformerEnd] = field(
        default_factory=list,
        metadata={
            "name": "TransformerEnd",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
        ï¿½C.
    :ivar r_ac50: AC resistance per unit length of the conductor at 50
        ï¿½C.
    :ivar r_ac75: AC resistance per unit length of the conductor at 75
        ï¿½C.
    :ivar radius: Outside radius of the wire.
    :ivar rated_current: Current carrying capacity of the wire under
        stated thermal conditions.
    :ivar r_dc20: DC resistance per unit length of the conductor at 20
        ï¿½C.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    core_strand_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "coreStrandCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gmr: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    insulated: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    insulation_material: Optional[WireInsulationKind] = field(
        default=None,
        metadata={
            "name": "insulationMaterial",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    insulation_thickness: Optional[float] = field(
        default=None,
        metadata={
            "name": "insulationThickness",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    material: Optional[WireMaterialKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r_ac25: Optional[float] = field(
        default=None,
        metadata={
            "name": "rAC25",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r_ac50: Optional[float] = field(
        default=None,
        metadata={
            "name": "rAC50",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r_ac75: Optional[float] = field(
        default=None,
        metadata={
            "name": "rAC75",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    radius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r_dc20: Optional[float] = field(
        default=None,
        metadata={
            "name": "rDC20",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    size_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "sizeDescription",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    strand_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "strandCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    acline_segment_phases: List["AclineSegmentPhase"] = field(
        default_factory=list,
        metadata={
            "name": "ACLineSegmentPhases",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_phase_info: List[WirePhaseInfo] = field(
        default_factory=list,
        metadata={
            "name": "WirePhaseInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    acline_segment: Optional["AclineSegment"] = field(
        default=None,
        metadata={
            "name": "ACLineSegment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wire_info: Optional[WireInfo] = field(
        default=None,
        metadata={
            "name": "WireInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Breaker(ProtectedSwitch):
    """
    A mechanical switching device capable of making, carrying, and breaking
    currents under normal circuit conditions and also making, carrying for a
    specified time, and breaking currents under specified abnormal circuit
    conditions e.g.  those of short circuit.

    :ivar in_transit_time: The transition time from open to close.
    """
    in_transit_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "inTransitTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    diameter_over_core: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverCore",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    diameter_over_insulation: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverInsulation",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    diameter_over_jacket: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverJacket",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    diameter_over_screen: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverScreen",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    is_strand_fill: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isStrandFill",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominal_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalTemperature",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    outer_jacket_kind: Optional[CableOuterJacketKind] = field(
        default=None,
        metadata={
            "name": "outerJacketKind",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sheath_as_neutral: Optional[bool] = field(
        default=None,
        metadata={
            "name": "sheathAsNeutral",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shield_material: Optional[CableShieldMaterialKind] = field(
        default=None,
        metadata={
            "name": "shieldMaterial",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ConformLoad(EnergyConsumer):
    """
    ConformLoad represent loads that follow a daily load change pattern where
    the pattern can be used to scale the load with a system load.

    :ivar load_group: Group of this ConformLoad.
    """
    load_group: Optional[ConformLoadGroup] = field(
        default=None,
        metadata={
            "name": "LoadGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ExternalNetworkInjection(RegulatingCondEq):
    """
    This class represents external network and it is used for IEC 60909
    calculations.

    :ivar governor_scd: Power Frequency Bias. This is the change in
        power injection divided by the change in frequency and negated.
        A positive value of the power frequency bias provides additional
        power injection upon a drop in frequency.
    :ivar ik_second: Indicates whether initial symmetrical short-circuit
        current and power have been calculated according to IEC (Ik").
    :ivar max_initial_sym_sh_ccurrent: Maximum initial symmetrical
        short-circuit currents (Ik" max) in A (Ik" = Sk"/(SQRT(3) Un)).
        Used for short circuit data exchange according to IEC 60909
    :ivar max_p: Maximum active power of the injection.
    :ivar max_q: Not for short circuit modelling; It is used for
        modelling of infeed for load flow exchange. If maxQ and minQ are
        not used ReactiveCapabilityCurve can be used
    :ivar max_r0_to_x0_ratio: Maximum ratio of zero sequence resistance
        of Network Feeder to its zero sequence reactance (R(0)/X(0)
        max). Used for short circuit data exchange according to IEC
        60909
    :ivar max_r1_to_x1_ratio: Maximum ratio of positive sequence
        resistance of Network Feeder to its positive sequence reactance
        (R(1)/X(1) max). Used for short circuit data exchange according
        to IEC 60909
    :ivar max_z0_to_z1_ratio: Maximum ratio of zero sequence impedance
        to its positive sequence impedance (Z(0)/Z(1) max). Used for
        short circuit data exchange according to IEC 60909
    :ivar min_initial_sym_sh_ccurrent: Minimum initial symmetrical
        short-circuit currents (Ik" min) in A (Ik" = Sk"/(SQRT(3) Un)).
        Used for short circuit data exchange according to IEC 60909
    :ivar min_p: Minimum active power of the injection.
    :ivar min_q: Not for short circuit modelling; It is used for
        modelling of infeed for load flow exchange. If maxQ and minQ are
        not used ReactiveCapabilityCurve can be used
    :ivar min_r0_to_x0_ratio: Indicates whether initial symmetrical
        short-circuit current and power have been calculated according
        to IEC (Ik"). Used for short circuit data exchange according to
        IEC 6090
    :ivar min_r1_to_x1_ratio: Minimum ratio of positive sequence
        resistance of Network Feeder to its positive sequence reactance
        (R(1)/X(1) min). Used for short circuit data exchange according
        to IEC 60909
    :ivar min_z0_to_z1_ratio: Minimum ratio of zero sequence impedance
        to its positive sequence impedance (Z(0)/Z(1) min). Used for
        short circuit data exchange according to IEC 60909
    :ivar p: Active power injection. Load sign convention is used, i.e.
        positive sign means flow out from a node. Starting value for
        steady state solutions.
    :ivar q: Reactive power injection. Load sign convention is used,
        i.e. positive sign means flow out from a node. Starting value
        for steady state solutions.
    :ivar reference_priority: Priority of unit for use as powerflow
        voltage phase angle reference bus selection. 0 = don t care
        (default) 1 = highest priority. 2 is less than 1 and so on.
    :ivar voltage_factor: Voltage factor in pu, which was used to
        calculate short-circuit current Ik" and power Sk".
    """
    governor_scd: Optional[float] = field(
        default=None,
        metadata={
            "name": "governorSCD",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ik_second: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ikSecond",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_initial_sym_sh_ccurrent: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxInitialSymShCCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_q: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxQ",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_r0_to_x0_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxR0ToX0Ratio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_r1_to_x1_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxR1ToX1Ratio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_z0_to_z1_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxZ0ToZ1Ratio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_initial_sym_sh_ccurrent: Optional[float] = field(
        default=None,
        metadata={
            "name": "minInitialSymShCCurrent",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "minP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_q: Optional[float] = field(
        default=None,
        metadata={
            "name": "minQ",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_r0_to_x0_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "minR0ToX0Ratio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_r1_to_x1_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "minR1ToX1Ratio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_z0_to_z1_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "minZ0ToZ1Ratio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reference_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "referencePriority",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltage_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltageFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FrequencyConverter(RegulatingCondEq):
    """A device to convert from one frequency to another (e.g., frequency F1 to
    F2) comprises a pair of FrequencyConverter instances.

    One converts from F1 to DC, the other converts the DC to F2.

    :ivar frequency: Frequency on the AC side.
    :ivar max_p: The maximum active power on the DC side at which the
        frequence converter should operate.
    :ivar max_u: The maximum voltage on the DC side at which the
        frequency converter should operate.
    :ivar min_p: The minimum active power on the DC side at which the
        frequence converter should operate.
    :ivar min_u: The minimum voltage on the DC side at which the
        frequency converter should operate.
    """
    frequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "minP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "minU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class LoadBreakSwitch(ProtectedSwitch):
    """
    A mechanical switching device capable of making, carrying, and breaking
    currents under normal operating conditions.
    """


@dataclass
class NonConformLoad(EnergyConsumer):
    """
    NonConformLoad represent loads that do not follow a daily load change
    pattern and changes are not correlated with the daily load change pattern.

    :ivar load_group: Group of this ConformLoad.
    """
    load_group: Optional[NonConformLoadGroup] = field(
        default=None,
        metadata={
            "name": "LoadGroup",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OverheadWireInfo(WireInfo):
    """
    Overhead wire data.
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
    :ivar ieee1547_control_settings:
    :ivar ieee1547_info:
    :ivar ieee1547_setting:
    :ivar ieee1547_trip_settings:
    :ivar power_electronics_connection_phases:
    :ivar power_electronics_unit:
    """
    inverter_mode: Optional[SmartInverterMode] = field(
        default=None,
        metadata={
            "name": "inverterMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_ifault: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxIFault",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_q: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxQ",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_q: Optional[float] = field(
        default=None,
        metadata={
            "name": "minQ",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ieee1547_control_settings: Optional["Ieee1547ControlSettings"] = field(
        default=None,
        metadata={
            "name": "IEEE1547ControlSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ieee1547_info: Optional[Ieee1547Info] = field(
        default=None,
        metadata={
            "name": "IEEE1547Info",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ieee1547_setting: Optional[Ieee1547Setting] = field(
        default=None,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ieee1547_trip_settings: Optional[Ieee1547TripSettings] = field(
        default=None,
        metadata={
            "name": "IEEE1547TripSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_electronics_connection_phases: List[PowerElectronicsConnectionPhase] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnectionPhases",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_electronics_unit: List[PowerElectronicsUnit] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Recloser(ProtectedSwitch):
    """
    Pole-mounted fault interrupter with built-in phase and ground relays,
    current transformer (CT), and supplemental controls.
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maximum_sections: Optional[int] = field(
        default=None,
        metadata={
            "name": "maximumSections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nom_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "nomU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normal_sections: Optional[int] = field(
        default=None,
        metadata={
            "name": "normalSections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phase_connection: Optional[PhaseShuntConnectionKind] = field(
        default=None,
        metadata={
            "name": "phaseConnection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sections: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shunt_compensator_phase: List[ShuntCompensatorPhase] = field(
        default_factory=list,
        metadata={
            "name": "ShuntCompensatorPhase",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sv_shunt_compensator_sections: Optional[SvShuntCompensatorSections] = field(
        default=None,
        metadata={
            "name": "SvShuntCompensatorSections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class StaticVarCompensator(RegulatingCondEq):
    """A facility for providing variable and controllable shunt reactive power.

    The SVC typically consists of a stepdown transformer, filter,
    thyristor-controlled reactor, and thyristor-switched capacitor arms.
    The SVC may operate in fixed MVar output mode or in voltage control
    mode. When in voltage control mode, the output of the SVC will be
    proportional to the deviation of voltage at the controlled bus from
    the voltage setpoint.  The SVC characteristic slope defines the
    proportion.  If the voltage at the controlled bus is equal to the
    voltage setpoint, the SVC MVar output is zero.

    :ivar capacitive_rating: Maximum available capacitive reactance.
    :ivar inductive_rating: Maximum available inductive reactance.
    :ivar q: Reactive power injection. Load sign convention is used,
        i.e. positive sign means flow out from a node. Starting value
        for a steady state solution.
    :ivar slope: The characteristics slope of an SVC defines how the
        reactive power output changes in proportion to the difference
        between the regulated bus voltage and the voltage setpoint.
    :ivar s_vccontrol_mode: SVC control mode.
    :ivar voltage_set_point: The reactive power output of the SVC is
        proportional to the difference between the voltage at the
        regulated bus and the voltage setpoint.  When the regulated bus
        voltage is equal to the voltage setpoint, the reactive power
        output is zero.
    """
    capacitive_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "capacitiveRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    inductive_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "inductiveRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    slope: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    s_vccontrol_mode: Optional[SvccontrolMode] = field(
        default=None,
        metadata={
            "name": "sVCControlMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltage_set_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltageSetPoint",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class StationSupply(EnergyConsumer):
    """
    Station supply with load derived from the station output.
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
    :ivar short_circuit_end_temperature: Maximum permitted temperature
        at the end of SC for the calculation of minimum short-circuit
        currents. Used for short circuit data exchange according to IEC
        60909
    :ivar x: Positive sequence series reactance of the entire line
        section.
    :ivar x0: Zero sequence series reactance of the entire line section.
    :ivar acline_segment_phases: The line segment phases which belong to
        the line segment.
    :ivar clamp: The clamps connected to the line segment.
    :ivar cut: Cuts applied to the line segment.
    :ivar line_faults: The line faults of the line segment.
    :ivar parallel_line_segment:
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    bch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    short_circuit_end_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "shortCircuitEndTemperature",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    acline_segment_phases: List[AclineSegmentPhase] = field(
        default_factory=list,
        metadata={
            "name": "ACLineSegmentPhases",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    clamp: List[Clamp] = field(
        default_factory=list,
        metadata={
            "name": "Clamp",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cut: List[Cut] = field(
        default_factory=list,
        metadata={
            "name": "Cut",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    line_faults: List[LineFault] = field(
        default_factory=list,
        metadata={
            "name": "LineFaults",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    parallel_line_segment: Optional[ParallelLineSegment] = field(
        default=None,
        metadata={
            "name": "ParallelLineSegment",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    per_length_impedance: Optional[PerLengthImpedance] = field(
        default=None,
        metadata={
            "name": "PerLengthImpedance",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wire_spacing_info: Optional[WireSpacingInfo] = field(
        default=None,
        metadata={
            "name": "WireSpacingInfo",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
        neutral strand at 20 ï¿½C.
    """
    diameter_over_neutral: Optional[float] = field(
        default=None,
        metadata={
            "name": "diameterOverNeutral",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutral_strand_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "neutralStrandCount",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutral_strand_gmr: Optional[float] = field(
        default=None,
        metadata={
            "name": "neutralStrandGmr",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutral_strand_radius: Optional[float] = field(
        default=None,
        metadata={
            "name": "neutralStrandRadius",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutral_strand_rdc20: Optional[float] = field(
        default=None,
        metadata={
            "name": "neutralStrandRDC20",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Ieee1547ControlSettings:
    class Meta:
        name = "IEEE1547ControlSettings"

    constant_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "constantPowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    constant_reactive_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "constantReactivePower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_intentional_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceIntentionalDelay",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_max_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMaxFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_max_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMaxVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_min_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMinFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enter_service_min_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "enterServiceMinVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    frequency_droop_response_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "frequencyDroopResponseTime",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    open_loop_response_time_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "openLoopResponseTimeP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    over_frequency_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "overFrequencyDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    over_frequency_droop: Optional[float] = field(
        default=None,
        metadata={
            "name": "overFrequencyDroop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_constant_open_loop: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeConstantOpenLoop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    time_constant_reference_voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeConstantReferenceVoltage",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    under_frequency_deadband: Optional[float] = field(
        default=None,
        metadata={
            "name": "underFrequencyDeadband",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    under_frequency_droop: Optional[float] = field(
        default=None,
        metadata={
            "name": "underFrequencyDroop",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_q1: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarQ1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_q2: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarQ2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_q3: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarQ3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_q4: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarQ4",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_v1: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarV1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_v2: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarV2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_v3: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarV3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_var_v4: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltVarV4",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_watt_p1: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltWattP1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_watt_p2: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltWattP2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_watt_v1: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltWattV1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volt_watt_v2: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltWattV2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    watt_var_p1: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarP1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    watt_var_p2: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarP2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    watt_var_p3: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarP3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    watt_var_p4: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarP4",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    watt_var_q1: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarQ1",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    watt_var_q2: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarQ2",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    watt_var_q3: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarQ3",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    watt_var_q4: Optional[float] = field(
        default=None,
        metadata={
            "name": "wattVarQ4",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    power_electronics_connections: List[PowerElectronicsConnection] = field(
        default_factory=list,
        metadata={
            "name": "PowerElectronicsConnections",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rotating_machines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "name": "RotatingMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    b_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "bPerSection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g0_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "g0PerSection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g_per_section: Optional[float] = field(
        default=None,
        metadata={
            "name": "gPerSection",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class NonlinearShuntCompensator(ShuntCompensator):
    """
    A non linear shunt compensator has bank or section admittance values that
    differs.
    """
    nonlinear_shunt_compensator_points: List[NonlinearShuntCompensatorPoint] = field(
        default_factory=list,
        metadata={
            "name": "NonlinearShuntCompensatorPoints",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tape_thickness: Optional[float] = field(
        default=None,
        metadata={
            "name": "tapeThickness",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


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
    :ivar generating_unit: A synchronous machine may operate as a
        generator and as such becomes a member of a generating unit.
    :ivar hydro_pump: The synchronous machine drives the turbine which
        moves the water from a low elevation to a higher elevation. The
        direction of machine rotation for pumping may or may not be the
        same as for generating.
    :ivar ieee1547_control_settings:
    :ivar ieee1547_info:
    :ivar ieee1547_setting:
    :ivar ieee1547_trip_settings:
    """
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_power_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedPowerFactor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_s: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedS",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_u: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedU",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    generating_unit: Optional["GeneratingUnit"] = field(
        default=None,
        metadata={
            "name": "GeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydro_pump: Optional[HydroPump] = field(
        default=None,
        metadata={
            "name": "HydroPump",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ieee1547_control_settings: Optional[Ieee1547ControlSettings] = field(
        default=None,
        metadata={
            "name": "IEEE1547ControlSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ieee1547_info: Optional[Ieee1547Info] = field(
        default=None,
        metadata={
            "name": "IEEE1547Info",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ieee1547_setting: Optional[Ieee1547Setting] = field(
        default=None,
        metadata={
            "name": "IEEE1547Setting",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ieee1547_trip_settings: Optional[Ieee1547TripSettings] = field(
        default=None,
        metadata={
            "name": "IEEE1547TripSettings",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AsynchronousMachine(RotatingMachine):
    """A rotating machine whose shaft rotates asynchronously with the
    electrical field.

    Also known as an induction machine with no external connection to
    the rotor windings, e.g squirrel-cage induction machine.

    :ivar asynchronous_machine_type: Indicates the type of Asynchronous
        Machine (motor or generator).
    :ivar converter_fed_drive: Indicates whether the machine is a
        converter fed drive. Used for short circuit data exchange
        according to IEC 60909
    :ivar efficiency: Efficiency of the asynchronous machine at nominal
        operation in percent. Indicator for converter drive motors. Used
        for short circuit data exchange according to IEC 60909
    :ivar ia_ir_ratio: Ratio of locked-rotor current to the rated
        current of the motor (Ia/Ir). Used for short circuit data
        exchange according to IEC 60909
    :ivar nominal_frequency: Nameplate data indicates if the machine is
        50 or 60 Hz.
    :ivar nominal_speed: Nameplate data.  Depends on the slip and number
        of pole pairs.
    :ivar pole_pair_number: Number of pole pairs of stator. Used for
        short circuit data exchange according to IEC 60909
    :ivar rated_mechanical_power: Rated mechanical power (Pr in the IEC
        60909-0). Used for short circuit data exchange according to IEC
        60909.
    :ivar reversible: Indicates for converter drive motors if the power
        can be reversible. Used for short circuit data exchange
        according to IEC 60909
    :ivar rx_locked_rotor_ratio: Locked rotor ratio (R/X). Used for
        short circuit data exchange according to IEC 60909
    """
    asynchronous_machine_type: Optional[AsynchronousMachineKind] = field(
        default=None,
        metadata={
            "name": "asynchronousMachineType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    converter_fed_drive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "converterFedDrive",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    efficiency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ia_ir_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "iaIrRatio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominal_frequency: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalFrequency",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominal_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "nominalSpeed",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pole_pair_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "polePairNumber",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_mechanical_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedMechanicalPower",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reversible: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rx_locked_rotor_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "rxLockedRotorRatio",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class GeneratingUnit(Equipment):
    """A single or set of synchronous machines for converting mechanical power
    into alternating-current power.

    For example, individual machines within a set may be defined for
    scheduling purposes while a single control signal is derived for the
    set. In this case there would be a GeneratingUnit for each member of
    the set and an additional GeneratingUnit corresponding to the set.

    :ivar max_operating_p: This is the maximum operating active power
        limit the dispatcher can enter for this unit.
    :ivar min_operating_p: This is the minimum operating active power
        limit the dispatcher can enter for this unit.
    :ivar gen_unit_op_cost_curves: A generating unit may have one or
        more cost curves, depending upon fuel mixture and fuel cost.
    :ivar gen_unit_op_schedule: A generating unit may have an operating
        schedule, indicating the planned operation of the unit.
    :ivar gross_to_net_active_power_curves: A generating unit may have a
        gross active power to net active power curve, describing the
        losses and auxiliary power requirements of the unit.
    :ivar rotating_machine: A synchronous machine may operate as a
        generator and as such becomes a member of a generating unit.
    """
    max_operating_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxOperatingP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_operating_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "minOperatingP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gen_unit_op_cost_curves: List[GenUnitOpCostCurve] = field(
        default_factory=list,
        metadata={
            "name": "GenUnitOpCostCurves",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gen_unit_op_schedule: Optional[GenUnitOpSchedule] = field(
        default=None,
        metadata={
            "name": "GenUnitOpSchedule",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gross_to_net_active_power_curves: List[GrossToNetActivePowerCurve] = field(
        default_factory=list,
        metadata={
            "name": "GrossToNetActivePowerCurves",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rotating_machine: List[RotatingMachine] = field(
        default_factory=list,
        metadata={
            "name": "RotatingMachine",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class SynchronousMachine(RotatingMachine):
    """An electromechanical device that operates with shaft rotating
    synchronously with the network.

    It is a single machine operating either as a generator or
    synchronous condenser or pump.

    :ivar ikk: Steady-state short-circuit current (in A for the profile)
        of generator with compound excitation during 3-phase short
        circuit. - Ikk=0: Generator with no compound excitation. -
        Ikk?0: Generator with compound excitation. Ikk is used to
        calculate the minimum steady-state short-circuit current for
        generators with compound excitation (Section 4.6.1.2 in the IEC
        60909-0) Used only for single fed short circuit on a generator.
        (Section 4.3.4.2. in the IEC 60909-0)
    :ivar max_q: Maximum reactive power limit. This is the maximum
        (nameplate) limit for the unit.
    :ivar min_q: Minimum reactive power limit for the unit.
    :ivar operating_mode: Current mode of operation.
    :ivar type: Modes that this synchronous machine can operate in.
    :ivar initial_reactive_capability_curve: The default reactive
        capability curve for use by a synchronous machine.
    :ivar reactive_capability_curves: All available reactive capability
        curves for this synchronous machine.
    """
    ikk: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    max_q: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxQ",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    min_q: Optional[float] = field(
        default=None,
        metadata={
            "name": "minQ",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operating_mode: Optional[SynchronousMachineOperatingMode] = field(
        default=None,
        metadata={
            "name": "operatingMode",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    type: Optional[SynchronousMachineKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    initial_reactive_capability_curve: Optional["ReactiveCapabilityCurve"] = field(
        default=None,
        metadata={
            "name": "InitialReactiveCapabilityCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reactive_capability_curves: List["ReactiveCapabilityCurve"] = field(
        default_factory=list,
        metadata={
            "name": "ReactiveCapabilityCurves",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis,
    Pelton, Kaplan).

    :ivar energy_conversion_capability: Energy conversion capability for
        generating.
    :ivar hydro_unit_water_cost: The equivalent cost of water that
        drives the hydro turbine.
    :ivar hydro_generating_efficiency_curves: A hydro generating unit
        has an efficiency curve.
    :ivar hydro_power_plant: The hydro generating unit belongs to a
        hydro power plant.
    :ivar penstock_loss_curve: A hydro generating unit has a penstock
        loss curve.
    :ivar tailbay_loss_curve: A hydro generating unit has a tailbay loss
        curve.
    """
    energy_conversion_capability: Optional[HydroEnergyConversionKind] = field(
        default=None,
        metadata={
            "name": "energyConversionCapability",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydro_unit_water_cost: Optional[float] = field(
        default=None,
        metadata={
            "name": "hydroUnitWaterCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydro_generating_efficiency_curves: List[HydroGeneratingEfficiencyCurve] = field(
        default_factory=list,
        metadata={
            "name": "HydroGeneratingEfficiencyCurves",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydro_power_plant: Optional["HydroPowerPlant"] = field(
        default=None,
        metadata={
            "name": "HydroPowerPlant",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    penstock_loss_curve: Optional[PenstockLossCurve] = field(
        default=None,
        metadata={
            "name": "PenstockLossCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tailbay_loss_curve: List[TailbayLossCurve] = field(
        default_factory=list,
        metadata={
            "name": "TailbayLossCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class NuclearGeneratingUnit(GeneratingUnit):
    """
    A nuclear generating unit.
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydrogen_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "hydrogenPressure",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    initially_used_by_synchronous_machines: List[SynchronousMachine] = field(
        default_factory=list,
        metadata={
            "name": "InitiallyUsedBySynchronousMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    synchronous_machines: List[SynchronousMachine] = field(
        default_factory=list,
        metadata={
            "name": "SynchronousMachines",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class SolarGeneratingUnit(GeneratingUnit):
    """A solar thermal generating unit, connected to the grid by means of a
    rotating machine.

    This class does not represent photovoltaic (PV) generation.
    """


@dataclass
class ThermalGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover could be a steam turbine, combustion
    turbine, or diesel engine.

    :ivar o_mcost: Operating and maintenance cost for the thermal unit.
    :ivar caesplant: A thermal generating unit may be a member of a
        compressed air energy storage plant.
    :ivar cogeneration_plant: A thermal generating unit may be a member
        of a cogeneration plant.
    :ivar combined_cycle_plant: A thermal generating unit may be a
        member of a combined cycle plant.
    :ivar emission_curves: A thermal generating unit may have  one or
        more emission curves.
    :ivar emmission_accounts: A thermal generating unit may have one or
        more emission allowance accounts.
    :ivar fossil_fuels: A thermal generating unit may have one or more
        fossil fuels.
    :ivar fuel_allocation_schedules: A thermal generating unit may have
        one or more fuel allocation schedules.
    :ivar heat_input_curve: A thermal generating unit may have a heat
        input curve.
    :ivar heat_rate_curve: A thermal generating unit may have a heat
        rate curve.
    :ivar incremental_heat_rate_curve: A thermal generating unit may
        have an incremental heat rate curve.
    :ivar shutdown_curve: A thermal generating unit may have a shutdown
        curve.
    :ivar startup_model: A thermal generating unit may have a startup
        model.
    """
    o_mcost: Optional[float] = field(
        default=None,
        metadata={
            "name": "oMCost",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    caesplant: Optional["Caesplant"] = field(
        default=None,
        metadata={
            "name": "CAESPlant",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cogeneration_plant: Optional[CogenerationPlant] = field(
        default=None,
        metadata={
            "name": "CogenerationPlant",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    combined_cycle_plant: Optional[CombinedCyclePlant] = field(
        default=None,
        metadata={
            "name": "CombinedCyclePlant",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    emission_curves: List[EmissionCurve] = field(
        default_factory=list,
        metadata={
            "name": "EmissionCurves",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    emmission_accounts: List[EmissionAccount] = field(
        default_factory=list,
        metadata={
            "name": "EmmissionAccounts",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fossil_fuels: List[FossilFuel] = field(
        default_factory=list,
        metadata={
            "name": "FossilFuels",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuel_allocation_schedules: List[FuelAllocationSchedule] = field(
        default_factory=list,
        metadata={
            "name": "FuelAllocationSchedules",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heat_input_curve: Optional[HeatInputCurve] = field(
        default=None,
        metadata={
            "name": "HeatInputCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heat_rate_curve: Optional[HeatRateCurve] = field(
        default=None,
        metadata={
            "name": "HeatRateCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    incremental_heat_rate_curve: Optional[IncrementalHeatRateCurve] = field(
        default=None,
        metadata={
            "name": "IncrementalHeatRateCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shutdown_curve: Optional[ShutdownCurve] = field(
        default=None,
        metadata={
            "name": "ShutdownCurve",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startup_model: Optional[StartupModel] = field(
        default=None,
        metadata={
            "name": "StartupModel",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class WindGeneratingUnit(GeneratingUnit):
    """A wind driven generating unit, connected to the grid by means of a
    rotating machine.

    May be used to represent a single turbine or an aggregation.

    :ivar wind_gen_unit_type: The kind of wind generating unit
    """
    wind_gen_unit_type: Optional[WindGenUnitKind] = field(
        default=None,
        metadata={
            "name": "windGenUnitType",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Caesplant(PowerSystemResource):
    """
    Compressed air energy storage plant.

    :ivar energy_storage_capacity: The rated energy storage capacity.
    :ivar rated_capacity_p: The CAES plant's gross rated generating
        capacity.
    :ivar air_compressor: An air compressor may be a member of a
        compressed air energy storage plant.
    :ivar thermal_generating_unit: A thermal generating unit may be a
        member of a compressed air energy storage plant.
    """
    class Meta:
        name = "CAESPlant"

    energy_storage_capacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "energyStorageCapacity",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rated_capacity_p: Optional[float] = field(
        default=None,
        metadata={
            "name": "ratedCapacityP",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    air_compressor: Optional["AirCompressor"] = field(
        default=None,
        metadata={
            "name": "AirCompressor",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    thermal_generating_unit: Optional[ThermalGeneratingUnit] = field(
        default=None,
        metadata={
            "name": "ThermalGeneratingUnit",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AirCompressor(PowerSystemResource):
    """
    Combustion turbine air compressor which is an integral part of a compressed
    air energy storage (CAES) plant.

    :ivar air_compressor_rating: Rating of the CAES air compressor.
    :ivar caesplant: An air compressor may be a member of a compressed
        air energy storage plant.
    """
    air_compressor_rating: Optional[float] = field(
        default=None,
        metadata={
            "name": "airCompressorRating",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    caesplant: Optional[Caesplant] = field(
        default=None,
        metadata={
            "name": "CAESPlant",
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )

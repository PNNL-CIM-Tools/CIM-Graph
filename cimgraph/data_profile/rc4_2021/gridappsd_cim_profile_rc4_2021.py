from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime

__NAMESPACE__ = "http://iec.ch/TC57/CIM100#"



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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    aliasName: Optional[str] = field(
        default=None,
        metadata={
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
    Names: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AcceptanceTest:
    """
    Acceptance test for assets.

    :ivar dateTime: Date and time the asset was last tested using the
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
    dateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
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
    customerNotificationType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    methodType: Optional[str] = field(
        default=None,
        metadata={
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
    CustomerAccount: Optional["CustomerAccount"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


class AccumulationKind(Enum):
    """
    Kind of accumulation behaviour for read / measured values from individual
    end points.

    :cvar boundedQuantity: A time-independent cumulative quantity much
        like a 'bulkQuantity' or a 'latchingQuantity', except that the
        accumulation stops at the maximum or minimum values. When the
        maximum is reached, any additional positive accumulation is
        discarded, but negative accumulation may be accepted (thus
        lowering the counter.) Likewise, when the negative bound is
        reached, any additional negative accumulation is discarded, but
        positive accumulation is accepted (thus increasing the counter.)
    :cvar bulkQuantity: A value from a register which represents the
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
    :cvar continuousCumulative: The sum of the previous billing period
        values and the present period value. Note:
        'continuousCumulative' is commonly used in conjunction with
        'demand', and it  would represent the cumulative sum of the
        previous billing period maximum demand values (as occurring with
        each demand reset) summed with the present period maximum demand
        value (which has yet to be reset.)
    :cvar cumulative: The sum of the previous billing period values.
        Note: 'cumulative' is commonly used in conjunction with
        ï¿½demand.ï¿½ Each demand reset causes the maximum demand value
        for the present billing period (since the last demand reset) to
        accumulate as an accumulative total of all maximum demands. So
        instead of 'zeroing' the demand register, a demand reset has the
        effect of adding the present maximum demand to this accumulating
        total.
    :cvar deltaData: The difference between the value at the end of the
        prescribed interval and the beginning of the interval. This is
        used for incremental interval data. Note: One common application
        would be for load profile data, another use might be to report
        the number of events within an interval (such as the number of
        equipment energisations within the specified period of time.)
    :cvar indicating: As if a needle is swung out on the meter face to a
        value to indicate the current value. Note: An 'indicating' value
        is typically measured over hundreds of milliseconds or greater,
        or may imply a ï¿½pusherï¿½ mechanism to capture a value.
        Compare this to 'instantaneous' which is measured over a shorter
        period of time.
    :cvar instantaneous: Typically measured over the fastest period of
        time allowed by the definition of the metric (usually
        milliseconds or tens of milliseconds.) Note: 'instantaneous' was
        moved to attribute #3 in Ed.2 of IEC 61968-9, from attribute #1
        in Ed.1 of IEC 61968-9.
    :cvar latchingQuantity: When this description is applied to a
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
    :cvar none: Not applicable, or implied by the unit of measure.
    :cvar summation: A form of accumulation which is selective with
        respect to time. Note : 'summation' could be considered a
        specialisation of 'bulkQuantity' as it selectively accumulates
        pulses over a timing pattern (while 'bulkQuantity' accumulates
        pulses all of the time).
    :cvar timeDelay: A form of computation which introduces a time delay
        characteristic to the data value.
    """
    boundedQuantity = "boundedQuantity"
    bulkQuantity = "bulkQuantity"
    continuousCumulative = "continuousCumulative"
    cumulative = "cumulative"
    deltaData = "deltaData"
    indicating = "indicating"
    instantaneous = "instantaneous"
    latchingQuantity = "latchingQuantity"
    none = "none"
    summation = "summation"
    timeDelay = "timeDelay"


class AggregateKind(Enum):
    """
    Kind of aggregation for read / measured values from multiple end points.

    :cvar average: The value represents average.
    :cvar excess: The value represents an amount over which a threshold
        was exceeded.
    :cvar fifthMaximum: The fifth highest value observed.
    :cvar fourthMaximum: The fourth highest value observed.
    :cvar highThreshold: The value represents a programmed high
        threshold.
    :cvar lowThreshold: The value represents a programmed low threshold.
    :cvar maximum: The highest value observed.
    :cvar minimum: The smallest value observed.
    :cvar nominal: The nominal value.
    :cvar none: Not applicable.
    :cvar normal: The normal value.
    :cvar secondMaximum: The second highest value observed.
    :cvar secondMinimum: The second smallest value observed.
    :cvar sum: The accumulated sum.
    :cvar thirdMaximum: The third highest value observed.
    """
    average = "average"
    excess = "excess"
    fifthMaximum = "fifthMaximum"
    fourthMaximum = "fourthMaximum"
    highThreshold = "highThreshold"
    lowThreshold = "lowThreshold"
    maximum = "maximum"
    minimum = "minimum"
    nominal = "nominal"
    none = "none"
    normal = "normal"
    secondMaximum = "secondMaximum"
    secondMinimum = "secondMinimum"
    sum = "sum"
    thirdMaximum = "thirdMaximum"


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


class AnalyticKind(Enum):
    """
    Possible kinds of analytics.
    """
    agingAnalytic = "agingAnalytic"
    faultAnalytic = "faultAnalytic"
    healthAnalytic = "healthAnalytic"
    other = "other"
    replacementAnalytic = "replacementAnalytic"
    riskAnalytic = "riskAnalytic"


class AssetFailureTypeification(Enum):
    defect = "defect"
    major = "major"
    majorNeedsReplacement = "majorNeedsReplacement"
    minor = "minor"


class AssetFailureMode(Enum):
    """What asset has failed to be able to do.

    Reason for breaker failure.
    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    failToCarryLoad = "failToCarryLoad"
    failToClose = "failToClose"
    failToInterrupt = "failToInterrupt"
    failToOpen = "failToOpen"
    failToProvideInsulationLevel = "failToProvideInsulationLevel"


class AssetGroupKind(Enum):
    """
    Possible kinds of asset groups.

    :cvar analysisGroup:
    :cvar complianceGroup:
    :cvar functionalGroup: assets grouped together for a particular
        function - such as a group of feeders.
    :cvar inventoryGroup:
    :cvar other:
    """
    analysisGroup = "analysisGroup"
    complianceGroup = "complianceGroup"
    functionalGroup = "functionalGroup"
    inventoryGroup = "inventoryGroup"
    other = "other"


class AssetHazardKind(Enum):
    """Type of hazard that is posed to asset in this location.

    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).

    :cvar ambientTempAbove38: Subject to ambient temperature above 38
        ï¿½C.
    :cvar ambientTempBelowMinus12: Subject to ambient temperature of
        below -12 ï¿½C.
    :cvar childrenAtPlay: Children play in area (stray kite/ball
        hazard).
    :cvar fishingArea: Fishing in area (fishing pole/line hazard).
    :cvar other: If other, look at type field for more information.
    :cvar vegetation: Vegetation growing below asset that may cause
        problem.
    """
    ambientTempAbove38 = "ambientTempAbove38"
    ambientTempBelowMinus12 = "ambientTempBelowMinus12"
    childrenAtPlay = "childrenAtPlay"
    fishingArea = "fishingArea"
    other = "other"
    vegetation = "vegetation"


class AssetKind(Enum):
    """
    :cvar breakerAirBlastBreaker:
    :cvar breakerBulkOilBreaker:
    :cvar breakerInsulatingStackAssembly:
    :cvar breakerMinimumOilBreaker:
    :cvar breakerSF6DeadTankBreaker:
    :cvar breakerSF6LiveTankBreaker:
    :cvar breakerTankAssembly:
    :cvar other: Other type of Asset. The type attribute may provide
        more details in this case.
    :cvar transformer:
    :cvar transformerTank:
    """
    breakerAirBlastBreaker = "breakerAirBlastBreaker"
    breakerBulkOilBreaker = "breakerBulkOilBreaker"
    breakerInsulatingStackAssembly = "breakerInsulatingStackAssembly"
    breakerMinimumOilBreaker = "breakerMinimumOilBreaker"
    breakerSF6DeadTankBreaker = "breakerSF6DeadTankBreaker"
    breakerSF6LiveTankBreaker = "breakerSF6LiveTankBreaker"
    breakerTankAssembly = "breakerTankAssembly"
    other = "other"
    transformer = "transformer"
    transformerTank = "transformerTank"


class AssetModelUsageKind(Enum):
    """
    Usage for an asset model.

    :cvar customerSubstation: Asset model is intended for use in
        customer substation.
    :cvar distributionOverhead: Asset model is intended for use in
        distribution overhead network.
    :cvar distributionUnderground: Asset model is intended for use in
        underground distribution network.
    :cvar other: Other kind of asset model usage.
    :cvar streetlight: Asset model is intended for use as streetlight.
    :cvar substation: Asset model is intended for use in substation.
    :cvar transmission: Asset model is intended for use in transmission
        network.
    :cvar unknown: Usage of the asset model is unknown.
    """
    customerSubstation = "customerSubstation"
    distributionOverhead = "distributionOverhead"
    distributionUnderground = "distributionUnderground"
    other = "other"
    streetlight = "streetlight"
    substation = "substation"
    transmission = "transmission"
    unknown = "unknown"


class AsynchronousMachineKind(Enum):
    """
    Kind of Asynchronous Machine.

    :cvar generator: The Asynchronous Machine is a generator.
    :cvar motor: The Asynchronous Machine is a motor.
    """
    generator = "generator"
    motor = "motor"


class AtmosphericAnalogKind(Enum):
    """
    Kinds of analogs measuring an atmospheric condition.

    :cvar albedo:
    :cvar ambientTemperature: The temperature measured b&lt;font
        color="#0f0f0f"&gt;y a thermometer exposed to the air in a place
        sheltered from direct solar radiation. &lt;/font&gt;Also known
        as "dry bulb" because&lt;font color="#0f0f0f"&gt; the air
        temperature is indicated by a thermometer not
        affecte&lt;/font&gt;d by the moisture of the air.
    :cvar atmosphericPressure:
    :cvar ceiling:
    :cvar dewPoint: The temperature to which air must be cooled at
        constant pressure and constant water-vapor content in order for
        saturation to occur. In other words, it is the temperature at
        which water vapor starts to condense out of the air.
    :cvar heatIndex: The temperature of how hot it "feels like" for a
        given combination of warm air temperature and relative humidity.
    :cvar horizontalVisibility:
    :cvar humidity:
    :cvar ice:
    :cvar illuminanceDiffuseHorizontal:
    :cvar illuminanceDirectNormal:
    :cvar illuminanceGlobalHorizontal:
    :cvar irradianceDiffuseHorizonal:
    :cvar irradianceDirectNormal:
    :cvar irradianceExtraTerrestrialHorizontal:
    :cvar irradianceExtraTerrestrialVertical:
    :cvar irradianceGlobalHorizontal:
    :cvar luminanceZenith:
    :cvar precipitation:
    :cvar rain:
    :cvar skyCoverageOpaque:
    :cvar skyCoverageTotal:
    :cvar snow: Snow amount over a specified period of time.
    :cvar verticalVisibility:
    :cvar windChill: The temperature of how cold it "feels like" based
        on the rate of heat loss from exposed skin caused by the effects
        of wind and cold temperatures.
    :cvar windSpeedGust: Maximum instantaneous wind speed in the 10
        minute period preceding a moment in time so long as more than 10
        knots of difference has been exhibited between peaks and lulls
        during that 10 minute time period. 0 value means no gusts during
        preceding 10 minute period.
    :cvar windSpeedInstantaneous: Wind speed at a moment in time.
    :cvar windSpeedPeak: Peak instantaneous wind speed in the 60 minutes
        preceding a moment in time as long as peak speed greater than 25
        knots. 0 value means speed did not exceed 25 knots during
        preceding 60 minutes.
    :cvar windSpeedSustained: Average instantaneous wind speed over the
        2-minute time period preceding a moment in time.
    """
    albedo = "albedo"
    ambientTemperature = "ambientTemperature"
    atmosphericPressure = "atmosphericPressure"
    ceiling = "ceiling"
    dewPoint = "dewPoint"
    heatIndex = "heatIndex"
    horizontalVisibility = "horizontalVisibility"
    humidity = "humidity"
    ice = "ice"
    illuminanceDiffuseHorizontal = "illuminanceDiffuseHorizontal"
    illuminanceDirectNormal = "illuminanceDirectNormal"
    illuminanceGlobalHorizontal = "illuminanceGlobalHorizontal"
    irradianceDiffuseHorizonal = "irradianceDiffuseHorizonal"
    irradianceDirectNormal = "irradianceDirectNormal"
    irradianceExtraTerrestrialHorizontal = "irradianceExtraTerrestrialHorizontal"
    irradianceExtraTerrestrialVertical = "irradianceExtraTerrestrialVertical"
    irradianceGlobalHorizontal = "irradianceGlobalHorizontal"
    luminanceZenith = "luminanceZenith"
    precipitation = "precipitation"
    rain = "rain"
    skyCoverageOpaque = "skyCoverageOpaque"
    skyCoverageTotal = "skyCoverageTotal"
    snow = "snow"
    verticalVisibility = "verticalVisibility"
    windChill = "windChill"
    windSpeedGust = "windSpeedGust"
    windSpeedInstantaneous = "windSpeedInstantaneous"
    windSpeedPeak = "windSpeedPeak"
    windSpeedSustained = "windSpeedSustained"


class BatteryState(Enum):
    """
    :cvar Charging: storedE is increasing
    :cvar Discharging: storedE is decreasing
    :cvar Empty: unable to Discharge, and not Charging
    :cvar Full: unable to Charge, and not Discharging
    :cvar Waiting: neither Charging nor Discharging, but able to do so
    """
    Charging = "Charging"
    Discharging = "Discharging"
    Empty = "Empty"
    Full = "Full"
    Waiting = "Waiting"


class BreakerApplicationKind(Enum):
    """Classifications of network roles in which breakers can be deployed.

    The classifications are intended to reflect both criticality of breaker in network operations and typical usage experienced by breaker.
    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    busBreaker = "busBreaker"
    busTieBreaker = "busTieBreaker"
    capacitorOrReactorBankBreaker = "capacitorOrReactorBankBreaker"
    feederBreaker = "feederBreaker"
    other = "other"
    spare = "spare"
    stepUpTransformerBreakerFossil = "stepUpTransformerBreakerFossil"
    stepUpTransformerBreakerHydro = "stepUpTransformerBreakerHydro"
    stepUpTransformerBreakerNuclear = "stepUpTransformerBreakerNuclear"
    stepUpTransformerBreakerPumpedStorage = "stepUpTransformerBreakerPumpedStorage"
    substationTransformerBreaker = "substationTransformerBreaker"
    transmissionFlowGateLineBreaker = "transmissionFlowGateLineBreaker"
    transmissionLineBreaker = "transmissionLineBreaker"
    transmissionTieLineBreaker = "transmissionTieLineBreaker"


class BreakerConfiguration(Enum):
    """
    Switching arrangement for bay.

    :cvar breakerAndAHalf: Breaker and a half.
    :cvar doubleBreaker: Double breaker.
    :cvar noBreaker: No breaker.
    :cvar singleBreaker: Single breaker.
    """
    breakerAndAHalf = "breakerAndAHalf"
    doubleBreaker = "doubleBreaker"
    noBreaker = "noBreaker"
    singleBreaker = "singleBreaker"


class BreakerFailureReasonKind(Enum):
    """Reason for breaker failure.

    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    SF6BlastValveFailure = "SF6BlastValveFailure"
    SF6PufferFailure = "SF6PufferFailure"
    blastValveFailure = "blastValveFailure"
    bushingFailure = "bushingFailure"
    closeCoilOpenShortedFailed = "closeCoilOpenShortedFailed"
    contaminatedAir = "contaminatedAir"
    contaminatedArcChutes = "contaminatedArcChutes"
    contaminatedGas = "contaminatedGas"
    contaminatedGasAir = "contaminatedGasAir"
    controlCircuitFailure = "controlCircuitFailure"
    degradedLubrication = "degradedLubrication"
    externalOrInternalContamination = "externalOrInternalContamination"
    highPressureAirPlant = "highPressureAirPlant"
    highResistanceLoadPath = "highResistanceLoadPath"
    highResistancePath = "highResistancePath"
    interrupterContactFailure = "interrupterContactFailure"
    interrupterFailure = "interrupterFailure"
    linkageFailure = "linkageFailure"
    lossOfOil = "lossOfOil"
    lossOfVacuum = "lossOfVacuum"
    lowGasPressure = "lowGasPressure"
    mechanismFailure = "mechanismFailure"
    mechanismOrLinkageFailure = "mechanismOrLinkageFailure"
    oilRelatedFailure = "oilRelatedFailure"
    poorOilQuality = "poorOilQuality"
    rackingMechanismFailure = "rackingMechanismFailure"
    resistorFailure = "resistorFailure"
    resistorGradingCapacitorFailure = "resistorGradingCapacitorFailure"
    solidDielectricFailure = "solidDielectricFailure"
    storedEnergyFailure = "storedEnergyFailure"
    tripCoilOpenShortedFailed = "tripCoilOpenShortedFailed"


class BusbarConfiguration(Enum):
    """
    Busbar layout for bay.

    :cvar doubleBus: Double bus.
    :cvar mainWithTransfer: Main bus with transfer bus.
    :cvar ringBus: Ring bus.
    :cvar singleBus: Single bus.
    """
    doubleBus = "doubleBus"
    mainWithTransfer = "mainWithTransfer"
    ringBus = "ringBus"
    singleBus = "singleBus"


class BushingInsulationKind(Enum):
    """
    Insulation kind for bushings.

    :cvar compound:
    :cvar oilImpregnatedPaper: &amp;lt;was paperoil&amp;gt;.
    :cvar other:
    :cvar resinBondedPaper:
    :cvar resinImpregnatedPaper:
    :cvar solidPorcelain:
    """
    compound = "compound"
    oilImpregnatedPaper = "oilImpregnatedPaper"
    other = "other"
    resinBondedPaper = "resinBondedPaper"
    resinImpregnatedPaper = "resinImpregnatedPaper"
    solidPorcelain = "solidPorcelain"


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


class CloudKind(Enum):
    altoCumulus = "altoCumulus"
    altoStratus = "altoStratus"
    cirroCumulus = "cirroCumulus"
    cirroStratus = "cirroStratus"
    cirrus = "cirrus"
    cumuloNimbus = "cumuloNimbus"
    cumulus = "cumulus"
    nimboStratus = "nimboStratus"
    other = "other"
    stratoCumulus = "stratoCumulus"
    stratus = "stratus"
    toweringCumulus = "toweringCumulus"


class ComDirectionKind(Enum):
    """
    Kind of communication direction.

    :cvar biDirectional: Communication with the device is bi-
        directional.
    :cvar fromDevice: Communication is from device.
    :cvar toDevice: Communication is to device.
    """
    biDirectional = "biDirectional"
    fromDevice = "fromDevice"
    toDevice = "toDevice"


class ComTechnologyKind(Enum):
    """
    Kind of communication technology.

    :cvar cellular: Communicates using a public cellular radio network.
        A specific variant of 'rf'.
    :cvar ethernet: Communicates using one or more of a family of frame-
        based computer networking technologies conforming to the IEEE
        802.3 standard.
    :cvar homePlug: Communicates using power line communication
        technologies conforming to the standards established by the
        HomePlug Powerline Alliance. A specific variant of 'plc'.
    :cvar pager: Communicates using a public one-way or two-way radio-
        based paging network. A specific variant of 'rf'.
    :cvar phone: Communicates using a basic, wireline telephone system.
    :cvar plc: Communicates using power line communication technologies.
    :cvar rf: Communicates using private or public radio-based
        technology.
    :cvar rfMesh: Communicates using a mesh radio technology. A specific
        variant of 'rf'.
    :cvar zigbee: Communicates using radio communication technologies
        conforming to the standards established by the ZigBee. A
        specific variant of 'rf'.
    """
    cellular = "cellular"
    ethernet = "ethernet"
    homePlug = "homePlug"
    pager = "pager"
    phone = "phone"
    plc = "plc"
    rf = "rf"
    rfMesh = "rfMesh"
    zigbee = "zigbee"


class CommodityKind(Enum):
    """
    Kind of commodity being measured.

    :cvar air:
    :cvar carbon:
    :cvar ch4: Methane CH&lt;sub&gt;4&lt;/sub&gt;
    :cvar co2: Carbon Dioxide CO&lt;sub&gt;2&lt;/sub&gt;
    :cvar communication: A measurement of the communication
        infrastructure itself.
    :cvar coolingFluid: The cool fluid returns warmer than when it was
        sent. The heat conveyed may be metered.
    :cvar electricityPrimaryMetered: It is possible for a meter to be
        outfitted with an external VT and/or CT. The meter might not be
        aware of these devices, and the display not compensate for their
        presence. Ultimately, when these scalars are applied, the value
        that represents the service value is called the ï¿½primary
        meteredï¿½ value. The ï¿½indexï¿½ in sub-category 3 mirrors
        those of sub-category 0.
    :cvar electricitySecondaryMetered: All types of metered quantities.
        This type of reading comes from the meter and represents a
        ï¿½secondaryï¿½ metered value.
    :cvar hch: Hexachlorocyclohexane HCH
    :cvar heatingFluid: This fluid is likely in liquid form. It is not
        necessarily water or water based. The warm fluid returns cooler
        than when it was sent. The heat conveyed may be metered.
    :cvar insulativeGas: (SF&lt;sub&gt;6&lt;/sub&gt; is found separately
        below.)
    :cvar insulativeOil:
    :cvar internet: Internet service
    :cvar naturalGas:
    :cvar none: Not Applicable
    :cvar nonpotableWater: Reclaimed water ï¿½ possibly used for
        irrigation but not sufficiently treated to be considered safe
        for drinking.
    :cvar nox: Nitrous Oxides NO&lt;sub&gt;X&lt;/sub&gt;
    :cvar pfc: Perfluorocarbons PFC
    :cvar potableWater: Drinkable water
    :cvar propane:
    :cvar refuse: trash
    :cvar sf6: Sulfurhexafluoride SF&lt;sub&gt;6&lt;/sub&gt;
    :cvar so2: Sulfur Dioxide SO&lt;sub&gt;2&lt;/sub&gt;
    :cvar steam: Water in steam form, usually used for heating.
    :cvar tvLicence: Television
    :cvar wasteWater: (Sewerage)
    """
    air = "air"
    carbon = "carbon"
    ch4 = "ch4"
    co2 = "co2"
    communication = "communication"
    coolingFluid = "coolingFluid"
    electricityPrimaryMetered = "electricityPrimaryMetered"
    electricitySecondaryMetered = "electricitySecondaryMetered"
    hch = "hch"
    heatingFluid = "heatingFluid"
    insulativeGas = "insulativeGas"
    insulativeOil = "insulativeOil"
    internet = "internet"
    naturalGas = "naturalGas"
    none = "none"
    nonpotableWater = "nonpotableWater"
    nox = "nox"
    pfc = "pfc"
    potableWater = "potableWater"
    propane = "propane"
    refuse = "refuse"
    sf6 = "sf6"
    so2 = "so2"
    steam = "steam"
    tvLicence = "tvLicence"
    wasteWater = "wasteWater"


@dataclass
class ControlledAppliance:
    """
    Appliance controlled with a PAN device control.

    :ivar isElectricVehicle: True if the appliance is an electric
        vehicle.
    :ivar isExteriorLighting: True if the appliance is exterior
        lighting.
    :ivar isGenerationSystem: True if the appliance is a generation
        system.
    :ivar isHvacCompressorOrFurnace: True if the appliance is HVAC
        compressor or furnace.
    :ivar isInteriorLighting: True if the appliance is interior
        lighting.
    :ivar isIrrigationPump: True if the appliance is an irrigation pump.
    :ivar isManagedCommercialIndustrialLoad: True if the appliance is
        managed commercial or industrial load.
    :ivar isPoolPumpSpaJacuzzi: True if the appliance is a pool, pump,
        spa or jacuzzi.
    :ivar isSimpleMiscLoad: True if the appliance is a simple
        miscellaneous load.
    :ivar isSmartAppliance: True if the appliance is a smart appliance.
    :ivar isStripAndBaseboardHeater: True if the appliance is a stip or
        baseboard heater.
    :ivar isWaterHeater: True if the appliance is a water heater.
    """
    isElectricVehicle: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isExteriorLighting: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isGenerationSystem: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isHvacCompressorOrFurnace: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isInteriorLighting: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isIrrigationPump: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isManagedCommercialIndustrialLoad: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isPoolPumpSpaJacuzzi: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isSimpleMiscLoad: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isSmartAppliance: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isStripAndBaseboardHeater: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isWaterHeater: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class CorporateStandardKind(Enum):
    """
    Kind of corporate standard.

    :cvar experimental: Asset model is used experimentally.
    :cvar other: Other kind of corporate standard for the asset model.
    :cvar standard: Asset model is used as corporate standard.
    :cvar underEvaluation: Asset model usage is under evaluation.
    """
    experimental = "experimental"
    other = "other"
    standard = "standard"
    underEvaluation = "underEvaluation"


class CoverageCodeKind(Enum):
    """
    Kinds of weather condition coverage.
    """
    brief = "brief"
    frequent = "frequent"
    intermittant = "intermittant"
    isolated = "isolated"
    numerous = "numerous"
    occasional = "occasional"
    partly = "partly"
    patchy = "patchy"
    periodsOf = "periodsOf"
    scattered = "scattered"
    widespread = "widespread"


class CrewStatusKind(Enum):
    """
    the enumerated values for the dispatch status.

    :cvar arrived: Indicates that one or more crews have arrived at the
        work site
    :cvar assigned: Indicates that one or more crews have been assigned
        to the work
    :cvar awaitingCrewAssignment: Indicates that the work is awaiting
        one or more crews to be assigned
    :cvar enroute: Indicates that one or more crews are traveling to the
        work site(s)
    :cvar fieldComplete: Indicates that the work at one or more work
        sites has been completed
    """
    arrived = "arrived"
    assigned = "assigned"
    awaitingCrewAssignment = "awaitingCrewAssignment"
    enroute = "enroute"
    fieldComplete = "fieldComplete"


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
    :ivar Curve: The curve of  this curve data point.
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
    Curve: Optional["Curve"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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


class CustomerKind(Enum):
    """
    Kind of customer.

    :cvar commercialIndustrial: Commercial industrial customer.
    :cvar energyServiceScheduler: Customer as energy service scheduler.
    :cvar energyServiceSupplier: Customer as energy service supplier.
    :cvar enterprise:
    :cvar internalUse: Internal use customer.
    :cvar other: Other kind of customer.
    :cvar pumpingLoad: Pumping load customer.
    :cvar regionalOperator:
    :cvar residential: Residential customer.
    :cvar residentialAndCommercial: Residential and commercial customer.
    :cvar residentialAndStreetlight: Residential and streetlight
        customer.
    :cvar residentialFarmService: Residential farm service customer.
    :cvar residentialStreetlightOthers: Residential streetlight or other
        related customer.
    :cvar subsidiary:
    :cvar windMachine: Wind machine customer.
    """
    commercialIndustrial = "commercialIndustrial"
    energyServiceScheduler = "energyServiceScheduler"
    energyServiceSupplier = "energyServiceSupplier"
    enterprise = "enterprise"
    internalUse = "internalUse"
    other = "other"
    pumpingLoad = "pumpingLoad"
    regionalOperator = "regionalOperator"
    residential = "residential"
    residentialAndCommercial = "residentialAndCommercial"
    residentialAndStreetlight = "residentialAndStreetlight"
    residentialFarmService = "residentialFarmService"
    residentialStreetlightOthers = "residentialStreetlightOthers"
    subsidiary = "subsidiary"
    windMachine = "windMachine"


@dataclass
class DERFunction:
    connectDisconnect: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    frequencyWattCurveFunction: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxRealPowerLimiting: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rampRateControl: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reactivePowerDispatch: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    realPowerDispatch: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltageRegulation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltVarCurveFunction: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltWattCurveFunction: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceGroup: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :cvar As: Ampere seconds (Aï¿½s).
    :cvar Btu: Energy, British Thermal Unit.
    :cvar Hz: Frequency in Hertz (1/s).
    :cvar Q: Quantity power, Q.
    :cvar Qh: Quantity energy, Qh.
    :cvar V: Electric potential in Volt (W/A).
    :cvar VA: Apparent power in Volt Ampere (See also real power and
        reactive power.)
    :cvar VAh: Apparent energy in Volt Ampere hours.
    :cvar VAr: Reactive power in Volt Ampere reactive. The
        ï¿½reactiveï¿½ or ï¿½imaginaryï¿½ component of electrical power
        (VIsin(phi)). (See also real power and apparent power). Note:
        Different meter designs use different methods to arrive at their
        results. Some meters may compute reactive power as an arithmetic
        value, while others compute the value vectorially. The data
        consumer should determine the method in use and the suitability
        of the measurement for the intended purpose.
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
        (Iï¿½R or VIcos(phi)), is expressed in Watts. (See also apparent
        power and reactive power.)
    :cvar WPerA: Active power per current flow, watt per Ampere.
    :cvar WPers: Ramp rate in Watt per second.
    :cvar Wh: Real energy in Watt hours.
    :cvar deg: Plane angle in degrees.
    :cvar degC: Relative temperature in degrees Celsius. In the SI unit
        system the symbol is ï¿½C. Electric charge is measured in
        coulomb that has the unit symbol C. To distinguish degree
        Celsius form coulomb the symbol used in the UML is degC. Reason
        for not using ï¿½C is the special character ï¿½ is difficult to
        manage in software.
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


class DINStandardEditionKind(Enum):
    """
    List of editions for DIN standards.
    """
    value_1985 = "1985"
    none = "none"
    unknown = "unknown"


class DINStandardKind(Enum):
    """
    List of DIN standards.

    :cvar value_51353: Testing of insulating oils; detection of
        corrosive sulfur; silver strip test.
    """
    value_51353 = "51353"


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

    :ivar inServiceDate: Date and time asset most recently put in
        service.
    :ivar installedDate: Date and time asset most recently installed.
    :ivar notYetInstalledDate: Date and time of asset deployment
        transition to not yet installed.
    :ivar outOfServiceDate: Date and time asset most recently taken out
        of service.
    :ivar removedDate: Date and time asset most recently removed.
    """
    inServiceDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    installedDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    notYetInstalledDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    outOfServiceDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    removedDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class DeploymentStateKind(Enum):
    """
    Possible states of asset deployment.
    """
    inService = "inService"
    installed = "installed"
    notYetInstalled = "notYetInstalled"
    outOfService = "outOfService"
    removed = "removed"


class DobleStandardEditionKind(Enum):
    """
    List of editions for Doble standards.
    """
    none = "none"
    unknown = "unknown"


class DobleStandardKind(Enum):
    """
    List of Doble standards.

    :cvar methanol: Doble test for methanol.
    """
    methanol = "methanol"


class EPAStandardEditionKind(Enum):
    """
    List of editions for EPA standards.
    """
    A = "A"
    none = "none"
    unknown = "unknown"


class EPAStandardKind(Enum):
    """
    List of EPA standards.

    :cvar value_8082: Polychlorinated Biphenyls (PCBs) by Gas
        Chromatography.
    """
    value_8082 = "8082"


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
    :ivar userID: User ID needed to log in, which can be for an
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
    userID: Optional[str] = field(
        default=None,
        metadata={
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

    :cvar carbonDioxide: Carbon diaoxide.
    :cvar carbonDisulfide: Carbon disulfide.
    :cvar chlorine: Clorine.
    :cvar hydrogenSulfide: Hydrogen sulfide.
    :cvar nitrogenOxide: Nitrogen oxide.
    :cvar sulfurDioxide: Sulfer dioxide.
    """
    carbonDioxide = "carbonDioxide"
    carbonDisulfide = "carbonDisulfide"
    chlorine = "chlorine"
    hydrogenSulfide = "hydrogenSulfide"
    nitrogenOxide = "nitrogenOxide"
    sulfurDioxide = "sulfurDioxide"


class EmissionValueSource(Enum):
    """
    The source of the emission value.

    :cvar calculated: Calculated.
    :cvar measured: Measured.
    """
    calculated = "calculated"
    measured = "measured"


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
    durationIndefinite: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceControl: Optional["EndDeviceControl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    connectDisconnect: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    demandResponse: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    electricMetering: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gasMetering: Optional[bool] = field(
        default=None,
        metadata={
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
    onRequestRead: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    outageHistory: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pressureCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pricingInfo: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pulseOutput: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    relaysProgramming: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reverseFlow: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    superCompressibilityCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    temperatureCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    textMessage: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    waterMetering: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class EndDeviceFunctionKind(Enum):
    """
    Kind of end device function.

    :cvar autonomousDst: Autonomous application of daylight saving time
        (DST).
    :cvar demandResponse: Demand response functions.
    :cvar electricMetering: Electricity metering.
    :cvar gasMetering: Gas metering.
    :cvar metrology: Presentation of metered values to a user or another
        system (always a function of a meter, but might not be supported
        by a load control unit).
    :cvar onRequestRead: On-request reads.
    :cvar outageHistory: Reporting historical power interruption data.
    :cvar relaysProgramming: Support for one or more relays that may be
        programmable in the meter (and tied to TOU, time pulse, load
        control or other functions).
    :cvar reverseFlow: Detection and monitoring of reverse flow.
    :cvar waterMetering: Water metering.
    """
    autonomousDst = "autonomousDst"
    demandResponse = "demandResponse"
    electricMetering = "electricMetering"
    gasMetering = "gasMetering"
    metrology = "metrology"
    onRequestRead = "onRequestRead"
    outageHistory = "outageHistory"
    relaysProgramming = "relaysProgramming"
    reverseFlow = "reverseFlow"
    waterMetering = "waterMetering"


@dataclass
class ExtensionItem:
    extName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    extType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    extValue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class FScale(Enum):
    """Fujita scale (referred to as EF-scale starting in 2007) for tornado
    damage.

    A set of wind estimates (not measurements) based on damage. It uses three-second gusts estimated at the point of damage based on a judgment of 8 levels of damage to 28 indicators. These estimates vary with height and exposure.
    Note: The 3 second gust is not the same wind as in standard surface observations.
    Enumerations based on NOAA conventions.

    :cvar five: Over 200 mph 3-second gust.
    :cvar four: 166-200 mph 3-second gust.
    :cvar minusNine: Unknown.
    :cvar one: 86-110 mph 3-second gust.
    :cvar three: 136-165 mph 3-second gust.
    :cvar two: 111-135 mph 3-second gust.
    :cvar zero: 65-85 mph 3-second gust.
    """
    five = "five"
    four = "four"
    minusNine = "minusNine"
    one = "one"
    three = "three"
    two = "two"
    zero = "zero"


class FacilityKind(Enum):
    """
    Types of facilities at which an asset can be deployed.
    """
    distributionPoleTop = "distributionPoleTop"
    substationDistribution = "substationDistribution"
    substationFossilPlant = "substationFossilPlant"
    substationHydroPlant = "substationHydroPlant"
    substationNuclearPlant = "substationNuclearPlant"
    substationSubTransmission = "substationSubTransmission"
    substationTransmission = "substationTransmission"


class FailureIsolationMethodKind(Enum):
    """
    How the failure has been isolated.
    """
    breakerOperation = "breakerOperation"
    burnedInTheClear = "burnedInTheClear"
    fuse = "fuse"
    manuallyIsolated = "manuallyIsolated"
    other = "other"


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rLineToLine: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xGround: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xLineToLine: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :cvar leading: Typically used to describe that a power factor is
        leading the reference value. Note: Leading power factors
        typically indicate capacitive loading.
    :cvar net: |Forward| - |Reverse|, See 61968-2. Note: In some
        systems, the value passed as a ï¿½netï¿½ value could become
        negative. In other systems the value passed as a ï¿½netï¿½ value
        is always a positive number, and rolls-over and rolls-under as
        needed.
    :cvar none: Not Applicable (N/A)
    :cvar q1minusQ4: Q1 minus Q4
    :cvar q1plusQ2: Reactive positive quadrants. (The term ï¿½laggingï¿½
        is preferred.)
    :cvar q1plusQ3: Quadrants 1 and 3
    :cvar q1plusQ4: Quadrants 1 and 4 usually represent forward active
        energy
    :cvar q2minusQ3: Q2 minus Q3
    :cvar q2plusQ3: Quadrants 2 and 3 usually represent reverse active
        energy
    :cvar q2plusQ4: Quadrants 2 and 4
    :cvar q3minusQ2: Q3 minus Q2
    :cvar q3plusQ4: Reactive negative quadrants. (The term ï¿½leadingï¿½
        is preferred.)
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
        the label ï¿½reverseï¿½ that it represents negative flow.
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
        for ï¿½Totalï¿½ and ï¿½Total by phaseï¿½ collapse to the same
        expression. For communication purposes however, the ï¿½Totalï¿½
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


class FuelType(Enum):
    """
    Type of fuel.

    :cvar coal: Generic coal, not including lignite type.
    :cvar gas: Natural gas.
    :cvar hardCoal: Hard coal
    :cvar lignite: The fuel is lignite coal.  Note that this is a
        special type of coal, so the other enum of coal is reserved for
        hard coal types or if the exact type of coal is not known.
    :cvar oil: Oil.
    :cvar oilShale: Oil Shale
    """
    coal = "coal"
    gas = "gas"
    hardCoal = "hardCoal"
    lignite = "lignite"
    oil = "oil"
    oilShale = "oilShale"


class GeosphericAnalogKind(Enum):
    """
    Kinds of analogs measuring a geospheric condition.

    :cvar lightningDensity: Flash rate in
        strikes/hour/km&lt;sup&gt;2&lt;/sup&gt;.
    :cvar seismicEastWest:
    :cvar seismicNorthSouth:
    :cvar seismicVertical:
    :cvar snowPackDepth:
    :cvar temperature:
    """
    lightningDensity = "lightningDensity"
    seismicEastWest = "seismicEastWest"
    seismicNorthSouth = "seismicNorthSouth"
    seismicVertical = "seismicVertical"
    snowPackDepth = "snowPackDepth"
    temperature = "temperature"


class HouseCooling(Enum):
    electric = "electric"
    heatPump = "heatPump"
    none = "none"


class HouseHeating(Enum):
    gas = "gas"
    heatPump = "heatPump"
    none = "none"
    resistance = "resistance"


class HydroEnergyConversionKind(Enum):
    """
    Specifies the capability of the hydro generating unit to convert energy as
    a generator or pump.

    :cvar generator: Able to generate power, but not able to pump water
        for energy storage.
    :cvar pumpAndGenerator: Able to both generate power and pump water
        for energy storage.
    """
    generator = "generator"
    pumpAndGenerator = "pumpAndGenerator"


class HydroPlantStorageKind(Enum):
    """
    The type of hydro power plant.

    :cvar pumpedStorage: Pumped storage.
    :cvar runOfRiver: Run of river.
    :cvar storage: Storage.
    """
    pumpedStorage = "pumpedStorage"
    runOfRiver = "runOfRiver"
    storage = "storage"


class HydrosphericAnalogKind(Enum):
    """
    Kinds of analogs measuring a hydrospheric condition.
    """
    floodLevel = "floodLevel"
    stormSurgeHeight = "stormSurgeHeight"
    surfaceTemperature = "surfaceTemperature"
    waterTemperature = "waterTemperature"
    waveHeight = "waveHeight"


class IEEE1547AbnormalPerfomanceCategory(Enum):
    CategoryI = "CategoryI"
    CategoryII = "CategoryII"
    CategoryIII = "CategoryIII"


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OF1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OF2frequency: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OF2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OV1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OV1voltage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OV2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OV2voltage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UF1frequency: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UF1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UF2frequency: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UF2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UV1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UV1voltage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UV2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UV2voltage: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerElectronicsConnections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RotatingMachines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class InUseDate:
    """Dates associated with asset 'in use' status.

    May have multiple in use dates for this device and a compound type
    allows a query to return multiple dates.

    :ivar inUseDate: Date asset was most recently put in use.
    :ivar notReadyForUseDate: Date of most recent asset transition to
        not ready for use state.
    :ivar readyForUseDate: Date of most recent asset transition to ready
        for use state.
    """
    inUseDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    notReadyForUseDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    readyForUseDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class IntensityCodeKind(Enum):
    """
    Kinds of weather condition intensity.
    """
    heavy = "heavy"
    light = "light"
    veryHeavy = "veryHeavy"
    veryLight = "veryLight"


class InterruptingMediumKind(Enum):
    airBlast = "airBlast"
    airMagnetic = "airMagnetic"
    bulkOil = "bulkOil"
    gasSinglePressure = "gasSinglePressure"
    gasTwoPressure = "gasTwoPressure"
    minimumOil = "minimumOil"
    vacuum = "vacuum"


@dataclass
class IrregularTimePoint:
    """
    TimePoints for a schedule where the time between the points varies.

    :ivar time: The time is relative to the schedule starting time.
    :ivar value1: The first value at the time. The meaning of the value
        is defined by the derived type of the associated schedule.
    :ivar value2: The second value at the time. The meaning of the value
        is defined by the derived type of the associated schedule.
    :ivar IntervalSchedule: An IrregularTimePoint belongs to an
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
    IntervalSchedule: Optional["IrregularIntervalSchedule"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


class LaborelecStandardEditionKind(Enum):
    """
    List of editions for Laborelec standards.
    """
    none = "none"
    unknown = "unknown"


class LaborelecStandardKind(Enum):
    """
    List of Laborelec standards.

    :cvar methanol: Laborelec test for methanol.
    """
    methanol = "methanol"


@dataclass
class LifecycleDate:
    """Dates for asset lifecycle state changes.

    May have multiple lifecycle dates for this device and a compound
    type allows a query to return multiple dates.

    :ivar installationDate: Date current installation was completed,
        which may not be the same as the in-service date. Asset may have
        been installed at other locations previously. Ignored if asset
        is (1) not currently installed (e.g., stored in a depot) or (2)
        not intended to be installed (e.g., vehicle, tool).
    :ivar manufacturedDate: Date the asset was manufactured.
    :ivar purchaseDate: Date the asset was purchased. Note that even
        though an asset may have been purchased, it may not have been
        received into inventory at the time of purchase.
    :ivar receivedDate: Date the asset was received and first placed
        into inventory.
    :ivar removalDate: Date when the asset was last removed from
        service. Ignored if (1) not intended to be in service, or (2)
        currently in service.
    :ivar retiredDate: Date the asset is permanently retired from
        service and may be scheduled for disposal. Ignored if asset is
        (1) currently in service, or (2) permanently removed from
        service.
    """
    installationDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    manufacturedDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    purchaseDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    receivedDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    removalDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    retiredDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class LocationKind(Enum):
    """
    :cvar center: The center of a phenomenon. Will typically be used
        with a Location with a single PositionPoint instance.
    :cvar extent: The area or line of a phenomenon, not the center. Will
        typically be used with a Location with multiple PositionPoint
        instances.
    :cvar primary: Primary area to which an environmental alert applies.
    :cvar secondary: Secondary area to which an environmental alert
        applies.
    """
    center = "center"
    extent = "extent"
    primary = "primary"
    secondary = "secondary"


class MacroPeriodKind(Enum):
    """
    Kind of macro period for calculations on read / measured values.

    :cvar billingPeriod: Captured during the billing period starting at
        midnight of the first day of the billing period (as defined by
        the billing cycle day). If during the current billing period, it
        specifies a period from the start of the current billing period
        until "now".
    :cvar daily: Daily period starting at midnight. If for the current
        day, this specifies the time from midnight to "now".
    :cvar monthly: Monthly period starting at midnight on the first day
        of the month. If within the current month, this specifies the
        period from the start of the month until "now."
    :cvar none: Not applicable.
    :cvar seasonal: A season of time spanning multiple months. E.g.
        "Summer," "Spring," "Fall," and "Winter" based cycle. If within
        the current season, it specifies the period from the start of
        the current season until "now."
    :cvar specifiedPeriod: For the period defined by the start and end
        of the TimePeriod element in the message.
    :cvar weekly: Weekly period starting at midnight on the first day of
        the week and ending the instant before midnight the last day of
        the week. If within the current week, it specifies the period
        from the start of the week until "now."
    """
    billingPeriod = "billingPeriod"
    daily = "daily"
    monthly = "monthly"
    none = "none"
    seasonal = "seasonal"
    specifiedPeriod = "specifiedPeriod"
    weekly = "weekly"


class MeasurementKind(Enum):
    """
    Kind of read / measured value.

    :cvar alarm:
    :cvar apTitle:
    :cvar apparentPowerFactor:
    :cvar applicationContext:
    :cvar assetNumber:
    :cvar audibleVolume: Sound
    :cvar bandwidth:
    :cvar batteryCarryover:
    :cvar batteryVoltage:
    :cvar billCarryover: Customerï¿½s bill for the (Currency)
    :cvar billLastPeriod: Customerï¿½s bill for the previous billing
        period (Currency)
    :cvar billToDate: Customerï¿½s bill, as known thus far within the
        present billing period (Currency)
    :cvar broadcastAddress:
    :cvar connectionFee: Monthly fee for connection to commodity.
    :cvar currency: funds
    :cvar current:
    :cvar currentAngle:
    :cvar currentImbalance:
    :cvar dataOverflowAlarm:
    :cvar date:
    :cvar demand:
    :cvar demandLimit:
    :cvar demandReset: Usually expressed as a count as part of a billing
        cycle
    :cvar deviceAddressType1:
    :cvar deviceAddressType2:
    :cvar deviceAddressType3:
    :cvar deviceAddressType4:
    :cvar deviceClass:
    :cvar diagnostic:
    :cvar distance:
    :cvar distortionPowerFactor:
    :cvar distortionVoltAmp:
    :cvar electronicSerialNumber:
    :cvar emergencyLimit:
    :cvar encoderTamper:
    :cvar endDeviceID:
    :cvar energization:
    :cvar energizationLoadSide:
    :cvar energy:
    :cvar fan:
    :cvar frequency:
    :cvar frequencyExcursion: Usually expressed as a ï¿½countï¿½
    :cvar fund: Dup with ï¿½currencyï¿½
    :cvar groupAddressType1:
    :cvar groupAddressType2:
    :cvar groupAddressType3:
    :cvar groupAddressType4:
    :cvar ieee1366ASAI:
    :cvar ieee1366ASIDI:
    :cvar ieee1366ASIFI:
    :cvar ieee1366CAIDI:
    :cvar ieee1366CAIFI:
    :cvar ieee1366CEMIn:
    :cvar ieee1366CEMSMIn:
    :cvar ieee1366CTAIDI:
    :cvar ieee1366MAIFI:
    :cvar ieee1366MAIFIe:
    :cvar ieee1366MomentaryInterruption:
    :cvar ieee1366MomentaryInterruptionEvent:
    :cvar ieee1366SAIDI:
    :cvar ieee1366SAIFI:
    :cvar ieee1366SustainedInterruption:
    :cvar interruptionBehaviour:
    :cvar inversionTamper:
    :cvar ipAddress:
    :cvar lineLoss:
    :cvar loadInterrupt:
    :cvar loadShed:
    :cvar loss:
    :cvar macAddress:
    :cvar maintenance:
    :cvar mfgAssignedConfigurationID:
    :cvar mfgAssignedPhysicalSerialNumber:
    :cvar mfgAssignedProductNumber:
    :cvar mfgAssignedUniqueCommunicationAddress:
    :cvar multiCastAddress:
    :cvar negativeSequence:
    :cvar none: Not Applicable
    :cvar oneWayAddress:
    :cvar phasorPowerFactor:
    :cvar phasorReactivePower:
    :cvar physicalTamper:
    :cvar positiveSequence:
    :cvar power:
    :cvar powerFactor:
    :cvar powerLossTamper:
    :cvar powerOutage:
    :cvar powerQuality:
    :cvar powerRestoration:
    :cvar programmed:
    :cvar pushbutton:
    :cvar quantityPower:
    :cvar relayActivation:
    :cvar relayCycle: Usually expressed as a count
    :cvar removalTamper:
    :cvar reprogrammingTamper:
    :cvar reverseRotationTamper:
    :cvar sag: or Voltage Dip
    :cvar signalStrength:
    :cvar signaltoNoiseRatio: Moved here from Attribute #9 UOM
    :cvar swell:
    :cvar switchArmed:
    :cvar switchDisabled:
    :cvar switchPosition:
    :cvar tamper:
    :cvar tapPosition:
    :cvar tariffRate:
    :cvar temperature:
    :cvar totalHarmonicDistortion:
    :cvar transformerLoss:
    :cvar twoWayAddress:
    :cvar unipedeVoltageDip10to15:
    :cvar unipedeVoltageDip15to30:
    :cvar unipedeVoltageDip30to60:
    :cvar unipedeVoltageDip60to90:
    :cvar unipedeVoltageDip90to100:
    :cvar voltage:
    :cvar voltageAngle:
    :cvar voltageExcursion:
    :cvar voltageImbalance:
    :cvar volume: Clarified  from Ed. 1. to indicate fluid volume
    :cvar volumetricFlow:
    :cvar watchdogTimeout:
    :cvar zeroFlowDuration:
    :cvar zeroSequence:
    """
    alarm = "alarm"
    apTitle = "apTitle"
    apparentPowerFactor = "apparentPowerFactor"
    applicationContext = "applicationContext"
    assetNumber = "assetNumber"
    audibleVolume = "audibleVolume"
    bandwidth = "bandwidth"
    batteryCarryover = "batteryCarryover"
    batteryVoltage = "batteryVoltage"
    billCarryover = "billCarryover"
    billLastPeriod = "billLastPeriod"
    billToDate = "billToDate"
    broadcastAddress = "broadcastAddress"
    connectionFee = "connectionFee"
    currency = "currency"
    current = "current"
    currentAngle = "currentAngle"
    currentImbalance = "currentImbalance"
    dataOverflowAlarm = "dataOverflowAlarm"
    date = "date"
    demand = "demand"
    demandLimit = "demandLimit"
    demandReset = "demandReset"
    deviceAddressType1 = "deviceAddressType1"
    deviceAddressType2 = "deviceAddressType2"
    deviceAddressType3 = "deviceAddressType3"
    deviceAddressType4 = "deviceAddressType4"
    deviceClass = "deviceClass"
    diagnostic = "diagnostic"
    distance = "distance"
    distortionPowerFactor = "distortionPowerFactor"
    distortionVoltAmp = "distortionVoltAmp"
    electronicSerialNumber = "electronicSerialNumber"
    emergencyLimit = "emergencyLimit"
    encoderTamper = "encoderTamper"
    endDeviceID = "endDeviceID"
    energization = "energization"
    energizationLoadSide = "energizationLoadSide"
    energy = "energy"
    fan = "fan"
    frequency = "frequency"
    frequencyExcursion = "frequencyExcursion"
    fund = "fund"
    groupAddressType1 = "groupAddressType1"
    groupAddressType2 = "groupAddressType2"
    groupAddressType3 = "groupAddressType3"
    groupAddressType4 = "groupAddressType4"
    ieee1366ASAI = "ieee1366ASAI"
    ieee1366ASIDI = "ieee1366ASIDI"
    ieee1366ASIFI = "ieee1366ASIFI"
    ieee1366CAIDI = "ieee1366CAIDI"
    ieee1366CAIFI = "ieee1366CAIFI"
    ieee1366CEMIn = "ieee1366CEMIn"
    ieee1366CEMSMIn = "ieee1366CEMSMIn"
    ieee1366CTAIDI = "ieee1366CTAIDI"
    ieee1366MAIFI = "ieee1366MAIFI"
    ieee1366MAIFIe = "ieee1366MAIFIe"
    ieee1366MomentaryInterruption = "ieee1366MomentaryInterruption"
    ieee1366MomentaryInterruptionEvent = "ieee1366MomentaryInterruptionEvent"
    ieee1366SAIDI = "ieee1366SAIDI"
    ieee1366SAIFI = "ieee1366SAIFI"
    ieee1366SustainedInterruption = "ieee1366SustainedInterruption"
    interruptionBehaviour = "interruptionBehaviour"
    inversionTamper = "inversionTamper"
    ipAddress = "ipAddress"
    lineLoss = "lineLoss"
    loadInterrupt = "loadInterrupt"
    loadShed = "loadShed"
    loss = "loss"
    macAddress = "macAddress"
    maintenance = "maintenance"
    mfgAssignedConfigurationID = "mfgAssignedConfigurationID"
    mfgAssignedPhysicalSerialNumber = "mfgAssignedPhysicalSerialNumber"
    mfgAssignedProductNumber = "mfgAssignedProductNumber"
    mfgAssignedUniqueCommunicationAddress = "mfgAssignedUniqueCommunicationAddress"
    multiCastAddress = "multiCastAddress"
    negativeSequence = "negativeSequence"
    none = "none"
    oneWayAddress = "oneWayAddress"
    phasorPowerFactor = "phasorPowerFactor"
    phasorReactivePower = "phasorReactivePower"
    physicalTamper = "physicalTamper"
    positiveSequence = "positiveSequence"
    power = "power"
    powerFactor = "powerFactor"
    powerLossTamper = "powerLossTamper"
    powerOutage = "powerOutage"
    powerQuality = "powerQuality"
    powerRestoration = "powerRestoration"
    programmed = "programmed"
    pushbutton = "pushbutton"
    quantityPower = "quantityPower"
    relayActivation = "relayActivation"
    relayCycle = "relayCycle"
    removalTamper = "removalTamper"
    reprogrammingTamper = "reprogrammingTamper"
    reverseRotationTamper = "reverseRotationTamper"
    sag = "sag"
    signalStrength = "signalStrength"
    signaltoNoiseRatio = "signaltoNoiseRatio"
    swell = "swell"
    switchArmed = "switchArmed"
    switchDisabled = "switchDisabled"
    switchPosition = "switchPosition"
    tamper = "tamper"
    tapPosition = "tapPosition"
    tariffRate = "tariffRate"
    temperature = "temperature"
    totalHarmonicDistortion = "totalHarmonicDistortion"
    transformerLoss = "transformerLoss"
    twoWayAddress = "twoWayAddress"
    unipedeVoltageDip10to15 = "unipedeVoltageDip10to15"
    unipedeVoltageDip15to30 = "unipedeVoltageDip15to30"
    unipedeVoltageDip30to60 = "unipedeVoltageDip30to60"
    unipedeVoltageDip60to90 = "unipedeVoltageDip60to90"
    unipedeVoltageDip90to100 = "unipedeVoltageDip90to100"
    voltage = "voltage"
    voltageAngle = "voltageAngle"
    voltageExcursion = "voltageExcursion"
    voltageImbalance = "voltageImbalance"
    volume = "volume"
    volumetricFlow = "volumetricFlow"
    watchdogTimeout = "watchdogTimeout"
    zeroFlowDuration = "zeroFlowDuration"
    zeroSequence = "zeroSequence"


class MeasuringPeriodKind(Enum):
    """
    Kind of period for reading / measuring values.

    :cvar fifteenMinute: 15-minute
    :cvar fiveMinute: 5-minute
    :cvar fixedBlock10Min: 10-minute Fixed Block
    :cvar fixedBlock15Min: 15-minute Fixed Block
    :cvar fixedBlock1Min: 1-minute Fixed Block
    :cvar fixedBlock20Min: 20-minute Fixed Block
    :cvar fixedBlock30Min: 30-minute Fixed Block
    :cvar fixedBlock5Min: 5-minute Fixed Block
    :cvar fixedBlock60Min: 60-minute Fixed Block
    :cvar none: Not applicable.
    :cvar oneMinute: 1-minute
    :cvar present: Within the present period of time
    :cvar previous: Shifted within the previous monthly cycle and data
        set
    :cvar rollingBlock10MinIntvl1MinSubIntvl: 10-minute Rolling Block
        with 1-minute sub-intervals
    :cvar rollingBlock10MinIntvl2MinSubIntvl: 10-minute Rolling Block
        with 2-minute sub-intervals
    :cvar rollingBlock10MinIntvl5MinSubIntvl: 10-minute Rolling Block
        with 5-minute sub-intervals
    :cvar rollingBlock15MinIntvl1MinSubIntvl: 15-minute Rolling Block
        with 1-minute sub-intervals
    :cvar rollingBlock15MinIntvl3MinSubIntvl: 15-minute Rolling Block
        with 3-minute sub-intervals
    :cvar rollingBlock15MinIntvl5MinSubIntvl: 15-minute Rolling Block
        with 5-minute sub-intervals
    :cvar rollingBlock30MinIntvl10MinSubIntvl: 30-minute Rolling Block
        with 10-minute sub-intervals
    :cvar rollingBlock30MinIntvl15MinSubIntvl: 30-minute Rolling Block
        with 15-minute sub-intervals
    :cvar rollingBlock30MinIntvl2MinSubIntvl: 30-minute Rolling Block
        with 2-minute sub-intervals
    :cvar rollingBlock30MinIntvl3MinSubIntvl: 30-minute Rolling Block
        with 3-minute sub-intervals
    :cvar rollingBlock30MinIntvl5MinSubIntvl: 30-minute Rolling Block
        with 5-minute sub-intervals.
    :cvar rollingBlock30MinIntvl6MinSubIntvl: 30-minute Rolling Block
        with 6-minute sub-intervals
    :cvar rollingBlock5MinIntvl1MinSubIntvl: 5-minute Rolling Block with
        1-minute sub-intervals
    :cvar rollingBlock60MinIntvl10MinSubIntvl: 60-minute Rolling Block
        with 10-minute sub-intervals
    :cvar rollingBlock60MinIntvl12MinSubIntvl: 60-minute Rolling Block
        with 12-minute sub-intervals
    :cvar rollingBlock60MinIntvl15MinSubIntvl: 60-minute Rolling Block
        with 15-minute sub-intervals
    :cvar rollingBlock60MinIntvl20MinSubIntvl: 60-minute Rolling Block
        with 20-minute sub-intervals
    :cvar rollingBlock60MinIntvl30MinSubIntvl: 60-minute Rolling Block
        with 30-minute sub-intervals
    :cvar rollingBlock60MinIntvl4MinSubIntvl: 60-minute Rolling Block
        with 4-minute sub-intervals
    :cvar rollingBlock60MinIntvl5MinSubIntvl: 60-minute Rolling Block
        with 5-minute sub-intervals
    :cvar rollingBlock60MinIntvl6MinSubIntvl: 60-minute Rolling Block
        with 6-minute sub-intervals
    :cvar sixtyMinute: 60-minute
    :cvar tenMinute: 10-minute
    :cvar thirtyMinute: 30-minute
    :cvar threeMinute: 3-minute
    :cvar twentyMinute: 20-minute interval
    :cvar twentyfourHour: 24-hour
    :cvar twoMinute: 2-minute
    """
    fifteenMinute = "fifteenMinute"
    fiveMinute = "fiveMinute"
    fixedBlock10Min = "fixedBlock10Min"
    fixedBlock15Min = "fixedBlock15Min"
    fixedBlock1Min = "fixedBlock1Min"
    fixedBlock20Min = "fixedBlock20Min"
    fixedBlock30Min = "fixedBlock30Min"
    fixedBlock5Min = "fixedBlock5Min"
    fixedBlock60Min = "fixedBlock60Min"
    none = "none"
    oneMinute = "oneMinute"
    present = "present"
    previous = "previous"
    rollingBlock10MinIntvl1MinSubIntvl = "rollingBlock10MinIntvl1MinSubIntvl"
    rollingBlock10MinIntvl2MinSubIntvl = "rollingBlock10MinIntvl2MinSubIntvl"
    rollingBlock10MinIntvl5MinSubIntvl = "rollingBlock10MinIntvl5MinSubIntvl"
    rollingBlock15MinIntvl1MinSubIntvl = "rollingBlock15MinIntvl1MinSubIntvl"
    rollingBlock15MinIntvl3MinSubIntvl = "rollingBlock15MinIntvl3MinSubIntvl"
    rollingBlock15MinIntvl5MinSubIntvl = "rollingBlock15MinIntvl5MinSubIntvl"
    rollingBlock30MinIntvl10MinSubIntvl = "rollingBlock30MinIntvl10MinSubIntvl"
    rollingBlock30MinIntvl15MinSubIntvl = "rollingBlock30MinIntvl15MinSubIntvl"
    rollingBlock30MinIntvl2MinSubIntvl = "rollingBlock30MinIntvl2MinSubIntvl"
    rollingBlock30MinIntvl3MinSubIntvl = "rollingBlock30MinIntvl3MinSubIntvl"
    rollingBlock30MinIntvl5MinSubIntvl = "rollingBlock30MinIntvl5MinSubIntvl"
    rollingBlock30MinIntvl6MinSubIntvl = "rollingBlock30MinIntvl6MinSubIntvl"
    rollingBlock5MinIntvl1MinSubIntvl = "rollingBlock5MinIntvl1MinSubIntvl"
    rollingBlock60MinIntvl10MinSubIntvl = "rollingBlock60MinIntvl10MinSubIntvl"
    rollingBlock60MinIntvl12MinSubIntvl = "rollingBlock60MinIntvl12MinSubIntvl"
    rollingBlock60MinIntvl15MinSubIntvl = "rollingBlock60MinIntvl15MinSubIntvl"
    rollingBlock60MinIntvl20MinSubIntvl = "rollingBlock60MinIntvl20MinSubIntvl"
    rollingBlock60MinIntvl30MinSubIntvl = "rollingBlock60MinIntvl30MinSubIntvl"
    rollingBlock60MinIntvl4MinSubIntvl = "rollingBlock60MinIntvl4MinSubIntvl"
    rollingBlock60MinIntvl5MinSubIntvl = "rollingBlock60MinIntvl5MinSubIntvl"
    rollingBlock60MinIntvl6MinSubIntvl = "rollingBlock60MinIntvl6MinSubIntvl"
    sixtyMinute = "sixtyMinute"
    tenMinute = "tenMinute"
    thirtyMinute = "thirtyMinute"
    threeMinute = "threeMinute"
    twentyMinute = "twentyMinute"
    twentyfourHour = "twentyfourHour"
    twoMinute = "twoMinute"


class MediumKind(Enum):
    """
    Kind of medium.
    """
    SF6 = "SF6"
    SF6CF4 = "SF6CF4"
    SF6N2 = "SF6N2"
    air = "air"
    gas = "gas"
    liquid = "liquid"
    mineralOil = "mineralOil"
    solid = "solid"


class MeterMultiplierKind(Enum):
    """
    Kind of meter multiplier.

    :cvar ctRatio: Current transformer ratio used to convert associated
        quantities to real measurements.
    :cvar kE: Test constant.
    :cvar kH: Meter kh (watthour) constant. The number of watthours that
        must be applied to the meter to cause one disk revolution for an
        electromechanical meter or the number of watthours represented
        by one increment pulse for an electronic meter.
    :cvar kR: Register multiplier. The number to multiply the register
        reading by in order to get kWh.
    :cvar ptRatio: Potential transformer ratio used to convert
        associated quantities to real measurements.
    :cvar transformerRatio: Product of the CT ratio and PT ratio.
    """
    ctRatio = "ctRatio"
    kE = "kE"
    kH = "kH"
    kR = "kR"
    ptRatio = "ptRatio"
    transformerRatio = "transformerRatio"


@dataclass
class MeterWorkTask:
    """
    Work task involving meters.

    :ivar Meter: Meter on which this non-replacement work task is
        performed.
    :ivar OldMeter: Old meter replaced by this work task.
    :ivar UsagePoint: Usage point to which this meter service work task
        applies.
    """
    Meter: Optional["Meter"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OldMeter: Optional["Meter"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoint: Optional["UsagePoint"] = field(
        default=None,
        metadata={
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
    :ivar NameTypes: All name types managed by this authority.
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
    NameTypes: List["NameType"] = field(
        default_factory=list,
        metadata={
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
    :ivar sectionNumber: The number of the section.
    :ivar NonlinearShuntCompensatorPhase:
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
    sectionNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NonlinearShuntCompensatorPhase: Optional["NonlinearShuntCompensatorPhase"] = field(
        default=None,
        metadata={
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
    :ivar sectionNumber: The number of the section.
    :ivar NonlinearShuntCompensator:
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
    sectionNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NonlinearShuntCompensator: Optional["NonlinearShuntCompensator"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


class NotificationTriggerKind(Enum):
    """
    Kind of trigger to notify customer.

    :cvar etrChange: Notify customer if estimated restoration time
        changes.
    :cvar informDispatched: Notify customer that a crew has been
        dispatched to investigate the problem.
    :cvar initialEtr: Notify customer for the first time that estimated
        restoration time is available.
    :cvar powerOut: Notify customer of planned outage.
    :cvar powerRestored: Notify customer when power has been restored.
    """
    etrChange = "etrChange"
    informDispatched = "informDispatched"
    initialEtr = "initialEtr"
    powerOut = "powerOut"
    powerRestored = "powerRestored"


class OilSampleLocation(Enum):
    oilDrainageDevice = "oilDrainageDevice"
    oilSampleValve = "oilSampleValve"
    other = "other"


class OilTemperatureSource(Enum):
    infraredGun = "infraredGun"
    other = "other"
    topOilTemperatureGauge = "topOilTemperatureGauge"


class OperatingMechanismKind(Enum):
    capacitorTrip = "capacitorTrip"
    hydraulic = "hydraulic"
    pneudraulic = "pneudraulic"
    pneumatic = "pneumatic"
    solenoid = "solenoid"
    spring = "spring"
    springHandCrank = "springHandCrank"
    springHydraulic = "springHydraulic"
    springMotor = "springMotor"


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


class PNNLTroubleCallKind(Enum):
    lineDown = "lineDown"
    powerOn = "powerOn"
    powerOut = "powerOut"


@dataclass
class PanPricingDetail:
    """
    Detail for a single price command/action.

    :ivar alternateCostDelivered: Alternative measure of the cost of the
        energy consumed. An example might be the emissions of CO2 for
        each kWh of electricity consumed providing a measure of the
        environmental cost.
    :ivar alternateCostUnit: Cost unit for the alternate cost delivered
        field. One example is kg of CO2 per unit of measure.
    :ivar currentTimeDate: Current time as determined by a PAN device.
    :ivar generationPrice: Price of the commodity measured in base unit
        of currency per 'unitOfMeasure'.
    :ivar generationPriceRatio: Ratio of 'generationPrice' to the
        "normal" price chosen by the commodity provider.
    :ivar price: Price of the commodity measured in base unit of
        currency per 'unitOfMeasure'.
    :ivar priceRatio: Ratio of 'price' to the "normal" price chosen by
        the commodity provider.
    :ivar priceTier: Pricing tier as chosen by the commodity provider.
    :ivar priceTierCount: Maximum number of price tiers available.
    :ivar priceTierLabel: Label for price tier.
    :ivar rateLabel: Label of the current billing rate specified by
        commodity provider.
    :ivar registerTier: Register tier accumulating usage information.
    :ivar unitOfMeasure: Defines commodity as well as its base unit of
        measure.
    :ivar PanPricing: PAN pricing command/action issuing this price
        detail.
    """
    alternateCostDelivered: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    alternateCostUnit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    currentTimeDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    generationPrice: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    generationPriceRatio: Optional[float] = field(
        default=None,
        metadata={
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
    priceRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    priceTier: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    priceTierCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    priceTierLabel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rateLabel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    registerTier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unitOfMeasure: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PanPricing: Optional["PanPricing"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class PetersenCoilModeKind(Enum):
    """
    The mode of operation for a Petersen coil.

    :cvar automaticPositioning: Automatic positioning.
    :cvar fixed: Fixed position.
    :cvar manual: Manual positioning.
    """
    automaticPositioning = "automaticPositioning"
    fixed = "fixed"
    manual = "manual"


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


@dataclass
class PhaseImpedanceData(IdentifiedObject):
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
    :ivar PhaseImpedance: Conductor phase impedance to which this data
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
    PhaseImpedance: Optional["PerLengthPhaseImpedance"] = field(
        default=None,
        metadata={
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
    :cvar Yn: Wye, with neutral brought out for grounding.
    """
    D = "D"
    G = "G"
    I = "I"
    Y = "Y"
    Yn = "Yn"


@dataclass
class PositionPoint:
    """Set of spatial coordinates that determine a point, defined in the
    coordinate system specified in 'Location.CoordinateSystem'.

    Use a single position point instance to desribe a point-oriented location. Use a sequence of position points to describe a line-oriented object (physical location of non-point oriented objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case, have first and last position point with the same values).

    :ivar groupNumber: Zero-relative sequence number of this group
        within a series of points; used when there is a need to express
        disjoint groups of points that are considered to be part of a
        single location.
    :ivar sequenceNumber: Zero-relative sequence number of this point
        within a series of points.
    :ivar xPosition: X axis position.
    :ivar yPosition: Y axis position.
    :ivar zPosition: (if applicable) Z axis position.
    :ivar Location: Location described by this position point.
    """
    groupNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xPosition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    yPosition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    zPosition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Location: Optional["Location"] = field(
        default=None,
        metadata={
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

    :cvar diagnosis: Diagnosis procedure.
    :cvar inspection: Inspection procedure.
    :cvar maintenance: Maintenance procedure.
    :cvar other: Other procedure.
    :cvar test: Test procedure.
    """
    diagnosis = "diagnosis"
    inspection = "inspection"
    maintenance = "maintenance"
    other = "other"
    test = "test"


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

    :cvar billing: Reading(s) taken or to be taken in response to a
        billing-related inquiry by a customer or other party. A variant
        of 'inquiry'.
    :cvar demandReset: Reading(s) taken or to be taken in conjunction
        with the resetting of one or more demand registers in a meter.
    :cvar inquiry: Reading(s) taken or to be taken in response to an
        inquiry by a customer or other party.
    :cvar installation: Reading(s) taken or to be taken in conjunction
        with installation of a meter.
    :cvar loadManagement: Reading(s) taken or to be taken to support
        management of loads on distribution networks or devices.
    :cvar loadResearch: Reading(s) taken or to be taken to support
        research and analysis of loads on distribution networks or
        devices.
    :cvar moveIn: Reading(s) taken or to be taken in conjunction with a
        customer move-in event.
    :cvar moveOut: Reading(s) taken or to be taken in conjunction with a
        customer move-out event.
    :cvar other: Reading(s) taken or to be taken for some other reason
        or purpose.
    :cvar removal: Reading(s) taken or to be taken in conjunction with
        removal of a meter.
    :cvar serviceConnect: Reading(s) taken or to be taken in conjunction
        with a connection or re-connection of service.
    :cvar serviceDisconnect: Reading(s) taken or to be taken in
        conjunction with a disconnection of service.
    """
    billing = "billing"
    demandReset = "demandReset"
    inquiry = "inquiry"
    installation = "installation"
    loadManagement = "loadManagement"
    loadResearch = "loadResearch"
    moveIn = "moveIn"
    moveOut = "moveOut"
    other = "other"
    removal = "removal"
    serviceConnect = "serviceConnect"
    serviceDisconnect = "serviceDisconnect"


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
    IntervalSchedule: Optional["RegularIntervalSchedule"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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


class RelativeDisplacementKind(Enum):
    """
    The types of relative displacement.
    """
    centreEarth = "centreEarth"
    ground = "ground"
    seaLevel = "seaLevel"


class ReportingMethodKind(Enum):
    """
    Method by which information is gathered from station.

    :cvar automated: Station automatically reports.
    :cvar manual: Station must be physically visited to gather
        observations.
    :cvar queried: Station must be queried to obtain observations.
    """
    automated = "automated"
    manual = "manual"
    queried = "queried"


class RevenueKind(Enum):
    """
    Accounting classification of the type of revenue collected for the customer
    agreement, typically used to break down accounts for revenue accounting.

    :cvar commercial: Commercial revenue.
    :cvar industrial: Industrial revenue.
    :cvar irrigation: Irrigation revenue.
    :cvar nonResidential: Non-residential revenue.
    :cvar other: Other revenue kind.
    :cvar residential: Residential revenue.
    :cvar streetLight: Streetlight revenue.
    """
    commercial = "commercial"
    industrial = "industrial"
    irrigation = "irrigation"
    nonResidential = "nonResidential"
    other = "other"
    residential = "residential"
    streetLight = "streetLight"


class RiskScoreKind(Enum):
    customerRisk = "customerRisk"
    financialRisk = "financialRisk"
    safetyRisk = "safetyRisk"


class SVCControlMode(Enum):
    """
    Static VAr Compensator control mode.
    """
    reactivePower = "reactivePower"
    voltage = "voltage"


class SampleContainerType(Enum):
    glassCan = "glassCan"
    metalCan = "metalCan"
    syringe = "syringe"


class ScaleKind(Enum):
    exponential = "exponential"
    linear = "linear"


class SealConditionKind(Enum):
    """
    Kind of seal condition.

    :cvar broken: Seal is broken.
    :cvar locked: Seal is locked.
    :cvar missing: Seal is missing.
    :cvar open: Seal is open.
    :cvar other: Other kind of seal condition.
    """
    broken = "broken"
    locked = "locked"
    missing = "missing"
    open = "open"
    other = "other"


class SealKind(Enum):
    """
    Kind of seal.

    :cvar lead: Lead seal.
    :cvar lock: Lock seal.
    :cvar other: Other kind of seal.
    :cvar steel: Steel seal.
    """
    lead = "lead"
    lock = "lock"
    other = "other"
    steel = "steel"


class ServiceKind(Enum):
    """
    Kind of service.

    :cvar air: Air service.
    :cvar electricity: Electricity service.
    :cvar gas: Gas service.
    :cvar heat: Heat service.
    :cvar heatingFluid: Heating fluid service.
    :cvar internet: Internet service.
    :cvar naturalGas: Natural gas service.
    :cvar other: Other kind of service.
    :cvar propane: Propane service.
    :cvar rates: Rates (e.g. tax, charge, toll, duty, tariff, etc.)
        service.
    :cvar refuse: Refuse (waster) service.
    :cvar sewerage: Sewerage service.
    :cvar steam: Steam service.
    :cvar time: Time service.
    :cvar tvLicence: TV license service.
    :cvar water: Water service.
    """
    air = "air"
    electricity = "electricity"
    gas = "gas"
    heat = "heat"
    heatingFluid = "heatingFluid"
    internet = "internet"
    naturalGas = "naturalGas"
    other = "other"
    propane = "propane"
    rates = "rates"
    refuse = "refuse"
    sewerage = "sewerage"
    steam = "steam"
    time = "time"
    tvLicence = "tvLicence"
    water = "water"


@dataclass
class ServiceLocation:
    """
    A real estate location, commonly referred to as premises.

    :ivar accessMethod: Method for the service person to access this
        service location. For example, a description of where to obtain
        a key if the facility is unmanned and secured.
    :ivar needsInspection: True if inspection is needed of facilities at
        this service location. This could be requested by a customer,
        due to suspected tampering, environmental concerns (e.g., a fire
        in the vicinity), or to correct incompatible data.
    :ivar siteAccessProblem: Problems previously encountered when
        visiting or performing work on this location. Examples include:
        bad dog, violent customer, verbally abusive occupant,
        obstructions, safety hazards, etc.
    :ivar CustomerAgreements: All customer agreements regulating this
        service location.
    :ivar EndDevices: All end devices that measure the service delivered
        to this service location.
    :ivar TroubleTicket:
    :ivar UsagePoints: All usage points delivering service (of the same
        type) to this service location.
    """
    accessMethod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    needsInspection: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    siteAccessProblem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CustomerAgreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDevices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TroubleTicket: List["TroubleTicket"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class ServiceMultiplierKind(Enum):
    """
    Kind of service multiplier.

    :cvar ctRatio: Current transformer ratio used to convert associated
        quantities to real measurements.
    :cvar ptRatio: Voltage transformer ratio used to convert associated
        quantities to real measurements.
    :cvar transformerRatio: Product of the CT ratio and PT ratio.
    """
    ctRatio = "ctRatio"
    ptRatio = "ptRatio"
    transformerRatio = "transformerRatio"


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


class SmartInverterMode(Enum):
    """
    :cvar constantPF:
    :cvar constantPQ: Required to dispatch P and Q
    :cvar loadFollowing: For batteries
    :cvar voltVar: Default IEEE 1547-2018
    :cvar voltWatt: Default IEEE 1547-2018
    """
    constantPF = "constantPF"
    constantPQ = "constantPQ"
    loadFollowing = "loadFollowing"
    voltVar = "voltVar"
    voltWatt = "voltWatt"


class SpaceAnalogKind(Enum):
    """
    Kinds of analogs measuring a space condition.
    """
    magneticFieldDirection = "magneticFieldDirection"
    magneticFieldStrength = "magneticFieldStrength"


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

    :ivar addressGeneral: First line of a free form address or some
        additional address information (for example a mail stop).
    :ivar addressGeneral2: (if applicable) Second line of a free form
        address.
    :ivar addressGeneral3: (if applicable) Third line of a free form
        address.
    :ivar buildingName: (if applicable) In certain cases the physical
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
    :ivar suiteNumber: Number of the apartment or suite.
    :ivar type: Type of street. Examples include: street, circle,
        boulevard, avenue, road, drive, etc.
    :ivar withinTownLimits: True if this street is within the legal
        geographical boundaries of the specified town (default).
    """
    addressGeneral: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    addressGeneral2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    addressGeneral3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    buildingName: Optional[str] = field(
        default=None,
        metadata={
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
    suiteNumber: Optional[str] = field(
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
    withinTownLimits: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class SynchronousMachineKind(Enum):
    """
    Synchronous machine type.
    """
    condenser = "condenser"
    generator = "generator"
    generatorOrCondenser = "generatorOrCondenser"
    generatorOrCondenserOrMotor = "generatorOrCondenserOrMotor"
    generatorOrMotor = "generatorOrMotor"
    motor = "motor"
    motorOrCondenser = "motorOrCondenser"


class SynchronousMachineOperatingMode(Enum):
    """
    Synchronous machine operating mode.
    """
    condenser = "condenser"
    generator = "generator"
    motor = "motor"


class TAPPIStandardEditionKind(Enum):
    """
    List of editions for TAPPI standards.
    """
    value_2009 = "2009"
    none = "none"
    unknown = "unknown"


class TAPPIStandardKind(Enum):
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

    :ivar areaCode: (if applicable) Area or region code.
    :ivar cityCode: City code.
    :ivar countryCode: Country code.
    :ivar dialOut: (if applicable) Dial out code, for instance to call
        outside an enterprise.
    :ivar extension: (if applicable) Extension for this telephone
        number.
    :ivar internationalPrefix: (if applicable) Prefix used when calling
        an international number.
    :ivar ituPhone: Phone number according to ITU E.164.
    :ivar localNumber: Main (local) part of this telephone number.
    """
    areaCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cityCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    countryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dialOut: Optional[str] = field(
        default=None,
        metadata={
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
    internationalPrefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ituPhone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    localNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class TestKind(Enum):
    """
    The test applied to determine if the condition is met.
    """
    equalTo = "equalTo"
    greaterThan = "greaterThan"
    greaterThanOrEqualTo = "greaterThanOrEqualTo"
    lessThan = "lessThan"
    lessThanOrEqualTo = "lessThanOrEqualTo"


class TestMethod(Enum):
    """
    :cvar value_60567ByDisplacement:
    :cvar value_60567ByPartition:
    :cvar value_60567ByVacuum:
    :cvar value_60970Automatic: Automatic method.
    :cvar value_60970Manual1: Manual method 1.
    :cvar value_60970Manual2: Manual method 2.
    :cvar value_61125A:
    :cvar value_61125B:
    :cvar value_61125C:
    :cvar value_62270AnnexA:
    :cvar value_62535AnnexA:
    :cvar value_62535Main:
    :cvar D1275A:
    :cvar D1275B:
    :cvar D3612A:
    :cvar D3612B:
    :cvar D3612C:
    """
    value_60567ByDisplacement = "60567ByDisplacement"
    value_60567ByPartition = "60567ByPartition"
    value_60567ByVacuum = "60567ByVacuum"
    value_60970Automatic = "60970Automatic"
    value_60970Manual1 = "60970Manual1"
    value_60970Manual2 = "60970Manual2"
    value_61125A = "61125A"
    value_61125B = "61125B"
    value_61125C = "61125C"
    value_62270AnnexA = "62270AnnexA"
    value_62535AnnexA = "62535AnnexA"
    value_62535Main = "62535Main"
    D1275A = "D1275A"
    D1275B = "D1275B"
    D3612A = "D3612A"
    D3612B = "D3612B"
    D3612C = "D3612C"


class TestReason(Enum):
    postOilTreatment = "postOilTreatment"
    postOperationFault = "postOperationFault"
    postRepair = "postRepair"
    routine = "routine"


class TestVariantKind(Enum):
    """
    :cvar value_0C: Testing done at temperature of 0ï¿½C.
    :cvar value_100C: Testing done at temperature of  100ï¿½C.
    :cvar value_164hours: Measurements taken at 164 hours.
    :cvar value_1mm: Specimen of 1 mm thickness used in testing.
    :cvar value_25C: Testing done at temperature of  25ï¿½C.
    :cvar value_2mm: Specimen of 2 mm thickness used in testing.
    :cvar value_30C: Testing done at temperature of 30ï¿½C.
    :cvar value_40C: Testing done at temperature of 40ï¿½C.
    :cvar value_72hours: Measurements taken at 72 hours.
    :cvar minus30C: Testing done at temperature of -30ï¿½C.
    :cvar minus40C: Testing done at temperature of -40ï¿½C.
    """
    value_0C = "0C"
    value_100C = "100C"
    value_164hours = "164hours"
    value_1mm = "1mm"
    value_25C = "25C"
    value_2mm = "2mm"
    value_30C = "30C"
    value_40C = "40C"
    value_72hours = "72hours"
    minus30C = "minus30C"
    minus40C = "minus40C"


class ThermostatControlMode(Enum):
    Cooling = "Cooling"
    Heating = "Heating"


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
    h = "h"
    m_1 = "m"
    s = "s"


@dataclass
class TownDetail:
    """
    Town details, in the context of address.

    :ivar code: Town code.
    :ivar country: Name of the country.
    :ivar name: Town name.
    :ivar section: Town section. For example, it is common for there to
        be 36 sections per township.
    :ivar stateOrProvince: Name of the state or province.
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
    stateOrProvince: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


class TransformerApplicationKind(Enum):
    """Classifications of network roles in which transformers can be deployed.

    The classifications are intended to reflect both criticality of transformer in network operations and typical usage experienced by transformer.
    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    distribution = "distribution"
    generatorStepUp = "generatorStepUp"
    transmissionBusToBus = "transmissionBusToBus"
    transmissionBusToDistribution = "transmissionBusToDistribution"


class TransformerFailureReasonKind(Enum):
    """Reason for transformer failure.

    Note: This enumeration provides essential information to asset health analytics. The existing list is a starting point and is anticipated to be fleshed out further as requirements are better understood (PAB 2016/01/09).
    """
    bushingFailure = "bushingFailure"
    lossOfOil = "lossOfOil"
    oilRelatedFailure = "oilRelatedFailure"
    poorOilQuality = "poorOilQuality"


class TransmissionModeKind(Enum):
    """
    Transmission mode for end device display controls, applicable to premises
    area network (PAN) devices.

    :cvar anonymous: Message transmission mode whereby messages or
        commands are broadcast to unspecified devices listening for such
        communications.
    :cvar both: Message transmission mode whereby messages or commands
        are sent by both 'normal' and 'anonymous' methods.
    :cvar normal: Message transmission mode whereby messages or commands
        are sent to specific devices.
    """
    anonymous = "anonymous"
    both = "both"
    normal = "normal"


class TroubleReportingKind(Enum):
    """
    Kind of trouble reporting.

    :cvar call: Trouble call received by customer service
        representative.
    :cvar email: Trouble reported by email.
    :cvar ivr: Trouble reported through interactive voice response
        system.
    :cvar letter: Trouble reported by letter.
    :cvar other: Trouble reported by other means.
    """
    call = "call"
    email = "email"
    ivr = "ivr"
    letter = "letter"
    other = "other"





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
    :cvar A2h: ampere-squared hour, Ampere-squared hour.
    :cvar A2s: Ampere squared time in square ampere (Aï¿½s).
    :cvar APerA: Current, Ratio of Amperages  Note: Users may need to
        supply a prefix such as ï¿½mï¿½ to show rates such as
        ï¿½mA/Aï¿½.
    :cvar APerm: A/m, magnetic field strength, Ampere per metre.
    :cvar Ah: Ampere-hours, Ampere-hours.
    :cvar As: Ampere seconds (Aï¿½s).
    :cvar Bq: Radioactivity in Becquerel (1/s).
    :cvar Btu: Energy, British Thermal Unit.
    :cvar C: Electric charge in Coulomb (Aï¿½s).
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
        need to supply a prefix such as ï¿½mï¿½ to show rates such as
        ï¿½mHz/Hzï¿½.
    :cvar HzPers: Rate of change of frequency in Hertz per second.
    :cvar J: Energy in joule (Nï¿½m = Cï¿½V = Wï¿½s).
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
    :cvar N: Force in Newton (kgï¿½m/sï¿½).
    :cvar NPerm: Surface tension, Newton per metre.
    :cvar Nm: Moment of force, Newton metre.
    :cvar Oe: Magnetic field, ï¿½rsted (1 Oe = (103/4p) A/m).
    :cvar Pa: Pressure in Pascal (N/mï¿½). Note: the absolute or
        relative measurement of pressure is implied with this entry. See
        below for more explicit forms.
    :cvar PaPers: Pressure change rate in Pascal per second.
    :cvar Pas: Dynamic viscosity, Pascal second.
    :cvar Q: Quantity power, Q.
    :cvar Qh: Quantity energy, Qh.
    :cvar S: Conductance in Siemens.
    :cvar SPerm: Conductance per length (F/m).
    :cvar Sv: Dose equivalent in Sievert (J/kg).
    :cvar T: Magnetic flux density in Tesla (Wb/m2).
    :cvar V: Electric potential in Volt (W/A).
    :cvar V2: Volt squared (Wï¿½/Aï¿½).
    :cvar V2h: volt-squared hour, Volt-squared-hours.
    :cvar VA: Apparent power in Volt Ampere (See also real power and
        reactive power.)
    :cvar VAh: Apparent energy in Volt Ampere hours.
    :cvar VAr: Reactive power in Volt Ampere reactive. The
        ï¿½reactiveï¿½ or ï¿½imaginaryï¿½ component of electrical power
        (VIsin(phi)). (See also real power and apparent power). Note:
        Different meter designs use different methods to arrive at their
        results. Some meters may compute reactive power as an arithmetic
        value, while others compute the value vectorially. The data
        consumer should determine the method in use and the suitability
        of the measurement for the intended purpose.
    :cvar VArh: Reactive energy in Volt Ampere reactive hours.
    :cvar VPerHz: Magnetic flux in Volt per Hertz.
    :cvar VPerV: Voltage, Ratio of voltages Note: Users may need to
        supply a prefix such as ï¿½mï¿½ to show rates such as
        ï¿½mV/Vï¿½.
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
        (Iï¿½R or VIcos(phi)), is expressed in Watts. (See also apparent
        power and reactive power.)
    :cvar WPerA: Active power per current flow, watt per Ampere.
    :cvar WPerW: Signal Strength, Ratio of power  Note: Users may need
        to supply a prefix such as ï¿½mï¿½ to show rates such as
        ï¿½mW/Wï¿½.
    :cvar WPerm2: Heat flux density, irradiance, Watt per square metre.
    :cvar WPerm2sr: radiance, Watt per square metre steradian.
    :cvar WPermK: Thermal conductivity in Watt/metre Kelvin.
    :cvar WPers: Ramp rate in Watt per second.
    :cvar WPersr: Radiant intensity, Watt per steradian.
    :cvar Wb: Magnetic flux in Weber (Vï¿½s).
    :cvar Wh: Real energy in Watt hours.
    :cvar anglemin: Plane angle, minute.
    :cvar anglesec: Plane angle, second.
    :cvar bar: Pressure, bar (1 bar = 100 kPa).
    :cvar cd: Luminous intensity in candela.
    :cvar charPers: Data rate (baud) in characters per second.
    :cvar character: Number of characters.
    :cvar cosPhi: Power factor, dimensionless. Note 1: This definition
        of power factor only holds for balanced systems. See the
        alternative definition under code 153. Note 2ï¿½: Beware of
        differing sign conventions in use between the IEC and EEI. It is
        assumed that the data consumer understands the type of meter in
        use and the sign convention in use by the utility.
    :cvar count: Amount of substance, Counter value.
    :cvar d: Time, day = 24 h = 86400 s.
    :cvar dB: Sound pressure level in decibel. Note:  multiplier ï¿½dï¿½
        is included in this unit symbol for compatibility with IEC
        61850-7-3.
    :cvar dBm: Power level (logrithmic ratio of signal strength , Bel-
        mW), normalized to 1mW. Note:  multiplier ï¿½dï¿½ is included in
        this unit symbol for compatibility with IEC 61850-7-3.
    :cvar deg: Plane angle in degrees.
    :cvar degC: Relative temperature in degrees Celsius. In the SI unit
        system the symbol is ï¿½C. Electric charge is measured in
        coulomb that has the unit symbol C. To distinguish degree
        Celsius form coulomb the symbol used in the UML is degC. Reason
        for not using ï¿½C is the special character ï¿½ is difficult to
        manage in software.
    :cvar ft3: Volume, cubic foot.
    :cvar gPerg: Concentration, The ratio of the mass of a solute
        divided by the mass of  the solution. Note: Users may need use a
        prefix such a ï¿½ï¿½ï¿½ to express a quantity such as
        ï¿½ï¿½g/gï¿½.
    :cvar gal: Volume, US gallon (1 gal = 231 in3 = 128 fl ounce).
    :cvar h_1: Time, hour = 60 min = 3600 s.
    :cvar ha: Area, hectare.
    :cvar kat: Catalytic activity, katal = mol / s.
    :cvar katPerm3: catalytic activity concentration, katal per cubic
        metre.
    :cvar kg: Mass in kilogram.  Note: multiplier ï¿½kï¿½ is included in
        this unit symbol for compatibility with IEC 61850-7-3.
    :cvar kgPerJ: Weigh per energy in kilogram/joule (kg/J). Note:
        multiplier ï¿½kï¿½ is included in this unit symbol for
        compatibility with IEC 61850-7-3.
    :cvar kgPerm3: Density in kilogram/cubic metre (kg/mï¿½). Note:
        multiplier ï¿½kï¿½ is included in this unit symbol for
        compatibility with IEC 61850-7-3.
    :cvar kgm: Moment of mass in kilogram metre (kgï¿½m) (first moment
        of mass). Note: multiplier ï¿½kï¿½ is included in this unit
        symbol for compatibility with IEC 61850-7-3.
    :cvar kgm2: Moment of mass in kilogram square metre (kgï¿½mï¿½)
        (Second moment of mass, commonly called the moment of inertia).
        Note: multiplier ï¿½kï¿½ is included in this unit symbol for
        compatibility with IEC 61850-7-3.
    :cvar kn: Speed, knot (1 kn = 1852/3600) m/s.
    :cvar l: Volume, litre = dm3 = m3/1000.
    :cvar lPerh: Volumetric flow rate, litre per hour.
    :cvar lPerl: Concentration, The ratio of the volume of a solute
        divided by the volume of  the solution. Note: Users may need use
        a prefix such a ï¿½ï¿½ï¿½ to express a quantity such as
        ï¿½ï¿½L/Lï¿½.
    :cvar lPers: Volumetric flow rate in litre per second.
    :cvar lm: Luminous flux in lumen (cdï¿½sr).
    :cvar lx: Illuminance in lux (lm/mï¿½).
    :cvar m_1: Length in meter.
    :cvar m2: Area in square metre (mï¿½).
    :cvar m2Pers: Viscosity in metre square / second (mï¿½/s).
    :cvar m3: Volume in cubic metre (mï¿½).
    :cvar m3Compensated: Volume, cubic metre, with the value compensated
        for weather effects.
    :cvar m3Perh: Volumetric flow rate, cubic metre per hour.
    :cvar m3Perkg: Specific volume, cubic metre per kilogram, v.
    :cvar m3Pers: Volumetric flow rate in cubic metres per second
        (mï¿½/s).
    :cvar m3Uncompensated: Volume, cubic metre, with the value
        uncompensated for weather effects.
    :cvar mPerm3: Fuel efficiency in metre per cubic metre (m/mï¿½).
    :cvar mPers: Velocity in metre per second (m/s).
    :cvar mPers2: Acceleration in metre per second squared (m/sï¿½).
    :cvar min: Time, minute  = 60 s.
    :cvar mmHg: Pressure, millimeter of mercury (1 mmHg is approximately
        133.3 Pa).
    :cvar mol: Amount of substance in mole.
    :cvar molPerkg: Concentration, Molality, the amount of solute in
        moles and the amount of solvent in kilograms.
    :cvar molPerm3: Concentration, The amount of substance
        concentration, (c), the amount of solvent in moles divided by
        the volume of solution in mï¿½.
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
        prefix such as ï¿½ï¿½ï¿½ to show rates such as ï¿½ï¿½s/sï¿½
    :cvar sr: Solid angle in steradian (m2/m2).
    :cvar therm: Energy, Therm.
    :cvar tonne: mass, ï¿½tonneï¿½ or ï¿½metric  tonï¿½ (1000 kg = 1
        Mg).
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

    :cvar blowingDust: "BD" weather code ("Blowing Dust").
    :cvar blowingSand: "BN" weather code ("Blowing Sand").
    :cvar blowingSnow: "BS" weather code ("Blowing Snow").
    :cvar cloudy:
    :cvar drizzle: "L" weather code ("Drizzle").
    :cvar fog: "F weather code ("Fog
    :cvar freezingDrizzle: "ZL" weather code ("Freezing Drizzle").
    :cvar freezingRain: "ZR" weather code ("Freezing Rain").
    :cvar freezingSpray: "ZF" weather code ("Freezing Spray").
    :cvar frost: "FR" weather code ("Frost").
    :cvar hail: "A" weather code ("Hail").
    :cvar haze: "H" weather code ("Haze").
    :cvar iceCrystals: "IC" weather code ("Ice Crystals").
    :cvar iceFog: "IF" weather code ("Ice Fog").
    :cvar mist: "BR" weather code ("Mist"),
    :cvar rain: "R" weather code ("Rain").
    :cvar rainShowers: "RW" weather code ("Rain Showers").
    :cvar rainSnowMix: "RS" weather code ("Rain/Snow Mix").
    :cvar sleet: "IP" weather code ("Ice Pellets/Sleet").
    :cvar smoke: "K" weather code ("Smoke").
    :cvar snow: "S" weather code ("Snow").
    :cvar snowShowers: "SW" weather code ("Snow Showers").
    :cvar snowSleetMix: "SI" weather code ("Snow/Sleet Mix").
    :cvar sunny:
    :cvar thunderStorms: "T" weather code ("Thunder Storms").
    :cvar volcanicAsh: "VA" weather code ("Volcanic Ash").
    :cvar waterSpouts: "WP" weather code ("Water Spouts")
    :cvar wintryMix: "WS" weather code ("Wintry Mix").
    """
    blowingDust = "blowingDust"
    blowingSand = "blowingSand"
    blowingSnow = "blowingSnow"
    cloudy = "cloudy"
    drizzle = "drizzle"
    fog = "fog"
    freezingDrizzle = "freezingDrizzle"
    freezingRain = "freezingRain"
    freezingSpray = "freezingSpray"
    frost = "frost"
    hail = "hail"
    haze = "haze"
    iceCrystals = "iceCrystals"
    iceFog = "iceFog"
    mist = "mist"
    rain = "rain"
    rainShowers = "rainShowers"
    rainSnowMix = "rainSnowMix"
    sleet = "sleet"
    smoke = "smoke"
    snow = "snow"
    snowShowers = "snowShowers"
    snowSleetMix = "snowSleetMix"
    sunny = "sunny"
    thunderStorms = "thunderStorms"
    volcanicAsh = "volcanicAsh"
    waterSpouts = "waterSpouts"
    wintryMix = "wintryMix"


class WindGenUnitKind(Enum):
    """
    Kind of wind generating unit.

    :cvar offshore: The wind generating unit is located offshore.
    :cvar onshore: The wind generating unit is located onshore.
    """
    offshore = "offshore"
    onshore = "onshore"


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


class WireUsageKind(Enum):
    """
    Kind of wire usage.

    :cvar distribution: Wire is used in medium voltage network.
    :cvar other: Other kind of wire usage.
    :cvar secondary: Wire is used in low voltage circuit.
    :cvar transmission: Wire is used in extra-high voltage or high
        voltage network.
    """
    distribution = "distribution"
    other = "other"
    secondary = "secondary"
    transmission = "transmission"



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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    curveStyleKind: Optional[CurveStyle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    numberOfIntervals: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeIntervalDuration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeIntervalUnit: Optional[TimeIntervalKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DERCurveData: List["DERCurveData"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DERMonitorableParameter: Optional["DERMonitorableParameter"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    durationIndefinite: Optional[bool] = field(
        default=None,
        metadata={
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
    extensionsItem: Optional[ExtensionItem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FieldDispatchStep:
    """
    Details of the step in the field dispatch history.

    :ivar dispatchStatus: The status of one or more crews dispatched to
        perform field work at one or more work sites
    :ivar occurredDateTime: The date and time at which the dispatch
        status occurred.
    :ivar remarks: freeform comments related to the dispatch to perform
        field work.
    :ivar sequenceNumber: The sequence number of the field dispatch step
        within the field dispatch history.  Begins with 1 and increments
        up.
    :ivar FieldDispatchHistory:
    """
    dispatchStatus: Optional[CrewStatusKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    occurredDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
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
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FieldDispatchHistory: Optional["FieldDispatchHistory"] = field(
        default=None,
        metadata={
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
    :ivar Names: All names of this type.
    :ivar NameTypeAuthority: Authority responsible for managing names of
        this type.
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
    Names: List["Name"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NameTypeAuthority: Optional[NameTypeAuthority] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PanDemandResponse(EndDeviceAction):
    """
    PAN control used to issue action/command to PAN devices during a demand
    response/load control event.

    :ivar avgLoadAdjustment: Used to define a maximum energy usage limit
        as a percentage of the client implementations specific average
        energy usage. The load adjustment percentage is added to 100%
        creating a percentage limit applied to the client
        implementations specific average energy usage. A -10% load
        adjustment percentage will establish an energy usage limit equal
        to 90% of the client implementations specific average energy
        usage. Each load adjustment percentage is referenced to the
        client implementations specific average energy usage. There are
        no cumulative effects. The range of this field is -100% to +100%
        with a resolution of 1. A -100% value equals a total load shed.
        A +100% value will limit the energy usage to the client
        implementations specific average energy usage.
    :ivar cancelControlMode: Encoding of cancel control.
    :ivar cancelDateTime: Timestamp when a canceling of the event is
        scheduled to start.
    :ivar cancelNow: If true, a canceling of the event should start
        immediately.
    :ivar coolingOffset: Requested offset to apply to the normal cooling
        setpoint at the time of the start of the event. It represents a
        temperature change that will be applied to the associated
        cooling set point. The temperature offsets will be calculated
        per the local temperature in the thermostat. The calculated
        temperature will be interpreted as the number of degrees to be
        added to the cooling set point. Sequential demand response
        events are not cumulative. The offset shall be applied to the
        normal setpoint.
    :ivar coolingSetpoint: Requested cooling set point. Temperature set
        point is typically defined and calculated based on local
        temperature.
    :ivar criticalityLevel: Level of criticality for the action of this
        control. The action taken by load control devices for an event
        can be solely based on this value, or in combination with other
        load control event fields supported by the device.
    :ivar dutyCycle: Maximum "on" state duty cycle as a percentage of
        time. For example, if the value is 80, the device would be in an
        "on" state for 80% of the time for the duration of the action.
    :ivar enrollmentGroup: Provides a mechanism to direct load control
        actions to groups of PAN devices. It can be used in conjunction
        with the PAN device types.
    :ivar heatingOffset: Requested offset to apply to the normal heating
        setpoint at the time of the start of the event. It represents a
        temperature change that will be applied to the associated
        heating set point. The temperature offsets will be calculated
        per the local temperature in the thermostat. The calculated
        temperature will be interpreted as the number of degrees to be
        subtracted from the heating set point. Sequential demand
        response events are not cumulative. The offset shall be applied
        to the normal setpoint.
    :ivar heatingSetpoint: Requested heating set point. Temperature set
        point is typically defined and calculated based on local
        temperature.
    :ivar appliance: Appliance being controlled.
    """
    avgLoadAdjustment: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cancelControlMode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cancelDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cancelNow: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    coolingOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    coolingSetpoint: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    criticalityLevel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dutyCycle: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enrollmentGroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heatingOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heatingSetpoint: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar confirmationRequired: If true, the requesting entity (e.g.
        retail electric provider) requires confirmation of the
        successful display of the text message.
    :ivar priority: Priority associated with the text message to be
        displayed.
    :ivar textMessage: Text to be displayed by a PAN device.
    :ivar transmissionMode: Transmission mode to be used for this PAN
        display control.
    """
    confirmationRequired: Optional[bool] = field(
        default=None,
        metadata={
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
    textMessage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transmissionMode: Optional[TransmissionModeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PanPricing(EndDeviceAction):
    """
    PAN action/command used to issue pricing information to a PAN device.

    :ivar providerID: Unique identifier for the commodity provider.
    :ivar PanPricingDetails: All pricing details issued by this PAN
        pricing command/action.
    """
    providerID: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PanPricingDetails: List[PanPricingDetail] = field(
        default_factory=list,
        metadata={
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
    :ivar PhaseTapChangerTable: The table of this point.
    """
    angle: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PhaseTapChangerTable: Optional["PhaseTapChangerTable"] = field(
        default=None,
        metadata={
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

    :ivar badReference: Measurement value may be incorrect due to a
        reference being out of calibration.
    :ivar estimatorReplaced: Value has been replaced by State Estimator.
        estimatorReplaced is not an IEC61850 quality bit but has been
        put in this class for convenience.
    :ivar failure: This identifier indicates that a supervision function
        has detected an internal or external failure, e.g. communication
        failure.
    :ivar oldData: Measurement value is old and possibly invalid, as it
        has not been successfully updated during a specified time
        interval.
    :ivar operatorBlocked: Measurement value is blocked and hence
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
    :ivar outOfRange: Measurement value is beyond a predefined range of
        value.
    :ivar overFlow: Measurement value is beyond the capability of being
        represented properly. For example, a counter value overflows
        from maximum count back to a value of zero.
    :ivar suspect: A correlation function has detected that the value is
        not consitent with other values. Typically set by a network
        State Estimator.
    :ivar test: Measurement value is transmitted for test purposes.
    :ivar validity: Validity of the measurement value.
    """
    badReference: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    estimatorReplaced: Optional[bool] = field(
        default=None,
        metadata={
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
    oldData: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operatorBlocked: Optional[bool] = field(
        default=None,
        metadata={
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
    outOfRange: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overFlow: Optional[bool] = field(
        default=None,
        metadata={
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

    :ivar RatioTapChangerTable: Table of this point.
    """
    RatioTapChangerTable: Optional["RatioTapChangerTable"] = field(
        default=None,
        metadata={
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

    :ivar reportingIntervalPeriod: Number of units of time making up
        reporting period.
    :ivar reportingMethod: Indicates how the weather station reports
        observations.
    :ivar EnvironmentalAnalog: One of the environmental value sets
        expressing one of the reporting capabilities.
    """
    reportingIntervalPeriod: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reportingMethod: Optional[ReportingMethodKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalAnalog: List["EnvironmentalAnalog"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class StreetAddress:
    """
    General purpose street and postal address information.

    :ivar poBox: Post office box.
    :ivar postalCode: Postal code for the address.
    :ivar status: Status of this address.
    :ivar streetDetail: Street detail.
    :ivar townDetail: Town detail.
    """
    poBox: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    postalCode: Optional[str] = field(
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
    streetDetail: Optional[StreetDetail] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    townDetail: Optional[TownDetail] = field(
        default=None,
        metadata={
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
    :ivar Terminal: The terminal associated with the power flow state
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
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
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
    :ivar ShuntCompensator: The shunt compensator for which the state
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
    ShuntCompensator: Optional["ShuntCompensator"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SvStatus(StateVariable):
    """
    State variable for status.

    :ivar inService: The in service status as a result of topology
        processing.
    :ivar phase: The individual phase status.    If the attribute is
        unspecified, then three phase model is assumed.
    :ivar ConductingEquipment: The conducting equipment associated with
        the status state variable.
    """
    inService: Optional[bool] = field(
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
    ConductingEquipment: Optional["ConductingEquipment"] = field(
        default=None,
        metadata={
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
    :ivar Switch: The switch associated with the switch state.
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
    Switch: Optional["Switch"] = field(
        default=None,
        metadata={
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
    :ivar TapChanger: The tap changer associated with the tap step
        state.
    """
    position: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TapChanger: Optional["TapChanger"] = field(
        default=None,
        metadata={
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
    :ivar ConnectivityNode:
    :ivar TopologicalNode: The topological node associated with the
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
    ConnectivityNode: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TopologicalNode: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )



@dataclass
class DERCurveData:
    intervalNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxYValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minYValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominalYValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DERMonitorableParameter: Optional["DERMonitorableParameter"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DispatchSchedule: Optional[DispatchSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceEvent: Optional["EndDeviceEvent"] = field(
        default=None,
        metadata={
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

    :ivar MeasurementValue: A MeasurementValue has a
        MeasurementValueQuality associated with it.
    """
    MeasurementValue: Optional["MeasurementValue"] = field(
        default=None,
        metadata={
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
    :ivar IdentifiedObject: Identified object that this name designates.
    :ivar NameType: Type of this name.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IdentifiedObject: Optional["IdentifiedObject"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    NameType: Optional[NameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SvEstVoltage(SvVoltage):
    angleVariance: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    vVariance: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Estimate: Optional["Estimate"] = field(
        default=None,
        metadata={
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
    :ivar sequenceNumber: Sequence number for this attribute in a list
        of attributes.
    :ivar ProcedureDataSets:
    :ivar value: Value of an attribute, including unit information.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ProcedureDataSets: List["ProcedureDataSet"] = field(
        default_factory=list,
        metadata={
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
class DERMonitorableParameter:
    DERParameter: Optional[DERParameterKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    flowDirection: Optional[FlowDirectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    yMultiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    yUnit: Optional[DERUnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    yUnitInstalledMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    yUnitInstalledMin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DERCurveData: Optional[DERCurveData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DispatchSchedule: List[DispatchSchedule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceGroup: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Estimate:
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvEstVoltages: List[SvEstVoltage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )




@dataclass
class Appointment(IdentifiedObject):
    """
    Meeting time and location.

    :ivar callAhead: True if requested to call customer when someone is
        about to arrive at their premises.
    :ivar meetingInterval: Date and time reserved for appointment.
    :ivar Persons: All persons for this appointment.
    """
    callAhead: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    meetingInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Persons: List["PersonRole"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetDeployment(IdentifiedObject):
    """
    Deployment of asset deployment in a power system resource role.

    :ivar breakerApplication: Type of network role breaker is playing in
        this deployment (applies to breaker assets only).
    :ivar deploymentState: Current deployment state of asset.
    :ivar facilityKind: Kind of facility (like substation or pole or
        building or plant or service center) at which asset deployed.
    :ivar likelihoodOfFailure: Likelihood of asset failure on a scale of
        1(low) to 100 (high).
    :ivar transformerApplication: Type of network role transformer is
        playing in this deployment (applies to transformer assets only).
    :ivar Asset: Asset in this deployment.
    :ivar BaseVoltage: Base voltage of this network asset deployment.
    :ivar deploymentDate: Dates of asset deployment.
    """
    breakerApplication: Optional[BreakerApplicationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    deploymentState: Optional[DeploymentStateKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    facilityKind: Optional[FacilityKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    likelihoodOfFailure: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformerApplication: Optional[TransformerApplicationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    BaseVoltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    deploymentDate: Optional[DeploymentDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    firmwareID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hardwareID: Optional[str] = field(
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
    programID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: Optional["Asset"] = field(
        default=None,
        metadata={
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

    :ivar basePower: Value used as base power.
    """
    basePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value1Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value1Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value2Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    value2Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BranchGroup(IdentifiedObject):
    """A group of branch terminals whose directed flow summation is to be
    monitored.

    A branch group need not form a cutset of the network.

    :ivar maximumActivePower: The maximum active power flow.
    :ivar maximumReactivePower: The maximum reactive power flow.
    :ivar minimumActivePower: The minimum active power flow.
    :ivar minimumReactivePower: The minimum reactive power flow.
    :ivar monitorActivePower: Monitor the active power flow.
    :ivar monitorReactivePower: Monitor the reactive power flow.
    :ivar BranchGroupTerminal:
    """
    maximumActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maximumReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimumActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimumReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    monitorActivePower: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    monitorReactivePower: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    BranchGroupTerminal: List["BranchGroupTerminal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CIM_GridAPPS_D_RC4_2021:
    class Meta:
        namespace = "http://iec.ch/TC57/CIM100#"

    IdentifiedObject: List[IdentifiedObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CatalogAssetType(IdentifiedObject):
    """
    assets that may be used for planning, work or design purposes.

    :ivar estimatedUnitCost: Estimated unit cost (or cost per unit
        length) of this type of asset. It does not include labor to
        install, construct or configure it.
    :ivar kind:
    :ivar stockItem: True if item is a stock item (default).
    :ivar type:
    :ivar AssetInfo:
    :ivar ProductAssetModel:
    :ivar quantity: The value, unit of measure, and multiplier for the
        quantity.
    """
    estimatedUnitCost: Optional[Decimal] = field(
        default=None,
        metadata={
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
    stockItem: Optional[bool] = field(
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
    AssetInfo: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ProductAssetModel: List["ProductAssetModel"] = field(
        default_factory=list,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Locations: List["Location"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CrewType(IdentifiedObject):
    """Custom description of the type of crew.

    This may be used to determine the type of work the crew can be
    assigned to. Examples include repair, tree trimming, switching, etc.

    :ivar Crews: All crews of this type.
    """
    Crews: List["Crew"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xMultiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xUnit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y1Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y1Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y2Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y2Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y3Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    y3Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CurveDatas: List[CurveData] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class DERGroupDispatch(IdentifiedObject):
    EndDeviceGroup: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class DERGroupForecast(IdentifiedObject):
    predictionCreationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceGroup: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
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

    :ivar SeasonDayTypeSchedules: Schedules that use this DayType.
    """
    SeasonDayTypeSchedules: List["SeasonDayTypeSchedule"] = field(
        default_factory=list,
        metadata={
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

    :ivar authorName: Name of the author of this document.
    :ivar comment: Free text comment.
    :ivar createdDateTime: Date and time that this document was created.
    :ivar lastModifiedDateTime: Date and time this document was last
        modified. Documents may potentially be modified many times
        during their lifetime.
    :ivar revisionNumber: Revision number for this document.
    :ivar subject: Document subject.
    :ivar title: Document title.
    :ivar type: Utility-specific classification of this document,
        according to its corporate standards, practices, and existing IT
        systems (e.g., for management of assets, maintenance, work,
        outage, customers, etc.).
    :ivar Approver: Approver of this document.
    :ivar Author: Author of this document.
    :ivar ConfigurationEvents: All configuration events created for this
        document.
    :ivar docStatus: Status of this document. For status of subject
        matter this document represents (e.g., Agreement, Work), use
        'status' attribute. Example values for 'docStatus.status' are
        draft, approved, cancelled, etc.
    :ivar Editor: Editor of this document.
    :ivar electronicAddress: Electronic address.
    :ivar Issuer: Issuer of this document.
    :ivar status: Status of subject matter (e.g., Agreement, Work) this
        document represents. For status of the document itself, use
        'docStatus' attribute.
    """
    authorName: Optional[str] = field(
        default=None,
        metadata={
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
    createdDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lastModifiedDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    revisionNumber: Optional[str] = field(
        default=None,
        metadata={
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
    Approver: Optional["Approver"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Author: Optional["Author"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConfigurationEvents: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    docStatus: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Editor: Optional["Editor"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    electronicAddress: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Issuer: Optional["Issuer"] = field(
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    eventOrAction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    subDomain: Optional[str] = field(
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
    EndDeviceControls: List["EndDeviceControl"] = field(
        default_factory=list,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    eventOrAction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    subDomain: Optional[str] = field(
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
    EndDeviceEvents: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
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

    :ivar ConfigurationEvent:
    :ivar Faults: All faults with this cause type.
    """
    ConfigurationEvent: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Faults: List["Fault"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FieldDispatchHistory(IdentifiedObject):
    """
    The history of field dispatch statuses for this work.
    """
    Crew: Optional["Crew"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FieldDispatchStep: List[FieldDispatchStep] = field(
        default_factory=list,
        metadata={
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
    :ivar actualPurchaseCost: The actual purchase cost of this
        particular asset.
    :ivar costDescription: Description of the cost.
    :ivar costType: Type of cost to which this Material Item belongs.
    :ivar financialValue: Value of asset as of 'valueDateTime'.
    :ivar plantTransferDateTime: Date and time asset's financial value
        was put in plant for regulatory accounting purposes (e.g., for
        rate base calculations). This is sometime referred to as the
        "in-service date".
    :ivar purchaseDateTime: Date and time asset was purchased.
    :ivar purchaseOrderNumber: Purchase order identifier.
    :ivar valueDateTime: Date and time at which the financial value was
        last established.
    :ivar warrantyEndDateTime: Date and time warranty on asset expires.
    :ivar Asset:
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
    actualPurchaseCost: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    costDescription: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    costType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    financialValue: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    plantTransferDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    purchaseDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    purchaseOrderNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    valueDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    warrantyEndDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: Optional["Asset"] = field(
        default=None,
        metadata={
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

    :ivar Regions: All sub-geograhpical regions within this geographical
        region.
    """
    Regions: List["SubGeographicalRegion"] = field(
        default_factory=list,
        metadata={
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
class IOPoint(IdentifiedObject):
    """The class describe a measurement or control value.

    The purpose is to enable having attributes and associations common
    for measurement and control.
    """


@dataclass
class Limit(IdentifiedObject):
    """Specifies one limit value for a Measurement.

    A Measurement typically has several limits that are kept together by
    the LimitSet class. The actual meaning and use of a Limit instance
    (i.e., if it is an alarm or warning limit or if it is a high or low
    limit) is not captured in the Limit class. However the name of a
    Limit instance may indicate both meaning and use.
    """
    Procedures: List["Procedure"] = field(
        default_factory=list,
        metadata={
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

    :ivar isPercentageLimits: Tells if the limit values are in
        percentage of normalValue or the specified Unit for Measurements
        and Controls.
    """
    isPercentageLimits: Optional[bool] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pConstantCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pConstantImpedance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pConstantPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pVoltageExponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    qConstantCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    qConstantImpedance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    qConstantPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    qVoltageExponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnergyConsumer: List["EnergyConsumer"] = field(
        default_factory=list,
        metadata={
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

    :ivar MeasurementValues: The MeasurementValues updated by the
        source.
    """
    MeasurementValues: List["MeasurementValue"] = field(
        default_factory=list,
        metadata={
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
    :ivar volumeSpec: The volume of the medium specified for this
        application. Note that the actual volume is a type of
        measurement associated witht the asset.
    :ivar Asset:
    """
    kind: Optional[MediumKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    volumeSpec: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: List["Asset"] = field(
        default_factory=list,
        metadata={
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
    :ivar Meter: Meter applying this multiplier.
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
    Meter: Optional["Meter"] = field(
        default=None,
        metadata={
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
    :ivar ReadingTypes: All reading types required to be collected by
        this metrology requirement.
    :ivar UsagePoints: All usage points having this metrology
        requirement.
    """
    reason: Optional[ReadingReasonKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReadingTypes: List["ReadingType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
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
    :ivar First_Terminal: The starting terminal for the calculation of
        distances along the first branch of the mutual coupling.
        Normally MutualCoupling would only be used for terminals of AC
        line segments.  The first and second terminals of a mutual
        coupling should point to different AC line segments.
    :ivar Second_Terminal: The starting terminal for the calculation of
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
    First_Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Second_Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
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

    :ivar EnvironmentalPhenomenon: An occurence of an environmental
        phenomenon associated with this identified phenomenon.
    """
    EnvironmentalPhenomenon: List["EnvironmentalPhenomenon"] = field(
        default_factory=list,
        metadata={
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

    :ivar OperatingShare: The operating shares of this operating
        participant.  An operating participant can be resused for any
        number of power system resources.
    """
    OperatingShare: List["OperatingShare"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    OperationalLimit: List["OperationalLimit"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Organisation(IdentifiedObject):
    """
    Organisation that might have roles as utility, contractor, supplier,
    manufacturer, customer, etc.

    :ivar electronicAddress: Electronic address.
    :ivar ParentOrganisation: Parent organisation of this organisation.
    :ivar phone1: Phone number.
    :ivar phone2: Additional phone number.
    :ivar postalAddress: Postal address, potentially different than
        'streetAddress' (e.g., another city).
    :ivar Roles: All roles of this organisation.
    :ivar streetAddress: Street address.
    """
    electronicAddress: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ParentOrganisation: Optional["ParentOrganization"] = field(
        default=None,
        metadata={
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
    postalAddress: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Roles: List["OrganisationRole"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    streetAddress: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PSRType(IdentifiedObject):
    """Classifying instances of the same class, e.g. overhead and underground
    ACLineSegments.

    This classification mechanism is intended to provide flexibility
    outside the scope of this standard, i.e. provide customisation that
    is non standard.

    :ivar PowerSystemResources: Power system resources classified with
        this power system resource type.
    """
    PowerSystemResources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Person(IdentifiedObject):
    """
    General purpose information for name and other information to contact
    people.

    :ivar firstName: Person's first name.
    :ivar lastName: Person's last (family, sir) name.
    :ivar mName: Middle name(s) or initial(s).
    :ivar prefix: A prefix or title for the person's name, such as Miss,
        Mister, Doctor, etc.
    :ivar specialNeed: Special service needs for the person (contact)
        are described; examples include life support, etc.
    :ivar suffix: A suffix for the person's name, such as II, III, etc.
    :ivar electronicAddress: Electronic address.
    :ivar landlinePhone: Landline phone number.
    :ivar mobilePhone: Mobile phone number.
    :ivar Roles: All roles of this person.
    """
    firstName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lastName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mName: Optional[str] = field(
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
    specialNeed: Optional[str] = field(
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
    electronicAddress: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    landlinePhone: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mobilePhone: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Roles: List["PersonRole"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class RatioTapChangerTable(IdentifiedObject):
    """
    Describes a curve for how the voltage magnitude and impedance varies with
    the tap step.

    :ivar RatioTapChanger: The ratio tap changer of this tap ratio
        table.
    :ivar RatioTapChangerTablePoint: Points of this table.
    """
    RatioTapChanger: List["RatioTapChanger"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RatioTapChangerTablePoint: List[RatioTapChangerTablePoint] = field(
        default_factory=list,
        metadata={
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
    :ivar subCategory: More specific nature of the reading value
        quality, as a further sub-categorisation of 'category'.
    :ivar systemId: Identification of the system which has declared the
        issue with the data or provided commentary on the data.
    :ivar ReadingQualities: All reading qualities of this type.
    """
    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    subCategory: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    systemId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReadingQualities: List["ReadingQuality"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ReportingSuperGroup(IdentifiedObject):
    """
    A reporting super group, groups reporting groups for a higher level report.
    """
    ReportingGroup: List["ReportingGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class RightOfWay(IdentifiedObject):
    ParallelLineSegments: List["ParallelLineSegment"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class Seal(IdentifiedObject):
    """
    Physically controls access to AssetContainers.

    :ivar appliedDateTime: Date and time this seal has been applied.
    :ivar condition: Condition of seal.
    :ivar kind: Kind of seal.
    :ivar sealNumber: (reserved word) Seal number.
    :ivar AssetContainer: Asset container to which this seal is applied.
    """
    appliedDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
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
    sealNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetContainer: Optional["AssetContainer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startDate: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SeasonDayTypeSchedules: List["SeasonDayTypeSchedule"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ServiceCategory(IdentifiedObject):
    """
    Category of service provided to the customer.

    :ivar kind: Kind of service.
    :ivar ConfigurationEvents: All configuration events created for this
        service category.
    :ivar CustomerAgreements: All customer agreements with this service
        category.
    :ivar PricingStructures: All pricing structures applicable to this
        service category.
    :ivar UsagePoints: All usage points that deliver this category of
        service.
    """
    kind: Optional[ServiceKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConfigurationEvents: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CustomerAgreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PricingStructures: List["PricingStructure"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
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
    :ivar UsagePoint: Usage point applying this multiplier.
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
    UsagePoint: Optional["UsagePoint"] = field(
        default=None,
        metadata={
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

    :ivar lifetimeFaultOperations: Total breaker fault operations to
        date.
    :ivar lifetimeMotorStarts: Total motor starts to date.
    :ivar lifetimeTotalOperations: Total breaker operations to date
        (including fault and non-fault).
    :ivar mostRecentFaultOperationDate: Date of most recent breaker
        fault operation.
    :ivar mostRecentMotorStartDate: Date of most recent motor start.
    :ivar mostRecentOperationDate: Date of most recent breaker operation
        (fault or non-fault).
    :ivar Breaker: Breaker asset to which this operation information
        applies.
    """
    lifetimeFaultOperations: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lifetimeMotorStarts: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lifetimeTotalOperations: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mostRecentFaultOperationDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mostRecentMotorStartDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mostRecentOperationDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Breaker: Optional["Asset"] = field(
        default=None,
        metadata={
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

    :ivar testMethod: Identification of test method used if multiple
        methods specified by test standard.
    :ivar testVariant: Identification of variant of test method or
        standard if one is specified by the standard.
    :ivar testStandardASTM: Which ASTM standard used to determine analog
        value result. Applies only if ASTM standard used.
    :ivar testStandardCIGRE: Which CIGRE standard used to determine
        analog value result. Applies only if CIGRE standard used.
    :ivar testStandardDIN: Which DIN standard used to determine analog
        value result. Applies only if DIN standard used.
    :ivar testStandardDoble: Which Doble standard used to determine
        analog value result. Applies only if Doble standard used.
    :ivar testStandardEPA: Which EPA standard used to determine analog
        value result. Applies only if EPA standard used.
    :ivar testStandardIEC: Which IEC standard used to determine analog
        value result. Applies only if IEC standard used.
    :ivar testStandardIEEE: Which IEEE standard used to determine analog
        value result. Applies only if IEEE standard used.
    :ivar testStandardISO: Which ISO standard used to determine analog
        value result. Applies only if ISO standard used.
    :ivar testStandardLaborelec: Which Laborelec standard used to
        determine analog value result. Applies only if Laborelec
        standard used.
    :ivar testStandardTAPPI: Which TAPPI standard used to determine
        analog value result. Applies only if TAPPI standard used.
    :ivar testStandardUKMinistryOfDefence: Which UK Ministry of Defence
        standard used to determine analog value result. Applies only if
        UK Ministry of Defence standard used.
    :ivar testStandardWEP: Which WEP standard used to determine analog
        value result. Applies only if WEP standard used.
    """
    testMethod: Optional[TestMethod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testVariant: Optional[TestVariantKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardASTM: Optional[ASTMStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardCIGRE: Optional[CIGREStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardDIN: Optional[DINStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardDoble: Optional[DobleStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardEPA: Optional[EPAStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardIEC: Optional[IECStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardIEEE: Optional[IEEEStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardISO: Optional[ISOStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardLaborelec: Optional[LaborelecStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardTAPPI: Optional[TAPPIStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardUKMinistryOfDefence: Optional[UKMinistryOfDefenceStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testStandardWEP: Optional[WEPStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    baseSetpoint: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    controlMode: Optional[ThermostatControlMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    priceCap: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rampHigh: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rampLow: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rangeHigh: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rangeLow: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    useOverride: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    usePredictive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    House: Optional["House"] = field(
        default=None,
        metadata={
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

    :ivar AngleRefTopologicalNode: The angle reference for the island.
        Normally there is one TopologicalNode that is selected as the
        angle reference for each island.   Other reference schemes
        exist, so the association is typically optional.
    :ivar TopologicalNodes: A topological node belongs to a topological
        island.
    """
    AngleRefTopologicalNode: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TopologicalNodes: List["TopologicalNode"] = field(
        default_factory=list,
        metadata={
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
    :ivar TransformerEnd: All transformer ends having this core
        admittance.
    :ivar TransformerEndInfo: Transformer end datasheet used to
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
    TransformerEnd: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerEndInfo: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
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
    FromTransformerEnd: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    FromTransformerEndInfo: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ToTransformerEnd: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    ToTransformerEndInfos: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
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
    :ivar TransformerEnd: All transformer ends having this star
        impedance.
    :ivar TransformerEndInfo: Transformer end datasheet used to
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
    TransformerEnd: List["TransformerEnd"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerEndInfo: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar ValueAliasSet: The ValueAliasSet having the ValueToAlias
        mappings.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ValueAliasSet: Optional["ValueAliasSet"] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xCoord: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    yCoord: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WirePhaseInfo: List["WirePhaseInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WireSpacingInfo: Optional["WireSpacingInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AccumulatorLimit(Limit):
    """
    Limit values for Accumulator measurements.

    :ivar value: The value to supervise against. The value is positive.
    :ivar LimitSet: The set of limits.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    LimitSet: Optional["AccumulatorLimitSet"] = field(
        default=None,
        metadata={
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

    :ivar signDate: Date this agreement was consummated among associated
        persons and/or organisations.
    :ivar validityInterval: Date and time interval this agreement is
        valid (from going into effect to termination).
    """
    signDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    validityInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AnalogLimit(Limit):
    """
    Limit values for Analog measurements.

    :ivar value: The value to supervise against.
    :ivar LimitSet: The set of limits.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    LimitSet: Optional["AnalogLimitSet"] = field(
        default=None,
        metadata={
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
    :ivar Analytic:
    :ivar AnalyticScore:
    :ivar Asset:
    """
    kind: Optional[AssetGroupKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Analytic: List["Analytic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AnalyticScore: List["AnalyticScore"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: List["Asset"] = field(
        default_factory=list,
        metadata={
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
    :ivar Locations: The location of this hazard.
    """
    kind: Optional[AssetHazardKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Locations: List["Location"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BranchGroupTerminal:
    """
    A specific directed terminal flow for a branch group.

    :ivar positiveFlowIn: The flow into the terminal is summed if set
        true.   The flow out of the terminanl is summed if set false.
    :ivar BranchGroup:
    :ivar Terminal: The terminal to be summed.
    """
    positiveFlowIn: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    BranchGroup: Optional[BranchGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar operationInProgress: Indicates that a client is currently
        sending control commands that has not completed.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operationInProgress: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unitMultiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    unitSymbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerSystemResource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Crew(IdentifiedObject):
    """
    Group of people with specific skills, tools, and vehicles.

    :ivar CrewMembers: All members of this crew.
    :ivar CrewType: Type of this crew.
    :ivar FieldDispatchHistory:
    :ivar Location:
    :ivar status: Status of this crew.
    """
    CrewMembers: List["CrewMember"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CrewType: Optional[CrewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FieldDispatchHistory: List[FieldDispatchHistory] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Location: Optional["Location"] = field(
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
class CustomerAccount(Document):
    """Assignment of a group of products and services purchased by the customer
    through a customer agreement, used as a mechanism for customer billing and
    payment.

    It contains common information from the various types of customer
    agreements to create billings (invoices) for a customer and receive
    payment.

    :ivar billingCycle: Cycle day on which the associated customer
        account will normally be billed, used to determine when to
        produce the billing.
    :ivar budgetBill: Budget bill code.
    :ivar lastBillAmount: The last amount that will be billed to the
        customer prior to shut off of the account.
    :ivar AccountNotification:
    :ivar Customer: Customer owning this account.
    :ivar CustomerAgreements: All agreements for this customer account.
    """
    billingCycle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    budgetBill: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lastBillAmount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AccountNotification: List[AccountNotification] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Customer: Optional["Customer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CustomerAgreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
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

    :ivar emissionType: The type of emission, for example sulfur dioxide
        (SO2). The y1AxisUnits of the curve contains the unit of measure
        (e.g. kg) and the emissionType is the type of emission (e.g.
        sulfer dioxide).
    :ivar emissionValueSource: The source of the emission value.
    :ivar ThermalGeneratingUnit: A thermal generating unit may have one
        or more emission allowance accounts.
    """
    emissionType: Optional[EmissionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    emissionValueSource: Optional[EmissionValueSource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ThermalGeneratingUnit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
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

    :ivar emissionContent: The emission content per quantity of fuel
        burned.
    :ivar emissionType: The type of emission, which also gives the
        production rate measurement unit. The y1AxisUnits of the curve
        contains the unit of measure (e.g. kg) and the emissionType is
        the type of emission (e.g. sulfer dioxide).
    :ivar isNetGrossP: Flag is set to true when output is expressed in
        net active power.
    :ivar ThermalGeneratingUnit: A thermal generating unit may have  one
        or more emission curves.
    """
    emissionContent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    emissionType: Optional[EmissionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isNetGrossP: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ThermalGeneratingUnit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    drProgramMandatory: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    issuerID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    issuerTrackingID: Optional[str] = field(
        default=None,
        metadata={
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
    EndDeviceAction: Optional[EndDeviceAction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceControlType: Optional[EndDeviceControlType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EndDeviceGroups: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDevices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    priceSignal: Optional[FloatQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    primaryDeviceTiming: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scheduledInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    secondaryDeviceTiming: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePointGroups: List["UsagePointGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
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
    :ivar EndDevice: End device that performs this function.
    :ivar Registers: All registers for quantities metered by this end
        device function.
    """
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDevice: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Registers: List["Register"] = field(
        default_factory=list,
        metadata={
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

    :ivar EnvironmentalInformation:
    :ivar EnvironmentalLocationKind: Location of relevance to this
        environmental phenomenon.
    :ivar NamedPhenomenon: The identified phenomenon to which this
        environmental phenomenon is associated.
    :ivar PhenomenonClassification:
    :ivar timeInterval: The timestamp of the phenomenon as a single
        point or time interval.
    """
    EnvironmentalInformation: List["EnvironmentalInformation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    EnvironmentalLocationKind: List["EnvironmentalLocationType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NamedPhenomenon: Optional[NamedPhenomenon] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PhenomenonClassification: Optional["PhenomenonTypeification"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    occurredDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
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
    stopDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FaultCauseTypes: List[FaultCauseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FaultyEquipment: Optional["Equipment"] = field(
        default=None,
        metadata={
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
    Location: Optional["Location"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FuelAllocationSchedule(Curve):
    """
    The amount of fuel of a given type which is allocated for consumption over
    a specified period of time.

    :ivar fuelAllocationEndDate: The end time and date of the fuel
        allocation schedule.
    :ivar fuelAllocationStartDate: The start time and date of the fuel
        allocation schedule.
    :ivar fuelType: The type of fuel, which also indicates the
        corresponding measurement unit.
    :ivar maxFuelAllocation: The maximum amount fuel that is allocated
        for consumption for the scheduled time period.
    :ivar minFuelAllocation: The minimum amount fuel that is allocated
        for consumption for the scheduled time period, e.g., based on a
        "take-or-pay" contract.
    :ivar FossilFuel: A fuel allocation schedule must have a fossil
        fuel.
    :ivar ThermalGeneratingUnit: A thermal generating unit may have one
        or more fuel allocation schedules.
    """
    fuelAllocationEndDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuelAllocationStartDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuelType: Optional[FuelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxFuelAllocation: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minFuelAllocation: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FossilFuel: Optional["FossilFuel"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ThermalGeneratingUnit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
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

    :ivar isNetGrossP: Flag is set to true when output is expressed in
        net active power.
    :ivar GeneratingUnit: A generating unit may have one or more cost
        curves, depending upon fuel mixture and fuel cost.
    """
    isNetGrossP: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    GeneratingUnit: Optional["GeneratingUnit"] = field(
        default=None,
        metadata={
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

    :ivar GeneratingUnit: A generating unit may have a gross active
        power to net active power curve, describing the losses and
        auxiliary power requirements of the unit.
    """
    GeneratingUnit: Optional["GeneratingUnit"] = field(
        default=None,
        metadata={
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

    :ivar auxPowerMult: Power output - auxiliary power multiplier
        adjustment factor.
    :ivar auxPowerOffset: Power output - auxiliary power offset
        adjustment factor.
    :ivar heatInputEff: Heat input - efficiency multiplier adjustment
        factor.
    :ivar heatInputOffset: Heat input - offset adjustment factor.
    :ivar isNetGrossP: Flag is set to true when output is expressed in
        net active power.
    :ivar ThermalGeneratingUnit: A thermal generating unit may have a
        heat input curve.
    """
    auxPowerMult: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    auxPowerOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heatInputEff: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    heatInputOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isNetGrossP: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ThermalGeneratingUnit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
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

    :ivar isNetGrossP: Flag is set to true when output is expressed in
        net active power.
    :ivar ThermalGeneratingUnit: A thermal generating unit may have a
        heat rate curve.
    """
    isNetGrossP: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ThermalGeneratingUnit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
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
    coolingSetpoint: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    coolingSystem: Optional[HouseCooling] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    floorArea: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    heatingSetpoint: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    heatingSystem: Optional[HouseHeating] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hvacPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    numberOfStories: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ServicePanel: Optional["EnergyConsumer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ThermostatController: Optional[ThermostatController] = field(
        default=None,
        metadata={
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

    :ivar HydroGeneratingUnit: A hydro generating unit has an efficiency
        curve.
    """
    HydroGeneratingUnit: Optional["HydroGeneratingUnit"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IncidentHazard(Hazard):
    """Hazardous situation associated with an incident.

    Examples are line down, gas leak, fire, etc.

    :ivar TroubleTicket: Trouble ticket associated with this hazard.
    """
    TroubleTicket: Optional["TroubleTicket"] = field(
        default=None,
        metadata={
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

    :ivar isNetGrossP: Flag is set to true when output is expressed in
        net active power.
    :ivar ThermalGeneratingUnit: A thermal generating unit may have an
        incremental heat rate curve.
    """
    isNetGrossP: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ThermalGeneratingUnit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IrregularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them varies.

    :ivar TimePoints: The point data values that define a curve.
    """
    TimePoints: List[IrregularTimePoint] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class LevelVsVolumeCurve(Curve):
    """Relationship between reservoir volume and reservoir level.

    The  volume is at the y-axis and the reservoir level at the x-axis.

    :ivar Reservoir: A reservoir may have a level versus volume
        relationship.
    """
    Reservoir: Optional["Reservoir"] = field(
        default=None,
        metadata={
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

    :ivar SubLoadAreas: The SubLoadAreas in the LoadArea.
    """
    SubLoadAreas: List["SubLoadArea"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


@dataclass
class MeasurementValue(IOPoint):
    """The current state for a measurement.

    A state value is an instance of a measurement from a specific
    source. Measurements can be associated with many state values, each
    representing a different source for the measurement.

    :ivar sensorAccuracy: The limit, expressed as a percentage of the
        sensor maximum, that errors will not exceed when the sensor is
        used under  reference conditions.
    :ivar timeStamp: The time when the value was last updated
    :ivar MeasurementValueQuality: A MeasurementValue has a
        MeasurementValueQuality associated with it.
    :ivar MeasurementValueSource: A reference to the type of source that
        updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc.
        User conventions for the names of sources are contained in the
        introduction to IEC 61970-301.
    :ivar ProcedureDataSet:
    """
    sensorAccuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeasurementValueQuality: Optional[MeasurementValueQuality] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeasurementValueSource: Optional[MeasurementValueSource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ProcedureDataSet: List["ProcedureDataSet"] = field(
        default_factory=list,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    excitingCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    excitingCurrentZero: Optional[float] = field(
        default=None,
        metadata={
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
    lossZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnergisedEnd: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energisedEndVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    openEndStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    openEndVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseShift: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnergisedEnd: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    OpenEnd: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
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
    :ivar OperatingParticipant: The operating participant having this
        share with the associated power system resource.
    :ivar PowerSystemResource: The power system resource to which the
        share applies.
    """
    percentage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OperatingParticipant: Optional[OperatingParticipant] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PowerSystemResource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
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

    :ivar OperationalLimitSet:
    :ivar OperationalLimitType: The limit type associated with this
        limit.
    """
    OperationalLimitSet: Optional["OperationalLimitSet"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    OperationalLimitType: Optional[OperationalLimitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OrganisationRole(IdentifiedObject):
    """
    Identifies a way in which an organisation may participate in the utility
    enterprise (e.g., customer, manufacturer, etc).

    :ivar ConfigurationEvents: All configuration events created for this
        organisation role.
    :ivar Organisation: Organisation having this role.
    """
    ConfigurationEvents: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Organisation: Optional[Organisation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OverfrequencyTripCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OvervoltageTripCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ParallelLineSegment(IdentifiedObject):
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ACLineSegment: Optional["ACLineSegment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    RightOfWay: Optional[RightOfWay] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ParentOrganization(Organisation):
    """
    :ivar Organisation: Organisation that is part of this parent
        organisation.
    """
    Organisation: List["Organisation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PenstockLossCurve(Curve):
    """Relationship between penstock head loss (in meters) and  total discharge
    through the penstock (in cubic meters per second).

    One or more turbines may be connected to the same penstock.

    :ivar HydroGeneratingUnit: A hydro generating unit has a penstock
        loss curve.
    """
    HydroGeneratingUnit: Optional["HydroGeneratingUnit"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PersonRole(IdentifiedObject):
    """
    :ivar Appointments: All appointments for this person.
    :ivar ConfigurationEvents: All configuration events created for this
        person role.
    :ivar Person: Person having this role.
    """
    Appointments: List[Appointment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConfigurationEvents: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Person: Optional[Person] = field(
        default=None,
        metadata={
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
    :ivar timeStamp: Date and time at which the quality code was
        assigned or ascertained.
    :ivar Reading: Reading value to which this quality applies.
    :ivar ReadingQualityType: Type of this reading quality.
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
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Reading: Optional["BaseReading"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReadingQualityType: Optional[ReadingQualityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeStep: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TimePoints: List[RegularTimePoint] = field(
        default_factory=list,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    groundedEndStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    leakageImpedance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    leakageImpedanceZero: Optional[float] = field(
        default=None,
        metadata={
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
    lossZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnergisedEnd: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    GroundedEnds: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
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

    :ivar shutdownCost: Fixed shutdown cost.
    :ivar shutdownDate: The date and time of the most recent generating
        unit shutdown.
    :ivar ThermalGeneratingUnit: A thermal generating unit may have a
        shutdown curve.
    """
    shutdownCost: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shutdownDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ThermalGeneratingUnit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
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

    :ivar ignitionFuelType: Type of ignition fuel.
    :ivar StartupModel: The unit's startup model may have a startup
        ignition fuel curve.
    """
    ignitionFuelType: Optional[FuelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StartupModel: Optional["StartupModel"] = field(
        default=None,
        metadata={
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

    :ivar mainFuelType: Type of main fuel.
    :ivar StartupModel: The unit's startup model may have a startup main
        fuel curve.
    """
    mainFuelType: Optional[FuelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StartupModel: Optional["StartupModel"] = field(
        default=None,
        metadata={
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

    :ivar hotStandbyRamp: The startup ramp rate in gross for a unit that
        is on hot standby.
    :ivar StartupModel: The unit's startup model may have a startup ramp
        curve.
    """
    hotStandbyRamp: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StartupModel: Optional["StartupModel"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SubGeographicalRegion(IdentifiedObject):
    """
    A subset of a geographical region of a power system network model.

    :ivar Lines: The lines within the sub-geographical region.
    :ivar Region: The geographical region to which this sub-geographical
        region is within.
    :ivar Substations: The substations in this sub-geographical region.
    """
    Lines: List["Line"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Region: Optional[GeographicalRegion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Substations: List["Substation"] = field(
        default_factory=list,
        metadata={
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

    :ivar HydroGeneratingUnit: A hydro generating unit has a tailbay
        loss curve.
    """
    HydroGeneratingUnit: Optional["HydroGeneratingUnit"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TargetLevelSchedule(Curve):
    """Reservoir water level targets from advanced studies or "rule curves".

    Typically in one hour increments for up to 10 days.

    :ivar highLevelLimit: High target level limit, above which the
        reservoir operation will be penalized.
    :ivar lowLevelLimit: Low target level limit, below which the
        reservoir operation will be penalized.
    :ivar Reservoir: A reservoir may have a water level target schedule.
    """
    highLevelLimit: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lowLevelLimit: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Reservoir: Optional["Reservoir"] = field(
        default=None,
        metadata={
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

    :ivar endDate: (if tariff became inactive) Date tariff was
        terminated.
    :ivar startDate: Date tariff was activated.
    :ivar PricingStructures: All pricing structures using this tariff.
    """
    endDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PricingStructures: List["PricingStructure"] = field(
        default_factory=list,
        metadata={
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
    :ivar recurrencePattern: Interval at which the scheduled action
        repeats (e.g., first Monday of every month, last day of the
        month, etc.).
    :ivar recurrencePeriod: Duration between time points, from the
        beginning of one period to the beginning of the next period.
        Note that a device like a meter may have multiple interval
        periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min).
    :ivar scheduleInterval: Schedule date and time interval.
    :ivar TimePoints: Sequence of time points belonging to this time
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
    recurrencePattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    recurrencePeriod: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scheduleInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TimePoints: List["TimePoint"] = field(
        default_factory=list,
        metadata={
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
    :ivar StarImpedance: (accurate for 2- or 3-winding transformers
        only) Pi-model impedances of this transformer end. By
        convention, for a two winding transformer, the full values of
        the transformer should be entered on the high voltage end
        (endNumber=1).
    :ivar Terminal: Terminal of the power transformer to which this
        transformer end belongs.
    :ivar ToMeshImpedance: All mesh impedances between this 'from' and
        other 'to' transformer ends.
    """
    endNumber: Optional[int] = field(
        default=None,
        metadata={
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
    BaseVoltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CoreAdmittance: Optional[TransformerCoreAdmittance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FromMeshImpedance: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PhaseTapChanger: Optional["PhaseTapChanger"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RatioTapChanger: Optional["RatioTapChanger"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StarImpedance: Optional[TransformerStarImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ToMeshImpedance: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class UnderfrequencyTripCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class UndervoltageTripCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VoltVarCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VoltWattCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class WattVarCurve(Curve):
    IEEE1547Setting: List["IEEE1547Setting"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AccumulatorLimitSet(LimitSet):
    """
    An AccumulatorLimitSet specifies a set of Limits that are associated with
    an Accumulator measurement.

    :ivar Limits: The limit values used for supervision of Measurements.
    :ivar Measurements: The Measurements using the LimitSet.
    """
    Limits: List[AccumulatorLimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    Measurements: List["Accumulator"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AccumulatorReset(Control):
    """
    This command reset the counter value to zero.

    :ivar AccumulatorValue: The accumulator value that is reset by the
        command.
    """
    AccumulatorValue: Optional["AccumulatorValue"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ActivePowerLimit(OperationalLimit):
    """
    Limit on active power flow.

    :ivar normalValue: The normal value of active power limit.
    :ivar value: Value of active power limit.
    """
    normalValue: Optional[float] = field(
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
class AnalogControl(Control):
    """
    An analog control used for supervisory control.

    :ivar maxValue: Normal value range maximum for any of the
        Control.value. Used for scaling, e.g. in bar graphs.
    :ivar minValue: Normal value range minimum for any of the
        Control.value. Used for scaling, e.g. in bar graphs.
    :ivar AnalogValue: The MeasurementValue that is controlled.
    """
    maxValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AnalogValue: Optional["AnalogValue"] = field(
        default=None,
        metadata={
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

    :ivar Limits: The limit values used for supervision of Measurements.
    :ivar Measurements: The Measurements using the LimitSet.
    """
    Limits: List[AnalogLimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Measurements: List["Analog"] = field(
        default_factory=list,
        metadata={
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

    :ivar calculationDateTime: Timestamp of when the score was
        calculated.
    :ivar effectiveDateTime: Date-time for when the score applies.
    :ivar value: Asset health score value.
    :ivar Analytic:
    :ivar Asset:
    :ivar AssetAggregateScore:
    :ivar AssetGroup:
    """
    calculationDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    effectiveDateTime: Optional[XmlDateTime] = field(
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
    Analytic: Optional["Analytic"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetAggregateScore: Optional["AggregateScore"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetGroup: Optional[AssetGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ApparentPowerLimit(OperationalLimit):
    """
    Apparent power limit.

    :ivar normalValue: The normal apparent power limit.
    :ivar value: The apparent power limit.
    """
    normalValue: Optional[float] = field(
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
class AssetOrganisationRole(OrganisationRole):
    """
    Role an organisation plays with respect to asset.

    :ivar Assets: All assets for this organisation role.
    """
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
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
    :ivar maxCoverage: The maximum percentage coverage
    :ivar minCoverage: The minimum percentage coverage
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
    maxCoverage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minCoverage: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar reportedDateTime: (used only when there are detailed auditing
        requirements) Date and time at which the reading was first
        delivered to the metering system.
    :ivar source: System that originally supplied the reading (e.g.,
        customer, AMI system, handheld reading system, another
        enterprise system, etc.).
    :ivar value: Value of this reading.
    :ivar ReadingQualities: All qualities of this reading.
    :ivar timePeriod: Start and end of the period for those readings
        whose type has a time attribute such as 'billing', seasonal' or
        'forTheSpecifiedPeriod'.
    """
    reportedDateTime: Optional[XmlDateTime] = field(
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
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReadingQualities: List[ReadingQuality] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timePeriod: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar NetworkAssetDeployment: A network asset deployment at this
        base voltage level.
    :ivar TopologicalNode: The topological nodes at the base voltage.
    :ivar TransformerEnds: Transformer ends at the base voltage.  This
        is essential for PU calculation.
    :ivar VoltageLevel: The voltage levels having this base voltage.
    """
    nominalVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConductingEquipment: List["ConductingEquipment"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NetworkAssetDeployment: List[AssetDeployment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TopologicalNode: List["TopologicalNode"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerEnds: List[TransformerEnd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    VoltageLevel: List["VoltageLevel"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CurrentLimit(OperationalLimit):
    """
    Operational limit on current.

    :ivar normalValue: The normal value for limit on current flow.
    :ivar value: Limit on current flow.
    """
    normalValue: Optional[float] = field(
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
class DocumentPersonRole(PersonRole):
    """
    Person role with respect to documents.
    """


@dataclass
class EnvironmentalDataProvider(OrganisationRole):
    """Entity providing environmental data.

    Could be an observed weather data provider, an entity providing
    forecasts, an authority providing alerts, etc.

    :ivar EnvironmentalAlert: Alert issued by this environmental data
        provider.
    :ivar EnvironmentalInformation: Environmental information provided
        by this environmental data provider.
    """
    EnvironmentalAlert: List["EnvironmentalAlert"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalInformation: List["EnvironmentalInformation"] = field(
        default_factory=list,
        metadata={
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
    :ivar EnvironmentalAlert: Environmental alert applying to location
        of this type.
    :ivar EnvironmentalPhenomenon: Environmental phenomenon for which
        this location is of relevance.
    :ivar Location: Location of this instance of ths kind of
        environmental location.
    """
    kind: Optional[LocationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalAlert: List["EnvironmentalAlert"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalPhenomenon: List[EnvironmentalPhenomenon] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Location: Optional["Location"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FossilFuel(IdentifiedObject):
    """The fossil fuel consumed by the non-nuclear thermal generating unit.

    For example, coal, oil, gas, etc.   This a the specific fuels that
    the generating unit can consume.

    :ivar fossilFuelType: The type of fossil fuel, such as coal, oil, or
        gas.
    :ivar fuelCost: The cost in terms of heat value for the given type
        of fuel.
    :ivar fuelDispatchCost: The cost of fuel used for economic
        dispatching which includes: fuel cost, transportation cost,  and
        incremental maintenance cost.
    :ivar fuelEffFactor: The efficiency factor for the fuel (per unit)
        in terms of the effective energy absorbed.
    :ivar fuelHandlingCost: Handling and processing cost associated with
        this fuel.
    :ivar fuelHeatContent: The amount of heat per weight (or volume) of
        the given type of fuel.
    :ivar fuelMixture: Relative amount of the given type of fuel, when
        multiple fuels are being consumed.
    :ivar fuelSulfur: The fuel's fraction of pollution credit per unit
        of heat content.
    :ivar highBreakpointP: The active power output level of the unit at
        which the given type of fuel is switched on. This fuel (e.g.,
        oil) is sometimes used to supplement the base fuel (e.g., coal)
        at high active power output levels.
    :ivar lowBreakpointP: The active power output level of the unit at
        which the given type of fuel is switched off. This fuel (e.g.,
        oil) is sometimes used to stabilize the base fuel (e.g., coal)
        at low active power output levels.
    :ivar FuelAllocationSchedules: A fuel allocation schedule must have
        a fossil fuel.
    :ivar ThermalGeneratingUnit: A thermal generating unit may have one
        or more fossil fuels.
    """
    fossilFuelType: Optional[FuelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuelCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuelDispatchCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuelEffFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuelHandlingCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuelHeatContent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuelMixture: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fuelSulfur: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    highBreakpointP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lowBreakpointP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FuelAllocationSchedules: List[FuelAllocationSchedule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ThermalGeneratingUnit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
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

    :ivar GeneratingUnit: A generating unit may have an operating
        schedule, indicating the planned operation of the unit.
    """
    GeneratingUnit: Optional["GeneratingUnit"] = field(
        default=None,
        metadata={
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

    :ivar HydroPump: The hydro pump has a pumping schedule over time,
        indicating when pumping is to occur.
    """
    HydroPump: Optional["HydroPump"] = field(
        default=None,
        metadata={
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
class IEEE1547Setting:
    constantPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    constantReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceIntentionalDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceMaxFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceMaxVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceMinFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceMinVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    frequencyDroopResponseTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    islandClearingTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    openLoopResponseTimeP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeConstantOpenLoop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeConstantReferenceVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    underFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    underFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OverfrequencyTripCurve: Optional[OverfrequencyTripCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OvervoltageTripCurve: Optional[OvervoltageTripCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerElectronicsConnections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RotatingMachines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UnderfrequencyTripCurve: Optional[UnderfrequencyTripCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UndervoltageTripCurve: Optional[UndervoltageTripCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    VoltVarCurve: Optional[VoltVarCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    VoltWattCurve: Optional[VoltWattCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WattVarCurve: Optional[WattVarCurve] = field(
        default=None,
        metadata={
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

    :ivar Reservoir: A reservoir may have a "natural" inflow forecast.
    """
    Reservoir: Optional["Reservoir"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class LineFault(Fault):
    """
    A fault that occurs on an AC line segment at some point along the length.

    :ivar lengthFromTerminal1: The length to the place where the fault
        is located starting from terminal with sequence number 1 of the
        faulted line segment.
    :ivar ACLineSegment: The line segment of this line fault.
    """
    lengthFromTerminal1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ACLineSegment: Optional["ACLineSegment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Manufacturer(OrganisationRole):
    """
    Organisation that manufactures asset products.

    :ivar ProductAssetModels: All asset models by this manufacturer.
    """
    ProductAssetModels: List["ProductAssetModel"] = field(
        default_factory=list,
        metadata={
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

    :ivar ConnectivityNode:
    :ivar Equipment: The equipment to which the limit set applies.
    :ivar OperationalLimitValue:
    :ivar Terminal:
    """
    ConnectivityNode: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Equipment: Optional["Equipment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OperationalLimitValue: List[OperationalLimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Terminal: Optional["ACDCTerminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PerLengthPhaseImpedance(PerLengthImpedance):
    """
    Impedance and admittance parameters per unit length for n-wire unbalanced
    lines, in matrix form.

    :ivar conductorCount: Number of phase, neutral, and other wires
        retained. Constrains the number of matrix elements and the phase
        codes that can be used with this matrix.
    :ivar PhaseImpedanceData: All data that belong to this conductor
        phase impedance.
    """
    conductorCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PhaseImpedanceData: List[PhaseImpedanceData] = field(
        default_factory=list,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseAngleClock: Optional[int] = field(
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
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerTransformer: Optional["PowerTransformer"] = field(
        default=None,
        metadata={
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
    :ivar dailyCeilingUsage: Absolute maximum valid non-demand usage
        quantity used in validating a customer's billed non-demand
        usage.
    :ivar dailyEstimatedUsage: Used in place of actual computed
        estimated average when history of usage is not available, and
        typically manually entered by customer accounting.
    :ivar dailyFloorUsage: Absolute minimum valid non-demand usage
        quantity used in validating a customer's billed non-demand
        usage.
    :ivar revenueKind: (accounting) Kind of revenue, often used to
        determine the grace period allowed, before collection actions
        are taken on a customer (grace periods vary between revenue
        classes).
    :ivar taxExemption: True if this pricing structure is not taxable.
    :ivar CustomerAgreements: All customer agreements with this pricing
        structure.
    :ivar ServiceCategory: Service category to which this pricing
        structure applies.
    :ivar Tariffs: All tariffs used by this pricing structure.
    :ivar UsagePoints: All service delivery points (with prepayment
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
    dailyCeilingUsage: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dailyEstimatedUsage: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    dailyFloorUsage: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    revenueKind: Optional[RevenueKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    taxExemption: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CustomerAgreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ServiceCategory: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Tariffs: List[Tariff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
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

    :ivar completedDateTime: Date and time procedure was completed.
    :ivar Asset: Asset to which this procedure data set applies.
    :ivar MeasurementValue:
    :ivar Procedure: Procedure capturing this data set.
    :ivar Properties: UserAttributes used to specify further properties
        of this procedure data set. Use 'name' to specify what kind of
        property it is, and 'value.value' attribute for the actual
        value.
    """
    completedDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeasurementValue: List[MeasurementValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Procedure: Optional["Procedure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Properties: List[UserAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Register(IdentifiedObject):
    """
    A device that indicates or records units of the commodity or other quantity
    measured.

    :ivar isVirtual: If true, the data it produces is  calculated or
        measured by a device other than a physical end device/meter.
        Otherwise, any data streams it produces are measured by the
        hardware of the end device/meter itself.
    :ivar leftDigitCount: Number of digits (dials on a mechanical meter)
        to the left of the decimal place; default is normally 5.
    :ivar rightDigitCount: Number of digits (dials on a mechanical
        meter) to the right of the decimal place.
    :ivar touTierName: Name used for the time of use tier (also known as
        bin or bucket).  For example, "peak", "off-peak", "TOU Category
        A", etc.
    :ivar Channels: All channels that collect/report values from this
        register.
    :ivar EndDeviceFunction: End device function metering quantities
        displayed by this register.
    :ivar touTier: Clock time interval for register to beging/cease
        accumulating time of usage (e.g., start at 8:00 am, stop at 5:00
        pm).
    """
    isVirtual: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    leftDigitCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rightDigitCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    touTierName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Channels: List["Channel"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceFunction: Optional[EndDeviceFunction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    touTier: Optional[TimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Season: Optional[Season] = field(
        default=None,
        metadata={
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

    :ivar fixedMaintCost: Fixed maintenance cost.
    :ivar hotStandbyHeat: The amount of heat input per time uint
        required for hot standby operation.
    :ivar incrementalMaintCost: Incremental maintenance cost.
    :ivar minimumDownTime: The minimum number of hours the unit must be
        down before restart.
    :ivar minimumRunTime: The minimum number of hours the unit must be
        operating before being allowed to shut down.
    :ivar riskFactorCost: The opportunity cost associated with the
        return in monetary unit. This represents the restart's "share"
        of the unit depreciation and risk of an event which would damage
        the unit.
    :ivar startupCost: Total miscellaneous start up costs.
    :ivar startupDate: The date and time of the most recent generating
        unit startup.
    :ivar startupPriority: Startup priority within control area where
        lower numbers indicate higher priorities.  More than one unit in
        an area may be assigned the same priority.
    :ivar stbyAuxP: The unit's auxiliary active power consumption to
        maintain standby mode.
    :ivar StartIgnFuelCurve: The unit's startup model may have a startup
        ignition fuel curve.
    :ivar StartMainFuelCurve: The unit's startup model may have a
        startup main fuel curve.
    :ivar StartRampCurve: The unit's startup model may have a startup
        ramp curve.
    :ivar ThermalGeneratingUnit: A thermal generating unit may have a
        startup model.
    """
    fixedMaintCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hotStandbyHeat: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    incrementalMaintCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimumDownTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimumRunTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    riskFactorCost: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startupCost: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startupDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    startupPriority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    stbyAuxP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StartIgnFuelCurve: Optional[StartIgnFuelCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StartMainFuelCurve: Optional[StartMainFuelCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StartRampCurve: Optional[StartRampCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ThermalGeneratingUnit: Optional["ThermalGeneratingUnit"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SteamSendoutSchedule(RegularIntervalSchedule):
    """
    The cogeneration plant's steam sendout schedule in volume per time unit.

    :ivar CogenerationPlant: A cogeneration plant has a steam sendout
        schedule.
    """
    CogenerationPlant: Optional["CogenerationPlant"] = field(
        default=None,
        metadata={
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
    :ivar StringMeasurement: Measurement to which this value is
        connected.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StringMeasurement: Optional["StringMeasurement"] = field(
        default=None,
        metadata={
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

    :ivar LoadArea: The LoadArea where the SubLoadArea belongs.
    :ivar LoadGroups: The Loadgroups in the SubLoadArea.
    """
    LoadArea: Optional[LoadArea] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    LoadGroups: List["LoadGroup"] = field(
        default_factory=list,
        metadata={
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

    :ivar dateTime: Absolute date and time for this time point. For
        calendar-based time point, it is typically manually entered,
        while for interval-based or sequence-based time point it is
        derived.
    :ivar relativeTimeInterval: (if interval-based) A point in time
        relative to scheduled start time in
        'TimeSchedule.scheduleInterval.start'.
    :ivar sequenceNumber: (if sequence-based) Relative sequence number
        for this time point.
    :ivar status: Status of this time point.
    :ivar TimeSchedule: Time schedule owning this time point.
    :ivar window: Interval defining the window of time that this time
        point is valid (for example, seasonal, only on weekends, not on
        weekends, only 8:00 am to 5:00 pm, etc.).
    """
    dateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    relativeTimeInterval: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequenceNumber: Optional[int] = field(
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
    TimeSchedule: Optional[TimeSchedule] = field(
        default=None,
        metadata={
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
    :ivar TransformerTank: Transformer this winding belongs to.
    """
    phases: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerTank: Optional["TransformerTank"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class TroubleTicket(Document):
    """
    :ivar dateTimeOfReport: Date and time the trouble has been reported.
    :ivar firstResponderStatus: Indicates whether the first responder
        such as police, fire department etc.has been notified and
        whether they are on site or en route.
    :ivar multiplePremises: Set to true if the outage report indicated
        that other neighbors are also out of power.
    :ivar reportingKind: Indicates how the customer reported trouble.
    :ivar resolvedDateTime: Date and time this trouble ticket has been
        resolved.
    :ivar troubleCode: Trouble code (e.g., power down, flickering
        lights, partial power, etc).
    :ivar troubleKind:
    :ivar Customer: Customer for whom this trouble ticket is relevant.
    :ivar IncidentHazard: All hazards reported with this trouble ticket.
    :ivar Notification: Notification for this trouble ticket.
    :ivar ServiceLocation:
    """
    dateTimeOfReport: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    firstResponderStatus: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    multiplePremises: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reportingKind: Optional[TroubleReportingKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    resolvedDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    troubleCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    troubleKind: Optional[PNNLTroubleCallKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Customer: Optional["Customer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IncidentHazard: List[IncidentHazard] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Notification: Optional["CustomerNotification"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ServiceLocation: Optional[ServiceLocation] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DemandResponsePrograms: List["DemandResponseProgram"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceControls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class VoltageLimit(OperationalLimit):
    """
    Operational limit applied to voltage.

    :ivar normalValue: The normal limit on voltage. High or low limit
        nature of the limit depends upon the properties of the
        operational limit type.
    :ivar value: Limit on voltage. High or low limit nature of the limit
        depends upon the properties of the operational limit type.
    """
    normalValue: Optional[float] = field(
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
class AccumulatorValue(MeasurementValue):
    """
    AccumulatorValue represents an accumulated (counted) MeasurementValue.

    :ivar value: The value to supervise. The value is positive.
    :ivar Accumulator: Measurement to which this value is connected.
    :ivar AccumulatorReset: The command that reset the accumulator
        value.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Accumulator: Optional["Accumulator"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AccumulatorReset: Optional[AccumulatorReset] = field(
        default=None,
        metadata={
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
    AnalyticScore: List["AnalyticScore"] = field(
        default_factory=list,
        metadata={
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
    :ivar Analog: Measurement to which this value is connected.
    :ivar AnalogControl: The Control variable associated with the
        MeasurementValue.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Analog: Optional["Analog"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AnalogControl: Optional[AnalogControl] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Approver(DocumentPersonRole):
    """
    Person who accepted/signed or rejected the document.

    :ivar Documents: All documents for this approver.
    """
    Documents: List["Document"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetOwner(AssetOrganisationRole):
    """
    Owner of the asset.

    :ivar Ownerships: All ownerships of this owner.
    """
    Ownerships: List["Ownership"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetTestSampleTaker(AssetOrganisationRole):
    """
    :ivar Specimen: Specimen taken by this sample taker.
    """
    Specimen: List["Specimen"] = field(
        default_factory=list,
        metadata={
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

    :ivar ActivityRecords: All activity records with this author.
    :ivar Documents: All documents of this this author.
    """
    ActivityRecords: List["ActivityRecord"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Documents: List[Document] = field(
        default_factory=list,
        metadata={
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

    :ivar isVirtual: If true, the data is being calculated by an
        enterprise system rather than metered directly.
    :ivar ReadingType: Reading type for register values
        reported/collected by this channel.
    :ivar Register: Register whose values are collected/reported by this
        channel.
    """
    isVirtual: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReadingType: Optional["ReadingType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Register: Optional[Register] = field(
        default=None,
        metadata={
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

    :ivar ConformLoadGroup: The ConformLoadGroup where the
        ConformLoadSchedule belongs.
    """
    ConformLoadGroup: Optional["ConformLoadGroup"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class CrewMember(OperationPersonRole):
    """
    Member of a crew.

    :ivar Crew: Crew to which this crew member belongs.
    """
    Crew: Optional["Crew"] = field(
        default=None,
        metadata={
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

    :ivar contactType: Type of contact (e.g., phone, email, etc.).
    :ivar contactValue: Value of contact type (e.g., phone number, email
        address, etc.).
    :ivar earliestDateTimeToCall: Earliest date time to call the
        customer.
    :ivar latestDateTimeToCall: Latest date time to call the customer.
    :ivar trigger: Trigger for this notification.
    :ivar Customer: Customer requiring this notification.
    :ivar TroubleTickets: All trouble tickets with this notification.
    """
    contactType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    contactValue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    earliestDateTimeToCall: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    latestDateTimeToCall: Optional[XmlDateTime] = field(
        default=None,
        metadata={
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
    Customer: Optional["Customer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TroubleTickets: List[TroubleTicket] = field(
        default_factory=list,
        metadata={
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

    :ivar centralPressure: The central pressure of the cyclone during
        the time interval.
    :ivar maxSurfaceWindSpeed: The maximum surface wind speed of the
        cyclone during the time interval.
    :ivar windForce: Wind Force as classified on the Beaufort Scale
        (0-12) during the time interval.
    """
    centralPressure: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxSurfaceWindSpeed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    windForce: Optional[int] = field(
        default=None,
        metadata={
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
    :ivar CustomerAgreements: All customer agreements through which the
        customer is enrolled in this demand response program.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CustomerAgreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceGroups: List["EndDeviceGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePointGroups: List[UsagePointGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    validityInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
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
    :ivar failureMode: Failuer mode, for example: Failure to Insulate;
        Failure to conduct; Failure to contain oil; Failure to provide
        ground plane; Other.
    :ivar finalCause: Cause of problem determined during diagnosis.
    :ivar finalCode: Code for diagnosed probem type.
    :ivar finalOrigin: Origin of problem determined during diagnosis.
    :ivar finalRemark: Remarks pertaining to findings during problem
        diagnosis.
    :ivar phaseCode: Phase(s) diagnosed.
    :ivar preliminaryCode: Code for problem type determined during
        preliminary assessment.
    :ivar preliminaryDateTime: Date and time preliminary assessment of
        problem was performed.
    :ivar preliminaryRemark: Remarks pertaining to preliminary
        assessment of problem.
    :ivar rootCause: Root cause of problem determined during diagnosis.
    :ivar rootOrigin: Root origin of problem determined during
        diagnosis.
    :ivar rootRemark: Remarks pertaining to root cause findings during
        problem diagnosis.
    """
    effect: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failureMode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    finalCause: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    finalCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    finalOrigin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    finalRemark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseCode: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    preliminaryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    preliminaryDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    preliminaryRemark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rootCause: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rootOrigin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rootRemark: Optional[str] = field(
        default=None,
        metadata={
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
    :ivar focalDepth: The depth below the earth's surface of the
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
    focalDepth: Optional[RelativeDisplacement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Editor(DocumentPersonRole):
    """
    Person who modified the document.

    :ivar Documents: All documents for this editor.
    """
    Documents: List["Document"] = field(
        default_factory=list,
        metadata={
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

    :ivar coverageKind: Code representing the coverage of the weather
        condition during the time interval.
    :ivar intensityKind: Code representing the intensity of the weather
        condition during the time interval.
    :ivar probabilityPercent: Probability of weather condition occurring
        during the time interval expressed as a percentage. Applicable
        only when weather condition is related to a forecast (not an
        observation).
    :ivar weatherKind: Code representing the type of weather condition
        during the time interval.
    """
    coverageKind: Optional[CoverageCodeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    intensityKind: Optional[IntensityCodeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    probabilityPercent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    weatherKind: Optional[WeatherCodeKind] = field(
        default=None,
        metadata={
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

    :ivar locationCondition: Description of the conditions of the
        location where the asset resides.
    :ivar AccordingToSchedules:
    """
    locationCondition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AccordingToSchedules: List["ScheduledEventData"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class IntervalReading(BaseReading):
    """Data captured at regular intervals of time.

    Interval data could be captured as incremental data, absolute data, or relative data. The source for the data is usually a tariff quantity or an engineering quantity. Data is typically captured in time-tagged, uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min.
    Note: Interval Data is sometimes also called "Interval Data Readings" (IDR).

    :ivar IntervalBlocks: All blocks containing this interval reading.
    """
    IntervalBlocks: List["IntervalBlock"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Issuer(DocumentPersonRole):
    """
    Person who issued the document and is responsible for its content.

    :ivar Documents: All documents for this issuer.
    """
    Documents: List["Document"] = field(
        default_factory=list,
        metadata={
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

    :ivar errorEllipseConfidence: Likelihood that strike fell within
        errorEllipse.
    :ivar errorEllipseMajorSemiAxis: Length of major semi-axis (longest
        radius) of the error ellipse.
    :ivar errorEllipseMinorSemiAxis: Length of minor semi-axis (shortest
        radius) of the error ellipse.
    :ivar errorEllipseOrientation: The orientation of the major semi-
        axis in degrees from True North.
    :ivar negativePolarity: The polarity of the strike, with T meaning
        negative. About 90% of all lightning strokes are negative
        strokes, meaning that they were initiated by a large
        concentration of negative charge in the cloud-base; this tends
        to induce an area of positive charge on the ground.
    :ivar peakAmplitude: Peak current of strike.
    """
    errorEllipseConfidence: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    errorEllipseMajorSemiAxis: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    errorEllipseMinorSemiAxis: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    errorEllipseOrientation: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    negativePolarity: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    peakAmplitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class LoadGroup(IdentifiedObject):
    """
    The class is the third level in a hierarchical structure for grouping of
    loads for the purpose of load flow load scaling.

    :ivar SubLoadArea: The SubLoadArea where the Loadgroup belongs.
    """
    SubLoadArea: Optional[SubLoadArea] = field(
        default=None,
        metadata={
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

    :ivar changeDst: Change in the disturbance  - storm time (Dst)
        index. The size of a geomagnetic storm is classified as: -
        moderate ( -50 nT &amp;gt;minimum of Dst &amp;gt; -100 nT) -
        intense (-100 nT &amp;gt; minimum Dst &amp;gt; -250 nT) or -
        super-storm ( minimum of Dst &amp;lt; -250 nT).
    """
    changeDst: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar conditionAfter: Condition of asset just following maintenance
        procedure.
    :ivar conditionBefore: Description of the condition of the asset
        just prior to maintenance being performed.
    :ivar maintCode: Code for the type of maintenance performed.
    """
    conditionAfter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    conditionBefore: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maintCode: Optional[str] = field(
        default=None,
        metadata={
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

    :ivar NonConformLoadGroup: The NonConformLoadGroup where the
        NonConformLoadSchedule belongs.
    """
    NonConformLoadGroup: Optional["NonConformLoadGroup"] = field(
        default=None,
        metadata={
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
    :ivar sequenceNumber: Sequence number in a sequence of procedures
        being performed.
    :ivar Assets: All assets to which this procedure applies.
    :ivar Limits:
    :ivar Measurements: Document containing this measurement.
    :ivar ProcedureDataSets: All data sets captured by this procedure.
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
    sequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Limits: List[Limit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Measurements: List["Measurement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ProcedureDataSets: List[ProcedureDataSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ProductAssetModel(IdentifiedObject):
    """
    Asset model by a specific manufacturer.

    :ivar catalogueNumber: Catalogue number for asset model.
    :ivar corporateStandardKind: Kind of corporate standard for this
        asset model.
    :ivar drawingNumber: Drawing number for asset model.
    :ivar instructionManual: Reference manual or instruction book for
        this asset model.
    :ivar modelNumber: Manufacturer's model number.
    :ivar modelVersion: Version number for product model, which
        indicates vintage of the product.
    :ivar overallLength: Overall length of this asset model.
    :ivar styleNumber: Style number of asset model.
    :ivar usageKind: Intended usage for this asset model.
    :ivar Asset: An asset of this model.
    :ivar AssetInfo:
    :ivar CatalogAssetType:
    :ivar Manufacturer: Manufacturer of this asset model.
    """
    catalogueNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    corporateStandardKind: Optional[CorporateStandardKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    drawingNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    instructionManual: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    modelNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    modelVersion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overallLength: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    styleNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    usageKind: Optional[AssetModelUsageKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetInfo: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CatalogAssetType: Optional[CatalogAssetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Manufacturer: Optional[Manufacturer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class RaiseLowerCommand(AnalogControl):
    """An analog control that increase or decrease a set point value with
    pulses.

    Unless otherwise specified, one pulse moves the set point by one.

    :ivar ValueAliasSet: The ValueAliasSet used for translation of a
        Control value to a name.
    """
    ValueAliasSet: Optional["ValueAliasSet"] = field(
        default=None,
        metadata={
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
    :ivar MeterReadings: All meter readings (sets of values) containing
        this reading value.
    :ivar ReadingType: Type information for this reading value.
    """
    reason: Optional[ReadingReasonKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeterReadings: List["MeterReading"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReadingType: Optional["ReadingType"] = field(
        default=None,
        metadata={
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

    :ivar RegulatingControl: Regulating controls that have this
        Schedule.
    :ivar VoltageControlZones: A VoltageControlZone may have a  voltage
        regulation schedule.
    """
    RegulatingControl: Optional["RegulatingControl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    VoltageControlZones: List["VoltageControlZone"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class SetPoint(AnalogControl):
    """
    An analog control that issue a set point value.

    :ivar normalValue: Normal value for Control.value e.g. used for
        percentage scaling.
    :ivar value: The value representing the actuator output.
    """
    normalValue: Optional[float] = field(
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
class SwitchSchedule(SeasonDayTypeSchedule):
    """A schedule of switch positions.

    If RegularTimePoint.value1 is 0, the switch is open.  If 1, the
    switch is closed.

    :ivar Switch: A SwitchSchedule is associated with a Switch.
    """
    Switch: Optional["Switch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TestDataSet(ProcedureDataSet):
    """
    Test results, usually obtained by a lab or other independent organisation.

    :ivar conclusion: Conclusion drawn from test results.
    :ivar specimenID: Identifier of specimen used in inspection or test.
    :ivar specimenToLabDateTime: Date and time the specimen was received
        by the lab.
    """
    conclusion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimenID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimenToLabDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
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

    :ivar pInjection: The active power injected into the bus at this
        location in addition to injections from equipment.  Positive
        sign means injection into the TopologicalNode (bus). Starting
        value for a steady state solution.
    :ivar qInjection: The reactive power injected into the bus at this
        location in addition to injections from equipment. Positive sign
        means injection into the TopologicalNode (bus). Starting value
        for a steady state solution.
    :ivar AngleRefTopologicalIsland: The island for which the node is an
        angle reference.   Normally there is one angle reference node
        for each island.
    :ivar BaseVoltage: The base voltage of the topologocial node.
    :ivar BusNameMarker: BusnameMarkers that may refer to a pre defined
        TopologicalNode.
    :ivar ConnectivityNodeContainer: The connectivity node container to
        which the toplogical node belongs.
    :ivar ConnectivityNodes: The connectivity nodes combine together to
        form this topological node.  May depend on the current state of
        switches in the network.
    :ivar ReportingGroup: The reporting group to which the topological
        node belongs.
    :ivar SvInjection: The injection flows state variables associated
        with the topological node.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    qInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AngleRefTopologicalIsland: Optional[TopologicalIsland] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    BaseVoltage: Optional[BaseVoltage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    BusNameMarker: List["BusNameMarker"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConnectivityNodeContainer: Optional["ConnectivityNodeContainer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConnectivityNodes: List["ConnectivityNode"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReportingGroup: Optional["ReportingGroup"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvInjection: List["SvInjection"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvVoltage: List[SvVoltage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Terminal: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TopologicalIsland: Optional[TopologicalIsland] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Tornado(AtmosphericPhenomenon):
    """
    A tornado, a violent destructive whirling wind accompanied by a funnel-
    shaped cloud that progresses in a narrow path over the land.

    :ivar fScale: Fujita scale (referred to as EF-scale starting in
        2007) for the tornado.
    :ivar width: Width of the tornado during the time interval.
    """
    fScale: Optional[FScale] = field(
        default=None,
        metadata={
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
    :ivar particleSize: The diameter of the particles during the time
        interval.
    """
    density: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    particleSize: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar createdDateTime: Date and time this activity record has been
        created (different from the 'status.dateTime', which is the time
        of a status change of the associated object, if applicable).
    :ivar reason: Reason for event resulting in this activity record,
        typically supplied when user initiated.
    :ivar severity: Severity level of event resulting in this activity
        record.
    :ivar type: Type of event resulting in this activity record.
    :ivar Assets: All assets for which this activity record has been
        created.
    :ivar Author: Author of this activity record.
    :ivar status: Information on consequence of event resulting in this
        activity record.
    """
    createdDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
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
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Author: Optional[Author] = field(
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
class ConformLoadGroup(LoadGroup):
    """
    A group of loads conforming to an allocation pattern.

    :ivar ConformLoadSchedules: The ConformLoadSchedules in the
        ConformLoadGroup.
    :ivar EnergyConsumers: Conform loads assigned to this
        ConformLoadGroup.
    """
    ConformLoadSchedules: List[ConformLoadSchedule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    EnergyConsumers: List["ConformLoad"] = field(
        default_factory=list,
        metadata={
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
    :ivar pucNumber: (if applicable) Public utilities commission (PUC)
        identification number.
    :ivar specialNeed: True if customer organisation has special service
        needs such as life support, hospitals, etc.
    :ivar vip: (use 'priority' instead) True if this is an important
        customer. Importance is for matters different than those in
        'specialNeed' attribute.
    :ivar CustomerAccounts: All accounts of this customer.
    :ivar CustomerAgreements: All agreements of this customer.
    :ivar CustomerNotifications: All notifications required by this
        customer.
    :ivar EndDevices: All end devices of this customer.
    :ivar priority: Priority of the customer.
    :ivar status: Status of this customer.
    :ivar TroubleTickets: All trouble tickets for this customer.
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
    pucNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specialNeed: Optional[str] = field(
        default=None,
        metadata={
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
    CustomerAccounts: List[CustomerAccount] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CustomerAgreements: List["CustomerAgreement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CustomerNotifications: List[CustomerNotification] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDevices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
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
    TroubleTickets: List[TroubleTicket] = field(
        default_factory=list,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DemandResponsePrograms: List[DemandResponseProgram] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DERFunction: Optional[DERFunction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DERGroupDispatch: List[DERGroupDispatch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DERGroupForecast: List[DERGroupForecast] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    DERMonitorableParameter: List[DERMonitorableParameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DispatchablePowerCapability: Optional["DispatchablePowerCapability"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceControls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDevices: List["EndDevice"] = field(
        default_factory=list,
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
    :ivar Procedures: Measurements are specified in types of documents,
        such as procedures.
    :ivar Terminal: One or more measurements may be associated with a
        terminal in the network.
    """
    measurementType: Optional[str] = field(
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
    Asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Locations: List["Location"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerSystemResource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Procedures: List[Procedure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Terminal: Optional["ACDCTerminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class NonConformLoadGroup(LoadGroup):
    """
    Loads that do not follow a daily and seasonal load variation pattern.

    :ivar EnergyConsumers: Conform loads assigned to this
        ConformLoadGroup.
    :ivar NonConformLoadSchedules: The NonConformLoadSchedules in the
        NonConformLoadGroup.
    """
    EnergyConsumers: List["NonConformLoad"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NonConformLoadSchedules: List[NonConformLoadSchedule] = field(
        default_factory=list,
        metadata={
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
    :ivar Asset: Asset that is object of this ownership.
    :ivar AssetOwner: Asset owner that is subject in this ownership.
    """
    share: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetOwner: Optional[AssetOwner] = field(
        default=None,
        metadata={
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
    :ivar consumptionTier: In case of common flat-rate pricing for
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
    :ivar flowDirection: Flow direction for a reading where the
        direction of flow of the commodity is important (for electricity
        measurements this includes current, energy, power, and demand).
    :ivar macroPeriod: Time period of interest that reflects how the
        reading is viewed or captured over a long period of time.
    :ivar measurementKind: Identifies "what" is being measured, as
        refinement of 'commodity'. When combined with 'unit', it
        provides detail to the unit of measure. For example, 'energy'
        with a unit of measure of 'kWh' indicates to the user that
        active energy is being measured, while with 'kVAh' or 'kVArh',
        it indicates apparent energy and reactive energy, respectively.
        'power' can be combined in a similar way with various power
        units of measure: Distortion power ('distortionVoltAmperes')
        with 'kVA' is different from 'power' with 'kVA'.
    :ivar measuringPeriod: Time attribute inherent or fundamental to the
        reading value (as opposed to 'macroPeriod' that supplies an
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
    :ivar Channel: Channel reporting/collecting register values with
        this type information.
    :ivar interharmonic: Indication of a "harmonic" or "interharmonic"
        basis for the measurement. Value 0 in 'numerator' and
        'denominator' means not applicable.
    :ivar IntervalBlocks: All blocks containing interval reading values
        with this type information.
    :ivar MetrologyRequirements: All metrology requirements that require
        this reading type to be collected.
    :ivar PendingCalculation: Pending calculation that produced this
        reading type.
    :ivar Readings: All reading values with this type information.
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
    consumptionTier: Optional[int] = field(
        default=None,
        metadata={
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
    flowDirection: Optional[FlowDirectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    macroPeriod: Optional[MacroPeriodKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measurementKind: Optional[MeasurementKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    measuringPeriod: Optional[MeasuringPeriodKind] = field(
        default=None,
        metadata={
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
    Channel: Optional[Channel] = field(
        default=None,
        metadata={
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
    IntervalBlocks: List["IntervalBlock"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MetrologyRequirements: List[MetrologyRequirement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PendingCalculation: Optional["PendingCalculation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Readings: List[Reading] = field(
        default_factory=list,
        metadata={
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
    :ivar AssetHealthScore: Individual health score associated with this
        risk score.
    """
    kind: Optional[RiskScoreKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetHealthScore: List["HealthScore"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ScheduledEventData:
    """
    Schedule parameters for an activity that is to occur, is occurring, or has
    completed.

    :ivar estimatedWindow: Estimated date and time for activity
        execution (with earliest possibility of activity initiation and
        latest possibility of activity completion).
    :ivar InspectionDataSet:
    :ivar requestedWindow: Requested date and time interval for activity
        execution.
    :ivar ScheduledEvents: All scheduled events with this specification.
    :ivar status:
    """
    estimatedWindow: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    InspectionDataSet: Optional[InspectionDataSet] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    requestedWindow: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ScheduledEvents: List["ScheduledEvent"] = field(
        default_factory=list,
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
class Specimen(IdentifiedObject):
    """
    Sample or specimen of a material (fluid or solid).

    :ivar ambientTemperatureAtSampling: Operating ambient temperature
        (in ï¿½C).
    :ivar humidityAtSampling: Operating ambient humidity (in percent).
    :ivar specimenID: Identifier of specimen used in inspection or test.
    :ivar specimenSampleDateTime: Date and time sample specimen taken.
    :ivar specimenToLabDateTime: Date and time the specimen was received
        by the lab.
    :ivar AssetTestSampleTaker: Test sampler taker who gathered this
        specimen.
    :ivar LabTestDataSet: Results from lab testing done on specimen.
    """
    ambientTemperatureAtSampling: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    humidityAtSampling: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimenID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimenSampleDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    specimenToLabDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetTestSampleTaker: Optional[AssetTestSampleTaker] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    LabTestDataSet: List["LabTestDataSet"] = field(
        default_factory=list,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    qInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConnectivityNode: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TopologicalNode: Optional[TopologicalNode] = field(
        default=None,
        metadata={
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

    :ivar Commands: The Commands using the set for translation.
    :ivar Discretes: The Measurements using the set for translation.
    :ivar RaiseLowerCommands: The Commands using the set for
        translation.
    :ivar Values: The ValueToAlias mappings included in the set.
    """
    Commands: List["Command"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Discretes: List["Discrete"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RaiseLowerCommands: List[RaiseLowerCommand] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Values: List[ValueToAlias] = field(
        default_factory=list,
        metadata={
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

    :ivar maxValue: Normal value range maximum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar AccumulatorValues: The values connected to this measurement.
    :ivar LimitSets: A measurement may have zero or more limit ranges
        defined for it.
    """
    maxValue: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AccumulatorValues: List[AccumulatorValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    LimitSets: List[AccumulatorLimitSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Analog(Measurement):
    """
    Analog represents an analog Measurement.

    :ivar maxValue: Normal value range maximum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar minValue: Normal value range minimum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar normalValue: Normal measurement value, e.g., used for
        percentage calculations.
    :ivar positiveFlowIn: If true then this measurement is an active
        power, reactive power or current with the convention that a
        positive value measured at the Terminal means power is flowing
        into the related PowerSystemResource.
    :ivar AnalogValues: The values connected to this measurement.
    :ivar LimitSets: A measurement may have zero or more limit ranges
        defined for it.
    """
    maxValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normalValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    positiveFlowIn: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AnalogValues: List[AnalogValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    LimitSets: List[AnalogLimitSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetHealthEvent(ActivityRecord):
    """An asset health-related event that is created by an analytic.

    The event is a record of a change in asset health.

    :ivar actionRecommendation: Recommendation for action.
    :ivar actionTimeline: Time horizon for action.
    :ivar effectiveDateTime: The date and time when the event is
        effective.
    :ivar Analytic:
    """
    actionRecommendation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    actionTimeline: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    effectiveDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Analytic: Optional["Analytic"] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    OperationalLimitSet: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvInjection: List[SvInjection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvVoltage: Optional[SvVoltage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Terminals: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TopologicalNode: Optional[TopologicalNode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Discrete(Measurement):
    """
    Discrete represents a discrete Measurement, i.e. a Measurement representing
    discrete values, e.g. a Breaker position.

    :ivar maxValue: Normal value range maximum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar minValue: Normal value range minimum for any of the
        MeasurementValue.values. Used for scaling, e.g. in bar graphs or
        of telemetered raw values.
    :ivar normalValue: Normal measurement value, e.g., used for
        percentage calculations.
    :ivar DiscreteValues: The values connected to this measurement.
    :ivar ValueAliasSet: The ValueAliasSet used for translation of a
        MeasurementValue.value to a name.
    """
    maxValue: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minValue: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normalValue: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DiscreteValues: List["DiscreteValue"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ValueAliasSet: Optional[ValueAliasSet] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    currentApparentPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    currentReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxApparentPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minApparentPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDevice: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceGroup: Optional[EndDeviceGroup] = field(
        default=None,
        metadata={
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

    :ivar breakerFailureReason: Reason for breaker failure.
    :ivar corporateCode: Code for asset failure.
    :ivar failureClassification: Classification of failure.
    :ivar failureDateTime: Time and date of asset failure.
    :ivar failureIsolationMethod: How the asset failure was isolated
        from the system.
    :ivar failureMode: What asset failed to be able to do.
    :ivar faultLocatingMethod: The method used for locating the faulted
        part of the asset. For example, cable options include: Cap
        Discharge-Thumping, Bridge Method, Visual Inspection, Other.
    :ivar location: Failure location on an object.
    :ivar rootCause: Root cause of asset failure.
    :ivar transformerFailureReason: Reason for transformer failure.
    """
    breakerFailureReason: Optional[BreakerFailureReasonKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    corporateCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failureClassification: Optional[AssetFailureTypeification] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failureDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failureIsolationMethod: Optional[FailureIsolationMethodKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    failureMode: Optional[AssetFailureMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    faultLocatingMethod: Optional[str] = field(
        default=None,
        metadata={
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
    rootCause: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    transformerFailureReason: Optional[TransformerFailureReasonKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class HealthScore(AggregateScore):
    """
    Score that is indicative of the health of one or more assets.

    :ivar AssetRiskScore: Risk score with which this health score is
        associated.
    """
    AssetRiskScore: Optional[RiskScore] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class LabTestDataSet(ProcedureDataSet):
    """
    Results of testing done by a lab.

    :ivar conclusion: Conclusion drawn from test results.
    :ivar conclusionConfidence: Description of confidence in conclusion.
    :ivar reasonForTest: Reason for performing test.
    :ivar testEquipmentID: Identity of lab equipment used to perform
        test.
    :ivar AssetTestLab: Test lab which produced this set of lab test
        results.
    :ivar Specimen: Specimen on which lab testing done in determining
        results.
    """
    conclusion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    conclusionConfidence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reasonForTest: Optional[TestReason] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    testEquipmentID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetTestLab: Optional["AssetTestLab"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Specimen: Optional[Specimen] = field(
        default=None,
        metadata={
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
    :ivar geoInfoReference: (if applicable) Reference to geographical
        information source, often external to the utility.
    :ivar type: Classification by utility's corporate standards and
        practices, relative to the location itself (e.g., geographical,
        functional accounting, etc., not a given property that happens
        to exist at that location).
    :ivar Assets: All assets at this location.
    :ivar ConfigurationEvents: All configuration events created for this
        location.
    :ivar CoordinateSystem: Coordinate system used to describe position
        points of this location.
    :ivar Crew:
    :ivar electronicAddress: Electronic address.
    :ivar EnvironmentalLocationKind: Kind of environmental location
        which this location is.
    :ivar Fault:
    :ivar Hazards: All asset hazards at this location.
    :ivar mainAddress: Main address of the location.
    :ivar Measurements:
    :ivar phone1: Phone number.
    :ivar phone2: Additional phone number.
    :ivar PositionPoints: Sequence of position points describing this
        location, expressed in coordinate system
        'Location.CoordinateSystem'.
    :ivar PowerSystemResources: All power system resources at this
        location.
    :ivar secondaryAddress: Secondary address of the location. For
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
    geoInfoReference: Optional[str] = field(
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
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConfigurationEvents: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CoordinateSystem: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Crew: List[Crew] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    electronicAddress: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalLocationKind: List[EnvironmentalLocationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Fault: List[Fault] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Hazards: List[AssetLocationHazard] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mainAddress: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
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
    PositionPoints: List[PositionPoint] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerSystemResources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    secondaryAddress: Optional[StreetAddress] = field(
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
class OilSpecimen(Specimen):
    oilSampleTakenFrom: Optional[OilSampleLocation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    oilSampleTemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    oilTemperatureSource: Optional[OilTemperatureSource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sampleContainer: Optional[SampleContainerType] = field(
        default=None,
        metadata={
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

    :ivar multiplyBeforeAdd: Whether scalars should be applied before
        adding the 'offset'.
    :ivar offset: (if applicable) Offset to be added as well as
        multiplication using scalars.
    :ivar scalarDenominator: (if scalar is rational number) When
        'IntervalReading.value' is multiplied by 'scalarNumerator' and
        divided by this value, it causes a unit of measure conversion to
        occur, resulting in the 'ReadingType.unit'.
    :ivar scalarFloat: (if scalar is floating number) When multiplied
        with 'IntervalReading.value', it causes a unit of measure
        conversion to occur, according to the 'ReadingType.unit'.
    :ivar scalarNumerator: (if scalar is integer or rational number)
        When the scalar is a simple integer, and this attribute is
        presented alone and multiplied with 'IntervalReading.value', it
        causes a unit of measure conversion to occur, resulting in the
        'ReadingType.unit'. It is never used in conjunction with
        'scalarFloat', only with 'scalarDenominator'.
    :ivar IntervalBlocks: All blocks of interval reading values to which
        this pending conversion applies.
    :ivar ReadingType: Reading type resulting from this pending
        conversion.
    """
    multiplyBeforeAdd: Optional[bool] = field(
        default=None,
        metadata={
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
    scalarDenominator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scalarFloat: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    scalarNumerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IntervalBlocks: List["IntervalBlock"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReadingType: Optional[ReadingType] = field(
        default=None,
        metadata={
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
    :ivar Assets:
    :ivar ScheduledEventData: Specification for this scheduled event.
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
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ScheduledEventData: Optional[ScheduledEventData] = field(
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
class StringMeasurement(Measurement):
    """
    StringMeasurement represents a measurement with values of type string.

    :ivar StringMeasurementValues: The values connected to this
        measurement.
    """
    StringMeasurementValues: List[StringMeasurementValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Analytic(Document):
    """
    An algorithm or calculation for making an assessment about an asset or
    asset grouping for lifecycle decision making.

    :ivar bestValue: Value that indicates best possible numeric value.
    :ivar kind: Kind of analytic this analytic is.
    :ivar scaleKind: The scoring scale kind.
    :ivar worstValue: Value that indicates worst possible numeric value.
    :ivar AnalyticScore:
    :ivar Asset:
    :ivar AssetGroup:
    :ivar AssetHealthEvent:
    """
    bestValue: Optional[float] = field(
        default=None,
        metadata={
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
    scaleKind: Optional[ScaleKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    worstValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AnalyticScore: List[AnalyticScore] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Asset: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetGroup: List[AssetGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetHealthEvent: List[AssetHealthEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetTestLab(AssetOrganisationRole):
    """
    Test lab that performs various types of testing related to assets.

    :ivar LabTestDataSet: A set of lab test results produced by this
        test lab.
    """
    LabTestDataSet: List[LabTestDataSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class DiscreteValue(MeasurementValue):
    """
    DiscreteValue represents a discrete MeasurementValue.

    :ivar value: The value to supervise.
    :ivar Command: The Control variable associated with the
        MeasurementValue.
    :ivar Discrete: Measurement to which this value is connected.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Command: Optional["Command"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Discrete: Optional[Discrete] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EnvironmentalStringMeasurement(StringMeasurement):
    """
    String measurement of relevance in the environmental domain.

    :ivar ClassificationCondition: Classification condition which this
        string measurement helps define.
    :ivar EnvironmentalInformation: Observation or forecast with which
        this environmental string is associated.
    """
    ClassificationCondition: Optional["TypeificationCondition"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalInformation: Optional["EnvironmentalInformation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class IntervalBlock:
    """Time sequence of readings of the same reading type.

    Contained interval readings may need conversion through the
    application of an offset and a scalar defined in associated pending.

    :ivar IntervalReadings: Interval reading contained in this block.
    :ivar MeterReading: Meter reading containing this interval block.
    :ivar PendingCalculation: Pending calculation to apply to interval
        reading values contained by this block (after which the
        resulting reading type is different than the original because it
        reflects the conversion result).
    :ivar ReadingType: Type information for interval reading values
        contained in this block.
    """
    IntervalReadings: List[IntervalReading] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeterReading: Optional["MeterReading"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PendingCalculation: Optional[PendingCalculation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReadingType: Optional[ReadingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class UsagePointLocation(Location):
    """
    Location of an individual usage point.

    :ivar accessMethod: Method for the service person to access this
        usage point location. For example, a description of where to
        obtain a key if the facility is unmanned and secured.
    :ivar remark: Remarks about this location.
    :ivar siteAccessProblem: Problems previously encountered when
        visiting or performing work at this location. Examples include:
        bad dog, violent customer, verbally abusive occupant,
        obstructions, safety hazards, etc.
    :ivar UsagePoints: All usage points at this location.
    """
    accessMethod: Optional[str] = field(
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
    siteAccessProblem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Command(Control):
    """
    A Command is a discrete control used for supervisory control.

    :ivar normalValue: Normal value for Control.value e.g. used for
        percentage scaling.
    :ivar value: The value representing the actuator output.
    :ivar DiscreteValue: The MeasurementValue that is controlled.
    :ivar ValueAliasSet: The ValueAliasSet used for translation of a
        Control value to a name.
    """
    normalValue: Optional[int] = field(
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
    DiscreteValue: Optional[DiscreteValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ValueAliasSet: Optional[ValueAliasSet] = field(
        default=None,
        metadata={
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
    :ivar EnvironmentalAnalog: Environmental analog associated with this
        observation or forecast.
    :ivar EnvironmentalDataProvider: Environmental data provider
        supplying this environmental information.
    :ivar EnvironmentalPhenomenon:
    :ivar EnvironmentalStringMeasurement: Environmental string
        measurement associated with this forecast or observation.
    """
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalAnalog: List["EnvironmentalAnalog"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalDataProvider: Optional[EnvironmentalDataProvider] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalPhenomenon: List[EnvironmentalPhenomenon] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalStringMeasurement: List[EnvironmentalStringMeasurement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class MeterReading(IdentifiedObject):
    """
    Set of values obtained from the meter.

    :ivar isCoincidentTrigger: If true, this meter reading is the meter
        reading for which other coincident meter readings are requested
        or provided.
    :ivar CustomerAgreement: (could be deprecated in the future)
        Customer agreement for this meter reading.
    :ivar EndDeviceEvents: All end device events associated with this
        set of measured values.
    :ivar IntervalBlocks: All interval blocks contained in this meter
        reading.
    :ivar Meter: Meter providing this reading.
    :ivar Readings: All reading values contained within this meter
        reading.
    :ivar UsagePoint: Usage point from which this meter reading (set of
        values) has been obtained.
    :ivar valuesInterval: Date and time interval of the data items
        contained within this meter reading.
    """
    isCoincidentTrigger: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CustomerAgreement: Optional["CustomerAgreement"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceEvents: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IntervalBlocks: List[IntervalBlock] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Meter: Optional["Meter"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Readings: List[Reading] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoint: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    valuesInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
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

    :ivar isPrePay: If true, the customer is a pre-pay customer for the
        specified service.
    :ivar loadMgmt: Load management code.
    :ivar shutOffDateTime: Final date and time the service will be
        billed to the previous customer.
    :ivar Customer: Customer for this agreement.
    :ivar CustomerAccount: Customer account owning this agreement.
    :ivar DemandResponsePrograms: All demand response programs the
        customer is enrolled in through this customer agreement.
    :ivar MeterReadings: (could be deprecated in the future) All meter
        readings for this customer agreement.
    :ivar PricingStructures: All pricing structures applicable to this
        customer agreement.
    :ivar ServiceCategory: Service category for this agreement.
    :ivar ServiceLocations: All service locations regulated by this
        customer agreement.
    :ivar UsagePoints: All service delivery points regulated by this
        customer agreement.
    """
    isPrePay: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    loadMgmt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shutOffDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Customer: Optional[Customer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CustomerAccount: Optional[CustomerAccount] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DemandResponsePrograms: List[DemandResponseProgram] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeterReadings: List[MeterReading] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PricingStructures: List[PricingStructure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ServiceCategory: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ServiceLocations: List[ServiceLocation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoints: List["UsagePoint"] = field(
        default_factory=list,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    issuerTrackingID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    userID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDevice: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceEventDetails: List[EndDeviceEventDetail] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceEventType: Optional[EndDeviceEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    MeterReading: Optional[MeterReading] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoint: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalAnalog(Analog):
    """
    Analog measurement of relevance in the environmental domain.

    :ivar ClassificationCondition: Classification condition which this
        analog helps define.
    :ivar EnvironmentalInformation: Observation or forecast with which
        this environmental analog measurement is associated.
    :ivar ReportingCapability: The reporting capability this
        environmental value set helps define.
    """
    ClassificationCondition: Optional["TypeificationCondition"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalInformation: Optional[EnvironmentalInformation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReportingCapability: Optional[ReportingCapability] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Forecast(EnvironmentalInformation):
    """
    A forecast group of value sets and/or phenomena.

    :ivar validFor: The interval for which the forecast is valid.  For
        example, a forecast issued now for tomorrow might be valid for
        the next 2 hours.
    """
    validFor: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Observation(EnvironmentalInformation):
    """
    Observed (actual non-forecast) values sets and/or phenomena.
    """
    EnvironmentalEvent: List["EnvironmentalEvent"] = field(
        default_factory=list,
        metadata={
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
class TypeificationCondition(IdentifiedObject):
    """
    A classification condition used to define preconditions that must be met by
    a phenomena classification.

    :ivar duration: The duration of the of the condition in seconds
    :ivar test: The test applied to the value.
    :ivar EnvironmentalAnalog: Analog which contributes to the
        definition of this classification condition.
    :ivar EnvironmentalStringMeasurement: String measurement which
        contributes to the definition of this classification condition.
    :ivar PhenomenonClassification: Phenomenon classification to which
        this condition relates.
    """
    class Meta:
        name = "ClassificationCondition"

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
    EnvironmentalAnalog: List[EnvironmentalAnalog] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalStringMeasurement: List[EnvironmentalStringMeasurement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PhenomenonClassification: Optional["PhenomenonTypeification"] = field(
        default=None,
        metadata={
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
    Observation: List[Observation] = field(
        default_factory=list,
        metadata={
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
    :ivar ConfigurationEvents: All configuration events created for this
        usage point.
    :ivar CustomerAgreement: Customer agreement regulating this service
        delivery point.
    :ivar EndDeviceControls: All end device controls sending commands to
        this usage point.
    :ivar EndDeviceEvents: All end device events reported for this usage
        point.
    :ivar EndDevices: All end devices at this usage point.
    :ivar Equipments: All equipment connecting this usage point to the
        electrical grid.
    :ivar MeterReadings: All meter readings obtained from this usage
        point.
    :ivar MeterServiceWorkTasks: All meter service work tasks at this
        usage point.
    :ivar MetrologyRequirements: All metrology requirements for this
        usage point.
    :ivar PricingStructures: All pricing structures applicable to this
        service delivery point (with prepayment meter running as a
        stand-alone device, with no CustomerAgreement or Customer).
    :ivar ServiceCategory: Service category delivered by this usage
        point.
    :ivar ServiceLocation: Service location where the service delivered
        by this usage point is consumed.
    :ivar ServiceMultipliers: All multipliers applied at this usage
        point.
    :ivar UsagePointGroups: All groups to which this usage point
        belongs.
    :ivar UsagePointLocation: Location of this usage point.
    """
    amiBillingReady: Optional[AmiBillingReadyKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    checkBilling: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    connectionState: Optional[UsagePointConnectedKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    estimatedLoad: Optional[float] = field(
        default=None,
        metadata={
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
    isSdp: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isVirtual: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimalUsageExpected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominalServiceVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    outageRegion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseCode: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    readCycle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    readRoute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    serviceDeliveryRemark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    servicePriority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConfigurationEvents: List["ConfigurationEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CustomerAgreement: Optional[CustomerAgreement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceControls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceEvents: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDevices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Equipments: List["Equipment"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeterReadings: List[MeterReading] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeterServiceWorkTasks: List[MeterWorkTask] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MetrologyRequirements: List[MetrologyRequirement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PricingStructures: List[PricingStructure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ServiceCategory: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ServiceLocation: Optional[ServiceLocation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ServiceMultipliers: List[ServiceMultiplier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePointGroups: List[UsagePointGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePointLocation: Optional["UsagePointLocation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar ChangedDocument: Document whose change resulted in this
        configuration event.
    :ivar ChangedLocation: Location whose change resulted in this
        configuration event.
    :ivar ChangedOrganisationRole: Organisation role whose change
        resulted in this configuration event.
    :ivar ChangedPersonRole: Person role whose change resulted in this
        configuration event.
    :ivar ChangedServiceCategory: Service category whose change resulted
        in this configuration event.
    :ivar ChangedUsagePoint: Usage point whose change resulted in this
        configuration event.
    :ivar FaultCauseType:
    :ivar PowerSystemResource:
    """
    effectiveDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    modifiedBy: Optional[str] = field(
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
    ChangedAsset: Optional["Asset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ChangedDocument: Optional[Document] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ChangedLocation: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ChangedOrganisationRole: Optional[OrganisationRole] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ChangedPersonRole: Optional["PersonRole"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ChangedServiceCategory: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ChangedUsagePoint: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FaultCauseType: Optional[FaultCauseType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PowerSystemResource: Optional["PowerSystemResource"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhenomenonTypeification(IdentifiedObject):
    """
    A pre-defined phenomenon classification as defined by a particular
    authority.

    :ivar ClassificationCondition: Condition contributing to the
        classification of this phenomenon.
    :ivar EnvironmentalDataAuthority: Authority defining this
        environmental phenomenon.
    :ivar EnvironmentalPhenomenon:
    """
    class Meta:
        name = "PhenomenonClassification"

    ClassificationCondition: List[TypeificationCondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalDataAuthority: Optional["EnvironmentalDataAuthority"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalPhenomenon: List[EnvironmentalPhenomenon] = field(
        default_factory=list,
        metadata={
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

    :ivar ActivityRecords: All activity records created for this asset.
    :ivar Analytic:
    :ivar AnalyticScore:
    :ivar AssetContainer: Container of this asset.
    :ivar AssetDeployment: This asset's deployment.
    :ivar AssetFunction:
    :ivar AssetGroup:
    :ivar AssetInfo: Data applicable to this asset.
    :ivar BreakerOperation: Breaker operation information for this
        breaker.
    :ivar ConfigurationEvents: All configuration events created for this
        asset.
    :ivar FinancialInfo:
    :ivar Location: Location of this asset.
    :ivar Measurements:
    :ivar Medium:
    :ivar OrganisationRoles: All roles an organisation plays for this
        asset.
    :ivar Ownerships: All ownerships of this asset.
    :ivar PowerSystemResources: All power system resources used to
        electrically model this asset. For example, transformer asset is
        electrically modelled with a transformer and its windings and
        tap changer.
    :ivar ProcedureDataSet: Procedure data set that applies to this
        asset.
    :ivar Procedures: All procedures applicable to this asset.
    :ivar ProductAssetModel: The model of this asset.
    :ivar ScheduledEvents:
    """
    ActivityRecords: List[ActivityRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Analytic: List[Analytic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AnalyticScore: List[AnalyticScore] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetContainer: Optional["AssetContainer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetDeployment: Optional[AssetDeployment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetFunction: List[AssetFunction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetGroup: List[AssetGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AssetInfo: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    BreakerOperation: Optional[SwitchOperationSummary] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConfigurationEvents: List[ConfigurationEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FinancialInfo: Optional[FinancialInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Medium: List[Medium] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OrganisationRoles: List[AssetOrganisationRole] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Ownerships: List[Ownership] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerSystemResources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ProcedureDataSet: List[ProcedureDataSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Procedures: List[Procedure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ProductAssetModel: Optional[ProductAssetModel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ScheduledEvents: List[ScheduledEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalDataAuthority(OrganisationRole):
    """
    An entity defining classifications or categories of environmental
    information, like phenomena or alerts.

    :ivar AlertTypeList: A specific version of a list of alerts
        published by this environmental data authority.
    :ivar PhenomenonClassification: Phenomenon classification defined by
        this environmental data authority.
    """
    AlertTypeList: List["AlertTypeList"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PhenomenonClassification: List[PhenomenonTypeification] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AlertTypeList(IdentifiedObject):
    """A named list of alert types.

    Note:  the name of the list is reflected in the .name attribute (inherited from IdentifiedObject).

    :ivar version: The version of the named list of alert types.
    :ivar EnvironmentalAlert: An alert whose type is drawn from this
        alert type list.
    :ivar EnvironmentalDataAuthority: The environmental data authority
        responsible for publishing this list of alert types.
    """
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalAlert: List["EnvironmentalAlert"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalDataAuthority: Optional[EnvironmentalDataAuthority] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AssetContainer(Asset):
    """
    Asset that is aggregation of other assets such as conductors, transformers,
    switchgear, land, fences, buildings, equipment, vehicles, etc.

    :ivar Assets: All assets within this container asset.
    :ivar Seals: All seals applied to this asset container.
    """
    Assets: List["Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Seals: List[Seal] = field(
        default_factory=list,
        metadata={
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

    :ivar Assets: All assets described by this data.
    :ivar CatalogAssetType:
    :ivar PowerSystemResources: All power system resources with this
        datasheet information.
    :ivar ProductAssetModel:
    """
    Assets: List[Asset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CatalogAssetType: Optional[CatalogAssetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerSystemResources: List["PowerSystemResource"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ProductAssetModel: Optional[ProductAssetModel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Bushing(Asset):
    """
    Bushing asset.

    :ivar FixedContact: Fixed contact of interrupter to which this
        bushing is attached.
    :ivar MovingContact: Moving contact of interrupter to which this
        bushing is attached.
    :ivar Terminal:
    """
    FixedContact: Optional["InterrupterUnit"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MovingContact: Optional["InterrupterUnit"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
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

    :ivar amrSystem: Automated meter reading (AMR) system communicating
        with this com module.
    :ivar supportsAutonomousDst: If true, autonomous daylight saving
        time (DST) function is supported.
    :ivar timeZoneOffset: Time zone offset relative to GMT for the
        location of this com module.
    :ivar ComFunctions: All functions this communication module
        performs.
    """
    amrSystem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsAutonomousDst: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeZoneOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ComFunctions: List["ComFunction"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class FACTSDevice(Asset):
    """
    FACTS device asset.
    """


@dataclass
class InterrupterUnit(Asset):
    """Breaker interrupter.

    Some interrupters have one fixed and one moving contact, some have 2
    fixed contacts, some 2 moving contacts. An interrupter will have
    relationships with 2 bushings and those relationships may be any
    combination of the FixedContact and MovingContact associations.

    :ivar Bushing: Bushing(s) to which the fixed contact(s) of this
        interrupter is(are) attached. Some interrupters have one fixed
        and one moving contact, some have 2 fixed contacts, some 2
        moving contacts. An interrupter will have relationships with 2
        bushings and those relationships may be any combination of the
        FixedContact and MovingContact associations.
    :ivar OperatingMechanism: Breaker mechanism controlling this
        interrupter.
    """
    Bushing: List["Bushing"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OperatingMechanism: Optional["OperatingMechanism"] = field(
        default=None,
        metadata={
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

    :ivar InterrupterUnit: Interrupter controlled by this mechanism.
    """
    InterrupterUnit: List["InterrupterUnit"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Streetlight(Asset):
    """
    Streetlight asset.

    :ivar armLength: Length of arm. Note that a new light may be placed
        on an existing arm.
    :ivar lightRating: Power rating of light.
    """
    armLength: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lightRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class StructureSupport(Asset):
    """
    Support for structure assets.

    :ivar anchorRodCount: (if anchor) Number of rods used.
    :ivar anchorRodLength: (if anchor) Length of rod used.
    :ivar direction: Direction of this support structure.
    :ivar length: Length of this support structure.
    :ivar size: Size of this support structure.
    :ivar SecuredStructure:
    """
    anchorRodCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    anchorRodLength: Optional[float] = field(
        default=None,
        metadata={
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
    SecuredStructure: Optional["Structure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BushingInfo(AssetInfo):
    """
    Bushing datasheet information.

    :ivar c1Capacitance: Factory measured capacitance, measured between
        the power factor tap and the bushing conductor.
    :ivar c1PowerFactor: Factory measured insulation power factor,
        measured between the power factor tap and the bushing conductor.
    :ivar c2Capacitance: Factory measured capacitance measured between
        the power factor tap and ground.
    :ivar c2PowerFactor: Factory measured insulation power factor,
        measured between the power factor tap and ground.
    :ivar insulationKind: Kind of insulation.
    :ivar ratedCurrent: Rated current for bushing as installed.
    :ivar ratedImpulseWithstandVoltage: Rated impulse withstand voltage,
        also known as BIL (Basic Impulse Level).
    :ivar ratedLineToGroundVoltage: Rated line-to-ground voltage. Also
        referred to as U&lt;sub&gt;y&lt;/sub&gt; on bushing nameplate.
    :ivar ratedVoltage: Rated voltage. Can be referred to as
        U&lt;sub&gt;m&lt;/sub&gt;, system voltage or class on bushing
        nameplate.
    """
    c1Capacitance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    c1PowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    c2Capacitance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    c2PowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    insulationKind: Optional[BushingInsulationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedImpulseWithstandVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedLineToGroundVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar amrAddress: Communication ID number (e.g. serial number, IP
        address, telephone number, etc.) of the AMR module which serves
        this meter.
    :ivar amrRouter: Communication ID number (e.g. port number, serial
        number, data collector ID, etc.) of the parent device associated
        to this AMR module.
    :ivar direction: Kind of communication direction.
    :ivar technology: Kind of communication technology.
    :ivar ComModule: Module performing this communication function.
    """
    amrAddress: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    amrRouter: Optional[str] = field(
        default=None,
        metadata={
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
    ComModule: Optional[ComModule] = field(
        default=None,
        metadata={
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

    :ivar circuitCount: Number of circuits in duct bank. Refer to
        associations between a duct (ConductorAsset) and an
        ACLineSegment to understand which circuits are in which ducts.
    :ivar WireSpacingInfos:
    """
    circuitCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WireSpacingInfos: List["WireSpacingInfo"] = field(
        default_factory=list,
        metadata={
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
    :ivar ServiceLocation: Service location whose service delivery is
        measured by this end device.
    :ivar UsagePoint: Usage point to which this end device belongs.
    """
    amrSystem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    installCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isPan: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isSmartInverter: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isVirtual: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeZoneOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Customer: Optional["Customer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DispatchablePowerCapability: List[DispatchablePowerCapability] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceControls: List[EndDeviceControl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceEvents: List["EndDeviceEvent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceFunctions: List[EndDeviceFunction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceGroups: Optional[EndDeviceGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EndDeviceInfo: Optional["EndDeviceInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ServiceLocation: Optional["ServiceLocation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoint: Optional["UsagePoint"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
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
    EndDevices: List["EndDevice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class EnvironmentalAlert(ActivityRecord):
    """
    An environmental alert issued by a provider or system.

    :ivar alertType: The type of the issued alert which is drawn from
        the specified alert type list.
    :ivar cancelledDateTime: Time and date alert cancelled. Used only if
        alert is cancelled before it expires.
    :ivar headline: An abbreviated textual description of the alert
        issued. Note: the full text of the alert appears in the
        .description attribute (inherited from IdentifiedObject).
    :ivar AlertTypeList: The list of alert types from which the type of
        this alert is drawn.
    :ivar EnvironmentalDataProvider: Environmental data provider for
        this alert.
    :ivar EnvironmentalLocationKind: Type of location to which this
        environmental alert applies.
    :ivar inEffect: The interval for which this weather alert is in
        effect.
    """
    alertType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cancelledDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
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
    AlertTypeList: Optional[AlertTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EnvironmentalDataProvider: Optional[EnvironmentalDataProvider] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnvironmentalLocationKind: List["EnvironmentalLocationType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    inEffect: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
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
class IEEE1547Info(AssetInfo):
    abnormalPerformanceCategory: Optional[IEEE1547AbnormalPerfomanceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    islandingCategory: Optional[IEEE1547IslandingCategory] = field(
        default=None,
        metadata={
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
    maximumU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minimumU: Optional[float] = field(
        default=None,
        metadata={
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
    normalPerformanceCategory: Optional[IEEE1547NormalPerformanceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overExcitedPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedPatUnityPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedPcharge: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedPoverExcited: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedPunderExcited: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedQabsorbed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedQinjected: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedScharge: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    serialNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsDynamicReactiveCurrent: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsIEC61850: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsIEEE1815: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsIEEE20305: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsIslanding: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsSunSpecModBusEthernet: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsSunSpecModBusRS485: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsVoltWatt: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    supportsWattVar: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    susceptanceCeaseToEnergize: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    underExcitedPF: Optional[float] = field(
        default=None,
        metadata={
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
    PowerElectronicsConnections: List["PowerElectronicsConnection"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RotatingMachines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class InterrupterUnitInfo(AssetInfo):
    """
    :ivar interruptingMedium: Interrupting medium.
    """
    interruptingMedium: Optional[InterruptingMediumKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class OperatingMechanismInfo(AssetInfo):
    """
    Breaker operating mechanism datasheet information.

    :ivar closeAmps: Close current (nominal).
    :ivar closeVoltage: Close voltage in volts DC.
    :ivar mechanismKind: Kind of breaker operating mechanism.
    :ivar motorRunCurrent: Rated motor run current in amps.
    :ivar motorStartCurrent: Rated motor start current in amps.
    :ivar motorVoltage: Nominal motor voltage in volts DC.
    :ivar tripAmps: Trip current (nominal).
    :ivar tripVoltage: Trip voltage in volts DC.
    """
    closeAmps: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    closeVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    mechanismKind: Optional[OperatingMechanismKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    motorRunCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    motorStartCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    motorVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tripAmps: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tripVoltage: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar AssetDatasheet: Datasheet information for this power system
        resource.
    :ivar Assets: All assets represented by this power system resource.
        For example, multiple conductor assets are electrically modelled
        as a single AC line segment.
    :ivar ConfigurationEvent:
    :ivar Controls: The controller outputs used to actually govern a
        regulating device, e.g. the magnetization of a synchronous
        machine or capacitor bank breaker actuator.
    :ivar Location: Location of this power system resource.
    :ivar Measurements: The measurements associated with this power
        system resource.
    :ivar OperatingShare: The operating shares of this power system
        resource.
    :ivar PSRType: Custom classification for this power system resource.
    :ivar ReportingGroup: Reporting groups to which this power system
        resource belongs.
    """
    AssetDatasheet: Optional[AssetInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Assets: List[Asset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConfigurationEvent: List[ConfigurationEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Controls: List[Control] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OperatingShare: List[OperatingShare] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PSRType: Optional[PSRType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReportingGroup: List["ReportingGroup"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar fumigantAppliedDate: Date fumigant was last applied.
    :ivar fumigantName: Name of fumigant.
    :ivar height: Visible height of structure above ground level for
        overhead construction (e.g., Pole or Tower) or below ground
        level for an underground vault, manhole, etc. Refer to
        associated DimensionPropertiesInfo for other types of
        dimensions.
    :ivar ratedVoltage: Maximum rated voltage of the equipment that can
        be mounted on/contained within the structure.
    :ivar removeWeed: True if weeds are to be removed around asset.
    :ivar weedRemovedDate: Date weed were last removed.
    :ivar StructureSupports:
    :ivar WireSpacingInfos:
    """
    fumigantAppliedDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fumigantName: Optional[str] = field(
        default=None,
        metadata={
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
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    removeWeed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    weedRemovedDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StructureSupports: List[StructureSupport] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WireSpacingInfos: List["WireSpacingInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isSinglePhase: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isUnganged: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lowPressureAlarm: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lowPressureLockOut: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    oilVolumePerTank: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedImpulseWithstandVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedInterruptingTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ctRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ptRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar TransformerStarImpedance: Transformer star impedance
        calculated from this transformer end datasheet.
    :ivar TransformerTankInfo: Transformer tank data that this end
        description is part of.
    """
    connectionKind: Optional[WindingConnection] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    emergencyS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    endNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    insulationU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseAngleClock: Optional[int] = field(
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
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shortTermS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CoreAdmittance: Optional["TransformerCoreAdmittance"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnergisedEndNoLoadTests: List[NoLoadTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnergisedEndOpenCircuitTests: List[OpenCircuitTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnergisedEndShortCircuitTests: List[ShortCircuitTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FromMeshImpedances: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    GroundedEndShortCircuitTests: List[ShortCircuitTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OpenEndOpenCircuitTests: List[OpenCircuitTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ToMeshImpedances: List[TransformerMeshImpedance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerStarImpedance: Optional[TransformerStarImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerTankInfo: Optional["TransformerTankInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    """
    PowerTransformerInfo: Optional["PowerTransformerInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TransformerEndInfos: List["TransformerEndInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
class CogenerationPlant(PowerSystemResource):
    """A set of thermal generating units for the production of electrical
    energy and process steam (usually from the output of the steam turbines).

    The steam sendout is typically used for industrial purposes or for
    municipal heating and cooling.

    :ivar cogenHPSendoutRating: The high pressure steam sendout.
    :ivar cogenHPSteamRating: The high pressure steam rating.
    :ivar cogenLPSendoutRating: The low pressure steam sendout.
    :ivar cogenLPSteamRating: The low pressure steam rating.
    :ivar ratedP: The rated output active power of the cogeneration
        plant.
    :ivar SteamSendoutSchedule: A cogeneration plant has a steam sendout
        schedule.
    :ivar ThermalGeneratingUnits: A thermal generating unit may be a
        member of a cogeneration plant.
    """
    cogenHPSendoutRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cogenHPSteamRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cogenLPSendoutRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cogenLPSteamRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SteamSendoutSchedule: Optional[SteamSendoutSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ThermalGeneratingUnits: List["ThermalGeneratingUnit"] = field(
        default_factory=list,
        metadata={
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

    :ivar combCyclePlantRating: The combined cycle plant's active power
        output rating.
    :ivar ThermalGeneratingUnits: A thermal generating unit may be a
        member of a combined cycle plant.
    """
    combCyclePlantRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ThermalGeneratingUnits: List["ThermalGeneratingUnit"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    ConnectivityNodes: List[ConnectivityNode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TopologicalNode: List[TopologicalNode] = field(
        default_factory=list,
        metadata={
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
    :ivar EnergyConsumer: The energy consumer to which this phase
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
    EnergyConsumer: Optional["EnergyConsumer"] = field(
        default=None,
        metadata={
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
    :ivar EnergySource: The energy sourceto which the phase belongs.
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnergySource: Optional["EnergySource"] = field(
        default=None,
        metadata={
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
    :ivar inService: If true, the equipment is in service.
    :ivar networkAnalysisEnabled: The equipment is enabled to
        participate in network analysis.  If unspecified, the value is
        assumed to be true.
    :ivar normallyInService: If true, the equipment is normally in
        service.
    :ivar AdditionalEquipmentContainer: Additional equipment container
        beyond the primary equipment container.  The equipment is
        contained in another equipment container, but also grouped with
        this equipment container.
    :ivar EquipmentContainer: Container of this equipment.
    :ivar Faults: All faults on this equipment.
    :ivar OperationalLimitSet: The operational limit sets associated
        with this equipment.
    :ivar UsagePoints: All usage points connected to the electrical grid
        through this equipment.
    """
    aggregate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    inService: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    networkAnalysisEnabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normallyInService: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AdditionalEquipmentContainer: List["EquipmentContainer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EquipmentContainer: Optional["EquipmentContainer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Faults: List["Fault"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OperationalLimitSet: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UsagePoints: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Meter(EndDevice):
    """Physical asset that performs the metering role of the usage point.

    Used for measuring consumption and detection of events.

    :ivar formNumber: Meter form designation per ANSI C12.10 or other
        applicable standard. An alphanumeric designation denoting the
        circuit arrangement for which the meter is applicable and its
        specific terminal arrangement.
    :ivar MeterMultipliers: All multipliers applied at this meter.
    :ivar MeterReadings: All meter readings provided by this meter.
    :ivar MeterReplacementWorkTasks: All work tasks on replacement of
        this old meter.
    :ivar MeterServiceWorkTask: All non-replacement work tasks on this
        meter.
    """
    formNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeterMultipliers: List[MeterMultiplier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeterReadings: List["MeterReading"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeterReplacementWorkTasks: List[MeterWorkTask] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    MeterServiceWorkTask: List[MeterWorkTask] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    cutLevel2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EnergyConsumers: List["EnergyConsumer"] = field(
        default_factory=list,
        metadata={
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
    :ivar PowerElectronicsConnection:
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
    PowerElectronicsConnection: Optional["PowerElectronicsConnection"] = field(
        default=None,
        metadata={
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
    :ivar RegulatingCondEq: The equipment that participates in this
        regulating control scheme.
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
    monitoredPhase: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    targetDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    targetValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RegulatingCondEq: List["RegulatingCondEq"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RegulationSchedule: List[RegulationSchedule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Terminal: Optional["Terminal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ReportingGroup(IdentifiedObject):
    """
    A reporting group is used for various ad-hoc groupings used for reporting.

    :ivar BusNameMarker: The bus name markers that belong to this
        reporting group.
    :ivar PowerSystemResource: Power system resources which belong to
        this reporting group.
    :ivar ReportingSuperGroup:
    :ivar TopologicalNode: The topological nodes that belong to the
        reporting group.
    """
    BusNameMarker: List["BusNameMarker"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerSystemResource: List[PowerSystemResource] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReportingSuperGroup: Optional[ReportingSuperGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TopologicalNode: List[TopologicalNode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Reservoir(PowerSystemResource):
    """A water storage facility within a hydro system, including: ponds, lakes,
    lagoons, and rivers.

    The storage is usually behind some type of dam.

    :ivar activeStorageCapacity: Storage volume between the full supply
        level and the normal minimum operating level.
    :ivar energyStorageRating: The reservoir's energy storage rating in
        energy for given head conditions.
    :ivar fullSupplyLevel: Full supply level, above which water will
        spill. This can be the spillway crest level or the top of closed
        gates.
    :ivar grossCapacity: Total capacity of reservoir.
    :ivar normalMinOperateLevel: Normal minimum operating level below
        which the penstocks will draw air.
    :ivar riverOutletWorks: River outlet works for riparian right
        releases or other purposes.
    :ivar spillTravelDelay: The spillway water travel delay to the next
        downstream reservoir.
    :ivar spillwayCapacity: The flow capacity of the spillway in cubic
        meters per second.
    :ivar spillwayCrestLength: The length of the spillway crest.
    :ivar spillwayCrestLevel: Spillway crest level above which water
        will spill.
    :ivar spillWayGateType: Type of spillway gate, including parameters.
    :ivar HydroPowerPlants: Generators discharge water to or pumps are
        supplied water from a downstream reservoir.
    :ivar InflowForecasts: A reservoir may have a "natural" inflow
        forecast.
    :ivar LevelVsVolumeCurves: A reservoir may have a level versus
        volume relationship.
    :ivar SpillsFromReservoir: A reservoir may spill into a downstream
        reservoir.
    :ivar TargetLevelSchedule: A reservoir may have a water level target
        schedule.
    :ivar UpstreamFromHydroPowerPlants: Generators are supplied water
        from or pumps discharge water to an upstream reservoir.
    """
    activeStorageCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    energyStorageRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    fullSupplyLevel: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    grossCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normalMinOperateLevel: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    riverOutletWorks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spillTravelDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spillwayCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spillwayCrestLength: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spillwayCrestLevel: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    spillWayGateType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HydroPowerPlants: List["HydroPowerPlant"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    InflowForecasts: List[InflowForecast] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    LevelVsVolumeCurves: List[LevelVsVolumeCurve] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SpillsFromReservoir: Optional["Reservoir"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TargetLevelSchedule: Optional[TargetLevelSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    UpstreamFromHydroPowerPlants: List["HydroPowerPlant"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normalSections: Optional[int] = field(
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
    sections: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ShuntCompensator: Optional["ShuntCompensator"] = field(
        default=None,
        metadata={
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
    :ivar normalOpen: Used in cases when no Measurement for the status
        value is present. If the SwitchPhase has a status measurement
        the Discrete.normalValue is expected to match with this value.
    :ivar phaseSide1: Phase of this SwitchPhase on the side with
        terminal sequence number equal 1. Should be a phase contained in
        that terminal&amp;rsquo;s phases attribute.
    :ivar phaseSide2: Phase of this SwitchPhase on the side with
        terminal sequence number equal 2.  Should be a phase contained
        in that terminal&amp;rsquo;s Terminal.phases attribute.
    :ivar ratedCurrent: Rated current through this phase, if different
        from the others.
    :ivar Switch: The switch of the switch phase.
    """
    closed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normalOpen: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseSide1: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseSide2: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Switch: Optional["Switch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TapChanger(PowerSystemResource):
    """
    Mechanism for changing transformer winding tap positions.

    :ivar controlEnabled: Specifies the regulation status of the
        equipment.  True is regulating, false is not regulating.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    highStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    initialDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lowStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ltcFlag: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutralStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutralU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normalStep: Optional[int] = field(
        default=None,
        metadata={
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
    subsequentDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvTapStep: Optional[SvTapStep] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TapChangerControl: Optional["TapChangerControl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TapSchedules: List[TapSchedule] = field(
        default_factory=list,
        metadata={
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

    :ivar BusbarSection: A VoltageControlZone is controlled by a
        designated BusbarSection.
    :ivar RegulationSchedule: A VoltageControlZone may have a  voltage
        regulation schedule.
    """
    BusbarSection: Optional["BusbarSection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    RegulationSchedule: Optional["RegulationSchedule"] = field(
        default=None,
        metadata={
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

    :ivar isCable: If true, this spacing data describes a cable.
    :ivar phaseWireCount: Number of wire sub-conductors in the
        symmetrical bundle (typically between 1 and 4).
    :ivar phaseWireSpacing: Distance between wire sub-conductors in a
        symmetrical bundle.
    :ivar usage: Usage of the associated wires.
    :ivar ACLineSegments:
    :ivar DuctBank:
    :ivar Structures:
    :ivar WireAssemblyInfo:
    :ivar WirePositions: All positions of single wires (phase or
        neutral) making the conductor.
    """
    isCable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseWireCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseWireSpacing: Optional[float] = field(
        default=None,
        metadata={
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
    ACLineSegments: List["ACLineSegment"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    DuctBank: Optional[DuctBank] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Structures: List[Structure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WireAssemblyInfo: List["WireAssemblyInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WirePositions: List[WirePosition] = field(
        default_factory=list,
        metadata={
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
    :ivar ReportingGroup: The reporting group to which this bus name
        marker belongs.
    :ivar Terminal: The terminals associated with this bus name marker.
    :ivar TopologicalNode: A user defined topological node that was
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
    ReportingGroup: Optional[ReportingGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Terminal: List["ACDCTerminal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    TopologicalNode: Optional[TopologicalNode] = field(
        default=None,
        metadata={
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

    :ivar compositeSwitchType: An alphanumeric code that can be used as
        a reference to extra information such as the description of the
        interlocking scheme if any.
    :ivar Switches: Switches contained in this Composite switch.
    """
    compositeSwitchType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Switches: List["Switch"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvStatus: List[SvStatus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Terminals: List["Terminal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Equipments: List["Equipment"] = field(
        default_factory=list,
        metadata={
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

    :ivar dischargeTravelDelay: Water travel delay from tailbay to next
        downstream hydro power station.
    :ivar genRatedP: The hydro plant's generating rating active power
        for rated head conditions.
    :ivar hydroPlantStorageType: The type of hydro power plant water
        storage.
    :ivar penstockType: Type and configuration of hydro plant
        penstock(s).
    :ivar plantDischargeCapacity: Total plant discharge capacity.
    :ivar plantRatedHead: The plant's rated gross head.
    :ivar pumpRatedP: The hydro plant's pumping rating active power for
        rated head conditions.
    :ivar surgeTankCode: A code describing the type (or absence) of
        surge tank that is associated with the hydro power plant.
    :ivar surgeTankCrestLevel: The level at which the surge tank spills.
    :ivar GenSourcePumpDischargeReservoir: Generators are supplied water
        from or pumps discharge water to an upstream reservoir.
    :ivar HydroGeneratingUnits: The hydro generating unit belongs to a
        hydro power plant.
    :ivar HydroPumps: The hydro pump may be a member of a pumped storage
        plant or a pump for distributing water.
    :ivar Reservoir: Generators discharge water to or pumps are supplied
        water from a downstream reservoir.
    """
    dischargeTravelDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    genRatedP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydroPlantStorageType: Optional[HydroPlantStorageKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    penstockType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    plantDischargeCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    plantRatedHead: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pumpRatedP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    surgeTankCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    surgeTankCrestLevel: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    GenSourcePumpDischargeReservoir: Optional[Reservoir] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    HydroGeneratingUnits: List["HydroGeneratingUnit"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HydroPumps: List["HydroPump"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Reservoir: Optional[Reservoir] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gPerSection: Optional[float] = field(
        default=None,
        metadata={
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
    NonlinearShuntCompensatorPhasePoints: List[NonlinearShuntCompensatorPhasePoint] = field(
        default_factory=list,
        metadata={
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

    :ivar TransformerEnd: Transformer end to which this phase tap
        changer belongs.
    """
    TransformerEnd: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerElectronicsConnection: Optional["PowerElectronicsConnection"] = field(
        default=None,
        metadata={
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

    :ivar stepVoltageIncrement: Tap step increment, in per cent of
        neutral voltage, per step position. When the increment is
        negative, the voltage decreases when the tap step increases.
    :ivar RatioTapChangerTable: The tap ratio table for this ratio  tap
        changer.
    :ivar TransformerEnd: Transformer end to which this ratio tap
        changer belongs.
    """
    stepVoltageIncrement: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RatioTapChangerTable: Optional[RatioTapChangerTable] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerEnd: Optional["TransformerEnd"] = field(
        default=None,
        metadata={
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

    :ivar limitVoltage: Maximum allowed regulated voltage on the PT
        secondary, regardless of line drop compensation. Sometimes
        referred to as first-house protection.
    :ivar lineDropCompensation: If true, the line drop compensation is
        to be applied.
    :ivar lineDropR: Line drop compensator resistance setting for normal
        (forward) power flow.
    :ivar lineDropX: Line drop compensator reactance setting for normal
        (forward) power flow.
    :ivar reverseLineDropR: Line drop compensator resistance setting for
        reverse power flow.
    :ivar reverseLineDropX: Line drop compensator reactance setting for
        reverse power flow.
    :ivar TapChanger: The tap changers that participates in this
        regulating tap control scheme.
    """
    limitVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lineDropCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lineDropR: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lineDropX: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reverseLineDropR: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    reverseLineDropX: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TapChanger: List["TapChanger"] = field(
        default_factory=list,
        metadata={
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

    :ivar PowerTransformer: Bank this transformer belongs to.
    :ivar TransformerTankEnds: All windings of this transformer.
    """
    PowerTransformer: Optional["PowerTransformer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerTankEnds: List[TransformerTankEnd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
class WireAssemblyInfo(AssetInfo):
    """
    Describes the construction of a multi-conductor wire.
    """
    PerLengthLineParameter: List[PerLengthLineParameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WirePhaseInfo: List["WirePhaseInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WireSpacingInfo: Optional[WireSpacingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar BusNameMarker: The bus name marker used to name the bus
        (topological node).
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    BusNameMarker: Optional[BusNameMarker] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Measurements: List[Measurement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    OperationalLimitSet: List[OperationalLimitSet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class BatteryUnit(PowerElectronicsUnit):
    """
    An electrochemical energy storage device.

    :ivar batteryState: indicates whether the battery is charging,
        discharging or idle
    :ivar ratedE: full energy storage capacity of the battery
    :ivar storedE: amount of energy currently stored; no more than
        ratedE
    """
    batteryState: Optional[BatteryState] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedE: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    storedE: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar bayEnergyMeasFlag: Indicates the presence/absence of energy
        measurements.
    :ivar bayPowerMeasFlag: Indicates the presence/absence of
        active/reactive power measurements.
    :ivar breakerConfiguration: Breaker configuration.
    :ivar busBarConfiguration: Bus bar configuration.
    :ivar Substation: Substation containing the bay.
    :ivar VoltageLevel: The voltage level containing this bay.
    """
    bayEnergyMeasFlag: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    bayPowerMeasFlag: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    breakerConfiguration: Optional[BreakerConfiguration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    busBarConfiguration: Optional[BusbarConfiguration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Substation: Optional["Substation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    VoltageLevel: Optional["VoltageLevel"] = field(
        default=None,
        metadata={
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

    :ivar lengthFromTerminal1: The length to the place where the clamp
        is located starting from side one of the line segment, i.e. the
        line segment terminal with sequence number equal to 1.
    :ivar ACLineSegment: The line segment to which the clamp is
        connected.
    """
    lengthFromTerminal1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ACLineSegment: Optional["ACLineSegment"] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NormalEnergizedSubstation: List["Substation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NormalEnergizingSubstation: Optional["Substation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NormalHeadTerminal: List["Terminal"] = field(
        default_factory=list,
        metadata={
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

    :ivar pumpDischAtMaxHead: The pumping discharge under maximum head
        conditions, usually at full gate.
    :ivar pumpDischAtMinHead: The pumping discharge under minimum head
        conditions, usually at full gate.
    :ivar pumpPowerAtMaxHead: The pumping power under maximum head
        conditions, usually at full gate.
    :ivar pumpPowerAtMinHead: The pumping power under minimum head
        conditions, usually at full gate.
    :ivar HydroPowerPlant: The hydro pump may be a member of a pumped
        storage plant or a pump for distributing water.
    :ivar HydroPumpOpSchedule: The hydro pump has a pumping schedule
        over time, indicating when pumping is to occur.
    :ivar RotatingMachine: The synchronous machine drives the turbine
        which moves the water from a low elevation to a higher
        elevation. The direction of machine rotation for pumping may or
        may not be the same as for generating.
    """
    pumpDischAtMaxHead: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pumpDischAtMinHead: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pumpPowerAtMaxHead: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    pumpPowerAtMinHead: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HydroPowerPlant: Optional[HydroPowerPlant] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HydroPumpOpSchedule: Optional[HydroPumpOpSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RotatingMachine: Optional["RotatingMachine"] = field(
        default=None,
        metadata={
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

    :ivar Region: The sub-geographical region of the line.
    """
    Region: Optional["SubGeographicalRegion"] = field(
        default=None,
        metadata={
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

    :ivar stepPhaseShiftIncrement: Phase shift per step position. A
        positive value indicates a positive phase shift from the winding
        where the tap is located to the other winding (for a two-winding
        transformer). The actual phase shift increment might be more
        accurately computed from the symmetrical or asymmetrical models
        or a tap step table lookup if those are available.
    :ivar xMax: The reactance depend on the tap position according to a
        "u" shaped curve. The maximum reactance (xMax) appear at the low
        and high tap positions.
    :ivar xMin: The reactance depend on the tap position according to a
        "u" shaped curve. The minimum reactance (xMin) appear at the mid
        tap position.
    """
    stepPhaseShiftIncrement: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xMin: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar voltageStepIncrement: The voltage step increment on the out of
        phase winding specified in percent of neutral voltage of the tap
        changer. When the increment is negative, the voltage decreases
        when the tap step increases.
    :ivar xMax: The reactance depend on the tap position according to a
        "u" shaped curve. The maximum reactance (xMax) appear at the low
        and high tap positions.
    :ivar xMin: The reactance depend on the tap position according to a
        "u" shaped curve. The minimum reactance (xMin) appear at the mid
        tap position.
    """
    voltageStepIncrement: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xMin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class PhaseTapChangerTabular(PhaseTapChanger):
    """
    :ivar PhaseTapChangerTable: The phase tap changer table for this
        phase tap changer.
    """
    PhaseTapChangerTable: Optional["PhaseTapChangerTable"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )

#RENAMED TO MATCH CIM XML MODELS
@dataclass
class PhotovoltaicUnit(PowerElectronicsUnit):
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerTransformerEnd: List[PowerTransformerEnd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerTanks: List[TransformerTank] = field(
        default_factory=list,
        metadata={
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
    :ivar varistorPresent: Describe if a metal oxide varistor (mov) for
        over voltage protection is configured at the series compensator.
    :ivar varistorRatedCurrent: The maximum current the varistor is
        designed to handle at specified duration.
    :ivar varistorVoltageThreshold: The dc voltage at which the varistor
        start conducting.
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
    varistorPresent: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    varistorRatedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    varistorVoltageThreshold: Optional[float] = field(
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
class Substation(EquipmentContainer):
    """
    A collection of equipment for purposes other than generation or
    utilization, through which electric energy in bulk is passed for the
    purposes of switching or modifying its characteristics.

    :ivar Bays: Bays contained in the substation.
    :ivar NamingFeeder: The primary feeder that normally energizes the
        secondary substation. Used for naming purposes.  Either this
        association or the substation to subgeographical region should
        be used for hiearchical containment specification.
    :ivar NormalEnergizedFeeder: The normal energized feeders of the
        substation. Also used for naming purposes.
    :ivar NormalEnergizingFeeder: The feeders that potentially energize
        the downstream substation.  Should be consistent with the
        associations that describe the naming hiearchy.
    :ivar Region: The SubGeographicalRegion containing the substation.
    :ivar VoltageLevels: The voltage levels within this substation.
    """
    Bays: List["Bay"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NamingFeeder: Optional["Feeder"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NormalEnergizedFeeder: List["Feeder"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NormalEnergizingFeeder: List["Feeder"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Region: Optional[SubGeographicalRegion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    VoltageLevels: List["VoltageLevel"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class Switch(ConductingEquipment):
    """A generic device designed to close, or open, or both, one or more
    electric circuits.

    All switches are two terminal devices including grounding switches.

    :ivar normalOpen: The attribute is used in cases when no Measurement
        for the status value is present. If the Switch has a status
        measurement the Discrete.normalValue is expected to match with
        the Switch.normalOpen.
    :ivar open: The attribute tells if the switch is considered open
        when used as input to topology processing.
    :ivar ratedCurrent: The maximum continuous current carrying capacity
        in amps governed by the device material and construction.
    :ivar retained: Branch is retained in a bus branch model.  The flow
        through retained switches will normally be calculated in power
        flow.
    :ivar CompositeSwitch: Composite switch to which this Switch
        belongs.
    :ivar SvSwitch: The switch state associated with the switch.
    :ivar SwitchPhase: The individual switch phases for the switch.
    :ivar SwitchSchedules: A Switch can be associated with
        SwitchSchedules.
    """
    normalOpen: Optional[bool] = field(
        default=None,
        metadata={
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
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
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
    CompositeSwitch: Optional[CompositeSwitch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvSwitch: List[SvSwitch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SwitchPhase: List[SwitchPhase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SwitchSchedules: List[SwitchSchedule] = field(
        default_factory=list,
        metadata={
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

    :ivar highVoltageLimit: The bus bar's high voltage limit
    :ivar lowVoltageLimit: The bus bar's low voltage limit
    :ivar BaseVoltage: The base voltage used for all equipment within
        the voltage level.
    :ivar Bays: The bays within this voltage level.
    :ivar Substation: The substation of the voltage level.
    """
    highVoltageLimit: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    lowVoltageLimit: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    BaseVoltage: Optional["BaseVoltage"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Bays: List["Bay"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Substation: Optional["Substation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WireAssemblyInfo: Optional[WireAssemblyInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    WireInfo: Optional["WireInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WirePosition: Optional[WirePosition] = field(
        default=None,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    VoltageControlZone: Optional["VoltageControlZone"] = field(
        default=None,
        metadata={
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

    :ivar lengthFromTerminal1: The length to the place where the cut is
        located starting from side one of the cut line segment, i.e. the
        line segment Terminal with sequenceNumber equal to 1.
    :ivar ACLineSegment: The line segment to which the cut is applied.
    """
    lengthFromTerminal1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ACLineSegment: Optional["ACLineSegment"] = field(
        default=None,
        metadata={
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
    phaseConnection: Optional[PhaseShuntConnectionKind] = field(
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
    EnergyConsumerPhase: List[EnergyConsumerPhase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    House: Optional[House] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    LoadResponse: Optional[LoadResponseCharacteristic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerCutZone: Optional[PowerCutZone] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    voltageAngle: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltageMagnitude: Optional[float] = field(
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
    EnergySourcePhase: List[EnergySourcePhase] = field(
        default_factory=list,
        metadata={
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
    :ivar nominalU: The nominal voltage for which the coil is designed.
    :ivar offsetCurrent: The offset current that the Petersen coil
        controller is operating from the resonant point.  This is
        normally a fixed amount for which the controller is configured
        and could be positive or negative.  Typically 0 to 60 Amperes
        depending on voltage and resonance conditions.
    :ivar positionCurrent: The control current used to control the
        Petersen coil also known as the position current.  Typically in
        the range of 20-200mA.
    :ivar xGroundMax: The maximum reactance.
    :ivar xGroundMin: The minimum reactance.
    :ivar xGroundNominal: The nominal reactance.  This is the operating
        point (normally over compensation) that is defined based on the
        resonance point in the healthy network condition.  The impedance
        is calculated based on nominal voltage divided by position
        current.
    """
    mode: Optional[PetersenCoilModeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominalU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    offsetCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    positionCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xGroundMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xGroundMin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    xGroundNominal: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar windingConnectionAngle: The phase angle between the in-phase
        winding and the out-of -phase winding used for creating phase
        shift. The out-of-phase winding produces what is known as the
        difference voltage.  Setting this angle to 90 degrees is not the
        same as a symmetrical transformer.
    """
    windingConnectionAngle: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar PhaseTapChangerTablePoint: The points of this table.
    :ivar PhaseTapChangerTabular: The phase tap changers to which this
        phase tap table applies.
    """
    PhaseTapChangerTablePoint: List[PhaseTapChangerTablePoint] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    PhaseTapChangerTabular: List[PhaseTapChangerTabular] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ProtectedSwitch(Switch):
    """
    A ProtectedSwitch is a switching device that can be operated by
    ProtectionEquipment.

    :ivar breakingCapacity: The maximum fault current a breaking device
        can break safely under prescribed conditions of use.
    """
    breakingCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RegulatingControl: Optional["RegulatingControl"] = field(
        default=None,
        metadata={
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
class Terminal(ACDCTerminal):
    """An AC electrical connection point to a piece of conducting equipment.

    Terminals are connected at physical connection points called
    connectivity nodes.

    :ivar BranchGroupTerminal: The directed branch group terminals for
        which this terminal is monitored.
    :ivar Bushing:
    :ivar ConductingEquipment: The conducting equipment of the terminal.
        Conducting equipment have  terminals that may be connected to
        other conducting equipment terminals via connectivity nodes or
        topological nodes.
    :ivar ConnectivityNode: The connectivity node to which this terminal
        connects with zero impedance.
    :ivar EquipmentFaults: The equipment faults at this terminal.
    :ivar HasFirstMutualCoupling: Mutual couplings associated with the
        branch as the first branch.
    :ivar HasSecondMutualCoupling: Mutual couplings with the branch
        associated as the first branch.
    :ivar NormalHeadFeeder: The feeder that this terminal normally
        feeds.  Only specifed for the terminals at head of feeders.
    :ivar RegulatingControl: The controls regulating this terminal.
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
    BranchGroupTerminal: List[BranchGroupTerminal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Bushing: Optional["Bushing"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ConductingEquipment: Optional["ConductingEquipment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ConnectivityNode: Optional["ConnectivityNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EquipmentFaults: List["EquipmentFault"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HasFirstMutualCoupling: List[MutualCoupling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HasSecondMutualCoupling: List[MutualCoupling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    NormalHeadFeeder: Optional["Feeder"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RegulatingControl: List["RegulatingControl"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvPowerFlow: List[SvPowerFlow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TopologicalNode: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TransformerEnd: List[TransformerEnd] = field(
        default_factory=list,
        metadata={
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
        ï¿½C.
    :ivar rAC50: AC resistance per unit length of the conductor at 50
        ï¿½C.
    :ivar rAC75: AC resistance per unit length of the conductor at 75
        ï¿½C.
    :ivar radius: Outside radius of the wire.
    :ivar ratedCurrent: Current carrying capacity of the wire under
        stated thermal conditions.
    :ivar rDC20: DC resistance per unit length of the conductor at 20
        ï¿½C.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    coreStrandCount: Optional[int] = field(
        default=None,
        metadata={
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
    insulationMaterial: Optional[WireInsulationKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    insulationThickness: Optional[float] = field(
        default=None,
        metadata={
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
    rAC25: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rAC50: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rAC75: Optional[float] = field(
        default=None,
        metadata={
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
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    rDC20: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sizeDescription: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    strandCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ACLineSegmentPhases: List["ACLineSegmentPhase"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WirePhaseInfo: List[WirePhaseInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ACLineSegment: Optional["ACLineSegment"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    WireInfo: Optional[WireInfo] = field(
        default=None,
        metadata={
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

    :ivar inTransitTime: The transition time from open to close.
    """
    inTransitTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    diameterOverCore: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    diameterOverInsulation: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    diameterOverJacket: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    diameterOverScreen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    isStrandFill: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominalTemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    outerJacketKind: Optional[CableOuterJacketKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sheathAsNeutral: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    shieldMaterial: Optional[CableShieldMaterialKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ConformLoad(EnergyConsumer):
    """
    ConformLoad represent loads that follow a daily load change pattern where
    the pattern can be used to scale the load with a system load.

    :ivar LoadGroup: Group of this ConformLoad.
    """
    LoadGroup: Optional[ConformLoadGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class ExternalNetworkInjection(RegulatingCondEq):
    """
    This class represents external network and it is used for IEC 60909
    calculations.

    :ivar governorSCD: Power Frequency Bias. This is the change in power
        injection divided by the change in frequency and negated.  A
        positive value of the power frequency bias provides additional
        power injection upon a drop in frequency.
    :ivar ikSecond: Indicates whether initial symmetrical short-circuit
        current and power have been calculated according to IEC (Ik").
    :ivar maxInitialSymShCCurrent: Maximum initial symmetrical short-
        circuit currents (Ik" max) in A (Ik" = Sk"/(SQRT(3) Un)). Used
        for short circuit data exchange according to IEC 60909
    :ivar maxP: Maximum active power of the injection.
    :ivar maxQ: Not for short circuit modelling; It is used for
        modelling of infeed for load flow exchange. If maxQ and minQ are
        not used ReactiveCapabilityCurve can be used
    :ivar maxR0ToX0Ratio: Maximum ratio of zero sequence resistance of
        Network Feeder to its zero sequence reactance (R(0)/X(0) max).
        Used for short circuit data exchange according to IEC 60909
    :ivar maxR1ToX1Ratio: Maximum ratio of positive sequence resistance
        of Network Feeder to its positive sequence reactance (R(1)/X(1)
        max). Used for short circuit data exchange according to IEC
        60909
    :ivar maxZ0ToZ1Ratio: Maximum ratio of zero sequence impedance to
        its positive sequence impedance (Z(0)/Z(1) max). Used for short
        circuit data exchange according to IEC 60909
    :ivar minInitialSymShCCurrent: Minimum initial symmetrical short-
        circuit currents (Ik" min) in A (Ik" = Sk"/(SQRT(3) Un)). Used
        for short circuit data exchange according to IEC 60909
    :ivar minP: Minimum active power of the injection.
    :ivar minQ: Not for short circuit modelling; It is used for
        modelling of infeed for load flow exchange. If maxQ and minQ are
        not used ReactiveCapabilityCurve can be used
    :ivar minR0ToX0Ratio: Indicates whether initial symmetrical short-
        circuit current and power have been calculated according to IEC
        (Ik"). Used for short circuit data exchange according to IEC
        6090
    :ivar minR1ToX1Ratio: Minimum ratio of positive sequence resistance
        of Network Feeder to its positive sequence reactance (R(1)/X(1)
        min). Used for short circuit data exchange according to IEC
        60909
    :ivar minZ0ToZ1Ratio: Minimum ratio of zero sequence impedance to
        its positive sequence impedance (Z(0)/Z(1) min). Used for short
        circuit data exchange according to IEC 60909
    :ivar p: Active power injection. Load sign convention is used, i.e.
        positive sign means flow out from a node. Starting value for
        steady state solutions.
    :ivar q: Reactive power injection. Load sign convention is used,
        i.e. positive sign means flow out from a node. Starting value
        for steady state solutions.
    :ivar referencePriority: Priority of unit for use as powerflow
        voltage phase angle reference bus selection. 0 = don t care
        (default) 1 = highest priority. 2 is less than 1 and so on.
    :ivar voltageFactor: Voltage factor in pu, which was used to
        calculate short-circuit current Ik" and power Sk".
    """
    governorSCD: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ikSecond: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxInitialSymShCCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxR0ToX0Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxR1ToX1Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxZ0ToZ1Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minInitialSymShCCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minR0ToX0Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minR1ToX1Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minZ0ToZ1Ratio: Optional[float] = field(
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
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    referencePriority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltageFactor: Optional[float] = field(
        default=None,
        metadata={
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
    :ivar maxP: The maximum active power on the DC side at which the
        frequence converter should operate.
    :ivar maxU: The maximum voltage on the DC side at which the
        frequency converter should operate.
    :ivar minP: The minimum active power on the DC side at which the
        frequence converter should operate.
    :ivar minU: The minimum voltage on the DC side at which the
        frequency converter should operate.
    """
    frequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minU: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar LoadGroup: Group of this ConformLoad.
    """
    LoadGroup: Optional[NonConformLoadGroup] = field(
        default=None,
        metadata={
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
    :ivar IEEE1547ControlSettings:
    :ivar IEEE1547Info:
    :ivar IEEE1547Setting:
    :ivar IEEE1547TripSettings:
    :ivar PowerElectronicsConnectionPhases:
    :ivar PowerElectronicsUnit:
    """
    inverterMode: Optional[SmartInverterMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxIFault: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minQ: Optional[float] = field(
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
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IEEE1547ControlSettings: Optional["IEEE1547ControlSettings"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IEEE1547Info: Optional[IEEE1547Info] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IEEE1547Setting: Optional[IEEE1547Setting] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IEEE1547TripSettings: Optional[IEEE1547TripSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerElectronicsConnectionPhases: List[PowerElectronicsConnectionPhase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerElectronicsUnit: List[PowerElectronicsUnit] = field(
        default_factory=list,
        metadata={
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
    maximumSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nomU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    normalSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    phaseConnection: Optional[PhaseShuntConnectionKind] = field(
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
    ShuntCompensatorPhase: List[ShuntCompensatorPhase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    SvShuntCompensatorSections: Optional[SvShuntCompensatorSections] = field(
        default=None,
        metadata={
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

    :ivar capacitiveRating: Maximum available capacitive reactance.
    :ivar inductiveRating: Maximum available inductive reactance.
    :ivar q: Reactive power injection. Load sign convention is used,
        i.e. positive sign means flow out from a node. Starting value
        for a steady state solution.
    :ivar slope: The characteristics slope of an SVC defines how the
        reactive power output changes in proportion to the difference
        between the regulated bus voltage and the voltage setpoint.
    :ivar sVCControlMode: SVC control mode.
    :ivar voltageSetPoint: The reactive power output of the SVC is
        proportional to the difference between the voltage at the
        regulated bus and the voltage setpoint.  When the regulated bus
        voltage is equal to the voltage setpoint, the reactive power
        output is zero.
    """
    capacitiveRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    inductiveRating: Optional[float] = field(
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
    slope: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    sVCControlMode: Optional[SVCControlMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltageSetPoint: Optional[float] = field(
        default=None,
        metadata={
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
    :ivar shortCircuitEndTemperature: Maximum permitted temperature at
        the end of SC for the calculation of minimum short-circuit
        currents. Used for short circuit data exchange according to IEC
        60909
    :ivar x: Positive sequence series reactance of the entire line
        section.
    :ivar x0: Zero sequence series reactance of the entire line section.
    :ivar ACLineSegmentPhases: The line segment phases which belong to
        the line segment.
    :ivar Clamp: The clamps connected to the line segment.
    :ivar Cut: Cuts applied to the line segment.
    :ivar LineFaults: The line faults of the line segment.
    :ivar ParallelLineSegment:
    :ivar PerLengthImpedance: Per-length impedance of this line segment.
    :ivar WireSpacingInfo:
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
    shortCircuitEndTemperature: Optional[float] = field(
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
    ACLineSegmentPhases: List[ACLineSegmentPhase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Clamp: List[Clamp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    Cut: List[Cut] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    LineFaults: List[LineFault] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ParallelLineSegment: Optional[ParallelLineSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PerLengthImpedance: Optional[PerLengthImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    WireSpacingInfo: Optional[WireSpacingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
        neutral strand at 20 ï¿½C.
    """
    diameterOverNeutral: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutralStrandCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutralStrandGmr: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutralStrandRadius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    neutralStrandRDC20: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class IEEE1547ControlSettings:
    constantPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    constantReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceIntentionalDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceMaxFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceMaxVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceMinFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    enterServiceMinVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    frequencyDroopResponseTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    openLoopResponseTimeP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    overFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeConstantOpenLoop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    timeConstantReferenceVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    underFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    underFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltVarQ1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltVarQ2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltVarQ3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltVarQ4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltVarV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltVarV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltVarV3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltVarV4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltWattP1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltWattP2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltWattV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    voltWattV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wattVarP1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wattVarP2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wattVarP3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wattVarP4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wattVarQ1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wattVarQ2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wattVarQ3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    wattVarQ4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PowerElectronicsConnections: List[PowerElectronicsConnection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RotatingMachines: List["RotatingMachine"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    bPerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    g0PerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    gPerSection: Optional[float] = field(
        default=None,
        metadata={
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
    NonlinearShuntCompensatorPoints: List[NonlinearShuntCompensatorPoint] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    tapeThickness: Optional[float] = field(
        default=None,
        metadata={
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
    :ivar ratedPowerFactor: Power factor (nameplate data). It is
        primarily used for short circuit data exchange according to IEC
        60909.
    :ivar ratedS: Nameplate apparent power rating for the unit. The
        attribute shall have a positive value.
    :ivar ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It
        is primarily used for short circuit data exchange according to
        IEC 60909.
    :ivar GeneratingUnit: A synchronous machine may operate as a
        generator and as such becomes a member of a generating unit.
    :ivar HydroPump: The synchronous machine drives the turbine which
        moves the water from a low elevation to a higher elevation. The
        direction of machine rotation for pumping may or may not be the
        same as for generating.
    :ivar IEEE1547ControlSettings:
    :ivar IEEE1547Info:
    :ivar IEEE1547Setting:
    :ivar IEEE1547TripSettings:
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
    ratedPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    GeneratingUnit: Optional["GeneratingUnit"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HydroPump: Optional[HydroPump] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IEEE1547ControlSettings: Optional[IEEE1547ControlSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IEEE1547Info: Optional[IEEE1547Info] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IEEE1547Setting: Optional[IEEE1547Setting] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IEEE1547TripSettings: Optional[IEEE1547TripSettings] = field(
        default=None,
        metadata={
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

    :ivar asynchronousMachineType: Indicates the type of Asynchronous
        Machine (motor or generator).
    :ivar converterFedDrive: Indicates whether the machine is a
        converter fed drive. Used for short circuit data exchange
        according to IEC 60909
    :ivar efficiency: Efficiency of the asynchronous machine at nominal
        operation in percent. Indicator for converter drive motors. Used
        for short circuit data exchange according to IEC 60909
    :ivar iaIrRatio: Ratio of locked-rotor current to the rated current
        of the motor (Ia/Ir). Used for short circuit data exchange
        according to IEC 60909
    :ivar nominalFrequency: Nameplate data indicates if the machine is
        50 or 60 Hz.
    :ivar nominalSpeed: Nameplate data.  Depends on the slip and number
        of pole pairs.
    :ivar polePairNumber: Number of pole pairs of stator. Used for short
        circuit data exchange according to IEC 60909
    :ivar ratedMechanicalPower: Rated mechanical power (Pr in the IEC
        60909-0). Used for short circuit data exchange according to IEC
        60909.
    :ivar reversible: Indicates for converter drive motors if the power
        can be reversible. Used for short circuit data exchange
        according to IEC 60909
    :ivar rxLockedRotorRatio: Locked rotor ratio (R/X). Used for short
        circuit data exchange according to IEC 60909
    """
    asynchronousMachineType: Optional[AsynchronousMachineKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    converterFedDrive: Optional[bool] = field(
        default=None,
        metadata={
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
    iaIrRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominalFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    nominalSpeed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    polePairNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedMechanicalPower: Optional[float] = field(
        default=None,
        metadata={
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
    rxLockedRotorRatio: Optional[float] = field(
        default=None,
        metadata={
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

    :ivar maxOperatingP: This is the maximum operating active power
        limit the dispatcher can enter for this unit.
    :ivar minOperatingP: This is the minimum operating active power
        limit the dispatcher can enter for this unit.
    :ivar GenUnitOpCostCurves: A generating unit may have one or more
        cost curves, depending upon fuel mixture and fuel cost.
    :ivar GenUnitOpSchedule: A generating unit may have an operating
        schedule, indicating the planned operation of the unit.
    :ivar GrossToNetActivePowerCurves: A generating unit may have a
        gross active power to net active power curve, describing the
        losses and auxiliary power requirements of the unit.
    :ivar RotatingMachine: A synchronous machine may operate as a
        generator and as such becomes a member of a generating unit.
    """
    maxOperatingP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minOperatingP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    GenUnitOpCostCurves: List[GenUnitOpCostCurve] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    GenUnitOpSchedule: Optional[GenUnitOpSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    GrossToNetActivePowerCurves: List[GrossToNetActivePowerCurve] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    RotatingMachine: List[RotatingMachine] = field(
        default_factory=list,
        metadata={
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
    :ivar maxQ: Maximum reactive power limit. This is the maximum
        (nameplate) limit for the unit.
    :ivar minQ: Minimum reactive power limit for the unit.
    :ivar operatingMode: Current mode of operation.
    :ivar type: Modes that this synchronous machine can operate in.
    :ivar InitialReactiveCapabilityCurve: The default reactive
        capability curve for use by a synchronous machine.
    :ivar ReactiveCapabilityCurves: All available reactive capability
        curves for this synchronous machine.
    """
    ikk: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    maxQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    minQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    operatingMode: Optional[SynchronousMachineOperatingMode] = field(
        default=None,
        metadata={
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
    InitialReactiveCapabilityCurve: Optional["ReactiveCapabilityCurve"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ReactiveCapabilityCurves: List["ReactiveCapabilityCurve"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis,
    Pelton, Kaplan).

    :ivar energyConversionCapability: Energy conversion capability for
        generating.
    :ivar hydroUnitWaterCost: The equivalent cost of water that drives
        the hydro turbine.
    :ivar HydroGeneratingEfficiencyCurves: A hydro generating unit has
        an efficiency curve.
    :ivar HydroPowerPlant: The hydro generating unit belongs to a hydro
        power plant.
    :ivar PenstockLossCurve: A hydro generating unit has a penstock loss
        curve.
    :ivar TailbayLossCurve: A hydro generating unit has a tailbay loss
        curve.
    """
    energyConversionCapability: Optional[HydroEnergyConversionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydroUnitWaterCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HydroGeneratingEfficiencyCurves: List[HydroGeneratingEfficiencyCurve] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HydroPowerPlant: Optional["HydroPowerPlant"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    PenstockLossCurve: Optional[PenstockLossCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    TailbayLossCurve: List[TailbayLossCurve] = field(
        default_factory=list,
        metadata={
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
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    hydrogenPressure: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    InitiallyUsedBySynchronousMachines: List[SynchronousMachine] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "min_occurs": 1,
        }
    )
    SynchronousMachines: List[SynchronousMachine] = field(
        default_factory=list,
        metadata={
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

    :ivar oMCost: Operating and maintenance cost for the thermal unit.
    :ivar CAESPlant: A thermal generating unit may be a member of a
        compressed air energy storage plant.
    :ivar CogenerationPlant: A thermal generating unit may be a member
        of a cogeneration plant.
    :ivar CombinedCyclePlant: A thermal generating unit may be a member
        of a combined cycle plant.
    :ivar EmissionCurves: A thermal generating unit may have  one or
        more emission curves.
    :ivar EmmissionAccounts: A thermal generating unit may have one or
        more emission allowance accounts.
    :ivar FossilFuels: A thermal generating unit may have one or more
        fossil fuels.
    :ivar FuelAllocationSchedules: A thermal generating unit may have
        one or more fuel allocation schedules.
    :ivar HeatInputCurve: A thermal generating unit may have a heat
        input curve.
    :ivar HeatRateCurve: A thermal generating unit may have a heat rate
        curve.
    :ivar IncrementalHeatRateCurve: A thermal generating unit may have
        an incremental heat rate curve.
    :ivar ShutdownCurve: A thermal generating unit may have a shutdown
        curve.
    :ivar StartupModel: A thermal generating unit may have a startup
        model.
    """
    oMCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CAESPlant: Optional["CAESPlant"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CogenerationPlant: Optional[CogenerationPlant] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CombinedCyclePlant: Optional[CombinedCyclePlant] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EmissionCurves: List[EmissionCurve] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    EmmissionAccounts: List[EmissionAccount] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FossilFuels: List[FossilFuel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    FuelAllocationSchedules: List[FuelAllocationSchedule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HeatInputCurve: Optional[HeatInputCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    HeatRateCurve: Optional[HeatRateCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    IncrementalHeatRateCurve: Optional[IncrementalHeatRateCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ShutdownCurve: Optional[ShutdownCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    StartupModel: Optional[StartupModel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class WindGeneratingUnit(GeneratingUnit):
    """A wind driven generating unit, connected to the grid by means of a
    rotating machine.

    May be used to represent a single turbine or an aggregation.

    :ivar windGenUnitType: The kind of wind generating unit
    """
    windGenUnitType: Optional[WindGenUnitKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class CAESPlant(PowerSystemResource):
    """
    Compressed air energy storage plant.

    :ivar energyStorageCapacity: The rated energy storage capacity.
    :ivar ratedCapacityP: The CAES plant's gross rated generating
        capacity.
    :ivar AirCompressor: An air compressor may be a member of a
        compressed air energy storage plant.
    :ivar ThermalGeneratingUnit: A thermal generating unit may be a
        member of a compressed air energy storage plant.
    """
    energyStorageCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    ratedCapacityP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    AirCompressor: Optional["AirCompressor"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ThermalGeneratingUnit: Optional[ThermalGeneratingUnit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )


@dataclass
class AirCompressor(PowerSystemResource):
    """
    Combustion turbine air compressor which is an integral part of a compressed
    air energy storage (CAES) plant.

    :ivar airCompressorRating: Rating of the CAES air compressor.
    :ivar CAESPlant: An air compressor may be a member of a compressed
        air energy storage plant.
    """
    airCompressorRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
        }
    )
    CAESPlant: Optional[CAESPlant] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )

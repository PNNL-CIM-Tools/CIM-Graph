from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime

__NAMESPACE__ = "http://iec.ch/TC57/CIM100#"


@dataclass
class ASTMStandard:
    """
    Standard published by ASTM (ASTM International).
    """


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
            "required": True,
        }
    )
    success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


class AsynchronousMachineKind(Enum):
    """
    Kind of Asynchronous Machine.

    :cvar generator: The Asynchronous Machine is a generator.
    :cvar motor: The Asynchronous Machine is a motor.
    """
    generator = "generator"
    motor = "motor"


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


@dataclass
class CIGREStandard:
    """
    Standard published by CIGRE (Council on Large Electric Systems).
    """


class ConstantPowerFactorSettingKind(Enum):
    """The kinds of constant power factor setting.

    Reference: IEEE1547-2018.

    :cvar abs: ABS.
    :cvar inj: INJ.
    """
    abs = "abs"
    inj = "inj"


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
            "required": True,
        }
    )
    isExteriorLighting: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isGenerationSystem: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isHvacCompressorOrFurnace: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isInteriorLighting: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isIrrigationPump: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isManagedCommercialIndustrialLoad: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isPoolPumpSpaJacuzzi: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isSimpleMiscLoad: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isSmartAppliance: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isStripAndBaseboardHeater: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isWaterHeater: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
    :cvar ISK: Icelandic króna.
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
    :cvar PYG: Paraguayan guaraní.
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
    :cvar STD: São Tomé and Príncipe dobra.
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
    :cvar VEF: Venezuelan bolívar fuerte.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    frequencyWattCurveFunction: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxRealPowerLimiting: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rampRateControl: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reactivePowerDispatch: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    realPowerDispatch: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltageRegulation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltVarCurveFunction: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltWattCurveFunction: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class DINStandard:
    """
    Standard published by DIN (German Institute of Standards).
    """


@dataclass
class DateInterval:
    """
    Interval between two dates.

    :ivar end: End date of this interval.
    :ivar start: Start date of this interval.
    """
    end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    start: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    installedDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    notYetInstalledDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    outOfServiceDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    removedDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    currentApparentPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    currentReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxApparentPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minApparentPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EndDevice: Optional["EndDevice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EndDeviceGroup: Optional["EndDeviceGroup"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class DobleStandard:
    """
    Standard published by Doble.
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EPAStandard:
    """
    Standard published by EPA (United States Environmental Protection Agency).
    """


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
            "required": True,
        }
    )
    email2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lan: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    radio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    userID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    web: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    communication: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    connectDisconnect: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    demandResponse: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    electricMetering: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    gasMetering: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    metrology: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    onRequestRead: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    outageHistory: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pressureCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pricingInfo: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pulseOutput: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    relaysProgramming: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reverseFlow: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    superCompressibilityCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    temperatureCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    textMessage: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    waterMetering: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Estimate:
    pass


@dataclass
class ExtensionItem:
    extName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    extType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    extValue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rLineToLine: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xGround: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xLineToLine: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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


@dataclass
class IEC61968CIMVersion:
    """
    IEC 61968 version number assigned to this UML model.

    :ivar date: Form is YYYY-MM-DD for example for January 5, 2009 it is
        2009-01-05.
    :ivar version: Form is IEC61968CIMXXvYY where XX is the major CIM
        package version and the YY is the minor version. For example
        IEC61968CIM10v17.
    """
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IEC61970CIMVersion:
    """
    This is the IEC 61970 CIM version number assigned to this UML model.

    :ivar date: Form is YYYY-MM-DD for example for January 5, 2009 it is
        2009-01-05.
    :ivar version: Form is IEC61970CIMXXvYY where XX is the major CIM
        package version and the YY is the minor version. For example
        IEC61970CIM13v18.
    """
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IEC62325CIMVersion:
    """
    IEC 62325 version number assigned to this UML model.

    :ivar date: Form is YYYY-MM-DD for example for January 5, 2009 it is
        2009-01-05.
    :ivar version: Form is IEC62325CIMXXvYY where XX is the major CIM
        package version and the YY is the minor version. For example
        IEC62325CIM10v03.
    """
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IECStandard:
    """
    Standard published by IEC (International Electrotechnical Commission).
    """


@dataclass
class IEEE1547ControlSettings:
    constantPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    constantReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceIntentionalDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceMaxFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceMaxVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceMinFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceMinVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    frequencyDroopResponseTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    openLoopResponseTimeP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    overFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    overFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeConstantOpenLoop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeConstantReferenceVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    underFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    underFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltVarQ1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltVarQ2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltVarQ3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltVarQ4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltVarV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltVarV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltVarV3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltVarV4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltWattP1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltWattP2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltWattV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltWattV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wattVarP1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wattVarP2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wattVarP3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wattVarP4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wattVarQ1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wattVarQ2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wattVarQ3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    wattVarQ4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IEEE1547Setting:
    constantPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    constantReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceIntentionalDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceMaxFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceMaxVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceMinFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enterServiceMinVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    frequencyDroopResponseTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    islandClearingTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    openLoopResponseTimeP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    overFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    overFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeConstantOpenLoop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeConstantReferenceVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    underFrequencyDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    underFrequencyDroop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IEEE1547TripSettings:
    OF1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    OF2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    OV1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    OV2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    UF1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    UF2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    UV1time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    UV2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IEEEStandard:
    """
    Standard published by IEEE (Institute of Electrical and Electronics
    Engineers).
    """


@dataclass
class ISOStandard:
    """
    Standard published by ISO (International Organization for Standardization).
    """


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
    """
    mRID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    aliasName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    notReadyForUseDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    readyForUseDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class LaborelecStandard:
    """
    Standard published by Laborelec.
    """


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
            "required": True,
        }
    )
    manufacturedDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    purchaseDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    receivedDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    removalDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    retiredDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class MonthDayInterval:
    """
    Interval between two times specified as mont and date.

    :ivar end: End time of this interval.
    :ivar start: Start time of this interval.
    """
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class NameTypeAuthority:
    """
    Authority responsible for creation and management of names of a given type;
    typically an organization or an enterprise system.

    :ivar description: Description of the name type authority.
    :ivar name: Name of the name type authority.
    """
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class NonlinearShuntCompensatorPhasePoint:
    """
    A per phase non linear shunt compensator bank or section admittance value.

    :ivar b: Positive sequence shunt (charging) susceptance per section
    :ivar g: Positive sequence shunt (charging) conductance per section
    :ivar sectionNumber: The number of the section.
    """
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sectionNumber: Optional[int] = field(
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
    """
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    b0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sectionNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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


@dataclass
class OverfrequencyTripCurveData:
    pass


@dataclass
class OvervoltageTripCurveData:
    pass


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
    :ivar ReadingType: Reading type resulting from this pending
        conversion.
    """
    multiplyBeforeAdd: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    scalarDenominator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    scalarFloat: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    scalarNumerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rank: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    numerator: Optional[int] = field(
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
            "required": True,
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
    """
    reportingIntervalPeriod: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


class SVCControlMode(Enum):
    """
    Static VAr Compensator control mode.
    """
    reactivePower = "reactivePower"
    voltage = "voltage"


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
    """
    accessMethod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    needsInspection: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    siteAccessProblem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    addressGeneral2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    addressGeneral3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    buildingName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    suiteNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    withinTownLimits: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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


@dataclass
class TAPPIStandard:
    """
    Standard published by TAPPI.
    """


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
            "required": True,
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    step: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    cityCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    countryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dialOut: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    internationalPrefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ituPhone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    localNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    start: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    section: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    stateOrProvince: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class UKMinistryOfDefenceStandard:
    """
    Standard published by United Kingdom Ministry of Defence.
    """


@dataclass
class UnderfrequencyTripCurveData:
    pass


@dataclass
class UndervoltageTripCurveData:
    pass


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
            "required": True,
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
            "required": True,
        }
    )
    revision: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class VoltVarCurveData:
    pass


@dataclass
class VoltWattCurveData:
    pass


@dataclass
class WEPStandard:
    """Standard published by Westinghouse - a WEP (Westinghouse Engineering Procedure)."""


@dataclass
class WattVarCurveData:
    pass


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


@dataclass
class Appointment(IdentifiedObject):
    """
    Meeting time and location.

    :ivar callAhead: True if requested to call customer when someone is
        about to arrive at their premises.
    :ivar meetingInterval: Date and time reserved for appointment.
    """
    callAhead: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    meetingInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
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
            "required": True,
        }
    )


@dataclass
class BaseVoltage(IdentifiedObject):
    """
    Defines a system base voltage which is referenced.

    :ivar nominalVoltage: The power system resource's base voltage.
    """
    nominalVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value1Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value1Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value2Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value2Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    maximumActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maximumReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minimumActivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minimumReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    monitorActivePower: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    monitorReactivePower: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    crsUrn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class CrewType(IdentifiedObject):
    """Custom description of the type of crew.

    This may be used to determine the type of work the crew can be
    assigned to. Examples include repair, tree trimming, switching, etc.
    """


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
    """
    curveStyle: Optional[CurveStyle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xMultiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xUnit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    y1Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    y1Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    y2Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    y2Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    y3Multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    y3Unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class DERDynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to DER dynamics models.
    """


@dataclass
class DERGroupDispatch(IdentifiedObject):
    pass


@dataclass
class DERGroupForecast(IdentifiedObject):
    predictionCreationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class DERMonitorableParameter:
    yMultiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    yUnitInstalledMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    yUnitInstalledMin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERCurveData: Optional["DERCurveData"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    abnormalOPcatKind: Optional[AbnormalOPcatKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    acVmax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    acVmin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fwVer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    normalOPcatKind: Optional[NormalOPcatKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reactiveSusceptance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    serialNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    supportsConstPFmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    supportsConstQmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    supportsPFmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    supportsPVmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    supportsQPmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    supportsQVmode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class DayType(IdentifiedObject):
    """Group of similar days.

    For example it could be used to represent weekdays, weekend, or
    holidays.
    """


@dataclass
class DecimalQuantity:
    """
    :ivar currency: Quantity with decimal value and associated unit or
        currency information.
    :ivar multiplier:
    :ivar unit:
    :ivar value:
    """
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    multiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar validityInterval: Interval within which the program is valid.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    validityInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    eventOrAction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    subDomain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    eventOrAction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    subDomain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar DERFunction:
    :ivar DispatchablePowerCapability:
    :ivar status:
    :ivar version:
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERFunction: Optional[DERFunction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DispatchablePowerCapability: Optional[DispatchablePowerCapability] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    version: Optional[Version] = field(
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
    :ivar interval: Start and end time of an interval during which end
        device control actions are to be executed.
    """
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    durationIndefinite: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
class EnergyConnectionProfile(IdentifiedObject):
    """Optional references to shapes for OpenDSS, and players or schedules for
    GridLAB-D.

    See attribute documentation for applicability.  The shapes, players,
    and schedules are not maintained in CIM, i.e., they must be made
    available to the simulator from an external source.

    :ivar dssDaily: Reference to OpenDSS Daily curve, for Load, Storage,
        PVSystem, Generator, and WindGen power
    :ivar dssDuty: Reference to OpenDSS Duty Cycle curve, for Load,
        Storage, PVSystem, Generator, and WindGen power
    :ivar dssLoadCvrCurve: Reference to OpenDSS CvrCurve, for Load
        objects
    :ivar dssLoadGrowth: Reference to OpenDSS Growth curve, for Load
        objects
    :ivar dssPVTDaily: Reference to OpenDSS Daily curve, for PVSystem
        temperature
    :ivar dssPVTDuty: Reference to OpenDSS Duty Cycle curve, for
        PVSystem temperature
    :ivar dssPVTYearly: Reference to OpenDSS Yearly curve, for PVSystem
        temperature
    :ivar dssSpectrum: Reference to OpenDSS harmonic current Spectrum,
        for Load, Storage, PVSystem, Generator, and WindGen power
    :ivar dssYearly: Reference to OpenDSS Yearly curve, for Load,
        Storage, PVSystem, Generator, and WindGen power
    :ivar gldPlayer: GridLAB-D Player for base_power attributes on Load
        and Triplex_Load objects, and P_Out for Battery objects.
        Netlisted as player.value.
    :ivar gldSchedule: GridLAB-D schedule for base_power attributes on
        Load and Triplex_Load objects, and P_Out attributes on Battery
        objects.
    """
    dssDaily: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dssDuty: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dssLoadCvrCurve: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dssLoadGrowth: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dssPVTDaily: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dssPVTDuty: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dssPVTYearly: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dssSpectrum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dssYearly: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    gldPlayer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    gldSchedule: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ExtensionsList:
    extensionsItem: Optional[ExtensionItem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class FaultCauseType(IdentifiedObject):
    """
    Type of cause of the fault.
    """


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
            "required": True,
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dbuf: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    kof: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    kuf: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    olrt: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    of1TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    of2TripF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    of2TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    uf1TripF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    uf1TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    uf2TripF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    uf2TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class GeographicalRegion(IdentifiedObject):
    """
    A geographical region of a power system network model.
    """


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
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IOPoint(IdentifiedObject):
    """The class describe a measurement or control value.

    The purpose is to enable having attributes and associations common
    for measurement and control.
    """


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
            "required": True,
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Limit(IdentifiedObject):
    """Specifies one limit value for a Measurement.

    A Measurement typically has several limits that are kept together by
    the LimitSet class. The actual meaning and use of a Limit instance
    (i.e., if it is an alarm or warning limit or if it is a high or low
    limit) is not captured in the Limit class. However the name of a
    Limit instance may indicate both meaning and use.
    """


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
            "required": True,
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
    :ivar pFrequencyExponent:
    :ivar pVoltageExponent: Exponent of per unit voltage effecting real
        power.
    :ivar qConstantCurrent: Portion of reactive power load modeled as
        constant current.
    :ivar qConstantImpedance: Portion of reactive power load modeled as
        constant impedance.
    :ivar qConstantPower: Portion of reactive power load modeled as
        constant power.
    :ivar qFrequencyExponent:
    :ivar qVoltageExponent: Exponent of per unit voltage effecting
        reactive power.
    """
    exponentModel: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pConstantCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pConstantImpedance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pConstantPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pFrequencyExponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pVoltageExponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    qConstantCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    qConstantImpedance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    qConstantPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    qFrequencyExponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    qVoltageExponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class MeasurementValueSource(IdentifiedObject):
    """MeasurementValueSource describes the alternative sources updating a
    MeasurementValue.

    User conventions for how to use the MeasurementValueSource
    attributes are described in the introduction to IEC 61970-301.
    """


@dataclass
class Medium(IdentifiedObject):
    """
    A substance that either (1) provides the means of transmission of a force
    or effect, such as hydraulic fluid, or (2) is used for a surrounding or
    enveloping substance, such as oil in a transformer or circuit breaker.

    :ivar volumeSpec: The volume of the medium specified for this
        application. Note that the actual volume is a type of
        measurement associated witht the asset.
    """
    volumeSpec: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class MetrologyRequirement(IdentifiedObject):
    """
    A specification of the metering requirements for a particular point within
    a network.
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hvrtT2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hvrtV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hvrtV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lvrtT1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lvrtT2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lvrtV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lvrtV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar NameTypeAuthority: Authority responsible for managing names of
        this type.
    """
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    NameTypeAuthority: Optional[NameTypeAuthority] = field(
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
    """


@dataclass
class OperatingParticipant(IdentifiedObject):
    """An operator of multiple power system resource objects.

    Note multple operating participants may operate the same power
    system resource object.   This can be used for modeling jointly
    owned units where each owner operates as a contractual share.
    """


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
    """
    acceptableDuration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    direction: Optional[OperationalLimitDirectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class PSRType(IdentifiedObject):
    """Classifying instances of the same class, e.g. overhead and underground
    ACLineSegments.

    This classification mechanism is intended to provide flexibility
    outside the scope of this standard, i.e. provide customisation that
    is non standard.
    """


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
    """
    firstName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lastName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    mName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    specialNeed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    electronicAddress: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    landlinePhone: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    mobilePhone: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class PhaseTapChangerTable(IdentifiedObject):
    """
    Describes a tabular curve for how the phase angle difference and impedance
    varies with the tap step.
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
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
            "required": True,
        }
    )
    estimatorReplaced: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    failure: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    oldData: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    operatorBlocked: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    oscillatory: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    outOfRange: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    overFlow: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    suspect: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    test: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class RatioTapChangerTable(IdentifiedObject):
    """
    Describes a curve for how the voltage magnitude and impedance varies with
    the tap step.
    """


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
    """
    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    subCategory: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    systemId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ReadingType(IdentifiedObject):
    """Detailed description for a type of a reading value.

    Values in attributes allow for the creation of recommended codes to be used for identifying reading value types as follows: &amp;lt;macroPeriod&amp;gt;.&amp;lt;aggregate&amp;gt;.&amp;lt;measuringPeriod&amp;gt;.&amp;lt;accumulation&amp;gt;.&amp;lt;flowDirection&amp;gt;.&amp;lt;commodity&amp;gt;.&amp;lt;measurementKind&amp;gt;.&amp;lt;interharmonic.numerator&amp;gt;.&amp;lt;interharmonic.denominator&amp;gt;.&amp;lt;argument.numerator&amp;gt;.&amp;lt;argument.denominator&amp;gt;.&amp;lt;tou&amp;gt;.&amp;lt;cpp&amp;gt;.&amp;lt;consumptionTier&amp;gt;.&amp;lt;phases&amp;gt;.&amp;lt;multiplier&amp;gt;.&amp;lt;unit&amp;gt;.&amp;lt;currency&amp;gt;.

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
    :ivar PendingCalculation: Pending calculation that produced this
        reading type.
    """
    consumptionTier: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    cpp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    multiplier: Optional[UnitMultiplier] = field(
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
            "required": True,
        }
    )
    tou: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    argument: Optional[RationalNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Channel: Optional["Channel"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    interharmonic: Optional[ReadingInterharmonic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PendingCalculation: Optional[PendingCalculation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ReportingGroup(IdentifiedObject):
    """
    A reporting group is used for various ad-hoc groupings used for reporting.
    """


@dataclass
class ReportingSuperGroup(IdentifiedObject):
    """
    A reporting super group, groups reporting groups for a higher level report.
    """


@dataclass
class RightOfWay(IdentifiedObject):
    pass


@dataclass
class Season(IdentifiedObject):
    """
    A specified time period of the year.

    :ivar endDate: Date season ends.
    :ivar startDate: Date season starts.
    """
    endDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    startDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ServiceCategory(IdentifiedObject):
    """
    Category of service provided to the customer.
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    highFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    highVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lowFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lowVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    permitService: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rampRate: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    randomizedDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    postalCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    streetDetail: Optional[StreetDetail] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    townDetail: Optional[TownDetail] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    unit: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value: Optional[str] = field(
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
            "required": True,
        }
    )
    sections: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
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
            "required": True,
        }
    )
    lifetimeMotorStarts: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lifetimeTotalOperations: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    mostRecentFaultOperationDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    mostRecentMotorStartDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    mostRecentOperationDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    testStandardASTM: Optional[ASTMStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardCIGRE: Optional[CIGREStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardDIN: Optional[DINStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardDoble: Optional[DobleStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardEPA: Optional[EPAStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardIEC: Optional[IECStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardIEEE: Optional[IEEEStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardISO: Optional[ISOStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardLaborelec: Optional[LaborelecStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardTAPPI: Optional[TAPPIStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardUKMinistryOfDefence: Optional[UKMinistryOfDefenceStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testStandardWEP: Optional[WEPStandard] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ThermostatController(IdentifiedObject):
    """
    a price-responsive or bidding smart thermostat.

    :ivar baseSetpoint: user's desired thermostat setpoint, including
        the effects of pre-programmed schedule
    :ivar priceCap: maximum price per kwh that the controller will bid,
        regardless of the market's price cap
    :ivar rangeHigh: maximum postive offset to the thermostat setpoint
    :ivar rangeLow: maximum negative offset to the thermostat setpoint
    :ivar House:
    """
    baseSetpoint: Optional[float] = field(
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
    """
    AngleRefTopologicalNode: Optional["TopologicalNode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar TransformerEndInfo: Transformer end datasheet used to
        calculate this core admittance.
    """
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    b0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TransformerEndInfo: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar r0:
    :ivar x: Positive sequence series reactance of the transformer end.
    :ivar x0: Zero sequence series reactance of the transformer end.
    :ivar TransformerEndInfo: Transformer end datasheet used to
        calculate this transformer star impedance.
    """
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TransformerEndInfo: Optional["TransformerEndInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    temperature: Optional[float] = field(
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
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveQ2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveQ3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveQ4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveV3: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveV4: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    olrt: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    vRef: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    vRefAutoModeEnabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    vRefOlrt: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveP2gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveP2load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveV1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveV2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    olrt: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ov1TripV: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ov2TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ov2TripV: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    uv1TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    uv1TripV: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    uv2TripT: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    uv2TripV: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveP1load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveP2gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveP2load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveP3gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveP3load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveQ1gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveQ1load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveQ2gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveQ2load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveQ3gen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveQ3load: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional["DERIEEEType1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class AccumulatorLimitSet(LimitSet):
    """
    An AccumulatorLimitSet specifies a set of Limits that are associated with
    an Accumulator measurement.
    """


@dataclass
class AnalogLimitSet(LimitSet):
    """
    An AnalogLimitSet specifies a set of Limits that are associated with an
    Analog measurement.
    """


@dataclass
class AssetDeployment(IdentifiedObject):
    """
    Deployment of asset deployment in a power system resource role.

    :ivar likelihoodOfFailure: Likelihood of asset failure on a scale of
        1(low) to 100 (high).
    :ivar Asset: Asset in this deployment.
    :ivar BaseVoltage: Base voltage of this network asset deployment.
    :ivar deploymentDate: Dates of asset deployment.
    """
    likelihoodOfFailure: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    BaseVoltage: Optional[BaseVoltage] = field(
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
            "required": True,
        }
    )


@dataclass
class AssetLocationHazard(Hazard):
    """Potential hazard related to the location of an asset.

    Examples are trees growing under overhead power lines, a park being
    located by a substation (i.e., children climb fence to recover a
    ball), a lake near an overhead distribution line (fishing pole/line
    contacting power lines), dangerous neighbour, etc.
    """


@dataclass
class CatalogAssetType(IdentifiedObject):
    """
    assets that may be used for planning, work or design purposes.

    :ivar estimatedUnitCost: Estimated unit cost (or cost per unit
        length) of this type of asset. It does not include labor to
        install, construct or configure it.
    :ivar stockItem: True if item is a stock item (default).
    :ivar type:
    :ivar AssetInfo:
    :ivar quantity: The value, unit of measure, and multiplier for the
        quantity.
    """
    estimatedUnitCost: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    stockItem: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetInfo: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    quantity: Optional[StringQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    y1value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    y2value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    y3value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Curve: Optional[Curve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseToNeutralApplicable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseToPhaseApplicable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ConstantPowerFactorSettings: Optional["ConstantPowerFactorSettings"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ConstantReactivePowerSettings: Optional[ConstantReactivePowerSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DerNameplateData: Optional[DERNameplateData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    FrequencyDroopSettings: Optional[FrequencyDroopSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    FrequencyTripSettings: Optional[FrequencyTripSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    MomentaryCessationSettings: Optional[MomentaryCessationSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PowerLimitSettings: Optional[PowerLimitSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ServiceSettings: Optional[ServiceSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    VoltageTripSettings: Optional[VoltageTripSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    VoltVarSettings: Optional[VoltVarSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    VoltWattSettings: Optional[VoltWattSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    WattVarSettings: Optional[WattVarSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    apparentPowerChargeMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    overPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pMaxCharge: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pMaxOverPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pMaxUnderPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    qMaxAbs: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    qMaxInj: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    underPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERNameplateData: Optional[DERNameplateData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar DERMonitorableParameter:
    """
    confidence: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    curveStyleKind: Optional[CurveStyle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    numberOfIntervals: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    startTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    DERMonitorableParameter: Optional[DERMonitorableParameter] = field(
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
    """
    drProgramLevel: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    drProgramMandatory: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    issuerID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    issuerTrackingID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EndDeviceAction: Optional["EndDeviceAction"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    priceSignal: Optional[FloatQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    primaryDeviceTiming: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    scheduledInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    secondaryDeviceTiming: Optional[EndDeviceTiming] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    actualPurchaseCost: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    costDescription: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    costType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    financialValue: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    plantTransferDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    purchaseDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    purchaseOrderNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    valueDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    warrantyEndDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Asset: Optional["Asset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    quantity: Optional[IntegerQuantity] = field(
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
            "required": True,
        }
    )
    auxPowerOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    heatInputEff: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    heatInputOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isNetGrossP: Optional[bool] = field(
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
    EnergyConsumer: Optional["EnergyConsumer"] = field(
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
            "required": True,
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
class IrregularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them varies.
    """


@dataclass
class LoadArea(EnergyArea):
    """
    The class is the root or first level in a hierarchical structure for
    grouping of loads for the purpose of load flow load scaling.
    """


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
    :ivar CoordinateSystem: Coordinate system used to describe position
        points of this location.
    :ivar electronicAddress: Electronic address.
    :ivar mainAddress: Main address of the location.
    :ivar phone1: Phone number.
    :ivar phone2: Additional phone number.
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
            "required": True,
        }
    )
    geoInfoReference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CoordinateSystem: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    electronicAddress: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    mainAddress: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phone1: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phone2: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    secondaryAddress: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    IdentifiedObject: Optional[IdentifiedObject] = field(
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

    :ivar OperationalLimitType: The limit type associated with this
        limit.
    """
    OperationalLimitType: Optional[OperationalLimitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar streetAddress: Street address.
    """
    electronicAddress: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ParentOrganisation: Optional["ParentOrganization"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phone1: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phone2: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    postalAddress: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    streetAddress: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class OverfrequencyTripCurve(Curve):
    pass


@dataclass
class OvervoltageTripCurve(Curve):
    pass


@dataclass
class ParallelLineSegment(IdentifiedObject):
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
class PersonRole(IdentifiedObject):
    """
    :ivar Person: Person having this role.
    """
    Person: Optional[Person] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    PhaseTapChangerTable: Optional[PhaseTapChangerTable] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class RatioTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the ratio tap changer tabular curve.

    :ivar RatioTapChangerTable: Table of this point.
    """
    RatioTapChangerTable: Optional[RatioTapChangerTable] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    coolantTemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hydrogenPressure: Optional[float] = field(
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
    """
    endTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeStep: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    shutdownDate: Optional[XmlDateTime] = field(
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
            "required": True,
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
            "required": True,
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
            "required": True,
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

    :ivar Region: The geographical region to which this sub-geographical
        region is within.
    """
    Region: Optional[GeographicalRegion] = field(
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
            "required": True,
        }
    )
    lowLevelLimit: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
class UnderfrequencyTripCurve(Curve):
    pass


@dataclass
class UndervoltageTripCurve(Curve):
    pass


@dataclass
class UserAttribute:
    """
    Generic name-value pair class, with optional sequence number and units for
    value; can be used to model parts of information exchange when concrete
    types are not known in advance.

    :ivar name: Name of an attribute.
    :ivar sequenceNumber: Sequence number for this attribute in a list
        of attributes.
    :ivar value: Value of an attribute, including unit information.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value: Optional[StringQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    ValueAliasSet: Optional[ValueAliasSet] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class VoltVarCurve(Curve):
    pass


@dataclass
class VoltWattCurve(Curve):
    pass


@dataclass
class WattVarCurve(Curve):
    pass


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
            "required": True,
        }
    )
    LimitSet: Optional[AccumulatorLimitSet] = field(
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
            "required": True,
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    LimitSet: Optional[AnalogLimitSet] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    powerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERIEEEType1: Optional[DERIEEEType1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Crew(IdentifiedObject):
    """
    Group of people with specific skills, tools, and vehicles.

    :ivar CrewType: Type of this crew.
    :ivar Location:
    :ivar status: Status of this crew.
    """
    CrewType: Optional[CrewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    value: Optional[float] = field(
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
            "required": True,
        }
    )
    maxYValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minYValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    nominalYValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERMonitorableParameter: Optional[DERMonitorableParameter] = field(
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
            "required": True,
        }
    )


@dataclass
class DocumentPersonRole(PersonRole):
    """
    Person role with respect to documents.
    """


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
            "required": True,
        }
    )
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    durationIndefinite: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    startDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EndDeviceControl: Optional[EndDeviceControl] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EnvironmentalLocationType:
    """Kind of environmental location.

    Used when an environmental alert or phenomenon has multiple
    locations associated with it.

    :ivar Location: Location of this instance of ths kind of
        environmental location.
    """
    Location: Optional[Location] = field(
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
            "required": True,
        }
    )
    value1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IntervalSchedule: Optional[IrregularIntervalSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    sensorAccuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    MeasurementValueQuality: Optional[MeasurementValueQuality] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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


@dataclass
class OperationPersonRole(PersonRole):
    """
    Person role in the context of utility operations.
    """


@dataclass
class OrganisationRole(IdentifiedObject):
    """
    Identifies a way in which an organisation may participate in the utility
    enterprise (e.g., customer, manufacturer, etc).

    :ivar Organisation: Organisation having this role.
    """
    Organisation: Optional[Organisation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ParentOrganization(Organisation):
    pass


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
            "required": True,
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xPosition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    yPosition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    zPosition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    value1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IntervalSchedule: Optional[RegularIntervalSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    Season: Optional[Season] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    hotStandbyHeat: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    incrementalMaintCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minimumDownTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minimumRunTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    riskFactorCost: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    startupCost: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    startupDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    startupPriority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    stbyAuxP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    StartIgnFuelCurve: Optional[StartIgnFuelCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    StartMainFuelCurve: Optional[StartMainFuelCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    StartRampCurve: Optional[StartRampCurve] = field(
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
class SubLoadArea(EnergyArea):
    """
    The class is the second level in a hierarchical structure for grouping of
    loads for the purpose of load flow load scaling.

    :ivar LoadArea: The LoadArea where the SubLoadArea belongs.
    """
    LoadArea: Optional[LoadArea] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    accessMethod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    siteAccessProblem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Approver(DocumentPersonRole):
    """
    Person who accepted/signed or rejected the document.
    """


@dataclass
class AssetOrganisationRole(OrganisationRole):
    """
    Role an organisation plays with respect to asset.
    """


@dataclass
class Author(DocumentPersonRole):
    """
    Person who created document or activity record.
    """


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
    :ivar timePeriod: Start and end of the period for those readings
        whose type has a time attribute such as 'billing', seasonal' or
        'forTheSpecifiedPeriod'.
    """
    reportedDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timePeriod: Optional[DateTimeInterval] = field(
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
    Crew: Optional[Crew] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Customer(OrganisationRole):
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
    :ivar priority: Priority of the customer.
    :ivar status: Status of this customer.
    """
    locale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pucNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    specialNeed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    vip: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    priority: Optional[Priority] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Editor(DocumentPersonRole):
    """
    Person who modified the document.
    """


@dataclass
class EnvironmentalDataAuthority(OrganisationRole):
    """
    An entity defining classifications or categories of environmental
    information, like phenomena or alerts.
    """


@dataclass
class EnvironmentalDataProvider(OrganisationRole):
    """Entity providing environmental data.

    Could be an observed weather data provider, an entity providing
    forecasts, an authority providing alerts, etc.
    """


@dataclass
class FieldDispatchHistory(IdentifiedObject):
    """
    The history of field dispatch statuses for this work.
    """
    Crew: Optional[Crew] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Issuer(DocumentPersonRole):
    """
    Person who issued the document and is responsible for its content.
    """


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
class Manufacturer(OrganisationRole):
    """
    Organisation that manufactures asset products.
    """


@dataclass
class Operator(OperationPersonRole):
    """
    Control room operator.
    """


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
            "required": True,
        }
    )
    cancelControlMode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    cancelDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    cancelNow: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    coolingOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    coolingSetpoint: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    criticalityLevel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dutyCycle: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    enrollmentGroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    heatingOffset: Optional[float] = field(
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
    appliance: Optional[ControlledAppliance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    confirmationRequired: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    textMessage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class PanPricing(EndDeviceAction):
    """
    PAN action/command used to issue pricing information to a PAN device.

    :ivar providerID: Unique identifier for the commodity provider.
    """
    providerID: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar reason: Reason for event resulting in this activity record,
        typically supplied when user initiated.
    :ivar severity: Severity level of event resulting in this activity
        record.
    :ivar type: Type of event resulting in this activity record.
    :ivar Author: Author of this activity record.
    :ivar status: Information on consequence of event resulting in this
        activity record.
    """
    createdDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    severity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Author: Optional[Author] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class AlertTypeList(IdentifiedObject):
    """A named list of alert types.

    Note:  the name of the list is reflected in the .name attribute (inherited from IdentifiedObject).

    :ivar version: The version of the named list of alert types.
    :ivar EnvironmentalDataAuthority: The environmental data authority
        responsible for publishing this list of alert types.
    """
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EnvironmentalDataAuthority: Optional[EnvironmentalDataAuthority] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class AssetOwner(AssetOrganisationRole):
    """
    Owner of the asset.
    """


@dataclass
class AssetTestLab(AssetOrganisationRole):
    """
    Test lab that performs various types of testing related to assets.
    """


@dataclass
class AssetTestSampleTaker(AssetOrganisationRole):
    pass


@dataclass
class AssetUser(AssetOrganisationRole):
    """
    Organisation that is a user of the asset.
    """


@dataclass
class ConformLoadGroup(LoadGroup):
    """
    A group of loads conforming to an allocation pattern.
    """


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
    :ivar Customer: Customer requiring this notification.
    """
    contactType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    contactValue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    earliestDateTimeToCall: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    latestDateTimeToCall: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    createdDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lastModifiedDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    revisionNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    subject: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Approver: Optional[Approver] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Author: Optional[Author] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    docStatus: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Editor: Optional[Editor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    electronicAddress: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Issuer: Optional[Issuer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EnvironmentalInformation(IdentifiedObject):
    """
    Abstract class (with concrete child classes of Observation and Forecast)
    that groups phenomenon and/or environmental value sets.

    :ivar created: The timestamp of when the forecast was created
    :ivar EnvironmentalDataProvider: Environmental data provider
        supplying this environmental information.
    """
    created: Optional[XmlDateTime] = field(
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
            "required": True,
        }
    )


@dataclass
class FieldDispatchStep:
    """
    Details of the step in the field dispatch history.

    :ivar occurredDateTime: The date and time at which the dispatch
        status occurred.
    :ivar remarks: freeform comments related to the dispatch to perform
        field work.
    :ivar sequenceNumber: The sequence number of the field dispatch step
        within the field dispatch history.  Begins with 1 and increments
        up.
    :ivar FieldDispatchHistory:
    """
    occurredDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    FieldDispatchHistory: Optional[FieldDispatchHistory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IntervalReading(BaseReading):
    """Data captured at regular intervals of time.

    Interval data could be captured as incremental data, absolute data, or relative data. The source for the data is usually a tariff quantity or an engineering quantity. Data is typically captured in time-tagged, uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min.
    Note: Interval Data is sometimes also called "Interval Data Readings" (IDR).
    """


@dataclass
class Maintainer(AssetOrganisationRole):
    """
    Organisation that maintains assets.
    """


@dataclass
class NonConformLoadGroup(LoadGroup):
    """
    Loads that do not follow a daily and seasonal load variation pattern.
    """


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
            "required": True,
        }
    )
    alternateCostUnit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    currentTimeDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    generationPrice: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    generationPriceRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    priceRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    priceTier: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    priceTierCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    priceTierLabel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rateLabel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    registerTier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    unitOfMeasure: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PanPricing: Optional[PanPricing] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class PhenomenonTypeification(IdentifiedObject):
    """
    A pre-defined phenomenon classification as defined by a particular
    authority.

    :ivar EnvironmentalDataAuthority: Authority defining this
        environmental phenomenon.
    """
    class Meta:
        name = "PhenomenonClassification"

    EnvironmentalDataAuthority: Optional[EnvironmentalDataAuthority] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ProductAssetModel(IdentifiedObject):
    """
    Asset model by a specific manufacturer.

    :ivar catalogueNumber: Catalogue number for asset model.
    :ivar drawingNumber: Drawing number for asset model.
    :ivar instructionManual: Reference manual or instruction book for
        this asset model.
    :ivar modelNumber: Manufacturer's model number.
    :ivar modelVersion: Version number for product model, which
        indicates vintage of the product.
    :ivar overallLength: Overall length of this asset model.
    :ivar styleNumber: Style number of asset model.
    :ivar AssetInfo:
    :ivar CatalogAssetType:
    :ivar Manufacturer: Manufacturer of this asset model.
    """
    catalogueNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    drawingNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    instructionManual: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    modelNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    modelVersion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    overallLength: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    styleNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetInfo: Optional["AssetInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CatalogAssetType: Optional[CatalogAssetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Manufacturer: Optional[Manufacturer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Reading(BaseReading):
    """Specific value measured by a meter or other asset, or calculated by a
    system.

    Each Reading is associated with a specific ReadingType.

    :ivar ReadingType: Type information for this reading value.
    """
    ReadingType: Optional[ReadingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Reading: Optional[BaseReading] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    validityInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Analytic(Document):
    """
    An algorithm or calculation for making an assessment about an asset or
    asset grouping for lifecycle decision making.

    :ivar bestValue: Value that indicates best possible numeric value.
    :ivar worstValue: Value that indicates worst possible numeric value.
    """
    bestValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    worstValue: Optional[float] = field(
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
    """


@dataclass
class AssetInfo(IdentifiedObject):
    """Set of attributes of an asset, representing typical datasheet
    information of a physical device that can be instantiated and shared in
    different data exchange contexts:

    - as attributes of an asset instance (installed or in stock)
    - as attributes of an asset model (product by a manufacturer)
    - as attributes of a type asset (generic type of an asset as used in designs/extension planning).
    """
    CatalogAssetType: Optional[CatalogAssetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ProductAssetModel: Optional[ProductAssetModel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TypeificationCondition(IdentifiedObject):
    """
    A classification condition used to define preconditions that must be met by
    a phenomena classification.

    :ivar duration: The duration of the of the condition in seconds
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
            "required": True,
        }
    )
    PhenomenonClassification: Optional[PhenomenonTypeification] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    ConformLoadGroup: Optional[ConformLoadGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar Customer: Customer owning this account.
    """
    billingCycle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    budgetBill: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lastBillAmount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar inEffect: The interval for which this weather alert is in
        effect.
    """
    alertType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    cancelledDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    headline: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    inEffect: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EnvironmentalEvent(ActivityRecord):
    """
    An environmental event tied to an observation that will be recorded against
    or affect one or more assets.
    """


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

    :ivar NamedPhenomenon: The identified phenomenon to which this
        environmental phenomenon is associated.
    :ivar PhenomenonClassification:
    :ivar timeInterval: The timestamp of the phenomenon as a single
        point or time interval.
    """
    NamedPhenomenon: Optional[NamedPhenomenon] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PhenomenonClassification: Optional[PhenomenonTypeification] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class FailureEvent(ActivityRecord):
    """An event where an asset has failed to perform its functions within
    specified parameters.

    This class is intended to reflect the failure itself. Additional
    information resulting from forensic analysis could be captured by a
    diagnosis data set.

    :ivar corporateCode: Code for asset failure.
    :ivar failureDateTime: Time and date of asset failure.
    :ivar faultLocatingMethod: The method used for locating the faulted
        part of the asset. For example, cable options include: Cap
        Discharge-Thumping, Bridge Method, Visual Inspection, Other.
    :ivar location: Failure location on an object.
    :ivar rootCause: Root cause of asset failure.
    """
    corporateCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    failureDateTime: Optional[XmlDateTime] = field(
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
            "required": True,
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rootCause: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
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
    NonConformLoadGroup: Optional[NonConformLoadGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Observation(EnvironmentalInformation):
    """
    Observed (actual non-forecast) values sets and/or phenomena.
    """


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
    :ivar taxExemption: True if this pricing structure is not taxable.
    :ivar ServiceCategory: Service category to which this pricing
        structure applies.
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dailyCeilingUsage: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dailyEstimatedUsage: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    dailyFloorUsage: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    taxExemption: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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


@dataclass
class Procedure(Document):
    """
    Documented procedure for various types of work or work tasks on assets.

    :ivar instruction: Textual description of this procedure.
    :ivar sequenceNumber: Sequence number in a sequence of procedures
        being performed.
    """
    instruction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Specimen(IdentifiedObject):
    """
    Sample or specimen of a material (fluid or solid).

    :ivar ambientTemperatureAtSampling: Operating ambient temperature
        (in °C).
    :ivar humidityAtSampling: Operating ambient humidity (in percent).
    :ivar specimenID: Identifier of specimen used in inspection or test.
    :ivar specimenSampleDateTime: Date and time sample specimen taken.
    :ivar specimenToLabDateTime: Date and time the specimen was received
        by the lab.
    :ivar AssetTestSampleTaker: Test sampler taker who gathered this
        specimen.
    """
    ambientTemperatureAtSampling: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    humidityAtSampling: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    specimenID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    specimenSampleDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    specimenToLabDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetTestSampleTaker: Optional[AssetTestSampleTaker] = field(
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
    """
    endDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    startDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    disabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    offset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    recurrencePattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    recurrencePeriod: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    scheduleInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar resolvedDateTime: Date and time this trouble ticket has been
        resolved.
    :ivar troubleCode: Trouble code (e.g., power down, flickering
        lights, partial power, etc).
    :ivar Customer: Customer for whom this trouble ticket is relevant.
    :ivar Notification: Notification for this trouble ticket.
    :ivar ServiceLocation:
    """
    dateTimeOfReport: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    firstResponderStatus: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    resolvedDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    troubleCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    Notification: Optional[CustomerNotification] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
class AccountNotification:
    """
    Notifications for move-in, move-out, delinquencies, etc.
    """
    customerNotificationType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    time: Optional[XmlDateTime] = field(
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


@dataclass
class Asset(IdentifiedObject):
    """Tangible resource of the utility, including power system equipment,
    various end devices, cabinets, buildings, etc.

    For electrical network equipment, the role of the asset is defined
    through PowerSystemResource and its subclasses, defined mainly in
    the Wires model (refer to IEC61970-301 and model package
    IEC61970::Wires). Asset description places emphasis on the physical
    characteristics of the equipment fulfilling that role.

    :ivar AssetContainer: Container of this asset.
    :ivar AssetDeployment: This asset's deployment.
    :ivar AssetInfo: Data applicable to this asset.
    :ivar BreakerOperation: Breaker operation information for this
        breaker.
    :ivar FinancialInfo:
    :ivar Location: Location of this asset.
    :ivar ProductAssetModel: The model of this asset.
    """
    AssetContainer: Optional["AssetContainer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetDeployment: Optional[AssetDeployment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetInfo: Optional[AssetInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    BreakerOperation: Optional[SwitchOperationSummary] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    FinancialInfo: Optional[FinancialInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ProductAssetModel: Optional[ProductAssetModel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    actionTimeline: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    effectiveDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Analytic: Optional[Analytic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    maxCoverage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minCoverage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    speed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    altitude: Optional[RelativeDisplacement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    base: Optional[RelativeDisplacement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    c1PowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    c2Capacitance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    c2PowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedImpulseWithstandVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedLineToGroundVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar ServiceCategory: Service category for this agreement.
    """
    isPrePay: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    loadMgmt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    shutOffDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    ServiceCategory: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    isSolidState: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    capability: Optional[EndDeviceCapability] = field(
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
class HydrosphericPhenomenon(EnvironmentalPhenomenon):
    """
    A hydrospheric phenomenon.
    """


@dataclass
class IEEE1547Info(AssetInfo):
    maximumU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minimumU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    overExcitedPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedPatUnityPF: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedPcharge: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedPoverExcited: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedPunderExcited: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedQabsorbed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedQinjected: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedScharge: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    susceptanceCeaseToEnergize: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    underExcitedPF: Optional[float] = field(
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
    TroubleTicket: Optional[TroubleTicket] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class InterrupterUnitInfo(AssetInfo):
    pass


@dataclass
class OilSpecimen(Specimen):
    oilSampleTemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class OperatingMechanismInfo(AssetInfo):
    """
    Breaker operating mechanism datasheet information.

    :ivar closeAmps: Close current (nominal).
    :ivar closeVoltage: Close voltage in volts DC.
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
            "required": True,
        }
    )
    closeVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    motorRunCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    motorStartCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    motorVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    tripAmps: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    tripVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar Location: Location of this power system resource.
    :ivar PSRType: Custom classification for this power system resource.
    """
    AssetDatasheet: Optional[AssetInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PSRType: Optional[PSRType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class PowerTransformerInfo(AssetInfo):
    """
    Set of power transformer data, from an equipment library.
    """


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
            "required": True,
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedReactivePower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SpacePhenomenon(EnvironmentalPhenomenon):
    """
    An extra-terrestrial phenomenon.
    """


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
            "required": True,
        }
    )
    isSinglePhase: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isUnganged: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lowPressureAlarm: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lowPressureLockOut: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    oilVolumePerTank: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedImpulseWithstandVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedInterruptingTime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    ctRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ptRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    relativeTimeInterval: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar insulationThickness: (if insulated conductor) Thickness of the
        insulation.
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
    """
    coreRadius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    coreStrandCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    gmr: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    insulated: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    insulationThickness: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rAC25: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rAC50: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rAC75: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    radius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rDC20: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sizeDescription: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    strandCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    effectiveDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Analytic: Optional[Analytic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Asset: Optional[Asset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetAggregateScore: Optional["AggregateScore"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetGroup: Optional[AssetGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class AssetContainer(Asset):
    """
    Asset that is aggregation of other assets such as conductors, transformers,
    switchgear, land, fences, buildings, equipment, vehicles, etc.
    """


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
            "required": True,
        }
    )
    firmwareID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hardwareID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    programID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Asset: Optional[Asset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class CableInfo(WireInfo):
    """
    Cable data.

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
    :ivar relativePermittivity:
    :ivar sheathAsNeutral: True if sheath / shield is used as a neutral
        (i.e., bonded).
    """
    diameterOverCore: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    diameterOverInsulation: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    diameterOverJacket: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    diameterOverScreen: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isStrandFill: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    nominalTemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    relativePermittivity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sheathAsNeutral: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class CloudCondition(AtmosphericPhenomenon):
    """
    A classified cloud phenomenon with a type.
    """


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
    """
    cogenHPSendoutRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    cogenHPSteamRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    cogenLPSendoutRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    cogenLPSteamRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    amrSystem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    supportsAutonomousDst: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeZoneOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    combCyclePlantRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ConnectivityNodeContainer(PowerSystemResource):
    """
    A base class for all objects that may contain connectivity nodes or
    topological nodes.
    """


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
            "required": True,
        }
    )
    operationInProgress: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeStamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    unitMultiplier: Optional[UnitMultiplier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    unitSymbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PowerSystemResource: Optional[PowerSystemResource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    maxSurfaceWindSpeed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    windForce: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    magnitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    focalDepth: Optional[RelativeDisplacement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class FACTSDevice(Asset):
    """
    FACTS device asset.
    """


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
            "required": True,
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
            "required": True,
        }
    )
    errorEllipseMajorSemiAxis: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    negativePolarity: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    peakAmplitude: Optional[float] = field(
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
            "required": True,
        }
    )


@dataclass
class OperatingMechanism(Asset):
    """
    Breaker mechanism.
    """


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
            "required": True,
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
    PowerSystemResource: Optional[PowerSystemResource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class OverheadWireInfo(WireInfo):
    """
    Overhead wire data.
    """


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
            "required": True,
        }
    )
    Asset: Optional[Asset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetOwner: Optional[AssetOwner] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    """
    cutLevel1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    cutLevel2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar Procedure: Procedure capturing this data set.
    """
    completedDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Asset: Optional[Asset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Procedure: Optional[Procedure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar SpillsFromReservoir: A reservoir may spill into a downstream
        reservoir.
    :ivar TargetLevelSchedule: A reservoir may have a water level target
        schedule.
    """
    activeStorageCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    energyStorageRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fullSupplyLevel: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    grossCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    normalMinOperateLevel: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    riverOutletWorks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    spillTravelDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    spillwayCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    spillwayCrestLength: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    spillwayCrestLevel: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    spillWayGateType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    SpillsFromReservoir: Optional["Reservoir"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TargetLevelSchedule: Optional[TargetLevelSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    lightRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Tornado(AtmosphericPhenomenon):
    """
    A tornado, a violent destructive whirling wind accompanied by a funnel-
    shaped cloud that progresses in a narrow path over the land.

    :ivar width: Width of the tornado during the time interval.
    """
    width: Optional[float] = field(
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
    """
    PowerTransformerInfo: Optional[PowerTransformerInfo] = field(
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
            "required": True,
        }
    )
    magnitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class UsagePoint(IdentifiedObject):
    """Logical or physical point in the network to which readings or events may
    be attributed.

    Used at the place where a physical or virtual meter may be located;
    however, it is not required that a meter be present.

    :ivar checkBilling: True if as a result of an inspection or
        otherwise, there is a reason to suspect that a previous billing
        may have been performed with erroneous data. Value should be
        reset once this potential discrepancy has been resolved.
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
    :ivar CustomerAgreement: Customer agreement regulating this service
        delivery point.
    :ivar ServiceCategory: Service category delivered by this usage
        point.
    :ivar ServiceLocation: Service location where the service delivered
        by this usage point is consumed.
    :ivar UsagePointLocation: Location of this usage point.
    """
    checkBilling: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    estimatedLoad: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isSdp: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isVirtual: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minimalUsageExpected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    nominalServiceVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    outageRegion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseCode: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    readCycle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    readRoute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    serviceDeliveryRemark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    servicePriority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CustomerAgreement: Optional[CustomerAgreement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    ServiceLocation: Optional[ServiceLocation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    UsagePointLocation: Optional[UsagePointLocation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    particleSize: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
class AggregateScore(AnalyticScore):
    """
    An aggregated indicative scoring by an analytic, which is based on other
    analytic scores, that can be used to characterize the health of or the risk
    associated with one or more assets.
    """


@dataclass
class Cabinet(AssetContainer):
    """
    Enclosure that offers protection to the equipment it contains and/or safety
    to people/animals outside it.
    """


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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    neutralStrandCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    neutralStrandGmr: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    neutralStrandRadius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    neutralStrandRDC20: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    modifiedBy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ChangedAsset: Optional[Asset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ChangedDocument: Optional[Document] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ChangedLocation: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ChangedOrganisationRole: Optional[OrganisationRole] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ChangedPersonRole: Optional[PersonRole] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ChangedServiceCategory: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ChangedUsagePoint: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    PowerSystemResource: Optional[PowerSystemResource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    failureMode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    finalCause: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    finalCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    finalOrigin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    finalRemark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseCode: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    preliminaryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    preliminaryDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    preliminaryRemark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rootCause: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rootOrigin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rootRemark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    circuitCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    installCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isPan: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isSmartInverter: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isVirtual: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    timeZoneOffset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    EndDeviceGroups: Optional[EndDeviceGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EndDeviceInfo: Optional[EndDeviceInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    UsagePoint: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EquipmentContainer(ConnectivityNodeContainer):
    """
    A modeling construct to provide a root class for containing equipment.
    """


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
            "required": True,
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
            "required": True,
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
    :ivar Reservoir: Generators discharge water to or pumps are supplied
        water from a downstream reservoir.
    """
    dischargeTravelDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    genRatedP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hydroPlantStorageType: Optional[HydroPlantStorageKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    penstockType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    plantDischargeCapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    plantRatedHead: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pumpRatedP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    surgeTankCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    surgeTankCrestLevel: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    Reservoir: Optional[Reservoir] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    Reservoir: Optional[Reservoir] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class InspectionDataSet(ProcedureDataSet):
    """
    Documents the result of one inspection, for a given attribute of an asset.

    :ivar locationCondition: Description of the conditions of the
        location where the asset resides.
    """
    locationCondition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class InterrupterUnit(Asset):
    """Breaker interrupter.

    Some interrupters have one fixed and one moving contact, some have 2
    fixed contacts, some 2 moving contacts. An interrupter will have
    relationships with 2 bushings and those relationships may be any
    combination of the FixedContact and MovingContact associations.

    :ivar OperatingMechanism: Breaker mechanism controlling this
        interrupter.
    """
    OperatingMechanism: Optional[OperatingMechanism] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class LabTestDataSet(ProcedureDataSet):
    """
    Results of testing done by a lab.

    :ivar conclusion: Conclusion drawn from test results.
    :ivar conclusionConfidence: Description of confidence in conclusion.
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
            "required": True,
        }
    )
    conclusionConfidence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    testEquipmentID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetTestLab: Optional[AssetTestLab] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Specimen: Optional[Specimen] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class LevelVsVolumeCurve(Curve):
    """Relationship between reservoir volume and reservoir level.

    The  volume is at the y-axis and the reservoir level at the x-axis.

    :ivar Reservoir: A reservoir may have a level versus volume
        relationship.
    """
    Reservoir: Optional[Reservoir] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    conditionBefore: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maintCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Seal(IdentifiedObject):
    """
    Physically controls access to AssetContainers.

    :ivar appliedDateTime: Date and time this seal has been applied.
    :ivar sealNumber: (reserved word) Seal number.
    :ivar AssetContainer: Asset container to which this seal is applied.
    """
    appliedDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sealNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AssetContainer: Optional[AssetContainer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class ServiceMultiplier(IdentifiedObject):
    """
    Multiplier applied at the usage point.

    :ivar value: Multiplier value.
    :ivar UsagePoint: Usage point applying this multiplier.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    UsagePoint: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    fumigantAppliedDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fumigantName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    removeWeed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    weedRemovedDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    tapeThickness: Optional[float] = field(
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
            "required": True,
        }
    )
    specimenID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    specimenToLabDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
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
    :ivar AngleRefTopologicalIsland: The island for which the node is an
        angle reference.   Normally there is one angle reference node
        for each island.
    :ivar BaseVoltage: The base voltage of the topologocial node.
    :ivar ConnectivityNodeContainer: The connectivity node container to
        which the toplogical node belongs.
    :ivar ReportingGroup: The reporting group to which the topological
        node belongs.
    :ivar TopologicalIsland: A topological node belongs to a topological
        island.
    """
    pInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    qInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AngleRefTopologicalIsland: Optional[TopologicalIsland] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    BaseVoltage: Optional[BaseVoltage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ConnectivityNodeContainer: Optional[ConnectivityNodeContainer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ReportingGroup: Optional[ReportingGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TopologicalIsland: Optional[TopologicalIsland] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    emergencyS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    endNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    insulationU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseAngleClock: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    shortTermS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CoreAdmittance: Optional[TransformerCoreAdmittance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TransformerStarImpedance: Optional[TransformerStarImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TransformerTankInfo: Optional[TransformerTankInfo] = field(
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
    A tropical cyclone, a subtype of cyclone that forms to the east of 90°E in
    the Southern Hemisphere whose intensity is measured by the Australian
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
            "required": True,
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
            "required": True,
        }
    )
    ReportingGroup: Optional[ReportingGroup] = field(
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
class Bushing(Asset):
    """
    Bushing asset.

    :ivar FixedContact: Fixed contact of interrupter to which this
        bushing is attached.
    :ivar MovingContact: Moving contact of interrupter to which this
        bushing is attached.
    :ivar Terminal:
    """
    FixedContact: Optional[InterrupterUnit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    MovingContact: Optional[InterrupterUnit] = field(
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EndDevice: Optional[EndDevice] = field(
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
    :ivar EquipmentContainer: Container of this equipment.
    :ivar UsagePoints: All usage points connected to the electrical grid
        through this equipment.
    """
    aggregate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    inService: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    networkAnalysisEnabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    normallyInService: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EquipmentContainer: Optional[EquipmentContainer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    UsagePoints: Optional[UsagePoint] = field(
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
    Region: Optional[SubGeographicalRegion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    formNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    excitingCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    excitingCurrentZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    loss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lossZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EnergisedEnd: Optional[TransformerEndInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    energisedEndVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    openEndStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    openEndVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseShift: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EnergisedEnd: Optional[TransformerEndInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    OpenEnd: Optional[TransformerEndInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Plant(EquipmentContainer):
    """
    A Plant is a collection of equipment for purposes of generation.
    """


@dataclass
class RiskScore(AggregateScore):
    """
    Score that is indicative of the risk associated with one or more assets.
    """


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
    :ivar status:
    """
    estimatedWindow: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    energisedEndStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    groundedEndStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    leakageImpedance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    leakageImpedanceZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    loss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lossZero: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EnergisedEnd: Optional[TransformerEndInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    anchorRodLength: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    direction: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    size: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    SecuredStructure: Optional[Structure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Substation(EquipmentContainer):
    """
    A collection of equipment for purposes other than generation or
    utilization, through which electric energy in bulk is passed for the
    purposes of switching or modifying its characteristics.

    :ivar NamingFeeder: The primary feeder that normally energizes the
        secondary substation. Used for naming purposes.  Either this
        association or the substation to subgeographical region should
        be used for hiearchical containment specification.
    :ivar Region: The SubGeographicalRegion containing the substation.
    """
    NamingFeeder: Optional["Feeder"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Region: Optional[SubGeographicalRegion] = field(
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
            "required": True,
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    v: Optional[float] = field(
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
    :ivar DuctBank:
    """
    isCable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseWireCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseWireSpacing: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DuctBank: Optional[DuctBank] = field(
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
    """
    connected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    BusNameMarker: Optional[BusNameMarker] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
    :ivar ComModule: Module performing this communication function.
    """
    amrAddress: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    amrRouter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ComModule: Optional[ComModule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    compositeSwitchType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    BaseVoltage: Optional[BaseVoltage] = field(
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
    :ivar SvVoltage:
    :ivar TopologicalNode: The topological node to which this
        connectivity node is assigned.  May depend on the current state
        of switches in the network.
    """
    ConnectivityNodeContainer: Optional[ConnectivityNodeContainer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    SvVoltage: Optional[SvVoltage] = field(
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
class Fault(IdentifiedObject):
    """
    Abnormal condition causing current flow through conducting equipment, such
    as caused by equipment failure or short circuits from objects not typically
    modeled (for example, a tree falling on a line).

    :ivar kind: The kind of phase fault.
    :ivar phases: The phases participating in the fault. The fault
        connections into these phases are further specified by the type
        of fault.
    :ivar stopDateTime: Time when the fault is repaired. If not
        specified, the fault is temporary and will clear itself as soon
        as it's deenergized.
    :ivar FaultyEquipment: Equipment carrying this fault.
    :ivar impedance: Fault impedance. Its usage is described by 'kind'.
    :ivar Location:
    """
    kind: Optional[PhaseConnectedFaultKind] = field(
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
            "required": True,
        }
    )
    stopDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    FaultyEquipment: Optional[Equipment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    impedance: Optional[FaultImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Feeder(EquipmentContainer):
    """A collection of equipment for organizational purposes, used for grouping
    distribution resources.

    The organization a feeder does not necessarily reflect connectivity
    or current operation state.

    :ivar NormalEnergizingSubstation: The substation that nominally
        energizes the feeder.  Also used for naming purposes.
    """
    NormalEnergizingSubstation: Optional[Substation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar GenUnitOpSchedule: A generating unit may have an operating
        schedule, indicating the planned operation of the unit.
    """
    maxOperatingP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minOperatingP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    GenUnitOpSchedule: Optional[GenUnitOpSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    pumpDischAtMinHead: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pumpPowerAtMaxHead: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    pumpPowerAtMinHead: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    HydroPowerPlant: Optional[HydroPowerPlant] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    HydroPumpOpSchedule: Optional[HydroPumpOpSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
class MeterMultiplier(IdentifiedObject):
    """
    Multiplier applied at the meter.

    :ivar value: Multiplier value.
    :ivar Meter: Meter applying this multiplier.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Meter: Optional[Meter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar Meter: Meter providing this reading.
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
            "required": True,
        }
    )
    CustomerAgreement: Optional[CustomerAgreement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Meter: Optional[Meter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    UsagePoint: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    valuesInterval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
    Meter: Optional[Meter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    OldMeter: Optional[Meter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    UsagePoint: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    leftDigitCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rightDigitCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    touTierName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EndDeviceFunction: Optional[EndDeviceFunction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    touTier: Optional[TimeInterval] = field(
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
    :ivar ScheduledEventData: Specification for this scheduled event.
    :ivar status:
    """
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ScheduledEventData: Optional[ScheduledEventData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SimpleEndDeviceFunction(EndDeviceFunction):
    """Simple end device function distinguished by 'kind'.

    Use this class for instances that cannot be represented by another
    end device function specialisations.
    """


@dataclass
class SvEstVoltage(SvVoltage):
    Estimate: Optional[Estimate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar Substation: The substation of the voltage level.
    """
    highVoltageLimit: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lowVoltageLimit: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    BaseVoltage: Optional[BaseVoltage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Substation: Optional[Substation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class WireAssemblyInfo(AssetInfo):
    """
    Describes the construction of a multi-conductor wire.
    """
    WireSpacingInfo: Optional[WireSpacingInfo] = field(
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

    :ivar xCoord: Signed horizontal distance from the wire at this
        position to a common reference point.
    :ivar yCoord: Signed vertical distance from the wire at this
        position: above ground (positive value) or burial depth below
        ground (negative value).
    :ivar WireSpacingInfo: Wire spacing data this wire position belongs
        to.
    """
    xCoord: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    yCoord: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    bayPowerMeasFlag: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    breakerConfiguration: Optional[BreakerConfiguration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    busBarConfiguration: Optional[BusbarConfiguration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Substation: Optional[Substation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    VoltageLevel: Optional[VoltageLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
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
    Register: Optional[Register] = field(
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
            "required": True,
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
            "required": True,
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
            "required": True,
        }
    )
    issuerTrackingID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    userID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EndDevice: Optional[EndDevice] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    UsagePoint: Optional[UsagePoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EnergyConnection(ConductingEquipment):
    EnergyConnectionProfile: Optional[EnergyConnectionProfile] = field(
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
            "required": True,
        }
    )
    GeneratingUnit: Optional[GeneratingUnit] = field(
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
    GeneratingUnit: Optional[GeneratingUnit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Ground(ConductingEquipment):
    """A point where the system is grounded used for connecting conducting
    equipment to ground.

    The power system model can have any number of grounds.
    """


@dataclass
class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis,
    Pelton, Kaplan).

    :ivar energyConversionCapability: Energy conversion capability for
        generating.
    :ivar hydroUnitWaterCost: The equivalent cost of water that drives
        the hydro turbine.
    :ivar HydroPowerPlant: The hydro generating unit belongs to a hydro
        power plant.
    :ivar PenstockLossCurve: A hydro generating unit has a penstock loss
        curve.
    """
    energyConversionCapability: Optional[HydroEnergyConversionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    hydroUnitWaterCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    HydroPowerPlant: Optional[HydroPowerPlant] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PenstockLossCurve: Optional[PenstockLossCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class IntervalBlock:
    """Time sequence of readings of the same reading type.

    Contained interval readings may need conversion through the
    application of an offset and a scalar defined in associated pending.

    :ivar MeterReading: Meter reading containing this interval block.
    :ivar PendingCalculation: Pending calculation to apply to interval
        reading values contained by this block (after which the
        resulting reading type is different than the original because it
        reflects the conversion result).
    :ivar ReadingType: Type information for interval reading values
        contained in this block.
    """
    MeterReading: Optional[MeterReading] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PendingCalculation: Optional[PendingCalculation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar PowerSystemResource: The power system resource that contains
        the measurement.
    :ivar Terminal: One or more measurements may be associated with a
        terminal in the network.
    """
    measurementType: Optional[str] = field(
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
            "required": True,
        }
    )
    Asset: Optional[Asset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PowerSystemResource: Optional[PowerSystemResource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Terminal: Optional[ACDCTerminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class NuclearGeneratingUnit(GeneratingUnit):
    """
    A nuclear generating unit.
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
    :ivar Terminal:
    """
    ConnectivityNode: Optional[ConnectivityNode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Equipment: Optional[Equipment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Terminal: Optional[ACDCTerminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class PerLengthLineParameter(IdentifiedObject):
    """
    Common type for per-length electrical catalogues describing line
    parameters.
    """
    WireAssemblyInfo: Optional[WireAssemblyInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
    """
    vectorGroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    varistorPresent: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    varistorRatedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    varistorVoltageThreshold: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SolarGeneratingUnit(GeneratingUnit):
    """A solar thermal generating unit, connected to the grid by means of a
    rotating machine.

    This class does not represent photovoltaic (PV) generation.
    """


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
            "required": True,
        }
    )
    pInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    qInjection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ConnectivityNode: Optional[ConnectivityNode] = field(
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
            "required": True,
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ConductingEquipment: Optional[ConductingEquipment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    normalOpen: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    open: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    retained: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CompositeSwitch: Optional[CompositeSwitch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Terminal(ACDCTerminal):
    """An AC electrical connection point to a piece of conducting equipment.

    Terminals are connected at physical connection points called
    connectivity nodes.

    :ivar Bushing:
    :ivar ConductingEquipment: The conducting equipment of the terminal.
        Conducting equipment have  terminals that may be connected to
        other conducting equipment terminals via connectivity nodes or
        topological nodes.
    :ivar ConnectivityNode: The connectivity node to which this terminal
        connects with zero impedance.
    :ivar NormalHeadFeeder: The feeder that this terminal normally
        feeds.  Only specifed for the terminals at head of feeders.
    :ivar TopologicalNode: The topological node associated with the
        terminal.   This can be used as an alternative to the
        connectivity node path to topological node, thus making it
        unneccesary to model connectivity nodes in some cases.   Note
        that the if connectivity nodes are in the model, this
        association would probably not be used as an input
        specification.
    """
    Bushing: Optional[Bushing] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ConductingEquipment: Optional[ConductingEquipment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ConnectivityNode: Optional[ConnectivityNode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    NormalHeadFeeder: Optional[Feeder] = field(
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
            "required": True,
        }
    )
    CAESPlant: Optional["CAESPlant"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CogenerationPlant: Optional[CogenerationPlant] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CombinedCyclePlant: Optional[CombinedCyclePlant] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    HeatInputCurve: Optional[HeatInputCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    HeatRateCurve: Optional[HeatRateCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IncrementalHeatRateCurve: Optional[IncrementalHeatRateCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ShutdownCurve: Optional[ShutdownCurve] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    StartupModel: Optional[StartupModel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    WireInfo: Optional[WireInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    WirePosition: Optional[WirePosition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    maxValue: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    maxValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    normalValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    positiveFlowIn: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class BranchGroupTerminal:
    """
    A specific directed terminal flow for a branch group.

    :ivar positiveFlowIn: The flow into the terminal is summed if set
        true.   The flow out of the terminanl is summed if set false.
    :ivar Terminal: The terminal to be summed.
    """
    positiveFlowIn: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Terminal: Optional[Terminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    ratedCapacityP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar ValueAliasSet: The ValueAliasSet used for translation of a
        MeasurementValue.value to a name.
    """
    maxValue: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minValue: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    normalValue: Optional[int] = field(
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
            "required": True,
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
            "required": True,
        }
    )
    emissionValueSource: Optional[EmissionValueSource] = field(
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
            "required": True,
        }
    )
    emissionType: Optional[EmissionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    isNetGrossP: Optional[bool] = field(
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
            "required": True,
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
            "required": True,
        }
    )
    EndDeviceEvent: Optional[EndDeviceEvent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    value: Optional[StringQuantity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseConnection: Optional[PhaseShuntConnectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    House: Optional[House] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    LoadResponse: Optional[LoadResponseCharacteristic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PowerCutZone: Optional[PowerCutZone] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    nominalVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltageAngle: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltageMagnitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EquipmentFault(Fault):
    """A fault applied at the terminal, external to the equipment.

    This class is not used to specify faults internal to the equipment.

    :ivar Terminal: The terminal connecting to the bus to which the
        fault is applied.
    """
    Terminal: Optional[Terminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar ThermalGeneratingUnit: A thermal generating unit may have one
        or more fossil fuels.
    """
    fossilFuelType: Optional[FuelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fuelCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fuelDispatchCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fuelEffFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fuelHandlingCost: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fuelHeatContent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fuelMixture: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fuelSulfur: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    highBreakpointP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lowBreakpointP: Optional[float] = field(
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
            "required": True,
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
            "required": True,
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
    HydroGeneratingUnit: Optional[HydroGeneratingUnit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    distance11: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    distance12: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    distance21: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    distance22: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    First_Terminal: Optional[Terminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Second_Terminal: Optional[Terminal] = field(
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
            "required": True,
        }
    )
    nominalU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    offsetCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    positionCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xGroundMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xGroundMin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xGroundNominal: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar reverseTargetDeadband:
    :ivar reverseTargetValue:
    :ivar targetDeadband: This is a deadband used with discrete control
        to avoid excessive update of controls like tap changers and
        shunt compensator banks while regulating. The units of those
        appropriate for the mode.
    :ivar targetValue: The target value specified for case input.   This
        value can be used for the target value without the use of
        schedules. The value has the units appropriate to the mode
        attribute.
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
            "required": True,
        }
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    mode: Optional[RegulatingControlModeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    monitoredPhase: Optional[PhaseCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reverseTargetDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reverseTargetValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    targetDeadband: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    targetValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Terminal: Optional[Terminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class RemoteInputSignal:
    """
    Supports connection to a terminal associated with a remote bus from which
    an input signal of a specific type is coming.
    """
    Terminal: Optional[Terminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
class StringMeasurement(Measurement):
    """
    StringMeasurement represents a measurement with values of type string.
    """


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
            "required": True,
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Terminal: Optional[Terminal] = field(
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

    :ivar phase: The terminal phase at which the connection is applied.
        If missing, the injection is assumed to be balanced among non-
        neutral phases.
    :ivar Switch: The switch associated with the switch state.
    """
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Switch: Optional[Switch] = field(
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
            "required": True,
        }
    )
    normalOpen: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseSide1: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseSide2: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Switch: Optional[Switch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SwitchSchedule(SeasonDayTypeSchedule):
    """A schedule of switch positions.

    If RegularTimePoint.value1 is 0, the switch is open.  If 1, the
    switch is closed.

    :ivar Switch: A SwitchSchedule is associated with a Switch.
    """
    Switch: Optional[Switch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    HydroGeneratingUnit: Optional[HydroGeneratingUnit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar TransformerTankInfo:
    """
    PowerTransformer: Optional[PowerTransformer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TransformerTankInfo: Optional[TransformerTankInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


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
    :ivar ParallelLineSegment:
    :ivar PerLengthImpedance: Per-length impedance of this line segment.
    :ivar WireSpacingInfo:
    """
    b0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    bch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    gch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    shortCircuitEndTemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ParallelLineSegment: Optional[ParallelLineSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PerLengthImpedance: Optional[PerLengthImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    Accumulator: Optional[Accumulator] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AccumulatorReset: Optional["AccumulatorReset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
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
            "required": True,
        }
    )
    Analog: Optional[Analog] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AnalogControl: Optional["AnalogControl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
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
            "required": True,
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
            "required": True,
        }
    )
    Command: Optional["Command"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EnergyConsumer: Optional[EnergyConsumer] = field(
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
            "required": True,
        }
    )
    EnergySource: Optional[EnergySource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    ClassificationCondition: Optional[TypeificationCondition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EnvironmentalInformation: Optional[EnvironmentalInformation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ReportingCapability: Optional[ReportingCapability] = field(
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
    ClassificationCondition: Optional[TypeificationCondition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    EnvironmentalInformation: Optional[EnvironmentalInformation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    fuelAllocationStartDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    fuelType: Optional[FuelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxFuelAllocation: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minFuelAllocation: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    FossilFuel: Optional[FossilFuel] = field(
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
            "required": True,
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
            "required": True,
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
    """
    conductorCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    bch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g0ch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    gch: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class Recloser(ProtectedSwitch):
    """
    Pole-mounted fault interrupter with built-in phase and ground relays,
    current transformer (CT), and supplemental controls.
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
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    RegulatingControl: Optional[RegulatingControl] = field(
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
    """
    RegulatingControl: Optional[RegulatingControl] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class StationSupply(EnergyConsumer):
    """
    Station supply with load derived from the station output.
    """


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
            "required": True,
        }
    )
    StringMeasurement: Optional[StringMeasurement] = field(
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
    :ivar reverseToNeutral:
    :ivar reversible:
    :ivar reversingDelay:
    :ivar reversingPowerThreshold:
    """
    lineDropCompensation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lineDropR: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lineDropX: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxLimitVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minLimitVoltage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reverseLineDropR: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reverseLineDropX: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reverseToNeutral: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reversible: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reversingDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reversingPowerThreshold: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ACLineSegment: Optional[ACLineSegment] = field(
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
            "required": True,
        }
    )


@dataclass
class AccumulatorReset(Control):
    """
    This command reset the counter value to zero.

    :ivar AccumulatorValue: The accumulator value that is reset by the
        command.
    """
    AccumulatorValue: Optional[AccumulatorValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    minValue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    AnalogValue: Optional[AnalogValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class AtmosphericAnalog(EnvironmentalAnalog):
    """
    Analog measuring an atmospheric condition.
    """


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
            "required": True,
        }
    )
    ACLineSegment: Optional[ACLineSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
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
            "required": True,
        }
    )
    ACLineSegment: Optional[ACLineSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class EnvironmentalCodedValue(StringMeasurementValue):
    """An environmental value described using a coded value.

    A triplicate of enumerated values representing intensity, coverage,
    type of weather is used. These may be concatenated into the string
    value.

    :ivar probabilityPercent: Probability of weather condition occurring
        during the time interval expressed as a percentage. Applicable
        only when weather condition is related to a forecast (not an
        observation).
    """
    probabilityPercent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    ikSecond: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxInitialSymShCCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxR0ToX0Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxR1ToX1Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxZ0ToZ1Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minInitialSymShCCurrent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minR0ToX0Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minR1ToX1Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minZ0ToZ1Ratio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    referencePriority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltageFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    maxP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class GeosphericAnalog(EnvironmentalAnalog):
    """
    Analog measuring a geospheric condition.
    """


@dataclass
class HydrosphericAnalog(EnvironmentalAnalog):
    """
    Analog measuring a hydrospheric condition.
    """


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
            "required": True,
        }
    )
    ACLineSegment: Optional[ACLineSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class PhaseImpedanceData:
    """Impedance and conductance matrix element values.

    The diagonal elements are described by the elements having the same
    toPhase and fromPhase value and the off diagonal elements have
    different toPhase and fromPhase values. The matrix can also be
    stored in symmetric lower triangular format using the row and column
    attributes, which map to ACLineSegmentPhase.sequenceNumber.

    :ivar b: Susceptance matrix element value, per length of unit.
    :ivar g: Conductance matrix element value, per length of unit.
    :ivar r: Resistance matrix element value, per length of unit.
    :ivar x: Reactance matrix element value, per length of unit.
    :ivar PhaseImpedance: Conductor phase impedance to which this data
        belongs.
    """
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PhaseImpedance: Optional[PerLengthPhaseImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class PowerElectronicsConnection(RegulatingCondEq):
    """
    A connection to the AC network for energy production or consumption that
    uses power electronics rather than rotating machines.

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
    """
    maxIFault: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    p: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERDynamics: Optional[DERDynamics] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IEEE1547ControlSettings: Optional[IEEE1547ControlSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IEEE1547Info: Optional[IEEE1547Info] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IEEE1547Setting: Optional[IEEE1547Setting] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IEEE1547TripSettings: Optional[IEEE1547TripSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedPowerFactor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    GeneratingUnit: Optional[GeneratingUnit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    HydroPump: Optional[HydroPump] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IEEE1547ControlSettings: Optional[IEEE1547ControlSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IEEE1547Info: Optional[IEEE1547Info] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IEEE1547Setting: Optional[IEEE1547Setting] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    IEEE1547TripSettings: Optional[IEEE1547TripSettings] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar SvShuntCompensatorSections: The state for the number of shunt
        compensator sections in service.
    """
    aVRDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maximumSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    nomU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    normalSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phaseConnection: Optional[PhaseShuntConnectionKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sections: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    SvShuntCompensatorSections: Optional[SvShuntCompensatorSections] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class SpaceAnalog(EnvironmentalAnalog):
    """
    Analog measuring a space (extra-terrestrial) condition.
    """


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
            "required": True,
        }
    )
    inductiveRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    slope: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    sVCControlMode: Optional[SVCControlMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    voltageSetPoint: Optional[float] = field(
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
    """
    controlEnabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ctRating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ctRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    highStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    initialDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    lowStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ltcFlag: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    neutralStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    neutralU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    normalStep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ptRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    step: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    subsequentDelay: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    SvTapStep: Optional[SvTapStep] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    TapChangerControl: Optional[TapChangerControl] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    RegulationSchedule: Optional[RegulationSchedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar DERDynamics: DER dynamics model associated with this
        asynchronous machine model.
    """
    asynchronousMachineType: Optional[AsynchronousMachineKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    converterFedDrive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    efficiency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    iaIrRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    nominalFrequency: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    nominalSpeed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    polePairNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedMechanicalPower: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    reversible: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rxLockedRotorRatio: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERDynamics: Optional[DERDynamics] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    VoltageControlZone: Optional[VoltageControlZone] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class DiscreteCommand(Command):
    pass


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
            "required": True,
        }
    )
    bPerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    g0PerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    gPerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class NonlinearShuntCompensator(ShuntCompensator):
    """
    A non linear shunt compensator has bank or section admittance values that
    differs.
    """


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
            "required": True,
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    q: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PowerElectronicsConnection: Optional[PowerElectronicsConnection] = field(
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
            "required": True,
        }
    )
    minP: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PowerElectronicsConnection: Optional[PowerElectronicsConnection] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    ValueAliasSet: Optional[ValueAliasSet] = field(
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
            "required": True,
        }
    )
    RatioTapChangerTable: Optional[RatioTapChangerTable] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar ShuntCompensator: Shunt compensator of this shunt compensator
        phase.
    """
    maximumSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    normalSections: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    phase: Optional[SinglePhaseKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ShuntCompensator: Optional[ShuntCompensator] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    :ivar DERDynamics: DER dynamics model associated with this
        synchronous machine model.
    :ivar InitialReactiveCapabilityCurve: The default reactive
        capability curve for use by a synchronous machine.
    """
    ikk: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    maxQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    minQ: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    operatingMode: Optional[SynchronousMachineOperatingMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    type: Optional[SynchronousMachineKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    DERDynamics: Optional[DERDynamics] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    InitialReactiveCapabilityCurve: Optional[ReactiveCapabilityCurve] = field(
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
    TapChanger: Optional[TapChanger] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class BatteryUnit(PowerElectronicsUnit):
    """
    An electrochemical energy storage device.

    :ivar ratedE: full energy storage capacity of the battery
    :ivar storedE: amount of energy currently stored; no more than
        ratedE
    """
    ratedE: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    storedE: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    gPerSection: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class NonlinearShuntCompensatorPhase(ShuntCompensatorPhase):
    """
    A per phase non linear shunt compensator has bank or section admittance
    values that differs.
    """


@dataclass
class PhotovoltaicUnit(PowerElectronicsUnit):
    """
    A photovoltaic device or an aggregation of such devices.
    """


@dataclass
class PowerElectronicsWindUnit(PowerElectronicsUnit):
    """
    A wind generating unit that connects to the AC network with power
    electronics rather than rotating machines or an aggregation of such units.
    """


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
    """
    endNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    rground: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xground: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    BaseVoltage: Optional[BaseVoltage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    CoreAdmittance: Optional[TransformerCoreAdmittance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PhaseTapChanger: Optional["PhaseTapChanger"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    RatioTapChanger: Optional[RatioTapChanger] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    StarImpedance: Optional[TransformerStarImpedance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    Terminal: Optional[Terminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    TransformerEnd: Optional[TransformerEnd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    phaseAngleClock: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    ratedU: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    PowerTransformer: Optional[PowerTransformer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
    """
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    x0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    FromTransformerEnd: Optional[TransformerEnd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    FromTransformerEndInfo: Optional[TransformerEndInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class TransformerTankEnd(TransformerEnd):
    """
    Transformer tank end represents an individual winding for unbalanced models
    or for transformer tanks connected into a bank (and bank is modelled with
    the PowerTransformer).

    :ivar TransformerTank: Transformer this winding belongs to.
    """
    TransformerTank: Optional[TransformerTank] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    xMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xMin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
        }
    )
    xMax: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )
    xMin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
        }
    )


@dataclass
class PhaseTapChangerTabular(PhaseTapChanger):
    """
    :ivar PhaseTapChangerTable: The phase tap changer table for this
        phase tap changer.
    """
    PhaseTapChangerTable: Optional[PhaseTapChangerTable] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iec.ch/TC57/CIM100#",
            "required": True,
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
            "required": True,
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

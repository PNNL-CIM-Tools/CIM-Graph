
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from importlib import resources as impresources
from typing import Optional

from pint import Quantity, UnitRegistry

import cimgraph.data_profile.units.cim_units as cim_units

units_file = impresources.files(cim_units) / 'units.txt'
ureg = UnitRegistry()
ureg.load_definitions(units_file)
ureg.default_format = '~P'

def pint(obj):
    if obj.multiplier.value != 'none':
        value_str = str(obj.value) + obj.multiplier.value + obj.unit.value
    else:
        value_str = str(obj.value) + obj.unit.value
    obj.pvalue = ureg.Quantity(value_str)
    return obj.pvalue

class UnitMultiplier( Enum ):
    '''
    The unit multipliers defined for the CIM. When applied to unit symbols,
    the unit symbol is treated as a derived unit. Regardless of the contents
    of the unit symbol text, the unit symbol shall be treated as if it were
    a single-character unit symbol. Unit symbols should not contain multipliers,
    and it should be left to the multiplier to define the multiple for an entire
    data type.
    For example, if a unit symbol is 'm2Pers' and the multiplier is 'k', then
    the value is k(m**2/s), and the multiplier applies to the entire final
    value, not to any individual part of the value. This can be conceptualized
    by substituting a derived unit symbol for the unit type. If one imagines
    that the symbol 'Þ' represents the derived unit 'm2Pers', then applying
    the multiplier 'k' can be conceptualized simply as 'kÞ'.
    For example, the SI unit for mass is 'kg' and not 'g'. If the unit symbol
    is defined as 'kg', then the multiplier is applied to 'kg' as a whole and
    does not replace the 'k' in front of the 'g'. In this case, the multiplier
    of 'm' would be used with the unit symbol of 'kg' to represent one gram.
    As a text string, this violates the instructions in IEC 80000-1. However,
    because the unit symbol in CIM is treated as a derived unit instead of
    as an SI unit, it makes more sense to conceptualize the 'kg' as if it were
    replaced by one of the proposed replacements for the SI mass symbol. If
    one imagines that the 'kg' were replaced by a symbol 'Þ', then it is easier
    to conceptualize the multiplier 'm' as creating the proper unit 'mÞ', and
    not the forbidden unit 'mkg'.
    '''
    E = 'E'
    '''
    Exa 10**18.
    '''
    G = 'G'
    '''
    Giga 10**9.
    '''
    M = 'M'
    '''
    Mega 10**6.
    '''
    P = 'P'
    '''
    Peta 10**15.
    '''
    T = 'T'
    '''
    Tera 10**12.
    '''
    Y = 'Y'
    '''
    Yotta 10**24.
    '''
    Z = 'Z'
    '''
    Zetta 10**21.
    '''
    a = 'a'
    '''
    Atto 10**-18.
    '''
    c = 'c'
    '''
    Centi 10**-2.
    '''
    d = 'd'
    '''
    Deci 10**-1.
    '''
    da = 'da'
    '''
    Deca 10**1.
    '''
    f = 'f'
    '''
    Femto 10**-15.
    '''
    h = 'h'
    '''
    Hecto 10**2.
    '''
    k = 'k'
    '''
    Kilo 10**3.
    '''
    m = 'm'
    '''
    Milli 10**-3.
    '''
    micro = 'micro'
    '''
    Micro 10**-6.
    '''
    n = 'n'
    '''
    Nano 10**-9.
    '''
    none = 'none'
    '''
    No multiplier or equivalently multiply by 1.
    '''
    p = 'p'
    '''
    Pico 10**-12.
    '''
    y = 'y'
    '''
    Yocto 10**-24.
    '''
    z = 'z'
    '''
    Zepto 10**-21.
    '''

class UnitSymbol( Enum ):
    '''
    The derived units defined for usage in the CIM. In some cases, the derived
    unit is equal to an SI unit. Whenever possible, the standard derived symbol
    is used instead of the formula for the derived unit. For example, the unit
    symbol Farad is defined as 'F' instead of 'CPerV'. In cases where a standard
    symbol does not exist for a derived unit, the formula for the unit is used
    as the unit symbol. For example, density does not have a standard symbol
    and so it is represented as 'kgPerm3'. With the exception of the 'kg',
    which is an SI unit, the unit symbols do not contain multipliers and therefore
    represent the base derived unit to which a multiplier can be applied as
    a whole.
    Every unit symbol is treated as an unparseable text as if it were a single-letter
    symbol. The meaning of each unit symbol is defined by the accompanying
    descriptive text and not by the text contents of the unit symbol.
    To allow the widest possible range of serializations without requiring
    special character handling, several substitutions are made which deviate
    from the format described in IEC 80000-1. The division symbol '/' is replaced
    by the letters 'Per'. Exponents are written in plain text after the unit
    as 'm3' instead of being formatted as 'm' with a superscript of 3 or introducing
    a symbol as in 'm^3'. The degree symbol '°' is replaced with the letters
    'deg'. Any clarification of the meaning for a substitution is included
    in the description for the unit symbol.
    Non-SI units are included in list of unit symbols to allow sources of data
    to be correctly labelled with their non-SI units (for example, a GPS sensor
    that is reporting numbers that represent feet instead of meters). This
    allows software to use the unit symbol information correctly convert and
    scale the raw data of those sources into SI-based units.
    The integer values are used for harmonization with IEC 61850.
    '''
    A = 'A'
    '''
    Current in amperes.
    '''
    A2 = 'A2'
    '''
    Amperes squared (A²).
    '''
    A2h = 'A2h'
    '''
    Ampere-squared hour, ampere-squared hour.
    '''
    A2s = 'A2s'
    '''
    Ampere squared time in square amperes (A²s).
    '''
    APerA = 'APerA'
    '''
    Current, ratio of amperages. Note: Users may need to supply a prefix such
    as ‘m’ to show rates such as ‘mA/A’.
    '''
    APerm = 'APerm'
    '''
    A/m, magnetic field strength, amperes per metre.
    '''
    Ah = 'Ah'
    '''
    Ampere-hours, ampere-hours.
    '''
    As = 'As'
    '''
    Ampere seconds (A·s).
    '''
    Bq = 'Bq'
    '''
    Radioactivity in becquerels (1/s).
    '''
    Btu = 'Btu'
    '''
    Energy, British Thermal Units.
    '''
    C = 'C'
    '''
    Electric charge in coulombs (A·s).
    '''
    CPerkg = 'CPerkg'
    '''
    Exposure (x rays), coulombs per kilogram.
    '''
    CPerm2 = 'CPerm2'
    '''
    Surface charge density, coulombs per square metre.
    '''
    CPerm3 = 'CPerm3'
    '''
    Electric charge density, coulombs per cubic metre.
    '''
    F = 'F'
    '''
    Electric capacitance in farads (C/V).
    '''
    FPerm = 'FPerm'
    '''
    Permittivity, farads per metre.
    '''
    g = 'g'
    '''
    Mass in grams
    '''
    G = 'G'
    '''
    Magnetic flux density, gausses (1 G = 10-4 T).
    '''
    Gy = 'Gy'
    '''
    Absorbed dose in grays (J/kg).
    '''
    GyPers = 'GyPers'
    '''
    Absorbed dose rate, grays per second.
    '''
    H = 'H'
    '''
    Electric inductance in henrys (Wb/A).
    '''
    HPerm = 'HPerm'
    '''
    Permeability, henrys per metre.
    '''
    Hz = 'Hz'
    '''
    Frequency in hertz (1/s).
    '''
    HzPerHz = 'HzPerHz'
    '''
    Frequency, rate of frequency change. Note: Users may need to supply a prefix
    such as ‘m’ to show rates such as ‘mHz/Hz’.
    '''
    HzPers = 'HzPers'
    '''
    Rate of change of frequency in hertz per second.
    '''
    J = 'J'
    '''
    Energy in joules (N·m = C·V = W·s).
    '''
    JPerK = 'JPerK'
    '''
    Heat capacity in joules/kelvin.
    '''
    JPerkg = 'JPerkg'
    '''
    Specific energy, Joules / kg.
    '''
    JPerkgK = 'JPerkgK'
    '''
    Specific heat capacity, specific entropy, joules per kilogram Kelvin.
    '''
    JPerm2 = 'JPerm2'
    '''
    Insulation energy density, joules per square metre or watt second per square
    metre.
    '''
    JPerm3 = 'JPerm3'
    '''
    Energy density, joules per cubic metre.
    '''
    JPermol = 'JPermol'
    '''
    Molar energy, joules per mole.
    '''
    JPermolK = 'JPermolK'
    '''
    Molar entropy, molar heat capacity, joules per mole kelvin.
    '''
    JPers = 'JPers'
    '''
    Energy rate in joules per second (J/s).
    '''
    K = 'K'
    '''
    Temperature in kelvins.
    '''
    KPers = 'KPers'
    '''
    Temperature change rate in kelvins per second.
    '''
    M = 'M'
    '''
    Length, nautical miles (1 M = 1852 m).
    '''
    Mx = 'Mx'
    '''
    Magnetic flux, maxwells (1 Mx = 10-8 Wb).
    '''
    N = 'N'
    '''
    Force in newtons (kg·m/s²).
    '''
    NPerm = 'NPerm'
    '''
    Surface tension, newton per metre.
    '''
    Nm = 'Nm'
    '''
    Moment of force, newton metres.
    '''
    Oe = 'Oe'
    '''
    Magnetic field in oersteds, (1 Oe = (103/4p) A/m).
    '''
    Pa = 'Pa'
    '''
    Pressure in pascals (N/m²). Note: the absolute or relative measurement
    of pressure is implied with this entry. See below for more explicit forms.
    '''
    PaPers = 'PaPers'
    '''
    Pressure change rate in pascals per second.
    '''
    Pas = 'Pas'
    '''
    Dynamic viscosity, pascal seconds.
    '''
    Q = 'Q'
    '''
    Quantity power, Q.
    '''
    Qh = 'Qh'
    '''
    Quantity energy, Qh.
    '''
    S = 'S'
    '''
    Conductance in siemens.
    '''
    SPerm = 'SPerm'
    '''
    Conductance per length (F/m).
    '''
    Sv = 'Sv'
    '''
    Dose equivalent in sieverts (J/kg).
    '''
    T = 'T'
    '''
    Magnetic flux density in teslas (Wb/m2).
    '''
    V = 'V'
    '''
    Electric potential in volts (W/A).
    '''
    V2 = 'V2'
    '''
    Volt squared (W²/A²).
    '''
    V2h = 'V2h'
    '''
    Volt-squared hour, volt-squared-hours.
    '''
    VA = 'VA'
    '''
    Apparent power in volt amperes. See also real power and reactive power.
    '''
    VAh = 'VAh'
    '''
    Apparent energy in volt ampere hours.
    '''
    VAr = 'VAr'
    '''
    Reactive power in volt amperes reactive. The “reactive” or “imaginary”
    component of electrical power (VIsin(phi)). (See also real power and apparent
    power).
    Note: Different meter designs use different methods to arrive at their
    results. Some meters may compute reactive power as an arithmetic value,
    while others compute the value vectorially. The data consumer should determine
    the method in use and the suitability of the measurement for the intended
    purpose.
    '''
    VArh = 'VArh'
    '''
    Reactive energy in volt ampere reactive hours.
    '''
    VPerHz = 'VPerHz'
    '''
    Magnetic flux in volt per hertz.
    '''
    VPerV = 'VPerV'
    '''
    Voltage, ratio of voltages. Note: Users may need to supply a prefix such
    as ‘m’ to show rates such as ‘mV/V’.
    '''
    VPerVA = 'VPerVA'
    '''
    Power factor, PF, the ratio of the active power to the apparent power.
    Note: The sign convention used for power factor will differ between IEC
    meters and EEI (ANSI) meters. It is assumed that the data consumers understand
    the type of meter being used and agree on the sign convention in use at
    any given utility.
    '''
    VPerVAr = 'VPerVAr'
    '''
    Power factor, PF, the ratio of the active power to the apparent power.
    Note: The sign convention used for power factor will differ between IEC
    meters and EEI (ANSI) meters. It is assumed that the data consumers understand
    the type of meter being used and agree on the sign convention in use at
    any given utility.
    '''
    VPerm = 'VPerm'
    '''
    Electric field strength, volts per metre.
    '''
    Vh = 'Vh'
    '''
    Volt-hour, Volt hours.
    '''
    Vs = 'Vs'
    '''
    Volt seconds (Ws/A).
    '''
    W = 'W'
    '''
    Real power in watts (J/s). Electrical power may have real and reactive
    components. The real portion of electrical power (I&#178;R or VIcos(phi)),
    is expressed in Watts. See also apparent power and reactive power.
    '''
    WPerA = 'WPerA'
    '''
    Active power per current flow, watts per Ampere.
    '''
    WPerHz = 'WPerHz'
    '''
    Active power per change in frequency.
    '''
    WPerW = 'WPerW'
    '''
    Signal Strength, ratio of power. Note: Users may need to supply a prefix
    such as ‘m’ to show rates such as ‘mW/W’.
    '''
    WPerm2 = 'WPerm2'
    '''
    Heat flux density, irradiance, watts per square metre.
    '''
    WPerm2sr = 'WPerm2sr'
    '''
    Radiance, watts per square metre steradian.
    '''
    WPermK = 'WPermK'
    '''
    Thermal conductivity in watt/metres kelvin.
    '''
    WPers = 'WPers'
    '''
    Ramp rate in watts per second.
    '''
    WPersr = 'WPersr'
    '''
    Radiant intensity, watts per steradian.
    '''
    Wb = 'Wb'
    '''
    Magnetic flux in webers (V·s).
    '''
    Wh = 'Wh'
    '''
    Real energy in watt hours.
    '''
    anglemin = 'anglemin'
    '''
    Plane angle, minutes.
    '''
    anglesec = 'anglesec'
    '''
    Plane angle, seconds.
    '''
    bar = 'bar'
    '''
    Pressure in bars, (1 bar = 100 kPa).
    '''
    cd = 'cd'
    '''
    Luminous intensity in candelas.
    '''
    charPers = 'charPers'
    '''
    Data rate (baud) in characters per second.
    '''
    character = 'character'
    '''
    Number of characters.
    '''
    cosPhi = 'cosPhi'
    '''
    Power factor, dimensionless.
    Note 1: This definition of power factor only holds for balanced systems.
    See the alternative definition under code 153.
    Note 2 : Beware of differing sign conventions in use between the IEC and
    EEI. It is assumed that the data consumer understands the type of meter
    in use and the sign convention in use by the utility.
    '''
    count = 'count'
    '''
    Amount of substance, Counter value.
    '''
    d = 'd'
    '''
    Time in days, day = 24 h = 86400 s.
    '''
    dB = 'dB'
    '''
    Sound pressure level in decibels. Note: multiplier “d” is included in this
    unit symbol for compatibility with IEC 61850-7-3.
    '''
    dBm = 'dBm'
    '''
    Power level (logarithmic ratio of signal strength , Bel-mW), normalized
    to 1mW. Note: multiplier “d” is included in this unit symbol for compatibility
    with IEC 61850-7-3.
    '''
    deg = 'deg'
    '''
    Plane angle in degrees.
    '''
    degC = 'degC'
    '''
    Relative temperature in degrees Celsius.
    In the SI unit system the symbol is °C. Electric charge is measured in
    coulomb that has the unit symbol C. To distinguish degree Celsius from
    coulomb the symbol used in the UML is degC. The reason for not using °C
    is that the special character ° is difficult to manage in software.
    '''
    ft3 = 'ft3'
    '''
    Volume, cubic feet.
    '''
    gPerg = 'gPerg'
    '''
    Concentration, The ratio of the mass of a solute divided by the mass of
    the solution. Note: Users may need use a prefix such a ‘µ’ to express a
    quantity such as ‘µg/g’.
    '''
    gal = 'gal'
    '''
    Volume in gallons, US gallon (1 gal = 231 in3 = 128 fl ounce).
    '''
    h = 'h'
    '''
    Time in hours, hour = 60 min = 3600 s.
    '''
    ha = 'ha'
    '''
    Area, hectares.
    '''
    kat = 'kat'
    '''
    Catalytic activity, katal = mol / s.
    '''
    katPerm3 = 'katPerm3'
    '''
    Catalytic activity concentration, katals per cubic metre.
    '''
    kg = 'kg'
    '''
    Mass in kilograms. Note: multiplier “k” is included in this unit symbol
    for compatibility with IEC 61850-7-3.
    '''
    kgPerJ = 'kgPerJ'
    '''
    Weight per energy in kilograms per joule (kg/J). Note: multiplier “k” is
    included in this unit symbol for compatibility with IEC 61850-7-3.
    '''
    kgPerm3 = 'kgPerm3'
    '''
    Density in kilogram/cubic metres (kg/m³). Note: multiplier “k” is included
    in this unit symbol for compatibility with IEC 61850-7-3.
    '''
    kgm = 'kgm'
    '''
    Moment of mass in kilogram metres (kg·m) (first moment of mass). Note:
    multiplier “k” is included in this unit symbol for compatibility with IEC
    61850-7-3.
    '''
    kgm2 = 'kgm2'
    '''
    Moment of mass in kilogram square metres (kg·m²) (Second moment of mass,
    commonly called the moment of inertia). Note: multiplier “k” is included
    in this unit symbol for compatibility with IEC 61850-7-3.
    '''
    kn = 'kn'
    '''
    Speed, knots (1 kn = 1852/3600) m/s.
    '''
    l = 'l'
    '''
    Volume in litres, litre = dm3 = m3/1000.
    '''
    lPerh = 'lPerh'
    '''
    Volumetric flow rate, litres per hour.
    '''
    lPerl = 'lPerl'
    '''
    Concentration, The ratio of the volume of a solute divided by the volume
    of the solution. Note: Users may need use a prefix such a ‘µ’ to express
    a quantity such as ‘µL/L’.
    '''
    lPers = 'lPers'
    '''
    Volumetric flow rate in litres per second.
    '''
    lm = 'lm'
    '''
    Luminous flux in lumens (cd·sr).
    '''
    lx = 'lx'
    '''
    Illuminance in lux (lm/m²).
    '''
    m = 'm'
    '''
    Length in metres.
    '''
    m2 = 'm2'
    '''
    Area in square metres (m²).
    '''
    m2Pers = 'm2Pers'
    '''
    Viscosity in square metres / second (m²/s).
    '''
    m3 = 'm3'
    '''
    Volume in cubic metres (m³).
    '''
    m3Compensated = 'm3Compensated'
    '''
    Volume, cubic metres, with the value compensated for weather effects.
    '''
    m3Perh = 'm3Perh'
    '''
    Volumetric flow rate, cubic metres per hour.
    '''
    m3Perkg = 'm3Perkg'
    '''
    Specific volume, cubic metres per kilogram, v.
    '''
    m3Pers = 'm3Pers'
    '''
    Volumetric flow rate in cubic metres per second (m³/s).
    '''
    m3Uncompensated = 'm3Uncompensated'
    '''
    Volume, cubic metres, with the value uncompensated for weather effects.
    '''
    mPerm3 = 'mPerm3'
    '''
    Fuel efficiency in metres per cubic metres (m/m³).
    '''
    mPers = 'mPers'
    '''
    Velocity in metres per second (m/s).
    '''
    mPers2 = 'mPers2'
    '''
    Acceleration in metres per second squared (m/s²).
    '''
    min = 'min'
    '''
    Time in minutes, minute = 60 s.
    '''
    mmHg = 'mmHg'
    '''
    Pressure, millimetres of mercury (1 mmHg is approximately 133.3 Pa).
    '''
    mol = 'mol'
    '''
    Amount of substance in moles.
    '''
    molPerkg = 'molPerkg'
    '''
    Concentration, Molality, the amount of solute in moles and the amount of
    solvent in kilograms.
    '''
    molPerm3 = 'molPerm3'
    '''
    Concentration, The amount of substance concentration, (c), the amount of
    solvent in moles divided by the volume of solution in m³.
    '''
    molPermol = 'molPermol'
    '''
    Concentration, Molar fraction, the ratio of the molar amount of a solute
    divided by the molar amount of the solution.
    '''
    none = 'none'
    '''
    Dimension less quantity, e.g. count, per unit, etc.
    '''
    ohm = 'ohm'
    '''
    Electric resistance in ohms (V/A).
    '''
    ohmPerm = 'ohmPerm'
    '''
    Electric resistance per length in ohms per metre ((V/A)/m).
    '''
    ohmm = 'ohmm'
    '''
    Resistivity, ohm metres, (rho).
    '''
    onePerHz = 'onePerHz'
    '''
    Reciprocal of frequency (1/Hz).
    '''
    onePerm = 'onePerm'
    '''
    Wavenumber, reciprocal metres, (1/m).
    '''
    ppm = 'ppm'
    '''
    Concentration in parts per million.
    '''
    rad = 'rad'
    '''
    Plane angle in radians (m/m).
    '''
    radPers = 'radPers'
    '''
    Angular velocity in radians per second (rad/s).
    '''
    radPers2 = 'radPers2'
    '''
    Angular acceleration, radians per second squared.
    '''
    rev = 'rev'
    '''
    Amount of rotation, revolutions.
    '''
    rotPers = 'rotPers'
    '''
    Rotations per second (1/s). See also Hz (1/s).
    '''
    s = 's'
    '''
    Time in seconds.
    '''
    sPers = 'sPers'
    '''
    Time, Ratio of time. Note: Users may need to supply a prefix such as ‘&#181;’
    to show rates such as ‘&#181;s/s’.
    '''
    sr = 'sr'
    '''
    Solid angle in steradians (m2/m2).
    '''
    therm = 'therm'
    '''
    Energy, therms.
    '''
    tonne = 'tonne'
    '''
    Mass in tons, “tonne” or “metric ton” (1000 kg = 1 Mg).
    '''

@dataclass
class ActivePower():
    '''
    Product of RMS value of the voltage and the RMS value of the in-phase
    component of the current.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.W)
    def __post_init__(self):
        pint(self)

@dataclass
class ActivePowerChangeRate():
    '''
    Rate of change of active power per time.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.WPers)
    def __post_init__(self):
        pint(self)

@dataclass
class ActivePowerPerCurrentFlow():
    '''
    Active power variation with current flow.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.WPerA)
    def __post_init__(self):
        pint(self)

@dataclass
class ActivePowerPerFrequency():
    '''
    Active power variation with frequency.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.WPerHz)
    def __post_init__(self):
        pint(self)

@dataclass
class Admittance():
    '''
    Ratio of current to voltage.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.S)
    def __post_init__(self):
        pint(self)

@dataclass
class AngleDegrees():
    '''
    Ratio of current to voltage.
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.deg
    def __post_init__(self):
        pint(self)

@dataclass
class AngleRadians():
    '''
    Ratio of current to voltage.
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.rad
    def __post_init__(self):
        pint(self)

@dataclass
class ApparentPower():
    '''
    Product of the RMS value of the voltage and the RMS value of the current.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.VA)
    def __post_init__(self):
        pint(self)

@dataclass
class Area():
    '''
    Area.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    @property #read-only
    def unit(self):
        return UnitSymbol.m2
    def __post_init__(self):
        pint(self)

@dataclass
class Capacitance():
    '''
    Capacitive part of reactance (imaginary part of impedance), at rated frequency.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.F)
    def __post_init__(self):
        pint(self)

@dataclass
class CapacitancePerLength():
    '''
    Capacitance per unit length.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.FPerm)
    def __post_init__(self):
        pint(self)

@dataclass
class Classification():
    '''
    Classification of level.  Specify as 1..n, with 1 being the most detailed,
    highest priority, etc as described on the attribute using this data type.
    '''
    value: int = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.rad
    def __post_init__(self):
        pint(self)

@dataclass
class Conductance():
    '''
    Factor by which voltage must be multiplied to give corresponding power lost
    from a circuit. Real part of admittance.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.S)
    def __post_init__(self):
        pint(self)

@dataclass
class ConductancePerLength():
    '''
    Real part of admittance per unit of length.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.SPerm)
    def __post_init__(self):
        pint(self)

@dataclass
class CurrentFlow():
    '''
    Electrical current with sign convention: positive flow is out of the
    conducting equipment into the connectivity node. Can be both AC and DC.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.A)
    def __post_init__(self):
        pint(self)

@dataclass
class Damping():
    '''
    Per-unit active power variation with frequency referenced on the system
    apparent power base. Typical values are in the range 1,0 - 2,0.
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.onePerHz
    def __post_init__(self):
        pint(self)

@dataclass
class Date():
    '''
    Date as "yyyy-mm-dd", which conforms with ISO 8601. UTC time zone is
    specified as "yyyy-mm-ddZ". A local timezone relative UTC is specified as
    "yyyy-mm-dd(+/-)hh:mm".
    '''

@dataclass
class DateInterval():
    '''
    Interval between two dates.
    '''
    start: MonthDay = field(default=None)
    end: MonthDay = field(default=None)

@dataclass
class Displacement():
    '''
    Unit of displacement relative to a reference position,
    hence can be negative.
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.m
    def __post_init__(self):
        pint(self)

@dataclass
class Duration():
    '''
    Duration as "PnYnMnDTnHnMnS" which conforms to ISO 8601, where nY expresses
    a number of years, nM a number of months, nD a number of days. The letter
    T separates the date expression from the time expression and, after it,
    nH identifies a number of hours, nM a number of minutes and nS a number
    of seconds. The number of seconds could be expressed as a decimal number,
    but all other numbers are integers.
    '''

@dataclass
class Emission():
    '''
    Quantity of emission per fuel heat content.
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.kgPerJ
    def __post_init__(self):
        pint(self)

@dataclass
class Frequency():
    '''
    Cycles per second.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    @property #read-only
    def unit(self):
        return UnitSymbol.Hz
    def __post_init__(self):
        pint(self)

@dataclass
class HeatRate():
    '''
    Heat generated, in energy per time unit of elapsed time.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    @property #read-only
    def unit(self):
        return UnitSymbol.JPers
    def __post_init__(self):
        pint(self)

@dataclass
class Hours():
    '''
    Time specified in hours
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.h
    def __post_init__(self):
        pint(self)

@dataclass
class Impedance():
    '''
    Ratio of voltage to current.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.ohm)
    def __post_init__(self):
        pint(self)

@dataclass
class Inductance():
    '''
    Inductive part of reactance (imaginary part of impedance), at rated frequency.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.H)
    def __post_init__(self):
        pint(self)


@dataclass
class InductancePerLength():
    '''
    Inductance per unit of length.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.HPerm)
    def __post_init__(self):
        pint(self)

@dataclass
class KiloActivePower():
    '''
    Inductance per unit of length.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.k)
    unit: UnitSymbol = field(default=UnitSymbol.W)
    def __post_init__(self):
        pint(self)

@dataclass
class Length():
    '''
    Unit of length. It shall be a positive value or zero.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    @property #read-only
    def unit(self):
        return UnitSymbol.m
    def __post_init__(self):
        pint(self)

@dataclass
class Mass():
    '''
    Heat generated, in energy per time unit of elapsed time.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.k)
    @property #read-only
    def unit(self):
        return UnitSymbol.g
    def __post_init__(self):
        pint(self)

@dataclass
class Minutes():
    '''
    Time in minutes.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.k)
    @property #read-only
    def unit(self):
        return UnitSymbol.min
    def __post_init__(self):
        pint(self)

@dataclass
class MonthDay():
    '''
    MonthDay format as "--mm-dd", which conforms with XSD data type gMonthDay.
    '''

@dataclass
class MonthDayInterval():
    '''
    Interval between two times specified as month and day.
    '''
    start: MonthDay = field(default=None)
    end: MonthDay = field(default=None)

@dataclass
class PU():
    '''
    Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.none)
    def __post_init__(self):
        pint(self)

@dataclass
class PerCent():
    '''
    Percentage on a defined base. For example, specify as 100 to indicate at the defined base.
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.none
    def __post_init__(self):
        pint(self)

@dataclass
class Pressure():
    '''
    Time in minutes.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    @property #read-only
    def unit(self):
        return UnitSymbol.Pa
    def __post_init__(self):
        pint(self)

@dataclass
class Reactance():
    '''
    Reactance (imaginary part of impedance), at rated frequency.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.ohm)
    def __post_init__(self):
        pint(self)


@dataclass
class ReactancePerLength():
    '''
    Reactance (imaginary part of impedance) per unit of length, at rated frequency.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.ohmPerm)
    def __post_init__(self):
        pint(self)

@dataclass
class ReactivePower():
    '''
    Product of RMS value of the voltage and the RMS value of the quadrature
    component of the current.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.VAr)
    def __post_init__(self):
        pint(self)

@dataclass
class Resistance():
    '''
    Resistance (real part of impedance).
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.ohm)
    def __post_init__(self):
        pint(self)

@dataclass
class ResistancePerLength():
    '''
    Resistance (real part of impedance) per unit of length.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.ohmPerm)
    def __post_init__(self):
        pint(self)

@dataclass
class RotationSpeed():
    '''
    Number of revolutions per second.
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.none
    def __post_init__(self):
        pint(self)

@dataclass
class Seconds():
    '''
    Time specified in seconds
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.s
    def __post_init__(self):
        pint(self)

@dataclass
class Speed():
    '''
    Distance per unit of time
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.mPers
    def __post_init__(self):
        pint(self)

@dataclass
class Susceptance():
    '''
    Imaginary part of admittance.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.S)
    def __post_init__(self):
        pint(self)

@dataclass
class SusceptancePerLength():
    '''
    Imaginary part of admittance per unit of length.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.SPerm)
    def __post_init__(self):
        pint(self)

@dataclass
class Temperature():
    '''
    Distance per unit of time
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.degC
    def __post_init__(self):
        pint(self)

@dataclass
class Time():
    '''
    Time as "hh:mm:ss.sss", which conforms with ISO 8601. UTC time zone is
    specified as "hh:mm:ss.sssZ". A local timezone relative UTC is specified
    as "hh:mm:ss.sss±hh:mm". The second component (shown here as "ss.sss")
    could have any number of digits in its fractional part to allow any
    kind of precision beyond seconds.
    '''

@dataclass
class TimeInterval():
    '''
    Interval between two times.
    '''
    start: MonthDay = field(default=None)
    end: MonthDay = field(default=None)

@dataclass
class Voltage():
    '''
    Electrical voltage, can be both AC and DC.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.V)
    def __post_init__(self):
        pint(self)

@dataclass
class VoltagePerReactivePower():
    '''
    Voltage variation with reactive power.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    unit: UnitSymbol = field(default=UnitSymbol.VPerVAr)
    def __post_init__(self):
        pint(self)

@dataclass
class Volume():
    '''
    Volume.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    @property #read-only
    def unit(self):
        return UnitSymbol.m3
    def __post_init__(self):
        pint(self)

@dataclass
class VolumeFlowRate():
    '''
    Volume per time
    '''
    value: float = field(default=None)
    @property #read-only
    def multiplier(self):
        return UnitMultiplier.none
    @property #read-only
    def unit(self):
        return UnitSymbol.m3Pers
    def __post_init__(self):
        pint(self)

@dataclass
class WaterLevel():
    '''
    Reservoir water level referred to a given datum such as mean sea level.
    '''
    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    @property #read-only
    def unit(self):
        return UnitSymbol.m
    def __post_init__(self):
        pint(self)

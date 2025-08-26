from enum import Enum


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
    as "m" to show rates such as "mA/A".
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
    such as "m" to show rates such as "mHz/Hz".
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
    as "m" to show rates such as "mV/V".
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
    such as "m" to show rates such as "mW/W".
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
    the solution. Note: Users may need use a prefix such a "µ" to express a
    quantity such as "µg/g".
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
    kgPerm = 'kgPerm'
    '''
    Mass per unit length (kg/m) Note: multiplier “k” is included
    in this unit symbol for compatibility with IEC 61850-7-3.
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
    of the solution. Note: Users may need use a prefix such a "µ" to express
    a quantity such as "µL/L".
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
    Time, Ratio of time. Note: Users may need to supply a prefix such as "&#181;"
    to show rates such as "&#181;s/s".
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

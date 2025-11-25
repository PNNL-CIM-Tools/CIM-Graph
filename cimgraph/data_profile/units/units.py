
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from importlib import resources as impresources
from typing import Optional

from pint import Quantity, UnitRegistry

import cimgraph.data_profile.units.cim_units as cim_units
from cimgraph.data_profile.units.cim_units import UnitMultiplier, UnitSymbol

units_file = impresources.files(cim_units).joinpath('units.txt')
ureg = UnitRegistry()
ureg.load_definitions(units_file)


class CIMUnit():
    value: Optional[float]|CIMUnit
    value: Optional[float]|CIMUnit
    unit: Optional[UnitSymbol]
    multiplier: Optional[UnitMultiplier]

    def __pint__(self, value:float|CIMUnit, input_unit:str, input_multiplier:str=None):
    def __pint__(self, value:float|CIMUnit, input_unit:str, input_multiplier:str=None):

        if input_multiplier is not None:
            input_unit = input_multiplier + input_unit
            
        if isinstance(value, CIMUnit):
            value = value.quantity.to(input_unit).magnitude

        if self.multiplier.value != 'none':
            self.quantity = ureg.Quantity(value=float(value), units=self.multiplier.value+input_unit)
            self.quantity = self.quantity.to(self.multiplier.value+self.unit.value)

        else:
            self.quantity = ureg.Quantity(value=float(value), units=input_unit)
            self.quantity = self.quantity.to(self.unit.value)

        self.value = self.quantity.magnitude

    def __repr__(self):
        return str(self.quantity)
    
    def __float__(self):
        return float(self.quantity.magnitude)
    
    def __int__(self):
        return int(self.quantity.magnitude)
    
    def to(self, unit:str):
        return self.quantity.to(unit).magnitude
        

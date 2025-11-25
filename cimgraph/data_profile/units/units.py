
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
    value: Optional[float]
    unit: Optional[UnitSymbol]
    multiplier: Optional[UnitMultiplier]

    def __pint__(self, value:float, input_unit:str, input_multiplier:str=None):

        if input_multiplier is not None:
            input_unit = input_multiplier + input_unit

        if self.multiplier.value != 'none':
            self.quantity = ureg.Quantity(value=float(value), units=self.multiplier.value+input_unit)
            self.quantity = self.quantity.to(self.multiplier.value+self.unit.value)

        else:
            self.quantity = ureg.Quantity(value=float(value), units=input_unit)
            self.quantity = self.quantity.to(self.unit.value)

        self.value = self.quantity.magnitude

    def __repr__(self):
        return str(self.quantity)

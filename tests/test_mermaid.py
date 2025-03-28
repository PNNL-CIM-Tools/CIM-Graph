


breaker = cim.Breaker(name = 'breaker12', open=False, inService=True)
substation = cim.Substation(name = 'sub1234')
t1 = cim.Terminal(name = 'brk12_t1')
t2 = cim.Terminal(name = 'brk12_t2')
basev = cim.BaseVoltage(name = 'base12kv', nominalVoltage=12470)
breaker.EquipmentContainer = substation
breaker.Terminals = [t1, t2]
breaker.BaseVoltage = basev

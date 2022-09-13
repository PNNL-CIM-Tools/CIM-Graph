from typing import List, Dict



def add_to_catalog(obj: object, catalog: Dict) -> Dict:
    if obj.mRID == None:
        raise ValueError('Object must contain an mRID')
    if obj.mRID not in catalog:
        catalog[obj.mRID] = obj
    return catalog

def add_to_typed_catalog(obj: object, typed_catalog: Dict) -> Dict:
    if type(obj) not in typed_catalog:
        typed_catalog[type(obj)] = {}
    if obj.mRID not in typed_catalog[type(obj)]:
        typed_catalog[type(obj)][obj.mRID] = obj
    return typed_catalog


def get_all_by_type(typed_catalog: Dict, obj_type: type) -> List[object]:
    objects = typed_catalog.get(obj_type) if typed_catalog.get(obj_type) is not None else []
    for obj in objects:
        if obj.mRID not in self.is_loaded:
            load_all_attributes(obj)
            
from cim.models.distributed_model import DistributedModel
from cim.models.switch_area import SwitchArea
from cim.models.secondary_area import SecondaryArea

__all__ = ['DistributedModel', 'SwitchArea', 'SecondaryArea']

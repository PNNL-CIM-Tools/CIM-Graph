import time
import json
import logging
import importlib

_log = logging.getLogger(__name__)

# from cimgraph.models.feeder_model import FeederModel


class FeederTopology():

    def __init__(self, cim_profile):
        self.cim = importlib.import_module('cimgraph.data_profile.' + cim_profile)

    def build_switch_areas(self,
                           graph,
                           switch_list: list[str] = None,
                           switch_classes: list[type] = None):

        if switch_classes is None:
            switch_classes = [self.cim.Breaker, self.cim.Sectionaliser]

        for class_type in switch_classes:
            for switch in graph[class_type].values():

                pass

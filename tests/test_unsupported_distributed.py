"""NodeBreakerModel and BusBranchModel have no distributed build; asking for one fails."""
from pathlib import Path

import cimprofiles.cim17.cimhub_2023 as cim
import pytest

from cimgraph.core import get_cim_profile
from cimgraph.databases import XMLFile
from cimgraph.models import BusBranchModel, NodeBreakerModel

IEEE13 = Path(__file__).parent / 'test_models' / 'ieee13.xml'


@pytest.mark.parametrize('model_class', [NodeBreakerModel, BusBranchModel])
def test_distributed_build_is_not_implemented(model_class, monkeypatch):
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2023')
    get_cim_profile.cache_clear()
    connection = XMLFile(str(IEEE13))
    with pytest.raises(NotImplementedError, match='distributed=True'):
        model_class(connection=connection, container=cim.Feeder(), distributed=True)
    get_cim_profile.cache_clear()

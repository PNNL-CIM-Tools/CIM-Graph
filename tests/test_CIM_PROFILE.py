from cimgraph.data_profile import CIM_PROFILE


def test_CIM_PROFILE():
    assert len(CIM_PROFILE) == 7
    assert CIM_PROFILE.CIM17V40.value == 'cim17v40'
    assert CIM_PROFILE.CIMHUB_2023.value == 'cimhub_2023'
    assert CIM_PROFILE.CIMHUB_2026.value == 'cimhub_2026'
    assert CIM_PROFILE.RC4_2021.value == 'rc4_2021'
    assert CIM_PROFILE.CIM18V17.value == 'cim18v17'

"""Tests for runtime-merged CIM profiles driving cim-graph connections and models.

The merge machinery itself is tested in cimprofiles.
"""
from __future__ import annotations

from pathlib import Path

_ROUND_TRIP_MODEL = Path(__file__).parent / 'test_models' / 'ieee9500bal.xml'
# Multi-part metadata header + two part files (connectivity + asset split):
_METADATA_CIMX = Path(__file__).parent / 'test_models' / 'ieee13_metadata.cimx'

# Namespace used by cim18gmdm fields (CIM101 draft).
_NS = {
    'cim': 'http://cim.ucaiug.io/CIM101/draft#',
    'gmdm': 'http://epri.com/gmdm/2025#',
}

# Comma-spec for the two-profile connectivity+electrical merge.
_CONN_ELEC_SPEC = (
    'cimprofiles.cim18.cim18gmdm.connectivity,'
    'cimprofiles.cim18.cim18gmdm.electrical'
)

# Comma-spec for connectivity+electrical+asset (needed to load the assets part file).
_CONN_ELEC_ASSET_SPEC = (
    'cimprofiles.cim18.cim18gmdm.connectivity,'
    'cimprofiles.cim18.cim18gmdm.electrical,'
    'cimprofiles.cim18.cim18gmdm.asset'
)


def test_merged_profile_reads_and_writes_real_xml(tmp_path, monkeypatch):
    """Baseline round-trip: a runtime-merged profile drives XMLFile + FeederModel.

    Proves the merged module satisfies the real profile contract against a
    single-file fixture — it loads into a graph and writes back out.
    """
    from cimgraph import utils
    from cimgraph.core.env_vars import get_cim_profile
    from cimgraph.databases import XMLFile
    from cimgraph.models import FeederModel

    monkeypatch.setenv('CIMG_CIM_PROFILE', _CONN_ELEC_SPEC)

    file = XMLFile(filename=str(_ROUND_TRIP_MODEL))
    network = FeederModel(container=None, connection=file)

    _, merged = get_cim_profile()
    MergedACLineSegment = getattr(merged, 'ACLineSegment')
    assert MergedACLineSegment in network.graph
    assert len(network.graph[MergedACLineSegment]) > 0

    out = tmp_path / 'round_trip.xml'
    utils.write_xml(network=network, filename=str(out), namespaces=_NS)
    assert out.exists()
    assert out.stat().st_size > 0


def test_class_identity_guaranteed_across_connection_and_model(monkeypatch):
    """Core identity guarantee: connection.cim and network.cim are the same object.

    This is the failure mode the whole 0.5 profile-identity work prevents.
    Both ConnectionInterface.__init__ and FeederModel.__post_init__ call
    get_cim_profile(); _merge_memo ensures they receive the identical module
    object (not two separately-constructed modules with structurally-equal but
    identity-distinct classes).

    If this breaks, graph.get(network.cim.ACLineSegment) silently returns None
    even when the graph contains ACLineSegments, because the key class objects
    are distinct.
    """
    from cimgraph.databases import XMLFile
    from cimgraph.models import FeederModel

    monkeypatch.setenv('CIMG_CIM_PROFILE', _CONN_ELEC_SPEC)

    file = XMLFile(filename=str(_ROUND_TRIP_MODEL))
    network = FeederModel(container=None, connection=file)

    # Both must resolve to the exact same module object via _merge_memo.
    assert file.cim is network.cim, (
        'file.cim and network.cim are different module objects — '
        'graph key lookup will silently fail'
    )
    # And the graph is actually populated using that shared class as key.
    assert file.cim.ACLineSegment in network.graph
    assert len(network.graph[file.cim.ACLineSegment]) > 0


def test_metadata_cimx_multi_part_merge(tmp_path, monkeypatch):
    """Full integration: .cimx metadata header + multi-profile merge.

    Replicates the 9500node_merge_metadata.ipynb workflow in a form you can
    hand-verify: a metadata graph resolves two part files (equipment + assets),
    each conforming to a different GMDM sub-profile, into one FeederModel.

    This proves:
    - XMLFile(metadata=...) resolves part paths relative to the .cimx file
    - The merged profile covers classes from both parts
    - Asset-only classes (TransformerEndInfo) appear alongside connectivity
      classes (ACLineSegment) in the same graph
    - Class identity holds: file.cim is network.cim
    - The merged graph round-trips through write_xml
    """
    from cimgraph import utils
    from cimgraph.databases import XMLFile
    from cimgraph.models import FeederModel

    monkeypatch.setenv('CIMG_CIM_PROFILE', _CONN_ELEC_ASSET_SPEC)

    file = XMLFile(metadata=str(_METADATA_CIMX), namespaces=_NS)

    # Metadata header was parsed and resolved to exactly two part files.
    assert file.metadata_graph is not None
    assert len(file.filename) == 2

    network = FeederModel(container=None, connection=file)

    cim = network.cim

    # Identity guarantee holds across the metadata path too.
    assert file.cim is network.cim

    # Equipment part contributes ACLineSegment objects.
    assert cim.ACLineSegment in network.graph
    assert len(network.graph[cim.ACLineSegment]) > 0

    # Asset part contributes TransformerEndInfo (asset-profile-only class).
    assert cim.TransformerEndInfo in network.graph
    assert len(network.graph[cim.TransformerEndInfo]) > 0

    # Both classes visible via the same merged profile — this is the cross-part
    # graph accumulation that the cim_override+chained-FeederModel trick used
    # to require. Now a single FeederModel call does it.
    acls_count = len(network.graph[cim.ACLineSegment])
    tei_count = len(network.graph[cim.TransformerEndInfo])
    print(f'\n  ACLineSegment: {acls_count}, TransformerEndInfo: {tei_count}')

    out = tmp_path / 'multi_part_round_trip.xml'
    utils.write_xml(network=network, filename=str(out), namespaces=_NS)
    assert out.exists()
    assert out.stat().st_size > 0


# ── Type-stub generation tests ─────────────────────────────────────────

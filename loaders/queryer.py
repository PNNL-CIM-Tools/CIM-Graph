from __future__ import annotations

from dataclasses import dataclass, field
from pprint import pprint
from typing import Type, List, Dict, Set, Optional

from gridappsd_cim import Terminal, Equipment, LinearShuntCompensator, RegulatingControl, ConnectivityNode, \
    TransformerTank

from SPARQLWrapper import SPARQLWrapper, JSON


@dataclass
class Connection:
    def execute(self, query):
        pass

    def next_result(self):
        pass

    def num_results(self):
        pass

    def retrive_instance(self, mrid: str) -> object:
        # Do query on this connection and retieve a typed instance from the datasource.

        return


@dataclass
class DummyConnection(Connection):
    def retrive_instance(self, mrid: str) -> object:
        if mrid == '_9D725810-BFD6-44C6-961A-2BC027F6FC95':
            return LinearShuntCompensator(mRID=mrid, name="ShutCompensator1")
        elif mrid == '_D2E930A7-B136-4ACA-A996-8DB5C60AADF3':
            return Terminal(mRID=mrid, name="Terminal")
        else:
            None
        # else:
        #     raise ValueError(f"mrid not found {mrid}")


@dataclass
class BlazeGraphConnection(Connection):
    url: str
    feeder_mrid: str = None
    sparql: SPARQLWrapper = None

    def load_attributes(self, obj: object):
        if isinstance(obj, LinearShuntCompensator):
            # load all attributes onto obj from a custom query for specific compensator
            setattr(obj, "b0PerSection", 5)

    def retrive_instance(self, mrid: str, feeder_mrid: str = None) -> object:
        if feeder_mrid is None:
            feeder_mrid = self.feeder_mrid
        if not feeder_mrid:
            raise ValueError("feeder must have been specified in constructor or as a parameter.")
        sparql = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX c:  <http://iec.ch/TC57/CIM100#>
        SELECT ?eqid ?eqname ?class
        {
          VALUES ?fdrid {"%s"}
          VALUES ?eqid {"%s"}
          ?fdr c:IdentifiedObject.mRID ?fdrid.
          ?eq c:IdentifiedObject.name ?eqname.
          bind(strafter(str(?eq),"#") as ?eqid).
          ?eq a ?classraw.
          bind(strafter(str(?classraw),"CIM100#") as ?class)
        }
        GROUP BY  ?eqid ?eqname ?class
        ORDER by  ?fdrid
        """ % (feeder_mrid, mrid)
        if self.sparql is None:
            self.sparql = SPARQLWrapper(self.url)
            self.sparql.setReturnFormat(JSON)
        self.sparql.setQuery(sparql)

        ret = self.sparql.query().convert()

        for result in ret['results']['bindings']:
            cls = result['class']['value']
            mrid = result['eqid']['value']
            return eval(f"{cls}(mRID='{mrid}')")

        #raise ValueError(f"Unknown equipment_id {mrid}")


@dataclass
class SwitchArea:
    connectivity_node: List[ConnectivityNode]
    addressable_equipment: List[str]
    unaddressable_equipment: List[str]
    boundary_switches: List[str]

    catalog: Dict[str, Type] = field(default_factory=dict)
    catalog_type: Dict[Type, List] = field(default_factory=dict)
    is_loaded: Optional[Set] = field(default_factory=set)
    __connection__: Optional[Connection] = None

    def get_by_type(self, obj_type: Type) -> List[Type]:
        items = self.catalog_type.get(obj_type) if self.catalog_type.get(obj_type) is not None else []
        for t in items:
            if t.mRID not in self.is_loaded:
                self.__connection__.load_attributes(t)
        return items

    @staticmethod
    def load_from_topo_response(topo_response: Dict, conn: Connection) -> SwitchArea:
        sa = SwitchArea(addressable_equipment=topo_response['addressable_equipment'],
                        unaddressable_equipment=topo_response['unaddressable_equipment'],
                        boundary_switches=topo_response['boundary_switches'],
                        catalog={}, catalog_type={}, connectivity_node=[]
                        )
        sa.__connection__ = conn

        for mrid in sa.addressable_equipment:
            obj = conn.retrive_instance(mrid)
            if not sa.catalog_type.get(type(obj)):
                sa.catalog_type[type(obj)] = []
            sa.catalog_type[type(obj)].append(obj)
            sa.catalog[mrid] = obj
                #raise ValueError("Only good mrid's should come back from topological response.")
        return sa


def get_topo_response() -> Dict:
    return {
        "feeders": {
            "feeder_id": "_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62",
            "addressable_equipment": ["_52DE9189-20DC-4C73-BDEE-E960FE1F9493", "_CE5D0651-676B-4AF3-8D67-41BF1B33E30C",
                                      "_43EF8365-F932-409B-A51E-FBED3F6DFFAA", "_43EF8365-F932-409B-A51E-FBED3F6DFFAA",
                                      "_2858B6C2-0886-4269-884C-06FA8B887319", "_517413CB-6977-46FA-8911-C82332E42884",
                                      "_CE5D0651-676B-4AF3-8D67-41BF1B33E30C", "_517413CB-6977-46FA-8911-C82332E42884",
                                      "_2858B6C2-0886-4269-884C-06FA8B887319"],
            "unaddressable_equipment": ["_44FC5A86-A099-45B8-B847-F685C5027AFB",
                                        "_B6363F07-B1BC-420B-AA4C-A34BB8F05827",
                                        "_E2E0FC64-8D45-4C55-BDB9-EAB827A46FBC",
                                        "_7c6f94c1-1419-4582-ab2d-a0b11772c26b",
                                        "_b393e719-0981-4498-9d96-07f1be7de009",
                                        "_f11a9ad9-5b68-483b-b52f-dd4af07bb77d",
                                        "_44FC5A86-A099-45B8-B847-F685C5027AFB",
                                        "_B6363F07-B1BC-420B-AA4C-A34BB8F05827",
                                        "_E2E0FC64-8D45-4C55-BDB9-EAB827A46FBC",
                                        "_A04CDFB1-E951-4FC4-8882-0323CD70AE3C",
                                        "_44FC5A86-A099-45B8-B847-F685C5027AFB",
                                        "_B6363F07-B1BC-420B-AA4C-A34BB8F05827",
                                        "_E2E0FC64-8D45-4C55-BDB9-EAB827A46FBC",
                                        "_5ad9e784-5b6c-4f2c-bc4d-1ccc31cfd96b",
                                        "_8dc4079e-6bbb-491d-9f4c-0c240228b647",
                                        "_fc4adc62-5608-467f-aab7-75893b574998",
                                        "_5d00b173-726b-4f64-b93e-c60648276c66",
                                        "_8d72f997-ba3e-4954-91b6-62fc3304d165",
                                        "_f782d376-467f-46bc-a0f5-3f500d6570aa",
                                        "_0a2f7676-f619-405b-bb80-8f51f4d7a25f",
                                        "_9f4bef6c-c68d-42a9-ade6-206a8b365ce9",
                                        "_c16593db-3c64-4504-9387-17f19f558549",
                                        "_44FC5A86-A099-45B8-B847-F685C5027AFB",
                                        "_B6363F07-B1BC-420B-AA4C-A34BB8F05827",
                                        "_E2E0FC64-8D45-4C55-BDB9-EAB827A46FBC",
                                        "_FBE26B35-13AB-457D-9795-DF58B28E309D",
                                        "_1C6781A2-5B9D-4525-8A9B-F9B32C4C4AC0",
                                        "_A04CDFB1-E951-4FC4-8882-0323CD70AE3C",
                                        "_198ca97f-d307-4fe7-8a79-5caa1c3e45d0",
                                        "_907b4408-7271-4407-9e38-3d019dc1bc68",
                                        "_cc70103a-126e-4ec1-8583-12412dd8195d",
                                        "_27897da2-d7e1-438c-a6e4-4b3cfe8e79fa",
                                        "_d92644c9-5bd2-4312-8e31-3bec6510e646",
                                        "_dad6dd20-9bfc-4bd9-b76e-2e0fd3b0d5ba",
                                        "_7ca7c18c-3861-47bf-82cf-5a72d618b18a",
                                        "_80ef10f9-3f4f-4fd2-8262-caedf7442fda",
                                        "_cd64f70b-91d8-460b-af28-688e9709f319",
                                        "_0cbdf98b-b5e4-4bc3-93d6-08db08947794",
                                        "_0f4457a6-a3cb-42b0-a06c-b31d5c7a17ff",
                                        "_bc165aa6-347d-4551-8abf-016044675a6f",
                                        "_65599f7e-3e93-4456-a2b1-bba7a46337b6",
                                        "_6bb8ef03-ec84-421f-8d28-cd1a3813e614",
                                        "_FBE26B35-13AB-457D-9795-DF58B28E309D",
                                        "_8b6bd68f-c84d-45e1-91b9-b0406fbaa3b1",
                                        "_d56a4982-0c80-45d0-8cb8-c24097138b63",
                                        "_d638fbbc-9b85-416e-87b8-37c9785e1611",
                                        "_1C6781A2-5B9D-4525-8A9B-F9B32C4C4AC0",
                                        "_0BBD0EA3-F665-465B-86FD-FC8B8466AD53",
                                        "_c7c58261-4885-46ee-beb9-c94c6c29451f",
                                        "_98a81464-d7b6-4044-9b48-a92e179884dc",
                                        "_d8ea43c7-2107-4975-9ddb-4279628daf18",
                                        "_2d9ed148-d492-4e7d-b9af-81a407e74a59",
                                        "_4e30ae83-418c-4cfb-99eb-5572e00b4ec4",
                                        "_d23fd30b-e3f9-4a43-b3c4-2f2697dba851",
                                        "_0BBD0EA3-F665-465B-86FD-FC8B8466AD53",
                                        "_7a436400-3a77-4eaf-bb04-ef7954fcbdd9",
                                        "_5f1dfa9f-e754-471d-9c74-c1a9441e95a3",
                                        "_84f75532-a514-4355-bf0e-2f8d82c736ae",
                                        "_e1b4fd36-01d0-4d7d-9223-2279911fe8c3",
                                        "_1E6B5C97-C4E8-4CED-B9A5-6E69F389DA93",
                                        "_5500424b-9931-4f09-a22b-d24a47517920",
                                        "_bd95505f-3f55-43d2-b8b2-2c97b2c86603",
                                        "_f3001cb9-4c00-45ab-a73f-537be73f583c",
                                        "_37fc9b9a-0bc9-4417-8214-52afc237735f",
                                        "_697532b4-9520-4de4-80e9-2b6a77c8a089",
                                        "_d9e22ddd-f4f2-426c-911d-cf08ff5cc9a0",
                                        "_1E6B5C97-C4E8-4CED-B9A5-6E69F389DA93",
                                        "_5ae00771-adeb-4ee2-92a3-7c991c579ce1",
                                        "_77cf5e05-b332-4203-937a-53f58b4f4585",
                                        "_247f50ee-6bc5-4588-bdf1-9b480e09840e",
                                        "_5842f2db-ad93-494a-a372-c8e83e637147",
                                        "_87c273f2-8e55-4169-adeb-2df020776c06",
                                        "_919d79f9-9719-492b-bf8b-46cffc7579ad",
                                        "_9d580686-9c5d-42a6-9e0b-ef08c7d80256",
                                        "_ab19de32-3fad-4654-b546-6b785b2d65e3",
                                        "_51037d29-941b-4e9f-ae86-99dd37bb2c9d",
                                        "_54e2019e-e234-4dbb-85d6-227b245040ae",
                                        "_48720b2c-7908-4f18-a80d-f7f7f4099753",
                                        "_683bbf2f-7ea6-45c6-805e-5e4b7f5000a2",
                                        "_0ab88ca4-fb60-4a67-8f77-5f15af245b64",
                                        "_25938754-4fe8-4621-9414-7d519bc9fde3",
                                        "_78116a30-9d83-4715-a9d2-dda61687a0b9",
                                        "_7cc37959-2a82-4911-8a23-8ad09378c85c",
                                        "_cd76b30b-8e1c-45fb-b03a-79847254ead8",
                                        "_d057e1e2-71ad-4293-b89e-e9e9e84a2522",
                                        "_f0af2090-d2aa-40fb-8878-45d75c4ae59f",
                                        "_07b694ae-bde0-431c-a740-362a9f476949",
                                        "_c3a9b1e7-7a52-4fa5-a199-1fd6035abc21",
                                        "_d2d52e14-2111-486e-a59a-d8c5b5f7bf92",
                                        "_8E180773-2A9B-4136-BC9A-132A52C8E276",
                                        "_0fe87976-0177-42f3-817b-b468225220b2",
                                        "_2d31c620-a2f9-4f84-9102-9a8fe574ab6b",
                                        "_8E180773-2A9B-4136-BC9A-132A52C8E276",
                                        "_fad827c5-f344-498e-ab39-29883d4c6bb6",
                                        "_7a84c113-d427-4802-a769-b6edc48451c7",
                                        "_162b4555-f748-4829-8e71-bbbecf4e4bcb",
                                        "_eb606875-f620-4c4e-b559-cd587ba0ecf8",
                                        "_6c08f0e8-eb6f-4261-a3f6-3aa9d1e99c75",
                                        "_7060D0BB-B30D-4932-8FA1-40820A0FC4D0",
                                        "_3e3bdc6c-d985-4659-9cb7-82ea8212ba4f",
                                        "_59c9a186-c0a8-4f85-a524-d6ef0d27700a",
                                        "_5c9a17db-6f03-4626-9464-41d3a5ddeb15",
                                        "_d3a28545-dbfd-4cc4-9f3a-52e2ff130d93",
                                        "_8007b83e-40fa-4e87-9df7-a1097dc3b3e7",
                                        "_2abd660f-3dc2-4611-95a0-9adebae7fe3b",
                                        "_387c6bab-0a0a-4c90-9b19-73a902ab1e28",
                                        "_4da919f1-762f-4755-b674-5faccf3faec6",
                                        "_7060D0BB-B30D-4932-8FA1-40820A0FC4D0",
                                        "_30c1c7d3-284e-4455-a398-6becc3bbc419",
                                        "_c3753e40-e1c9-4900-83ff-93e50887c281",
                                        "_0a2d1460-0def-479a-9f66-a7963a5619de",
                                        "_a5edf08d-b163-4ff1-a145-bf8267fed689",
                                        "_b0a947d6-9890-4c7e-a5dd-11fce0760768",
                                        "_21e0ccb4-f0d0-43bd-bc70-06447e050e41",
                                        "_4e068301-03a3-43ee-8709-744b2f4c8158",
                                        "_6e809a5d-d7dd-4c35-882c-3f20b6da557a",
                                        "_874dae15-637c-4c9e-bee1-d859ac3acf12",
                                        "_306f6f7f-bf58-40e0-9343-62de5f7d9bce",
                                        "_5e3ded69-b21a-4850-bc90-ebe5bf7ef970",
                                        "_4db89787-187e-4855-ae11-5e10ebf69b00",
                                        "_615d912b-7ece-44e7-9bbe-d9a8d8b41e4a",
                                        "_c4b054eb-540c-44fd-9113-388d682ede70",
                                        "_ff45d777-d004-498c-8ad9-cea09c4f91d2",
                                        "_ABF53597-A808-422A-B7EE-552F24D83A5F",
                                        "_7cdb4378-79d9-4b6b-96c1-f3b55cbbc40d",
                                        "_7d0172fb-0d05-4d30-bb80-4cb3619271f4",
                                        "_f6662bb7-67f0-452f-ab3a-e430723626e1",
                                        "_def62366-746e-4fcb-b3ee-ebebb90d72d4",
                                        "_df6e0f8d-1af3-49f2-803b-454c93b19773",
                                        "_e87a1d11-7eaf-4535-9745-1e1a8e6b8e11",
                                        "_ABF53597-A808-422A-B7EE-552F24D83A5F",
                                        "_45395C84-F20A-4F5A-977F-B80348256421",
                                        "_17A934C7-1510-481F-BAD7-189058957FF1",
                                        "_5105857b-b776-4824-99fa-a324fac89dec",
                                        "_e4712e37-525d-43f4-b880-d126a4d9c603",
                                        "_aeb839c8-9228-4fff-a538-d2699191aa2b",
                                        "_bcdf5a28-bce3-46e6-91a2-8eb3781605eb",
                                        "_d054a67b-8e35-4b2a-bd32-6cbfbde656a6",
                                        "_502fa582-ba5f-496f-882a-260d909a9b9f",
                                        "_198ea415-1a31-4d0e-b31d-950e31a1346a",
                                        "_53cfe1f2-0064-46d6-bc8a-54c08992ec95",
                                        "_67214379-2364-4d28-9025-10eb7a90cff4",
                                        "_b59a587c-fd11-41ad-9172-f83d78d54ac3",
                                        "_d11aff18-688e-45f0-82c2-a277fa1b97c0",
                                        "_14aae74c-674a-4d1e-a911-4779136ff0ba",
                                        "_17A934C7-1510-481F-BAD7-189058957FF1",
                                        "_3ad2ed0c-59fd-4663-a2cf-0b8e08c40061",
                                        "_ee47f9b3-eb23-4134-9d66-63055155dc27",
                                        "_3dbf1b7a-905f-41de-8ab2-e5451623e69e",
                                        "_628087e8-502d-444f-a014-fb11514fa82c",
                                        "_95407ba3-6edf-43ec-b6c1-e3283b916f63",
                                        "_e55a4c7a-c006-4596-b658-e23bc771b5cb",
                                        "_c462ff83-15a8-4e0d-9708-f64f41a6a8ce",
                                        "_3ff8a15e-f522-47bc-9ca4-0e06c3d58ef0",
                                        "_5332bdb4-b316-4166-a37f-8531db278687",
                                        "_25b08cbe-ee08-4787-bb32-3e87c660b679",
                                        "_a19c2246-4854-45e4-be1e-0169686dfe65",
                                        "_4c491539-dfc1-4fda-9841-3bf10348e2fa",
                                        "_e92f7019-68ec-4ee5-8fc6-e66580f24794",
                                        "_D34B0D01-B082-4081-A3CC-B68B9B8313A4",
                                        "_4C04F838-62AA-475E-AEFA-A63B7C889C13",
                                        "_45395C84-F20A-4F5A-977F-B80348256421",
                                        "_4812ecc5-53dd-4f8e-8375-74ee2c2b3edd",
                                        "_70cb7d70-edc3-4223-a9c1-d99be8bc8c52",
                                        "_e77eeaf8-7c47-49f7-b932-5fc89b8b628c",
                                        "_08175e8f-b762-4c9b-92c4-07f369f69bd4",
                                        "_617f766c-5379-49e5-a036-9442f73698aa",
                                        "_ffc4a375-69d5-4c91-aa0a-54e4735d30ba",
                                        "_1f8096d5-8e7e-4292-bb96-98b5c2efefbc",
                                        "_5544e071-22c3-4c7f-b15c-98aac3edfa6f",
                                        "_7fcfa7bd-f93a-4f03-8111-43b8851cb078",
                                        "_0f5150f9-f959-4f7b-a661-d80afe862e58",
                                        "_35a3ba96-f644-4144-b955-1bc959c2311b",
                                        "_c8a56420-f87b-4ce4-ac38-ba431ecfcdb2",
                                        "_63abd794-ccfc-467d-aa2a-b99c7a0b636a",
                                        "_f3d3c954-605b-4a20-b1d9-18d69b5ca3fb",
                                        "_813c727c-973e-4185-8bcb-482d7b01eaba",
                                        "_90b9792b-e126-4aa2-832e-c99ac3702516",
                                        "_e8b9bcff-5105-4f74-8b85-adf530750445",
                                        "_0c27bd24-120f-40b2-b0dd-e7cc58e7ebc7",
                                        "_142ea530-f364-4dd9-887d-390c4aca512e",
                                        "_569f6c28-79d6-4192-a238-1294a899cee3",
                                        "_4C04F838-62AA-475E-AEFA-A63B7C889C13",
                                        "_881b2079-132d-42b6-a2e4-3d9a954199fc",
                                        "_aaa5a1e5-ddd2-4324-b1d7-0b2d1b251f32",
                                        "_c549a164-fcff-4b13-9c64-5173fb43994f",
                                        "_D34B0D01-B082-4081-A3CC-B68B9B8313A4",
                                        "_ABF877D7-DAC2-4BF0-AB58-9A8A02E92EB3",
                                        "_a4da4cea-b5b0-4f42-af2e-33ed8aa9e9dd",
                                        "_c0b0b188-ad4a-4be3-90c1-2fbb1f507a15",
                                        "_357b3424-9587-4839-8d63-e6818f43cecb",
                                        "_2f50b72c-d10f-4197-b2b9-e7268bc7c6d9",
                                        "_488bdd39-7f23-4aff-bff0-66abe4c7e2a7",
                                        "_ABF877D7-DAC2-4BF0-AB58-9A8A02E92EB3",
                                        "_6f1c625b-7fe9-4020-9ba6-4e7293c01771",
                                        "_6593c292-7c82-482f-99ab-61094ffc214a",
                                        "_7d0b45c3-8aaf-4d87-8bf7-7e9b8433b384",
                                        "_259E820F-B4AF-4E1A-8271-687534EDAECC",
                                        "_40f101aa-e9f1-45ee-ba01-f743fc956e64",
                                        "_6aba464f-3217-4e5f-b725-6b1a37aa225f",
                                        "_daaf1a85-7aad-4cb6-8fd3-13390711fdfb",
                                        "_416e0482-8b0b-4255-baf0-830e9910d377",
                                        "_7d30fc85-4e4f-40f7-82e1-04313602ddbd",
                                        "_f2560013-e260-44af-80f9-3cc218d9ef19",
                                        "_259E820F-B4AF-4E1A-8271-687534EDAECC",
                                        "_c5545620-2c8c-42ff-b59d-33cd7e02b8e5",
                                        "_dda6be90-3cd1-4a27-a691-3f95aa4e4e13",
                                        "_f3cc955e-8013-447a-848e-4c7af516cb34",
                                        "_7bbbda89-9830-472c-82bc-4e4f599369bb",
                                        "_a870a258-34be-46b8-a4de-faee32275a9a",
                                        "_bc0d2bad-2c6b-4266-8c47-b32a536288f0",
                                        "_259E820F-B4AF-4E1A-8271-687534EDAECC",
                                        "_0c48c74a-ceee-4c99-bd73-28079561ca7a",
                                        "_3c60208a-8ef8-483c-828b-30ee42d402dc",
                                        "_43f80e34-281e-4baa-8aba-d931a9a3ab87",
                                        "_40ac2899-1d2a-469f-a14a-1e14ea29d172",
                                        "_8e7f04ee-a032-4128-838e-a3442a1c3026",
                                        "_ab18a8e1-f023-4f9e-bf02-c75bf05164df",
                                        "_9f5cb9c4-71d6-4f2b-9dc1-26c7e9f84410",
                                        "_aec42b89-f3c0-47e9-b21a-82736b2a1149",
                                        "_baccfd49-ec98-4380-8be9-d242dc8611f3",
                                        "_95b3fb0f-6430-4679-a3f5-5bf37515620d",
                                        "_ca50f7c2-b14c-405a-941b-fe2acba3419a",
                                        "_f5412896-9ac0-44d9-8a67-4ab020a3f0d3"],
            "connectivity_node": ["_04984C4D-CC29-477A-9AF4-61AC7D74F16F", "_A8A25B50-3AE3-4A31-A18B-B3FA13397ED3",
                                  "_7BEDDADD-0A14-429F-8601-9EA8B892CA6E"],
            "switch_areas": [{
                "boundary_switches": ["_52DE9189-20DC-4C73-BDEE-E960FE1F9493", "_CE5D0651-676B-4AF3-8D67-41BF1B33E30C",
                                      "_43EF8365-F932-409B-A51E-FBED3F6DFFAA"],
                "addressable_equipment": ["g"],
                "unaddressable_equipment": ["_44FC5A86-A099-45B8-B847-F685C5027AFB",
                                            "_B6363F07-B1BC-420B-AA4C-A34BB8F05827",
                                            "_E2E0FC64-8D45-4C55-BDB9-EAB827A46FBC",
                                            "_7c6f94c1-1419-4582-ab2d-a0b11772c26b",
                                            "_b393e719-0981-4498-9d96-07f1be7de009",
                                            "_f11a9ad9-5b68-483b-b52f-dd4af07bb77d",
                                            "_44FC5A86-A099-45B8-B847-F685C5027AFB",
                                            "_B6363F07-B1BC-420B-AA4C-A34BB8F05827",
                                            "_E2E0FC64-8D45-4C55-BDB9-EAB827A46FBC",
                                            "_A04CDFB1-E951-4FC4-8882-0323CD70AE3C",
                                            "_44FC5A86-A099-45B8-B847-F685C5027AFB",
                                            "_B6363F07-B1BC-420B-AA4C-A34BB8F05827",
                                            "_E2E0FC64-8D45-4C55-BDB9-EAB827A46FBC",
                                            "_5ad9e784-5b6c-4f2c-bc4d-1ccc31cfd96b",
                                            "_8dc4079e-6bbb-491d-9f4c-0c240228b647",
                                            "_fc4adc62-5608-467f-aab7-75893b574998",
                                            "_5d00b173-726b-4f64-b93e-c60648276c66",
                                            "_8d72f997-ba3e-4954-91b6-62fc3304d165",
                                            "_f782d376-467f-46bc-a0f5-3f500d6570aa",
                                            "_0a2f7676-f619-405b-bb80-8f51f4d7a25f",
                                            "_9f4bef6c-c68d-42a9-ade6-206a8b365ce9",
                                            "_c16593db-3c64-4504-9387-17f19f558549",
                                            "_44FC5A86-A099-45B8-B847-F685C5027AFB",
                                            "_B6363F07-B1BC-420B-AA4C-A34BB8F05827",
                                            "_E2E0FC64-8D45-4C55-BDB9-EAB827A46FBC",
                                            "_FBE26B35-13AB-457D-9795-DF58B28E309D",
                                            "_1C6781A2-5B9D-4525-8A9B-F9B32C4C4AC0",
                                            "_A04CDFB1-E951-4FC4-8882-0323CD70AE3C",
                                            "_198ca97f-d307-4fe7-8a79-5caa1c3e45d0",
                                            "_907b4408-7271-4407-9e38-3d019dc1bc68",
                                            "_cc70103a-126e-4ec1-8583-12412dd8195d",
                                            "_27897da2-d7e1-438c-a6e4-4b3cfe8e79fa",
                                            "_d92644c9-5bd2-4312-8e31-3bec6510e646",
                                            "_dad6dd20-9bfc-4bd9-b76e-2e0fd3b0d5ba",
                                            "_7ca7c18c-3861-47bf-82cf-5a72d618b18a",
                                            "_80ef10f9-3f4f-4fd2-8262-caedf7442fda",
                                            "_cd64f70b-91d8-460b-af28-688e9709f319",
                                            "_0cbdf98b-b5e4-4bc3-93d6-08db08947794",
                                            "_0f4457a6-a3cb-42b0-a06c-b31d5c7a17ff",
                                            "_bc165aa6-347d-4551-8abf-016044675a6f",
                                            "_65599f7e-3e93-4456-a2b1-bba7a46337b6",
                                            "_6bb8ef03-ec84-421f-8d28-cd1a3813e614",
                                            "_FBE26B35-13AB-457D-9795-DF58B28E309D",
                                            "_8b6bd68f-c84d-45e1-91b9-b0406fbaa3b1",
                                            "_d56a4982-0c80-45d0-8cb8-c24097138b63",
                                            "_d638fbbc-9b85-416e-87b8-37c9785e1611",
                                            "_1C6781A2-5B9D-4525-8A9B-F9B32C4C4AC0",
                                            "_0BBD0EA3-F665-465B-86FD-FC8B8466AD53",
                                            "_c7c58261-4885-46ee-beb9-c94c6c29451f",
                                            "_98a81464-d7b6-4044-9b48-a92e179884dc",
                                            "_d8ea43c7-2107-4975-9ddb-4279628daf18",
                                            "_2d9ed148-d492-4e7d-b9af-81a407e74a59",
                                            "_4e30ae83-418c-4cfb-99eb-5572e00b4ec4",
                                            "_d23fd30b-e3f9-4a43-b3c4-2f2697dba851",
                                            "_0BBD0EA3-F665-465B-86FD-FC8B8466AD53",
                                            "_7a436400-3a77-4eaf-bb04-ef7954fcbdd9",
                                            "_5f1dfa9f-e754-471d-9c74-c1a9441e95a3",
                                            "_84f75532-a514-4355-bf0e-2f8d82c736ae",
                                            "_e1b4fd36-01d0-4d7d-9223-2279911fe8c3"],
                "connectivity_node": ["brkr", "rg60", "632", "633", "645", "646"],
                "secondary_areas": []
            }, {
                "boundary_switches": ["_43EF8365-F932-409B-A51E-FBED3F6DFFAA"],
                "addressable_equipment": [],
                "unaddressable_equipment": ["_1E6B5C97-C4E8-4CED-B9A5-6E69F389DA93",
                                            "_5500424b-9931-4f09-a22b-d24a47517920",
                                            "_bd95505f-3f55-43d2-b8b2-2c97b2c86603",
                                            "_f3001cb9-4c00-45ab-a73f-537be73f583c",
                                            "_37fc9b9a-0bc9-4417-8214-52afc237735f",
                                            "_697532b4-9520-4de4-80e9-2b6a77c8a089",
                                            "_d9e22ddd-f4f2-426c-911d-cf08ff5cc9a0",
                                            "_1E6B5C97-C4E8-4CED-B9A5-6E69F389DA93",
                                            "_5ae00771-adeb-4ee2-92a3-7c991c579ce1",
                                            "_77cf5e05-b332-4203-937a-53f58b4f4585",
                                            "_247f50ee-6bc5-4588-bdf1-9b480e09840e",
                                            "_5842f2db-ad93-494a-a372-c8e83e637147",
                                            "_87c273f2-8e55-4169-adeb-2df020776c06",
                                            "_919d79f9-9719-492b-bf8b-46cffc7579ad",
                                            "_9d580686-9c5d-42a6-9e0b-ef08c7d80256",
                                            "_ab19de32-3fad-4654-b546-6b785b2d65e3",
                                            "_51037d29-941b-4e9f-ae86-99dd37bb2c9d",
                                            "_54e2019e-e234-4dbb-85d6-227b245040ae",
                                            "_48720b2c-7908-4f18-a80d-f7f7f4099753",
                                            "_683bbf2f-7ea6-45c6-805e-5e4b7f5000a2",
                                            "_0ab88ca4-fb60-4a67-8f77-5f15af245b64",
                                            "_25938754-4fe8-4621-9414-7d519bc9fde3",
                                            "_78116a30-9d83-4715-a9d2-dda61687a0b9",
                                            "_7cc37959-2a82-4911-8a23-8ad09378c85c",
                                            "_cd76b30b-8e1c-45fb-b03a-79847254ead8",
                                            "_d057e1e2-71ad-4293-b89e-e9e9e84a2522",
                                            "_f0af2090-d2aa-40fb-8878-45d75c4ae59f",
                                            "_07b694ae-bde0-431c-a740-362a9f476949",
                                            "_c3a9b1e7-7a52-4fa5-a199-1fd6035abc21",
                                            "_d2d52e14-2111-486e-a59a-d8c5b5f7bf92"],
                "connectivity_node": ["xf1"],
                "secondary_areas": [{
                    "distribution_transformer": ["_1E6B5C97-C4E8-4CED-B9A5-6E69F389DA93"],
                    "addressable_equipment": ["_D2E930A7-B136-4ACA-A996-8DB5C60AADF3",
                                              "_7B671984-4C56-4FF1-9733-B4B6FCA5F2AA",
                                              "_B21C5599-1D00-4FCF-904B-58D9D4CAC49A",
                                              "_C39149DE-3451-4D33-B4C2-B1E6C6FC9AAB",
                                              "_3B2021A7-4BFC-418D-9C20-BD6838E52CF8"],
                    "unaddressable_equipment": ["_5ae00771-adeb-4ee2-92a3-7c991c579ce1",
                                                "_77cf5e05-b332-4203-937a-53f58b4f4585",
                                                "_247f50ee-6bc5-4588-bdf1-9b480e09840e",
                                                "_5842f2db-ad93-494a-a372-c8e83e637147",
                                                "_87c273f2-8e55-4169-adeb-2df020776c06",
                                                "_919d79f9-9719-492b-bf8b-46cffc7579ad",
                                                "_9d580686-9c5d-42a6-9e0b-ef08c7d80256",
                                                "_ab19de32-3fad-4654-b546-6b785b2d65e3",
                                                "_51037d29-941b-4e9f-ae86-99dd37bb2c9d",
                                                "_54e2019e-e234-4dbb-85d6-227b245040ae",
                                                "_48720b2c-7908-4f18-a80d-f7f7f4099753",
                                                "_683bbf2f-7ea6-45c6-805e-5e4b7f5000a2",
                                                "_0ab88ca4-fb60-4a67-8f77-5f15af245b64",
                                                "_25938754-4fe8-4621-9414-7d519bc9fde3",
                                                "_78116a30-9d83-4715-a9d2-dda61687a0b9",
                                                "_7cc37959-2a82-4911-8a23-8ad09378c85c",
                                                "_cd76b30b-8e1c-45fb-b03a-79847254ead8",
                                                "_d057e1e2-71ad-4293-b89e-e9e9e84a2522",
                                                "_f0af2090-d2aa-40fb-8878-45d75c4ae59f",
                                                "_07b694ae-bde0-431c-a740-362a9f476949",
                                                "_c3a9b1e7-7a52-4fa5-a199-1fd6035abc21",
                                                "_d2d52e14-2111-486e-a59a-d8c5b5f7bf92"],
                    "connectivity_node": ["_0DCC57AF-F4FA-457D-BB24-2EFDA9865A1A"]
                }]
            }, {
                "boundary_switches": ["_2858B6C2-0886-4269-884C-06FA8B887319"],
                "addressable_equipment": ["_9D725810-BFD6-44C6-961A-2BC027F6FC95"],
                "unaddressable_equipment": ["_8E180773-2A9B-4136-BC9A-132A52C8E276",
                                            "_0fe87976-0177-42f3-817b-b468225220b2",
                                            "_2d31c620-a2f9-4f84-9102-9a8fe574ab6b",
                                            "_8E180773-2A9B-4136-BC9A-132A52C8E276",
                                            "_fad827c5-f344-498e-ab39-29883d4c6bb6",
                                            "_7a84c113-d427-4802-a769-b6edc48451c7",
                                            "_162b4555-f748-4829-8e71-bbbecf4e4bcb",
                                            "_eb606875-f620-4c4e-b559-cd587ba0ecf8",
                                            "_6c08f0e8-eb6f-4261-a3f6-3aa9d1e99c75"],
                "connectivity_node": ["tap", "611"],
                "secondary_areas": []
            }, {
                "boundary_switches": ["_517413CB-6977-46FA-8911-C82332E42884"],
                "addressable_equipment": ["_A9DE8829-58CB-4750-B2A2-672846A89753"],
                "unaddressable_equipment": ["_7060D0BB-B30D-4932-8FA1-40820A0FC4D0",
                                            "_3e3bdc6c-d985-4659-9cb7-82ea8212ba4f",
                                            "_59c9a186-c0a8-4f85-a524-d6ef0d27700a",
                                            "_5c9a17db-6f03-4626-9464-41d3a5ddeb15",
                                            "_d3a28545-dbfd-4cc4-9f3a-52e2ff130d93",
                                            "_8007b83e-40fa-4e87-9df7-a1097dc3b3e7",
                                            "_2abd660f-3dc2-4611-95a0-9adebae7fe3b",
                                            "_387c6bab-0a0a-4c90-9b19-73a902ab1e28",
                                            "_4da919f1-762f-4755-b674-5faccf3faec6",
                                            "_7060D0BB-B30D-4932-8FA1-40820A0FC4D0",
                                            "_30c1c7d3-284e-4455-a398-6becc3bbc419",
                                            "_c3753e40-e1c9-4900-83ff-93e50887c281",
                                            "_0a2d1460-0def-479a-9f66-a7963a5619de",
                                            "_a5edf08d-b163-4ff1-a145-bf8267fed689",
                                            "_b0a947d6-9890-4c7e-a5dd-11fce0760768",
                                            "_21e0ccb4-f0d0-43bd-bc70-06447e050e41",
                                            "_4e068301-03a3-43ee-8709-744b2f4c8158",
                                            "_6e809a5d-d7dd-4c35-882c-3f20b6da557a",
                                            "_874dae15-637c-4c9e-bee1-d859ac3acf12",
                                            "_306f6f7f-bf58-40e0-9343-62de5f7d9bce",
                                            "_5e3ded69-b21a-4850-bc90-ebe5bf7ef970",
                                            "_4db89787-187e-4855-ae11-5e10ebf69b00",
                                            "_615d912b-7ece-44e7-9bbe-d9a8d8b41e4a",
                                            "_c4b054eb-540c-44fd-9113-388d682ede70",
                                            "_ff45d777-d004-498c-8ad9-cea09c4f91d2"],
                "connectivity_node": ["692", "675"],
                "secondary_areas": []
            }, {
                "boundary_switches": ["_CE5D0651-676B-4AF3-8D67-41BF1B33E30C", "_517413CB-6977-46FA-8911-C82332E42884",
                                      "_2858B6C2-0886-4269-884C-06FA8B887319"],
                "addressable_equipment": [],
                "unaddressable_equipment": ["_ABF53597-A808-422A-B7EE-552F24D83A5F",
                                            "_7cdb4378-79d9-4b6b-96c1-f3b55cbbc40d",
                                            "_7d0172fb-0d05-4d30-bb80-4cb3619271f4",
                                            "_f6662bb7-67f0-452f-ab3a-e430723626e1",
                                            "_def62366-746e-4fcb-b3ee-ebebb90d72d4",
                                            "_df6e0f8d-1af3-49f2-803b-454c93b19773",
                                            "_e87a1d11-7eaf-4535-9745-1e1a8e6b8e11",
                                            "_ABF53597-A808-422A-B7EE-552F24D83A5F",
                                            "_45395C84-F20A-4F5A-977F-B80348256421",
                                            "_17A934C7-1510-481F-BAD7-189058957FF1",
                                            "_5105857b-b776-4824-99fa-a324fac89dec",
                                            "_e4712e37-525d-43f4-b880-d126a4d9c603",
                                            "_aeb839c8-9228-4fff-a538-d2699191aa2b",
                                            "_bcdf5a28-bce3-46e6-91a2-8eb3781605eb",
                                            "_d054a67b-8e35-4b2a-bd32-6cbfbde656a6",
                                            "_502fa582-ba5f-496f-882a-260d909a9b9f",
                                            "_198ea415-1a31-4d0e-b31d-950e31a1346a",
                                            "_53cfe1f2-0064-46d6-bc8a-54c08992ec95",
                                            "_67214379-2364-4d28-9025-10eb7a90cff4",
                                            "_b59a587c-fd11-41ad-9172-f83d78d54ac3",
                                            "_d11aff18-688e-45f0-82c2-a277fa1b97c0",
                                            "_14aae74c-674a-4d1e-a911-4779136ff0ba",
                                            "_17A934C7-1510-481F-BAD7-189058957FF1",
                                            "_3ad2ed0c-59fd-4663-a2cf-0b8e08c40061",
                                            "_ee47f9b3-eb23-4134-9d66-63055155dc27",
                                            "_3dbf1b7a-905f-41de-8ab2-e5451623e69e",
                                            "_628087e8-502d-444f-a014-fb11514fa82c",
                                            "_95407ba3-6edf-43ec-b6c1-e3283b916f63",
                                            "_e55a4c7a-c006-4596-b658-e23bc771b5cb",
                                            "_c462ff83-15a8-4e0d-9708-f64f41a6a8ce",
                                            "_3ff8a15e-f522-47bc-9ca4-0e06c3d58ef0",
                                            "_5332bdb4-b316-4166-a37f-8531db278687",
                                            "_25b08cbe-ee08-4787-bb32-3e87c660b679",
                                            "_a19c2246-4854-45e4-be1e-0169686dfe65",
                                            "_4c491539-dfc1-4fda-9841-3bf10348e2fa",
                                            "_e92f7019-68ec-4ee5-8fc6-e66580f24794",
                                            "_D34B0D01-B082-4081-A3CC-B68B9B8313A4",
                                            "_4C04F838-62AA-475E-AEFA-A63B7C889C13",
                                            "_45395C84-F20A-4F5A-977F-B80348256421",
                                            "_4812ecc5-53dd-4f8e-8375-74ee2c2b3edd",
                                            "_70cb7d70-edc3-4223-a9c1-d99be8bc8c52",
                                            "_e77eeaf8-7c47-49f7-b932-5fc89b8b628c",
                                            "_08175e8f-b762-4c9b-92c4-07f369f69bd4",
                                            "_617f766c-5379-49e5-a036-9442f73698aa",
                                            "_ffc4a375-69d5-4c91-aa0a-54e4735d30ba",
                                            "_1f8096d5-8e7e-4292-bb96-98b5c2efefbc",
                                            "_5544e071-22c3-4c7f-b15c-98aac3edfa6f",
                                            "_7fcfa7bd-f93a-4f03-8111-43b8851cb078",
                                            "_0f5150f9-f959-4f7b-a661-d80afe862e58",
                                            "_35a3ba96-f644-4144-b955-1bc959c2311b",
                                            "_c8a56420-f87b-4ce4-ac38-ba431ecfcdb2",
                                            "_63abd794-ccfc-467d-aa2a-b99c7a0b636a",
                                            "_f3d3c954-605b-4a20-b1d9-18d69b5ca3fb",
                                            "_813c727c-973e-4185-8bcb-482d7b01eaba",
                                            "_90b9792b-e126-4aa2-832e-c99ac3702516",
                                            "_e8b9bcff-5105-4f74-8b85-adf530750445",
                                            "_0c27bd24-120f-40b2-b0dd-e7cc58e7ebc7",
                                            "_142ea530-f364-4dd9-887d-390c4aca512e",
                                            "_569f6c28-79d6-4192-a238-1294a899cee3",
                                            "_4C04F838-62AA-475E-AEFA-A63B7C889C13",
                                            "_881b2079-132d-42b6-a2e4-3d9a954199fc",
                                            "_aaa5a1e5-ddd2-4324-b1d7-0b2d1b251f32",
                                            "_c549a164-fcff-4b13-9c64-5173fb43994f",
                                            "_D34B0D01-B082-4081-A3CC-B68B9B8313A4",
                                            "_ABF877D7-DAC2-4BF0-AB58-9A8A02E92EB3",
                                            "_a4da4cea-b5b0-4f42-af2e-33ed8aa9e9dd",
                                            "_c0b0b188-ad4a-4be3-90c1-2fbb1f507a15",
                                            "_357b3424-9587-4839-8d63-e6818f43cecb",
                                            "_2f50b72c-d10f-4197-b2b9-e7268bc7c6d9",
                                            "_488bdd39-7f23-4aff-bff0-66abe4c7e2a7",
                                            "_ABF877D7-DAC2-4BF0-AB58-9A8A02E92EB3",
                                            "_6f1c625b-7fe9-4020-9ba6-4e7293c01771",
                                            "_6593c292-7c82-482f-99ab-61094ffc214a",
                                            "_7d0b45c3-8aaf-4d87-8bf7-7e9b8433b384"],
                "connectivity_node": ["mid", "670", "671", "680", "684", "652"],
                "secondary_areas": [{
                    "distribution_transformer": ["_17A934C7-1510-481F-BAD7-189058957FF1"],
                    "addressable_equipment": ["_CEC0FC3A-0FD1-4F1C-9C51-7D9BEF4D8222",
                                              "_682AB7A9-4FBF-4204-BDE1-27EAB3425DA0",
                                              "_32F02D2B-EE6E-4D3F-8486-1B5CAEF70204"],
                    "unaddressable_equipment": ["_3ad2ed0c-59fd-4663-a2cf-0b8e08c40061",
                                                "_ee47f9b3-eb23-4134-9d66-63055155dc27",
                                                "_3dbf1b7a-905f-41de-8ab2-e5451623e69e",
                                                "_628087e8-502d-444f-a014-fb11514fa82c",
                                                "_95407ba3-6edf-43ec-b6c1-e3283b916f63",
                                                "_e55a4c7a-c006-4596-b658-e23bc771b5cb",
                                                "_c462ff83-15a8-4e0d-9708-f64f41a6a8ce",
                                                "_3ff8a15e-f522-47bc-9ca4-0e06c3d58ef0",
                                                "_5332bdb4-b316-4166-a37f-8531db278687",
                                                "_25b08cbe-ee08-4787-bb32-3e87c660b679",
                                                "_a19c2246-4854-45e4-be1e-0169686dfe65",
                                                "_4c491539-dfc1-4fda-9841-3bf10348e2fa",
                                                "_e92f7019-68ec-4ee5-8fc6-e66580f24794"],
                    "connectivity_node": ["_0A98A62D-7642-4F03-8317-A8605CBDBA37"]
                }]
            }]
        }
    }


if __name__ == '__main__':
    # Get topology processor switch delimited area
    # gridapps = GridAPPSD()
    # topic = "goss.gridappsd.request.data.topology"
    #
    # message = {
    #    "requestType": "GET_SWITCH_AREAS",
    #    "modelID":  "_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62",
    #    "resultFormat": "JSON"
    # }
    #
    # switch_areas_response = gapps.get_response(topic, message, timeout=30)
    topo_response = get_topo_response()

    switch_areas_response: List[Dict] = [x for x in topo_response["feeders"]["switch_areas"]]
    areas = []
    for switch_area in switch_areas_response:
        areas.append(SwitchArea.load_from_topo_response(switch_area,
                                                        BlazeGraphConnection("http://localhost:8889/bigdata/namespace/kb/sparql",
                                                                             feeder_mrid="_EE71F6C9-56F0-4167-A14E-7F4C71F10EAA")))

    for index, a in enumerate(areas):
        print(f"# compensator in area {index}? {len(a.get_by_type(LinearShuntCompensator))}")
        for c in a.get_by_type(LinearShuntCompensator):
            pprint(c.__dict__)

        for c in a.get_by_type(Terminal):
            pprint(c.__dict__)

        for c in a.get_by_type(TransformerTank):
            pprint(c.__dict__)

# from dataclasses import field, dataclass
#
# @dataclass
# class Model:
#     feeder: Feeder
#     catalog: Dict[str, object] = field(default_factory=dict)
#     typed_catalog: Dict[Type, List[object]] = field(default_factory=dict)
#
#     def add_to_catalog(mrid, obj):
#         if mrid in self.catalog:
#             raise AlreadyExists()
#         self.catalog[mrid] = obj
#         if type(obj) in self.typed_catalog:
#             self.typed_catalog[type(obj)].append(obj)
#     def get_terminals() -> List[Terminal]:
#         return self.typed_catalog[Terminal]
#     def get_object(self, mrid) -> object:
#         return self.catalog[mrid]
#
#
#
# feeder = Model(f)
# feeder.add_to_catalog(t.mRID, t)

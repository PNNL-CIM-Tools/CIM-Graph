from __future__ import annotations

from typing import Dict, List, Optional

from SPARQLWrapper import SPARQLWrapper, JSON

from cim.loaders import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
import cim.data_profile as cim


def query_string_parser(obj_dict: Dict, mRID: str, query: List, key: str):
    try:
        setattr(obj_dict[mRID], key, query[key]['value'])
    except:
        []


def query_class_parser(obj_dict: Dict, mRID: str, query: List, class_name: str):
    try:
        cls = class_name
        setattr(obj_dict[mRID], class_name, eval(f"{cls}(mRID='{query[class_name]['value']}')"))
    except:
        []


def query_list_parser(obj_dict: Dict, mRID: str, query: List, key, separator):
    # print(query[key]['value'].split(separator))
    try:
        setattr(obj_dict[mRID], key, query[key]['value'].split(separator))
    except:
        []


class BlazegraphConnection(ConnectionInterface):
    sparql: Optional[SPARQLWrapper] = None

    def connect(self):
        if not self.sparql:
            url = self.connection_params.parameters[0].value
            self.sparql = SPARQLWrapper(url)
            self.sparql.setReturnFormat(JSON)

    def disconnect(self):
        self.sparql = None

    def load_attributes(self, obj: object):
        if isinstance(obj, cim.Terminal):
            # load terminal stuff here
            pass

    def create_default_instances(self, feeder_mrid: str | cim.Feeder, mrid_list: List[str]) -> List[object]:
        """ Creates an empty CIM object with the correct class type with mRID and name fields populated

            @param: feeder_id: str:

            """
        """Example function with types documented in the docstring.
        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:
        Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter.
        Returns:
            bool: The return value. True for success, False otherwise.
        .. _PEP 484:
            https://www.python.org/dev/peps/pep-0484/
        """

        query_message = """
                    PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX c:  <http://iec.ch/TC57/CIM100#>
                    SELECT ?eqid ?eqname ?class
                    {
                      VALUES ?fdrid {"%s"}
                      VALUES ?eqid {""" % feeder_mrid
        for mrid in mrid_list:
            query_message += ' "%s" \n' % mrid

        query_message += """               } 
                      ?fdr c:IdentifiedObject.mRID ?fdrid.
                      ?eq c:IdentifiedObject.name ?eqname.
                      ?eq c:IdentifiedObject.mRID ?eqid.
                      ?eq a ?classraw.
                      bind(strafter(str(?classraw),"CIM100#") as ?class)
                    }
                    GROUP BY  ?eqid ?eqname ?class
                    ORDER by  ?fdrid
                    """
        # print(query_message)
        #         results = gapps.query_data(query = query_message, timeout = 60)
        #         output = results['data']['results']['bindings']
        self.connect()
        self.sparql.setQuery(query_message)

        output = self.sparql.query().convert()
        #         print(output)

        objects = []
        for result in output['results']['bindings']:
            print(result)
            cls = result['class']['value']
            mrid = result['eqid']['value']
            try:
                objects.append(eval(f"cim.{cls}(mRID='{mrid}')"))
                print(cls)
            except:
                print('warning: object class missing:', cls)
        return objects

    def execute(self, query: str) -> QueryResponse:
        raise RuntimeError("Must have implemented query in the inherited class")

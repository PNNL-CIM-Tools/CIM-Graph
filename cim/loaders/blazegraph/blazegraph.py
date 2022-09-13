from __future__ import annotations

from typing import Dict, List, Optional

from SPARQLWrapper import SPARQLWrapper, JSON, POST

from cim.loaders import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
from cim.models import add_to_catalog, add_to_typed_catalog
import cim.data_profile as cim
import cim.loaders.blazegraph as blazegraph


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
        self.sparql.setMethod(POST)

        output = self.sparql.query().convert()
        #         print(output)

        objects = []
        for result in output['results']['bindings']:
           # print(result)
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
        
    def get_all_attributes(typed_catalog, cim_class):
        if isinstance(cim_class, cim.ACLineSegment):
            pass
        elif isinstance(cim_class, cim.LinearShuntCompensator):
            
        

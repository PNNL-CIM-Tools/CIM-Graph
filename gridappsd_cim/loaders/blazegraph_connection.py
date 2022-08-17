
from gridappsd_cim import *



@dataclass
class BlazeGraphConnection(Connection):
    url: str
    feeder_mrid: str = None
    sparql: SPARQLWrapper = None

    def load_attributes(self, obj: object):
        if isinstance(obj, LinearShuntCompensator):
            # load all attributes onto obj from a custom query for specific compensator
            setattr(obj, "b0PerSection", 5)

    def retrieve_instance(self, mrid: str, feeder_mrid: str = None) -> object:
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
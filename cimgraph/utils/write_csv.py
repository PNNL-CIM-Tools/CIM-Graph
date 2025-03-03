from __future__ import annotations

import logging
import os
from zipfile import ZIP_DEFLATED, ZipFile

from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def write_csv(network: GraphModel, destination: str) -> None:

    try:
        os.remove(f'{destination}/{network.container.mRID}.zip')
    except:
        pass

    for cim_class in list(network.graph.keys()):
        attributes = list(cim_class.__dataclass_fields__.keys())

        with open(f'{cim_class.__name__}.csv', 'w') as csv_file:
            header = ','.join(attributes)
            csv_file.write(f'{header}\n')

        with open(f'{cim_class.__name__}.csv', 'a') as csv_file:
            # Get JSON-LD representation of model
            table = network.__dumps__(cim_class, show_empty=True, json_ld=True)
            fields = cim_class.__dataclass_fields__
            # Insert each power system object in CIMantic Graphs model
            for obj in table.values():
                # Create SQL Query
                row = []
                # sql_params = [self.username, int(time.time())]

                # Iterate through each attribute
                for attr in list(obj.keys()):

                    if 'List' in fields[attr].type:
                        row.append(f'"{obj[attr]}"')    # JSON-LD List of RDF links
                    elif 'float' in fields[attr].type:
                        row.append(obj[attr])    # float
                    else:
                        row.append(f'"{obj[attr]}"')    # free text
                csv_row = ','.join(row)
                csv_file.write(f'{csv_row}\n')

        with ZipFile(f'{destination}/{network.container.mRID}.zip', 'a', ZIP_DEFLATED) as zip_file:
            zip_file.write(f'{cim_class.__name__}.csv')
            os.remove(f'{cim_class.__name__}.csv')

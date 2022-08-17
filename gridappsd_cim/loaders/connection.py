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


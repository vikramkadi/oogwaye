
class DataPull:
    def __init__(self, status, message, data, facts=[], dimensions=[]):
        self.status=status
        self.message=message
        self.data=data
        self.facts=facts
        self.dimensions=dimensions

class ColumnMetadata:
    def __init__(self, colname, index):
        self.colname=colname
        self.index=index

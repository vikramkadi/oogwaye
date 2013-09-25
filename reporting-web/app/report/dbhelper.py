from app.report import datasources
from app.report import models
from sqlalchemy import types

def pull_from_db(db_id, sql):
    status = 0
    engine = datasources.lookup_engine(db_id)
    if not engine:
        return models.DataPull(-1, "Database has not been configured right", None)

    conn = engine.connect()
    result = conn.execute(sql)
    result_metadata = result._cursor_description()
    column_count = len(result_metadata)
    facts, dimensions = derive_facts_dimensions(result_metadata)
    data = []
    for row in result:
        datarow = []
        for col in range(column_count):
            datarow.append(row[col])
        data.append(datarow)
    
    conn.close()
    return models.DataPull(0, "success", data, facts, dimensions) 

def derive_facts_dimensions(rsmd):
    facts = []
    dimensions = []
    for i, colinfo in enumerate(rsmd):
        colname=colinfo[0]
        coltype=colinfo[1]
        if coltype == 3:
            dimensions.append(models.ColumnMetadata(colname, i, 'integer'))
        elif coltype == 253:
            facts.append(models.ColumnMetadata(colname, i, 'string'))
        elif coltype == None:
            facts.append(models.ColumnMetadata(colname, i, 'string'))
       
    return facts, dimensions 

import sqlalchemy
import pandas as pd
import urllib

from ScriptorQL.script import df_to_SQL_insert

# Variables
server = '.\\sql2016'
database = 'DWH_Model_old'
schemaname = 'dbo'
tablename = 'ProjectAuth'
driver = 'SQL Server Native Client 11.0'

params = urllib.parse.quote_plus("DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes"
                                 .format(driver=driver,
                                         server=server,
                                         database=database))
engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

query = '''
    SELECT top 10 *
    FROM {schemaname}.{tablename};
'''.format(database=database, schemaname=schemaname, tablename=tablename)

# Reading query to df
df = pd.read_sql(query, engine)

print(df_to_SQL_insert(df, table="ProjectAuth"))

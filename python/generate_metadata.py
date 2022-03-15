from config import gsproperty as conf
# import pyodbc


def getClob_and_Blobs():
   query  = """
with TablDataType as(
select
    t.table_name  table_name, 
       c.COLUMN_NAME COLUMN_NAME,
       c.data_type data_type
from information_schema.columns c
    inner join INFORMATION_SCHEMA.tables t
        on c.TABLE_SCHEMA = t.TABLE_SCHEMA
        and c.TABLE_NAME = t.TABLE_NAME
where t.TABLE_TYPE = 'BASE TABLE' 
and t.TABLE_CATALOG='ELCM' and t.TABLE_TYPE!='VIEW'
and ((c.data_type in ('VARCHAR', 'NVARCHAR') and c.character_maximum_length = -1)
or c.data_type in ('TEXT', 'NTEXT', 'IMAGE', 'VARBINARY', 'XML', 'FILESTREAM', 'DATETIME', 'DATETIME','SMALL DATETIME'))
) 
SELECT tab.table_name
     ,''''+ STUFF((
       SELECT '=String,' + t1.COLUMN_NAME
         FROM TablDataType t1
        WHERE tab.table_name = t1.table_name
        ORDER BY t1.COLUMN_NAME
          FOR XML PATH('')), 1, LEN('=String,'), '') +'=String' +'''' AS hive_columns
  FROM TablDataType tab
GROUP BY tab.table_name
ORDER BY tab.table_name;
"""
   print(query)
    connection = pyodbc.connect( 'DRIVER=' + conf.driver + ';SERVER=' + conf.server +
                                                   ';DATABASE=' + conf.database + ';UID=' + conf.sql_user +
                                                   ';PWD=' + conf.sql_password)
    cursor = connection.cursor()


def genMetaData(inputfile, outputfile, tab):

    with open(inputfile, "r") as infile:
        with open(outputfile, "w") as outfile:
            lines = infile.readline()
            while lines:
                print(tab[lines.strip()])
                outfile.write("{0}\n".format(tab[lines.strip()]))
                lines = infile.readline()


__name__ = "__main__"

inputfile = 'C:\\Users\\amirr\\PycharmProjects\\pythontraining\\python\\hello_file.txt'
outputfile = 'C:\\Users\\amirr\\PycharmProjects\\pythontraining\\python\\hello_file1.txt'
#genMetaData(inputfile, outputfile, getClob_and_Blobs())
getClob_and_Blobs()
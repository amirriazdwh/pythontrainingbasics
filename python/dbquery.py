import pyodbc

clob_blob_query = """
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


class DBquery:
    def __init__(self, driver, server, database, sql_user, sql_password):
        self.driver = driver
        self.server = server
        self.database = database
        self.sql_user = sql_user
        self.sql_password = sql_password

    def connect(self):
        connection = pyodbc.connect('DRIVER=' + self.driver + ';SERVER=' + self.server +
                                    ';DATABASE=' + self.database + ';UID=' + self.sql_user +
                                    ';PWD=' + self.sql_password)
        return connection.cursor()

    def dbclose(self, cursor):
        cursor.close()



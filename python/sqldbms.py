import pyodbc

# retrive data types needs conversion
qr_clob_blob = """
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

# retrive tables to be loaded 
qr_table = """
	select table_name  from INFORMATION_SCHEMA.tables t
	where t.TABLE_TYPE = 'BASE TABLE' 
	and t.TABLE_CATALOG='ELCM' and t.TABLE_TYPE!='VIEW'"""

ins_query = """
INSERT  INTO dlingestionuat.tbljobconfig ( batch_id,src_schema, src_obj_name,dest_schema,dest_obj_name,primary_key, fetch_size,hive_mapping, java_mapping,select_columns, incremental_key,
        fields_terminated_by, file_formats,compression_type,mappers,split_by_key,where_clause,query,pre_run_script,post_run_script,load_priority, additional_arguments,import_export )
         values({0},'{1}','{2}','{3}','{4}',{5},{6},'{7}','{8}',{9},{10},'{11}','{12}','{13}',{14},{15},
        {16},{17},'{18}',{19},{20},{21},'{22}' );\n"""


class MssqlDB:
    def __init__(self, driver, server, database, sql_user, sql_password):
        self.connection = None
        self.dbcursor = None
        self.driver = driver
        self.server = server
        self.database = database
        self.sql_user = sql_user
        self.sql_password = sql_password

    def __enter__(self):
        self.connection = pyodbc.connect('DRIVER=' + self.driver + ';SERVER=' + self.server +
                                         ';DATABASE=' + self.database + ';UID=' + self.sql_user +
                                         ';PWD=' + self.sql_password)
        self.dbcursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.dbcursor.close()

    def load_data_by_query(self, query, rtype):
        if rtype == 'D':
            print("creating dictionary from rows...")
            rs_clob_blob = self.dbcursor.execute(query).fetchall()
            rs_table = {getattr(row, 'table_name').replace('\n', ' '): getattr(row, 'hive_columns').replace('\n', ' ')
                        for
                        row
                        in rs_clob_blob}
            return rs_table
        else:
            print("creating list from rows...")
            rs_tab_list = self.dbcursor.execute(query).fetchall()
            rs_table = [getattr(row, 'table_name').replace('\n', ' ') for row in rs_tab_list]
            return rs_table

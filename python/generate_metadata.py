import dbquery
from config import gsproperty as conf

rs_sqldb = dbquery.DBquery(conf.driver, conf.server, conf.database, conf.sql_user, conf.sql_password)
rs_cursor =  rs_sqldb.connect()
rs_clob_blob = rs_cursor.execute(dbquery.clob_blob_query).fetchall()
rs_table = {getattr(row, 'table_name').replace('\n', ' '): getattr(row, 'hive_columns').replace('\n', ' ') for row in
            rs_clob_blob}

print("table:{0} columns:{1}".format('EL_CFPM_TR_TERMS_CONDITIONS',rs_table['EL_CFPM_TR_TERMS_CONDITIONS']))
rs_sqldb.dbclose(rs_cursor)


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
# genMetaData(inputfile, outputfile, getClob_and_Blobs())
#getClob_and_Blobs()

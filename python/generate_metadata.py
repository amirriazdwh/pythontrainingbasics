import dbquery

from config import gsproperty as conf

rs_cursor = dbquery.DBquery(conf.driver, conf.server, conf.database, conf.sql_user, conf.sql_password).connect()
rs_clob_blob = rs_cursor.execute(dbquery.clob_blob_query)
print(rs_clob_blob)

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

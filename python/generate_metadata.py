from sqldbms import MssqlDB, qr_clob_blob
from config import gsproperty as conf


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

with MssqlDB(conf.driver, conf.server, conf.database, conf.sql_user, conf.sql_password) as db:
    rs_table = db.get_clob_blob_table(qr_clob_blob,'D')
    for x, y in rs_table.items():
        print(x, y )
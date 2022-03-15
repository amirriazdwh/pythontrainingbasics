from sqldbms import MssqlDB, qr_clob_blob, qr_table
from config import gsproperty as conf

__name__ = "__main__"

genfile = 'C:\\Users\\amirr\\PycharmProjects\\pythontraining\\python\\hello_file1.txt'

with open(genfile, "w") as outputfile:
    with MssqlDB(conf.driver, conf.server, conf.database, conf.sql_user, conf.sql_password) as db:
        rs_lookup_table = db.load_data_by_query(qr_clob_blob, 'D')
        rs_load_table = db.load_data_by_query(qr_table, 'T')

        for tab_key in rs_load_table:
            if tab_key in rs_lookup_table:
                outputfile.write("insert into {0} values ({1})".format(tab_key, rs_load_table[tab_key]))
            else:
                outputfile.write("insert into {0} values ({1})".format(tab_key, "null"))

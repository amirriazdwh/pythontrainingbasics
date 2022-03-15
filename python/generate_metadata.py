from config import gsproperty as conf
from sqldbms import MssqlDB, qr_clob_blob, qr_table, ins_query

__name__ = "__main__"

batch_id = 1101
src_schema = '''ELCM'''
dest_schema = '''ELCM'''
primary_key = '''null'''
fetch_size = 500
select_columns = '''null'''
incremental_key = '''null'''
fields_terminated_by = 'null'
file_formats = '''parquete'''
compression_type = '''xyz'''
mappers = 8
split_by_key = '''null'''
where_clause = '''null'''
query = '''select * from {0}'''
pre_run_script = '''null'''
post_run_script = '''null'''
load_priority = 1
additional_arguments = '''null'''
import_export = '''I'''

genfile = '/home/cibg_uat_user/obdx/genfile/meta_catalog.sql'

with open(genfile, "w") as outputfile:
    with MssqlDB(conf.driver, conf.server, conf.database, conf.sql_user, conf.sql_password) as db:
        rs_lookup_table = db.load_data_by_query(qr_clob_blob, 'D')
        rs_load_table = db.load_data_by_query(qr_table, 'T')

        for tab_key in rs_load_table:
            if tab_key in rs_lookup_table:
                outputfile.write(
                    ins_query.format(batch_id, src_schema, tab_key, dest_schema, tab_key, primary_key, fetch_size,
                                     rs_lookup_table[tab_key], rs_lookup_table[tab_key],
                                     select_columns, incremental_key, fields_terminated_by, file_formats,
                                     compression_type,
                                     mappers, split_by_key, where_clause, query, pre_run_script,
                                     post_run_script, load_priority, additional_arguments, import_export))
            else:
                outputfile.write(
                    ins_query.format(batch_id, src_schema, tab_key, dest_schema, tab_key, primary_key, fetch_size,
                                     'null','null',
                                     select_columns, incremental_key, fields_terminated_by, file_formats,
                                     compression_type,
                                     mappers, split_by_key, where_clause, query, pre_run_script,
                                     post_run_script, load_priority, additional_arguments, import_export))

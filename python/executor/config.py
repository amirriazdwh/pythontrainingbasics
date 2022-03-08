class gsproperty:

    server = "192.168.56.102"
    server_port = 1433
    database = "HADOOP_REPO"
    sql_user = "HADOOP"
    sql_password = "HADOOP"
    driver = '{ODBC Driver 17 for SQL Server}'
    sql_url = 'jdbc:sqlserver://%s:%s;databaseName=%s;user=%s;password=%s' % (
        server, server_port, database, sql_user, sql_password)
    sql_driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    sql_config_table = "DLINGESTIONUAT.executorconfigobtf"
    sql_result_table = "DLINGESTIONUAT.executorresultobtf"

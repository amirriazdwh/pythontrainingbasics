'''
Module Name : filehandling.py
Created On : 10th Nov 2019
Created By : Neha Goel
Purpose : This module is for mail messaging functionalities related functions called at certain stages
'''

#Importing Python Libraries 
import os
import shutil
from shutil import make_archive, rmtree
import time
import xlsxwriter
import sys
import logging

#Importing Package Modules
import configurations
import sessionutils

def create_zip_file(fileslist,batchname):
	try:
		#Creating a Temp directory
		currdatetime = sessionutils.getcurrdatetime()
		tmpfolderfullpath = configurations.ziptmpdir + batchname.replace(' ','') + '_' + currdatetime
		os.mkdir(tmpfolderfullpath,configurations.ziptmpdiraccsrights)

		#Copying all logs to temp zip directory, so that it can be zipped later
		for a in fileslist:
			shutil.copy2(a,tmpfolderfullpath)

		#Creating a Zip file of the folder
		shutil.make_archive(tmpfolderfullpath,'zip',tmpfolderfullpath)

		#Remove the directory, Only Zip file will be available on the server
		shutil.rmtree(tmpfolderfullpath)

		return tmpfolderfullpath + '.zip'
	except Exception as e:
		raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(sys.exc_info()[-1].tb_lineno)  + ' : ' + str(e))


def create_excel_file(metadbconn,batchname,batchrunid):
	try:
		workbook = ''

		#Get the directory to create excel file at
		currdatetime = sessionutils.getcurrdatetime()
		tmpfolderfullpath = configurations.exltmpdir + batchname.replace(' ','') + '_' + currdatetime
		workbookname = tmpfolderfullpath + '.xlsx'

		#Create the excel workbook object and fetch data
		workbook = xlsxwriter.Workbook(workbookname)
		conn = metadbconn
		cursor = conn.cursor()
		sqlquery = 'select a.dest_schema, a.dest_obj_name, b.run_status, b.prescriptstatus, b.sqoopstatus, b.postscriptstatus \
						from {}.tbljobconfig a, {}.tbljobrundetails b where a.job_id = \
						b.job_id and b.batch_run_id = {} order by run_status'.format(configurations.metadb_schema, configurations.metadb_schema, batchrunid)
		cursor.execute(sqlquery)

		data = cursor.fetchall()
		worksheet = workbook.add_worksheet("Tables Load Stats")

		#Defining some formatting objects to use
		headerrow = workbook.add_format({'bold':True,'font_color':'white','bg_color':'#0F243E'})
		datarow = workbook.add_format({'font_color':'black','bg_color':'#DDD9C4'})

		#Writing data headers in the excel
		worksheet.write('A1','Schema', headerrow)
		worksheet.write('B1','Object', headerrow)
		worksheet.write('C1','Overall Status', headerrow)
		worksheet.write('D1','Pre Script Status', headerrow)
		worksheet.write('E1','Sqoop Status', headerrow)
		worksheet.write('F1','Post Script Status', headerrow)
		worksheet.set_column(0,6,25)

		# Iterate over the data and write it out row by row. 
		row = 1
		col = 0
		for schema, name, status, pres, sqoops, posts in (data): 
			worksheet.write(row, col, schema, datarow) 
			worksheet.write(row, col + 1, name, datarow) 
			worksheet.write(row, col + 2, status, datarow) 
			worksheet.write(row, col + 3, pres, datarow)
			worksheet.write(row, col + 4, sqoops, datarow)
			worksheet.write(row, col + 5, posts, datarow)
			row += 1

		return workbookname
	except Exception as e:
		raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(sys.exc_info()[-1].tb_lineno)  + ' : ' + str(e))
	finally:
		if workbook != '':
			workbook.close() 
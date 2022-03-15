from config import gsproperty as conf
# import pyodbc


def getClob_and_Blobs():
   return {"table1": "c1,c2"}


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
genMetaData(inputfile, outputfile, getClob_and_Blobs())

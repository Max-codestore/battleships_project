import csv
def read_text_file(file,end="\n"):#requires file to be imputed when the fuction is called and defines end as new line charater 
    data=[]#creats the list data 
    f=open(file,"r")#opens the file specified when the fuction is called
    for line in f.readlines():#for as many lines as the file has read them
        data.append(line.strip(end))#reads each line until it finds a new line charater and adds the content to the list data
    f.close()#closes the file after all lines have been read
    return data#returns the list data to the rest of the code

#def read_text_file_muti_collum(file,end="\n"):
#    data1=[]
#    data2=[]
#    final_data=[]
#    f=open(file,"r")
#    for line in f.readlines():
#        data1.append(line.strip(end))
#        data2.append(column.strip)
#    f.close
#    final_data.append([data1,data2])
#    return final_data
#read_text_file_muti_collum("random text.txt")
#print(final_data)
def read_text_file_muti_collum(file,end="\n"):
    dataTwo=[]
    f = open(file, 'r')
    for line in f.readlines():
        line=line.split()
        record=[]
        for item in line:
            record.append(item.strip(end))
        dataTwo.append(record)
    f.close()
    return dataTwo 
#dataTwo=read_text_file_muti_collum("random text2.txt")
#print(dataTwo)
def read_text_file_2D(text_file): 
	data=[] 
	file = open(text_file, 'r') 
	for line in file.readlines(): 
		line=line.split() 
		record=[] 
		for item in line: 
			record.append(item.strip("\n"))
		data.append(record)
	file.close()
	return data

def read_csv_file(csv_file):
    l=[]
    file=open(csv_file)
    r=csv.reader(file)
    num=0
    for i in r:
        l.append(i)
        num=num+1
    file.close()
    return l
#print(read_csv_file("read_excel_test.csv"))
def write_file_list(file,list):
    f=open(file,'w')
    f.writelines(list)
    f.close()

#write_file_list("hello",list=['this work too?'])

def write_text_file(text,file,end=""):
    for i in range(len(text)):
        text[i]=text[i]+end 
	
    f=open(file,'w')
    f.writelines(text)
    f.close() 
 
#write_text_file(["hello"],'r.dll')

def append_file_list(file,list):
    f=open(file,'a')
    f.writelines(list)
    f.close()

#append_file_list("hello",list=['still?'])

def help():
    print("to read a text file use text_file_manger.read_text_file(put the name of the file you want to read here) to read a muti collum file use read_text_file_2D(put the name of the file you want to read here)to read a csv file use text_file_manger.read_csv_file(enter file name here) and to write a file  use text_file_manger.write_file_list('what you want to call the file.txt'['enter text you want to enter here','enter text you want here'] and to append a text file text_file_manger.append_file_list('what you want to call the file.txt'['enter text you want to enter here','enter text you want here'] ")  

text=[['Bart', 'Simpson', 12, 17, 18], 
      ['Nelson', 'Muntz', 15, 16, 19], 
      ['Ralf', 'Wiggum', 23, 10, 10]] 


def write_text_file_2d(data,file,end=""): 	
	f=open(file,'w'); 
	for line in data: 
		for item in line: 
			item=str(item)+" " 
			f.write(item) 
		f.write(end) 
	f.close()
text=[['Bart', 'Simpson', 12, 17, 18], 
      ['Nelson', 'Muntz', 15, 16, 19], 
      ['Ralf', 'Wiggum', 23, 10, 10]] 

#write_text_file_2d(text,"13.students_out.txt",end="\n")

def append_text(text,file): 
	f=open(file,"a") 
	print(f.write(text)) 
	f.close() 

#text="Lisa Simpson 0 0 0 10" 
#append_text(text,"13.students_out.txt")

#data=read_text_file_2D("13.students_out.txt") 
#data[0].append(7) 
#data[1].append(8) 
#data[2].append(9) 
#data=write_text_file_2d(data,"13.students_out.txt", end="\n") 

# Add row 
def append_text(text,file): 
	f=open(file,"a") 
	print(f.write(text)) 
	f.close() 

#text="Lisa Simpson 0 0 0 10" 
#append_text(text,"students.txt")

def copy_file(copy,paste):
    fi = open(copy, 'r')
    fo = open(paste, 'w')
    for line in fi.readlines():
        fo.write(line)
        print(data)
    fi.close()
    fo.close()
#copy_file("students.txt","r.dll")
#data=read_text_file_2D("13.students_out.txt") 
#print(data) 


import mysql.connector as connector

class Operation:
    
    def __init__(self) :
        self.con=connector.connect(host='localhost',port='3306',user='root',password='root',database='jobAssistent')

        query='create table if not exists jobs(jobID int primary key AUTO_INCREMENT,Qualification varchar(150), Experience varchar(150),specialization varchar(50),jobRole varchar(50),jobDescription varchar(500),noOfPosts int)'
        
        cur=self.con.cursor()
        cur.execute(query)
        # print('Table Created.')

    def showAllJobs(self):
        query='select * from jobs where experience="fresher"'  
        cur=self.con.cursor()
        cur.execute(query)
        for count,row in enumerate(cur,1):
            print('Job ID   :', row[0])
            print('Qualfication :', row[1])
            print('Experiance     :', row[2])
            print('Job Role   :', row[3])
            print('Job Description  :', row[4])
            print('No of Posts     :', row[5])
            print('')
            
            
    
    # Function for access the jobs list from database..
    def searchJobs(self,qualification,experiance=None,specialization=None,jobRole=None):
        if (specialization==None and experiance==None and jobRole==None):
            query=f'SELECT COUNT(jobID) FROM jobs WHERE Qualification = "{qualification}"'
            cur=self.con.cursor()
            cur.execute(query) 
            records = cur.fetchall()
            if records[0][0]>0:
                return records[0][0]
            else:
                return False
            
        elif(jobRole==None and specialization==None):
            query=f'SELECT COUNT(jobID) FROM jobs WHERE Qualification = "{qualification}" and Experience="{experiance}" '
            cur=self.con.cursor()
            cur.execute(query) 
            records = cur.fetchall()
            if records[0][0]>0:
                return records[0][0]
            else:
                return False
            
        elif(jobRole==None):
            query=f'SELECT COUNT(jobID) FROM jobs WHERE Qualification = "{qualification}" and Experience="{experiance}" and specialization="{specialization}"'
            cur=self.con.cursor()
            cur.execute(query) 
            records = cur.fetchall()
            if records[0][0]>0:
                return records[0][0]
            else:
                return False
                
        else:   
            query=f'SELECT COUNT(jobID) FROM jobs WHERE Qualification = "{qualification}" and Experience="{experiance}" and specialization="{specialization}" and jobRole="{jobRole}"'
            cur=self.con.cursor()
            cur.execute(query) 
            records = cur.fetchall()
            if records[0][0]>0:
                query=f'SELECT * FROM jobs WHERE Qualification = "{qualification}" and Experience="{experiance}" and specialization="{specialization}" and jobRole="{jobRole}"'
                cur=self.con.cursor()
                cur.execute(query)
                return records[0][0],cur
            else:
                return False 
        
        
            

# os=Operation()
# os.searchJobs('b tech','fresher','compuer science','software developer')
        # if productID!=None:
        #     query=f'SELECT COUNT(ProductID) FROM Products WHERE ProductID = {productID}'
        #     cur=self.con.cursor()
        #     cur.execute(query) 
        #     records = cur.fetchall()
        #     if records[0][0]>0:
        #         query=f'select * from Products where ProductID={productID}' 
        #     else:
        #         print('This Id is not found.')   
        #         return 
        # else:
        #     query=f'select * from Products ' 
        # cur=self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print('Job ID   :', row[0])
        #     print('Qualfication :', row[1])
        #     print('Experiance     :', row[2])
        #     print('Job Role   :', row[3])
        #     print('Job Description  :', row[4])
        #     print('No of Posts     :', row[5])
        #     print('')
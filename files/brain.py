import datetime
from files import commands
import webbrowser as wb
from files.jobHelper import Operation

op=Operation()

def wishMe ():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        commands.speak(f"Good Morning!")
    elif hour>=12 and hour<18:
        commands.speak(f"Good Afternoon!")   
    else:
        commands.speak(f"Good Evening!")  
    commands.speak("I am Alina, your personal assistant sir!.how may I help you...")
    

    
def search_jobs(qualification,experiance=None,specialization=None,jobRole=None):
    if (experiance==None and specialization==None and jobRole==None):
        noOfJobs=op.searchJobs(qualification)
        if noOfJobs!=False:
            commands.speak(f'There are {noOfJobs} jobs available in {qualification}.')
        else:
            commands.speak(f'There are Not any jobs available in {qualification}.')
            return False
                
    elif (specialization==None and jobRole==None):
        noOfJobs=op.searchJobs(qualification,experiance)
        if noOfJobs!=False:
            commands.speak(f'There are {noOfJobs} jobs available in {qualification} for {experiance}.')
        else:
            commands.speak(f'There are Not any jobs available in {qualification} for {experiance}')
            return False
            
            
    elif (jobRole==None):
        noOfJobs=op.searchJobs(qualification,experiance,specialization)
        if noOfJobs!=False:
            commands.speak(f'There are {noOfJobs} jobs available in {qualification} for {experiance} in {specialization} field.')
        else:
            commands.speak(f'There are Not any jobs available for {experiance} in {specialization} field.')
            return False
            
    else:
        noOfJobs,jobs=op.searchJobs(qualification,experiance,specialization,jobRole)    
        if noOfJobs!=False:
            commands.speak(f'There are {noOfJobs} jobs available for post {jobRole} in {qualification} for {experiance}.  Here are more details about the job.')
            for row in jobs:
                print('Job ID   :', row[0])
                print('Qualfication :', row[1])
                print('Experiance     :', row[2])
                print('Specialization     :', row[3])

                print('Job Role   :', row[4])
                print('Job Description  :', row[5])
                print('No of Posts     :', row[6])
                print('')
                return False
        else:
            commands.speak(f'sorry sir There are Not any jobs available for post {jobRole} in {qualification} for {experiance}jobs available.')    
            return False
    

    
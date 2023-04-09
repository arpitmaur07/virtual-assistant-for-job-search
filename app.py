from files import commands
from files import brain


if __name__=='__main__':
    brain.wishMe()
    while True:

        query=commands.takeCommand()
        if commands.check_message(['search','job'],query) or commands.check_message(['find','job'],query):
                        
            commands.speak('what is your qualification?')
            qualification=commands.takeCommand()
            check=brain.search_jobs(qualification)
            if check==False:
                break
        
            commands.speak('what is your experiance?')
            experiance=commands.takeCommand()
            if commands.check_message(['pressure'],experiance) or commands.check_message(['fresher'],experiance) or commands.check_message(['fresh'],experiance) or commands.check_message(['trisha'],experiance) or commands.check_message(['no','experiance'],experiance):
                
                experiance='fresher'
                check=brain.search_jobs(qualification,experiance)
                if check==False:
                    break
            elif(commands.check_message(['experiance'],experiance) or commands.check_message(['experianced'],experiance) or commands.check_message(['not','fresher'],experiance) or commands.check_message(['year'],experiance))or commands.check_message(['years'],experiance):
                
                experiance='experianced'
                check=brain.search_jobs(qualification,experiance)
                if check==False:
                    break
            else:
                experiance=experiance  
         
            commands.speak('what is your specialization')
            specialization=commands.takeCommand()
            check=brain.search_jobs(qualification,experiance,specialization)
            if check==False:
                break
            
            commands.speak('what job role you are searching for?')
            jobRole=commands.takeCommand()
            check=brain.search_jobs(qualification,experiance,specialization,jobRole)
            if check==False:
                break
        else:
            if query=='None':
                print('waiting...')
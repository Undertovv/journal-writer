import datetime

#A list of prompts, feel free to edit later. 
prompts = ['How long did I sleep for?: ', 'How much have I eaten?: ', 'Who have I talked to today?: ',
          'Have I left the house?: ', 'Did anything else happen today? ']

#create and name file timestamped with current date/time 
getTime = datetime.datetime.now()
getTime = str(getTime)
journal = open(getTime, 'w')

#print all prompts as output to the file and request user input
for prompt in prompts:
    journal.write(str('\n' + prompt + '\n'))
    #Blankspace at the start of the page, it hurts my soul but it'll have to stay.
    journal.write(str(input(prompt)))
    journal.write(str('\n'))


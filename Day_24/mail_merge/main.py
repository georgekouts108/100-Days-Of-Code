#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


start_letter = open('./Input/Letters/starting_letter.txt', 'r')
template = start_letter.read()
start_letter.close()

names_file = open('./Input/Names/invited_names.txt', 'r')
invited_ppl = names_file.read()
names = invited_ppl.split('\n')
names = [name.title() for name in names]
names_file.close()

names_set = set(names)

for name in names_set:
    invitation = template.replace('[name]', name)
    name_count = names.count(name)

    if name_count > 1:
        for nc in range(name_count):
            file = open(f'./Output/ReadyToSend/invite_for_{name}_{nc+1}.txt', 'w')
            file.write(invitation)
            file.close()
    else:
        file = open(f'./Output/ReadyToSend/invite_for_{name}.txt', 'w')
        file.write(invitation)
        file.close()
        

# Dictionaries and Maps

#Adding contacts
agenda = dict()
num_contacts = int(input())
for i in range(0, num_contacts):
    entry = list(input().split())
    agenda[entry[0]] = entry[1]
#Checking contacts
while 1:
    try:
        check = input()
        if check in agenda:
            print(f'{check}={agenda.get(check)}')
        else:
            print('Not found')
    except:
        break

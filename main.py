import requests
import jsons
import json

file=input("enter file name : ")
fileReader=open(file,"r")
l=fileReader.read().strip("\n").split(',')

#loop through file
for i in l:
    print("details for DOI {}".format(i))

# api-endpoint
# i is the single DOI
URL = "https://api.crossref.org/works/"+i 
r = requests.get(url = URL)

# extracting data in json format
data = r.json()

print("title:",end="  ")
title=data['message']['title'][0]
print(title)
authors=[]

print("author(s):",end="\n\t")
for i in range(len(data['message']['author'])):
    name=data['message']['author'][i]['given'] + data['message']['author'][i]['family']
    authors.append(name)

print("\n\t".join(authors))


print("published date:",end="  ")
get_date_parts=data['message']['issued']['date-parts']
#print(get_date_parts)
if(len(get_date_parts[0])==1):
    date_issued=str(get_date_parts[0][0])
elif(len(get_date_parts[0])==2):
    date_issued=str(get_date_parts[0][1])+"-"+str(get_date_parts[0][0])

else:    
    date_issued=str(get_date_parts[0][2])+"-"+str(get_date_parts[0][1])+"-"+str(get_date_parts[0][0])

print(date_issued)
print()
print()
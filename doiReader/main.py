import requests

file=input("enter file name : ")
fileOpener=open(file,"r")
fileReader=fileOpener.read().strip("\n").split(',')
csv_file=open("output.csv","w")
csv_file.write("DOI Number, Title of Publication, Author(s), Date of Publication, Journal Name, Volume(Issue), \n")

#loop through file
for i in fileReader:
    #print("details for DOI {}".format(i))

    # api-endpoint
    # i is the single DOI
    csv_file.write(i+",")
    URL = "https://api.crossref.org/works/"+i 
    r = requests.get(url = URL)

    # extracting data in json format
    data = r.json()
   

    #print("title:",end="  ")
    title=data['message']['title'][0]
    #print(title)
    title=title.replace(",","")
    csv_file.write(title+",")
    authors=[]

    #print("author(s):",end="\n\t")
    for i in range(len(data['message']['author'])):
        name=data['message']['author'][i]['given'] + data['message']['author'][i]['family']
        authors.append(name)       

    #print("\n\t".join(authors))
    authors=" ".join(authors)
    csv_file.write(authors+",")


    #print("published date:",end="  ")
    get_date_parts=data['message']['issued']['date-parts']
    #print(get_date_parts)
    if(len(get_date_parts[0])==1):
        date_issued=str(get_date_parts[0][0])
    elif(len(get_date_parts[0])==2):
        date_issued=str(get_date_parts[0][1])+"-"+str(get_date_parts[0][0])

    else:    
        date_issued=str(get_date_parts[0][2])+"-"+str(get_date_parts[0][1])+"-"+str(get_date_parts[0][0])

    csv_file.write(date_issued+"\n")
    
    #print journal name
    journals=[]
    for i in range(len(data['message']['container-title'])):
        journalName=data['message']['container-title'][i]
        journals.append(journalName)

    journals=" ".join(journals)
    csv_file.write(journals+",")

    #volume 
    volumes=[]
    
    for i in range(len(data['message']['volume'])-1):
        volumeNum=data['message']['volume'][i]
        volumes.append(volumeNum)
       
    

    volumes="".join(volumes)
    csv_file.write(volumes)
    
 

    

print("finished and wrote to csv file")
  

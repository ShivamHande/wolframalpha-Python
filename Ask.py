import wolframalpha 
def Ask():

    query=input("Ask the Question:--")
    app_id = "your app id"  
    client = wolframalpha.Client(app_id)  
    res = client.query(query) 
    sol = next(res.results).text 
    print(sol)

Ask()
while True:
    s=input("Do you want Ask again?? (y/n)")
    if(s=='y' or s=='Y'):
        Ask()
    else:
        exit()    

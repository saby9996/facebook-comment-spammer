import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy

def spam():
    token="CAACEdEose0cBAK7gbUKb6ZBczyblSNWQiSL2dgoZAKKhmTch0ZABnNZB0CtfhNZBHZBQSJZAcy39E01J1E0voKkmBcsyu0vmBo454QywPgRL8xUJLjqQoKuitw7PgaQqYxXsJlzs1ZCtl1A6kjojHJrdRFlrlOGWZAxgTOU5vrZAA8GJxZCWzcQPWNT7ZBzkVI5oFBXcvW7cZCUzAYFhAdrU2UmJ9CGwCGm1cZCxUZD"#Insert access token here.  
    facebook=fb.graph.api(token)
    graph1 = GraphAPI(token)
    
    vid=input("Enter victim's id: ")
    query=str(vid)+"/posts?fields=id&limit=5000000000"
    r=graph1.get(query)
    
    
    
    idlist=[x['id'] for x in r['data']]
    idlist.reverse()
    print("There are "+ str(len(idlist)) +" spammable posts.")
    
    char1=raw_input("Do you want to spam? (y/n) ")
    count=0
    if char1=='y':
        nos=input("Enter number of posts to be spammed with comments: ")
        mess=raw_input("Enter the message to be commented: ")
        if nos<=len(idlist):
           for indid in (idlist[(len(idlist)-nos):]):
        
              facebook.publish(cat="comments",id=indid,message=mess) #Comments on each post
              facebook.publish(cat="likes",id=indid)                 #Likes each post
              count=count+1
              print("Notification number:"+str(count)+" on www.facebook.com/"+str(indid).split('_')[0]+"/posts/"+str(indid).split('_')[1])
        else: 
              print("Not that many spammable posts available. No spam happening.")
    else :
      print("No spam happening then.")

spam()
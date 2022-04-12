import requests
import tkinter as tk
from datetime import datetime
import socket
import geocoder
import folium
import json
url = "https://www.fast2sms.com/dev/bulk"
c="7980721034"



def IP():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    g=geocoder.ip("me")
    label.config(text=g)
    

def trackBTC():
    url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response=requests.get(url).json()
    
    price=response["USD"]
    time=datetime.now().strftime("%H:%M:%S")
    
    label.config(text=str(price)+" $"+" "+"updated at:"+time)
    
    canvas.after(1000,trackBTC)

def sendSMS():
    my_data = { 
    # Your default Sender ID 
    'sender_id': 'FSTSMS', 
    
    # Put your message here! 
    'message': 'This is a test message', 
    
    'language': 'english', 
    'route': 'p', 
    
    # You can send sms to multiple numbers 
    # separated by comma. 
    'numbers': c    
}
    headers = { 
    'authorization': 'NB9GLWDnYTMJCo0PfRQuqtsc7dvXEhiI5epO4kS3aAwKZjFx8mlgO2mR8PYzpIGJsXNUHMZnao9viESD', 
    'Content-Type': "application/x-www-form-urlencoded", 
    'Cache-Control': "no-cache"
}

    # make a post request 
    response = requests.request("POST",url,data = my_data,headers = headers) 

    returned_msg = json.loads(response.text)
    label.config(text="Message sent successfully")
    
    
    
    
    
    
def getNews():
    api_key="7b55f6a3be0f4829b84a23f22b99650f"
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
    news=requests.get(url).json()
    articles=news["articles"]
    my_articles=[]
    my_news=""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news=my_news+str(i+1)+". "+my_articles[i]+"\n"


    label.config(text=my_news)


canvas=tk.Tk()
canvas.geometry("900x900")
canvas.title("NEWS APP")
canvas.config(bg="blue")
canvas.title("NEWS APP")

button=tk.Button(canvas,font=42,bg="yellow",text="TRACKWORLD APP",command=getNews)
button.pack(pady=20)
button=tk.Button(canvas,font=24,bg="white",text="TOP NEWS",command=getNews)
button.pack(pady=20)
button=tk.Button(canvas,font=24,bg="white",text="BITCOIN PRICE(USD)",command=trackBTC)
button.pack(pady=20)
button=tk.Button(canvas,font=24,bg="white",text="LOCATION",command=IP)
button.pack(pady=20)
button=tk.Button(canvas,font=24,bg="white",text="SEND SMS",command=sendSMS)
button.pack(pady=20)
label=tk.Label(canvas,font=18,justify="left")
label.pack(pady=20)
canvas.mainloop()

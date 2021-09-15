import paho.mqtt.client as mqtt
import requests
import json
#import context  # Ensures paho is in PYTHONPATH



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("get/from/0089227fmik")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  try:
   url = "https://api.github.com/repos/ansali1/mikmon/contents/LGLS7752a1d2e6palm"
   payload="{\"message\":\"message\",\"content\":\"555\",\"sha\":\"ea634f4e54088f7521da90fdcdbaded4bdb652e8\"}"
   headers = {
   'Authorization': 'Bearer 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',
   'Content-Type': 'text/plain'
   }
   response = requests.request("GET", url, headers=headers, data=payload)
   data = json.loads(response)
   for i in data['sha']:
     print(response.text)
  #st.write(msg.topic+" التوبك وصل ياشباب"+str(msg.payload))

#url = "https://api.github.com/repos/ansali1/mikmon/contents/LGLS7752a1d2e6palm"

#payload="{\"message\":\"message\",\"content\":\"555\",\"sha\":\"ea634f4e54088f7521da90fdcdbaded4bdb652e8\"}"
#headers = {
#  'Authorization': 'Bearer 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',
 # 'Content-Type': 'text/plain'
#}

#response = requests.request("PUT", url, headers=headers, data=payload)

#print(response.text)
 
   #print(data.decode("utf-8"))

  except:
   x=1

   
 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.mqtt-dashboard.com", 1883, 60)
client.loop_forever()

 

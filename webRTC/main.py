from fastapi import FastAPI
app = FastAPI()

'''

Process to create peer to peer connection

1 - Client 1 - Creates and offer, sends to signaling server.
2 - Client 2 - Request for an offer, Creates an Answer.
3 - Client 2 - Send the Answer to signaling server.
4 - Client 1 - Receives the Answer.

'''


#data dictionary to store the offer

data = {}

# Create offer by Client - ONE

@app.get('/offer')
async def baseRoute():
    return {"details" : "offer"}



# See offer by Client - Two
@app.get('/get_offer')
async def baseRoute():
    return {"details" : "offer"}


# Client - TWO -> Response of the offer 
@app.get('/answer')
async def baseRoute():
    return {"details" : "offer"}


# Client - ONE -> Get the answer
@app.get('/get_answer')
async def baseRoute():
    return {"details" : "offer"}


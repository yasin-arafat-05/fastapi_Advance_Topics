from fastapi import FastAPI
app = FastAPI()


'''
app.add_middleware(...): This line adds middleware to the FastAPI application.
Middleware functions are components that can process requests and responses globally 
before they reach the route handlers or after they leave the route handlers.


CORSMiddleware: Cross-Origin Resource Sharing (CORS) is a security feature implemented by web 
browsers to restrict webpages from making requests to a different domain than the one that 
served the original webpage. CORSMiddleware is a middleware provided by Starlette 
(the underlying web framework for FastAPI) that helps handle CORS headers.


allow_origins=["*"]: This specifies which origins are allowed to make requests to your FastAPI 
application. In this case, "*" means any origin is allowed. In a production setting, 
you might want to specify specific origins instead of allowing all ("*").


allow_credentials=True: This allows the use of credentials (like cookies and HTTP authentication) 
when making requests from the allowed origins. This is useful if your application requires user 
authentication.


allow_methods=["*"]: This specifies which HTTP methods are allowed for cross-origin requests. 
Again, "*" means all methods are allowed.


allow_headers=["*"]: This specifies which HTTP headers are allowed for cross-origin requests. 
"*" means all headers are allowed.
'''

from starlette.middleware.cors import CORSMiddleware

app.add_middleware(
 CORSMiddleware,
 allow_origins=['*'],
 allow_credentials = True,
 allow_methods = ["*"],
 allow_headers = ["*"]
)


# WE know to connect WebRTC we need WebSockets:
'''
    In webRTC - architure(pdf in my github). We see that,

    1) RTCPeerConnection() object is the entry point of: p2p.

    2) RTCPeerConnection object configures streams so they
    could connect to each other, peer-to-peer. This signaling is done via HTTP or WEBSockets.
'''


# RTCPeerConnection object:
from aiortc import RTCPeerConnection,RTCSessionDescription
class Connection:
    def __init__(self):
        self.pc = RTCPeerConnection()

#  p2p connection/signaling done via WebSockets:
from fastapi import WebSocket
@app.websocket("/ws")
async def WEBSOCKET_ENDPOINT(websocket : WebSocket):
    await websocket.accept()
    connetn  = Connection()

    #As long as we received data from websocket:
    while True:
        data = await websocket.receive_text()

        # (data=="offer"):
        '''
        The specific check data == "offer" in the code is 
        essentially a signaling convention chosen by the developer.

        In the context of WebRTC applications, signaling is the process 
        by which two peers communicate and exchange information needed to establish a connection.

        This is a signaling message (data=="offer"). It's like the client saying, 
        "I want to establish a connection, let's start the process."
        '''

        # createOffer()
        '''
        The server, upon receiving the "offer" message, generates an offer using 
        connection.pc.createOffer().

        An "offer" in WebRTC is a description of the server's capabilities and settings related 
        to media communication (audio, video, etc.). The createOffer() method is used 
        to generate this offer.
        '''

        # setLocalDescription():
        '''
        The local description is a configuration that describes the server's end of the connection. 
        It includes details such as supported codecs, media formats, and other settings. 

        server's end mainly taking about the server: In a WebRTC application, there are typically 
        two participants: a client and a server.
        '''

        #sent_text(connetn.pc.localDescription.sdp):
        '''
        The server sends the SDP (Session Description Protocol) part of the local description back to 
        the client.
        '''

        # Summary of the code: 
        '''
        Summary:
        -> The "offer" message triggers the start of the WebRTC connection negotiation process.
        -> The server creates an offer that describes its capabilities.
        -> The local description is updated with this offer, representing the server's configuration.
        -> The server sends the SDP part of the local description to the client, allowing both peers to exchange information and establish a common set of parameters for their WebRTC connection.
        '''
        if data == "offer":
            offer = await connetn.pc.createOffer()
            await connetn.pc.setLocalDescription(offer)
            await websocket.send_text(connetn.pc.localDescription.sdp) # (udp + tcp) -> we use sdp

            '''
                when the received data starts with the string "answer".
                The SDP (Session Description Protocol) part of the received message is extracted. 
                The message format appears to be "answer SDP_CONTENT", and splitting at the first 
                space retrieves the SDP content.
            '''
        elif data.startswith("answer"):
            sdp = data.split(" ", 1)[1]
            await connetn.pc.setRemoteDescription(RTCSessionDescription(sdp=sdp))
        elif data.startswith("ice"):
            ice = data.split(" ", 1)[1]
            await connetn.pc.addIceCandidate(ice)


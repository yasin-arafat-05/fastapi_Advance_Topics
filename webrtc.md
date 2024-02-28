
<br><br><br><br><br><br>

# ________________________Lecture-01______________________

<br><br><br><br><br><br>

# What is WebRTC ? | Webrtc Introduction to beginners |

 - `Webrtc or web real-time communication` is a set of protocols and api's that enable real-time communication over peer-to-peer connection.

 - In 2011, google released `browser-based webrtc project` and this technology will help you to make different apps like `video conferencing`, `file transfer`, `chats` and `desktop sharing` without any external applications.
 
 - Webrtc uses real-time transfer protocols to `transfer video and audio` over peer connection this is completely `open source and free` under the terms of berkeley source distribution license.
 
 - Webrtc supports on browsers like `chrome mozilla, opera, microsoft edge, android blackberry` etc.
 
# let's talk why should we use this technology:
-  It is completely `open source and free` next reason is you just required only a `webrtc compatible browser` to work this technology 

# Webrtc provided some api's to develop the application:

- **`GetUserMedia()`**  this api helps to access `user webcam and microphone` from the browser.

- **`RTCPeerConnection()`** this api helps to set up `video and audio calls` between peer connection also it take care of encoding and decoding NAT traversal 
**we will explain these terms in the upcoming chanpter**
- **`RTCDataChannel()`** this api helps to `share data over peer connection`.

- **`GetStats()`** this api helps to get `webrtc session` in the browser.



<br><br><br><br><br><br>

# ________________________Lecture-02______________________

<br><br><br><br><br><br>

# WebRTC Vs Websocket:

### Web sockets:
 **Web sockets** are a `bi-directional mechanism` for browser communication. There are two types of transport channels for communication in browsers one is `http` and other is `web sockets`. http mainly used to fetch resources like `web pages images javascript` etc. `http is a client server protocol` where the `browser is the client` and the `web server is the server`
 
- `Websocket` are two way commnucation system.`http` is unidirectional protocol that means `client send request and server send response`.

- Websocket is created by the commands like `ws:// or wss://` another important property of websocket is `stateful protocol` that means connection between `client and server will be alive until the connection terminated by either server or client` this new connection is known as websocket.

- Websocket has the property stateful protocol it can be used in real-time web applications and chat applications.

<br> 

# **WebRTC:**
 There are some advantages for `webrtc` than a `web socket` let us look what are they webrtc is designed for high performance high quality communication of video audio and data webrtc is `browser to browser` communication and really fast another interesting thing is webrtc uses.

### **Why webRTC is better than WebSocket:**

- **WebSocket** use `udp` connection but websocket uses `tcp` connection.
    - **udp**: It stands for **User Datagram Protocol**.
    - **tcp**:  It stands for **Transmission Control Protocol**.
    - [Difference Between UDP and TCP](https://www.youtube.com/watch?v=4ksqUnW7eak&ab_channel=LearnCoding)
    ![Alt text](/images/image7.png)
<br>

- Another important advantage is `latency`. Webrtc provides smooth audio video communication with `low latency` whereas `websocket provide high latency` with `choppy playback`.

<br>

### Does **webRTC** use **websockets**:

- Another interesting fact is **webrtc** uses **websocket** connection. WebRTC uses peer to peer technology and once the connection is up and running, you do not need to pass the **communication** via a server. When setting up  Webrtc **communication** you have to use uses **signaling mechanism** to achieve the connection.

<br><br><br><br><br><br>

# ________________________Lecture-03______________________


<br><br><br><br><br><br>

# WebRTC signaling - Why it is required ? | STUN & TURN | 

 - First **signaling** is the process of setting up **controlling and terminating** a communication session between the clients.

- Signaling is necessary to communicate between endpoint users in p2p(peer to peer) communication. Generally, to communicate between two endpoint **major three process needs to be happen:** 

    - first, session control information need to be shared.
    - exchange ip address and port related information between end users.
    - Lastly, codec and media types of the end user need to be shared.
    - **("codec" stands for "coder-decoder" or "compression-decompression" .It refers to a technology or algorithm that is used to compress and decompress data, typically for the purpose of encoding and decoding audio or video information.)** `like: XVID -> openCV`

# **now let us look why these components are required in the communication session**

- **Session Control** information will determine, when needs to be connected closed and send information between end users.

- **Ip and port related information** are required to identify the end user and where he or she located.

- **Codec and media type exchange** is required to set up the particular resolution and media configuration between end users.

`And these data's our (metadata) then how this metadata are shared in between end users. And here comes session description protocol (SDP) protocol sdp will be used for the exchange of metadata.

# Why signaling?
- We already know that webrtc is a **web browser based technology** so there should be a **server required** to exchange the user data initially to set up webrtc connection. This server is called a **signaling server** and the process of sharing metadata is called **signaling** after the signaling process all the media and data will be exchanged via rtc peer connection of webrtc.





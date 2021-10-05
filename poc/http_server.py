from socket import *

PORT = 9001

def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    try:
        serverSocket.bind(('localhost', PORT))
        serverSocket.listen(5)

        while(1):
            (clientSocket, address) = serverSocket.accept()

            rd = clientSocket.recv(5000).decode()
            pieces = rd.split("\n")

            if (len(pieces) > 0):
                print(pieces[0])
            
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello world! :D</body></html>\r\n\r\n"

            clientSocket.sendall(data.encode())
            clientSocket.shutdown(SHUT_WR) 
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    
    serverSocket.close()

print("Access http://localhost:%s" % PORT)
createServer()
#####################################################################
#                                                                   #
#  This code creates a server to be housed locally on the testing   #
#       station (at the moment this would be the raspberry pi)      #
#                                                                   #
#####################################################################

## MAYBE TURN THIS INTO A CLASS THAT IS INSTANTIATED IN THIS FILE ##

# importing necessary modules
import time, zmq, json, sys, io
# Should contain imports for the test scripts
from GenResTest import GenResTest
# Creates a context class which contains the method to create a socket.
cxt = zmq.Context()
socket = cxt.socket(zmq.REP)

# Server-side for talking to a network point. "Bind"   ## socket.connect() is only used for CLIENTS
socket.bind("tcp://*:5555")

print ("Server has started.")
time.sleep(1)


try:
    # Sets up an infinite loop so the server is always on until a keyboard interrupt occurs
    while 1>0:
        #  Wait for next request from client
        # string = socket.recv_string().lower()
        print("Wating for request...")
        message = socket.recv_string().lower()
        print("Received request: %s " % message)

        # Testing to see what the request sent to the server was. The only requests we
        # care about are test1, test2, test3, & test4. Anything else will send back 
        # "invalid request" to the client.
        if message == "test1":
            print("Received request for test 1")

            # Switches the environment for print statements
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout

            # Simulates the test running
            test1 = GenResTest()
            test1.run_test()
            output = new_stdout.getvalue()
            output_byte_string = bytes(output,'UTF-8')

            try:
                for message in output:
                    try:
                        socket.send(output_byte_string)
                    except:
                        break
            except:
                pass
            
            # Switches back to the normal print environment
            sys.stdout = old_stdout

            # Test code to ensure json/text sending is working correctly
            try:
                socket.send(b"Unknown Error")
            except:
                pass

        elif message == "test2":
            print("Received request for test 2")

            # Simulates the test running
            # test2 = run_test2()
            # test2.run_test()
            time.sleep(3)

            # Test code to ensure json/text sending is working correctly
            current_JSON_file = open("./PythonFiles/utils/testingJSON.JSON")
            current_JSON_data = json.load(current_JSON_file)

            json_string = json.dumps(current_JSON_data)
            json_byte_string = bytes(json_string,'UTF-8')

            print(json_string)
        
            socket.send(json_byte_string)

        elif message == "test3":
            print("Received request for test 3")

            # Simulates the test running
            # test3 = run_test3()
            # test3.run_test()
            time.sleep(3)

            # Test code to ensure json/text sending is working correctly
            socket.send(b"Test Failed")

        elif message == "test4":
            print("Received request for test 4")

            # Simulates the test running
            # test4 = run_test4()
            # test4.run_test()
            time.sleep(3)

            # Test code to ensure json/text sending is working correctly
            current_JSON_file = open("./PythonFiles/utils/testingJSON.JSON")
            current_JSON_data = json.load(current_JSON_file)

            json_string = json.dumps(current_JSON_data)
            json_byte_string = bytes(json_string,'UTF-8')

            print(json_string)
        
            socket.send(json_byte_string)

        else:
            socket.send(b"Invalid request.")

# Keyboard interrupt with ZMQ has a bug when on BOTH Windows AND Python at the same time.
# This code should allow for CTRL + C interrupt for the server on any non-windows system.
except KeyboardInterrupt:
    print("Closing the server...")
    socket.close()
    cxt.term()
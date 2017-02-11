README-

1. As of now my server is spawing only one instance which is listening to any of the call from client if it is a valid connection on port 12348, and server returns the evaluated value of 'x' if a message in the format of '[func_name]<value>' is received from client, where func_name can be any func name defined, as in 'a' or 'B' or 'C' or 'D' or 'E'
2. Now the client is running a loop over the input file and sending requests to the server for evaluating different functions.
3. The setup can be easily done.
3.b The server should be run from console by 'python server.py' and client should be run by 'python client.py'. This is assuming the input file is present else it would throw an exception of file not present.
4. The input file should have name 'input.txt' and have first line as 'X = <value>' where <value> has the value of x
5. The next lines should have any valid mathematical expression, and it would be compiled as long as it is valid.
6. The output would be on the console, so when the client runs the input file it would display output in the format=
Expression = Output
Expression is the given mathematical expression and output is the calculated output.
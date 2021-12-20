
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|
|   REST add	| 3.10  	|  3.83 	| 270.31 	|
|   gRPC add	|  0.44 	|  0.72 	|  140.01  	|
|   REST rawimg	| 4.99  	|  23.22 	|  1156.73 	|
|   gRPC rawimg	| 5.76      |  6.19 	| 145.63  	|
|   REST dotproduct	| 3.61  	|   3.52	|  271.30	|
|   gRPC dotproduct	|  0.52 	|  0.68 	|  140.20  	|
|   REST jsonimg	|  36.33 	|  50.52	|   1280.23	|
|   gRPC jsonimg	|  23.36     | 26.8  	|  175.92 	|
|   PING        |  0.035     |  0.260    |   136    |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.

Reasons for difference in time between gRPC and REST
1) gRPC uses the same TCP session for all of its queries, while REST initiates a new TCP connection each time
2) REST uses HTTP/1.1 for transmission, while gRPC uses HTTP/2.0
3) The data representation format in gRPC is Protocol buffers, whereas in REST queries we use JSON. As discussed in class, JSON is slower than protocol buffers

Because of these reasons gRPC is generally faster than REST queries as we can see from the table above.

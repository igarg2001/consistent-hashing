# Consistent Hashing Implementation

This project provides implementations of consistent hashing in Java and Python. Consistent hashing is a technique used to distribute data across a cluster of servers in a way that minimizes the amount of data that needs to be redistributed when servers are added or removed. This is particularly useful in distributed systems where scalability and fault tolerance are important.

## Overview

The core idea behind consistent hashing is to map both the data and the servers to a circular ring. Each data item is then assigned to the nearest server in the ring. When a server is added or removed, only the data items that were previously assigned to that server need to be reassigned.

## Implementations

This project includes Java and Python implementations of consistent hashing.

### Java Implementation

The Java implementation uses a `TreeMap` to maintain a sorted ring of server hashes. The `MessageDigest` class is used to generate hash values for both servers and data items. The core class is `ConsistentHashing.java`.

#### Key Components:

*   **`ring`**: A `TreeMap<Long, String>` representing the hash ring.  It maps hash values to server names.
*   **`noOfReplicas`**:  An integer defining the number of virtual nodes per server.
*   **`md`**: A `MessageDigest` instance for generating MD5 hashes.
*   **`generateHash(String key)`**:  Generates a hash value for a given key using MD5.
*   **`addServer(String server)`**: Adds a server to the ring by creating virtual nodes.
*   **`removeServer(String server)`**: Removes a server from the ring by removing its virtual nodes.
*   **`getServerForRequest(String requestKey)`**:  Finds the server responsible for a given request key.

### Python Implementation

The Python implementation uses the `sortedcontainers` library to maintain a sorted ring of server hashes. The `hashlib` library is used to generate hash values for both servers and data items. The core class is `ConsistentHashing.py`.

#### Key Components:

*   **`ring`**: A `SortedDict` representing the hash ring. It maps hash values to server names.
*   **`n`**: An integer defining the number of virtual nodes per server.
*   **`hashfunc`**: A `hashlib.md5` instance for generating MD5 hashes.
*   **`_generateHash(self, key: str)`**: Generates a hash value for a given key using MD5.
*   **`add_server(self, server_name: str)`**: Adds a server to the ring by creating virtual nodes.
*   **`remove_server(self, server_name: str)`**: Removes a server from the ring by removing its virtual nodes.
*   **`get_server(self, key: str)`**: Returns the server to which the given key is mapped.

## Operations

The `ConsistentHashing` class (Java and Python) provides the following operations:

*   **Initialization**: Initializes the consistent hashing ring with a specified number of virtual nodes/replicas.
*   **Adding a Server**: Adds a server to the ring, creating virtual nodes to improve distribution.
*   **Removing a Server**: Removes a server from the ring, deleting its associated virtual nodes.
*   **Getting Server for a Key/Request**:  Determines and returns the server responsible for a given key or request.

## Details

*   **Virtual Nodes:** Both implementations use virtual nodes (controlled by the `n` parameter in the Python constructor and `noOfReplicas` in Java) to improve the distribution of data across the servers. Each server is represented by multiple virtual nodes in the ring, which helps to reduce the impact of adding or removing a server.
*   **Hash Function:** The Java implementation uses the `MD5` algorithm via `MessageDigest`. The Python implementation uses the `md5` hash function from the `hashlib` library. The hash function can be customized by modifying the relevant methods.
*   **Sorted Ring:** The Java implementation uses a `TreeMap` and the Python implementation uses a `SortedDict` data structure from the `sortedcontainers` library to maintain the sorted ring of server hashes. These data structures provide efficient lookup and insertion operations, which are crucial for the consistent hashing algorithm.

## Future Enhancements

*   **Customizable Hash Function:** Allow users to specify a custom hash function.
*   **Replication:** Add support for data replication to improve fault tolerance.
*   **Weighting:** Allow servers to have different weights, so that some servers can handle more data than others.

## How to Run
### Running the Java Implementation

To run the Java implementation, compile the `ConsistentHashing.java` file and then execute the compiled class file:

```bash
javac java/ConsistentHashing.java
java java/ConsistentHashing
```

### Running the Python Implementation

To run the Python implementation, execute the ConsistentHashing.py file using the Python interpreter:

```bash
python python/ConsistentHashing.py
```
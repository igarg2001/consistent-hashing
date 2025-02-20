from sortedcontainers import SortedDict, SortedList
import sys
import hashlib


class ConsistentHashing:
    def __init__(self, n: int) -> None:
        self.ring = SortedDict()
        self.n = n
        # self.hashfunc = ?
        self.hashfunc = hashlib.md5()

    def _generateHash(self, key: str) -> int:
        key = key.encode("utf-8")
        self.hashfunc.update(key)
        digest = self.hashfunc.hexdigest()
        digest = int(digest, 16)
        self.hashfunc = hashlib.md5()
        return digest

    def add_server(self, server_name: str) -> None:
        for i in range(0, self.n):
            hash_value = self._generateHash(f"{server_name}_{i}")
            # print(f"Server {server_name}_{i} has hash value {hash_value}")
            self.ring[hash_value] = server_name

    def remove_server(self, server_name: str) -> None:
        for i in range(0, self.n):
            hash_value = self._generateHash(f"{server_name}_{i}")
            if hash_value not in self.ring:
                raise Exception("Illegal operation: server not found")
            del self.ring[hash_value]

    def get_server(self, key: str) -> str:
        key_hash = self._generateHash(key)
        if key_hash in self.ring:
            return self.ring[key_hash]
        return (
            self.ring.peekitem(0)[1]
            if self.ring.bisect_left(key_hash) >= len(self.ring)
            else self.ring.peekitem(self.ring.bisect_left(key_hash))[1]
        )


if __name__ == "__main__":
    ch = ConsistentHashing(n=3)
    ch.add_server("100.203.106.231")
    ch.add_server("160.167.38.53")
    ch.add_server("59.230.24.125")

    # sys.exit(0)

    requests = ["166.191.137.39", "186.154.90.98"]

    for request in requests:
        print(
            f"Request with IP address {request} is mapped to server with IP address {ch.get_server(request)}"
        )

    new_ip = "94.134.173.185"

    print("Adding a server with IP : " + new_ip)

    ch.add_server(new_ip)

    for request in requests:
        print(
            f"Request with IP address {request} is mapped to server with IP address {ch.get_server(request)}"
        )

    print("Removing server: 160.167.38.53")
    ch.remove_server("160.167.38.53")

    for request in requests:
        print(
            f"Request with IP address {request} is mapped to server with IP address {ch.get_server(request)}"
        )

    print("Removing server: 100.203.106.231")
    ch.remove_server("100.203.106.231")

    for request in requests:
        print(
            f"Request with IP address {request} is mapped to server with IP address {ch.get_server(request)}"
        )

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.SortedMap;
import java.util.TreeMap;

public class ConsistentHashing {
    private final TreeMap<Long, String> ring;
    private final int noOfReplicas;
    private final MessageDigest md;

    ConsistentHashing(int noOfReplicas) throws NoSuchAlgorithmException {
        this.ring = new TreeMap<>();
        this.noOfReplicas = noOfReplicas;
        this.md = MessageDigest.getInstance("MD5");
    }

    public long generateHash(String key) {
        md.reset();
        byte[] bytes = key.getBytes();
        md.update(bytes);

        byte[] digest = md.digest();

        long hash = ((long) (digest[3] & 0xFF) << 24) |
                ((long) (digest[2] & 0xFF) << 16) |
                ((long) (digest[1] & 0xFF) << 8) |
                ((long) (digest[0] & 0xFF));
        return hash;
    }

    public void addServer(String server) {
        for (int i = 0; i < noOfReplicas; ++i) {
            long hash = generateHash(server + i);
            ring.put(hash, server);
        }
    }

    public void removeServer(String server) {
        for (int i = 0; i < noOfReplicas; ++i) {

            long hash = generateHash(server + i);
            ring.remove(hash);
        }
    }

    public String getServerForRequest(String requestKey) {
        if (ring.isEmpty())
            return null;

        long hash = generateHash(requestKey);

        if (!ring.containsKey(hash)) {
            SortedMap<Long, String> tailMap = ring.tailMap(hash);
            hash = tailMap.isEmpty() ? ring.firstKey() : tailMap.firstKey();
        }

        return ring.get(hash);
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        ConsistentHashing ch = new ConsistentHashing(3);
        // System.out.println(ch.generateHash("ishan"));
        ch.addServer("server1");
        ch.addServer("server2");
        ch.addServer("server3");

        System.out.println("req1: is present on server: " + ch.getServerForRequest("req1"));
        System.out.println("request1u9023u0: is present on server: " + ch.getServerForRequest("request1u9023u0"));

        ch.removeServer("server1");
        System.out.println("After removing server1");

        System.out.println("req1: is present on server: " + ch.getServerForRequest("req1"));
        System.out.println("request1u9023u0: is present on server: " + ch.getServerForRequest("request1u9023u0"));
    }

}
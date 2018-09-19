class HashNode<K, V> {
    public K key;
    public V value;
    public HashNode<K, V> next;

    public HashNode(K key, V value) {
        this.key = key;
        this.value = value;
    }
}

public class HashMapSeperateChaining<K, V> {
    private HashNode<K, V>[] bucketList;
    private int size;
    private int numBuckets;

    public HashMapSeperateChaining() {
        size = 0;
        numBuckets = 10;

        bucketList = new HashNode[numBuckets];
    }

    public int getBucketId(K key) {
        return Math.abs(key.hashCode() % numBuckets);
    }

    public int getSize() {
        return size;
    }

    public V get(K key) {
        HashNode<K, V> curBucket = bucketList[getBucketId(key)];
        while (curBucket != null) {
            if (curBucket.key == key) {
                return curBucket.value;
            }

            curBucket = curBucket.next;
        }

        return null;
    }

    public void put(K key, V value) {
        int bucketId = getBucketId(key);

        if (bucketList[bucketId] == null) {
            bucketList[bucketId] = new HashNode<>(key, value);
            return;
        }

        HashNode<K, V> curBucket = bucketList[bucketId];
        while (curBucket.next != null) {
            curBucket = curBucket.next;
        }

        curBucket.next = new HashNode<>(key, value);
    }
}

class Main {
    public static void main(String[] args) {
        HashMapSeperateChaining<String, String> map = new HashMapSeperateChaining<String, String>() {{
            put("name", "Aravind");
            put("designation", "Software Engineer");
        }};

        System.out.printf("%s is a %s", map.get("name"), map.get("designation"));
    }
}
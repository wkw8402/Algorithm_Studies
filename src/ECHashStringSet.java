import java.util.LinkedList;
import java.util.List;

/** A set of String values.
 *  @author Kyung-Wan Woo
 */
class ECHashStringSet implements StringSet {
    private final int MAX = 5;

    public ECHashStringSet() {
        _buckets = (LinkedList<String>[]) new LinkedList[MAX];
        _numElements = 0;
    }

    @Override
    public void put(String input) {
        if (MAX < _numElements / _buckets.length ) {
            resize();
        }
        if (_buckets[where(input)] == null) {
            _buckets[where(input)] = new LinkedList<String>();
        }
        _buckets[where(input)].add(input);
        _numElements++;
    }

    private void resize() {
        LinkedList<String> [] resized = new LinkedList[_buckets.length * 2];
        LinkedList<String> [] tmp = _buckets;
        _buckets = resized;
        _numElements = 0;

        for (LinkedList<String> bucket : tmp) {
            if (bucket != null) {
                for (String s : bucket) {
                    this.put(s);
                }
            }
        }
    }

    @Override
    public boolean contains(String input) {
        if (_buckets[where(input)] != null) {
            return _buckets[where(input)].contains(input);
        }
        return false;
    }

    @Override
    public List<String> asList() {
        LinkedList<String> lst = new LinkedList<String>();
        for (int i = 0; i < _numElements; i++) {
            if (_buckets[i] != null) {
                for (String elem : _buckets[i]) {
                    lst.add(elem);
                }
            }
        }
        return lst;
    }

    private int where(String input) {
        int last = 1 & input.hashCode();
        int hash = last | input.hashCode() >>> 1;

        return hash % _buckets.length;
    }

    private LinkedList<String> [] _buckets;
    private int _numElements;
}

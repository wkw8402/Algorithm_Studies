import org.checkerframework.checker.units.qual.A;

import java.util.Iterator;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Stack;

/**
 * Implementation of a BST based String Set.
 * @author Kyung-Wan Woo
 */
public class BSTStringSet implements StringSet, Iterable<String> {
    /** Creates a new empty set. */
    public BSTStringSet() {
        _root = null;
    }

    @Override
    public void put(String s) {
        Node place = where(s);
        if (place == null) {
            _root = new Node(s);
        } else {
            if (place.s.compareTo(s) > 0) {
                place.left = new Node(s);
            } else if (place.s.compareTo(s) < 0) {
                place.right = new Node(s);
            }
        }
    }

    @Override
    public boolean contains(String s) {
        Node place = where(s);
        if (place != null) {
            return place.s.equals(s);
        }
        return false;
    }

    @Override
    public List<String> asList() {
        ArrayList<String> lst = new ArrayList<String>();
        for (String str: this) {
            lst.add(str);
        }
        return lst;
    }

    /**
     * Helper method to return the most
     * suitable place for the input String
     * @param s input String
     */
    public Node where(String s) {
        if (_root == null) {
            return null;
        }
        Node now = _root;
        while (true) {
            Node next = null;
            if (now.s.compareTo(s) > 0) {
                next = now.left;
            } else if (now.s.compareTo(s) < 0) {
                next = now.right;
            }
            if (next == null) {
                return now;
            } else {
                now = next;
            }
        }
    }


    /** Represents a single Node of the tree. */
    private static class Node {
        /** String stored in this Node. */
        private String s;
        /** Left child of this Node. */
        private Node left;
        /** Right child of this Node. */
        private Node right;

        /** Creates a Node containing SP. */
        Node(String sp) {
            s = sp;
        }
    }

    /** An iterator over BSTs. */
    private static class BSTIterator implements Iterator<String> {
        /** Stack of nodes to be delivered.  The values to be delivered
         *  are (a) the label of the top of the stack, then (b)
         *  the labels of the right child of the top of the stack inorder,
         *  then (c) the nodes in the rest of the stack (i.e., the result
         *  of recursively applying this rule to the result of popping
         *  the stack. */
        private Stack<Node> _toDo = new Stack<>();

        /** A new iterator over the labels in NODE. */
        BSTIterator(Node node) {
            addTree(node);
        }

        @Override
        public boolean hasNext() {
            return !_toDo.empty();
        }

        @Override
        public String next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }

            Node node = _toDo.pop();
            addTree(node.right);
            return node.s;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }

        /** Add the relevant subtrees of the tree rooted at NODE. */
        private void addTree(Node node) {
            while (node != null) {
                _toDo.push(node);
                node = node.left;
            }
        }
    }

    @Override
    public Iterator<String> iterator() {
        return new BSTIterator(_root);
    }

    // FIXME: UNCOMMENT THE NEXT LINE FOR PART B
    // @Override
    public Iterator<String> iterator(String low, String high) {
        return null;  // FIXME: PART B (OPTIONAL)
    }


    /** Root node of the tree. */
    private Node _root;
}

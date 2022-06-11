import java.util.Arrays;

/**
 * Note that every sorting algorithm takes in an argument k. The sorting 
 * algorithm should sort the array from index 0 to k. This argument could
 * be useful for some of your sorts.
 *
 * Class containing all the sorting algorithms from 61B to date.
 *
 * You may add any number instance variables and instance methods
 * to your Sorting Algorithm classes.
 *
 * You may also override the empty no-argument constructor, but please
 * only use the no-argument constructor for each of the Sorting
 * Algorithms, as that is what will be used for testing.
 *
 * Feel free to use any resources out there to write each sort,
 * including existing implementations on the web or from DSIJ.
 *
 * All implementations except Counting Sort adopted from Algorithms,
 * a textbook by Kevin Wayne and Bob Sedgewick. Their code does not
 * obey our style conventions.
 */
public class MySortingAlgorithms {

    /**
     * Java's Sorting Algorithm. Java uses Quicksort for ints.
     */
    public static class JavaSort implements SortingAlgorithm {
        @Override
        public void sort(int[] array, int k) {
            Arrays.sort(array, 0, k);
        }

        @Override
        public String toString() {
            return "Built-In Sort (uses quicksort for ints)";
        }
    }

    /** Insertion sorts the provided data. */
    public static class InsertionSort implements SortingAlgorithm {
        @Override
        public void sort(int[] array, int k) {
            for (int i = 0; i < k; i++) {
                for (int j = i; j > 0; j--) {
                    if (array[j] < array[j - 1]) {
                        int tmp = array[j];
                        array[j] = array[j - 1];
                        array[j - 1] = tmp;
                    }
                }
            }
        }

        @Override
        public String toString() {
            return "Insertion Sort";
        }
    }

    /**
     * Selection Sort for small K should be more efficient
     * than for larger K. You do not need to use a heap,
     * though if you want an extra challenge, feel free to
     * implement a heap based selection sort (i.e. heapsort).
     */
    public static class SelectionSort implements SortingAlgorithm {
        @Override
        public void sort(int[] array, int k) {
            for (int i = 0; i < k; i++) {
                int min = i;
                for (int j = i; j < k; j++) {
                    if (array[j] < array[min]) {
                        min = j;
                    }
                }
                int tmp = array[i];
                array[i] = array[min];
                array[min] = tmp;
            }
        }

        @Override
        public String toString() {
            return "Selection Sort";
        }
    }

    /** Your mergesort implementation. An iterative merge
      * method is easier to write than a recursive merge method.
      * Note: I'm only talking about the merge operation here,
      * not the entire algorithm, which is easier to do recursively.
      */
    public static class MergeSort implements SortingAlgorithm {
        @Override
        public void sort(int[] array, int k) {
            int[] result = mergeSort(array, k);
            System.arraycopy(result, 0, array, 0, k);
        }

        private int[] mergeSort(int[] array, int k){
            if (array.length == 0 | array.length == 1) {
                return array;
            }
            int[] left = new int[k / 2];

            int[] right;
            if (k % 2 == 0) {
                right = new int[k / 2];
            } else {
                right = new int[k / 2 + 1];
            }

            for (int i = 0; i < k/2; i++) {
                left[i] = array[i];
            }
            for (int j = k/2; j < k; j++) {
                right[j - k/2] = array[j];
            }

            left = mergeSort(left, left.length);
            right = mergeSort(right, right.length);

            return merge(left, right);
        }

        private int[] merge(int[] left, int[] right) {
            int[] result = new int[left.length + right.length];
            int index = 0;
            int l = 0;
            int r = 0;
            while (index < result.length) {
                if (l >= left.length && r < right.length) {
                    result[index] = right[r];
                    r++;
                } else if (r >= right.length && l < left.length) {
                    result[index] = left[l];
                    l++;
                } else if (left[l] <= right[r]) {
                    result[index] = left[l];
                    l++;
                } else {
                    result[index] = right[r];
                    r++;
                }
                index++;
            }
            return result;
        }

        @Override
        public String toString() {
            return "Merge Sort";
        }
    }

    /**
     * Your Counting Sort implementation.
     * You should create a count array that is the
     * same size as the value of the max digit in the array.
     */
    public static class CountingSort implements SortingAlgorithm {
        @Override
        public void sort(int[] array, int k) {

        }

        // may want to add additional methods

        @Override
        public String toString() {
            return "Counting Sort";
        }
    }

    /** Your Heapsort implementation.
     */
    public static class HeapSort implements SortingAlgorithm {
        @Override
        public void sort(int[] array, int k) {
            // FIXME
        }

        @Override
        public String toString() {
            return "Heap Sort";
        }
    }

    /** Your Quicksort implementation.
     */
    public static class QuickSort implements SortingAlgorithm {
        @Override
        public void sort(int[] array, int k) {
            // FIXME
        }

        @Override
        public String toString() {
            return "Quicksort";
        }
    }

    /* For radix sorts, treat the integers as strings of x-bit numbers.  For
     * example, if you take x to be 2, then the least significant digit of
     * 25 (= 11001 in binary) would be 1 (01), the next least would be 2 (10)
     * and the third least would be 1.  The rest would be 0.  You can even take
     * x to be 1 and sort one bit at a time.  It might be interesting to see
     * how the times compare for various values of x. */

    /**
     * LSD Sort implementation.
     */
    public static class LSDSort implements SortingAlgorithm {
        @Override
        public void sort(int[] a, int k) {
            int max = 0;
            for (int i = 1; i < k; i++) {
                if (a[i] > a[max]) {
                    max = i;
                }
            }

            int test = a[max];
            int num = 1;
            while (test > 0) {
                test /= 10;
                num++;
            }

            for (int p = 1; p < num; p++) {
                int[] count = new int[10];
                for (int q = 0; q < k; q++) {
                    if (p == 1) {
                        count[a[q] % 10]++;
                    } else {
                        count[(int) ((a[q] / (Math.pow(10, p - 1))) % 10)]++;
                    }
                }
                int[] place = new int[10];
                place[0] = 0;
                for (int w = 1; w < 10; w++) {
                    place[w] = place[w - 1] + count[w - 1];
                }
                int[] result = new int[k];
                for (int r = 0; r < k; r++) {
                    if (p == 1) {
                        result[place[a[r] % 10]] = a[r];
                        place[a[r] % 10]++;
                    } else {
                        result[place[(int) ((a[r] / (Math.pow(10, p - 1))) % 10)]] = a[r];
                        place[(int) ((a[r] / (Math.pow(10, p - 1))) % 10)]++;
                    }
                }
                System.arraycopy(result, 0, a, 0, k);
            }
        }

        @Override
        public String toString() {
            return "LSD Sort";
        }
    }

    /**
     * MSD Sort implementation.
     */
    public static class MSDSort implements SortingAlgorithm {
        @Override
        public void sort(int[] a, int k) {
            // FIXME
        }

        @Override
        public String toString() {
            return "MSD Sort";
        }
    }

    /** Exchange A[I] and A[J]. */
    private static void swap(int[] a, int i, int j) {
        int swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

}

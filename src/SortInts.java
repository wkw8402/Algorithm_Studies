import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

/** HW #7, Distribution counting for large numbers.
 *  @author Kyung-Wan Woo
 */
public class SortInts {

    /** Sort A into ascending order.  Assumes that 0 <= A[i] < n*n for all
     *  i, and that the A[i] are distinct. */
    static void sort(long[] A) {
        if (A.length == 0) {
            return;
        }
        LSDsort(A, A.length);
    }

    private static void LSDsort(long[] a, int k) {
        for (int p = 0; p < 2; p++) {
            long[] result = new long[k];
            int[] count = new int[k];
            int[] place = new int[k];
            for (int q = 0; q < k; q++) {
                count[(int) ((a[q] / (Math.pow(k, p))) % k)]++;
            }
            for (int u = 1; u < k; u++) {
                place[u] = place[u-1] + count[u-1];
            }
            for (int t = 0; t < k; t++) {
                result[place[(int) ((a[t] / (Math.pow(k, p))) % k)]] = a[t];
                place[(int) ((a[t] / (Math.pow(k, p))) % k)]++;
            }
            System.arraycopy(result, 0, a, 0, k);
        }
    }

    /** Test intervals. */
    static final long[] ints = {14, 13, 6, 23, 9};
    /** Covered length of INTERVALS. */
    static final long[] CORRECT = {6, 9, 13, 14, 23};

    /** Performs a basic functionality test on the coveredLength method. */
    @Test
    public void basicTest() {
        sort(ints);
        assertArrayEquals(CORRECT, ints);
    }

    /** Runs provided JUnit test. ARGS is ignored. */
    public static void main(String[] args) {
        System.exit(ucb.junit.textui.runClasses(Intervals.class));
    }

}


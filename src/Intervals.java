import org.junit.Test;
import static org.junit.Assert.*;

import java.util.*;

/** HW #7, Sorting ranges.
 *  @author Kyung-Wan Woo
  */
public class Intervals {
    /** Assuming that INTERVALS contains two-element arrays of integers,
     *  <x,y> with x <= y, representing intervals of ints, this returns the
     *  total length covered by the union of the intervals. */
    public static int coveredLength(List<int[]> intervals) {
        if (intervals.size() == 0) {
            return 0;
        }

        Collections.sort(intervals, new SortStart());

        int begin = intervals.get(0)[0];
        int end = intervals.get(0)[1];
        int totalCover = 0;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals.get(i)[0] >= end | intervals.get(i)[1] <= begin) {
                totalCover = totalCover + (end - begin);
                begin = intervals.get(i)[0];
                end = intervals.get(i)[1];
            } else if (intervals.get(i)[0] < begin &&  intervals.get(i)[1] <= end){
                begin =  intervals.get(i)[0];
            } else if ( intervals.get(i)[0] >= begin &&  intervals.get(i)[1] > end) {
                end =  intervals.get(i)[1];
            }
        }
        totalCover = totalCover + (end - begin);
        return totalCover;
    }

    /** Test intervals. */
    static final int[][] INTERVALS = {
        {19, 30},  {8, 15}, {3, 10}, {6, 12}, {4, 5},
    };

    static final int[][] INTERVALS2 = {
        {2, 3}, {4, 5}, {7, 8}, {2, 99}, {23, 46}, {34, 43}, {23, 28}
    };

    //one interval that encompasses the set of interval, the last/first interval different cases of overlapping

    /** Covered length of INTERVALS. */
    static final int CORRECT = 23;
    static final int CORRECT2 = 97;

    /** Performs a basic functionality test on the coveredLength method. */
    @Test
    public void basicTest() {
        assertEquals(CORRECT, coveredLength(Arrays.asList(INTERVALS)));
        assertEquals(CORRECT2, coveredLength(Arrays.asList(INTERVALS2)));
    }

    /** Runs provided JUnit test. ARGS is ignored. */
    public static void main(String[] args) {
        System.exit(ucb.junit.textui.runClasses(Intervals.class));
    }

}

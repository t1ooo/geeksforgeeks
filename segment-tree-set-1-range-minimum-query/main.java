
// Driver Code
import java.util.*;
import java.lang.*;

class Minimum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            sc.next();
            int n = sc.nextInt();
            int arr[] = new int[n];

            for (int i = 0; i < n; i++)
                arr[i] = sc.nextInt();

            GfG gfg = new GfG();
            int Q = sc.nextInt();

            int st[] = gfg.constructST(arr, n);
            int l, r;
            for (int i = 0; i < Q; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                l = Math.min(a, b);
                r = Math.max(a, b);
                System.out.print(gfg.RMQ(st, n, l, r) + " ");
            }
            System.out.println();
        }
    }
}

class GfG {
    int st[];

    int minVal(int x, int y) {
        return (x < y) ? x : y;
    }

    int getMid(int s, int e) {
        return s + (e - s) / 2;
    }

    int RMQUtil(int ss, int se, int qs, int qe, int index) {
        if (qs <= ss && qe >= se)
            return st[index];

        if (se < qs || ss > qe)
            return Integer.MAX_VALUE;

        int mid = getMid(ss, se);
        return minVal(RMQUtil(ss, mid, qs, qe, 2 * index + 1), RMQUtil(mid + 1, se, qs, qe, 2 * index + 2));
    }

    public int RMQ(int[] st, int n, int qs, int qe) {
        if (qs < 0 || qe > n - 1 || qs > qe) {
            System.out.println("Invalid Input");
            return -1;
        }

        return RMQUtil(0, n - 1, qs, qe, 0);
    }

    int constructSTUtil(int[] arr, int ss, int se, int si) {
        if (ss == se) {
            st[si] = arr[ss];
            return arr[ss];
        }

        int mid = getMid(ss, se);
        st[si] = minVal(constructSTUtil(arr, ss, mid, si * 2 + 1), constructSTUtil(arr, mid + 1, se, si * 2 + 2));
        return st[si];
    }

    public int[] constructST(int[] arr, int n) {
        int x = (int) (Math.ceil(Math.log(n) / Math.log(2)));

        int max_size = 2 * (int) Math.pow(2, x) - 1;
        st = new int[max_size];

        constructSTUtil(arr, 0, n - 1, 0);
        return st;
    }
}

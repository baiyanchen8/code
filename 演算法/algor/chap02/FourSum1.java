public class FourSum1 {
    // print distinct 4-tuples (i, j, k, l) such that a[i] + a[j] + a[k] + a[l] = 0
    public static void printAll(long[] a) {
        int n = a.length;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                for (int k = j+1; k < n; k++) {
                    for (int l = k+1; l < n; l++) {
                        if (a[i] + a[j] + a[k] + a[l] == 0) {
                            System.out.println(a[i] + " " + a[j] + " " + a[k] + " " + a[l]);
                        }
                    }
                }
            }
        }
    }

    // return number of distinct 4-tuples (i, j, k, l) such that a[i] + a[j] + a[k] + a[l] = 0
    public static int count(long[] a) {
        int n = a.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                for (int k = j+1; k < n; k++) {
                    for (int l = k+1; l < n; l++) {
                        if (a[i] + a[j] + a[k] + a[l] == 0) {
                            count++;
                        }
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args)  {
        long[] a={-6,-5,-4,-1,0,1,2,3,5,6} ;
        int count = count(a);
        System.out.println(count);
    }
}

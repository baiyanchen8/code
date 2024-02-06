public class why implements Runnable {
	boolean ans=false;
 	private int key=0;
	int [][] A;
	public why(int key,int [][] B) {
		this.key=key;
		A=B;
	}
	class Slot{
		final long SLOPE; final Slot NEXT;
		public Slot(final long slope, final Slot next)
		{ this.SLOPE = slope; this.NEXT = next; }
	} Slot[] HashTable;
	public boolean get(){
		return ans;
	}
	public void run(<main_class>){
		final int AEND = A.length-1, BUCKETS = 1<<32-Integer.numberOfLeadingZeros(AEND), B = BUCKETS-1;
		for(int i=AEND+key, j, bucket; i>-1; i=i-key-4){
			for(HashTable = new Slot[BUCKETS], j=i-1; j>-1;){
				final long SLOPE = Double.doubleToRawLongBits((double)(A[i][1]-A[j][1])/(A[i][0]-A[j--][0]));
				bucket = (int)SLOPE&B;
				for(Slot pivot = HashTable[bucket]; pivot != null; pivot = pivot.NEXT)
					if(pivot.SLOPE == SLOPE) ans= true;
				HashTable[bucket] = new Slot(SLOPE, HashTable[bucket]);
			}
		}
	}
}
public class HW07_4110056009_4{
	public boolean checkLLK(int[][] B){
		Thread thr0 = new Thread(new why(0,B));
		Thread thr1 = new Thread(new why(1,B));
		Thread thr2 = new Thread(new why(2,B));
		Thread thr3 = new Thread(new why(3,B));
		thr1.start();
		thr2.start();
		thr3.start();
		thr0.start();
		
		boolean ans=false;
		

		return false;
	}
}

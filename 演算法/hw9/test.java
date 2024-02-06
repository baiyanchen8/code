
import java.util.ArrayList;
public class test extends LSD{

	public static void main(String[] args) {
		test A=new test();
		int[][] a= {{0,1},{0,2},{0,4},{1,3},{1,4},{2,5},{6,7}}; 

		System.out.println(A.Distance(a));
		
	}

	int q[]=new int[999999];
	int fir=-1;
	int top=0;
	public int Distance(int[][] array) {
		int i;
		int len=array.length;
		int big=0;
		for(i=0;i<len;i++)
		{
			if(array[i][0]>big)
				big=array[i][0];
			if(array[i][1]>big)
				big=array[i][1];
		}
		big=big+2;
		ArrayList<Integer>[] map=new ArrayList[big];
		
		for(i=0;i<big;i++)
		{
			map[i]=new ArrayList<Integer>();
		}
		
		for(i=0;i<len;i++)
		{
			if(!(map[array[i][0]].contains(array[i][1])));
				map[array[i][0]].add((array[i][1]));
			if(!(map[array[i][1]].contains(array[i][0])));
				map[array[i][1]].add((array[i][0]));
		}
		int cou=0;
		
		
		int c[]=new int[big];
		int dis[]=new int[big];
		push(array[0][0]);
		c[array[0][0]]=1;
		
		int now=0;
		dis[array[0][0]]=0;
		while(fir!=top-1)
		{
			now=pop();
			cou=map[now].size();
			for(i=0;i<cou;i++)
			{
				map[now].get(i);
				if(c[map[now].get(i)]<=0)
				{
					c[map[now].get(i)]+=1;
					push(map[now].get(i));
					dis[map[now].get(i)]=dis[now]+1;
			    }
			}		
			
		}
		top=0;fir=-1;
		push(now);
		dis[now]=0;
		while(fir!=top-1)
		{
			now=pop();
			cou=map[now].size();
			for(i=0;i<cou;i++)
			{
				map[now].get(i);
				if(c[map[now].get(i)]<=1)
				{
					c[map[now].get(i)]+=1;
					push(map[now].get(i));
					dis[map[now].get(i)]=dis[now]+1;
			    }
			}		
		}
		return dis[now]+2-1;
	}
	void push(int a)
	{
		q[top]=a;
		top++;
	}
	int pop()
	{
		fir++;
		int t=q[fir];
		
		return t;
	}
	
}
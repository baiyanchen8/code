public class HW10_4110056009_01 extends Buy_Phone{
    
    public int[][] bestPhone(int[][] inputArr) {
        int n =inputArr.length;
        int mark[]=new int [n];
        int sum=0;
        for(int i=0;i<n;i++){
            if(mark[i]==1){
                continue;
            }
            for (int j=i+1;j<n;j++){
                if(inputArr[i][0]>=inputArr[j][0]&&inputArr[i][1]>=inputArr[j][1]){
                    mark[j]=1;
                }  
                if(inputArr[i][0]<=inputArr[j][0]&&inputArr[i][1]<=inputArr[j][1]){
                    mark[i]=1;
                }
            }
        }
        for (int i : mark) {
            if(i==0){
                sum++;
            }
        }
        int ans[][]=new int [sum][]; 
        sum=0;
        for (int i=0;i<n;i++){
            if(mark[i]==0){
                ans[sum++]=inputArr[i];
            }
        }
        
        return ans;
    }


}
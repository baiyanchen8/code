public class help {
    
public boolean[] one0k(String[] str) {
		
    boolean[] result = new boolean[str.length];
    int i = 0, j = 0, num0 = 0, num1 = 0;
    boolean flag = true;
    
    for (i = 0; i < str.length; i++) {
        num0=0;num1=0;flag=true;
        for (j = 0; j < str[i].length(); j++) {
            if (str[i].charAt(j) == '0') {
                if (num1 > 0) {
                    flag = false;
                    break;
                }
                num0++;
            } else if (str[i].charAt(j) == '1') {
                num1++;
            }
        }
        if (num0 == num1) {
            result[i] = flag;
        } else {
            result[i] = false;
        }
    }
    return result;
}
}

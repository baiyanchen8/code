import java.util.Random;

public class RandomStringGenerator {
    public static String[] generateRandomString( int length) {
        Random rand = new Random();
        Random rand1 = new Random();
        String[] sb = new String[length];
        for (int i = 0; i < length; i++) {
            int bit = rand.nextInt(10)+1;
            StringBuilder aa = new StringBuilder();
            for(int j =0;j<bit;j++){
                int kit=rand1.nextInt(2);
                aa.append(kit);
            }
            sb[i]=aa.toString();
        }
        
        return sb;
    }
    
    
}
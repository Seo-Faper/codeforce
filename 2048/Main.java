import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] D = sc.nextLine().split(" ");
        
        Arrays.sort(D);
        // System.out.println(Arrays.toString(D));
        if (D[0].equals(D[1]) && D[0].equals(D[2])) {
            System.out.println(10000 + Integer.parseInt(D[0]) * 1000);
        } else if (D[0].equals(D[1])) {
            System.out.println(1000 + Integer.parseInt(D[0]) * 100);
        } else if (D[1].equals(D[2])) {
            System.out.println(1000 + Integer.parseInt(D[1]) * 100);
        } else {
            System.out.println(Integer.parseInt(D[2]) * 100);
        }
    }
}

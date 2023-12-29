import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        String[][] board = new String[N][M];
        for (int i = 0; i < N; i++) {
            String[] input = sc.nextLine().split(" ");
            for (int j = 0; j < M; j++) {
                board[i][j] = input[j];
            }
        }
        show(board);
    }

    public static void show(String[][] b) {
        for (int i = 0; i < b.length; i++) {
            for (int j = 0; j < b[i].length; j++) {
                System.out.print(b[i][j] + " ");
            }
            System.out.println();
        }
    }

}

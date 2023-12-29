package codeforce;

import java.util.Scanner;

public class BOJ_1059 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int L = sc.nextInt();
		int[] arr = new int[L];
		for(int i = 0; i<L; i++) {
			arr[i] = sc.nextInt();
		}
		int n = sc.nextInt();
		int x = 0;
		for(int i = 0; i<L; i++) {
			if(arr[i]==n) {
				System.out.println(0);
				System.exit(-1);
			}
			if(arr[i] < n && x < arr[i]) x = arr[i];
		}
		
		int y = 1001;
		for(int i = 0; i<L; i++) {
			if(arr[i] > n && y > arr[i]) y = arr[i];
		}
		x++;
		y--;
		System.out.println((n-x)*(y-n+1)+(y-n));	
	}
}

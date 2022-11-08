package codeforce;

import java.util.Scanner;

public class BOJ_1105 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String[] LR = sc.nextLine().split(" ");
		String L = LR[0];
		String R = LR[1];
		int a = L.length();
		int b = R.length();
		//System.out.println(a+","+b);

		if(a != b) System.out.println(0);
		else {
			int ans = 0;
			for(int i =0; i<a; i++) {
				if(L.charAt(i) == R.charAt(i)) {
					if(L.charAt(i)=='8') ans++;
				}else {
					break;
				}
				
			}
			System.out.println(ans);
		}
		
	}
}

package codeforce;

import java.util.Scanner;

public class BOJ_1058 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String[] friends = new String[n];
		sc.nextLine();
		for(int i = 0; i < n; i++) {
			friends[i] = sc.nextLine();
		}
		int answer = 0;
		for(int i = 0; i < n; i++) {
			int count = 0;
			for(int j = 0; j < n; j++) {
				if(i==j) continue;
				if(friends[i].charAt(j) == 'Y') {
					count++;
				}else {
					for(int k = 0; k<n; k++) {
						if(friends[j].charAt(k) == 'Y' && friends[k].charAt(i) == 'Y') {
							count++;
							break;
						}
					}
				}
			}
			answer = Math.max(answer, count);
		}
		System.out.println(answer);
	}

}

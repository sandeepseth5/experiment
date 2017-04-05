package interview.main;

import java.util.Scanner;

import com.datastructure.suffixtree.SuffixTree;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter the text: ");
		String s = sc.nextLine();
		//System.out.println(s);
		SuffixTree sfTree = new SuffixTree(s);
		System.out.print("Enter the string to search: ");
		String patt = sc.nextLine();
		
		System.out.println(sfTree.search(patt));
		sc.close();
	}
}

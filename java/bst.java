import java.util.*;

class Node {
	int value;
	public Node left,right;
	
	public Node(int value) {
		this.value=value;
		this.left=this.right=null;
	}
}
class BSTree {
	Node root;
	public BSTree() {
		root=null;
	}
	public void inOrder_(Node root) {
		if(root!=null) {
			inOrder_(root.left);
		
			System.out.print(root.value+"\t");
		
			inOrder_(root.right);
		}
	}
	public void inOrder() {
		inOrder_(root);
	}
	public void insert_(Node root,int value) {
		if(value < root.value) {
				if(root.left==null)
					root.left=new Node(value);
				else
					insert_(root.left,value);
		}
		else {
				if(root.right==null)
					root.right=new Node(value);
				else
					insert_(root.right,value);
		}
	}
	public void insert(int value) {
		if(root!=null) {
			insert_(root, value);
		}
		else {
			root=new Node(value);
		}
	}
	public static int[] randomArray(int n) {
		int[] ret=new int[n];
		
		for(int i=0;i<n;i++) {
			ret[i]=(int)(Math.random() * 10000);
		}
		return ret;
	}
	public static void main(String[] args) {
		BSTree bst=new BSTree();
		int[] a=randomArray(1000000000);
		for(int x: a) {
			bst.insert(x);
		}
		bst.inOrder();
	}
}

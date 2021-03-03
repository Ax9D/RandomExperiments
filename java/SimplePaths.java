import java.util.*;
public class SimplePaths {

	public static int findPaths(ArrayList<Integer>[] edges) {
		HashSet<Integer> visited=new HashSet<Integer>();
		Queue<Integer> toVisit=new LinkedList<Integer>();
		
		toVisit.add(1);
		int total=0;
		int current;
		while(!toVisit.isEmpty()){
			current=toVisit.poll();
			
			visited.add(current);	
			
			int unvisited=0;
			
			for(int vertex: edges[current]) {
				if(!visited.contains(vertex))
				{
					unvisited++;
					toVisit.offer(vertex);
				}
			}
			int nEdges=edges[current].size();
			total= nEdges + total * nEdges * unvisited;
		}
		return total;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		int t=sc.nextInt();
		for(int i=0;i<t;i++) {
			int n=sc.nextInt();
			var graph=new ArrayList<Integer>[ n+1 ];
			
			for(int j=0;j<n;j++)
				graph[j]=new ArrayList<Integer>();
				
			for(int j=0;j<n;j++)
				graph[sc.nextInt()].add(sc.nextInt());
			System.out.println(findPaths(graph));
		}
	}
}

import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
class Box
{
	int r,c;
	int dist;
	public Box(int r,int c,int dist)
	{
		this.r=r;
		this.c=c;
		this.dist=dist;
	}
}
class Solution{

	public static boolean inMaze(int r,int c,int h,int w)
	{
		return !(r<0 || r>=h || c<0 || c>=w);
	}
	public static int shortest(int[][] map)
	{
		int h=map.length;
		int w=map[0].length;
		
		int r,c;
		Queue<Box> toVisit=new LinkedList<Box>();
		toVisit.add(new Box(0,0,1));
		map[0][0]=-1;
				
		while(!toVisit.isEmpty())
		{
		
			Box current=toVisit.remove();
			r=current.r;
			c=current.c;
			//System.out.println("Visiting ("+r+","+c+")");
			if(r==h-1 && c==w-1) //If reached end
				return current.dist;
			
			//Check neighbors
			//LEFT
			if(inMaze(r,c-1,h,w) && map[r][c-1]!=1 && map[r][c-1]!=-1)
			{
				toVisit.add(new Box(r,c-1,current.dist+1));
				map[r][c-1]=-1;
			}
			//RIGHT
			if(inMaze(r,c+1,h,w) && map[r][c+1]!=1 && map[r][c+1]!=-1)
			{
				toVisit.add(new Box(r,c+1,current.dist+1));
				map[r][c+1]=-1;
			}
			//UP
			if(inMaze(r-1,c,h,w) && map[r-1][c]!=1 && map[r-1][c]!=-1)
			{
				toVisit.add(new Box(r-1,c,current.dist+1));
				map[r-1][c]=-1;
			}
			//DOWN
			if(inMaze(r+1,c,h,w) && map[r+1][c]!=1 && map[r+1][c]!=-1)
			{
				toVisit.add(new Box(r+1,c,current.dist+1));
				map[r+1][c]=-1;
			}
			
		}
		return Integer.MAX_VALUE ;//Should never happen
	}
	public static void createCopy(int[][] map,int[][] copy)
	{
		for(int i=0;i<map.length;i++)
		{
			for(int j=0;j<map[0].length;j++)
				copy[i][j]=map[i][j];
		}
	}
	public static int solution(int[][] map)
	{
		int[][] copy=new int[map.length][map[0].length];
		ArrayList<Integer> distances=new ArrayList<Integer>();
		createCopy(map,copy);
		distances.add(shortest(copy));
		for(int i=0;i<map.length;i++)
		{
			for(int j=0;j<map[0].length;j++)
			{
				if(map[i][j]==1)
				{	
					createCopy(map,copy);
					copy[i][j]=0;
					distances.add(shortest(copy));
				}
			}
		}
		int min=map.length*map[0].length;
		for(int x:distances)
		{
			if(x<min)
				min=x;
		}
		System.out.println(distances);
		return min;	
	}
	
	public static int[][] testMap()
	{
		int[][] ret=new int[20][20];
		for(int i=0;i<20;i++)
		{
			for(int j=0;j<20;j++)
			{
				ret[i][j]=0;
			}
		}
		return ret;
	}
	public static void main(String[] args)
	{
		int[][] map1=new int[][]{{0,1,1,0},{0,0,0,1},{1,1,0,0},{1,1,1,0}};
		int[][] map2=new int[][]{{0,0,0,0,0,0},{1,0,1,1,1,0},{0,0,0,0,0,0},{0,1,1,1,1,1},{0,1,1,1,1,1},{0,0,0,0,0,0}};
		int[][] map3=testMap();
		int[][] map4=new int[][]{{0,1,1,1,0,0},
								 {0,1,0,0,0,0},
								 {0,0,0,1,1,0},
								 {1,1,1,1,0,0},
								 {1,0,0,0,0,0}};
		int[][] map5=new int[][]{{0,0,0},{1,1,1},{0,0,0}};
		System.out.println(solution(map5));
	}
}

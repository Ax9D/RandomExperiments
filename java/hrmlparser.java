import java.util.*;

class Tag
{
	HashMap<String,String> nvpairs;
	HashMap<String,Tag> childTags;
	public Tag()
	{
		nvpairs=new HashMap<String,String>();
		childTags=new HashMap<String,Tag>();
	}
	public void addTag(String tname,Tag t)
	{
		childTags.put(tname,t);
	}
}
class HRMLParser
{
	Tag root;
	Stack<Tag> tagStack;

	public HRMLParser()
	{
		root=new Tag();
		tagStack=new Stack<Tag>();
		tagStack.push(root);
	}
	public void parseLine(String line)
	{
		//Format --> <tagName attribute1 = "val1" attribute2 = "val2" etc.>

		line=line.substring(1,line.length()-1); //Strip < >

		if(line.charAt(0)!='/')//If starting tag
		{
			int firstSpace=line.indexOf(" ");
			String tagName;
			Tag newTag=new Tag();
			if(firstSpace>0)
			{
				tagName=line.substring(0,firstSpace);

				line+=" ";
				String[] nvs=line.substring(firstSpace+1,line.length()).split("\" ");

				String name,value;
				
				String[] pair;

				for(int i=0;i<nvs.length;i++)
				{
					pair=nvs[i].split("=");		// [ <space>attribute_x<space> , <space>"value_x ]
					name=pair[0].trim();		// <space>attribute_x<space> --> attribute_x
					value=pair[1].trim();		// <space>"value_x --> "value_x
					value=value.substring(1);	// Remove leading quote "value_x--> value_x

					//System.out.println(name+"="+value);

					newTag.nvpairs.put(name,value);
				}
				
			}
			else
				tagName=line;

			Tag parent=tagStack.peek();
			parent.addTag(tagName,newTag);
			tagStack.push(newTag);


			System.out.println(tagName);
		}
		else
			tagStack.pop();
	}
	public void eval(String str)
	{
		String[] tagInfo=str.split("\\.");

		Tag currentTag=root;	
		if(tagInfo.length>0)
		{
			String[] reqTag=tagInfo[tagInfo.length-1].split("~");	
			//System.out.println(tagInfo[tagInfo.length-1]);
			for(int i=0;i<tagInfo.length-1;i++)
				currentTag=currentTag.childTags.get(tagInfo[i]);
			System.out.println(currentTag.childTags.get(reqTag[0]).nvpairs.get(reqTag[1]));
		}
		else
			{
				String[] reqTag=str.split("~");
				System.out.println(reqTag[0]);
				System.out.println(currentTag.childTags.get(reqTag[0]).nvpairs.get(reqTag[1]));
			}

	}
	public static void main(String[] args)
	{
		Scanner sc=new Scanner(System.in);
		int n,q;
		n=sc.nextInt();
		q=sc.nextInt();
		sc.nextLine();
		
		String line;
		String query;
		
		HRMLParser parser=new HRMLParser();

		for(int i=0;i<n;i++)
		{
			line=sc.nextLine();
			parser.parseLine(line);
		}

		for(int i=0;i<q;i++)
		{	query=sc.nextLine();
			parser.eval(query);
		}
	}
}

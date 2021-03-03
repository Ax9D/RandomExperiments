#include <iostream>
#include <cstdlib>
#include <queue>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <errno.h>
#include <cstring>

bool isfile(std::string path)
{
	struct stat buf;
	stat(path.c_str(),&buf);
	return S_ISREG(buf.st_mode);
}
bool isdir(std::string path)
{
	struct stat buf;
	stat(path.c_str(),&buf);
	return S_ISDIR(buf.st_mode);
}


int main(int argc,char** argv)
{
	std::queue<std::string> dirs;
	
	char* abspath=realpath(argv[1],NULL);
	
	printf("%s\n",abspath);
	
	dirs.push(std::string(abspath));
	
	free(abspath);
	
	std::string current;
	
	
	struct dirent* dir_entry;
	int c=0;
	while(!dirs.empty())
	{
		current=dirs.front();
		dirs.pop();
		
		DIR* dir=opendir(current.c_str());
		
		if(dir!=NULL)
		{
		//printf("%s\n",current.c_str());
		
			while((dir_entry=readdir(dir))!=NULL)
			{	
				//std::cout << dir_entry->d_name;
				if(!(strcmp(dir_entry->d_name,".")==0 || strcmp(dir_entry->d_name,"..")==0))
				{	
					//std::cout << current << "/" << dir_entry->d_name << std::endl;
					std::string stuff=current + "/"+dir_entry->d_name;
					if(isfile(stuff))
						c++;
					else if(isdir(stuff)) 
						dirs.push(stuff);
				}
			}
			
			closedir(dir);
		}
		else 
			printf("Couldn't open %s\n",current.c_str());
	}
	printf("%d Files\n",c);
	
}

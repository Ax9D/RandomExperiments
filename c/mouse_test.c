#include <stdio.h>
#include <sys/time.h>
#include <stdlib.h>
#include <linux/input.h>
//#include <linux/input-event-codes.h>


int main(int argc,char** argv)
{
		FILE* fp=fopen("/dev/input/event11","r");
		
		struct input_event* eventBuff=malloc(sizeof(struct input_event));
		
		while(1)
		{
			fgets(eventBuff,sizeof( struct input_event ),fp);
			//printf("%s",eventBuff);
			printf("type=%d\ncode=%d\nvalue=%d\n",eventBuff->type,eventBuff->code,eventBuff->value);
		}
		fclose(fp);
}

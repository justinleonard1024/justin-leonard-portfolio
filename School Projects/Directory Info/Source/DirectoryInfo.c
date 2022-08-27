/********************************
 * Directory Info
 * DirectoryInfo.c
 * Created by Justin Leonard
********************************/

#define _POSIX_C_SOURCE 200112L
#define _ISOC99_SOURCE
#define __EXTENSIONS__
#define _XOPEN_SOURCE 600

#include <dirent.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <linux/limits.h>
#include <sys/stat.h>



/*
 * Function: checkStats(struct stat src, struct stat trg)
 * @parameter:
 * 	src:	the source file stats
 * 	trg:	the target file stats
 * @return:
 * 	0:	the file stats are not the same
 * 	1:	the file stats are the same
 */
int checkStats(struct stat src, struct stat trg) {
	// Variables
	int check = 0;
	
	// Check if file stats are the same
	if ((src.st_dev == trg.st_dev) && (src.st_ino == trg.st_ino)) {
		check = 1;
	}
	
	// Return result
	return check;
}



/*
 * Function: prependDirectory(char *src, char *trg)
 * @parameter:
 * 	src:	the source string
 * 	trg:	the target string
 */
void prependDirectory(char *src, char *trg) {
	// Variables
	char buf[PATH_MAX];
	int isInitialDir = (strlen(trg) == 0);
	
	// Check if string is too big
	if (strlen(src) + strlen(trg) + 2 >= PATH_MAX) {
		return;
	}
	
	// Set target string to buffer
	strcpy(buf,trg);
	
	// Clear target string
	memset(trg,0,strlen(trg));
	
	// Make target string the source string
	strcpy(trg,src);
	if (strcmp(src,"/") != 0 && !isInitialDir)
		strcat(trg,"/");
	
	// Append target string with original string
	strcat(trg,buf);
}



/*
 * Function: myprintcwd(char *str)
 * @parameter:
 * 	str:	string to use
 */
void myprintcwd(char *str) {
	// Print message
	printf("Current Working Directory: %s\n", str);
}



/*
 * Function: mygetcwd(void)
 * @return:
 * 	EXIT_FAILURE:	failure
 * 	EXIT_SUCCESS:	success
 */
int mygetcwd(void) {
	// Variables
	int keepGoing = 1;
	char str[PATH_MAX];
	struct stat rootStats;
	struct stat currentStats;
	struct stat childStats;
	struct dirent *childDir;
	DIR *parentDir;
	
	// Get root stats
	if(stat("/", &rootStats) == -1) {
		fprintf(stderr, "stat() on %s error: %s\n", "/", strerror(errno));
		return EXIT_FAILURE;
	}
	
	// Get current working directory
	while(keepGoing) {
		// Get current directory stats
		if(stat(".", &currentStats) == -1) {
			fprintf(stderr, "stat() on %s error: %s\n", ".", strerror(errno));
			return EXIT_FAILURE;
		}
		
		// Check if current directory is root
		if(checkStats(currentStats,rootStats)) {
			prependDirectory("/", str);
			myprintcwd(str);
			break;
		}
		
		// Change directory to parent
		if(chdir("..") == -1) {
			fprintf(stderr, "chdir() on %s error: %s\n", "..", strerror(errno));
			return EXIT_FAILURE;
		}
		
		// Open directory
		parentDir = opendir(".");
		if(parentDir == NULL) {
			fprintf(stderr, "opendir() on %s error: %s\n", ".", strerror(errno));
			return EXIT_FAILURE;
		}
		
		// Get directory name
		childDir = readdir(parentDir);
		while(childDir != NULL) {
			// Get child directory stats
			if(stat(childDir->d_name, &childStats) == -1) {
				fprintf(stderr, "stat() on %s error: %s\n", childDir->d_name, strerror(errno));
				return EXIT_FAILURE;
			}
			
			// Check if current directory is child directory
			if(checkStats(currentStats,childStats)) {
				prependDirectory(childDir->d_name, str);
				break;
			}
			
			// Read directory
			childDir = readdir(parentDir);
		}
	}
	
	// Return success
	return EXIT_SUCCESS;
}





int main(void) {
	// End
	return mygetcwd();
}



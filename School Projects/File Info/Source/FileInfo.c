/********************************
 * File Info
 * FileInfo.c
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
 * Function: listfileinfo()
 */
int listfileinfo() {
	// Variables
	int keepGoing = 1;
	char buf[PATH_MAX];
	struct stat fileStats;
	struct dirent *dirEnt;
	DIR *dirInfo;
	
	// Get input
    printf("Path name: ");
	scanf("%s", buf);
	
	// Open directory
	dirInfo = opendir(buf);
	
	// Error
	if(dirInfo == NULL) {
		fprintf(stderr, "opendir() on %s error: %s ", buf, strerror(errno));
		return EXIT_FAILURE;
	}
	
	// Change directory
	chdir(buf);
	
	// Get directory name
	dirEnt = readdir(dirInfo);
	
	// Get all info
	while(dirEnt != NULL) {
		// Get child directory stats
		if(stat(dirEnt->d_name, &fileStats) == -1) {
			fprintf(stderr, "stat() on %s error: %s ", dirEnt->d_name, strerror(errno));
			return EXIT_FAILURE;
		}
		
		// Print current file info
		printf("Name: %s\nDevice ID: %ld\nINode Number: %ld\nMode: %d\nUser ID: %d\nGroup ID: %u\nSize: %ld\nAccess Time: %ld\nModification Time: %ld\nCreated Time: %ld\n\n\n\n", dirEnt->d_name, fileStats.st_dev, fileStats.st_ino, fileStats.st_mode, fileStats.st_uid, fileStats.st_gid, fileStats.st_size, fileStats.st_atime, fileStats.st_mtime, fileStats.st_ctime);
		
		// Read directory
		dirEnt = readdir(dirInfo);
	}
	
	// Close directory
	closedir(dirInfo);

	// Return
	return EXIT_SUCCESS;
}



/*
 * Function: main(void)
 */
int main(void) {
	// Return
	return listfileinfo();
}



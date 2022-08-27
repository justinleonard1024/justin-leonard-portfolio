/********************************
 * String Editor
 * StringEditor.c
 * Created by Justin Leonard
********************************/

#define _POSIX_C_SOURCE 200112L
#define _ISOC99_SOURCE
#define __EXTENSIONS__
#define _XOPEN_SOURCE 600

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 32
#define CHOICE_CONVERTUPPER 1
#define CHOICE_CONVERTLOWER 2
#define CHOICE_CHECKDIGITS 3
#define CHOICE_ENCRYPT 4
#define CHOICE_DECRYPT 5
#define CHOICE_EXIT 6



/*
 * Function: menu_wait(void)
 */
void menu_wait(void) {
	// Print message
	printf("\nPress enter key to continue");
	
	// Wait for enter key press
	while(getchar() != '\n');
}



/*
 * Function: menu_clear(void)
 */
void menu_clear(void) {
	// Variables
	char tmp;
	
	// Clear input
	while((tmp = getchar()) != '\n' && tmp != EOF);
}



/*
 * Function: menu_convertupper(void)
 */
void menu_convertupper(void) {
	// Variables
	int i;
	char buf[BUFFER_SIZE];
	
	// Print title
	printf("\n\n\n********************************\n\n      Upper Case Conversion\n\n********************************\n\nPlease enter a string: ");
	
	// Get input
	fgets(buf, sizeof buf, stdin);
	
	// Convert all lower case letters to upper case letters
	for(i = 0; i < strlen(buf); ++i) {
		// Letter is lower case
		if(buf[i] >= 97 && buf[i] <= 122)
			buf[i] -= 32;
	}
	
	// Print converted string
	printf("\nConverted string: %s", buf);
	
	// Wait
	menu_wait();
}



/*
 * Function: menu_convertlower(void)
 */
void menu_convertlower(void) {
	// Variables
	int i;
	char buf[BUFFER_SIZE];
	
	// Print title
	printf("\n\n\n********************************\n\n      Lower Case Conversion\n\n********************************\n\nPlease enter a string: ");
	
	// Get input
	fgets(buf, sizeof buf, stdin);
	
	// Convert all upper case letters to lower case letters
	for(i = 0; i < strlen(buf); ++i) {
		// Letter is upper case
		if(buf[i] >= 65 && buf[i] <= 90)
			buf[i] += 32;
	}
	
	// Print converted string
	printf("\nConverted string: %s", buf);
	
	// Wait
	menu_wait();
}



/*
 * Function: menu_checkdigits(void)
 */
void menu_checkdigits(void) {
	// Variables
	int i = 0;
	int keepGoing = 1;
	int hasDigits = 0;
	char buf[BUFFER_SIZE];
	
	// Print title
	printf("\n\n\n********************************\n\n          Check Digits\n\n********************************\n\nPlease enter a string: ");
	
	// Get input
	fgets(buf, sizeof buf, stdin);
	
	// Check digits
	while(keepGoing) {
		// Character is digit
		if(buf[i] >= 48 && buf[i] <= 57) {
			keepGoing = 0;
			hasDigits = 1;
		}
		
		// Increment
		i++;
		
		// Check if at end of string
		if(i >= strlen(buf))
			keepGoing = 0;
	}
	
	// Print if the string has digits
	if(hasDigits)
		printf("\nThe string has digits\n");
	else
		printf("\nThe string does not have digits\n");
	
	// Wait
	menu_wait();
}



/*
 * Function: menu_encrypt(void)
 */
void menu_encrypt(void) {
	// Variables
	int i;
	int advance = 0;
	char buf[BUFFER_SIZE];
	
	// Print title for string
	printf("\n\n\n********************************\n\n           Encryption\n\n********************************\n\nPlease enter a string: ");
	
	// Get input for string
	fgets(buf, sizeof buf, stdin);
	
	// Print title for advance integer
	printf("Please enter the advance integer: ");
	
	// Get input for advance integer
	scanf("%d", &advance);

	// Clear input
	menu_clear();
	
	// Input is negative
	while(advance < 0) {
		// Print title for advance integer
		printf("\nError: Advance integer must be positive\nPlease enter the advance integer: ");
		
		// Get input for advance integer
		scanf("%d", &advance);

		// Clear input
		menu_clear();
	}
	
	// Encrypt string
	for(i = 0; i < strlen(buf); ++i) {
		// Check if character is upper case
		if(buf[i] >= 65 && buf[i] <= 90) {
			buf[i] = 'A' + (((buf[i] - 'A') + advance) % 26);
		}
		// Check if character is lower case
		else if(buf[i] >= 97 && buf[i] <= 122) {
			buf[i] = 'a' + (((buf[i] - 'a') + advance) % 26);
		}
	}
	
	// Print encrypted string
	printf("\nEncrypted string: %s", buf);
	
	// Wait
	menu_wait();
}



/*
 * Function: menu_decrypt(void)
 */
void menu_decrypt(void) {
	// Variables
	int i;
	int advance = 0;
	char buf[BUFFER_SIZE];
	
	// Print title for string
	printf("\n\n\n********************************\n\n           Decryption\n\n********************************\n\nPlease enter a string: ");
	
	// Get input for string
	fgets(buf, sizeof buf, stdin);
	
	// Print title for advance integer
	printf("Please enter the advance integer: ");
	
	// Get input for advance integer
	scanf("%d", &advance);

	// Clear input
	menu_clear();
	
	// Input is negative
	while(advance < 0) {
		// Print title for advance integer
		printf("\nError: Advance integer must be positive\nPlease enter the advance integer: ");
		
		// Get input for advance integer
		scanf("%d", &advance);

		// Clear input
		menu_clear();
	}
	
	// Decrypt string
	for(i = 0; i < strlen(buf); ++i) {
		// Check if character is upper case
		if(buf[i] >= 65 && buf[i] <= 90) {
			buf[i] = 'A' + (((buf[i] - 'A') - advance) % 26);
			if(buf[i] < 65)
				buf[i] += 26;
		}
		// Check if character is lower case
		else if(buf[i] >= 97 && buf[i] <= 122) {
			buf[i] = 'a' + (((buf[i] - 'a') - advance) % 26);
			if(buf[i] < 97)
				buf[i] += 26;
		}
	}
	
	// Print decrypted string
	printf("\nDecrypted string: %s", buf);
	
	// Wait
	menu_wait();
}



/*
 * Function: menu(void)
 */
void menu(void) {
	// Variables
	int keepGoing = 1;
	int choice = 0;
	
	// Menu loop
	while(keepGoing) {
		// Print title
		printf("\n\n\n********************************\n\n        String Editor\n\n 1. Upper Case Conversion\n 2. Lower Case Conversion\n 3. Check Digits\n 4. Encryption\n 5. Decryption\n 6. Exit\n\n********************************\n\nPlease select your option (1-6): ");
		
		// Get input
		scanf("%1d", &choice);
	
		// Clear input
		menu_clear();
		
		// Check choice
		switch(choice) {
			// Convert to upper case
			case CHOICE_CONVERTUPPER:
				menu_convertupper();
				break;
			
			// Convert to lower case
			case CHOICE_CONVERTLOWER:
				menu_convertlower();
				break;
			
			// Check if string has digits
			case CHOICE_CHECKDIGITS:
				menu_checkdigits();
				break;
				
			// Encrypt string
			case CHOICE_ENCRYPT:
				menu_encrypt();
				break;
				
			// Decrypt string
			case CHOICE_DECRYPT:
				menu_decrypt();
				break;
				
			// Exit
			case CHOICE_EXIT:
				keepGoing = 0;
				break;
			
			// Default
			default:
				break;
		}
	}
}



int main(int argc, char *argv[]) {
	// Run the menu
	menu();
	
	// End
	return EXIT_SUCCESS;
}



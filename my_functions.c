#include <stdio.h>

int square(int i) {
	return i * i;
}


int heavy(int n) {
	
	int j = 0 ;
	while(j<n){ 
		j++;
	}

	printf("value :%d",j);
	return 0;
}


int main(){
    
	heavy(1000000000);
	return 0 ;
}

char* mostCommonWord(char* paragraph, char** banned, int bannedSize) {
    char  letter[1000];
    char array[500][1000];
    int val=0;int j=0;
    int size=strlen(paragraph);
    for(int i=0;i<=size;i++){
        if(isalnum(paragraph[i])){
            letter[val++]=tolower(paragraph[i]);
        }
        else{
            letter[val]='\0';
            if(val>0){
            strcpy(array[j],letter);
            j++; }
            val=0;
        }
        
    }

    char *s=(char *)malloc(1000*sizeof(char));
    int count,max=0,index;
    for(int i=0;i<j;i++){
        count=1;
        if(strcmp(array[i],"0")==0) continue;
        for(int k=i+1;k<j;k++){
            if(strcmp(array[i],array[k])==0){
                count++;
                strcpy(array[k],"0");
            }
        }
        int flag=1;
        for(int l=0;l<bannedSize;l++){
            if(strcmp(banned[l],array[i])==0){
                    flag=0;
                    break;
            }
        }
        if(flag==0) continue;
        if(count>max){
            max=count;
            strcpy(s,array[i]);
        }
    }
    return s;
}

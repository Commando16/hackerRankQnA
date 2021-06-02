string fairRations(vector<int> B) {
    
    int odd = 0;
    int bread = 0;
    for(int i = 0; i<B.size(); i++)
    {
        // cout<<B[i]<<" ";
        if(B[i]%2!=0){
            odd++;
        }
        
    }
    
    if(odd%2!=0)
        return("NO");
    
    for(int i = 0; i<B.size()-1; i++)
    {
        // cout<<B[i]<<" ";
        if(B[i]%2!=0){
            bread+=2;
            B[i]++;
            B[i+1]++;
        }
        
    }
    
    return(to_string(bread));
}




//Done
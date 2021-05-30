#include<iostream>
#include<vector>
#include<cmath>
#include <bits/stdc++.h>

using namespace std;
int flatlandSpaceStations(int n, vector<int> c) {

    int max = 0;
    sort(c.begin(), c.end());
    
    for(int i=0; i<c.size()-1; i++){
        int dist = (abs(c[i]-c[i+1]))/2;
        cout<<dist<<" ";
        if( max < dist){
            max = dist;
        }
    }
    
    if( max < (abs(0-c[0]))){
        max = (abs(0-c[0]));
        cout<<max<<" ";
    }

 
    
    if( max < (abs(n-c.back()))-1){
        max = (abs(n-c.back()))-1;
        cout<<max<<" ";
    }
    
    return max;

}

int main(){

    vector<int> ss_city = {13, 1, 11, 10, 6};

    cout<<"The longest distance is- "<<flatlandSpaceStations(20,ss_city);

    return 0;
}



//Done
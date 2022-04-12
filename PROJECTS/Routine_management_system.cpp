#include<bits/stdc++.h>
using namespace std;
void ndfs(int u, int v,vector<vector<string>> v1 ){

    int k=v;
    for (int i = 0; i < 7; ++i)
    {
        
    
    while(k!=7){
     cout<<v1[u][k]<<" ";
     k++;
    }
    u++;
    k=0;
    cout<<endl;
}
}
void ndfs1(int u, int v,vector<vector<string>> v1 ){

    int k=v-1;
    int h=u;
    for (int i = 0; i < 7; ++i)
    {
        
    
    while(k!=7){
     cout<<v1[h][k]<<" ";
     k++;
    }
    
}

}

int main(){
    vector<vector<string>> v(5, vector<string> (7, "abc"));
v[0][0]="MON :";
v[0][1]="MATHS";
v[0][2]="TRW";
v[0][3]="ANALOG ELECTRONIC CIRCUITS";
v[0][4]="PROJECT(APP DEVELOPMENT)";
v[0][5]="SDP";
v[0][6]="SDP";
v[1][0]="TUE :";
v[1][1]="MATHS";
v[1][2]="MATHS";
v[1][3]="DS";
v[1][4]="ANALOG";
v[1][5]="TRW";
v[1][6]="DIGITAL";
v[2][0]="WED :";
v[2][1]="DIGITAL";
v[2][2]="ANALOG LAB";
v[2][3]="ANALOG LAB";
v[2][4]="MATHS";
v[2][5]="DS LAB";
v[2][6]="DS LAB";
v[3][0]="THU :";
v[3][1]="ANALOG";
v[3][2]="TRW";
v[3][3]="MATHS";
v[3][4]="PLACEMENT";
v[3][5]="PLACEMENT";
v[3][6]="MOOCS1";
v[4][0]="FRI :";
v[4][1]="ANALOG";
v[4][2]="SDP";
v[4][3]="SDP";
v[4][4]="DS";
v[4][5]="DIGITAL LAB";
v[4][6]="DIGITAL LAB";

cout<<"------------------ROUTINE---------------------"<<endl;
cout<<"Press 'yes' to see the full routine"<<endl;
cout<<"Press 'day' name to see that day's routine"<<endl;
cout<<endl;
string s;
cin>>s;
if(s=="yes"){
    cout<<"----------------FULL ROUTINE------------------"<<endl;
ndfs(0,0,v);   
}
if(s=="MON"){
ndfs1(0,1,v);
}
if(s=="TUE"){
ndfs1(1,1,v);    
}
if(s=="WED"){
    ndfs1(2,1,v);
}
if(s=="THU"){
    ndfs1(3,1,v);
}
if(s=="FRI"){
    ndfs1(4,1,v);
}
cout<<endl;
cout<<"Do you want to change any day's routine? If yes, press 'y'"<<endl;
char c;
cin>>c;
if(c=='y'){
    cout<<"Enter the day's name "<<endl;
    string d;
    cin>>d;
    if(d=="MON"){
    cout<<"Enter the period no."<<endl;
    int n1;
    cin>>n1;
    cin>>v[0][n1];
    cout<<"The routine is updated successfully"<<endl;
    }
    if(d=="TUE"){
     cout<<"Enter the period no."<<endl;
     int n2;
     cin>>n2;   
     cin>>v[1][n2];
     cout<<"The routine is updated successfully"<<endl;
    }
    if(d=="WED"){
        cout<<"Enter the period no."<<endl;
        int n3;
        cin>>n3;
        cin>>v[2][n3];
        cout<<"The routine is updated successfully"<<endl;
    }
    if(d=="THU"){
        cout<<"Enter the period no."<<endl;
        int n4;
        cin>>n4;
        cin>>v[3][n4];
        cout<<"The routine is updated successfully"<<endl;
    }
    if(d=="FRI"){
        cout<<"Enter the period no."<<endl;
        int n5;
        cin>>n5;
        cin>>v[4][n5];
        cout<<"The routine is updated successfully"<<endl;
    }
}

}
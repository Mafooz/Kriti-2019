/*#include<iostream>
using namespace std;
#include<bits/stdc++.h>
int main(){
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		vector<int>arr(n);
		vector<pair<int,int> >aux(n+1,make_pair(0,0));
		for(int i=0;i<n;i++){
			cin>>arr[i];
			aux[i+1].first=aux[i].first^arr[i];
			aux[i+1].second=i+1;
		}
		int sum=0;
		for(int i=0;i<n+1;i++){
			cout<<aux[i].first<<" ";
		}
		sort(aux.begin(),aux.end());
		for(int i=0;i<n+1;i++){
			int j=i+1;
			int count=1;
			int val=0;
			while(j!=n+1&&aux[j-1].first==aux[j].first){

				val+=(aux[j].second-aux[j-1].second-1)*count+count-1;
				count++;
				j++;
			}
			sum+=val;
			i=j-1;
		}
		cout<<sum<<"\n";
	}

}*/
#include<iostream>
using namespace std;
#include<bits/stdc++.h>
#include<limits.h>
void merge(int a1,int a2,int a3,int a4,int a5,int s1,int s2,int count,int *sum,pair<int,int>&ans){
	if(count==5){
		if(*sum>abs(s2-s1)){
			ans.first=s1;
			ans.second=s2;
			*sum=abs(s2-s1);
		}
		return;
	}
	if(count==0){
		s1=s1+a1;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s1-=a1;
		s2+=a1;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s2+=s2-a1;
	}
	if(count==1){
		s1=s1+a2;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s1-=a2;
		s2+=a2;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s2+=s2-a2;
	}
	if(count==2){
		s1=s1+a3;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s1-=a3;
		s2+=a3;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s2+=s2-a3;
	}
	if(count==3){
		s1=s1+a4;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s1-=a4;
		s2+=a4;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s2+=s2-a4;
	}
	if(count==4){
		s1=s1+a5;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s1-=a5;
		s2+=a5;
		merge(a1,a2,a3,a4,a5,s1,s2,count+1,sum,ans);
		s2+=s2-a5;
	}
}
int main()
{
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		vector<int>arr(n);
		for(int i=0;i<n;i++){
			cin>>arr[i];
		}
		int sum=0;
		vector<vector<pair<int,int> > >X(n+1);
		for(int i=0;i<n;i++){
			X[0].push_back(make_pair(0,0));
			X[1].push_back(make_pair(0,arr[i]));
		}
		X[0].push_back(make_pair(0,0));
		for(int i=2;i<=n;i++){
			for(int j=0;j<=n-i;j++){
				X[i].push_back(make_pair(-1,-1));
				pair<int,int> temp;
				int a=INT_MAX;
				for(int k=0;k<i-1;k++){
					pair<int,int> p=X[k][j];
					pair<int,int> q=X[i-k-1][k+j+1];
					int e=arr[j+k];
					pair<int,int>ans;
					int c=INT_MAX;
					int a1=p.first;
					int a2=p.second;
					int a3=q.first;
					int a4=q.second;
					merge(a1,a2,a3,a4,e,0,0,0,&c,ans);
					if(a>abs(ans.first-ans.second)){
						a=abs(ans.first-ans.second);
						X[i][j]=ans;
					}
				}
		   }
		}	
		cout<<abs(X[n][X[n].size()-1].second-X[n][X[n].size()-1].first)<<"\n";
	}
}

/*
-> Como usar o getline para leitura de sentenças (ex.: "uma duas três")
-> Problema 1: com "cin >>" apenas se lê uma palavra por vez
-> Problema 2: o getline não lia a última senteça.

Contest Codeforces div 4: https://codeforces.com/contest/2094
*/
#include <bits/stdc++.h>
using namespace std;

int main(){
  ios::sync_with_stdio(0); cin.tie(0);
  int n;
  cin >> n;
  cin.ignore(); // A solução: limpa o "\n" que ficou no buffer
  for(int j=0; j<n; j++) {
    string p;
    getline(cin,p);
    stringstream q(p);
    vector<string>v;
    string e;
    while(getline(q,e,' ')){
      v.push_back(e);
    }
    string s = "";
    for(int i=0; i<v.size(); i++) {
      s += v[i][0];
    }
    cout << s << "\n";
  }
}
//g++ -std=gnu++17 -O2 -static -o c a.cpp && ./c

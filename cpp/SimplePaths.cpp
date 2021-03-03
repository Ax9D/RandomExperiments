#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int simplePaths(vector<vector<int>> edges) {
}
int main() {
	 int t;
	cin >> t;
	int n;
	for(int i=0;i<t;i++) {
		cin >> n;
		vector< vector<int> > graph;
		graph.reserve(n);
		
		int from,to;
		for(int j=0;j<n;j++) {
			cin >> from ;
			cin >> to ;
			graph[from].push_back(to);
		}
	}
}

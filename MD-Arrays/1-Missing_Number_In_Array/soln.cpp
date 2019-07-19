#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        int arr[n];
        int sum_n = n*(n+1)/2;
        int arr_sum = 0;
        for (int i=1; i<n; i++){
            cin >> arr[i];
            arr_sum = arr_sum + arr[i];
        }
        cout << (sum_n - arr_sum) <<endl;
    }
	//code
	return 0;
}

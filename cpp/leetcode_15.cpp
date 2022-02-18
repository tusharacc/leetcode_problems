#include <iostream>
#include <vector>
using namespace std;

void threeSum(vector<int> nums) {
    for(int item:nums){
        cout << item << endl;
    }
}


int main(int argc,char *argv[]){
    //std::cout << reverse(-2147483648);
    cout << threeSum({-1,0,1,2,-1,-4,-2,-3,3,0,4}) << endl;

}
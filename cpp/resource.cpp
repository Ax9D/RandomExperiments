#include <iostream>
#include <vector>
#include <chrono>

class Resource{
	public:
		Resource(std::vector<int>& d,int dt): dataSet(d), data(dt){
			this->dataSet=dataSet;
			this->data=data;
		}
		~Resource(){
			this->dataSet.push_back(this->data);
		}
		std::vector<int>& dataSet;
		int data;
};
class ResourceManager {
	private:
		std::vector<int> data;
	public:
		ResourceManager(){
		}
		void put(int x){
			this->data.push_back(x);
		}
		Resource get(){
			int last=this->data.back();
			this->data.pop_back();
			return Resource(this->data,last);
		}
		~ResourceManager(){
			
		}
};
int main(){
	auto prev=std::chrono::system_clock::now();
	ResourceManager rm;
	for(int i=0;i<1000000;i++) {
		rm.put(1);
		rm.put(2);
		rm.put(3);
	}
	float c=0;
	for(int i=0;i<50000;i++) {
		Resource x=rm.get();
		Resource y=rm.get();
		c+=x.data + y.data*i/x.data;
	}
	std::cout << c << std::endl;
	
	auto now = std::chrono::system_clock::now();
	auto milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(now - prev);
	std::cout << milliseconds.count() << " ms" << std::endl;
}

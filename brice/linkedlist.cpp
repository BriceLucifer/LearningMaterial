#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct ListNode {
	int val;
      	ListNode *next;
      	ListNode() : val(0), next(nullptr) {}
      	ListNode(int x) : val(x), next(nullptr) {}
      	ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *mergeTwoList(ListNode* n1,ListNode* n2){
	if(n1 == nullptr){
		return n2;
	}

	if(n2 == nullptr){
		return n1;
	}

	if(n1->val <= n2->val){
		n1->next = mergeTwoList(n1->next,n2);
		return n1;
	}
	n2->next = mergeTwoList(n1,n2->next);
	return n2;
}

int main(){

}

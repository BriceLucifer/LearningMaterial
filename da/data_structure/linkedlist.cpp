#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

    void insert(int x) {
        if (this->next == nullptr) {
            this->next = new ListNode(x);
        } else {
            this->next->insert(x);
        }
    }

    void deleteNode() {
        if (this == nullptr) {
            return;
        }

        if (this->next != nullptr) {
            ListNode* temp = this->next;
            this->next = this->next->next;
            delete temp;
        } else {
            // 如果当前节点是尾节点，则直接删除
            delete this;
        
        }
    }

    void print() {
        if (this == nullptr) {
            cout << "null";
            return;
        } else {
            cout << this->val << "->";
            if (this->next != nullptr) {
                this->next->print();
            } else {
                cout << "null"; // 打印完当前节点后终止递归
            }
        }
    }
};

ListNode *mergeTwoLists(ListNode* n1, ListNode* n2) {
    if (n1 == nullptr) {
        return n2;
    }

    if (n2 == nullptr) {
        return n1;
    }

    if (n1->val <= n2->val) {
        n1->next = mergeTwoLists(n1->next, n2);
        return n1;
    } else {
        n2->next = mergeTwoLists(n1, n2->next);
        return n2;
    }
}

int main() {
    ListNode* n1 = new ListNode(1);
    n1->insert(2);
    n1->insert(3);
    n1->insert(4);
    n1->deleteNode(); // 修改方法名以避免与C++关键字冲突
    n1->print();
	cout << endl;
    return 0;
}
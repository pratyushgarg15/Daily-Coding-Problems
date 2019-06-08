/*
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
*/

#include <iostream>
using namespace std;

class LinkedListNode{
public:	
	int data;
	LinkedListNode* link;

	LinkedListNode(int val){
		this->data = val;
		this->link = nullptr;
	}
};

class XORLinkedList{
public:	
	LinkedListNode* head;

	XORLinkedList(){
		this->head = nullptr;
	}

	LinkedListNode* XOR(LinkedListNode* x , LinkedListNode* y){
		return (LinkedListNode*)((uintptr_t)(x) ^ (uintptr_t)(y));
	}

	void add(int val){
		LinkedListNode* newNode = new LinkedListNode(val);
		
		if(this->head == nullptr){
			this->head = newNode;
			return ;
		}

		if(this->head->link == nullptr){
			this->head->link = newNode;
			newNode->link = this->head;
			return ;
		}

		LinkedListNode* node ;
		LinkedListNode* follow;
		LinkedListNode* temp;
	
		follow = this->head;
		node = follow->link;

		while(node->link != follow){
			temp = follow;
			follow = node;
			node = XOR(temp, node->link);
		}

		node->link = XOR(follow, newNode);
		newNode->link = node;
		
        temp = nullptr;
		node = nullptr;
		follow = nullptr;
		delete node;
		delete follow;
		delete temp;
	}

	LinkedListNode* get(int index){
		LinkedListNode* node;
		LinkedListNode* follow;
		LinkedListNode* temp;

		if(index == 0){
			return this->head;
		}

		follow = this->head;
		node = follow->link;

		for (int i = 1; i < index; ++i)
		{
			temp = follow;
			follow = node;
			node = XOR(temp, node->link);
		}

		temp = nullptr;
		follow = nullptr;
		delete follow;
		delete temp;
		
		return node;

	}

	void printLinkedList(){

		if(this->head->link == nullptr){
			cout << this->head->data;
			return ;
		}

		LinkedListNode* node ;
		LinkedListNode* follow;
		LinkedListNode* temp;
		
		follow = this->head;
		node = follow->link;

		while(node->link != follow){
			cout << follow->data << "->" ;
			temp = follow;
			follow = node;
			node = XOR(temp, node->link);
		}

		cout << follow->data << "->";
		cout << node->data << endl;

		temp = nullptr;
		node = nullptr;
		follow = nullptr;
		delete node;
		delete follow;
		delete temp;
	}
};

int main(){
	XORLinkedList* list = new XORLinkedList();

	list->add(1);
	list->add(2);
	list->add(3);
	list->add(4);
	list->add(5);

	list->printLinkedList();

	LinkedListNode* getval= list->get(2);

	cout << getval->data << endl;

}
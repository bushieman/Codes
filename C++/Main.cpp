#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "lets start c++";
}



handle failures
cout << cin.fail()

cin.clear()
cin.ignore(1000, '\n')




length of an array
sizeof(arr)/sizeof(arr[0])



the continue keyword jumps over the expected output for the specified conditions.
for(int x=1; x < 10;x++) {
    if (x==2 || x==4) {
        continue;
    }
    cout << x << endl;
}



initializing your pointers is optional
you can redefine a pointer

when a number is added to a pointer of an array reference, this creates a for loop on that array  
int x[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int *head = x;
for (int i = 0; i < 10; i+=2) {
    head = x + i;
    cout << head << endl;
    cout << *head << endl;
}



tuples
#include <tuple>
tuple <int, string> person; - declaring tuples
person = make_tuple(21, "bushman"); - initializing the tuple
tuple <int, string> person(21, "bushman"); - initializing tuples
cout << get <1> (person); - returning an item inside a tuple at specific index
get <1> (person) = "bushie"; - modify an existing tuple
person.swap(person2); - swapping tuples
decomposing a tuple
tuple <int, string> person(21, "bushman");
int x;
string y;
tie(x,y) = person;
cout << x << endl;  
cout << y << endl;  
tuple concatenation
tuple <int, string> person(21, "bushman");
tuple <char, float> person2('b', 1.2); 
auto person3 = tuple_cat(person, person2);
cout << get <0> (person3) << endl; 



maps
#include <map>
map<int, string> users = {
    {1, "bushman"},
    {2, "rachel"},
    {3, "monica"},
    {4, "sandra"},
    {5, "lornah"},
};
cout << users[3] << endl;

inserting an element into a map
users[6] = "barbra"; - method1
pair<int, string> p1(7, "hamilton"); - method2
users.insert(p1);
cout << p1.first << endl; - returns the first item inside a pair with p1.second returning the second item

erasing elements
users.erase(p1.first);
clear elements
users.clear();

map size
cout << users.size() << endl;

dereferencing the iterator
map<int, string> users = {
    {1, "bushman"},
    {2, "rachel"},
    {3, "monica"},
    {4, "sandra"},
    {5, "lornah"},
};

for (auto itr = users.begin(); itr != users.end(); itr++) {
    cout << itr->second << endl;
}
auto represents map<int, string>::iterator
example
string details = "my name is bushman";
map<char, int> freq;

for (char i = 0; i < details.length(); i++) {
    char letter = details[i];
    if (freq.find(letter) == freq.end()) {
        freq[letter] = 0;
    }
    freq[letter]++;
}

for (auto itr = freq.begin(); itr != freq.end(); itr++) {
    cout << itr -> first << ":" << itr -> second << endl;
}



vectors
#include <vector>

defining vectors
vector<int> v1 {1, 2, 3, 4, 5};
basics
v1.push_back(6);
v1.pop_back();
v1.insert(v1.begin(), 0);
v1.erase(v1.begin());
v1.shrink_to_fit();
cout << v1[0] << endl;
cout << v1.front() << endl;
cout << v1.back() << endl;
cout << v1.size() << endl;
cout << v1.capacity() << endl;

iterate over vectors
for (int i = 0; i < v1.size(); i++) {
    cout << v1[i] << endl;
};
for (auto itr = v1.begin(); itr != v1.end(); itr++) {
    cout << *itr << endl;
};



sets
sets store one instance of each item
#include <set>
set<int> s1 {0, 1, 2, 3, 4, 5, 2, 4, 5};
s1.insert(19);
s1.erase(2);


optional parameter
int number(int x=2) {
    return x;
}

pair<int, int> number(int x, int y) {
    return pair<int, int>(x, y);
}
int main() {
    cout << number(2, 3).second;
}

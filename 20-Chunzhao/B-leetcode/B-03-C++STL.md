# 栈和队列
### 栈实现
**栈是以底层容器完成其所有的工作，对外提供统一的接口，底层容器是可插拔的（也就是说我们可以控制使用哪种容器来实现栈的功能）。**
**我们常用的SGI STL，如果没有指定底层实现的话，默认是以deque为缺省情况下栈的底层结构。** deque是一个双向队列，只要封住一段，只开通另一端就可以实现栈的逻辑了。
 我们也可以指定vector为栈的底层实现，初始化语句如下：
`std::stack<int, std::vector<int> > third;  // 使用vector为底层容器的栈`

### 队列实现
**SGI STL中 队列底层实现缺省情况下一样使用deque实现的。**
也可以指定list 为起底层实现，初始化queue的语句如下：
`std::queue<int, std::list<int>> third; // 定义以list为底层容器的队列`

> 栈和队列都不归类为容器，而是容器适配器container adapter
> 栈提供push 和 pop 等等接口，所有元素必须符合先进后出规则，所以栈不提供走访功能，也不提供迭代器(iterator)。 不像是set 或者map 提供迭代器iterator来遍历所有元素。队列中先进先出的数据结构，同样不允许有遍历行为，不提供迭代器.


# 容器系列

## 删除/插入操作
### 队列（Queue）
push(): 插入元素至队尾
pop(): 取出队头元素
**front(): 访问队头元素**
**back(): 访问队尾元素**
### 栈（Stack）
push(): 插入元素至栈顶
pop(): 取出栈顶元素
**top(): 访问栈顶元素**
### 双向队列（Deque）
push_back()
push_front()
pop_back()
pop_front()
front()
back()
### 向量（Vector）
push_back()：插入至数组尾部
pop_back(): 取出数组尾部元素
insert(iterator position, [n], val): 插入[n]个相同的元素val至position（迭代器）
erase(iterator first, [iterator last] ): 删除指定位置元素（迭代器）

## set
### 创建
使用头文件：`#include<set>`
```cpp
/*创建set对象，共5种方式,如果无自定义函数对象,则采用系统默认方式*/
//方式1：创建空的set对象，元素类型为int
set<int> s1;
//方式2：创建空的set对象，元素类型为char*,比较函数对象（即排序准则）为自定义strLess
set<const char*,strLess> s2(strLess);
//方式3：利用set对象s1,拷贝生成set对象s2
set<int> s3(s1);
//方式4：用迭代区间[&first,&last]所指的元素，创建一个set对象
int iArray[] = {13,32,19};
set<int> s4(iArray,iArray+3);
//方式5：用迭代区间[&first,&last]所指的元素，及比较函数对象strLess,创建一个set对象
const char* szArray[] = {"hello","world","bird"};
set<const char*,strLess> s5(szArray,szArray+3,strLess());
```
### 遍历
1. 迭代器：`for (it=next(ordered_nums.begin()); it!=ordered_nums.end(); it++ )`
2. 取前一个/后一个：`*(prev(it))`, `*(next(it))`
3. 计算两个迭代变量之间的距离：`distance(it1, it2)`
	*注意不能直接相减，也不能用+1 -1来对获取it的下一个或者上一个*
### 操作
```cpp
s.begin()
s.end()
s.clear()
s.empty()
s.insert()
s.erase()  //删除指定的一个元素
s.size() 
```

### 查找
```cpp
/*元素查找：共2种方式*/
//方式1：count(value)返回set对象内元素值为value的元素个数
// 因为key值不会重复，所以只能是1 or 0
cout <<"\ns1.count(10) = "<<s1.count(10)<<",s1.count(80) = " <<s1.count(80)<<endl;
//方式2：find(value)返回value所在位置，找不到则返回end()
cout <<"s1.find(10): ";
if(s1.find(10) != s1.end())
	cout <<"find it"<<endl;
else
	cout<<"not found!"<<endl;

```

### 其他函数
`s1.swap(s2)` ：交换两个set
`lower_bound()`：返回键值>=给定元素的第一个位置
`upper_bound()`：返回键值>给定元素的第一个位置
## map
### 创建
头文件：`#include<map>`

### 插入
三种方式有区别： *即当map中有这个关键字时，insert操作是不能在插入数据的，但是用数组方式就不同了，它可以覆盖以前该关键字对 应的值*

```cpp
// 定义一个map对象
map<int, string> mapStudent;
 
// 第一种 用insert函數插入pair
mapStudent.insert(pair<int, string>(000, "student_zero"));
 
// 第二种 用insert函数插入value_type数据
mapStudent.insert(map<int, string>::value_type(001, "student_one"));
 
// 第三种 用"array"方式插入
mapStudent[123] = "student_first";
mapStudent[456] = "student_second";
```

### 查找
find()函数：找不到返回end()
count()函数： 返回0或1，因为key值不能重复


### 删除与清空
```cpp
//迭代器刪除
iter = mapStudent.find("123");
mapStudent.erase(iter);
 
//用关键字刪除
int n = mapStudent.erase("123"); //如果刪除了會返回1，否則返回0
 
//用迭代器范围刪除 : 把整个map清空
mapStudent.erase(mapStudent.begin(), mapStudent.end());
//等同于mapStudent.clear()
```

### 其他函数
`m1.swap(m2)` ：交换两个map
`lower_bound()`：返回键值>=给定元素的第一个位置
`upper_bound()`：返回键值>给定元素的第一个位置

## 优先级队列

### 实现堆排序
自定义比较函数：注意和vector是相反的
```cpp
struct cmp{
    bool operator()(const string& s1, const string& s2) const{
        // 和vector排序写法相反
        // a < b : [vec] 升序    [pri] 大顶堆
        return (s1.size() < s2.size()) || (s1.size() == s2.size() && s1 > s2);
    }
};

void t_prique(){
    vector<string> strs = {"xhh", "mmcy", "mi", "xhz", "abcdef"};

    priority_queue<string, vector<string>, cmp> pri_que(strs.begin(), strs.end());

    while(!pri_que.empty()){
        cout << pri_que.top().size() << "  " << pri_que.top() << endl;
        pri_que.pop();
    }
}

```

# 头文件
## algorithm

### 二分查找
![[Pasted image 20240412180542.png]]


# 循环
1.  for_each： `for_each(v.begin(), v.end(), print);`
## 哈希表

### 字母异位词：vector

[242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/)

给定两个字符串 `_s_` 和 `_t_` ，编写一个函数来判断 `_t_` 是否是 `_s_` 的字母异位词。
**注意：** 若 `_s_` 和 `_t_` 中每个字符出现的次数都相同，则称 `_s_` 和 `_t_` 互为字母异位词。

解答：
```C++
#include <map>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> table(26,0);
        if(s.length()!=t.length()){return false;}
        for(auto& c:s){
            table[c-'a']++;
        }
        for(auto& c:t){
            table[c-'a']--;
            if(table[c-'a']<0){
                return false;
            }
        }
        return true;
    }
};
```

注意点：

- 创建哈希表： `vector<int> table(26,0);` ——————类似于数组
- 数组长度: nums.size(); 字符串长度 string.length();



### 两数之和：unordered_map

关键语句：
unordered_map中，first指向key，second指向value
`auto it = nummap.find(ttarget);`
`return {it->second,i};`

```C++
#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> nummap;
        int length = nums.size();
        for (int i=0;i<length;i++){
            int ttarget = target-nums[i];
            auto it = nummap.find(ttarget);
            if(it==nummap.end()){
                nummap[nums[i]]=i;
            }
            else{
                return {it->second,i};
            }
        }
        return {};
    }
};
```


## 四数之和：sort函数+排序+双指针

1. 直接用sort函数排序`sort(nums.begin(),nums.end());      // 排序`
2. vector数组用push_back函数：`res.push_back(vector<int>{nums[i],nums[left],nums[right]});`


## 环形链表：set的插入和查询是否存在key

[142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)

```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        //方法一：存储遍历过的结点，遇到第一个重复遇到的结点，即输出
        // unordered_set<ListNode*> visited;
        // while (head!=nullptr){
        //     if(!visited.count(head)){
        //         visited.insert(head);
        //         head=head->next;
        //     }
        //     else{
        //         return head;
        //     }
        // }
        // return nullptr;


        //方法二：双指针-slow & fast
        ListNode *slow=head,*fast=head;
        while(fast!=nullptr){
            slow=slow->next;
            if(fast->next==nullptr){
                return nullptr;
            }
            fast=fast->next->next;
            if(slow==fast){
                ListNode *ptr =head;
                while (slow!=ptr){
                    slow=slow->next;
                    ptr=ptr->next;
                }
                return ptr;
            }
        }
        return nullptr;
    }
};
```


## 不同路径：动态规划

[63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/)

1. 二维数组的维度
```C++
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
    
        int row = obstacleGrid.size();
        int col = obstacleGrid[0].size();

        vector<vector<int>> dp(row, vector<int>(col));
        //初始化，考虑如果有障碍物
        // 00有可能为障碍物
        dp[0][0] = (obstacleGrid[0][0] == 1 ? 0 : 1);

        for(int i=1;i<row;i++){
            dp[i][0] = (obstacleGrid[i][0] == 1 ? 0 : dp[i - 1][0]);
        }
        for(int j=1;j<col;j++){
            dp[0][j] = (obstacleGrid[0][j] == 1 ? 0 : dp[0][j - 1]);
        }

              
        //dp计算
        for(int i=1;i<row;i++){
            for (int j=1;j<col;j++){
                dp[i][j] = (obstacleGrid[i][j] == 1 ? 0 : (dp[i][j - 1] + dp[i - 1][j]));
            }
        }
        return dp[row-1][col-1];
    }
};
```
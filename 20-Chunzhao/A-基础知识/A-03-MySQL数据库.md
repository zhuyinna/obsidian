


# 基本教程@菜鸟教程
冗余，主键，外键，复合键，**索引**
## 索引
### 分类
1. 普通索引
   CREATE INDEX index_name ON TABLE (column1)；
   ALTER TABLE ADD INDEX index_name  (column)；
   CREATE TABLE table_name(....., INDEX idx_age (age));
   删除 DROP INDEX index_name ON table_name; 
   ALTER TABLE table_name DROP INDEX index_name;
2. 唯一索引
   索引中的值是唯一的，不允许有重复值
   CREATE UNIQUE INDEX index_name；
   ALTER table mytable 
	ADD CONSTRAINT unique_constraint_name UNIQUE (column1, column2, ...);
   用法基本和普通索引相同
3. 聚焦索引
   ```ad-question
   是否就是 第一个唯一索引？
   ```

### 其他概念
1. **索引覆盖**
   只需要在一颗索引树就能获取SQL所需的所有列数据，无需回表，速度更快。
2. 怎么实现索引覆盖？
   - 将被查询的字段，建立到联合索引里去
     例如单列索引(name)升级为联合索引(name, sex)
     能够命中name索引，索引叶子节点存储了主键id，通过name的索引树即可获取id和name，无需回表，符合索引覆盖，效率较高。
     画外音，Extra：Using index。
3. 索引下推优化
	   简称ICP优化，取出索引的同时，判断是否可以进行where条件过滤再进行索引查询。——减少回表次数。当你的查询语句的执行计划里，出现了 Extra 为 `Using index condition`，那么说明使用了索引下推的优化。
## 事务
InnoDB存储引擎才有。
特点：原子性、一致性、隔离性、持久性。
BEGIN或者START TRANSACTION
ROLLBACK
COMMIT

## 回表

主键索引的查询：只需要搜索id这颗B+树，就能确定记录。
基于非主键索引的查询：例如对普通索引进行，先搜索索引树，得到主键ID的值，再去ID索引树搜索一次。
明显，主键查询效率更高。 

*结论*
使用聚焦索引（主键或第一个唯一索引）就不会回标，普通索引就会回表

# 基础篇@小林coding
## 执行查询语句

<img src=https://s2.loli.net/2024/03/31/IxiAdk5Ys2LpQgE.png width='100%'>

执行语句的流程
- 连接器
	- 建立连接，管理连接，校验用户身份
	- 基于TCP协议——三次握手四次挥手
	- 长连接 || 短连接
- 查询缓存
	- 比较鸡肋
- 解析SQL
	- 词法分析：关键字，非关键字
	- 语法分析：是否满足MySQL语法，但不会检查表/字段是否存在
- 执行SQL
	- prepare阶段：检查是否存在；替换\*为所有列
	- optimize优化器 ：确定执行方案——例如表里面有多个索引，会选择代价小的索引
	- execute执行器：

## 存储
1. 总体结构
![[Pasted image 20240331212739.png|400]]

2. 行记录存储
   ![[Pasted image 20240331213342.png|550]]
   变长字段长度列表是逆序存储的：记录头信息指向的是下一个记录头信息和真实数据之间的位置，左读就是头信息，右读是数据。可以同时在一个CPU cacheline里，提高CPU cache命中率。
   **NULL值记录信息**：NULL为1，非NULL为0，高位补0来满足一个字节长度，注意也是逆序。   ![[Pasted image 20240331213722.png|675]]

3. 主键索引
   如果使用的是 MyISAM 存储引擎，B+ 树索引的叶子节点保存数据的物理地址，即用户数据的指针，如下图：
   <img src=https://s2.loli.net/2024/03/31/HYqdLfc1SzuINE7.png width='100%'>
   
   如果使用的是 InnoDB 存储引擎， B+ 树索引的叶子节点保存数据本身，如下图所示：
   <img src=https://s2.loli.net/2024/03/31/7mHDwaBXg1izdQ6.png width='100%'>
   
# 索引篇@小林coding

## TL;DR
<img src=https://s2.loli.net/2024/03/31/ao3npGMCZghXEQO.png width='100%'>
<img src=https://s2.loli.net/2024/03/31/QWpIUwAG4y9EPLn.png width='100%'>


### 联合索引

1. 联合索引：最左匹配原则

 <img src=https://s2.loli.net/2024/03/31/Li4aNQT3cJVDdAl.png width='100%'>
 
1. 联合索引：范围查询
   联合索引的最左匹配原则会一直向右匹配直到遇到「范围查询」就会停止匹配。**也就是范围查询的字段可以用到联合索引，但是在范围查询字段的后面的字段无法用到联合索引**。

### 索引失效

1. 当我们使用左或者左右模糊匹配的时候，也就是 `like %xx` 或者 `like %xx%` 这两种方式都会造成索引失效。
2. 用一些 MySQL 自带的函数来得到我们想要的结果，这时候要注意了，如果查询条件中对索引字段使用函数，就会导致索引失效。（原因：索引保存的是索引字段的原始值，而不是经过函数计算后的值，自然就没办法走索引了）
3. 查询条件中对索引进行表达式计算
4. 对索引隐式类型转换
   > mysql会将字符串转为数字，如果需要比较的类型不同，如果转换部分是在key上，则导致索引失效。如果转换部分在value上，则还是走索引扫描。
5. 联合索引非最左匹配
6. where子句的or：如果or前是索引列，or之后不是



# 事务篇@小林coding
## 并发事务问题

### 脏读
**如果一个事务「读到」了另一个「未提交事务修改过的数据」，就意味着发生了「脏读」现象。**
### 不可重复读
**在一个事务内多次读取同一个数据，如果出现前后两次读到的数据不一样的情况，就意味着发生了「不可重复读」现象。**

### 幻读
**在一个事务内多次查询某个符合查询条件的「记录数量」，如果出现前后两次查询到的记录数量不一样的情况，就意味着发生了「幻读」现象。**

## 解决方法
- **读未提交（_read uncommitted_）**，指一个事务还没提交时，它做的变更就能被其他事务看到；
- **读提交（_read committed_）**，指一个事务提交之后，它做的变更才能被其他事务看到；
- **可重复读（_repeatable read_）**，指一个事务执行过程中看到的数据，一直跟这个事务启动时看到的数据是一致的，**MySQL InnoDB 引擎的默认隔离级别**；
- **串行化（_serializable_ ）**；会对记录加上读写锁，在多个事务对这条记录进行读写操作时，如果发生了读写冲突的时候，后访问的事务必须等前一个事务执行完成，才能继续执行；

<img src=https://s2.loli.net/2024/03/31/Krt7DGBlhFsw9Li.png width='100%'>
#Todo 

# 锁篇@小林coding



# TODO：问题汇总
#todo
1. sql，mysq区别
2. MVCC实现
# 概念
```ad-question
redis和Mysql区别？
```

类型上和存储方式上：
mysql是关系型数据库，存于磁盘。redis是非关系型数据库，也就是缓存数据库，能够大大提高运行效率，但是存储时间有限。
作用上：
mysql用于存储持久化数据，功能强大，但是速度慢。redis用于存储读取频繁的数据在缓存上，读取速度快。
适用存放的数据：
redis适用于频繁访问的，例如消息队列推送、好友关注、排行榜等。
一般是mysql(主要)+redis(辅助)

## redis数据类型


![[Pasted image 20240330145852.png]]


**String（字符串），Hash（哈希），List（列表），Set（集合）、Zset（有序集合）**
和底层的数据结构的对应关系：
![[Pasted image 20240402141859.png]]

### String
String 类型的底层的数据结构实现主要是 int 和 SDS（简单动态字符串）
字符串对象的内部编码（encoding）有 3 种 ：**int、raw和 embstr**。
- int
- raw：短文本，只读，一次性分配空间（redisobject+SDS）
- embstr：长文本，可写，分配两次空间
	常用命令：SET, GET, DEL, MSET(批量设置)，MGET, INCR,  INCRBY .. 10, DECR, DECRBY ... 10, SETNX(不存在就插入)
场景：在开发后台管理系统时，会使用 Session 来保存用户的会话(登录)状态，这些 Session 信息会被保存在服务器端，但这只适用于单系统应用，如果是分布式系统此模式将不再适用。因为分布式系统会在用户登录时，把请求随机分配到不同的服务器，所以需要redis进行session共享。

### List
List 类型的底层数据结构是由**双向链表或压缩列表**实现的：
**在 Redis 3.2 版本之后，List 数据类型底层数据结构就只由 quicklist 实现了，替代了双向链表和压缩列表**。
常用命令：
LPUSH, RPUSH, LPOP, RPOP
场景：
消息队列 LPUSH + RPOP （或者反过来，RPUSH+LPOP）命令实现消息队列。
缺陷：不支持多个消费者读取同一条消息，这个问题由Redis 从 5.0 版本开始提供的 Stream 数据类型解决。

### Hash
hash相比于string，更适合存储对象。
Hash 类型的底层数据结构是由**压缩列表或哈希表**实现的**在 Redis 7.0 中，压缩列表数据结构已经废弃了，交由 listpack 数据结构来实现了**。
```python
# 存储一个哈希表key的键值
HSET key field value   
# 获取哈希表key对应的field键值
HGET key field

# 在一个哈希表key中存储多个键值对
HMSET key field value [field value...] 
# 批量获取哈希表key中多个field键值
HMGET key field [field ...]       
# 删除哈希表key中的field键值
HDEL key field [field ...]    

# 返回哈希表key中field的数量
HLEN key       
# 返回哈希表key中所有的键值
HGETALL key 

# 为哈希表key中field键的值加上增量n
HINCRBY key field n        
```

应用场景:
缓存对象，购物车

### Set
Set 类型的底层数据结构是由**哈希表或整数集合**实现的：

- 如果集合中的元素都是整数且元素个数小于 `512` （默认值，`set-maxintset-entries`配置）个，Redis 会使用**整数集合**作为 Set 类型的底层数据结构；
- 如果集合中的元素不满足上面条件，则 Redis 使用**哈希表**作为 Set 类型的底层数据结构

应用场景：
*无序、不可重复、支持并交差等操作。*

不可重复：点赞、抽奖
支持聚合运算（并交差）：共同关注


### Zset

不能有重复元素+有序。
Zset 类型的底层数据结构是由**压缩列表或跳表**实现的：


### Bitmap

底层是String实现。只有0和1
场景：由于 bit 是计算机中最小的单位，使用它进行储存将非常节省空间，特别适合一些数据量大且使用**二值统计的场景**。eg：签到统计、用户登录

### Stream

Redis Stream 是 Redis 5.0 版本新增加的数据类型，Redis 专门为消息队列设计的数据类型。在5.0之前：
	- 发布订阅模式：不能持久化也就是无法可靠保存消息，客户端离线再重连无法读取到历史消息 #todo (什么是发布订阅模式？)
		- ![[Pasted image 20240402153104.png]]
	- List实现队列：不能重复消费，需要生产者自己生成一个全局唯一ID
stream改进：
- 消息保序：XADD/XREAD（时间戳+当前时间戳中的序号）
- 阻塞读取： XREAD block，可以设置时间
- 重复消息处理：XADD 自动生成ID
- 消息可靠性：PENDING LIST保存被消费者读取但未发送ACK确认的消息
- 支持消费组：组内不能重复消费，但是不同组可以（用于同一个组快速处理消息）
stream问题：
- 消息丢失：生产者和消费者都不会，但是消息中间件会
  ![[Pasted image 20240402152819.png]]
  - 消息可堆积吗？redis数据都存储在内存中，有可能OOM，可以指定队列最大长度，如果超出了则删除旧消息。
综上：redis作为消息队列可能有两个问题：1. 丢数据； 2. 消息挤压造成资源紧张。


### 其他
HyperLogLog：提供不精确的去重基数统计，相比Hash和Map非常节省空间(12k)
	百万级网页 UV 计数
GEO：底层是sorted set，存储地理位置
	滴滴叫车

# Redis线程模型--单线程

![[Pasted image 20240402154519.png|475]]

1. 初始化
    - 调用epoll_create函数创建一个epoll，调用socket创建一个服务端socket
    - bind（）端口，调用listen监听该socket
    - epoll_ctl()将 listen socket 加入到 epoll，同时注册「连接事件」处理函数
2. 事件循环函数（蓝色部分）
	- 处理发送队列函数：如果有，触发write函数将客户端发送缓存区里的数据发送出去
	- 调用 epoll_wait 函数等待事件的到来
		  连接事件：调用 accpet 获取已连接的 socket -> 调用 epoll_ctl 将已连接的 socket 加入到 epoll -> 注册「读事件」处理函数
		  read事件：read，解析，执行，把客户端对象添加到发送队列，执行结果加入到缓存，write
		  write事件：发送，如果这一轮没法送完，继续注册write，等待 epoll_wait 发现可写后再处理 。

```ad-question
单线程为什么还这么快？
```
- 大部分都在内存中完成，并且采用了高效的数据结构
- 避免了多线程的竞争：例如线程切换带来的时间和性能开销，死锁等
- I/O多路复用机制：允许内核同时存在多个监听socket和已连接socket，就实现了一个 Redis 线程处理多个 IO 流的效果。
注意多线程I/O，不代表redis是多线程，redis仍然是单线程。

# Redis持久化
- AOF日志
  先执行命令，再把命令记录到AOF（磁盘）
  ![[Pasted image 20240402173543.png]]
  AOF 日志过大，会触发AOF重写机制，压缩。
  Redis 的**重写 AOF 过程是由后台子进程 _bgrewriteaof_ 来完成的**：注意是一个子进程，而不是线程： - 子进程重写期间，主进程可以继续处理，避免阻塞； - 避免了多线程会加锁导致性能下降的问题。子进程和主进程资源共享，但是是只读，如果发生了写，会进行【写时复制】，避免了加锁。
  【写时复制】可能导致复制之后主进程改变了数据，导致数据不一致？Redis 设置了一个 **AOF 重写缓冲区**，这个缓冲区在创建 bgrewriteaof 子进程之后开始使用
- RDB快照
  两个命令：save 和 bgsave。其中save在主线程执行，会阻塞主线程。bgsave会创建一个子进程，不会阻塞。
- 混合
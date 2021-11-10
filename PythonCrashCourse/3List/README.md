
# List

## 访问

list[0] -> list[-1]

## 修改

list[i] = a

## 增加

list.append(element)

list.insert(index, element)  //摆放到 index 处，其他后移

## 删除

1. 使用del语句删除元素。需要知道索引，没有返回值

`del list[index]`

2. 使用pop()方法。如果没有传入参数，默认删除列表最后一个元素；如果有参数，并且参数为列表的索引，则删除指定索引的值。返回值为被删除的值

receive = list.pop()

receive = list.pop(index)


3. 根据列表中的值来删除元素,remove(value)。没有返回值,且只删除第一个指定的值


list.remove(value)


## 排序

### 永久改变

list.sort()  //字典排序方法

list.sort(reverse=True)


### 临时改变

sorted(list)


## 翻转


list.reverse()

reversed(list)  //区别同上

## 长度

len(list)

## 操作

eg1:

```python
for element in list:
    pass
```

eg2: 可以方便计数

range(start, end, step)

```python
for value in range(start, end): #range 遵循左闭右开的原则
    pass
```

eg3: list 解析 `!!! 觉得非常简洁好看 !!!`

形同集合的描述方法

```python
squares = [value**2 for value in range(1,11)]
```


## 切片

clip = list[start:end]  //也是符合左闭右开，index 是从 0 开始的

clip = list[:end] // 默认从 0 开始

clip = list[start:] // 终点结束，包含最后一个

print(list[1:-1])  // ok



## 复制  利用切片

创建一个同时省略起始索引和终止索引的切片。复制，是创造一个副本，而不是让两个变量都指向同一个列表。

friend_food=my_food[:] #复制my_food列表，是两个列表，创造了一个副本

friend_food=my_food #将friend_food这个列表指向my_food这个列表


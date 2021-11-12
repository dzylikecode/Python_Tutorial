
# dictionary

## 形式

dict = {key1:value1, key2:value2}

空

dict = {}

## 访问

dict[key]


## 增加

dict 不关心顺序，只关心映射

dict[new_key] = new_value


## 删除

del dict[key]


## 遍历

```python
# key and value
for key, value in dict.items():
    pass

# key
for key in dict.keys():
    pass

# key
for key in dict:
    pass

# sorted keys
for key in sorted(dict.keys()):
    pass

# value
for key in dict.values():
    pass

# value to keep unique
for key in set(dict.keys()):
    pass

```


### 嵌套

复合利用列表和字典
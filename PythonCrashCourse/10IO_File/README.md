rstrip() 可以删除末尾的换行符 `\n`

```python
# r means raw string
a = r'hello\world'

with open(file, 'r') as f:
    for line in f.readlines():
        pass
with open(file, 'r') as f:
    for line in f: # is the same as above ?
        pass
```

【Python 文件使用方式标识详解】

1.  r':默认值，表示从文件读取数据。

2. 'w':表示要向文件写入数据，并截断以前的内容

3. 'a':表示要向文件写入数据，添加到当前内容尾部

4. 'r+':表示对文件进行可读写操作（删除以前的所有数据）

5. 'r+a'：表示对文件可进行读写操作（添加到当前文件尾部）

6. 'b':表示要读写二进制数据


Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。



## 储存数据

json `[javascript object notation]`


存入 json

json.dump(list, file_object)

加载

list = json.load(file_object)

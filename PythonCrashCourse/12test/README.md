

# 测试



[单元测试](https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936)

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行


SetUp 类似 init 但是 init 是给类实现用的，测试框架用 Setup

可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码
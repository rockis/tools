# 一些小工具

## dumpstack.py

排查Java高CPU占用原因的工具，用可以导出一个java进程CPU占用高的线程栈
用法 :
```
python dumpstack.py <pid> 
```

命令执行成功后在生成的*top.txt*中查看占用cpu高的线程id，在jstack.txt根据pid查询对应的线程栈
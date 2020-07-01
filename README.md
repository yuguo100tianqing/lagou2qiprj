#python环境笔记
##git命令
git add README.md（创建）
git config --global user.email "you@example.com"（第一次使用git需要配置）
git config --global user.name "Your Name"（第一次使用git需要配置）
git commit -m "first commit"（提交到本地仓库）
git remote add origin https://github.com/yuguo100tianqing/lagou2qiprj.git （与远程建立连接）
git push -u origin master（将本地的代码push到远程仓库）

#参考链接
https://github.com/yuguo100tianqing/lagou2qiprj.git
#python实战（一）作业
1、搭建好python,pycharm, git 环境，在本地创建一个pythoncode，和README.MD, 上传到github上，将代码github链接地址贴到作业贴下即可。 
2、创建模块，模块里面创建方法，定义有参数，和无数，有返回值和无返回值的情况，并说明 无返回值的默认返回值。
#python实战（二）作业
1、创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

2、创建子类【猫】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=短毛，
- 添加一个新的方法， 会捉老鼠，
- 复写父类的‘【会叫】的方法，改成【喵喵叫】

3、创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】

4、创建一个猫猫实例
- 调用捉老鼠的方法
- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。

5、创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。

6、使用 yaml 来管理实例的属性

7、提交代码到自己的github仓库， 贴到作业贴上
#pytest作业（一）
1、补全计算器（加减乘除）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、conftest.py中创建fixture 完成setup和teardown
4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】



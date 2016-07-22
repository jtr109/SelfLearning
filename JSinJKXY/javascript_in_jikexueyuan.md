# JavaScript in JiKeXueYuan
## 课堂笔记
`function`定义中，`argument`为传入参数。

`console.log()`：在`console`中输出。

`document.write()`打印输出。

## JavaScript 语法详解
### 改变页面内容的方式
    <p id="myid"><p>
    <script>
        var m = "abc";
        document.getElementById("myid").innerHTML=m;
    </script>
### 加法运算符
任何类型与字符串相加都会转化为字符串类型
### 比较运算符
`==`要求值相等

`===`要求值和类型均相等
### 条件运算符
#### switch语句
    switch(i) {
        case 1:
            break;
        case 2:
            break;
        ...
        default:  // 以上case均不满足
            break;
    }
## JavaScript函数
### 带参数的函数
参数在传递时，其顺序必须一致。
### 局部变量和全局变量
在`function`中的变量：
    var n = 10; m = 10; // 全局变量
    function demo() {
        var i = 10; //局部变量
        x = 10; //全局变量
    }
    
## JS面对对象
创建对象方法一：

    (function(){  // 闭包方式
        var n = "ime";  // 局部变量，只能在类中访问
        function People(name) { // 创建函数，当作类使用
            this._name = name;  //指定参数
        }
        People.prototype.say = function() { // 创建类的方法、属性
            alert("peo-hello" + this._name + n);
        }
        window.People = People;  //加入窗口，向外部公开接口
    }()); // 使类自己执行
    
    (function(){
        function Student(name) { // 创建类
            this._name = name;  // 子类指定参数
        }
        Student.prototype = new People(); // 继承
        var superSsay = Student.prototype.say;
        Student.prototype.say = funciton(){
            superSsay.call(this);
            alert("stu-hello"+this._name);
        }
        window.Student = Student;
    }());

    var s = new Student("iwen"); // 创建对象
    s.say();
    
创建对象方法二：

    (function(){  // 闭包
        var n = "ime";  // 内部变量
        function Person(name) {
            var _this = {};  // 创建空对象,承载属性、方法
            _this._name = name;  // 定义属性
            _this.sayHello = function () {  // 定义方法
                alert("PHello" + _this._name + n);  // 方法行为
            }
            return _this;  // 重要:返回_this
        }
        window.Person = Person;
    }());
    
    (function () {
        function Teacher(name) {
            var _this = Person(name);
            var superSay = _this.sayHello;  // 调用父类方法
            _this.sayHello = function () {  // 覆写
                superSay.call(_this);  // 强制调用父类
                alert("THello" + _this._name);
            }
            return _this;
        }
        window.Teacher = Teacher;
    }());
    
    var t = Teacher("iwen");
    t.sayHello();
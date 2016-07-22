/**
 * Created by jtr109 on 6/23/16.
 */
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
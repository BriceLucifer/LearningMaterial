# JS_FEATURES
## static

- 不加static和加static的区别：
1. static属性和方法 可以不用实例化就可以使用
2. 没有static的属性和方法 必须实例后使用
3. 对于实例化后的对象, 不可以访问static关键字的属性和方法

```JS
// 示例代码
class aaa{
    static age=100000;
    static logt(){
        return  "love❤";
    }
    year = 2004;
    yearprint(){
        return ++this.year;
    }
}
console.log(aaa.age);
console.log(aaa.logt());

const a = new aaa();
console.log(a.year);
console.log(a.yearprint());
console.log(aaa.year);
```
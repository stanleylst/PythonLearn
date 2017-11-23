/**
 * Created by stanley on 12/11/2017.
 */

//  单行注释, c语言类型
// console.log('hello world')

/*
    多行注释  不能嵌套
 */

// 常量/变量

// 定义变量
// var v = 3;  // 该种变量定义的方式是为了兼容旧版
// console.log(v);
//
// let x = 4;  // 新版引用的定义方式，如果没有特别原因，变量都应该使用let定义，因为var定义变量，会提升作用域，即所有var定义的作用域为全局作用域
// console.log(x)


// 定义常量
// const x = 5;  // 常量不能重新赋值
// let y = 6;  // 变量也不能重新赋值

// 什么时候选择常量，什么时候选择变量？
// 如果没有特殊需求都应该使用常量而不是变量，可以减少 BUG 机率


// 数据类型

// number 数值型， 包括整型和浮点型
// boolean 布尔型，包括true和false
// string 字符串
// null 只有一个值，就是null
// undefined 只有一个值，就是undefined
// symbol ES新引入
// object 复合类型，以上5种属于基本类型



// ES 属于弱类型语言

// const x = 3;
// console.log(typeof(x));
//
// const y = 'hello world';
// console.log(typeof(y));
//
// const z = x + y;   // number 类型隐式转化成了string类型
// console.log(z)
// console.log(typeof(z))


// console.log(typeof(3 + false))
// console.log(typeof('hello' + false))
// console.log(typeof(3 + null))
// console.log(typeof('hello' + null))
// console.log(typeof(false + null))
// console.log(typeof(null + undefined))

// 优化权：  null/undefined < boolean < number < string
// 当优先权小的和优先权大的运算，会隐式转化为优先权大的类型
// 不依赖隐式转化，需要做显示转化


// null和undefined区别
//
// console.log(xxx == undefined)

// let k = {
//     a: 3
// }
//
//
// console.log(k.b === undefined)
// console.log(k.b === null)


// 字符串
// 可以是双引号，单引号  ==> 没有任何区别
// 也可以使用反引号定义， 允许写在多行，且会自动保留换行符,允许插值(引入变量)

// let name = 'stanley'
// let z = `this
// is string ${name}`
// console.log(z)
//
//
// // 分支结构
// if(3 < 5){  // 大括号开始新的语句块，条件必须用小括号
//     console.log('3 < 5');
// }


// 算术运算符   x++  x--
// 自增操作只能用在变量上，不能使用在常量上
// 加号在后，表示先求值，后自增，加号在前则刚好相反

// 比较运算
// console.log(3 < 5);
// console.log(3 <= 5);
// console.log(3 > 5);
// console.log(3 >= 5);
// console.log(3 === 5);
// console.log(3 !== 5);
//
// console.log('3' == 3);   // 只比较值，不比较类型
// console.log('3' === 3);  // 值和类型都比较


// 逻辑运算  && || !
// console.log(true && true)  // and
// console.log(true || true)  // or
// console.log(!false)  // not

// 短路操作
// function  yes(){
//     console.log('yes')
//     return true
// }
//
// function no() {
//     console.log('no')
//     return false
// }
//
// console.log(yes() || no())
// console.log(no() && yes())


// 三元运算符，条件运算符   条件 ？ 真值:假值
// console.log(3>5 ? '3>5':'3<5');

// 逗号操作符 允许将多个语句写到一起
// let x = 3, y = 5;



// 流程控制

// 分支结构  使用大括号区别代码块. 从ES6开始，ES支持块级作用域，每个大括号开启一个新的作用域
//
// let pp = 3;
// {
//     let pp = 4;
//     console.log(`pp in block is ${pp}`)
// }
// console.log(`pp is ${pp}`)


// if (){
//
// } else {
//
// }
//
//
// if (){
//
// }else if (){
//
// }else if (){
//
// }else {
//
// }


//
// let x = 1
// switch (x) {
//     case 1:
//         console.log(1);
//         break   // 避免穿透
//     case 2:
//         console.log(2)
//         break
//     default:
//         console.log('default')
// }

// 循环  c语言风格的循环
// for (let x = 0; x < 10; x++) {
//     console.log(x)
// }


// for  .. in 循环，但返回的是索引
//
// let arr = [1, 2, 3, 4]
// let obj = {
//     a: 1,
//     b: 2,
//     c: 3
// }
//
// console.log(arr[2])
// console.log(obj.a)  // 使用点操作符或下标操作符访问
// console.log(obj['b'])  // 使用点操作符或下标操作符访问


// for (let idx in arr) {
//     console.log(idx)  // 结果却是从0开始的，因为返回的是索引
//     console.log(arr[idx])  // 返回value值
// }



// for (let key in obj) {
//     console.log(key)
//     //console.log(${key}})
// }


// for .. of 迭代数据，返回值，不能迭代字典
// for (let v of arr) {
//     console.log(v)  // 返回值
// }

// while语句  当while语句满足的时候执行
// let x = 0
// while (x < 10) {
//     console.log(x)
//     x++
// }


// do while语句
// let x = 0
// do {
//     console.log(x)
//     x++
// } while (x < 10)
//


// 标签语法  当加了标签之后 ，break到标签指定的地方。 通常结合 continue 和 break 搭配使用
// for (let x of [0, 1, 2, 3]) {
//     for (let y of [2, 3, 4, 5]){
//         if (y > 2) {
//             break
//         }
//     console.log(`${x} -> ${y}`)
//     }
// }


//
// outter: for (let x of [0, 1, 2, 3]) {
//     for (let y of [2, 3, 4, 5]){
//         if (y > 2) {
//             break  outter
//         }
//         console.log(`${x} -> ${y}`)
//     }
// }

/*
  * 函数定义
 */

// function add(x, y) {
//     return x + y
// }
//
// let val = add(1, 3)
// console.log(val)


/*
函数表达式
 */
//
// const add = function (x, y) {
//     return x + y
// }
//
// let val = add(3,4)
// console.log(val)


// 也可以直接调用
// let val = function (x, y) {
//     return x + y
// }(1,10)
// console.log(val)


// 递归


// 高阶函数
//
// const map = function (arr, fn) {
//     const result = []
//     for (let v of arr){
//         result.push(fn(v))
//     }
//     return result
// }
//
// const square = function (x) {
//     return x * x;
// }
//
// const val = map([1,2,3,4],square)
// console.log(val)

// const val = map([1, 2, 3, 4], function (x) {
//     return x * x
// })
// console.log(val)


// 箭头函数
// const square = (x) => {
//     return x * x
//     }

// const square = x => {  // 当只有一个参数时，可以省略参数小括号
//     return x * x
// }

// const square = x => x * x;  // 当只有一个参数，且函数体只有一个表达式时，可以当省略大括号和return
// console.log(square(4))

//
// const counter = function () {
//     let c = 0
//     return function () {
//         return ++c
//     }
// }
//
// const c = counter()
//
// for (let x in [1,2,3,4]){
//     console.log(c())
// }




// 函数的参数
//
// const add = function (x, y) {
//     return x + y
// }
//
// console.log(add(2,4))


// 默认参数
// const add = function (x, y =5) {
//     return x + y
// }
//
// console.log(add(2))
//
// const add = function (x = 4, y =5) {  // 默认参数也可以在前，ES没有关键字参数
//     return x + y
// }
//
// console.log(add(2))


// 可变参数

//
// const sum = function(...args) {
//     //console.log(args)
//     let ret = 0
//     for (let v of args) {
//         ret += v
//     }
//     return ret
// }
//
// const val = sum(1,2,3)
// console.log(val)


// 参数解构
//
// const add = function (x, y) {
//     return x + y
// }
//
// console.log(add(...[1,2]))  // 也是3个点号，支持参数解构

// 参数解构不能用object


// 多返回值

// const fn = function () {
//     return 1,2
// }
//
// console.log(fn())   // 只能返回最后一个值，因此不支持多返回值
//
// const fn = function (...args) {
//     console.log(arguments)
// }
//
// fn(1,2,3,4)


// ES6 实现面向对象   1. 使用class定义类； 2. 使用constructor构造方法；  3. 使用new关键字实例化对象
// class Point {
//     constructor(x,y) {
//         this.x = x;
//         this.y = y;
//     }
//
//     point() {
//         console.log(`<${this.x}>, ${this.y}`)
//     }
// }
//
//
// let point = new Point(3, 5)
// console.log(point.x)
// console.log(point.y)

//ES没有私有属性
//静态方法

// class Point {
//     constructor(x,y) {
//         this.x = x;
//         this.y = y;
//     }
//
//
//     static info(){
//         console.log('this is static method')
//     }
// }
//
// let point = new Point(1,2)
// point.info()   // 实例方法不能直接调用静态方法
// point.constructor.info()   // 静态方法必须通过constructor调用



// // * 静态属性 当前nodejs还不支持
// class Point {
//     static offset = {
//         x: 1,
//         y: 2
//     }
// }

// this 函数的坑
/*
* JS中，this的值是由上下文决定的，解决方案如下：
* 1. 显示传递，但是丑陋
* 2. bind方法  ==> 通常的解决方案
* 3. 使用箭头函数  // 不可靠，子类会无法重写他
 */

// 类的继承

// class Point3D extends Point {
//     constructor(x, y, z){
//         // // this.z = x + y // this 不能在super之前使用，会出现undefined报错
//         // super(x, y)
//         // this.z = z
//         constructor(`x: ${x}, y: ${y}`)
//         super(x, y)
//         this.z = z
//         this.format = this.format.bind(this)
//     }
//
//     print(format) {
//         // 调用父类的print
//         super.print(format)  // 注意和构造函数的区别
//         console.log(this.z)
//
//     }
//
//     format() {
//         return super.format() + 'xxx'  // 方法重写
//     }
// }
//
// let p = new Point3D(3, 5, 8)
// p.print(p.format)
//

/*
* 高阶对象, MixIn 模式
 */

/*
异常处理
 */


// throw new Error('some error')

// throw 'some error 2'  // throw 抛出异常，异常对象可以是任意对象

//
// try {
//     throw {message: 'some error', code: 500}
// } catch(err){
//     console.log(`${err.message}: ${err.code}`)     // 使用catch捕获异常，有且仅有一个catch子句
// } finally {
//     console.log('finally')                       // 可选的finally子句，finally块始终执行
// }

/*
模块
 */

// ES6之前都没有自己的模块化系统 : 因为ES是前端程序，难度要比服务端语言困难很多，代码不存在本地，代码都需要远程下载，因此没有ES6之前都没有模块化

// nodejs 不支持模块导入,导入方式如下

// mod_a.js
// export class A {
//     print（） {
//         console.log('class A')
// }
// }

// mode_import.js
// import {A} from 'mod_a'
// require('./mode_a')



// 代码转义
// http://babeljs.io/  把不支持的语法转化为支持的语法，前端开发者比较激进，不会去等浏览器支持,因此把语法转化为浏览器支持的命令

// sourcemap 支持debug找到对应的源代码


// 解构

// const arr = [1,2]
// const [a, b] = arr
// console.log(a)
// console.log(b)

// const [a, b, ] = [1, 2, 3]
// console.log(a,b)

// const obj = {
//     a: 1,
//     b: 2,
//     c: 22
// }

// const {a, b, c} = obj
// console.log(a, b, c)


// const {a: A, b: B} = obj
// console.log(A, B)


// const {a: A, b: B, d:D = 18} = obj
// console.log(A, B, D)

/*
嵌套结构
 */
//
// const arr = [1, [2, 3], 4]
// const [a, [b, c, e=12], d] = arr
// const [a, [b, ...c], d] = arr
// console.log(a, b, d, e)
//


// arr 操作
// const arr = [1, 2, 3]
// console.log(arr)
// arr.push(4)
// console.log(arr)
// console.log(arr.pop())
// console.log(arr)
/*
map方法
//  */
// const sqr = arr.map(x => x * x)   // 返回新的数组
// console.log(sqr)

// arr.forEach(x => console.log(x))  // foreach不返回新的数组
// console.log(arr.filter(x => x % 2 === 0))

// obj

const obj = {
    a: 1,
    b: 2,
    c:3
}
//
// console.log(Object.keys(obj))   // 返回所有的key
// console.log(Object.values(obj))   // 返回所的value
// console.log(Object.entries(obj))  // 返回所有的entry

const copy = Object.assign({},obj,{c: 44});
console.log(copy)








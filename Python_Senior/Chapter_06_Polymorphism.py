# 类的特性 多态
"""
    有时候一个类会有多种表现形式，比如网站页面有个button按钮，这个button按钮的设计可以不一样（单选框、多选框、勾选按钮，提交按键），尽管形状不同
    但他们都有一个共同的调用方式就是 onClick()方法。只要在页面上点击就会触发这个方法，点击后有的会变成选中形态，有的会提交表单，有的会弹窗。
    这种多个对象共用一个接口，又表现的形态不一样的现象，称为多态（Polymorphism）
"""

# 多态代码演示
class Dog(object):
    

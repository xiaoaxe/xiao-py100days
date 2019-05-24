#!/usr/bin/env python
# encoding: utf-8

"""
@description: adv class

@author: baoqiang
@time: 2019-05-24 20:29
"""

from math import sqrt
from abc import ABCMeta, abstractmethod


# 抽象类
class Pet(metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def run_pet():
    pets = [Dog("旺财"), Cat("凯蒂"), Dog("大黄")]

    for pet in pets:
        pet.make_voice()


#

class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2

        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def run_triangle():
    a, b, c = 3, 4, 5

    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
        print(Triangle.perimeter(t))
    else:
        print("无法构成三角形")


class Person:
    # 限制属性只能是这三个，只对当前类有作用，对子类没有任何作用
    __slots__ = ["_name", "_age", "_gender"]

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print("%s正在玩飞行棋." % self._name)
        else:
            print("%s正在玩斗地主." % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def run_inherit():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('骆昊', 38, '老叫兽')
    t.teach('Python程序设计')
    t.watch_av()


def run_person():
    person = Person("王大锤", 12)
    person.play()

    person.age = 22
    person.play()

    # person.name = "白元芳"


def run_person2():
    person = Person("王大锤", 12)
    person.play()

    person._gender = "男"
    # person._is_gay = True


if __name__ == '__main__':
    # run_person2()
    # run_triangle()
    # run_inherit()
    run_pet()

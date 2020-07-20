# -*- coding:utf-8 -*-


class SupClass(object):
    X = 1
    Y = 2

    @staticmethod
    def average(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        # 通过类名调用，如果类名修改，此处需要修改不太方便
        return SupClass.average(SupClass.X, SupClass.Y)

    @classmethod
    def class_method(cls):
        # 通过cls调用，如果类名修改，此处不需要修改
        return cls.average(cls.X, cls.Y)


class Subclass(SupClass):
    X = 3
    Y = 5

    @staticmethod
    def average(*mixes):
        return sum(mixes) / 3


if __name__ == '__main__':
    func = Subclass()
    print(func.static_method())  # Function.average(Function.X, Function.Y) = 1.5
    print(func.class_method())  # Subclass.average(Subclass.X, Subclass.Y) = 2.66666666666

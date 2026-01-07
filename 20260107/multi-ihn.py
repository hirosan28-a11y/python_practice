class A:    # p291
    def printA(self):
        print("A")


class B:
    def printB(self):
        print("B")


class C:
    def printC(self):
        print("C")


class D(A, B, C):   # クラスA、クラスB、クラスCを継承したクラスD
    def printD(self):
        print("D")

    def printAll(self):
        self.printA()
        self.printB()
        self.printC()
        self.printD()


obj = D()          # クラスDのインスタンスを作成
obj.printA()       # クラスAのprintA()メソッドを実行
obj.printB()       # クラスBのprintB()メソッドを実行
obj.printC()       # クラスCのprintC()メソッドを実行
obj.printD()       # クラスDのprintD()メソッドを実行
obj.printAll()     # クラスDのprintAll()メソッドを実行

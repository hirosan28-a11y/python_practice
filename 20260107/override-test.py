class SuperClass: # p289
    def hoge(self):
        print("SuperClass.hoge")


class SubClass(SuperClass):   # SuperClass を継承した SubClass を定義
    def hoge(self):           # SuperClass のメソッドと同名のメソッドを定義
        print("SubClass.hoge")


it = SubClass()   # SubClass のインスタンスを作成
it.hoge()         # hoge() メソッドを実行

# オーバーライドの意味=親クラスにあるメソッドと「同じ名前」のメソッドを
# 子クラスで定義すると、子クラスの方が優先される（上書きされる）
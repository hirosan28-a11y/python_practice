class SuperClass:   # p290
    def hoge(self, id):
        print("----")
        print("SuperClass.hoge=", id)


class SubClass(SuperClass):
    def hoge(self, id):
        # 基底クラスの hoge メソッドを呼び出す
        super().hoge(id)
        print("SubClass.hoge=", id)


# 基底クラスの hoge メソッドの実行例
rc = SuperClass()
rc.hoge(100)

# 派生クラスの hoge メソッドを実行する
sc = SubClass()
sc.hoge(300)

class A:
    def fun1(self):
        print("Feature_1 of class A")
    
    def fun2(self):
        print("feature_2 of class A")


class B(A):
    def fun1(self):
        print("Modifying feature_1 of class A by class B")

    def fun2(self):
        print("Modifying feature_2 of class A by class B")
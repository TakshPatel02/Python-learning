# MRO : Method Resolution Order
# it is the order in which python looks for a method in a hierarchy of classes.

class A:
    label = "A : base class"

class B(A):
    label = "B : masala blend"

class C(A):
    label = "C : herbal blend"

class D(C , B ):
    pass

cup = D()
print(cup.label) # it will print B : masala blend because B comes before C in the inheritance list of D
print(D.__mro__) # the order in which python looks for a method is : D-->B-->C-->A-->object
print(D.mro()) # same as above 
from calc.models import CalcSymbol

a = CalcSymbol('Test')

print(a.name)

# class TestClass:
#     name = 'test class'
#
#     def __test(self):
#         return str(self)
#     def test(self):
#         return str(self)
#     def __str__(self):
#         return f'{self.name}'
#
# # print(TestClass().__test())
#
# def testTypo(testString: TestClass, text='test text') -> str:
#     return f'{testString} + {text}'
#
# print(testTypo(TestClass()))

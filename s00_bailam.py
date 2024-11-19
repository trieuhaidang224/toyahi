#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hi

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/uYheiLdfy6K8LVQj6

--- debai / problem
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi(name='Mom')               | Hi Mom!
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi 1, 22, 333, and 4444!
"""

#endregion debai


#region bailam
def hi(*args):
   result = ''
   length = len(args)

   # Kiểm tra nếu không có đối số hoặc đối số đầu tiên là rỗng hoặc None
   if length == 0 or (args[0] == '' or args[0] is None):
      result = 'Hi!'

   # Nếu chỉ có 1 đối số và nó là None
   elif length == 1:
      result = 'Hi ' + args[0] + '!'

   # Nếu có 2 đối số
   elif length == 2:
      result = 'Hi ' + args[0] + ', and ' + args[1] + '!'

   # Nếu có 3 đối số
   elif length == 3:
      result = 'Hi ' + args[0] + ', ' + args[1] + ', ' + 'and ' + args[2] + '!'

   # Nếu có 4 đối số
   elif length == 4:
      result = 'Hi ' + args[0] + ', ' + args[1] + ', ' + args[
          2] + ', ' + 'and ' + args[3] + '!'

   return result


print('=============================')
print(hi(None))

#endregion bailam

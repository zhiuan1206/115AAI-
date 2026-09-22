# 學生成績格式化輸出範例
name = input('請輸入學生姓名：')
chinese = float(input('請輸入國文成績：'))
english = float(input('請輸入英文成績：'))
math = float(input('請輸入數學成績：'))

print(f'學生姓名：{name}')
print(f'國文成績：{chinese:6.1f}分')
print(f'英文成績：{english:6.1f}分')
print(f'數學成績：{math:6.1f}分')
print(f'平均成績：{(chinese+english+math)/3:6.2f}分')


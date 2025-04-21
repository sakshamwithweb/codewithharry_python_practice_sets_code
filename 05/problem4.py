# What will be the length of following set s:
s = set()
print(len(s))  # 0

s.add(20)
s.add(20.0)
s.add('20')  # length of s after these operations?

print(len(s))  # 2 as 20.0 = 20 because python will check the value

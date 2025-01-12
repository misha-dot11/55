numbers = ['h', '6', 'l']

result = None
if 'h' in numbers:
    result = 'есть несчастливая буква '
else:
    result = 'все ок'
print('результат выражения:\n', result)

result = 'есть несчастливая буква' if 'h' in numbers else 'все ок'
print('результат выражения:\n', result)

print('есть несчастливая буква' if 'h' in numbers else 'все ок')



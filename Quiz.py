# 問題文を出力
print('\n問題{}'.format(quiz + 1))
print(questions[quiz][1])

# 回答選択肢を出力
print('\n---- 回答選択肢 -----')

for i, ans in enumerate(answers):
    print('{}: {}'.format(i+1, ans))

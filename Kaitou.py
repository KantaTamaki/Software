while True:
    user_ans = input('\n回答選択肢を入力してください\n')
    if user_ans in ['1','2','3','4']:
        break
    else:
        continue
print('あなたの回答は{}です'.format(user_ans))
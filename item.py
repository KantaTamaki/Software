# 必要なライブラリの読み込み
import csv
import random


# 問題集ファイル（csv）の読み込み。1行目はヘッダなので読み込まない。
test_file = open('test.csv')
test_data = csv.reader(test_file)
questions = []
for row in test_data:
    if test_data.line_num == 1:
        continue
    questions.append(row)
test_file.close()


# 純不同に出題するためにシャッフル
random.shuffle(questions)


# 正答率を計算するために、初期値として正答数に0をセット
correct_count = 0

# アイテム使用回数を保存
num_used = 0




# ループを回してランダムに出題しながら都度回答を表示
for quiz, question in enumerate(questions):
    # 選択肢を作る　（１）誤りの３つをいれる
    print(quiz)
    answers = []
    reserve = []
    while len(answers) < 3:
        choice = random.randint(1, len(questions))
        if (choice != quiz + 1) and (questions[choice-1][2] not in answers): # 正解ではない、かつ既に含まれていない
            answers.append(questions[choice-1][2])
            reserve.append(questions[choice-1][2])

    # 選択肢を作る　（２）正解を入れる
    correct_ans = questions[quiz][2]
    answers.append(correct_ans)
    reserve.append(correct_ans)

    # 選択肢を作る　（３）シャッフルする
    random.shuffle(answers)

    # 問題文を出力
    print('\n問題{}'.format(quiz + 1))
    print(questions[quiz][1])

    # 回答選択肢を出力
    print('\n---- 回答選択肢 -----')

    for i, ans in enumerate(answers):
        print('{}: {}'.format(i+1, ans))
    if num_used == 0:
        print('{}: {}'.format(5, '50:50'))
        
    # 回答の受付と入力された値のチェック
    while True:
        user_ans = input('\n回答選択肢を入力してください。\n')
        if user_ans in ['1', '2', '3', '4']:
            break
        elif user_ans in ['5']:
            if num_used == 1:
                continue
            num_used += 1
            # 正解の番号の取得
            ans_num = answers.index(questions[quiz][2]) + 1
            while True:
                # 選択肢を消すための数字をランダムで選ぶ
                delete = random.randint(1,4)
                erase = random.randint(1,4)
                if (delete == ans_num) or (erase == ans_num) or (erase == delete): # 正解の番号,またはeraseとdeleteが異なる場合の数字を取得
                    continue
                elif delete > erase:
                    answers[delete-1] = ' '
                    answers[erase-1] = ' '
                else:
                    answers[erase-1] = ' '
                    answers[delete-1] = ' '
                # 問題文を出力
                print('\n問題{}'.format(quiz + 1))
                print(questions[quiz][1])
                print('\n---- 回答選択肢 -----')
                for i, ans in enumerate(answers):
                    print('{}: {}'.format(i+1, ans))
                break
        else:
            continue

    # 正解の表示
    print('\n----- 正解は -----')
    correct_num = answers.index(questions[quiz][2]) + 1
    print('{}: {}'.format(correct_num, questions[quiz][2]))

    # 結果
    if correct_num == int(user_ans):
        print('😀😀😀正解😀😀😀')
        correct_count += 1
    else:
        print('☠️☠️☠️残念☠️☠️☠️')
    print('\n\n■ □ ■ □ ■ □ ■ □ ■ □ ■ □ ■ □ ■ □ ')

# 最終結果を出力
correct_rate = int(correct_count / len(questions) * 100)
print('\n⭐️⭐️⭐️最終結果⭐️⭐️⭐️')
print('正答率は {}％です。{}問中 {}問正解'.format(correct_rate, len(questions), correct_count))


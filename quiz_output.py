import random
questions = []

#問題をシャッフル
random.shuffle(questions)
#ランダムに問題を出題
for quiz,question in enumerate(questions):
    #選択肢を作るコード

    #問題文を出力
    print('\n問題{}'.format(quiz + 1))
    print(questions[quiz][1])

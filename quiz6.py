# 正解の表示
    print('\n----- 正解は -----')
    correct_num = answers.index(questions[quiz][2]) + 1
    print('{}: {}'.format(correct_num, questions[quiz][2]))

    # 結果
    if correct_num == int(user_ans):
        print("結果", "正解です！！")
        correct_count += 1
    else:
        print("結果", "不正解です...")
        #一階層に戻る？
        
    #print('\n\n■ □ ■ □ ■ □ ■ □ ■ □ ■ □ ■ □ ■ □ ')

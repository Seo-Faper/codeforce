def replaceRight(original, old, new, count_right):
    repeat=0
    text = original
    old_len = len(old)
    
    count_find = original.count(old)
    if count_right > count_find : # 바꿀 횟수가 문자열에 포함된 old보다 많다면
        repeat = count_find # 문자열에 포함된 old의 모든 개수(count_find)만큼 교체한다
    else :
        repeat = count_right # 아니라면 입력받은 개수(count)만큼 교체한다

    while(repeat):
      find_index = text.find(old) # 
      text = text[:find_index] + new + text[find_index+old_len:]

      repeat -= 1
      
    return text

print(replaceRight("fffaaa", "f", "b", 2))
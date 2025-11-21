def num_series_normal(numIndexFinal):
    numstring = ""
    cur_num = 0
    cur_num_index = 0
    while cur_num_index < numIndexFinal:
        cur_num += 1
        num_split = list(str(cur_num))
        for num_char in num_split:
            numstring += str(num_char) + " "
            cur_num_index += 1
            if cur_num_index >= numIndexFinal:
                break
    numstring = numstring[:-1] # removing the last space
    return [numstring, cur_num] # numstring -> print string, cur_num -> num at numIndexFinal

print("")
ans_1, ans_2 = num_series_normal(int(input("? n = ")))
print("")
print("final number: ", ans_1, "\n")
print("generated string:", ans_2, "\n")

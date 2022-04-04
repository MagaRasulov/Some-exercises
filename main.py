# def get_result(array_start, array_goal):
#     # Write your code here...
#     j = 0
#     k = 0
#     result = 0
#     for i in array_start:
#         if i != array_goal[j]:
#             result += 1
#             if array_start.index(i) == array_goal.index(array_start[array_goal.index(i)]):
#                 k += 1
#             print(k)
#         j += 1
#     if k == 0:
#         return result - 1
#     else:
#         return result - int(k/2)
#
# print(get_result([3, 2, 1, 4], [1, 2, 3, 4]))



# def get_result(s, symbol):
#     summ_list = []
#     list_s = s.split(' ')
#     space = 0
#     for i in list_s:
#         summ = 0
#         if symbol in i:
#             summ = len(i) + 1 + space
#             for j in list_s[list_s.index(i)+1:]:
#                 if summ > len(j) and symbol not in j:
#                     summ += len(j) + 1
#                 elif symbol in j:
#                     summ += len(j) + 1
#                 else:
#                     summ_list.append(summ)
#                     space = 1
#                     break
#             summ_list.append(summ-1)
#     print(summ_list)
#     result = max(summ_list)
#     return result
# #
# print(get_result("b aaa bbb cc dd eeeeeeeeeeeeeeee bb r sssssssss", "b"))



# def get_result(weight):
#     # Write your code here...
#     result = []
#     if (len(weight) / 4) - (len(weight) // 4) > 0:
#         result.append(int((len(weight) // 4) + 1))
#     else:
#         result.append(int(len(weight) / 4))
#     if (sum(weight) / 420) - (sum(weight) // 420) > 0:
#         result.append(int((sum(weight) // 420) + 1))
#     else:
#         result.append(int(sum(weight) / 420))
#     j = 0
#     print(result)
#     if result[0] == result[1]:
#         weight.sort(reverse=True)
#         print(weight)
#         for i in range(1, result[0]+1):
#             print(sum(weight[j:i*4]))
#             if sum(weight[j:i*4]) > 420:
#                 j += i*4+1
#                 print('я сработал')
#                 continue
#             else:
#                 return result[0]+i-1
#     else:
#         return max(result)
#
# print(get_result([89, 46, 134, 78, 79, 67, 63, 81]))



# def get_result(sub_array, k):
#     # Write your code here...
#     if len(set(sub_array)) == 1:
#         if k % sub_array.count(sub_array[0]) == 0:
#             return True
#     elif len(set(sub_array)) == 2:
#         for i in range(1, k):
#             for j in range(1, k):
#                 if sub_array.count(list(set(sub_array))[0])*i + sub_array.count(list(set(sub_array))[1])*j == k:
#                     return True
#     else:
#         for i in range(1, k):
#             for j in range(1, k):
#                 for r in range(1, k):
#                     if sub_array.count(list(set(sub_array))[0]) * i + sub_array.count(list(set(sub_array))[1]) * j + \
#                     sub_array.count(list(set(sub_array))[2]) * r == k:
#                         return True
#     return False
#
#
# print(get_result(["x", "x", "x", "y", "y"], 12))



# def get_result(rocket_pos, rocket_speed):
#     # Write your code here...
#     j = 0
#     delete_nahui = []
#     result = []
#     while j < 3000:
#         for i in range(len(rocket_pos)):
#             new_data = rocket_pos[i] + rocket_speed[i]
#             if new_data in result:
#                 rocket_speed[result.index(new_data)] += rocket_speed[i]
#                 delete_nahui.append(i)
#             else:
#                 result.append(new_data)
#         c = 0
#         for i in delete_nahui:
#             rocket_speed.pop(i - c)
#             c += 1
#         delete_nahui = []
#         rocket_pos = result.copy()
#         result.clear()
#         j += 1
#     return len(rocket_pos)
#
# print(get_result([9, 3, 11], [2, 5, 1]))



# scheme = ["1-0-0-0-0-0-0-0",
#           "1-0-0-0-0-0-0-0",
#           "1-0-0-0-0-0-0-0",
#           "1-0-0-0-0-0-0-0",
#           "1-0-0-0-0-0-0-0",
#           "1-0-0-0-0-0-0-0",
#           "1-0-0-0-0-0-0-0"]
# price_pipes = {
#         17 : [[-1, 0], [0, -1]],
#         32 : [[-1, 0], [0, -1], [0, 1]],
#         10 : [[-1, 0], [0, 1]],
#         31 : [[-1, 0], [0, 1], [1, 0]],
#         63 : [[-1, 0], [0, -1], [0, 1], [1, 0]],
#         40 : [[-1, 0], [0, -1], [1, 0]],
#         15 : [[0, -1], [1, 0]],
#         29 : [[0, -1], [0, 1], [1, 0]],
#         13 : [[0, 1], [1, 0]],
#         20 : [[-1, 0], [1, 0]],
#         21 : [[0, -1], [0, 1]]
#     }
# new_scheme = []
# result = {}
# result_value = []
# where_pipes = []
# going = [[1,0], [0,-1],[-1,0],[0,1]]
# return_result = 0
# start_finish = 0
# for i in scheme:
#     new_scheme.append(i.split('-'))
# for i in range(len(new_scheme)):
#     for j in range(len(new_scheme[i])):
#         if new_scheme[i][j] == '1':
#             where_pipes.append([i, j])
# for i in where_pipes:
#     if start_finish == 0 or start_finish == len(where_pipes)-1:
#         if i[1] == 0:
#             result_value.append([0, 1])
#         if i[0] == 0:
#             result_value.append([1, 0])
#         if i[1] == len(scheme[0]) - 1:
#             result_value.append([0, -1])
#         if i[0] == len(scheme) - 1:
#             result_value.append([-1, 0])
#     for j in where_pipes:
#         if [i[0]-j[0], i[1]-j[1]] in going:
#             result_value.append([i[0]-j[0], i[1]-j[1]])
#     result[where_pipes.index(i)] = sorted(result_value.copy())
#     result_value.clear()
#     start_finish += 1
# for i in result:
#     for k, j in price_pipes.items():
#         if j == result[i]:
#             return_result += k
#
# print(where_pipes)
# print(return_result)



# def get_result(s, k, string_goal):
#     # Write your code here...
#     if string_goal in s and s.index(string_goal) <= k:
#         return len(string_goal)
#     j = 0
#     for i in s:
#         if i == string_goal[j]:
#             j += 1
#         else:
#             k -= 1
#         if k < 0:
#             break
#     return j
#





# cash=[51, 48, 62]
# s=11
# new_cash = 0
# while s > 2:
#     new_cash = min(cash) + 3
#     cash.remove(min(cash))
#     cash.append(new_cash)
#     new_cash = 0
#     s -= 3
# new_cash = min(cash) + s
# cash.remove(min(cash))
# cash.append(new_cash)
# result = 0
# for i in cash:
#     if i < max(cash):
#         result += 1


# arr = [3, 2, 4, 5]
# w = 6
# k = 0
# while sum(arr) >= w:
#     res = max(arr)//2
#     arr.remove(max(arr))
#     arr.append(res)
#     k += 1
#     if k >= max(arr) and sum(arr) >= w:
#         print(False)
#         break



# nums = [1, 2, 3, 4, 5]
# new_nums = sorted(nums)
# print(new_nums)
# medin = new_nums[len(nums)//2]
# print(medin)
# print(new_nums[:new_nums.index(medin)])



# def get_result(calendar, date_of_birth, name, phrases):
#     j = 0
#     if calendar - date_of_birth != eval(phrases[0]):
#         return False
#     if len(name) - len(phrases[1]) == 0:
#         for i in range(len(name)):
#             if name[i] != phrases[0][i]:
#                 j += 1
#     if j > 1:
#         return False
#     if (len(name) - len(phrases[1]))*(len(name) - len(phrases[1])) > 1:
#         return False
#     return True



# nums = [1, 5, 7, 3]
# targets = [10, 13]
# result = 0
# k = 'a'
# for i in targets:
#     for j in nums:
#         a = i - j
#         if a in nums and k != j:
#             nums.append(i)
#             k = a
#             result += 1
# print(result)



# passersby = [3, 10, 4, 8, 5]
# new_pass = sorted(passersby)
# if len(passersby) % 2 == 0:
#     a = new_pass[:int(len(passersby)/2)]
#     b = new_pass[int(len(passersby)/2):]
# else:
#     a = new_pass[:int(len(passersby) // 2)]
#     b = new_pass[int(len(passersby) // 2) + 1:]
#
# result = sum(b) - sum(a)
# return result


# chests = [1, 4, 2, 10, 15, 60]
# t = 1
#
# def get_result(chests, t):
#     # Write your code here...
#     j = 0
#     k = -1
#     d = 0
#     result = []
#     end_res = []
#     if t % 2 == 0:
#         for i in range(1, 2 + int(t/2)):
#             k += 1
#             result.append(chests[j:int(t/2)+k])
#             j = 1 + 2 * (i - 1)
#     else:
#         for i in range(1, 2 + int(t // 2)):
#             d += 1
#             result.append(chests[j:int(t // 2) + d])
#             j = 2 + 2 * (i - 1)
#     for i in result:
#         end_res.append(sum(i))
#     return max(end_res)
#
# print(get_result([1, 4, 2, 10, 15, 60], t = 7))



# chests = [1, 4, 2, 10, 15, 60, 7]
# t = 8
# new_chets = sorted(chests, reverse=True)
# new_index = []
# for i in new_chets:
#     new_index.append(chests.index(i))
#
# result = []
# d = 0
#
# for i in range(len(new_index)):
#     if t > new_index[i] + 1:
#         result.append(chests[new_index[i]])
#         d += new_index[i]
#         while d < t:
#             for j in new_index[new_index[i]:]:
#                 if j < i:
#                     if d+1 < t:
#                         result[i] += chests[new_index[j]]
#                         d += 1
#                 else:
#                     if j + 1 < t:
#                         result[i] += chests[new_index[j]]
#                         d += j + 1 - d
#
#
# print(result)






# deal = ["a-bt","b-c","c-ad","d", "t-xc"]
# start = deal[0][0]
# result = [start]
# d = 0
#
#
# def pzdc(deal):
#     global d
#     global start
#     for i in deal:
#         if start == i[0]:
#             if len(i) >= 3:
#                 for j in i[2:]:
#                     result[d] += j
#                     start = j
#                     if result[d][0] == j:
#                         result.append(result[d])
#                         d += 1
#
#                     else:
#                         pzdc(deal)
#             else:
#                 result[d] += i
#                 if result[d][0] == i:
#                     d += 1
#                     result.append('')
#
#                 else:
#                     pzdc(deal)
#     return result
#
# print(pzdc(["a-b","b-c","c-ad","d"]))



# def get_result(cave):
#     k = 0
#     # Write your code here...
#     finish = cave.index(-1)
#     while finish in cave:
#         if cave.count(finish) > 1:
#             for i in cave:
#                 if i == finish and cave.index(i, k) in cave:
#                     finish = cave.index(cave.index(i,k))
#                 elif i == finish and cave.index(i) not in cave:
#                     k += 1
#         elif cave.count(finish) == 1:
#             finish = cave.index(finish)
#         else:
#             return finish
#
#     return finish
#
# print(get_result([1, -1, 1, 2]))



# def get_result(nums, k):
#     # Write your code here...
#     new_nums = sorted(nums)
#     result = 0
#     for i in new_nums:
#         if i <= k:
#             k += 1
#             result += 1
#         else:
#             return result
#     return result



# def get_result(fences):
#     # Write your code here...
#     new_fences = sorted(fences)
#     lenth = len(fences) - 1
#     if lenth in fences:
#         return True
#     for i in new_fences[:lenth+1]:
#         k = []
#         k.append(i)
#         for j in new_fences[1:]:
#             k.append(j)
#             if sum(k) == lenth:
#                 if len(k) == lenth:
#                     break
#                 for c in k:
#                     if c < 0 and len(k[1:]) <= 2:
#                         break
#                     elif c > lenth:
#                         break
#                     else:
#                         return True
#             elif sum(k) > lenth:
#                 break
#     return False
#
# print(get_result([0, 2, 4, 1, 6, 2]))
#




# def get_result(names, statements):
#     dict = {
#     'is not youngest': 3,
#     'is oldest': 4,
#     'is not oldest': 2,
#     'is youngest': 1
#     }
#     new_names = []
#     rating = []
#     result = []
#     k = 0
#     for i in statements:
#         rating.append(dict[i.split('-')[1]])
#         new_names.append([rating[k], i.split('-')[0]])
#         try:
#             names.remove(i.split('-')[0])
#         except:
#             pass
#         k += 1
#
#     if len(names) == 0:
#         for i in sorted(new_names):
#             if i[1] not in result:
#                 result.append(i[1])
#
#     else:
#         if 1 in rating and 4 in rating:
#             result.append(new_names[rating.index(1)][1])
#             result.append(new_names[rating.index(4)][1])
#             result.insert(1, names[0])
#         elif 4 in rating and 1 not in rating:
#             result.append(new_names[rating.index(3)][1])
#             result.append(new_names[rating.index(4)][1])
#             result.insert(0, names[0])
#         elif 1 in rating and 4 not in rating:
#             result.append(new_names[rating.index(1)][1])
#             result.append(new_names[rating.index(2)][1])
#             result.append(names[0])
#         else:
#             return ["Mark", "Jack", "Kevin"]
#     return result




# def get_result(actions):
#     # Write your code here...
#     result = 0
#     result_x = 0
#     key_count = actions.count("keystrokes")
#     if key_count > 0:
#         while key_count > 0:
#             for i in actions[actions.index("keystrokes"):]:
#                 if i == 'click':
#                     result += 1
#                 elif i == 'power':
#                     result_x += result // 2
#                     result = 0
#                     key_count -= 1
#                     actions.remove("keystrokes")
#                     break
#     else:
#         return 0
#
#     return result_x



# def get_result(cash, k):
#     # Write your code here...
#     result = []
#     sort_cash = sorted(cash)
#     s = 1
#     b = k
#     for i in cash:
#         if i >= max(sort_cash):
#             result.append(s)
#             s += 1
#         else:
#             while k > 0:
#                 sort_cash[-1] -= 1
#                 sorted(sort_cash)
#                 k -= 1
#             if i + b > max(sort_cash):
#                 result.append(s)
#             s += 1
#         sort_cash = sorted(cash)
#         k = b
#     return result




# def get_result(numb):
#     # Write your code here...
#     k = 0
#     result = 0
#     if len(numb) % 2 > 0:
#         for i in numb:
#             if numb.count(i) % 2 > 0:
#                 k +=1
#         if k > 1:
#             return False
#         else:
#             return True
#     else:
#         for i in numb:
#             if numb.count(i) % 2 != 0:
#                 k += 1
#         if k > 0:
#             return False
#         else:
#             return True


#
# Implement function get_result
#
# def get_result(fighters_stamina):
#     # Write your code here...
#     result = []
#     result_x = [0, 0, 0, 0]
#     if fighters_stamina.count(fighters_stamina[0]) == 4:
#         return [25, 25, 25, 25]
#
#     result.append([abs(fighters_stamina[0] - fighters_stamina[1]), abs(fighters_stamina[2] - fighters_stamina[3])])
#     result.append([abs(fighters_stamina[0] - fighters_stamina[2]), abs(fighters_stamina[1] - fighters_stamina[3])])
#     result.append([abs(fighters_stamina[0] - fighters_stamina[3]), abs(fighters_stamina[2] - fighters_stamina[1])])
#     for i in result:
#         if i[0] > i[1]:
#             if fighters_stamina[0] > fighters_stamina[1 + result.index(i)]:
#                 result_x[0] += 33
#             else:
#                 result_x[1 + result.index(i)] += 33
#         elif i[0] == i[1] and i[0] != 0:
#             if fighters_stamina[0] > fighters_stamina[1 + result.index(i)]:
#                 result_x[0] += 17
#             else:
#                 result_x[1 + result.index(i)] += 17
#             if result.index(i) < 2:
#                 if fighters_stamina[3] > fighters_stamina[2 - result.index(i)]:
#                     result_x[3] += 17
#                 else:
#                     result_x[2 - result.index(i)] += 17
#             else:
#                 if fighters_stamina[1] > fighters_stamina[2]:
#                     result_x[1] += 17
#                 else:
#                     result_x[2] += 17
#         elif i[0] == i[1] and i[0] == 0:
#             result_x[0] += 8
#             result_x[1] += 8
#             result_x[2] += 8
#             result_x[3] += 8
#         else:
#             if result.index(i) < 2:
#                 if fighters_stamina[3] > fighters_stamina[2 - result.index(i)]:
#                     result_x[3] += 33
#                 else:
#                     result_x[2 - result.index(i)] += 33
#             else:
#                 if fighters_stamina[1] > fighters_stamina[2]:
#                     result_x[1] += 33
#                 else:
#                     result_x[2] += 33
#     return result_x

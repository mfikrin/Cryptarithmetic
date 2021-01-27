if pil_sol == 1:
    cut_string = permute[0:len(unique)]
    # print("----------------")
    # print(answer)
    for solusi in answer:
        if solusi != cut_string:
            answer.remove("dummy")
            answer.append(cut_string)
            for i in range(len(arrStr)):
                if i == len(arrStr) - 2:
                    print(get_val(arrStr, i), end=" +\n")
                elif i == len(arrStr) - 1:
                    print("------")
                    print(get_val(arrStr, i))
                else:
                    print(get_val(arrStr, i))
else:
    for i in range(len(arrStr)):
        if i == len(arrStr) - 2:
            print(get_val(arrStr, i), end=" +\n")
        elif i == len(arrStr) - 1:
            print("------")
            print(get_val(arrStr, i))
        else:
            print(get_val(arrStr, i))
    break
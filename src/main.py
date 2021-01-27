import time
import math

print("-----------------------------")
print("|         Opsi input        |")
print("|   1. Menggunakan file     |")
print("|   2. Input manual         |")
print("-----------------------------")

pil = int(input("Masukkan pilihan : "))

if (pil == 1):
    filename = input("Masukkan nama file (eg : tc1) (Tanpa ekstensi file) : ")
    test = open("../test/" + filename + ".txt", 'r')
    temp = test.readlines()
    del temp[len(temp) - 2:len(temp) - 1]
    temps = []
    for char in temp:
        temps.append(char.replace("\n", ""))
    arrStr = [char.replace('+', '') for char in temps]
else:
    N_Op = int(input("Masukkan banyaknya operand : "))
    arrStr = ["*" for i in range(N_Op + 1)]
    for i in range(N_Op):
        arrStr[i] = input("Operand ke-" + str(i + 1) + " : ")
    arrStr[N_Op] = input("Hasil Operasi : ")
    filename = input("Masukkan nama file output (Tanpa ekstensi file) : ")

temp = ""
for i in range(len(arrStr)):
    temp += arrStr[i]

unique = list(dict.fromkeys(temp))

dict = {}
for char in unique:
    dict[char] = 0

print("-----------------------------")
print("|        Opsi Solusi        |")
print("|   1. Semua Solusi         |")
print("|   2. Satu Solusi          |")
print("-----------------------------")

pil_sol = int(input("Masukkan pilihan : "))

def get_val(arrStr,i):
    sum = 0
    multiple = 1

    for k in range((len(arrStr[i]))-1,-1,-1):
        sum += dict[arrStr[i][k]]*multiple
        multiple *= 10

    return sum

string = "9567108234"
len_string = len(string)
strings = list(string)
def toString(List):
    return ''.join(List)
arr = []
def permutation(kata, l, r):

    if l == r:
        temp = toString(kata)
        arr.append(toString(temp))
    else:
        for i in range(l, r + 1):
            kata[l], kata[i] = kata[i], kata[l]
            permutation(kata, l + 1, r)
            kata[l], kata[i] = kata[i], kata[l]
permutation(strings, 0 , len_string-1)

def is_proper(arrStr):
    N = len(arrStr)
    sum = 0
    for i in range(N-1):
        sum += get_val(arrStr,i)

    result = get_val(arrStr,N-1)

    if (sum == result):
        for string in range(len(arrStr)):
            if dict[arrStr[string][0]] == 0:
                return False
        return True
    else:
        return False

answer = ["dummy"]

if pil_sol == 1:
    name_output = filename + "_out_V_AllSol.txt"
    outfile = open("../test/" + name_output, 'w')
    print("-----------------------------")
    print("|                           |")
    print("|       START TIME !!!      |")
    print("|                           |")
    print("-----------------------------")
    t_initial = time.time()
    percobaan = 0
    banyak_sol = 0
    for permute in arr:
        idx = 0
        for char in unique:
            dict[char] = int(permute[idx])
            idx += 1
        if is_proper(arrStr):
            cut_string = permute[0:len(unique)]
            for solusi in answer:
                if solusi == cut_string:
                    break
                elif solusi != cut_string:
                    banyak_sol += 1
                    if "dummy" in answer:
                        answer.remove("dummy")
                    answer.append(cut_string)

                    print("Question\n")
                    outfile.write("Question\n")
                    outfile.write("\n")
                    for i in range(len(arrStr)):
                        if i == len(arrStr) - 2:
                            print(arrStr[i], end=" +\n")
                            outfile.write(str(arrStr[i]))
                            outfile.write(" +\n")
                        elif i == len(arrStr) - 1:
                            print("------")
                            outfile.write("------\n")
                            print(arrStr[i])
                            outfile.write(str(arrStr[i]))
                            outfile.write("\n")
                            print()
                            outfile.write("\n")
                        else:
                            print(arrStr[i])
                            outfile.write(str(arrStr[i]))
                            outfile.write("\n")

                    print("Answer\n")
                    outfile.write("Answer\n")
                    outfile.write("\n")

                    for i in range(len(arrStr)):
                        if i == len(arrStr) - 2:
                            print(get_val(arrStr, i), end=" +\n")
                            outfile.write(str(get_val(arrStr, i)))
                            outfile.write(" +\n")
                        elif i == len(arrStr) - 1:
                            print("------")
                            outfile.write("------\n")
                            print(get_val(arrStr, i))
                            outfile.write(str(get_val(arrStr, i)))
                            outfile.write("\n")
                            print("Waktu yang dibutuhkan :", time.time()- t_initial, "detik")
                            outfile.write("Waktu yang dibutuhkan : ")
                            outfile.write(str(time.time() - t_initial))
                            outfile.write(" detik")
                            outfile.write("\n")
                            print("Jumlah percobaan :", percobaan)
                            outfile.write("Jumlah percobaan : ")
                            outfile.write(str(percobaan))
                            outfile.write("\n")
                            print("Banyaknya solusi sejauh ini :", banyak_sol)
                            outfile.write("Banyaknya solusi sejauh ini : ")
                            outfile.write(str(banyak_sol))
                            outfile.write("\n")
                            print()
                            outfile.write("\n")
                        else:
                            print(get_val(arrStr, i))
                            outfile.write(str(get_val(arrStr, i)))
                            outfile.write("\n")
                    break
        else:
            percobaan += 1
    if percobaan == math.factorial(len_string):
        print("Question\n")
        outfile.write("Question\n")
        outfile.write("\n")
        for i in range(len(arrStr)):
            if i == len(arrStr) - 2:
                print(arrStr[i], end=" +\n")
                outfile.write(str(arrStr[i]))
                outfile.write(" +\n")
            elif i == len(arrStr) - 1:
                print("------")
                outfile.write("------\n")
                print(arrStr[i])
                outfile.write(str(arrStr[i]))
                outfile.write("\n")
                outfile.write("\n")
            else:
                print(arrStr[i])
                outfile.write(str(arrStr[i]))
                outfile.write("\n")

        print("\nTidak ada kemungkinan angka yang memenuhi :')")
        outfile.write("Tidak ada kemungkinan angka yang memenuhi :')")
        outfile.write("\n")
        print("Waktu yang dibutuhkan :", time.time() - t_initial, "detik")
        outfile.write("Waktu yang dibutuhkan : ")
        outfile.write(str(time.time() - t_initial))
        outfile.write(" detik")
        outfile.write("\n")
        print("Jumlah percobaan :", percobaan)
        outfile.write("Jumlah percobaan : ")
        outfile.write(str(percobaan))
        outfile.write("\n")
        print("Banyaknya solusi sejauh ini :", banyak_sol)
        outfile.write("Banyaknya solusi sejauh ini : ")
        outfile.write(str(banyak_sol))
        outfile.write("\n")
        print()
        outfile.write("\n")
    outfile.close()
elif pil_sol == 2:
    name_output = filename + "_out_V_OneSol.txt"
    outfile = open("../test/"+name_output, 'w')
    print("-----------------------------")
    print("|                           |")
    print("|       START TIME !!!      |")
    print("|                           |")
    print("-----------------------------")
    t_initial = time.time()
    percobaan = 0
    for permute in arr:
        idx = 0
        for char in unique:
            dict[char] = int(permute[idx])
            idx += 1
        if is_proper(arrStr):
            print("Question\n")
            outfile.write("Question\n")
            outfile.write("\n")

            for i in range(len(arrStr)):
                if i == len(arrStr) - 2:
                    print(arrStr[i], end=" +\n")
                    outfile.write(str(arrStr[i]))
                    outfile.write(" +\n")
                elif i == len(arrStr) - 1:
                    print("------")
                    outfile.write("------\n")
                    print(arrStr[i])
                    outfile.write(str(arrStr[i]))
                    outfile.write("\n")
                    print()
                    outfile.write("\n")
                else:
                    print(arrStr[i])
                    outfile.write(str(arrStr[i]))
                    outfile.write("\n")

            print("Answer\n")
            outfile.write("Answer\n")
            outfile.write("\n")

            for i in range(len(arrStr)):
                if i == len(arrStr) - 2:
                    print(get_val(arrStr, i), end=" +\n")
                    outfile.write(str(get_val(arrStr, i)))
                    outfile.write(" +\n")
                elif i == len(arrStr) - 1:
                    print("------")
                    outfile.write("------\n")
                    print(get_val(arrStr, i))
                    outfile.write(str(get_val(arrStr, i)))
                    outfile.write("\n")
                    print("Waktu yang dibutuhkan : ", time.time() - t_initial, "detik")
                    outfile.write("Waktu yang dibutuhkan : ")
                    outfile.write(str(time.time() - t_initial))
                    outfile.write(" detik")
                    outfile.write("\n")
                    print("Jumlah percobaan : ", percobaan)
                    outfile.write("Jumlah percobaan : ")
                    outfile.write(str(percobaan))
                    outfile.write("\n")
                    print()
                    outfile.write("\n")
                else:
                    print(get_val(arrStr, i))
                    outfile.write(str(get_val(arrStr, i)))
                    outfile.write("\n")
            break
        else:
            percobaan += 1
    if percobaan == math.factorial(len_string):
        print("Question\n")
        outfile.write("Question\n")
        outfile.write("\n")
        for i in range(len(arrStr)):
            if i == len(arrStr) - 2:
                print(arrStr[i], end=" +\n")
                outfile.write(str(arrStr[i]))
                outfile.write(" +\n")
            elif i == len(arrStr) - 1:
                print("------")
                outfile.write("------\n")
                print(arrStr[i])
                outfile.write(str(arrStr[i]))
                outfile.write("\n")
                outfile.write("\n")
            else:
                print(arrStr[i])
                outfile.write(str(arrStr[i]))
                outfile.write("\n")

        print("\nTidak ada kemungkinan angka yang memenuhi :')")
        outfile.write("Tidak ada kemungkinan angka yang memenuhi :')")
        outfile.write("\n")
        print("Waktu yang dibutuhkan :", time.time() - t_initial, "detik")
        outfile.write("Waktu yang dibutuhkan : ")
        outfile.write(str(time.time() - t_initial))
        outfile.write(" detik")
        outfile.write("\n")
        print("Jumlah percobaan :", percobaan)
        outfile.write("Jumlah percobaan : ")
        outfile.write(str(percobaan))
        outfile.write("\n")
        print()
        outfile.write("\n")

    outfile.close()























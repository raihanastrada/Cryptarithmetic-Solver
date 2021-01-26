def get_files(filename):
    # Mengembalikan list berisi kata-kata yang berada dalam file
    list_of_words = []
    cur_path = os.path.dirname(__file__)
    fpath = os.path.join(cur_path, '..\\test\\'+filename)
    try:
        f = open(fpath, "r")
        EOF = False
        while (not EOF):
            word = ""
            char = f.read(1)
            # Skip Blank or Line
            while (char == " ") or (char == "-"):
                char = f.read(1)
            # { EOP = (char != " ") or (char != "-") }
            # Copy Word
            while (char) and (char != "\n"):
                word += char
                char = f.read(1)
                if (char == "+"):
                    char = f.read(1)
            # { EOP = (not char) or (char = "\n") }
            if (word != ""):
                list_of_words.append(word)
            if not char:
                EOF = True                
        # { EOP = EOF }
        f.close()

    except:
        print("Tidak ditemukan file dengan nama tersebut\n")
    
    return list_of_words

def isFirst(words, char):
    # Mengembalikan True jika char merupakan huruf pertama suatu kata
    first = False
    i = 0
    while not(first) and (i < len(words)):
        if (char == words[i][0]):
            first = True
        else:
            i += 1
    # { EOP : first or i >= len(words) }
    return first

def isAllAssigned(chars_value):
    # Mengembalikan True jika seluruh char sudah diassign suatu angka
    allAssigned = True
    i = 0
    while (allAssigned) and (i < len(chars_value)):
        if (chars_value[i][1] == -1):
            allAssigned = False
        else :
            i += 1
    # { EOP : allAssigned or i >= len(chars_value) }
    return allAssigned

def getValue(char, chars_value):
    # Mengembalikan angka yang telah diassign ke char
    i = 0
    while (i < len(chars_value)):
        if (char == chars_value[i][0]):
            return (chars_value[i][1])
        else:
            i += 1
    
def isSolved(words, chars_value):
    # Mengembalikan True jika nilai chars_value menyelesaikan Cryptarithmetic
    numbers = []
    for i in range(len(words)):
        number = ""
        for char in words[i]:
            number += str(getValue(char, chars_value))                    
        numbers.append(int(number))

    operands = len(words)-1
    sum = 0
    for i in range(operands):
        sum += numbers[i]
    return (sum == numbers[-1])

def longestWord(words):
    # Mengembalikan panjang kata yang terbesar
    longest = 0
    for i in range(len(words)):
        if (len(words[i]) > longest):
            longest = len(words[i])
    return longest

def printSolution(words, chars_value):
    # Mencetak solusi sesuai format
    n = longestWord(words)
    for i in range(len(words)+1):
        # Print Soal
        if (i == len(words)-2):
            print(" + ",end = "")
        else:
            print("   ",end = "")

        if (i == len(words)-1):
            for k in range(n):
               print("—",end = "")

        else:
            if (i == len(words)):
                # Cetak spasi
                for j in range(n-len(words[i-1])):
                    print(" ", end = "")
                # Cetak huruf
                for j in range(len(words[i-1])):
                    print(words[i-1][j], end = "")
            else:
                # Cetak spasi
                for j in range(n-len(words[i])):
                    print(" ", end = "")
                # Cetak huruf
                for j in range(len(words[i])):
                    print(words[i][j], end = "")

        # Print Jarak
        print("          ", end = "")

        # Print Jawaban
        if (i == len(words)-2):
            print(" + ",end = "")
        else:
            print("   ",end = "")

        if (i == len(words)-1):
            for k in range(n):
               print("—",end = "")
               if (k == n-1):
                   print("")

        else:
            if (i == len(words)):
                # Cetak spasi
                for j in range(n-len(words[i-1])):
                    print(" ", end = "")
                # Cetak angka
                for j in range(len(words[i-1])):
                    print(getValue(words[i-1][j], chars_value), end = "")
                    if (j == len(words[i-1])-1):
                        print("")
            else:
                # Cetak spasi
                for j in range(n-len(words[i])):
                    print(" ", end = "")
                # Cetak angka
                for j in range(len(words[i])):
                    print(getValue(words[i][j], chars_value), end = "")
                    if (j == len(words[i])-1):
                        print("")
    print("")

def solve(words, chars_value, i, used_num):
    if not(isAllAssigned(chars_value)): # Jika terdapat char yang belom ter-assign
        for j in range(10):
            if (j not in used_num): # Cek apakah bilangan j sudah digunakan
                if (isFirst(words,chars_value[i][0])) and (j!=0): # Jika char merupakan huruf pertama dari kata, maka tidak boleh 0
                    chars_value[i][1] = j
                    used_num.append(j)
                    solve(words, chars_value, i+1, used_num) # Rekurens untuk mengassign char berikutnya
                    used_num.remove(j)
                    chars_value[i][1] = -1

                elif not(isFirst(words,chars_value[i][0])): # Jika char bukan merupakan huruf pertama, bebas selama j belom digunakan
                    chars_value[i][1] = j
                    used_num.append(j)
                    solve(words, chars_value, i+1, used_num) # Rekurens untuk mengassign char berikutnya
                    used_num.remove(j)
                    chars_value[i][1] = -1
            
    else: # allAssigned
        global tries
        tries += 1
        if (isSolved(words, chars_value)): # Cek apakah menyelesaikan cryptarithm
            # Print Solusi
            printSolution(words, chars_value) 
            # Print jumlah tes yang dilakukan
            print("Total tes: ", end = "")
            print(tries)
            # Print waktu eksekusi
            print("Estimated time: ", end = "")
            end_time = time.time()
            global start_time
            print(str(end_time-start_time) + "s")
            print("————————————————————————————————————————")

def menu():
    print("╔════════════════════╗")
    print("║        MENU        ║")
    print("║════════════════════║")
    print("║ 1. RUN PROGRAM     ║")
    print("║ 0. EXIT            ║")
    print("╚════════════════════╝")
    print("")

# Modul yang digunakan
import time
import os

running = True
while (running):
    menu()
    print("Masukkan pilihan: ", end = "")
    choice = int(input())
    if (choice == 1):
        filename = str(input("Masukkan nama file: "))
        start_time = time.time()
        words = get_files(filename)
        if len(words) != 0: # Jika isi file tidak kosong
            # Tiap huruf dalam kata dimasukkan ke dalam list
            chars_value = []
            for i in range(len(words)):
                for char in words[i]:
                    if ([char,-1]) not in chars_value:
                        chars_value.append([char,-1]) # Assign huruf dengan nilai -1

            used_num = [] # Inisialisasi list angka yang terpakai
            i = 0 # Index chars_value
            tries = 0 # Jumlah percobaan
            print("Mencari solusi...")
            print("————————————————————————————————————————")
            solve(words, chars_value, i, used_num)
            print("")
    elif (choice == 0):
        running = False
    else:
        print("Pilihan tidak tersedia")
    # { EOP: running = False }
"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3.
На стержень 1 надета пирамидка из n дисков различного диаметра в порядке возрастания диаметра.
Диски можно перекладывать с одного стержня на другой строго по одному.
При этом, диск нельзя класть сверху на диск меньшего диаметра.
Необходимо переложить всю пирамидку со стержня 1 на стержень 3 за минимальное число перекладываний.
Напишите программу, которая для числа дисков n печатает последовательность перекладываний, необходимую для решения.
"""


def tower_of_hanoi(n: int, start, end):
    if n == 1:
        print(f"Move disk 1 from rod {start} to rod {end}")
    else:
        buf = 6 - start - end
        tower_of_hanoi(n - 1, start, buf)
        print(f"Move disk {n} from rod {start} to rod {end}")
        tower_of_hanoi(n - 1, buf, end)


tower_of_hanoi(4, 1, 3)

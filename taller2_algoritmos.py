# Implementaciones: bubble, merge, quick
import random
import time
import tracemalloc
import statistics
import csv
import os
import sys
sys.setrecursionlimit(1000000)

def bubble_sort(arr):
    a = arr[:]  # copia para no modificar original
    n = len(a)
    swapped = True
    for i in range(n-1):
        if not swapped:
            break
        swapped = False
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # merge
    res = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i+=1
        else:
            res.append(right[j]); j+=1
    res.extend(left[i:]); res.extend(right[j:])
    return res

def quick_sort(arr):
    a = arr[:]
    def _qs(lo, hi):
        if lo >= hi: return
        pivot = a[(lo+hi)//2]
        i, j = lo, hi
        while i <= j:
            while a[i] < pivot: i+=1
            while a[j] > pivot: j-=1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i+=1; j-=1
        _qs(lo, j)
        _qs(i, hi)
    _qs(0, len(a)-1)
    return a

# Medición de tiempo y memoria
def measure_time_and_mem(func, arr, repeats=5):
    times = []
    mem_peaks = []
    for _ in range(repeats):
        arr_copy = arr[:]  # copia para cada repetición
        tracemalloc.start()
        t0 = time.perf_counter()
        func(arr_copy)
        t1 = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(t1-t0)
        mem_peaks.append(peak)
    return statistics.mean(times), statistics.stdev(times), statistics.mean(mem_peaks)

# Main
if __name__ == "__main__":
    tamanos = [1000, 2000, 5000, 10000, 20000]
    resultados = []

    # archivo CSV
    nombre_archivo = "resultados_taller2.csv"
    ruta = os.path.join(os.getcwd(), nombre_archivo)

    with open(ruta, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algoritmo", "Tamaño_n", "Tiempo_promedio_s", "Desv_std_s", "Memoria_KB"])

        for n in tamanos:
            arr = [random.randint(0, n) for _ in range(n)]
            print(f"\nTamaño n={n}")
            for nombre, func in [("Bubble", bubble_sort), ("Merge", merge_sort), ("Quick", quick_sort)]:
                t_prom, t_std, mem_prom = measure_time_and_mem(func, arr, repeats=3)
                writer.writerow([nombre, n, t_prom, t_std, round(mem_prom / 1024, 2)])
                print(f"{nombre:8s} → tiempo {t_prom:.5f}s ±{t_std:.5f}s, memoria {mem_prom/1024:.1f} KB")

    print(f"\nResultados guardados en: {ruta}")
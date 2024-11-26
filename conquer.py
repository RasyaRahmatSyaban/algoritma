import random

# Memilih angaka acak dari 1-100 sebanyak 50
angka_acak = random.choices(range(1, 100), k=50)
print("Angka Asli:", angka_acak)

# Divide and Conquer Sorting (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    pivot = len(arr) // 2
    bagian_kiri = merge_sort(arr[:pivot])  
    bagian_kanan = merge_sort(arr[pivot:]) 
    
    # Conquer (Merge)
    return merge(bagian_kiri, bagian_kanan)

def merge(kiri, kanan):
    sorted_list = []
    i = j = 0
    
    while i < len(kiri) and j < len(kanan):
        if kiri[i] < kanan[j]:
            sorted_list.append(kiri[i])
            i += 1
        else:
            sorted_list.append(kanan[j])
            j += 1
    
    sorted_list.extend(kiri[i:])
    sorted_list.extend(kanan[j:])
    
    return sorted_list

hasil = merge_sort(angka_acak)
print("\nHasil Sorting (Divide and Conquer):", hasil)

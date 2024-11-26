import random

# Memilih angaka acak dari 1-100 sebanyak 50
angka_acak = random.choices(range(1, 100), k=50) 
print("Angka Asli:", angka_acak)

# Naive-Bayes Sorting
def naive_bayes_sort(arr):
    
    probabilities = [1 / (val + 1) for val in arr]
    
    paired = list(zip(arr, probabilities))
    sorted_paired = sorted(paired, key=lambda x: x[1], reverse=True)
    return [val[0] for val in sorted_paired]  

sorted_data_naive = naive_bayes_sort(angka_acak)
print("\nHasil Sorting (Naive-Bayes):", sorted_data_naive)

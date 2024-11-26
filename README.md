# algoritma
RASYA RAHMAT SYABAN F55123041 TEKNIK INFORMATIKA-B



ANALISIS KUIZ 2

-Naive Bayes
    Metode Naive-Bayes Sort bekerja dengan cara memberikan probabilitas kepada setiap angka. Semakin besar angka, semakin kecil probabilitasnya. Setelah itu, kita menyortir angka berdasarkan probabilitas tersebut. Secara teori, waktu yang dibutuhkan untuk melakukan sorting ini adalah O(n log n), sama seperti algoritma sorting biasa. Best case terjadi jika data sudah terurut. Meskipun data sudah terurut, algoritma ini tetap harus menghitung probabilitas dan mengurutkan ulang data, jadi kompleksitas waktunya tetap O(n log n).
-Divide and Conquer
    Merge Sort adalah contoh algoritma yang menggunakan prinsip Divide and Conquer. Prinsip ini bekerja dengan cara membagi masalah besar (data yang perlu diurutkan) menjadi masalah kecil (bagian data yang lebih kecil). Setiap bagian diurutkan secara terpisah, lalu hasilnya digabungkan kembali secara urut. Merge Sort menggunakan cara ini untuk mengurutkan data. Keuntungan utama dari Merge Sort adalah bahwa ia tetap bekerja dengan waktu O(n log n), baik untuk data yang sudah terurut atau yang tidak terurut. Ini membuatnya stabil dan efisien dalam berbagai situasi.
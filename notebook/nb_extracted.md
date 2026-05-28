<!-- Markdown Cell 0 -->
# Proyek Analisis Data: [E-Commerce Public Dataset]
- **Nama:** [Louie Jason Liman]
- **Email:** [krenzlouie39@gmail.com]
- **ID Dicoding:** [Louie Jason]


<!-- Markdown Cell 1 -->
## Menentukan Pertanyaan Bisnis


<!-- Markdown Cell 2 -->
**SMART Question** adalah sebuah framework untuk merumuskan pertanyaan secara terstruktur agar memeperoleh informasi yang mendalam.

* **Spesific (Spesifik)**
  * Pertanyaan harus jelas, fokus pada sebuah topik tertentu, dan tidak bermakna ganda. Hindari pertanyaan yang terlalu luas.
    * Salah: Bagaimana cara meningkatkan penjualan?
    * Benar: Faktor apa saja yang memengaruhi penurunan penjualan produk kategori elektronik di wilayah Jakarta selama kuartal terakhir?
* **Measurable (Terukur)**
  * Pertanyaan harus bisa dijawab dengan angka atau matrix yang konkret, harus tahu apa yang akan dihitung.
    * Salah: Apakah pelanggan senang dengan layanan kita?
    * Benar: Berapa skor rata-rata Customer Satisfaction untuk layanan purna jual bulan ini dibandingkan bulan lalu?
* **Action-Oriented (Berorientasi Aksi)**
  * Hasil dari pertanyaan harus bisa memberikan arahan untuk melakukan tindakan nyata. Jika pertanyaan terjawab, stakeholder harus tahu apa langkah selanjutnya.
    * Salah: Mengapa orang suka berbelanja?
    * Benar: Fitur apa pada aplikasi yang paling sering digunakan sebelum pengguna memutuskan untuk melakukan checkout?
* **Relevant (Relevan)**
  * Hasil dari pertanyaan harus sejalan dengan tujuan utama bisnis atau masalah yang sedang dihadapi.
    * Salah: Menanyakan tentang stok gudang saat masalah utamanya adalah efektivitas kampanye media sosial.
    * Benar: Apakah kampanye iklan di Instagram memberikan Return on Ad Spend (ROAS) yang lebih tinggi dibandingkan iklan di TikTok?
* **Time-bound (Terikat Waktu)**
  * Pertanyaan harus ada batasan waktu yang jelas agar analisis memiliki konteks yang tepat.
    * Salah: Berapa banyak pengguna baru kita?
    * Benar: Berapa tingkat pertumbuhan pengguna baru secara bulanan (Month-over-Month) sepanjang tahun 2025?


<!-- Markdown Cell 3 -->
**Pertanyaan 1**
- How do monthly order volume and total revenue evolve from 2016 to 2018, and what key trends can be identified to support business decision-making?

Keterangan:

- Specific: Fokus pada analisis "jumlah order" dan "total revenue" secara bulanan dalam dataset e-commerce.
- Measurable: Menggunakan metrik kuantitatif seperti jumlah order unik dan total nilai pembayaran setiap bulan.
- Action-Oriented: Hasil analisis dapat digunakan untuk mengidentifikasi tren peningkatan atau penurunan yang dapat mendukung strategi pemasaran atau penjualan.
- Relevant: Memahami tren penjualan sangat penting untuk pengambilan keputusan bisnis dalam e-commerce.
- Time-bound: Analisis dibatasi pada periode tahun 2016 hingga 2018.

**Pertanyaan 2**

- Which product categories contribute the most to total revenue between 2016 and 2018, and how can this information be used to prioritize product strategy?

Keterangan:

- Specific: Fokus pada kategori produk yang memberikan kontribusi terbesar terhadap total revenue.
-Measurable: Diukur berdasarkan total nilai pembayaran dari masing-masing kategori produk.
- Action-Oriented: Hasil analisis dapat digunakan untuk menentukan prioritas produk, seperti meningkatkan stok atau promosi pada kategori dengan performa tinggi.
- Relevant: Mengetahui kategori unggulan penting untuk meningkatkan efektivitas strategi bisnis dan penjualan.
- Time-bound: Analisis dilakukan pada periode 2016 hingga 2018.

**Pertanyaan 3**

- What payment methods are most frequently used by customers from 2016 to 2018, and how can this insight support optimization of payment services?

Keterangan:

- Specific: Fokus pada metode pembayaran yang digunakan oleh pelanggan dalam transaksi e-commerce.
- Measurable: Diukur berdasarkan jumlah penggunaan masing-masing metode pembayaran.
-Action-Oriented: Insight ini dapat digunakan untuk mengoptimalkan layanan pembayaran, seperti meningkatkan dukungan pada metode yang paling sering digunakan.
- Relevant: Metode pembayaran berpengaruh terhadap kenyamanan pelanggan dan keberhasilan transaksi.
- Time-bound: Analisis dibatasi pada periode 2016 hingga 2018.


<!-- Markdown Cell 4 -->
## Import Semua Packages/Library yang Digunakan


<!-- Markdown Cell 6 -->
## Data Wrangling


<!-- Markdown Cell 7 -->
### Gathering Data


<!-- Markdown Cell 10 -->
### Data Understanding

Tahap ini bertujuan untuk memahami struktur data dan isi dari setiap dataset.


<!-- Markdown Cell 13 -->
### Feature Selection

Pada tahap ini dilakukan pemilihan kolom yang relevan dengan pertanyaan bisnis. Hal ini bertujuan untuk menyederhanakan dataset serta meningkatkan efisiensi dalam proses analisis.

Kolom yang dipilih meliputi informasi terkait waktu transaksi, customer, produk, pembayaran, serta review.


<!-- Markdown Cell 16 -->
### Assessing Data


<!-- Markdown Cell 19 -->
**Insight:**
- Distribusi nilai pembayaran bersifat right-skewed, dengan mayoritas transaksi berada pada nominal rendah.
- Terdapat outlier dengan nilai transaksi sangat tinggi yang berpotensi mempengaruhi analisis statistik.
- Hal ini menunjukkan adanya perbedaan antara transaksi umum dan transaksi bernilai besar.
- Distribusi kategori produk tidak seimbang, dengan beberapa kategori mendominasi jumlah transaksi.
- Ketidakseimbangan data ini berpotensi menimbulkan bias sehingga perlu diperhatikan dalam analisis.


<!-- Markdown Cell 20 -->
### Cleaning Data

Tahap ini bertujuan untuk membersihkan data dari missing values, duplikasi, serta memastikan tipe data sudah sesuai untuk analisis.


<!-- Markdown Cell 29 -->
**Insight:**
- Missing values pada kolom product_category_name diisi dengan nilai "unknown" agar data tetap lengkap dan dapat digunakan dalam analisis.

- Ditemukan adanya data duplikat dalam dataset. Namun, duplikasi ini tidak langsung dihapus karena kemungkinan merupakan data transaksi yang valid, di mana satu order dapat memiliki lebih dari satu produk atau pembayaran.

- tipe data pada kolom waktu diubah menjadi datetime agar dapat digunakan dalam analisis berbasis waktu.

- Outlier berhasil dikurangi sehingga distribusi data lebih stabil


<!-- Markdown Cell 30 -->
## Exploratory Data Analysis (EDA)


<!-- Markdown Cell 31 -->
### Explore Tren Order & Revenue per month


<!-- Markdown Cell 33 -->
**Insight:**
- Jumlah order dan revenue menunjukkan tren meningkat dari tahun 2017 hingga awal 2018.
- Puncak transaksi terjadi pada November 2017, dengan jumlah order dan revenue tertinggi dibanding bulan lainnya.
- Setelah mencapai puncak, terjadi fluktuasi namun nilai transaksi tetap relatif tinggi pada tahun 2018.
- Secara keseluruhan, terdapat pola pertumbuhan yang signifikan dalam aktivitas transaksi dari waktu ke waktu.


<!-- Markdown Cell 34 -->
### Explore Products with biggest revenue


<!-- Markdown Cell 36 -->
**Insight:**
- Kategori cama_mesa_banho memiliki kontribusi revenue tertinggi dibandingkan kategori lainnya.
- Beberapa kategori seperti beleza_saude, moveis_decoracao, dan esporte_lazer juga menunjukkan performa penjualan yang tinggi.
- Terdapat perbedaan revenue yang cukup signifikan antara kategori teratas dan kategori di bawahnya.
- Hal ini menunjukkan bahwa penjualan didominasi oleh beberapa kategori utama.


<!-- Markdown Cell 37 -->
### Explore Payment Methods Distribution



<!-- Markdown Cell 39 -->
**Insight:**
- Metode pembayaran credit_card mendominasi transaksi dengan jumlah yang jauh lebih tinggi dibanding metode lainnya.
- Metode boleto menjadi pilihan kedua, namun selisihnya cukup signifikan dibanding credit card.
- Metode voucher dan debit_card digunakan dalam jumlah yang jauh lebih sedikit.
- Hal ini menunjukkan bahwa pelanggan memiliki preferensi kuat terhadap penggunaan kartu kredit dalam bertransaksi.


<!-- Markdown Cell 40 -->
## Visualization & Explanatory Analysis


<!-- Markdown Cell 41 -->
### Pertanyaan 1:


<!-- Markdown Cell 43 -->
**Insight:**

- Revenue menunjukkan tren meningkat secara signifikan dari awal 2017 hingga akhir 2017.
- Puncak revenue terjadi sekitar November 2017, yang menjadi periode dengan pendapatan tertinggi.
- Setelah mencapai puncak, revenue tetap berada pada level tinggi di awal 2018 meskipun mengalami fluktuasi.
- Pada pertengahan hingga akhir 2018, terlihat adanya penurunan revenue secara bertahap.
Penurunan drastis pada bulan terakhir kemungkinan disebabkan oleh data yang tidak lengkap, sehingga tidak merepresentasikan kondisi sebenarnya.


<!-- Markdown Cell 44 -->
### Pertanyaan 2:


<!-- Markdown Cell 46 -->



<!-- Markdown Cell 47 -->
### Pertanyaan 3


<!-- Markdown Cell 49 -->
**Insight:**
- Analisis tren menunjukkan bahwa jumlah order dan revenue mengalami peningkatan signifikan sepanjang tahun 2017 hingga mencapai puncaknya pada akhir tahun, sebelum mengalami fluktuasi pada tahun 2018.
- Distribusi revenue antar kategori produk tidak merata, di mana beberapa kategori seperti cama_mesa_banho dan beleza_saude mendominasi kontribusi pendapatan.
- Hal ini menunjukkan adanya kategori produk unggulan yang menjadi sumber utama revenue dalam platform.
- Dari sisi metode pembayaran, terlihat bahwa credit card merupakan metode yang paling dominan digunakan oleh pelanggan.
- Perbedaan yang signifikan antar metode pembayaran menunjukkan adanya preferensi kuat pelanggan terhadap metode tertentu dalam bertransaksi.


<!-- Markdown Cell 50 -->
## Analisis Lanjutan (Opsional)


<!-- Markdown Cell 59 -->
**Insight:**
- Sebagian besar pelanggan berada pada kategori Mid Value, diikuti oleh High Value, dan paling sedikit adalah Low Value.
- Pelanggan High Value memiliki rata-rata nilai transaksi (monetary) paling tinggi dibandingkan segmen lainnya.
- Pelanggan Low Value memiliki nilai transaksi paling rendah dan recency yang lebih tinggi, menunjukkan mereka sudah lama tidak bertransaksi.
- Pelanggan Mid Value berada di antara kedua segmen tersebut dan memiliki potensi untuk ditingkatkan menjadi High Value.
- Secara umum, frekuensi transaksi cenderung rendah (sekitar 1), yang menunjukkan sebagian besar pelanggan hanya melakukan pembelian satu kali.


<!-- Markdown Cell 60 -->
## Conclusion


<!-- Markdown Cell 61 -->
## Conclusion

- Conclusion Question 1: Jumlah order bulanan dan revenue menunjukkan tren peningkatan selama periode 2016–2018, dengan puncak terjadi pada akhir tahun 2017 sebelum cenderung stabil pada tahun 2018. Penurunan tajam di akhir periode disebabkan oleh data yang tidak lengkap.

- Conclusion Question 2: Selama periode 2016–2018, beberapa kategori produk memberikan kontribusi yang jauh lebih besar terhadap total revenue dibandingkan kategori lainnya, yang menunjukkan adanya ketimpangan distribusi performa penjualan antar kategori.

- Conclusion Question 3: Selama periode 2016–2018, metode pembayaran credit card merupakan yang paling sering digunakan, diikuti oleh boleto, sementara metode lainnya memiliki kontribusi yang relatif kecil.


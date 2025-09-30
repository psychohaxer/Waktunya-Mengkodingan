# Character definitions
define a = Character('Ayu', color="#40a040")
define d = Character('Dewi', color="#4040a0")
define l = Character('Lestarta', color="#a04040")
define p = Character('Pandu', color="#a0a040")
define s = Character('Siti', color="#a040a0")

# Variables
define confirm_ready = 0

label start:
    scene corridor_f morning with fade

    show ayu relaxed with moveinright:
        xalign 0.25
        yalign 1.0
    pause 0.5

    show ayu waving with dissolve

    a "Halo! Selamat datang di Waktunya Mengkodingan!"

    show ayu relaxed with dissolve

    a "Di sini, kamu akan belajar dasar-dasar pemrograman melalui sebuah cerita interaktif."
    a "Kamu akan bertemu dengan karakter-karakter menarik dan membuat pilihan yang mempengaruhi alur cerita."

    show ayu pointing with dissolve

    a "Jadi, siap untuk memulai petualangan coding-mu?"

    jump are_you_ready

label are_you_ready:
    menu:
        "Ya, aku siap!":
            if (confirm_ready == 0):
                
                show ayu excited with dissolve

                a "Hebat! Mari kita langsung mulai!"

                show ayu amused with dissolve

                a "Kamu bersemangat sekali! Tapi sebelum itu, ada baiknya aku ingatkan bahwa belajar itu butuh kesabaran dan ketekunan."
                a "Nantinya, kamu juga bisa membuat game-mu sendiri, lho!"
                a "Tapi ingat, jangan terlalu terburu-buru. Nikmati proses belajarnya, ya!"

            else:

                show ayu happy with dissolve

                a "Wah, akhirnya kamu sudah siap! Aku senang mendengarnya!"

                show ayu laughing with dissolve

                a "Perlu meyakinkan kamu [confirm_ready] kali, ya? Hehe."

                show ayu relaxed with dissolve

                a "Tapi yang penting sekarang kamu sudah siap untuk memulai petualangan coding-mu!"
                a "Semoga kamu menikmati proses belajarnya!"
                a "Ingat, kesabaran dan ketekunan adalah kunci utama dalam belajar."

            jump lesson_menu

        "Belum siap, aku butuh waktu lebih banyak.":
            show ayu thinking with dissolve
            a "Tidak masalah! Ambil waktu yang kamu butuhkan. Ketika kamu siap, aku akan menunggumu di sini."

            show ayu relaxed with dissolve
            a "Ingat, belajar adalah sebuah perjalanan, bukan tujuan akhir. Jadi, nikmati prosesnya!"

            show ayu pointing with dissolve
            a "Jadi, apakah kamu sudah siap untuk memulai petualangan coding-mu?"

            $ confirm_ready += 1
            jump are_you_ready

label lesson_menu:
    scene jombor lineart with fade
    
    menu:
        "1. Pengenalan Pemrograman":
            jump lesson_1

        "2. Struktur Dasar Program":
            jump lesson_2

        "3. Tipe Data dan Variabel":
            jump lesson_3

        "4. Operator dan Ekspresi":
            jump lesson_4

        "5. Percabangan":
            jump lesson_5

        "6. Perulangan":
            jump lesson_6

        "7. Fungsi":
            jump lesson_7

        "8. Membuat Game di Ren'Py":
            jump lesson_8

        "Keluar":
            menu:
                "Ya, aku yakin ingin keluar.":
                    return

                "Tidak, aku ingin kembali ke menu pelajaran.":
                    jump lesson_menu

label lesson_1:
    scene classroom morning with fade

    show ayu relaxed with moveinright:
        xalign 0.25
        yalign 1.0
    pause 0.5

    show ayu smiling with dissolve

    a "Selamat datang di pelajaran pertama: Pengenalan Pemrograman!"
    a "Pemrograman adalah proses menulis instruksi yang dapat dimengerti oleh komputer untuk melakukan tugas tertentu."
    a "Dengan pemrograman, kita dapat membuat berbagai aplikasi, mulai dari situs web hingga game."
    a "Bahasa pemrograman adalah alat yang kita gunakan untuk menulis instruksi tersebut."
    a "Seperti halnya bahasa manusia, bahasa pemrograman memiliki tata bahasa dan aturan yang harus diikuti agar komputer dapat memahaminya."
    a "Pada intinya, pemrograman adalah membuat komputer melakukan apa yang kita inginkan dengan cara yang terstruktur dan logis."
    a "Jadi kita tidak perlu repot-repot melakukan semuanya secara manual karena sudah ada komputer yang membantu kita."
    a "Sekarang, mari kita bahas beberapa bahasa pemrograman yang populer."
    a "Ada banyak bahasa pemrograman yang berbeda, masing-masing dengan kelebihan dan kekurangan."
    a "Beberapa bahasa pemrograman populer termasuk Python, JavaScript, Java, C++, PHP, dan banyak lagi."
    a "Setiap bahasa pemrograman memiliki kegunaan dan aplikasi yang berbeda, jadi penting untuk memilih bahasa yang sesuai dengan kebutuhanmu."
    a "Sebagai contoh, Python sering digunakan untuk pengembangan web dan analisis data. Game yang kamu mainkan ini juga dibuat menggunakan Python!"
    a "PHP adalah bahasa yang sering digunakan untuk pengembangan web."

    show ayu excited with dissolve

    a "E-Learning sekolah kita juga dibuat menggunakan PHP, lho!"
    a "Iya, kamu tidak salah dengar. Nama bahasa pemrogramannya memang PHP."

    show ayu laughing with dissolve

    a "Bukan singkatan dari 'Pemberi Harapan Palsu'. Hahahaha. Tapi singkatan dari 'PHP: Hypertext Preprocessor' ya!"

    show ayu relaxed with dissolve

    a "Berikutnya, Java banyak digunakan untuk aplikasi Android, dan C++ sering digunakan dalam pengembangan game."
    a "JavaScript adalah bahasa yang digunakan untuk membuat situs web interaktif."
    a "Java dan JavaScript sebenarnya adalah dua bahasa yang berbeda, meskipun namanya mirip."
    a "Meskipun namanya mirip, perbedaannya ibarat naga dan nagasari."
    a "Jadi, itulah pengenalan singkat tentang pemrograman dan beberapa bahasa pemrograman populer."
    a "Pada mata pelajaran ini, kita akan fokus pada Python dan Ren'Py, yang merupakan bahasa dan engine yang digunakan untuk membuat visual novel seperti ini."
    a "Sebelumnya, kita sudah pernah belajar tentang dasar-dasar Python kan?"
    a "Kalau belum, tidak apa-apa. Kita akan mengulangnya sedikit demi sedikit."
    a "Jadi, jangan khawatir jika kamu merasa belum siap. Aku akan membantumu sepanjang perjalanan ini."
    a "Kalau tidak salah, dulu kita sudah belajar tentang variabel, tipe data, dan operator dasar."
    a "Kita juga sudah belajar tentang percabangan kan?"
    a "Sebelumnya, kita belajar menggunakan Jupyter Notebook."
    a "Di sini, kita akan belajar menggunakan Ren'Py, yang merupakan engine untuk membuat visual novel."
    a "Ren'Py menggunakan bahasa pemrograman Python, jadi kamu akan merasa familiar."

    show ayu pointing with dissolve

    a "Sebaiknya kamu tidak lupa ya dengan aturan penulisan kode di Python."
    a "Karena di Ren'Py, kita juga akan menulis kode menggunakan Python."
    a "Jadi, spasi dan indentasi itu penting! Indentasi adalah lebar spasi di awal baris kode."
    a "Di Python, indentasi biasanya menggunakan 4 spasi."

    show ayu laughing with dissolve

    a "Kan tidak lucu kalau kamu menulis kode di Python, tapi indentasinya berantakan."
    a "Nanti bisa-bisa programnya tidak berjalan, atau malah error terus."
    a "Ujung-ujungnya kamu malah stress sendiri. Padahal salahmu cuma di indentasi doang."
    a "Hehehe."

    show ayu relaxed with dissolve

    a "Oke, sepertinya itu saja untuk pelajaran pertama ini."
    a "Kalau kamu sudah siap, kita bisa lanjut ke kuis singkat untuk menguji pemahamanmu."
    a "Kalau kamu merasa belum siap, tidak apa-apa. Kita bisa ulangi lagi nanti."
    a "Jadi, kamu mau lanjut ke kuis sekarang?"

    menu:
        "Ya, aku siap untuk kuis!":
            jump quiz_1

        "Belum, aku ingin mengulang pelajarannya.":
            jump lesson_1

        "Tidak, aku ingin kembali ke menu pelajaran.":
            jump lesson_menu

label quiz_1:
    define quiz_1_score = 0

    scene library bookshelf with fade

    show ayu relaxed with moveinleft:
        xalign 0.25
        yalign 1.0
    pause 0.5

    show ayu amused with dissolve

    a "Hehehe. Oke, mari kita mulai kuisnya!"

    show ayu pointing with dissolve
    a "Soal pertama: Apa itu pemrograman?"
    menu:
        "Proses menulis instruksi untuk komputer agar melakukan tugas tertentu.":
            $ quiz_1_score += 1

            show ayu happy with dissolve
            a "Benar! Pemrograman adalah proses menulis instruksi yang dapat dimengerti oleh komputer untuk melakukan tugas tertentu."

        "Cara untuk memperbaiki komputer yang rusak.":
            show ayu thinking with dissolve
            a "Hampir benar, tapi bukan itu. Pemrograman adalah proses menulis instruksi yang dapat dimengerti oleh komputer untuk melakukan tugas tertentu."

        "Bahasa yang digunakan manusia untuk berkomunikasi.":
            show ayu laughing with dissolve
            a "Hahaha. Bukan itu. Pemrograman adalah proses menulis instruksi yang dapat dimengerti oleh komputer untuk melakukan tugas tertentu."

        "Proses memperbaiki kesalahan dalam kode.":
            show ayu thinking with dissolve
            a "Hampir benar, tapi bukan itu. Pemrograman adalah proses menulis instruksi yang dapat dimengerti oleh komputer untuk melakukan tugas tertentu."

    show ayu pointing with dissolve
    a "Soal kedua: Apa tujuan dari pemrograman?"
    menu:
        "Menyibukkan diri.":
            show ayu laughing with dissolve
            a "Hahaha. Kalo gabut sih mending main game aja. Bukan itu. Tujuan dari pemrograman adalah untuk membuat komputer melakukan tugas tertentu sesuai dengan instruksi yang kita berikan."

        "Merancang dan membuat animasi.":
            show ayu thinking with dissolve
            a "Bukan itu. Tujuan dari pemrograman adalah untuk membuat komputer melakukan tugas tertentu sesuai dengan instruksi yang kita berikan."

        "Membuat komputer melakukan tugas tertentu sesuai dengan instruksi yang kita berikan.":
            $ quiz_1_score += 1

            show ayu happy with dissolve
            a "Benar! Tujuan dari pemrograman adalah untuk membuat komputer melakukan tugas tertentu sesuai dengan instruksi yang kita berikan."

        "Menghancurkan komputer.":
            show ayu laughing with dissolve
            a "Hahaha. Bukan itu. Tujuan dari pemrograman adalah untuk membuat komputer melakukan tugas tertentu sesuai dengan instruksi yang kita berikan."

    show ayu pointing with dissolve
    a "Soal ketiga: Apa itu bahasa pemrograman?"
    menu:
        "Bahasa yang digunakan manusia untuk berkomunikasi.":
            show ayu laughing with dissolve
            a "Hahaha. Bukan itu. Bahasa pemrograman adalah alat yang kita gunakan untuk menulis instruksi yang dapat dimengerti oleh komputer."

        "Bahasa yang digunakan untuk ngodein doi.":
            show ayu amused with dissolve
            a "Yaelah malah ngodein doi. Hahaha. Bukan itu. Bahasa pemrograman adalah alat yang kita gunakan untuk menulis instruksi yang dapat dimengerti oleh komputer."

        "Bahasa yang digunakan untuk menulis instruksi yang dapat dimengerti oleh komputer.":
            $ quiz_1_score += 1

            show ayu happy with dissolve
            a "Benar! Bahasa pemrograman adalah alat yang kita gunakan untuk menulis instruksi yang dapat dimengerti oleh komputer."

        "Bahasa yang digunakan untuk bercanda.":
            show ayu laughing with dissolve
            a "Hahaha. Bukan itu. Bahasa pemrograman adalah alat yang kita gunakan untuk menulis instruksi yang dapat dimengerti oleh komputer."

    show ayu pointing with dissolve
    a "Soal keempat: Bahasa pemrograman apa yang digunakan untuk membuat game ini?"
    menu:
        "Java":
            show ayu laughing with dissolve
            a "Hahaha. Bukan itu. Game ini dibuat menggunakan Ren'Py, yang menggunakan bahasa pemrograman Python."

        "Python":
            $ quiz_1_score += 1

            show ayu happy with dissolve
            a "Benar! Game ini dibuat menggunakan Ren'Py, yang menggunakan bahasa pemrograman Python."

        "PHP":
            show ayu thinking with dissolve
            a "Itu mah bahasa pemrograman untuk web. Dipakai buat bikin E-Learning sekolah kita. Bukan itu. Game ini dibuat menggunakan Ren'Py, yang menggunakan bahasa pemrograman Python."

        "JaviraScript":
            show ayu laughing with dissolve
            a "Hahahaha. Bahasa apa itu? Bukan itu. Game ini dibuat menggunakan Ren'Py, yang menggunakan bahasa pemrograman Python."

    show ayu pointing with dissolve
    a "Soal kelima: Mengapa indentasi itu penting di Python?"
    menu:
        "Untuk menunjukkan blok kode.":
            $ quiz_1_score += 1

            show ayu happy with dissolve
            a "Benar! Indentasi digunakan untuk menunjukkan blok kode di Python."

        "Untuk mempercantik tampilan kode.":
            show ayu thinking with dissolve
            a "Hmmm. Bukan itu. Indentasi digunakan untuk menunjukkan blok kode di Python."

        "Agar kode terlihat rapi.":
            show ayu laughing with dissolve
            a "Ada benarnya juga, tapi bukan itu tujuan utamanya. Indentasi digunakan untuk menunjukkan blok kode di Python."

        "Supaya komputer tidak bingung.":
            show ayu amused with dissolve
            a "Hahaha. Bukan itu. Indentasi digunakan untuk menunjukkan blok kode di Python."

    show ayu relaxed with dissolve
    a "Oke, itu saja untuk kuis singkat ini!"
    a "Dari 5 soal, kamu mendapatkan [quiz_1_score] jawaban benar."

    if (quiz_1_score == 5):
        show ayu excited with dissolve
        a "Wah, sempurna! Kamu benar-benar menguasai materi ini!"
        a "Hebat sekali!"

    elif (quiz_1_score >= 3):
        show ayu happy with dissolve
        a "Bagus! Kamu sudah memahami sebagian besar materi ini."
        a "Teruskan usaha baikmu!"

    else:
        show ayu thinking with dissolve
        a "Tidak apa-apa. Mungkin kamu perlu mengulang pelajarannya lagi."
        a "Jangan menyerah, ya! Aku yakin kamu bisa lebih baik lagi."

    menu:
        "Aku ingin mengulangi kuisnya.":
            jump quiz_1

        "Jelaskan lagi pelajarannya.":
            jump lesson_1

        "Aku ingin kembali ke menu pelajaran.":
            jump lesson_menu

    
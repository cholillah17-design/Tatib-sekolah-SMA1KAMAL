# QUIZ JAWA TIMUR (10 SOAL)
questions = [
    {
        "question": "1. Apa ibu kota Provinsi Jawa Timur?",
        "options": ["a. Surabaya", "b. Malang", "c. Kediri", "d. Blitar"],
        "answer": "a"
    },
    {
        "question": "2. Gunung tertinggi di Jawa Timur adalah?",
        "options": ["a. Semeru", "b. Bromo", "c. Arjuno", "d. Raung"],
        "answer": "a"
    },
    {
        "question": "3. Ikon hewan di Tugu Surabaya adalah?",
        "options": ["a. Harimau & Ayam", "b. Sapi & Banteng", "c. Suro & Boyo", "d. Kuda & Singa"],
        "answer": "c"
    },
    {
        "question": "4. Kota yang dijuluki Kota Apel adalah?",
        "options": ["a. Jember", "b. Malang", "c. Gresik", "d. Lamongan"],
        "answer": "b"
    },
    {
        "question": "5. Tari tradisional terkenal dari Jawa Timur adalah?",
        "options": ["a. Tari Pendet", "b. Tari Kuda Lumping", "c. Tari Gandrung", "d. Tari Jaipong"],
        "answer": "c"
    },
    # 10 SOAL TAMBAHAN
    {
        "question": "6. Kota di Jawa Timur yang dijuluki Kota Reog adalah?",
        "options": ["a. Kediri", "b. Ponorogo", "c. Madiun", "d. Gresik"],
        "answer": "b"
    },
    {
        "question": "7. Candi peninggalan Majapahit yang terbesar di Jawa Timur (terletak di Blitar) adalah?",
        "options": ["a. Candi Singasari", "b. Candi Penataran", "c. Candi Jago", "d. Candi Trowulan"],
        "answer": "b"
    },
    {
        "question": "8. Jembatan terpanjang di Indonesia yang menghubungkan Pulau Jawa (Surabaya) dan Pulau Madura adalah?",
        "options": ["a. Suramadu", "b. Kedung Cowek", "c. Kalikuto", "d. Pasupati"],
        "answer": "a"
    },
    {
        "question": "9. Makanan khas Surabaya yang terkenal dengan isian irisan hidung sapi (cingur)?",
        "options": ["a. Pecel", "b. Rawon", "c. Rujak Cingur", "d. Tahu Tek"],
        "answer": "c"
    },
    {
        "question": "10. Pelabuhan utama dan tersibuk di Jawa Timur yang melayani perdagangan internasional adalah?",
        "options": ["a. Tanjung Perak", "b. Ketapang", "c. Probolinggo", "d. Gresik"],
        "answer": "a"
    },
    
]

score = 0
total_questions = len(questions) # Total pertanyaan sekarang 10

print("=== QUIZ JAWA TIMUR ===")
print("Jawab dengan memilih: a / b / c / d\n")

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
        
    # Menggunakan strip() untuk menghilangkan spasi ekstra
    answer = input("Jawaban kamu: ").strip().lower()
    if answer == q["answer"]:
        print("✔ Betul!\n")
        score += 1
    else:
        # Menambahkan informasi jawaban yang benar 
        print(f"✘ Salah! Jawaban yang benar adalah {q['answer'].upper()}.\n")

# --- Bagian Perhitungan dan Tampilan Skor Akhir ---

# Hitung skor persentase (Skor Benar / Total Soal) * 100
# Contoh: 9 benar dari 10 soal -> (9/10) * 100 = 90
final_score = (score / total_questions) * 100

print("=== HASIL AKHIR ===")
print(f"Jawaban benar: {score} dari {total_questions}")
print(f"Skor Akhir Kamu: {final_score:.0f}") # Menampilkan skor persentase (misal: 90)

if score == total_questions:
    print("Keren! Kamu sangat mengenal Jawa Timur!")
elif final_score >= 80:
    print("Hebat! Pengetahuanmu tentang Jawa Timur sangat bagus.")
elif final_score >= 50:
    print("Good job! Pengetahuanmu tentang Jawa Timur lumayan.")
else:
    print("Masih perlu belajar lagi tentang Jawa Timur nih!")
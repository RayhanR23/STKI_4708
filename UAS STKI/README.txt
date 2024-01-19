*Dataset
Dataset yang digunakan berasal dari kaggle yakni https://www.kaggle.com/datasets/arnabchaki/popular-video-games-1980-2023/data dimana ada 1511 data dengan 10 kolom berupa index,nama game,tanggal rilis,tim developer,rating,total list dari user,total review dari user,genre,deskripsi,dan review user

*Permasalahan dan Tujuan Eksperimen
Permasalahan dalam eksperimen ini adalah bagaimana mengembangkan sebuah mesin pencarian game yang efisien dan efektif dengan menerapkan metode Vector Space Model pada deskripsi sebuah game, sehingga mampu memberikan hasil pencarian yang relevan dan berkualitas kepada pengguna dalam menghadapi masalah informasi berlebih di industri game.

*Model dan Alur Tahapan Eksperimen
Untuk model yang digunakan ialah Vector Space Model,jadi user akan memberikan sebuah inputan berupa query mengenai game dalam bahasa inggris sesuai dengan keiinginan user dan query tersebut akan dibandingkan dengan semua data yang ada pada dataset. Dari perbandingan tersebut akan diurut dokumen mana yang memiliki nilai kemiripan paling tinggi dengan query dari user

*Uji Performa Model
Uji performa model dilakukan dengan menggunakan stopwords untuk memilah kata-kata yang kurang penting pada deskripsi game dan query,setelah dipilah kata-kata tersebut kemudian diberikan bobot,dan kemudian dihitung nilai kemiripannya dengan query menggunakan VSM. Setelah itu nilai kemiripan akan diurut dari tertinggi ke terendah

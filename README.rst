PUEBI — Pedoman Umum Ejaan Bahasa Indonesia
==========================================

Repositori ini menyusun kembali **Pedoman Umum Ejaan Bahasa Indonesia (PUEBI)**
yang ditetapkan melalui *Peraturan Menteri Pendidikan dan Kebudayaan Republik
Indonesia Nomor 50 Tahun 2015* dan diterbitkan oleh Badan Pengembangan dan
Pembinaan Bahasa, Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi.

Tujuan
------

Menyediakan dokumentasi PUEBI yang:

* mudah dinavigasi per bab dan per aturan,
* ditautkan silang antar-bab,
* memuat catatan perbandingan dengan edisi ejaan sebelumnya (EYD 1972,
  EYD 1987, dan EYDB 1991), dan
* dapat dibangun secara statis dengan `Sphinx` lalu dipublikasikan ke
  `Read the Docs`.

Ruang Lingkup
-------------

Empat bab utama sesuai dokumen resmi:

* **Bab I** — Pemakaian Huruf (abjad, vokal, konsonan, diftong,
  gabungan konsonan, kapital, miring, tebal)
* **Bab II** — Penulisan Kata (kata dasar, berimbuhan, bentuk ulang,
  gabungan kata, pemenggalan, kata depan, partikel, singkatan dan
  akronim, angka dan bilangan, kata ganti, kata sandang)
* **Bab III** — Tanda Baca
* **Bab IV** — Penulisan Unsur Serapan

Halaman tambahannya (``bahasa-jawa``, ``nama-keren``, ``nama-panggilan``,
``tulisan-miring``) adalah materi pelengkap di luar naskah resmi PUEBI.

Membangun Dokumentasi Secara Lokal
----------------------------------

Butuh Python 3.10 atau yang lebih baru. Jalankan:

.. code-block:: console

   (.venv) $ pip install -r docs/requirements.txt
   (.venv) $ cd docs
   (.venv) $ sphinx-build -T -E -b html -d _build/doctrees -D language=id . _build/html

Hasil build HTML akan tersedia di ``docs/_build/html/index.html``.

Atau gunakan target ``make`` yang sudah disediakan:

.. code-block:: console

   (.venv) $ cd docs
   (.venv) $ make html

Deployment
----------

Konfigurasi Read the Docs ada di ``.readthedocs.yaml``. Baca
`panduan RTD v2 <https://docs.readthedocs.io/en/stable/config-file/v2.html>`_
bila perlu menyesuaikannya.

Kontribusi
----------

Kontribusi perbaikan terhadap dokumen ini sangat terbuka. Beberapa hal
yang perlu diperhatikan:

* Pertahankan nomor aturan (mis. ``I.F.3``, ``II.H.2.b``, ``III.A.1``,
  ``IV.a``) supaya tetap cocok dengan dokumen resmi.
* Penomoran sub-aturan menggunakan format Indonesia (a, b, c) untuk
  sub-aturan pertama, kemudian ``1, 2, 3`` untuk tingkat berikutnya.
* Konsolidasikan "Catatan" yang membandingkan dengan edisi sebelumnya ke
  akhir setiap aturan.
* Hindari membuat klaim baru tentang ejaan yang tidak ada di dokumen
  resmi.

Lisensi
-------

Dokumen resmi PUEBI ini diterbitkan oleh pemerintah Republik Indonesia.
Repositori PUEBI mendokumentasikan ulang isi PUEBI untuk keperluan
navigasi dan pencarian. Aturan ejaan itu sendiri tunduk pada peraturan
perundang-undangan yang berlaku.

EYD Edisi V — Ejaan Bahasa Indonesia yang Disempurnakan
=======================================================

Repositori ini menyajikan kaidah **Ejaan Bahasa Indonesia yang
Disempurnakan (EYD) Edisi V** dalam format dokumentasi Sphinx,
disarikan dari laman resmi Badan Pengembangan dan Pembinaan Bahasa,
Kementerian Pendidikan Dasar dan Menengah.

Latar Belakang
--------------

EYD Edisi V ditetapkan melalui *Keputusan Kepala Badan Pengembangan dan
Pembinaan Bahasa Nomor 0424/I/BS.00.01/2022* tanggal 16 Agustus 2022 dan
menggantikan *Pedoman Umum Ejaan Bahasa Indonesia* (PUEBI) 2015.

Struktur
--------

.. code-block:: text

   docs/
     index.rst
     penggunaan-huruf/
     penulisan-kata/
     penggunaan-tanda-baca/
     unsur-serapan/

Membangun Dokumentasi
---------------------

.. code-block:: console

   (.venv) $ pip install -r docs/requirements.txt
   (.venv) $ cd docs
   (.venv) $ sphinx-build -T -E -b html -d _build/doctrees -D language=id . _build/html

Sumber
------

Kaidah pada repositori ini disarikan dari laman resmi EYD V:
https://ejaan.kemendikdasmen.go.id.

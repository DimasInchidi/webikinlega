from django.shortcuts import render


def index(request):
    data = {
        'nama': 'OnlineLega',
        'usaha': 'Web Instant',
        'slogan': 'Punya web, memang bikin lega',
        'title_img': 'https://cdn.wallpaper.com/main/galleries/15/11/google-03.jpg',
        'config': {

        },
        'row_about': (
            (
                {
                    'icon': 'flash_on',
                    'title': 'Hasil Cepat',
                    'desc': 'Pembuatan web untuk anda dalam waktu singkat, bahkan bisa ditunggu!'
                },
                {
                    'icon': 'forum',
                    'title': 'Komunikasi',
                    'desc': 'Jangan ragu untuk bertanya! Karena kami akan selalu transparan mengenai website anda.',
                },
                {
                    'icon': 'free_breakfast',
                    'title': 'Sederhana',
                    'desc': 'Proses yang mudah dan sederhana. Halaman menajemen dibuat se-sederhana mungkin untuk kemudahan anda. Pesan, tunggu, lihat hasil, baru bayar.',
                },
                {
                    'icon': 'event',
                    'title': 'Masa Aktif',
                    'desc': 'Kami memberikan masa aktif website anda hingga 1 tahun dan garansi 6 bulan untuk harga yang sangat murah.',
                },
            ),
        ),
        'row_barang': (
            # first row
            (
                {
                    'nama': 'Jangkauan',
                    'gambar': 'https://cdn.wallpaper.com/wallpaper/live/galleryimages/17050154/gallery/testuser5_oct2007_02_prada_meech_tiaqkU_BxaGcF.jpg',
                    'harga': '150000',
                    'keterangan': 'Jangkau lebih banyak konsumen anda',
                    'medium_lenght': 12 / 3,
                },
                {
                    'nama': 'Kepercayaan',
                    'gambar': 'https://cdn.wallpaper.com/wallpaper/live/images/1383838052_Saint_Laurent_video_F.jpg',
                    'harga': '150000',
                    'keterangan': 'Dapatkan kepercayaan lebih dengan website sebagai identitas anda',
                    'medium_lenght': 12 / 3,
                },
                {
                    'nama': 'Komunikasi',
                    'gambar': 'https://cdn.wallpaper.com/wallpaper/live/galleryimages/17051935/gallery/01_Etienne-Russo_as230610.jpg',
                    'harga': '150000',
                    'keterangan': 'Konsumen akan lebih mudah mencari anda',
                    'medium_lenght': 12 / 3,
                },
            ),
            (
                # second row
            )
        ),
        'testi': (
            {
                'gambar': 'http://samevine.co.uk/assets/uploads/2015/05/Testimony.jpg',
            },
        ),
        'foot': {
            'about': 'Kami adalah web developer profesional yang menyediakan website murah untuk usaha anda.',
            'kontak': [
                ('https://facebook.com/diamsaja', 'Facebook'),
                ('https://instagram.com/dimasinchidi', 'Instagram'),
                ('https://github.com/dimasinchidi', 'Github')
            ]

        }
    }
    return render(request, 'base.html', data)

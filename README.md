# File Analyzer

File Analyzer, PE (Portable Executable) dosyalarını analiz eden ve zararlı yazılımları tespit etmek için Yara kuralları kullanan bir Python aracıdır. Ayrıca, dosya izinlerini kontrol etme ve analiz raporları oluşturma özellikleri sunar.

## Özellikler

- PE dosya formatı analizi
- Yara kuralları ile zararlı yazılım tespiti
- Dosya izinlerinin kontrolü
- Analiz raporları oluşturma

## Gereksinimler

- Python 3.x
- `pefile` modülü
- `yara-python` modülü

## Kurulum

1. **Python'u Yükleyin:** [Python İndir](https://www.python.org/downloads/)
2. **Gerekli Paketleri Yükleyin:** `pip install pefile yara-python`
3. **Depoyu Klonlayın:** `git clone https://github.com/username/file-analyzer.git && cd file-analyzer`

## Kullanım

### PE Dosyası Analizi

PE dosyası analizini başlatmak için:
`python file_analyzer.py <file_path>`

### Yara Tespiti

Yara kuralları ile zararlı yazılım tespiti yapmak için:
`python yara_scanner.py <file_path> <rule_file>`

### Dosya İzinleri Kontrolü

Dosya izinlerini kontrol etmek için:
`python activity_monitor.py <file_path>`

### Rapor Oluşturma

Rapor oluşturmak için:
`python report_generator.py`

## Örnekler

### PE Dosyası Analizi

`python file_analyzer.py C:\path\to\testfile.exe`

### Yara Tespiti

`python yara_scanner.py C:\path\to\testfile.exe C:\path\to\rules.yara`

### Dosya İzinleri Kontrolü

`python activity_monitor.py C:\path\to\testfile.exe`

### Rapor Oluşturma

`python report_generator.py`

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya `issues` açarak geri bildirimde bulunun.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## İletişim

- [GitHub Profilim](https://github.com/azizyilmazcetin)
- Email: azizyilmazcetin@gmail.com

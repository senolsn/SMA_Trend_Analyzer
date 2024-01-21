# Yatırım Trend Analiz Betiği

## Yasal Uyarı
Bu Python betiği yalnızca eğitim ve öğretim amacı taşımaktadır. Sunulan veriler ve analizler, herhangi bir yatırım tavsiyesi olarak değerlendirilmemelidir. Finansal kararlarınızı verirken kendi araştırmanızı yapmalı ve uzman tavsiyelerine başvurmalısınız. Bu betiğin kullanımından kaynaklanan herhangi bir zarardan sorumluluk kabul edilmemektedir.

## Betiğin İşlevi
Bu Python betiği, yatırımcılara bir hisse senedinin belirli hareketli ortalamalara göre trend analizi yapma imkanı sunar. Hareketli ortalamaların geçmiş performansını kullanarak, mevcut fiyatın bu ortalamalara göre konumunu belirler ve olası bir trend değişikliğini gösterir.

## Kullanım
Proje için gerekli paketleri yüklemek ve sanal ortamı oluşturmak için aşağıdaki adımları takip edin:
1. Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) Python'u indirip yükleyin.
2. Terminal veya komut istemcisine gidin ve projenin bulunduğu dizine gidin.
3. Sanal ortamı oluşturun:
    ```bash
    python -m venv analyzer
    ```
4. Sanal ortamı etkinleştirin:
   - Windows:
     ```bash
     .\analyzer\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source analyzer/bin/activate
     
5. Gerekli paketleri indirmek için terminal veya komut istemcisine şu komutları yazın:
    ```bash
    pip install pandas yfinance tabulate colorama
    ```
6. Betiği çalıştırmak için terminal veya komut istemcisine gidin ve betiği çalıştırın:
    ```bash
    python MA_Trend_Analyzer.py
    ```
7. Program sizi bir hisse senedi simgesi girmeniz konusunda yönlendirecek. Örneğin, "AKBNK" gibi bir hisse senedi simgesi girin.
8. Betiğin analiz sonuçlarını görüntüleyin. Renkli simgelerle birlikte, hisse senedinin belirli hareketli ortalamalara göre mevcut trendini gösteren bir tablo görünecektir.

Betiği kullanırken dikkate almanız gereken önemli noktaları anladığınızdan emin olun ve yatırım kararlarınızı kendi analizleriniz ve uzman görüşleri temelinde verin.

## Resimler
Proje ile ilgili görseller ve ekran görüntüleri bu bölümde yer alacaktır.

![Örnek Resim](https://i.imgur.com/HxsCfuO.png)

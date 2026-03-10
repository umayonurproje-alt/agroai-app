# 38 Bitki Hastalığı Sınıfı için Türkçe Açıklamalar ve Tedavi Önerileri

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "name": "Elma - Elma Kabuğu Uyuzu (Scab)",
        "emoji": "🍎",
        "severity": "Orta",
        "description": (
            "Elma kabuğu uyuzu, Venturia inaequalis mantarı tarafından oluşan "
            "yaygın bir bitki hastalığıdır. Yapraklarda ve meyvede koyu, kadifemsi "
            "lekeler oluşturur. Islak ve serin koşullar hastalığın yayılmasını hızlandırır."
        ),
        "symptoms": [
            "Yapraklarda koyu yeşil/siyah lekeler",
            "Meyve kabuğunda çatlama ve bozulma",
            "Erken yaprak dökülmesi",
        ],
        "treatment": [
            "Fungisit uygulaması (kaptafol, maneb veya bakır bazlı)",
            "Hasta yaprak ve meyvelerin toplanıp imha edilmesi",
            "Ağaçlar arası hava sirkülasyonunu artırma",
            "Dayanıklı elma çeşitlerinin tercih edilmesi",
        ],
    },
    "Apple___Black_rot": {
        "name": "Elma - Siyah Çürüklük",
        "emoji": "🍎",
        "severity": "Yüksek",
        "description": (
            "Botryosphaeria obtusa mantarından kaynaklanan siyah çürüklük, "
            "meyvelerde, yapraklarda ve dallarda ciddi hasara yol açar. "
            "Sıcak ve nemli havalarda hızla yayılır."
        ),
        "symptoms": [
            "Yapraklarda kahverengi halkalı lekeler (Frog-eye lekesi)",
            "Meyvede siyah, çürük alanlar",
            "Dallar üzerinde kanser benzeri lezyonlar",
        ],
        "treatment": [
            "Hasta sürgün ve dalların budanması",
            "Captan veya thiophanate-methyl içerikli fungisit",
            "Bahçe hijyenine dikkat edilmesi",
            "Hasarlı meyvelerin toplanması",
        ],
    },
    "Apple___Cedar_apple_rust": {
        "name": "Elma - Sedir-Elma Pası",
        "emoji": "🍎",
        "severity": "Orta",
        "description": (
            "Gymnosporangium juniperi-virginianae mantarının neden olduğu bu pas "
            "hastalığı, hem ard ağacı (sedir/ardıç) hem de elma ağacına ihtiyaç duyar. "
            "Yapraklarda turuncu sarı lekeler oluşturur."
        ),
        "symptoms": [
            "Yaprak üstünde parlak turuncu/sarı lekeler",
            "Yaprak altında tüp şeklinde sporlar",
            "Erken yaprak dökülmesi",
        ],
        "treatment": [
            "Yakın çevredeki ardıç/sedir ağaçlarını uzaklaştırın",
            "Myclobutanil veya trifloxystrobin fungisitleri",
            "İlkbaharda koruyucu fungisit uygulaması",
            "Pas'a dayanıklı elma çeşitleri tercih edin",
        ],
    },
    "Apple___healthy": {
        "name": "Elma - Sağlıklı",
        "emoji": "🍎",
        "severity": "Yok",
        "description": "Bitkinin yaprakları sağlıklı görünmektedir. Herhangi bir hastalık belirtisi tespit edilmedi.",
        "symptoms": [],
        "treatment": [
            "Düzenli sulama ve gübreleme yapın",
            "Periyodik budama ile hava sirkülasyonu sağlayın",
            "Koruyucu fungisit programı uygulayın",
        ],
    },
    "Blueberry___healthy": {
        "name": "Yaban Mersini - Sağlıklı",
        "emoji": "🫐",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor, hastalık belirtisi yok.",
        "symptoms": [],
        "treatment": [
            "Asidik toprak pH'ını koruyun (4.5-5.5)",
            "Düzenli sulama ve organik malçlama",
        ],
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "name": "Kiraz - Külleme Hastalığı",
        "emoji": "🍒",
        "severity": "Orta",
        "description": (
            "Podosphaera clandestina mantarının neden olduğu külleme, "
            "kiraz yapraklarını beyaz unlu bir tabaka ile kaplar. "
            "Kuru ve sıcak havalarda yaygınlaşır."
        ),
        "symptoms": [
            "Yapraklarda beyaz, unlu kaplama",
            "Yaprak kıvrılması ve büyüme geriliği",
            "Genç sürgünlerde şekil bozukluğu",
        ],
        "treatment": [
            "Kükürt veya potasyum bikarbonat fungisiti",
            "Aşırı azotlu gübreden kaçının",
            "Bitki arası hava akışını artırın",
            "Hasta yaprakları imha edin",
        ],
    },
    "Cherry_(including_sour)___healthy": {
        "name": "Kiraz - Sağlıklı",
        "emoji": "🍒",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Düzenli bakım ve budama yapın"],
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "name": "Mısır - Gri Yaprak Lekesi",
        "emoji": "🌽",
        "severity": "Yüksek",
        "description": (
            "Cercospora zeae-maydis mantarından kaynaklanan gri yaprak lekesi, "
            "mısır üretiminde ciddi verim kayıplarına yol açabilir. "
            "Yapraklarda uzun, gri-kahverengi lekeler oluşturur."
        ),
        "symptoms": [
            "Yapraklarda dikdörtgen gri-kahve lekeler",
            "Erken yaprak kuruma",
            "Verim kaybı",
        ],
        "treatment": [
            "Triazol veya strobilurin grubu fungisitler",
            "Dayanıklı hibrit çeşit kullanımı",
            "Ekim nöbeti uygulaması",
            "Tarla artıklarının toprağa işlenmesi",
        ],
    },
    "Corn_(maize)___Common_rust_": {
        "name": "Mısır - Yaygın Pas",
        "emoji": "🌽",
        "severity": "Orta",
        "description": (
            "Puccinia sorghi mantarı tarafından oluşturulan mısır pası, "
            "yapraklarda kiremit kırmızısı renkte pustüller oluşturur."
        ),
        "symptoms": [
            "Yaprak yüzeyinde kırmızı-kahve oval pustüller",
            "Ağır enfeksiyonda yaprak sararması",
        ],
        "treatment": [
            "Mancozeb veya propiconazole fungisiti",
            "Dayanıklı çeşit seçimi",
            "Erken ekim dönemini tercih etme",
        ],
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "name": "Mısır - Kuzey Yaprak Yanıklığı",
        "emoji": "🌽",
        "severity": "Yüksek",
        "description": (
            "Exserohilum turcicum mantarından kaynaklanan bu hastalık, "
            "uzun sigara şeklinde kahverengi lekeler oluşturur ve ciddi verim kayıplarına neden olabilir."
        ),
        "symptoms": [
            "Uzun, soluk yeşil-kahverengi lekeler (5-15 cm)",
            "Yaprak üzerinde koyu sporlar",
            "Şiddetli vakalarda bitkinin tamamen kuruma",
        ],
        "treatment": [
            "Propiconazole veya azoxystrobin fungisiti",
            "Dayanıklı hibrit kullanımı",
            "Ekim nöbeti ve toprak işleme",
        ],
    },
    "Corn_(maize)___healthy": {
        "name": "Mısır - Sağlıklı",
        "emoji": "🌽",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Dengeli gübreleme ve sulama programı uygulayın"],
    },
    "Grape___Black_rot": {
        "name": "Üzüm - Siyah Çürüklük",
        "emoji": "🍇",
        "severity": "Yüksek",
        "description": (
            "Guignardia bidwellii mantarının neden olduğu siyah çürüklük, "
            "üzüm bağlarında ciddi meyve kayıplarına yol açar."
        ),
        "symptoms": [
            "Yapraklarda küçük sarı lekeler, zamanla kahverengi",
            "Meyvelerde siyah, buruşmuş görüntü (mumya üzüm)",
        ],
        "treatment": [
            "Mancozeb veya myclobutanil uygulaması",
            "Mumya meyvelerin toplanıp imha edilmesi",
            "İyi havalandırma için budama",
        ],
    },
    "Grape___Esca_(Black_Measles)": {
        "name": "Üzüm - Esca (Siyah Kızamık)",
        "emoji": "🍇",
        "severity": "Yüksek",
        "description": (
            "Birden fazla mantarın neden olduğu karmaşık bir hastalık. "
            "Yapraklarda kaplan derisi görünümü ve meyvelerde mor lekeler oluşturur."
        ),
        "symptoms": [
            "Yapraklarda sarı/kırmızı şeritlenme (kaplan derisi)",
            "Üzümlerde mor, siyah lekeler",
            "Dal içinde kahverengi çürüme",
        ],
        "treatment": [
            "Hasta dalların budanıp imha edilmesi",
            "Propiconazole uygulaması",
            "Yara yerlerine fungisitli macun sürülmesi",
        ],
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "name": "Üzüm - Yaprak Yanıklığı",
        "emoji": "🍇",
        "severity": "Orta",
        "description": (
            "Isariopsis clavispora mantarının neden olduğu yaprak yanıklığı, "
            "gelişmiş yapraklarda düzensiz kahverengi lekeler oluşturur."
        ),
        "symptoms": [
            "Yaprak kenarlarında kahverengi lekeler",
            "Lekelerin çevresinde sarı hale",
            "Erken yaprak dökülmesi",
        ],
        "treatment": [
            "Bakırlı fungisit uygulaması",
            "Sulama sırasında yaprakları ıslatmaktan kaçının",
            "İyi havalandırma sağlayın",
        ],
    },
    "Grape___healthy": {
        "name": "Üzüm - Sağlıklı",
        "emoji": "🍇",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Bağ bakımını düzenli yapın, budama programına uyun"],
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "name": "Portakal - Turunçgil Yeşillenmesi (HLB)",
        "emoji": "🍊",
        "severity": "Çok Yüksek",
        "description": (
            "Candidatus Liberibacter bakterisinin neden olduğu HLB, "
            "turunçgil üretiminde en yıkıcı hastalıklardan biridir. "
            "Yapraklarda asimetrik sarılık ve meyvelerde ciddi bozulmaya yol açar."
        ),
        "symptoms": [
            "Yapraklarda asimetrik sarılık (sarı-yeşil mozaik)",
            "Küçük, şekli bozuk, acı meyveler",
            "Erken meyve dökülmesi",
        ],
        "treatment": [
            "⚠️ Kesin tedavisi yoktur! Hasta ağaçlar sökülerek imha edilmeli",
            "Hastalığı taşıyan Asya psyllid böceğine karşı ilaçlama",
            "Sertifikalı fidan kullanımı",
            "Sıkı karantina önlemleri",
        ],
    },
    "Peach___Bacterial_spot": {
        "name": "Şeftali - Bakteriyel Benek",
        "emoji": "🍑",
        "severity": "Orta",
        "description": (
            "Xanthomonas campestris bakterisinin neden olduğu bu hastalık, "
            "yaprak, dal ve meyvede lezyonlar oluşturur."
        ),
        "symptoms": [
            "Yapraklarda su emdirilmiş görünümlü lekeler",
            "Lekeler kuruyunca delik oluşumu (buckshot)",
            "Meyve yüzeyinde çatlak ve lekeler",
        ],
        "treatment": [
            "Bakır oksiklorid içerikli ilaç uygulaması",
            "Dayanıklı çeşit seçimi",
            "Hasta dal ve yaprakları uzaklaştırın",
        ],
    },
    "Peach___healthy": {
        "name": "Şeftali - Sağlıklı",
        "emoji": "🍑",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Düzenli bakım ve koruyucu ilaçlama programı uygulayın"],
    },
    "Pepper,_bell___Bacterial_spot": {
        "name": "Biber - Bakteriyel Benek",
        "emoji": "🫑",
        "severity": "Orta",
        "description": (
            "Xanthomonas campestris pv. vesicatoria bakterisinin neden olduğu "
            "bu hastalık, sulama suyu ve yağmurla hızla yayılır."
        ),
        "symptoms": [
            "Yapraklarda küçük, su emdirilmiş lekeler",
            "Lekelerin sararması ve dökülmesi",
            "Meyvede üzeri çäkur lekeler",
        ],
        "treatment": [
            "Bakır bazlı bakterisit uygulaması",
            "Sertifikalı, hastalıksız tohum kullanımı",
            "Damla sulama sistemi tercih edilmesi",
            "Ekim nöbeti",
        ],
    },
    "Pepper,_bell___healthy": {
        "name": "Biber - Sağlıklı",
        "emoji": "🫑",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Dengeli sulama ve gübreleme yapın"],
    },
    "Potato___Early_blight": {
        "name": "Patates - Erken Yaprak Yanıklığı",
        "emoji": "🥔",
        "severity": "Orta",
        "description": (
            "Alternaria solani mantarından kaynaklanan erken yanıklık, "
            "yaşlı yapraklarda koyu kahverengi halkalar (boğa gözü) oluşturur."
        ),
        "symptoms": [
            "Yapraklarda konsantrik halkalar ile koyu lekeler",
            "Yaprak sararması ve erken dökülmesi",
            "Şiddetli vakalarda gövde lezyonları",
        ],
        "treatment": [
            "Chlorothalonil veya mancozeb fungisiti",
            "Alçak yoğunluklu dikim yapılması",
            "Fazla nem ve yaprak ıslaklığından kaçınılması",
        ],
    },
    "Potato___Late_blight": {
        "name": "Patates - Geç Yaprak Yanıklığı",
        "emoji": "🥔",
        "severity": "Çok Yüksek",
        "description": (
            "Phytophthora infestans oomikota'sının neden olduğu geç yanıklık, "
            "tarihin en yıkıcı bitki hastalıklarından biridir (1840'lar İrlanda Büyük Açlığı). "
            "24-48 saat içinde tarlayı mahvedebilir."
        ),
        "symptoms": [
            "Yapraklarda su emdirilmiş, koyu kahverengi lekeler",
            "Yaprak altında beyaz küfümsü sporlar",
            "Kötü kokulu, çürüyen bitki",
            "Yumrularda kahverengi-mor çürüme",
        ],
        "treatment": [
            "Metalaxyl + mancozeb kombinasyonu fungisit",
            "Hasta bitkilerin derhal söküp imha edilmesi",
            "Hava tahminini takip ederek koruyucu ilaçlama",
            "Dayanıklı çeşit kullanımı (Sarpo Mira vb.)",
        ],
    },
    "Potato___healthy": {
        "name": "Patates - Sağlıklı",
        "emoji": "🥔",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Düzenli sulama, dengeli gübreleme ve ekim nöbeti uygulayın"],
    },
    "Raspberry___healthy": {
        "name": "Ahududu - Sağlıklı",
        "emoji": "🍓",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Yıllık budama ve organik malçlama yapın"],
    },
    "Soybean___healthy": {
        "name": "Soya Fasulyesi - Sağlıklı",
        "emoji": "🌿",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["İyi drenaj ve uygun ekim sıklığı sağlayın"],
    },
    "Squash___Powdery_mildew": {
        "name": "Kabak - Külleme",
        "emoji": "🎃",
        "severity": "Orta",
        "description": (
            "Podosphaera xanthii mantarından kaynaklanan külleme, "
            "kabakgil sebzelerinde çok yaygın ve hızla yayılan bir hastalıktır."
        ),
        "symptoms": [
            "Yapraklarda parlak beyaz-gri toz görünümü",
            "Yaprak kıvrılması ve sararması",
            "Erken yaprak dökülmesi",
        ],
        "treatment": [
            "Kükürt veya potasyum bikarbonat spreyi",
            "Süt-su karışımı (1:9) doğal alternatif",
            "İyi havalandırma sağlayın",
            "Aşırı azot gübresinden kaçının",
        ],
    },
    "Strawberry___Leaf_scorch": {
        "name": "Çilek - Yaprak Yanması",
        "emoji": "🍓",
        "severity": "Orta",
        "description": (
            "Diplocarpon earlianum mantarından kaynaklanan yaprak yanması, "
            "çilek yapraklarında kırmızı-mor lekeler oluşturur."
        ),
        "symptoms": [
            "Yaprak yüzeyinde küçük kırmızı-mor noktalar",
            "Ağır enfeksiyonda yaprak kahverengileşme ve kuruma",
            "Bitki gücünde azalma",
        ],
        "treatment": [
            "Captan veya myclobutanil fungisiti",
            "Sulama sistemini damla sulamaya çevirin",
            "Yoğun bitki örtüsünü seyrekleştirin",
            "Sonbaharda eski yaprakları temizleyin",
        ],
    },
    "Strawberry___healthy": {
        "name": "Çilek - Sağlıklı",
        "emoji": "🍓",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Düzenli çapa ve mulçlama yapın, azot gübresi dengeli kullanın"],
    },
    "Tomato___Bacterial_spot": {
        "name": "Domates - Bakteriyel Benek",
        "emoji": "🍅",
        "severity": "Orta",
        "description": (
            "Xanthomonas perforans bakterisinin neden olduğu bu hastalık, "
            "sera ve açık tarla domatesciliğinde yaygın bir sorundur."
        ),
        "symptoms": [
            "Yapraklarda küçük, su emdirilmiş lekeler",
            "Lekelerin çevresinde sarı hale",
            "Meyvede yüzeysel, sert lekeler",
        ],
        "treatment": [
            "Bakır bazlı bakterisit",
            "Hastalıksız tohum ve fide kullanımı",
            "Yaprak ıslamasını en aza indirin",
            "Ekim nöbeti uygulayın",
        ],
    },
    "Tomato___Early_blight": {
        "name": "Domates - Erken Yanıklık",
        "emoji": "🍅",
        "severity": "Orta",
        "description": (
            "Alternaria solani mantarından kaynaklanan erken yanıklık, "
            "domateste en yaygın yaprak hastalıklarından biridir. "
            "Boğa gözü benzeri konsantrik lekeler oluşturur."
        ),
        "symptoms": [
            "Yaşlı yapraklarda koyu kahve halkalar (boğa gözü)",
            "Yaprak sararması ve dökülmesi",
            "Meyve sapı yakınında siyah lekeler",
        ],
        "treatment": [
            "Chlorothalonil, mancozeb veya azoxystrobin",
            "Alt yaprakların uzaklaştırılması",
            "Mulçlama ile toprak-yaprak temasını azaltma",
            "Sulama zamanlamasına dikkat edin",
        ],
    },
    "Tomato___Late_blight": {
        "name": "Domates - Geç Yanıklık",
        "emoji": "🍅",
        "severity": "Çok Yüksek",
        "description": (
            "Phytophthora infestans'ın neden olduğu geç yanıklık, "
            "serin ve nemlil havalarda 3-5 gün içinde tarlayı yakabilir."
        ),
        "symptoms": [
            "Yapraklarda su emdirilmiş geniş lekeler",
            "Yaprak altında beyaz küf",
            "Kara-kahverengi gövde lezyonları",
        ],
        "treatment": [
            "Cymoxanil + mancozeb veya metalaxyl kombinasyonu",
            "Hasta bitkileri derhal imha edin",
            "Hava durumu takibiyle ilaçlama yapın",
        ],
    },
    "Tomato___Leaf_Mold": {
        "name": "Domates - Yaprak Küfü",
        "emoji": "🍅",
        "severity": "Orta",
        "description": (
            "Passalora fulva mantarından kaynaklanan yaprak küfü, "
            "özellikle sera domatesciliğinde görülen önemli bir hastalıktır."
        ),
        "symptoms": [
            "Yaprak üstünde soluk sarı lekeler",
            "Yaprak altında kadife görünümlü yeşil-kahve küf",
            "Yaprak sararması ve dökülmesi",
        ],
        "treatment": [
            "Chlorothalonil veya maneb fungisiti",
            "Sera nem ve ısısını kontrol edin",
            "Hasta yaprakları hemen uzaklaştırın",
        ],
    },
    "Tomato___Septoria_leaf_spot": {
        "name": "Domates - Septoria Yaprak Lekesi",
        "emoji": "🍅",
        "severity": "Orta",
        "description": (
            "Septoria lycopersici mantarından kaynaklanan bu hastalık, "
            "domateste en yaygın yaprak hastalıklarından biridir."
        ),
        "symptoms": [
            "Küçük, yuvarlak lekeler (koyu kenar, açık merkez)",
            "Leke içinde küçük siyah nokta (piknidia)",
            "Yoğun enfeksiyonda yaprak dökülmesi",
        ],
        "treatment": [
            "Mancozeb, chlorothalonil veya copper-based fungisit",
            "Alt yaprakları uzaklaştırın",
            "Mulçlama ile topraktan bulaşmayı önleyin",
        ],
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "name": "Domates - İki Noktalı Kırmızı Örümcek",
        "emoji": "🍅",
        "severity": "Orta",
        "description": (
            "Tetranychus urticae zararlısı yaprak özsu emip yapraklarda "
            "gümüşümsü bronz renk bozukluğuna yol açar. Kuru ve sıcak havalarda patlama yapar."
        ),
        "symptoms": [
            "Yaprakta gümüşümsü-bronz renk bozukluğu",
            "Yaprak altında ince ağ ve küçük hareketli noktalar",
            "Yaprak dökülmesi ve bitki gücünde azalma",
        ],
        "treatment": [
            "Akarisit (abamektin, bifenazate)",
            "Yüksek basınçlı su püskürtme",
            "Doğal düşman: Phytoseiulus persimilis böceği",
            "Bitkiler arası nemlendirme artırma",
        ],
    },
    "Tomato___Target_Spot": {
        "name": "Domates - Hedef Lekesi",
        "emoji": "🍅",
        "severity": "Orta",
        "description": (
            "Corynespora cassiicola mantarından kaynaklanan hedef lekesi, "
            "konsantrik halkalar içeren kahverengi lekeler oluşturur."
        ),
        "symptoms": [
            "Yapraklarda hedef tahtası görünümlü lekeler",
            "Meyve yüzeyinde depresif lekeler",
            "Erken yaprak ve meyve dökümü",
        ],
        "treatment": [
            "Chlorothalonil veya azoxystrobin fungisiti",
            "İyi havalandırma sağlayın",
            "Gece yaprak ıslamasını önleyin",
        ],
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "name": "Domates - Sarı Yaprak Kıvırma Virüsü",
        "emoji": "🍅",
        "severity": "Çok Yüksek",
        "description": (
            "TYLCV, beyazsinek (Bemisia tabaci) tarafından taşınan bir virüstür. "
            "Genç bitkilerde enfeksiyona uğradığında %100'e varan verim kaybına neden olabilir."
        ),
        "symptoms": [
            "Yapraklarda yukarı doğru kıvrılma",
            "Yapraklarda sararma ve küçülme",
            "Bitki bodurlaşması",
            "Çiçek ve meyve bağlamama",
        ],
        "treatment": [
            "⚠️ Virüs için kimyasal tedavi yoktur",
            "Beyazsinekle mücadele: imidacloprid veya pymetrozine",
            "Sarı yapışkan tuzak kullanımı",
            "TYLCV'ye dayanıklı çeşit kullanımı",
            "Sert enfekteli bitkileri söküp imha edin",
        ],
    },
    "Tomato___Tomato_mosaic_virus": {
        "name": "Domates - Mozaik Virüsü",
        "emoji": "🍅",
        "severity": "Yüksek",
        "description": (
            "Tomato Mosaic Virus (ToMV), tohum, toprak ve mekanik yolla çok kolay yayılır. "
            "Yapraklarda mozaik renk bozukluğu ve meyvelerde verim kaybı yapar."
        ),
        "symptoms": [
            "Yapraklarda açık-koyu yeşil mozaik görünüm",
            "Yaprak şekil bozukluğu",
            "Meyvelerde iç kahverengi lekeler",
        ],
        "treatment": [
            "Virüs için kimyasal ilaç yoktur",
            "Sertifikalı, virüssüz tohum kullanımı",
            "Aletler arasında %10 çamaşır suyu ile dezenfeksiyon",
            "Hasta bitkileri imha edin, sigara içmekten kaçının (ToMV yayabilir)",
        ],
    },
    "Tomato___healthy": {
        "name": "Domates - Sağlıklı",
        "emoji": "🍅",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor. Herhangi bir hastalık belirtisi tespit edilmedi.",
        "symptoms": [],
        "treatment": [
            "Dengeli sulama ve gübreleme programı uygulayın",
            "Hava sirkülasyonunu artırmak için budama yapın",
            "Koruyucu fungisit programı izleyin",
        ],
    },
    # ═══════════════════════════════════════════════════════════════
    # 20K Crop Disease Dataset — Buğday, Pamuk, Pirinç, Şeker Kamışı
    # Not: Sınıf isimleri veri setindeki klasör isimlerine göre
    # eğitim sonrası class_names.txt ile eşleşmelidir
    # ═══════════════════════════════════════════════════════════════
    # ── BUĞDAY (Wheat) ──
    "Wheat___Brown_Rust": {
        "name": "Buğday - Kahverengi Pas",
        "emoji": "🌾",
        "severity": "Yüksek",
        "description": (
            "Puccinia triticina mantarının neden olduğu kahverengi pas, "
            "dünya genelinde buğdayda en yaygın hastalıklardan biridir. "
            "Yaprak yüzeyinde turuncu-kahverengi pustüller oluşturur."
        ),
        "symptoms": [
            "Yapraklarda küçük, turuncu-kahverengi pustüller",
            "Pustüller yaprak üst yüzeyinde dağınık",
            "Ağır enfeksiyonda erken yaprak kuruma",
        ],
        "treatment": [
            "Propiconazole veya tebuconazole fungisiti",
            "Dayanıklı buğday çeşitleri kullanımı",
            "Erken ekim ile hastalık döneminden kaçınma",
            "Ekim nöbeti uygulaması",
        ],
    },
    "Wheat___Yellow_Rust": {
        "name": "Buğday - Sarı Pas",
        "emoji": "🌾",
        "severity": "Çok Yüksek",
        "description": (
            "Puccinia striiformis mantarının neden olduğu sarı pas, "
            "serin ve nemli bölgelerde buğdayda ciddi verim kayıplarına yol açar. "
            "Yapraklarda sarı çizgili pustüller oluşturur."
        ),
        "symptoms": [
            "Yaprak damarları boyunca sarı-turuncu pustül şeritleri",
            "Yaprak uçlarından başlayan lekeler",
            "Şiddetli vakalarda bitkinin tamamen sararması",
        ],
        "treatment": [
            "Triazol grubu fungisitler (propiconazole, tebuconazole)",
            "Dirençli çeşit kullanımı",
            "Erken uyarı sistemi ile zamanında ilaçlama",
        ],
    },
    "Wheat___Healthy": {
        "name": "Buğday - Sağlıklı",
        "emoji": "🌾",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Dengeli gübreleme ve sulama programı uygulayın"],
    },
    "Wheat___Septoria": {
        "name": "Buğday - Septoria Yaprak Lekesi",
        "emoji": "🌾",
        "severity": "Yüksek",
        "description": (
            "Septoria tritici mantarı tarafından oluşturulan bu hastalık, "
            "buğday yapraklarında kahverengi-sarı lekeler yaratır ve verim kaybına neden olur."
        ),
        "symptoms": [
            "Yapraklarda oval kahverengi lekeler",
            "Lekelerin içinde siyah noktalar (piknidia)",
            "Alt yapraklardan başlayarak yukarı yayılma",
        ],
        "treatment": [
            "Azoxystrobin veya chlorothalonil fungisiti",
            "Dirençli çeşit seçimi",
            "Ekim nöbeti ve sap parçalama",
        ],
    },
    # ── PAMUK (Cotton) ──
    "Cotton___Bacterial_Blight": {
        "name": "Pamuk - Bakteriyel Yanıklık",
        "emoji": "🏵️",
        "severity": "Yüksek",
        "description": (
            "Xanthomonas citri pv. malvacearum bakterisinin neden olduğu bu hastalık, "
            "pamuk yapraklarında köşeli su emdirilmiş lekeler oluşturur."
        ),
        "symptoms": [
            "Yapraklarda köşeli, su emdirilmiş lekeler",
            "Lekelerin kahverengileşmesi ve kuruması",
            "Kozalarda siyah lezyonlar",
        ],
        "treatment": [
            "Sertifikalı, hastalıksız tohum kullanımı",
            "Bakırlı ilaç uygulaması",
            "Ekim nöbeti (2-3 yıl)",
            "Hasta bitki artıklarının imhası",
        ],
    },
    "Cotton___Curl_Virus": {
        "name": "Pamuk - Yaprak Kıvırma Virüsü",
        "emoji": "🏵️",
        "severity": "Çok Yüksek",
        "description": (
            "Beyazsinek (Bemisia tabaci) tarafından taşınan bu virüs, "
            "pamuk bitkisinde ciddi verim kayıplarına yol açar."
        ),
        "symptoms": [
            "Yapraklarda yukarı veya aşağı kıvrılma",
            "Yaprak küçülmesi ve koyu yeşilleşme",
            "Bitki bodurlaşması",
            "Koza oluşumunda azalma",
        ],
        "treatment": [
            "⚠️ Virüse karşı kimyasal tedavi yoktur",
            "Beyazsinekle mücadele (imidacloprid, thiamethoxam)",
            "Dirençli pamuk çeşitlerinin tercih edilmesi",
            "Sarı yapışkan tuzak kullanımı",
        ],
    },
    "Cotton___Fusarium_Wilt": {
        "name": "Pamuk - Fusarium Solgunluğu",
        "emoji": "🏵️",
        "severity": "Yüksek",
        "description": (
            "Fusarium oxysporum f.sp. vasinfectum mantarının neden olduğu solgunluk, "
            "toprak kaynaklı bir hastalık olup iletim demetlerini tıkayarak bitkiyi soldurur."
        ),
        "symptoms": [
            "Tek taraflı yaprak sararması",
            "Bitkinin aniden solması",
            "Gövde kesitinde kahverengi halka (iletim demeti)",
        ],
        "treatment": [
            "Dirençli pamuk çeşitleri kullanımı",
            "Toprak solarizasyonu",
            "Uzun süreli ekim nöbeti (5-7 yıl)",
            "Toprak fumigasyonu (ciddi vakalarda)",
        ],
    },
    "Cotton___Healthy": {
        "name": "Pamuk - Sağlıklı",
        "emoji": "🏵️",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Dengeli gübreleme ve zararlı takibi yapın"],
    },
    # ── PİRİNÇ (Rice) ──
    "Rice___Brown_Spot": {
        "name": "Pirinç - Kahverengi Leke",
        "emoji": "🍚",
        "severity": "Orta",
        "description": (
            "Bipolaris oryzae mantarının neden olduğu kahverengi leke hastalığı, "
            "pirinç yapraklarında oval kahverengi lekeler oluşturur."
        ),
        "symptoms": [
            "Yapraklarda oval, kahverengi lekeler",
            "Lekelerin etrafında sarı hale",
            "Tanelerde beneklenme",
        ],
        "treatment": [
            "Mancozeb veya tricyclazole fungisiti",
            "Dengeli potasyum gübrelemesi",
            "Sertifikalı, sağlıklı tohum kullanımı",
        ],
    },
    "Rice___Leaf_Blast": {
        "name": "Pirinç - Yaprak Yanıklığı (Blast)",
        "emoji": "🍚",
        "severity": "Çok Yüksek",
        "description": (
            "Magnaporthe oryzae mantarının neden olduğu blast, "
            "pirinçte en yıkıcı hastalıklardan biridir. "
            "Yapraklarda elmas şeklinde lekeler oluşturur."
        ),
        "symptoms": [
            "Yapraklarda elmas/gözyaşı şeklinde gri-beyaz lekeler",
            "Leke kenarlarında kahverengi halka",
            "Boğum yanıkları (düğüm blast)",
        ],
        "treatment": [
            "Tricyclazole veya isoprothiolane fungisiti",
            "Aşırı azot gübrelemesinden kaçınma",
            "Dirençli pirinç çeşitleri",
            "Bitki artıklarının temizlenmesi",
        ],
    },
    "Rice___Bacterial_Leaf_Blight": {
        "name": "Pirinç - Bakteriyel Yaprak Yanıklığı",
        "emoji": "🍚",
        "severity": "Yüksek",
        "description": (
            "Xanthomonas oryzae pv. oryzae bakterisinin neden olduğu bu hastalık, "
            "yaprak kenarlarından başlayarak yaprak yüzeyini kurutur."
        ),
        "symptoms": [
            "Yaprak kenarından başlayan su emdirilmiş lekeler",
            "Lekelerin sarı-beyaz renge dönmesi",
            "Yaprakların balmumu görünümlü sızıntıları",
        ],
        "treatment": [
            "Dirençli çeşit kullanımı (en etkili yöntem)",
            "Dengeli gübrelenme (aşırı azottan kaçınma)",
            "Bakır bazlı ilaçlar",
            "Sulu alanların drenajı",
        ],
    },
    "Rice___Healthy": {
        "name": "Pirinç - Sağlıklı",
        "emoji": "🍚",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Su yönetimi ve dengeli gübreleme yapın"],
    },
    # ── ŞEKER KAMIŞI (Sugarcane) ──
    "Sugarcane___Red_Rot": {
        "name": "Şeker Kamışı - Kırmızı Çürüklük",
        "emoji": "🎋",
        "severity": "Çok Yüksek",
        "description": (
            "Colletotrichum falcatum mantarının neden olduğu kırmızı çürüklük, "
            "şeker kamışında en yıkıcı hastalıktır. Gövde içinden yayılarak bitkiyi öldürür."
        ),
        "symptoms": [
            "Gövde orta kısmında kırmızı çürüme",
            "Yapraklarda solma ve sararma",
            "Gövde kesitinde kırmızı-beyaz şeritlenme",
            "Alkol kokusu",
        ],
        "treatment": [
            "Hastalıksız tohumluk kullanımı",
            "Sıcak su ile tohum dezenfeksiyonu (52°C, 30 dk)",
            "Hasta bitkilerin söküp yakılması",
            "Dirençli çeşit kullanımı",
        ],
    },
    "Sugarcane___Rust": {
        "name": "Şeker Kamışı - Pas",
        "emoji": "🎋",
        "severity": "Yüksek",
        "description": (
            "Puccinia melanocephala mantarının neden olduğu pas hastalığı, "
            "yapraklarda turuncu-kahverengi pustüller oluşturur ve fotosentezi azaltır."
        ),
        "symptoms": [
            "Yapraklarda turuncu-kahverengi pustüller",
            "Yaprak altında koyu sporlar",
            "Ağır enfeksiyonda yaprak kuruması",
        ],
        "treatment": [
            "Dirençli çeşit kullanımı",
            "Triazol grubu fungisitler",
            "Hasta yaprakların uzaklaştırılması",
        ],
    },
    "Sugarcane___Healthy": {
        "name": "Şeker Kamışı - Sağlıklı",
        "emoji": "🎋",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Düzenli sulama ve gübreleme yapın"],
    },
    "Sugarcane___Mosaic": {
        "name": "Şeker Kamışı - Mozaik Virüsü",
        "emoji": "🎋",
        "severity": "Yüksek",
        "description": (
            "Sugarcane Mosaic Virus (SCMV) yapraklarda açık-koyu yeşil mozaik deseni oluşturur. "
            "Yaprak bitleri ile taşınır ve verim kaybına yol açar."
        ),
        "symptoms": [
            "Yapraklarda açık-koyu yeşil mozaik desen",
            "Yaprak renginin solması",
            "Bitki büyümesinde gerileme",
        ],
        "treatment": [
            "Virüssüz tohumluk kullanımı",
            "Yaprak bitlerine karşı ilaçlama",
            "Dirençli çeşit seçimi",
            "Hasta bitkilerin imhası",
        ],
    },
    # ═══════════════════════════════════════════════════════════════
    # Indoor Plant Disease Dataset — Ev Bitkileri
    # ═══════════════════════════════════════════════════════════════
    # ── ALOE VERA ──
    "Indoor_Aloe_Vera_Healthy": {
        "name": "Aloe Vera - Sağlıklı",
        "emoji": "🪴",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Parlak dolaylı ışıkta tutun, aşırı sulamadan kaçının"],
    },
    "Indoor_Aloe_Vera_Rust": {
        "name": "Aloe Vera - Pas Hastalığı",
        "emoji": "🪴",
        "severity": "Orta",
        "description": (
            "Aloe vera yapraklarında turuncu-kahverengi lekeler oluşturan mantar hastalığı. "
            "Aşırı nem ve yetersiz havalandırma ana sebeplerdir."
        ),
        "symptoms": [
            "Yapraklarda turuncu-kahverengi lekeler",
            "Yaprak yüzeyinde kabarcıklanma",
            "Yaprak uçlarında kuruma",
        ],
        "treatment": [
            "Etkilenen yaprakları kesin",
            "Sulamayı azaltın",
            "Havalandırmayı artırın",
            "Bakır bazlı fungisit uygulayın",
        ],
    },
    "Indoor_Aloe_Vera_Anthracnose": {
        "name": "Aloe Vera - Antraknoz",
        "emoji": "🪴",
        "severity": "Yüksek",
        "description": (
            "Colletotrichum mantarının neden olduğu antraknoz, "
            "yapraklarda çökük kahverengi lekeler oluşturur."
        ),
        "symptoms": [
            "Yapraklarda çökük, koyu kahverengi lekeler",
            "Lekelerin genişleyerek yaprak çürümesi",
            "Yumuşak, sulu dokular",
        ],
        "treatment": [
            "Hasta yaprakları hemen kesin",
            "Bitkiyi izole edin",
            "Sulamayı minimuma indirin",
            "Fungisitli sprey uygulayın",
        ],
    },
    "Indoor_Aloe_Vera_Leaf_Spot": {
        "name": "Aloe Vera - Yaprak Lekesi",
        "emoji": "🪴",
        "severity": "Orta",
        "description": "Yapraklarda çeşitli mantar veya bakterilerin neden olduğu lekeler.",
        "symptoms": [
            "Yapraklarda farklı boyutlarda koyu lekeler",
            "Lekelerin etrafında sarı hale",
        ],
        "treatment": [
            "Etkilenen yaprakları çıkarın",
            "Sulama sıklığını azaltın",
            "İyi drenajlı toprak kullanın",
        ],
    },
    "Indoor_Aloe_Vera_SunBurn": {
        "name": "Aloe Vera - Güneş Yanığı",
        "emoji": "🪴",
        "severity": "Düşük",
        "description": "Direkt güneş ışığına aşırı maruz kalma sonucu yapraklarda yanık oluşumu.",
        "symptoms": [
            "Yapraklarda beyaz-kahverengi yanık lekeleri",
            "Yaprak renginin solması",
            "Yaprak uçlarında kuruma",
        ],
        "treatment": [
            "Bitkiyi dolaylı ışığa taşıyın",
            "Yavaş yavaş güneşe alıştırın",
            "Yanmış yaprakları kesmeyin (iyileşebilir)",
        ],
    },
    # ── KAKTÜS (Cactus) ──
    "Indoor_Cactus_Healthy": {
        "name": "Kaktüs - Sağlıklı",
        "emoji": "🌵",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Az sulayın, bol güneş verin, kışın sulamayı kesin"],
    },
    "Indoor_Cactus_Dactylopius_Opuntia": {
        "name": "Kaktüs - Koşnil Böceği",
        "emoji": "🌵",
        "severity": "Yüksek",
        "description": (
            "Dactylopius coccus böceği kaktüs yüzeyinde beyaz pamuksu kitleler oluşturur. "
            "Bitki özsuyu emerek bitkiyi zayıflatır."
        ),
        "symptoms": [
            "Beyaz pamuksu kitleler",
            "Ezildiğinde kırmızı renk (karmin boya)",
            "Bitkinin zayıflaması ve solması",
        ],
        "treatment": [
            "Alkollü pamukla tek tek temizleyin",
            "Yüksek basınçlı su ile yıkayın",
            "Neem yağı spreyi uygulayın",
            "Ağır vakalarda insektisit kullanın",
        ],
    },
    # ── PARA ÇİÇEĞİ (Money Plant) ──
    "Indoor_Money_Plant_Healthy": {
        "name": "Para Çiçeği - Sağlıklı",
        "emoji": "🌿",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Dolaylı ışık, düzenli sulama, ayda bir sıvı gübre"],
    },
    "Indoor_Money_Plant_Bacterial_Wilt": {
        "name": "Para Çiçeği - Bakteriyel Solgunluk",
        "emoji": "🌿",
        "severity": "Yüksek",
        "description": (
            "Bakterilerin iletim demetlerini tıkamasıyla oluşan solgunluk. "
            "Aşırı sulama ve kötü drenaj ana sebeplerdir."
        ),
        "symptoms": [
            "Yaprakların aniden solması",
            "Gövde tabanında kahverengi leke",
            "Kök çürümesi belirtileri",
        ],
        "treatment": [
            "Sulamayı hemen durdurun",
            "Sağlam kısımlardan çelik alın",
            "Hasta kısımları kesin",
            "Yeni, steril toprak kullanın",
        ],
    },
    "Indoor_Money_Plant_Manganese_Toxicity": {
        "name": "Para Çiçeği - Manganez Toksisitesi",
        "emoji": "🌿",
        "severity": "Orta",
        "description": "Toprakta aşırı manganez birikimi yapraklarda kahverengi beneklere neden olur.",
        "symptoms": [
            "Yaşlı yapraklarda kahverengi benekler",
            "Yaprak damarlarının kahverengileşmesi",
            "Büyüme yavaşlaması",
        ],
        "treatment": [
            "Toprak pH'ını 6.0-6.5'e ayarlayın",
            "Saksıyı bol su ile yıkayın (leach)",
            "Temiz toprakla değiştirin",
        ],
    },
    # ── YILAN BİTKİSİ (Snake Plant) ──
    "Indoor_Snake_Plant_Healthy": {
        "name": "Yılan Bitkisi - Sağlıklı",
        "emoji": "🌿",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Az sulayın (2-3 haftada bir), dolaylı-az ışık yeterli"],
    },
    "Indoor_Snake_Plant_Anthracnose": {
        "name": "Yılan Bitkisi - Antraknoz",
        "emoji": "🌿",
        "severity": "Yüksek",
        "description": "Mantar kaynaklı hastalık, yapraklarda çökük kahverengi lekeler oluşturur.",
        "symptoms": [
            "Yapraklarda çökük, koyu lekeler",
            "Lekeler üzerinde turuncu sporlar",
            "Yaprak yumuşaması ve çürüme",
        ],
        "treatment": [
            "Hasta yaprakları dipten kesin",
            "Sulamayı azaltın",
            "Yaprakları ıslatmaktan kaçının",
            "Bakır bazlı fungisit",
        ],
    },
    "Indoor_Snake_Plant_Leaf_Withering": {
        "name": "Yılan Bitkisi - Yaprak Solması",
        "emoji": "🌿",
        "severity": "Orta",
        "description": "Aşırı sulama, soğuk veya kök çürümesinden kaynaklanan yaprak solması.",
        "symptoms": [
            "Yaprakların yumuşaması ve eğilmesi",
            "Yaprak tabanında sarı-kahverengi lekeler",
            "Kök bölgesinde kötü koku",
        ],
        "treatment": [
            "Sulamayı hemen durdurun",
            "Kök çürümesi varsa sağlam köklerle yeniden dikin",
            "İyi drenajlı kaktüs toprağı kullanın",
            "Sıcak ve kuru ortamda tutun",
        ],
    },
    # ── ÖRÜMCEK BİTKİSİ (Spider Plant) ──
    "Indoor_Spider_Plant_Healthy": {
        "name": "Örümcek Bitkisi - Sağlıklı",
        "emoji": "🌿",
        "severity": "Yok",
        "description": "Bitki sağlıklı görünüyor.",
        "symptoms": [],
        "treatment": ["Parlak dolaylı ışık, düzenli sulama, yaz aylarında sıvı gübre"],
    },
    "Indoor_Spider_Plant_Fungal_Leaf_Spot": {
        "name": "Örümcek Bitkisi - Mantar Yaprak Lekesi",
        "emoji": "🌿",
        "severity": "Orta",
        "description": "Mantar kaynaklı yaprak lekesi, nemli koşullarda yaygınlaşır.",
        "symptoms": [
            "Yapraklarda kahverengi-siyah yuvarlak lekeler",
            "Lekelerin büyümesi ve birleşmesi",
            "Yaprak uçlarında kuruma",
        ],
        "treatment": [
            "Etkilenen yaprakları kesin",
            "Yaprakları ıslatmadan sulayın",
            "Havalandırmayı artırın",
            "Neem yağı veya bakır fungisit",
        ],
    },
    "Indoor_Spider_Plant_Leaf_Tip_Necrosis": {
        "name": "Örümcek Bitkisi - Yaprak Ucu Nekrozu",
        "emoji": "🌿",
        "severity": "Düşük",
        "description": (
            "Yaprak uçlarının kahverengileşip kuruması. "
            "Genellikle şebekeden gelen flor veya klor nedeniyle oluşur."
        ),
        "symptoms": [
            "Yaprak uçlarının kahverengileşmesi",
            "Uçlardan yaprak boyunca kuruma ilerlemesi",
        ],
        "treatment": [
            "Arıtılmış veya dinlendirilmiş su kullanın",
            "Kahverengi uçları makasla kesin",
            "Düzenli ama aşırı olmayan sulama yapın",
            "Flor içeren gübrelerden kaçının",
        ],
    },
}

# Sınıf listesi (train klasörü sırasına göre)
CLASS_NAMES = sorted(DISEASE_INFO.keys())

def get_disease_info(class_name: str) -> dict:
    """Model çıktısı olan sınıf adına göre Türkçe hastalık bilgilerini döner."""
    info = DISEASE_INFO.get(class_name, {
        "name": class_name.replace("_", " ").replace("___", " - "),
        "emoji": "🌿",
        "severity": "Bilinmiyor",
        "description": "Bu hastalık hakkında bilgi mevcut değil.",
        "symptoms": [],
        "treatment": ["Bir uzmanla görüşün."],
    })
    return info

SEVERITY_COLORS = {
    "Yok": "#22c55e",
    "Orta": "#f59e0b",
    "Yüksek": "#ef4444",
    "Çok Yüksek": "#dc2626",
    "Bilinmiyor": "#6b7280",
}

def get_severity_color(severity: str) -> str:
    return SEVERITY_COLORS.get(severity, "#6b7280")

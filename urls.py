import unzipper
from typing import Final


SAAD_AL_GHAMADI: Final[unzipper.Unzipper] = unzipper.AyatUnzipper(
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_1-3.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_4-6.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_7-9.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_10-12.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_13-15.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_16-18.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_19-21.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_22-24.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_25-27.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Ghamadi_40kbps/Ghamadi_40kbps_28-30.ayt",
)

MUHAMMAD_JIBREEL: Final[unzipper.Unzipper] = unzipper.AyatUnzipper(
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_1-3.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_4-6.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_7-9.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_10-12.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_13-15.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_16-18.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_19-21.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_22-24.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_25-27.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Muhammad_Jibreel_64kbps/Muhammad_Jibreel_64kbps_28-30.ayt",
)

HUDHAIFY: Final[unzipper.Unzipper] = unzipper.AyatUnzipper(
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_1-3.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_4-6.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_7-9.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_10-12.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_13-15.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_16-18.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_19-21.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_22-24.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_25-27.ayt",
    "https://quran.ksu.edu.sa/ayat/download/Hudhaify_64kbps/Hudhaify_64kbps_28-30.ayt",
)

ABDUL_BASIT_MURATTAL: Final[unzipper.Unzipper] = unzipper.EveryAyahUnzipper(
    "https://everyayah.com/data/Abdul_Basit_Murattal_192kbps/000_versebyverse.zip"
)

HUSARY: Final[unzipper.Unzipper] = unzipper.EveryAyahUnzipper(
    "https://everyayah.com/data/Husary_128kbps/000_versebyverse.zip"
)

MINSHAWY_MURATTAL: Final[unzipper.Unzipper] = unzipper.EveryAyahUnzipper(
    "https://everyayah.com/data/Minshawy_Murattal_128kbps/000_versebyverse.zip"
)


YASSER_AD_DUSSARY: Final[unzipper.Unzipper] = unzipper.EveryAyahUnzipper(
    "https://everyayah.com/data/Yasser_Ad-Dussary_128kbps/000_versebyverse.zip"
)

MOHAMMAD_AL_TABLAWAY: Final[unzipper.Unzipper] = unzipper.EveryAyahUnzipper(
    "https://everyayah.com/data/Mohammad_al_Tablaway_128kbps/000_versebyverse.zip"
)

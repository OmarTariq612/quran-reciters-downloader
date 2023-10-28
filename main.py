from unzipper import Unzipper
from urls import *
from os import mkdir, chdir
from shutil import make_archive
from typing import Final


def main():
    RECITERS: Final[list[Unzipper]] = [
        SAAD_AL_GHAMADI,
        MUHAMMAD_JIBREEL,
        ABDUL_BASIT_MURATTAL,
        HUSARY,
        MINSHAWY_MURATTAL,
        HUDHAIFY,
        YASSER_AD_DUSSARY,
        MOHAMMAD_AL_TABLAWAY,
    ]

    mkdir("audio")
    chdir("audio")

    for reciter in RECITERS:
        reciter.unzip_from_source()

    chdir("..")
    print("[INFO] creating audio zip file")
    make_archive("audio", "zip", base_dir="audio")


if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod
from shutil import copyfileobj, rmtree
import urllib.parse
import urllib3
import zipfile
from os import path, mkdir, chdir, getcwd, link, remove
from glob import glob


class Unzipper(ABC):
    @abstractmethod
    def unzip_from_source(self) -> None:
        pass


class AyatUnzipper(Unzipper):
    AYAT_EXT = ".ayt"

    def __init__(self, url: str, *rest_urls: str) -> None:
        self.urls = [url, *rest_urls]
        basename = path.basename(path.splitext(urllib.parse.urlparse(url).path)[0])
        self.all_ayat_dirname = basename[: basename.rfind("_")]
        self.http_client = urllib3.PoolManager(
            cert_reqs="CERT_NONE"
        )  # currently ayat website has invalid certificate

        for url in self.urls:
            _, ext = path.splitext(urllib.parse.urlparse(url).path)
            if ext != AyatUnzipper.AYAT_EXT:
                raise ValueError(f"Invalid extenstion: '{ext}'")

    def unzip_from_source(self) -> None:
        mkdir(self.all_ayat_dirname)
        chdir(self.all_ayat_dirname)

        print(f"[INFO] unzip_from_source: {self.all_ayat_dirname}")

        for url in self.urls:
            basename = path.basename(path.splitext(urllib.parse.urlparse(url).path)[0])
            mkdir("zipcontent")
            zipfile_name = path.join("zipcontent", f"{basename}.zip")

            print(f"\tdownloading: {basename}")

            with open(zipfile_name, "wb") as archive:
                response = self.http_client.request("GET", url, preload_content=False)
                copyfileobj(response, archive)

            with zipfile.ZipFile(zipfile_name, "r") as archive:
                print(f"\textracting: {basename}")
                archive.extractall("zipcontent")

            audio_files_path = path.join(
                getcwd(), "zipcontent", "audio", self.all_ayat_dirname
            )

            print(f"\tlinking: {basename}")

            for filename in glob(f"{audio_files_path}/*.mp3"):
                basename = path.basename(filename)
                link(
                    filename, basename
                )  # just create a hard link (we don't really need to copy the content)

            rmtree("zipcontent", ignore_errors=True)

        chdir("..")


class EveryAyahUnzipper(Unzipper):
    def __init__(self, url: str) -> None:
        self.url = url
        self.all_ayat_dirname = path.split(
            path.split(urllib.parse.urlparse(url).path)[0]
        )[1]

    def unzip_from_source(self) -> None:
        mkdir(self.all_ayat_dirname)
        chdir(self.all_ayat_dirname)

        print(f"[INFO] unzip_from_source: {self.all_ayat_dirname}")

        print(f"\tdownloading: {self.all_ayat_dirname}")

        zipfile_name = self.all_ayat_dirname
        with open(zipfile_name, "wb") as archive:
            response = urllib3.request("GET", self.url, preload_content=False)
            copyfileobj(response, archive)

        with zipfile.ZipFile(zipfile_name, "r") as archive:
            print(f"\textracting: {self.all_ayat_dirname}")
            archive.extractall()

        for filename in set(glob("*")) - set(glob("*.mp3")):
            remove(filename)

        chdir("..")

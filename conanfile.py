from conan.tools.microsoft import msvc_runtime_flag
from conans import ConanFile, CMake, tools
import functools
import os
import re
import shutil
import stat

required_conan_version = ">=1.36.0"


class TheoraConan(ConanFile):
    name = "theora"
    description = "Theora is a free and open video compression format from the Xiph.org Foundation"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/xiph/theora"
    topics = ("theora", "video", "video-compressor", "video-format")
    license = "BSD-3-Clause"

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
    }

    generators = "cmake"
    _cmake = None

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    @property
    def _build_subfolder(self):
        return "build_subfolder"

    def export_sources(self):
        self.copy("CMakeLists.txt")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            del self.options.fPIC
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd

    def requirements(self):
        self.requires("ogg/1.3.5")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version][0], strip_root=True, destination=self._source_subfolder)

        source = self.conan_data["sources"][self.version][1]
        url = source["url"]
        filename = url[url.rfind("/") + 1:]
        tools.download(url, filename)
        tools.check_sha256(filename, source["sha256"])

        shutil.move(filename, os.path.join(self._source_subfolder, "lib", filename))

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        self._cmake.configure(build_folder=self._build_subfolder)
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["theora"]


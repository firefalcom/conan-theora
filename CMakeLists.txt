cmake_minimum_required(VERSION 3.4)
project(theora)

include(conanbuildinfo.cmake)
conan_basic_setup()

set(THEORA_SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder)

add_library(theora STATIC "${THEORA_SRC_DIR}/lib/apiwrapper.c"
	"${THEORA_SRC_DIR}/lib/bitpack.c" "${THEORA_SRC_DIR}/lib/dequant.c"
	"${THEORA_SRC_DIR}/lib/fragment.c" "${THEORA_SRC_DIR}/lib/idct.c"
	"${THEORA_SRC_DIR}/lib/info.c" "${THEORA_SRC_DIR}/lib/internal.c"
	"${THEORA_SRC_DIR}/lib/state.c" "${THEORA_SRC_DIR}/lib/quant.c"
	"${THEORA_SRC_DIR}/lib/decapiwrapper.c" "${THEORA_SRC_DIR}/lib/decinfo.c"
	"${THEORA_SRC_DIR}/lib/decode.c" "${THEORA_SRC_DIR}/lib/huffdec.c")


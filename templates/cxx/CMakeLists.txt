cmake_minimum_required(VERSION 3.7)
project(prog)

set(PKG_NAMES )

file(GLOB_RECURSE SRC_LIST src/*.cxx)

find_package(PkgConfig REQUIRED)
pkg_check_modules(PKGS REQUIRED ${PKG_NAMES})
include_directories(${PKGS_INCLUDE_DIRS})
list(APPEND LIBS_LIST ${PKGS_LIBRARIES})

set(CMAKE_CXX_STANDARD 23)
add_compile_options(-Wall -Wextra -Wpedantic)

include_directories(src)

add_executable(${PROJECT_NAME} ${SRC_LIST})
target_link_libraries(${PROJECT_NAME} ${LIBS_LIST})

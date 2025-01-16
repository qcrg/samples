cmake_minimum_required(VERSION 3.10)
project(prog)

set(CXXFLAGS -Wall -Wextra -Wpedantic -ggdb)
set(PKG_NAMES )
set(BOOST_PKGS )
set(PKGS )

file(GLOB_RECURSE SRC_LIST src/*.cxx)

if (NOT "${PKG_NAMES}" STREQUAL "")
  find_package(PkgConfig REQUIRED)
  pkg_check_modules(PKGS REQUIRED $ENV{PKG_NAMES} ${PKG_NAMES})
  include_directories(${PKGS_INCLUDE_DIRS})
  list(APPEND LIBS_LIST ${PKGS_LIBRARIES})
endif ()

if (NOT "${BOOST_PKGS}" STREQUAL "")
  cmake_policy(SET CMP0167 NEW)
  find_package(Boost REQUIRED ${BOOST_PKGS})
  include_directories(${Boost_INCLUDE_DIRS})
  list(APPEND LIBS_LIST ${Boost_LIBRARIES})
endif ()

foreach (PKG IN LISTS PKGS)
  find_package(${PKG} REQUIRED)
  include_directories(${${PKG}_INCLUDE_DIRS})
  list(APPEND LIBS_LIST ${${PKG}_LIBRARIES})
endforeach ()

set(CMAKE_CXX_STANDARD 23)
add_compile_options($ENV{CXXFLAGS} ${CXXFLAGS})

include_directories(src)

add_executable(${PROJECT_NAME} ${SRC_LIST})
target_link_libraries(${PROJECT_NAME} ${LIBS_LIST})

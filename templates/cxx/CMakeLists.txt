cmake_minimum_required(VERSION 3.10)
project(prog)

option(BUILD_TESTS "Build tests" OFF)
option(INIT_THREADS "Thread enabled if tests are build" OFF)

if (BUILD_TESTS)
  add_definitions(-DBUILD_TESTS)
  set(INIT_THREADS ON)
endif ()

set(CXXFLAGS -Wall -Wextra -Wpedantic -Wconversion -ggdb)
set(PKG_NAMES )
set(BOOST_PKGS )
set(CMAKE_PKGS )

set(PROJECT_BUNDLE_NAME ${PROJECT_NAME}l)
set(MAIN_SRC_FILE_PATH ${CMAKE_SOURCE_DIR}/src/main.cxx)

file(GLOB_RECURSE SRC_LIST ${CMAKE_SOURCE_DIR}/src/*.cxx)
list(REMOVE_ITEM SRC_LIST ${MAIN_SRC_FILE_PATH})

if (POLICY CMP0167)
  cmake_policy(SET CMP0167 NEW)
endif ()

if (PKG_NAMES)
  find_package(PkgConfig REQUIRED)
  pkg_check_modules(PKGS REQUIRED $ENV{PKG_NAMES} ${PKG_NAMES})
  include_directories(${PKGS_INCLUDE_DIRS})
  list(APPEND LIBS_LIST ${PKGS_LIBRARIES})
endif ()

if (BOOST_PKGS)
  find_package(Boost REQUIRED ${BOOST_PKGS})
  include_directories(${Boost_INCLUDE_DIRS})
  list(APPEND LIBS_LIST ${Boost_LIBRARIES})
endif ()

if (INIT_THREADS)
  list(APPEND CMAKE_PKGS Threads)
endif ()

foreach (PKG IN LISTS CMAKE_PKGS)
  find_package(${PKG} REQUIRED)
  include_directories(${${PKG}_INCLUDE_DIRS})
  list(APPEND LIBS_LIST ${${PKG}_LIBRARIES})
endforeach ()

# GTEST if tests builds
if (BUILD_TESTS)
  find_package(GTest REQUIRED)
  include_directories(${GTEST_INCLUDE_DIRS})
  list(APPEND LIBS_LIST ${GTEST_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT})
endif ()

if (INIT_THREADS)
  list(APPEND LIBS_LIST ${CMAKE_THREAD_LIBS_INIT})
endif ()

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_compile_options($ENV{CXXFLAGS} ${CXXFLAGS})

include_directories(src)

if (SRC_LIST)
  add_library(${PROJECT_BUNDLE_NAME} ${SRC_LIST})
  target_link_libraries(${PROJECT_BUNDLE_NAME} ${LIBS_LIST})
else ()
  set(PROJECT_BUNDLE_NAME "")
endif ()

add_executable(${PROJECT_NAME} ${MAIN_SRC_FILE_PATH})
target_link_libraries(${PROJECT_NAME} ${PROJECT_BUNDLE_NAME})

if (BUILD_TESTS)
  add_subdirectory(test)
endif ()

file(
  CREATE_LINK
  ${MAIN_SRC_FILE_PATH}
  ${CMAKE_CURRENT_BINARY_DIR}/main.cxx
  SYMBOLIC
)

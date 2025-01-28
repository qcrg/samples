cmake_minimum_required(VERSION 3.10)
project(test)

include_directories(src)

set(MAIN_SRC_FILE ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cxx)

file(GLOB_RECURSE CURRENT_SRC_LIST ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cxx)
list(REMOVE_ITEM CURRENT_SRC_LIST ${MAIN_SRC_FILE})

add_executable(${PROJECT_NAME} ${CURRENT_SRC_LIST} ${MAIN_SRC_FILE})
target_link_libraries(${PROJECT_NAME} ${LIBS_LIST} ${PROJECT_BUNDLE_NAME})

file(
  CREATE_LINK
  ${CMAKE_CURRENT_SOURCE_DIR}/data
  ${CMAKE_CURRENT_BINARY_DIR}/data
  SYMBOLIC
)

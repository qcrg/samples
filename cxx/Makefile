PKGS := 

CXXFLAGS := -Wall -Wpedantic -Wextra -std=c++23 -O0 -ggdb

APP_NAME := $(if ${APP_NAME},${APP_NAME},prog)
BUILD_DIR := $(if ${BUILD_DIR},${BUILD_DIR},build)
SRC_DIR := $(if ${SRC_DIR},${SRC_DIR},src)

BUILD_DIR_TARGET := ${BUILD_DIR}/build_dir

BIN_PATH := ${BUILD_DIR}/${APP_NAME}
SRC := $(wildcard ${SRC_DIR}/*.cxx)
HEADER := $(wildcard ${SRC_DIR}/*.hxx)
OBJ := $(patsubst ${SRC_DIR}%,${BUILD_DIR}%,$(patsubst %.cxx,%.o,${SRC}))

run: build
	${BIN_PATH}

build: ${BUILD_DIR_TARGET} ${BIN_PATH}

${BUILD_DIR_TARGET}: 
	if [ ! -d ${BUILD_DIR} ]; then mkdir ${BUILD_DIR}; fi
	touch $@

${BIN_PATH}: ${OBJ} ${HEADER}
	${CXX} ${CXXFLAGS} `pkg-config --cflags --libs ${PKGS}` -o $@ ${OBJ}

${BUILD_DIR}/%.o: ${SRC_DIR}/%.cxx ${HEADER}
	${CXX} ${CXXFLAGS} -c -o $@ $<

clean:
	${RM} -r ${BUILD_DIR}

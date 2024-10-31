import os
import sys

bin_dir = "./RidenModbus"

if len(sys.argv) < 1:
    print("No arguments given")
    print("Possible arguments:")
    print("build")
    print("make")
    print("flash")

if "clean" in sys.argv:
    os.system("cd ./build && rm Makefile")
    os.system("cd ./build && rm CMakeCache.txt")
    os.system("cd ./build && rm -rf CMakeFiles")
    os.system("cd ./build && rm cmake_install.cmake")

if "make" in sys.argv:
    os.system("cd ./build && cmake .")

if "build" in sys.argv:
    os.system("cd ./build && make")

if "run" in sys.argv:
    os.system("cd ./build && " + bin_dir)

cmake_minimum_required(VERSION 3.22)

# Set the project name
set(PROJECT_NAME RidenModbus)
set(CMAKE_CXX_STANDARD 17)

# Set output directory of fieal executable
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY
#     "${CMAKE_SOURCE_DIR}/../deploy"
# )

# set(ENV{CXX} "/usr/bin/g++")
# set(ENV{ASM} "/usr/bin/as")
# set(ENV{CC} "/usr/bin/gcc")

# Set compiler flags
set(CMAKE_C_FLAGS "")
set(CMAKE_CXX_FLAGS "-std=gnu++17")

project(${PROJECT_NAME})

# Add the include directories
include_directories(
    ../
)

# Add the source file
set(SOURCE_FILES
    ../main.cpp
    ../riden_handler.cpp
)

# Create the executable
add_executable(${PROJECT_NAME}
    ${SOURCE_FILES}
)

# Find the required packages
# find_package(OpenGL REQUIRED)
# find_package(glfw3 REQUIRED)

# Link the ImGui library and the required backend libraries
target_link_libraries(${PROJECT_NAME} PRIVATE
    # ${CMAKE_SOURCE_DIR}/../libraries/imgui/build/libimgui.a
    # ${CMAKE_SOURCE_DIR}/../libraries/sqlite3/build/libsqlite3.a
    # OpenGL::GL
    # glfw
)

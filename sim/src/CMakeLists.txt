#
# CMakeLists.txt for src
#

# Add the necessary source files from the "examples" directory
file(GLOB EXAMPLE_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/examples/*.cpp")

# Add the necessary source files from the "lib" directory
file(GLOB LIB_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/lib/*.cpp")

# Add the necessary header files from the "include" directory
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/include")
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/../third-party/cereal/include")

# Create an executable target for each example file
foreach(EXAMPLE_SOURCE ${EXAMPLE_SOURCES})

    # Get the base name of the example file without extension
    get_filename_component(EXAMPLE_NAME ${EXAMPLE_SOURCE} NAME_WE)

    # Create a unique executable target for each example file
    add_executable(${EXAMPLE_NAME} ${EXAMPLE_SOURCE} ${LIB_SOURCES})

    # Set the output directory for each executable
    set_target_properties(${EXAMPLE_NAME} PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/../build/bin
    )

endforeach()


# Optionally, you can install the executable
# This is needed when to install the project to Global environment
# install(TARGETS ${PROJECT_NAME} DESTINATION bin)

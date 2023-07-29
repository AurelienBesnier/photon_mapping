add_executable(main "main.cpp")
target_link_libraries(main PUBLIC pm)
target_link_libraries(main INTERFACE pm)
target_include_directories(main INTERFACE "../../src/cpp/include")

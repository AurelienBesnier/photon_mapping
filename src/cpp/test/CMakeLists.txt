add_executable(test_image "test_image.cpp")
target_link_libraries(test_image PUBLIC pm)

add_executable(test_camera "test_camera.cpp")
target_link_libraries(test_camera PUBLIC pm)

add_executable(test_intersector "test_intersector.cpp")
target_link_libraries(test_intersector PUBLIC pm)

add_executable(visualize_photon_map "visualize_photon_map.cpp")
target_link_libraries(visualize_photon_map PUBLIC pm)

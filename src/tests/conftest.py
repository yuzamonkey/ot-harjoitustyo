from build import initialize_data_directories

def pytest_configure():
  initialize_data_directories()
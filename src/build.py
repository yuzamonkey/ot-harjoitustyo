import os

def initialize_data_directories():
  try:
    if os.path.exists("./data/scores"):
      print("\n BUILD HAS ALREADY BEEN COMPLETED \n 'poetry run invoke start' to start the program \n")
    else:
      data_dir = "data"
      parent_dir = "./"

      path = os.path.join(parent_dir, data_dir)
      os.mkdir(path)

      scores_dir = "scores"
      parent_dir = "./data"

      path = os.path.join(parent_dir, scores_dir)
      os.mkdir(path)

      print("\n BUILD COMPLETED \n 'poetry run invoke start' to start the program \n")
  except:
    print(
    """
  BUILD FAILED

Either build was already completed or a failure happened. Check that you don't have a diectory called 'data' already defined in the root of the project before running build.

'poetry run invoke start' starts the program, but the program is unable to load or save files. 
    """
    )

if __name__ == '__main__':
    initialize_data_directories()
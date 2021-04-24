import os

def initialize_database():
  try:
    data_dir = "data"
    parent_dir = "./"

    path = os.path.join(parent_dir, data_dir)
    os.mkdir(path)

    scores_dir = "scores"
    parent_dir = "./data"

    path = os.path.join(parent_dir, scores_dir)
    os.mkdir(path)

    print("\n BUILD COMPLETED \n")
    
  except:
    print(" \n BUILD FAILED \n")

if __name__ == '__main__':
    initialize_database()
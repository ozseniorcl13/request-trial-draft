from api import start_api
from train import start_train

if __name__ == '__main__':
    print("Starting train...")
    start_train()
    
    print("Starting api...")
    start_api()
    
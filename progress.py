from time import sleep
from tqdm import tqdm

def progress(mins):
    seconds = mins * 60
    for i in tqdm(range(seconds)):
        sleep(1)


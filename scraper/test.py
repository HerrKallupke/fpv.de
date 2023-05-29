from datetime import datetime
import time

start = datetime.now()

time.sleep(2)

print(f'{datetime.now() - start}ms')
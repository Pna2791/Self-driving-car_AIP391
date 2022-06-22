import time



list_images = []


count  = 0
t_end = time.time() + 10

while(t_end > time.time()):
    model.predict()
    count += 1
print(count)

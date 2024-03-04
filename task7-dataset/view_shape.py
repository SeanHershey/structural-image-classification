import numpy as np
import imageio

data = np.load('task7_X_train.npy')
y = np.load('task7_y_train.npy')

#print(data.shape, y.shape)

undamaged = 0
minor = 0
damaged = 0
extreme = 0

count = 0

for item in y:
    if (item[0] == 1):
        extreme += 1
    if (item[1] == 1):
        damaged += 1
    if (item[2] == 1):
        minor += 1
    if (item[3] == 1):
        undamaged += 1
    count += 1


print(undamaged)
print(minor)
print(damaged)
print(extreme)


for i in range(len(data)):
    if i < 20:
        fname = './test-images/%s/%05d_p%s.bmp' % ("extreme",i, y[i])
        imageio.imsave(fname, data[i].astype(np.uint8))
    
    if i > 919 and i < 939:
        fname = './test-images/%s/%05d_p%s.bmp' % ("damage",i, y[i])
        imageio.imsave(fname, data[i].astype(np.uint8))
    
    if i > 1788 and i < 1808:
        fname = './test-images/%s/%05d_p%s.bmp' % ("minor",i, y[i])
        imageio.imsave(fname, data[i].astype(np.uint8))
    
    if i > 2587 and i < 2607:
        fname = './test-images/%s/%05d_p%s.bmp' % ("no damage",i, y[i])
        imageio.imsave(fname, data[i].astype(np.uint8))

        # im = Image.fromarray((data[i]).astype(np.uint8))
        # im.save(fname)

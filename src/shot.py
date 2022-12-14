import os
import numpy as np
import matplotlib.pyplot as plt
from .pupil import Pupil
from .sky import Sky
import json
import imageio

# ____________________________________________________________________________________________________
# Shot object ๐ธ

class Shot:
    def __init__(self, sky:Sky, pupil:Pupil):
        self.sky = sky
        self.pupil = pupil
        self.picture = generate(sky, pupil)

    def _imshow(self):
        plt.figure(figsize=(10,10))
        plt.imshow(self.picture, cmap='gray')
        plt.title("Sky")
        plt.colorbar()

    def show(self):
        self._imshow()
        plt.show()

    def save(self, path):
        self._imshow()
        if not os.path.isdir(dir := os.path.split(path)[0]):
            os.makedirs(dir)
        plt.savefig(path + ".png")
        self.sky.save_stars(path)
    
    def save_ai_ready(self, path):
<<<<<<< HEAD
        imageio.imwrite(path+".jpg", self.picture.astype(np.uint8))
        # np.savez_compressed(path, picture=self.picture)
=======
        np.savez_compressed(path, picture=self.picture)
>>>>>>> c2b87e0c12f0864061ca4daa02ace67056400dee
        self.sky.save_stars_ai_ready(path)

# ______________________________________________________________________________________________________________
# Generating shot ๐ธ

def generate(sky:Sky, pupil:Pupil) -> np.ndarray:
    """
    Generate a shot from a sky and a pupil.
    """
    if sky.N != pupil.N:
        raise ValueError("Sky and pupil must have the same size.")
    N = sky.N
    sky_freq = np.roll(np.fft.fft2(sky.picture), (N//2, N//2), (0,1))
    shot_freq = sky_freq * pupil.picture
    shot = abs(np.fft.ifft2(shot_freq))

    return shot

# ______________________________________________________________________________________________________________
# Test zone ๐งช

if __name__ == "__main__":

    # Generating sky ๐
    sky = Sky(512, 1, 1, 0.1, 0.1)

    # Generating pupil ๐ญ
    pupil = Pupil(512, 1, 0.5, 0, 1, 0)

    # Generating shot ๐ธ
    shot = Shot(sky, pupil)

    # Showing shot ๐ผ๏ธ
    shot.show()
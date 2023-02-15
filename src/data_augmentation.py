'''
This file defines the data augmentation methods we will use.
As described in the reference paper, we will apply:
    1. Audio framing.
    In the original paper, they extract 3-sec long sequences of audio from the original files with 50% overlap,
    resulting in an increase from 1_000 samples to 19_000 samples

Additionally, we could perform random data augmentation to simulate noise, compression errors, etc, in order to increase the
robustness of our model. 

However, some typical image augmentation will be irrelevant in our case. For instance, flipping vertically or horizontally
makes no sense, neither does rotating or zooming, etc. Geometrical transformations will probably be irrelevant in general.

Transformations on contrast / brightness of the spectrogram could be relevant though, to increase robustness
towards amplified or deafened audios.
'''
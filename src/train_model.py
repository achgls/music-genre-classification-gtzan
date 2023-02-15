'''
This script receives a compiled model as input, as well as the training and validation data.
It then does the training and stops according to the specified callbacks or number of epochs.

Once it's done, the model and its weights are saved on disk such that it is ready to be loaded and used for inference.
The script should also save the training history and 'TensorBoard' logs, such that its training can be studied and
compared with those of other models.


Ideally, it should also make snapshots of the model during training such that it can be resumed from a
past checkpoint if something bad happens during training.


Default parameters for training used in reference paper:
Batch size = 64
Epochs = 50
Reshuffle at each epoch = True
Optimizer: Adam
'''

def train_model(model, train_data, validation_data):
    ...
    return model

if __name__ == '__main__':
    import sys
    import os

    # Import the data
    ...

    # Train the model
    ...

    # Save model and logs
    ...

    # Print out a summary of the final performance on test set
    # Accuracy, Precision, Recall, F1-scores for each class, confusion matrix...
    # As well as metrics about training / convergence speed (epochs/minute, #epochs needed for the kept version of the model)
    ...
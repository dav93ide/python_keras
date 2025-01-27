from keras.datasets import mnist
from keras.utils import to_categorical
from keras import layers
from keras import models

def main():
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (28, 28, 1) ))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation = 'relu'))

    # L'ultimo tensore 3D di output (di forma (3, 3, 64)) viene passato a una RETE CLASSIFICATORE DENSAMENTE CONNESSA (uno stack di strati Dense).
    # Questa processa vettori 1D, pertanto bisogna prima appiattire il tensore 3D di output a 1D.
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation = 'relu'))
    model.add(layers.Dense(10, activation = 'softmax'))

    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    train_images = train_images.reshape((60000, 28, 28, 1))
    train_images = train_images.astype('float32') / 255
    test_images = test_images.reshape((10000, 28, 28, 1))
    test_images = test_images.astype('float32') / 255
    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)

    model.compile(
        optimizer = 'rmsprop',
        loss = 'categorical_crossentropy',
        metrics = ['accuracy']
    )
    model.fit(
        train_images,
        train_labels,
        epochs = 5,
        batch_size = 64
    )
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print("[+] test_acc = %s" % test_acc)                                       # +- 0.9921


if __name__ == "__main__":
    main()

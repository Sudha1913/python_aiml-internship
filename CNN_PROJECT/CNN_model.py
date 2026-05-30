import tensorflow as tf

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_path = "dataset/train"
test_path = "dataset/test"

train_datagen = ImageDataGenerator(

    rescale=1./255,

    rotation_range=20,

    zoom_range=0.2,

    horizontal_flip=True,

    shear_range=0.2

)

test_datagen = ImageDataGenerator(

    rescale=1./255

)

train_data = train_datagen.flow_from_directory(

    train_path,

    target_size=(224,224),

    batch_size=32,

    class_mode='categorical'

)

test_data = test_datagen.flow_from_directory(

    test_path,

    target_size=(224,224),

    batch_size=32,

    class_mode='categorical'

)

model = Sequential()

model.add(

    Conv2D(

        32,

        (3,3),

        activation='relu',

        input_shape=(224,224,3)

    )

)

model.add(

    MaxPooling2D(pool_size=(2,2))

)

model.add(

    Conv2D(

        64,

        (3,3),

        activation='relu'

    )

)

model.add(

    MaxPooling2D(pool_size=(2,2))

)

model.add(

    Conv2D(

        128,

        (3,3),

        activation='relu'

    )

)

model.add(

    MaxPooling2D(pool_size=(2,2))

)

model.add(

    Flatten()

)

model.add(

    Dense(

        256,

        activation='relu'

    )

)

model.add(

    Dropout(0.5)

)

model.add(

    Dense(

        train_data.num_classes,

        activation='softmax'

    )

)

model.compile(

    optimizer='adam',

    loss='categorical_crossentropy',

    metrics=['accuracy']

)


history = model.fit(

    train_data,

    epochs=20,

    validation_data=test_data

)

loss, accuracy = model.evaluate(test_data)

print("\nTest Accuracy:", accuracy)
model.save("cnn_model.h5")
print("\nModel saved successfully as cnn_model.h5")
print("\nDetected Classes:")
print(train_data.class_indices)


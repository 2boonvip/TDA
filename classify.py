import load_data
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv1D, BatchNormalization, Activation, MaxPool1D, Flatten, Dense, Input,Reshape,MaxPooling1D
from keras.models import Model
from keras.optimizers import Adam
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

X,y = load_data.data()
X = X.reshape(-1,384 , 1)
y = to_categorical(y.reshape(-1, 1))


#正規化
for i in range(len(X)):
    for j in range(len(X[i])):
        if X[i][j] == 0:
            X[i][j] = 1
X = (X - np.amin(X,axis=0)) /( np.amax(X,axis=0))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.276, random_state=0)

def create_single_module(input_tensor, output_channel):
    x = Conv1D(output_channel, kernel_size=3)(input_tensor)
    x = BatchNormalization()(x)
    return Activation("relu")(x)


#モデル作成
input = Input(shape=(384, 1)) # 384dim
x = create_single_module(input, 28) # 30->28 dim
x = MaxPool1D(2)(x) # 28 -> 14dim
x = create_single_module(x, 12) # 14 -> 12
x = create_single_module(x, 10) # 12 -> 10
x = MaxPool1D(2)(x) # 10 -> 5
x = create_single_module(x, 32)
x = Flatten()(x)
x = Dense(7, activation="softmax")(x)

model = Model(input, x)
model.compile(Adam(lr=1e-3), loss="binary_crossentropy", metrics=["acc"])
history = model.fit(X_train, y_train, batch_size=32, epochs=100, validation_data=(X_test, y_test)).history

max_val_acc = max(history["val_acc"])
plt.plot(np.arange(100)+1, history["val_acc"])
plt.ylim((0.8, 1))
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.title(f"EGM in CNN / max val_acc = {max_val_acc:.3}")
plt.show()




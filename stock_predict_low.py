import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dense
from keras.callbacks import ModelCheckpoint
from keras import*
import datetime
from pytz import timezone
import yfinance as yf
import tensorflow as tf
from split.split_data import split_num_data

# get today date
date1 = datetime.datetime.now(timezone('US/Eastern'))
date1 = date1.date()
# get data from yahoo, when stock market end start model
Data = yf.download('AAPL', start=date1)
Data = Data['Low']
Data = Data.values

data = pd.read_csv('/AAPL (4).csv')
# add new data
data = data.drop(0, axis=0)
data = data[::-1]
new_data = pd.DataFrame({'Date': [1], 'Open': [1], 'High': [1], 'Low': [Data], 'Close': [1], 'Adj Close': [1], 'Volume': [1]})
data = pd.concat([data, new_data])
high = data['Low'].values
new = pd.DataFrame({"high": high}).dropna().reset_index(drop=True)
# scaling datas to 1~0
scaler = MinMaxScaler()
scaler.fit(new)
new = scaler.transform(new)

# split data
x_train, y_train, x_val, y_val, x_pre = split_num_data(100, 1, new)  # split data

# save best weight
model_ckpt = ModelCheckpoint('model_ckpt.h5', monitor='val_accuracy', save_best_only=True, mode='auto')  

drop_rate = 0.5
# LSTM
model = Sequential()
model.add(LSTM(100, return_sequences=True, input_shape=(100, 1)))
model.add(tf.keras.layers.Dropout(drop_rate))
model.add(LSTM(1000, return_sequences=False))
model.add(tf.keras.layers.Dropout(drop_rate))
model.add(Dense(1, activation='relu'))
model.compile(loss='mse', optimizer='adam', metrics='accuracy')
model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size=10, epochs=10, callbacks=[model_ckpt])
loss, score = model.evaluate(x_val, y_val)  # save model score with adding metrics='accuracy'

pre = model.predict_classes(x_pre)  # predict
pre = scaler.inverse_transform(pre)  # rescale?
# write score and predict result
f = open("/model_accuracy.txt", "a")
f.write("%d{score=")
f.write(str(score))
f.write(", Low")
f.write(str(pre))
f.write("}\n")
f.close()
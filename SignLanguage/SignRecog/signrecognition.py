def recognize_sign():
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    from keras.models import load_model
    import os
    model = load_model(os.path.join(os.getcwd(), 'sign'))
    import cv2
    alpha_map = {i - 97 : chr(i) for i in range(97, 123)}
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resizedFrame = cv2.resize(grayFrame, (28, 28))
        reshapedFrame = np.reshape(resizedFrame, (28, 28, 1))
        fun = lambda x: x / 255.0
        arr = np.vectorize(fun)
        result = model.predict(np.asarray([arr(reshapedFrame)]))
        index = np.argmax(result)
        letter = alpha_map[index]
        cv2.putText(frame, letter, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow("Live-Feed", frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
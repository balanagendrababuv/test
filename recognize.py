import face_recognition
import joblib
import logging
import cv2
import pickle

logging.basicConfig(filename='recognize1.log',level = logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
logging.basicConfig(filename='recognize_bug.log',level = logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# recognition = pickle.load(open('model.pkl', 'rb'))
recognition = joblib.load('new_face_weights2')

def reg_test(test_image):
    try:
        name = ['No face detected']
        prob = [[0]]
        face_locations = face_recognition.face_locations(test_image)
        no = len(face_locations)
        for i in range(no):
            test_image_enc = face_recognition.face_encodings(test_image)[i]
            name = recognition.predict([test_image_enc])
            prob = recognition.predict_proba([test_image_enc])
        return(name[0],max(prob[0]))
    except Exception as e:
        logging.debug(e)
# img = cv2.imread("train_dir/Arul/arul1.jpg")
# face = face_recognition.load_image_file("train_dir/Arul/arul1.jpg")
# temp = reg_test(face)
# print(temp)





import face_recognition
from sklearn import svm
import os
import joblib
import logging
import pickle
logging.basicConfig(filename='weights.log',level = logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def face_recognize(dir):
    try:
      encodings = []
      names = []


      if dir[-1]!='/':
            dir += '/'
      train_dir = os.listdir(dir)

      for person in train_dir:
            pix = os.listdir(dir + person)

            for person_img in pix:
                        face = face_recognition.load_image_file(
                              dir + person + "/" + person_img)
                        face_bounding_boxes = face_recognition.face_locations(face)

                        if len(face_bounding_boxes) == 1:
                              face_enc = face_recognition.face_encodings(face)[0]
                              encodings.append(face_enc)
                              names.append(person)
                        else:
                              logging.info(person + "/" + person_img + " can't be used for training")
      return encodings,names
      # # Split the data into training and test sets
      # from sklearn.model_selection import train_test_split
      # X_train, X_test, y_train, y_test = train_test_split(encodings, names, test_size=0.2)

      # # Train the SVM model on the training set
      # clf = svm.SVC(gamma='scale', probability=True)
      # clf.fit(X_train, y_train)

      # # Use the trained model to make predictions on the test set
      # y_pred = clf.predict(X_test)

      # # Calculate the accuracy of the model
      # from sklearn.metrics import accuracy_score
      # accuracy = accuracy_score(y_test, y_pred)
      # print('Accuracy:', accuracy)

      # clf = svm.SVC(gamma ='scale',probability=True)
      # clf.fit(encodings, names)
      # # pickle.dump(clf, open('model1.pkl', 'wb'))
      # joblib.dump(clf,'face_weights11')
    except Exception as e:
      logging.info(e)

X_train,y_train = face_recognize(r'C://Users//balan//Downloads//Final Train Images')
X_test,y_test = face_recognize(r'C://Users//balan//Downloads//Final Test Images')
# data,y = face_recognize(r'C://Users//balan//Downloads//')
clf = svm.SVC(gamma='scale', probability=True)
clf.fit(X_train, y_train)
joblib.dump(clf,'new_face_weights2')


y_pred = clf.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
# face_recognize('train_dir')
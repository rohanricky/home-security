import cv2
import face_recognition

rohan_image= face_recognition.load_image_file("rohan.jpg")
rohan_face_encoding = face_recognition.face_encodings(rohan_image)[0]
def face(unknown_image):
#    unknown_image = face_recognition.load_image_file(frame)
    try:
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    except:
        return False
    face_locations = face_recognition.face_locations(unknown_image)
    known_faces = [rohan_face_encoding]
    if len(face_locations) > 0:
        return True

    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(unknown_image, (left, top), (right, bottom), (255, 255, 255), 2)

#    cv2.imshow('image',unknown_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2

img = cv2.imread("PRO-104-Project-Image-main/solar-system.jpg")

cv2.putText(img,
            "sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            ),
cv2.putText(img,
            "mercury",
            (100,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            ),
cv2.putText(img,
            "venus",
            (190,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            ),
cv2.putText(img,
            "earth",
            (290,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            ),
cv2.putText(img,
            "mars",
            (380,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            ),
cv2.putText(img,
            "jupiter",
            (430,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            ),
cv2.putText(img,
            "saturn",
            (750,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            ),
cv2.putText(img,
            "uranus",
            (950,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            ),
cv2.putText(img,
            "neptune",
            (1100,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )



cv2.imshow("output",img)
cv2.waitKey(0)
# Machine Learning: Gesture Recognition

* Cloud Server: Set up a cloud server on Amazon Web Services (AWS) and send continuous accelerometer data of at least 10Hz. Display the data on the cloud through the terminal
* Databases: Created a MongoDB database (with key-value pairs) to be hosted on the AWS server and we will access it using HTTP commands. This database will be used to store accelerometer sensor readings from our smartwatch and was used as our labeled training data
* Supervised Learning: Trained a Random Forest Classifier model (using Scikit-learn) which was capable of recognizing gestures based on accelerometer data from the smartwatch and classifying the letters “C”, “O”, “L”, “U”, “M”, “B”, “I”, “A”
* Visualization: Deployed the model onto the AWS server where it enabled real-time classiﬁcation of the leters. Display the word “COLUMBIA” one letter at a time

> <img src="./media/C.gif" alt="C" width="500"/>\
> <img src="./media/O.gif" alt="O" width="500"/>\
> <img src="./media/L.gif" alt="L" width="500"/>\
> <img src="./media/U.gif" alt="U" width="500"/>\
> <img src="./media/M.gif" alt="M" width="500"/>\
> <img src="./media/B.gif" alt="B" width="500"/>\
> <img src="./media/I.gif" alt="I" width="500"/>\
> <img src="./media/A.gif" alt="A" width="500"/>

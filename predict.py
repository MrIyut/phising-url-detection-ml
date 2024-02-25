#!/usr/bin/python3
from features import having_ip_address, abnormal_url, count_dot, count_www, count_atrate, no_of_dir, no_of_embed, shortening_service, count_http, count_https, count_per, count_ques
from features import count_hyphen, count_equal, url_length, hostname_length, suspicious_words, digit_count, letter_count, fd_length, tld_length, google_index
from tld import get_tld
import numpy as np
import joblib

def init():
    global phishing_ml
    phishing_ml = joblib.load('phishing_ml.pkl')

def getFeatures(url: str):
    features = []
    features.append(having_ip_address(url))
    features.append(abnormal_url(url))
    features.append(count_dot(url))
    features.append(count_www(url))
    features.append(count_atrate(url))
    features.append(no_of_dir(url))
    features.append(no_of_embed(url))
    features.append(shortening_service(url))
    features.append(count_https(url))
    features.append(count_http(url))
    features.append(count_per(url))
    features.append(count_ques(url))
    features.append(count_hyphen(url))
    features.append(count_equal(url))
    features.append(url_length(url))
    features.append(hostname_length(url))
    features.append(suspicious_words(url))
    features.append(fd_length(url))
    features.append(tld_length(get_tld(url,fail_silently=True)))
    features.append(digit_count(url))
    features.append(letter_count(url))
    features.append(google_index(url))

    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    features = np.array(features).reshape((1, -1))
    return features

def predict(url: str):
    features = getFeatures(url)
    prediction = phishing_ml.predict(features)
    return prediction[0]

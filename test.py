#!/usr/bin/python3
from predict import init, predict
init()

urls = ['chaseonlinesecurity.chase.com.jyxhjfygya9girghrx4vy2fn1pgnl46rcus.gshhetrde.for-the.biz/mui/email.php',
        'linkedin.com/pub/dir/+/Avishai',
        'ebay.co.uk.ektabhattacharya.com/ws/eBayISAPI4c5c.html',
        'kansascity.com/2011/11/04/3247343/review-james-galway-brilliant.html',
        'houstonhotels.com/houston/attractions/outdoor-attractions/lillie-and-hugh-roy-cullen-sculpture-garden.html',
        'docstoc.com/docs/2911279/Faculty-University-and-Distinguished-Professors-Bernard-M-Bass-Bartle-Distinguished',
        '14am.net/ad/paypal/',
        'vimeo.com/user5188102/videos',
        'google.com',
        "holtankoljak.hu/logs/",
        "virtualtourist.com/hotels/Caribbean_and_Central_America/Martinique/Fort_de_France-1707435/Hotels_and_Accommodations-Fort_de_France-TG-C-1.html",
        "mixedmartialarts.com/news/359811/Florian-Not-everyone-can-be-a-champion-planning-return-at-lightweight/",
        "en.wikipedia.org/wiki/Office_and_Professional_Employees_International_Union",
        "allstalberthomes.com/",
        "pipl.com/directory/name/Rougeau/Lynn",
        "manta.com/c/mm3z1vh/laurie-a-elliott-md" 
        ]
for url in urls:
    prediction = predict(url)
    if prediction == 0:
        print("benign: " + url + '\n')
    elif prediction == 1:
        print("phishing: " + url + "\n")
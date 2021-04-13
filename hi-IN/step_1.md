## परिचय:

इस प्रोजेक्ट में आप Sense HAT के सेंसरों से डेटा एकत्र करेंगे और उसे एक फाइल में लॉग करेंगे। फिर आप उस डेटा को लाइन ग्राफ के रूप में प्रदर्शित करने के लिए PyGal मॉड्यूल का उपयोग करेंगे।

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/5e246d8212?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark">
</iframe> <img src="images/weather-final.png" />
</div>

### क्लब नेताओं के लिए अतिरिक्त जानकारी

यदि आप इस प्रोजेक्ट को प्रिंट करना चाहते हैं, तो कृपया [प्रिंटर अनुकूल संस्करण](https://projects.raspberrypi.org/hi-IN/projects/weather-logger/print) का उपयोग करें।

--- collapse ---
---
title: क्लब नेता की टिप्पणियाँ
---

## परिचय:

इस परियोजना में, बच्चे सीखेंगे कि Sense HAT के सेंसर से डेटा को किसी फ़ाइल में कैसे सहेजें और फिर डेटा को Pygal के साथ ग्राफ पर प्रदर्शित करें।

## ऑनलाइन संसाधन

**इस प्रोजेक्ट में Python 3 का उपयोग किया जाता है।** Python को ऑनलाइन लिखने के लिए हम [Trinket](https://trinket.io/) का उपयोग करने की सलाह देते हैं। इस परियोजना में निम्नलिखित ट्रिंकेट शामिल हैं:

* ['मौसम लॉग करना' स्टार्टर Trinket -- jumpto.cc/weather-go](http://jumpto.cc/weather-go)

एक ऐसा trinket भी है जिसमें पूर्ण किया गया परियोजना है:

* [‘मौसम लॉग करना’ समाप्त -- trinket.io/python/5e246d8212](https://trinket.io/python/5e246d8212)

## ऑफ़लाइन संसाधन

इस प्रोजेक्ट को Sense HAT से किसी Raspberry Pi कंप्यूटर पर [ऑफ़लाइन भी पूरा किया जा सकता है](https://www.codeclubprojects.org/en-GB/resources/physical-sense-hat/)। आप इस प्रोजेक्ट के लिए 'प्रोजेक्ट सामग्री' लिंक पर क्लिक करके प्रोजेक्ट के संसाधनों पर पहुँच प्राप्त कर सकते हैं। इस लिंक में 'प्रोजेक्ट संसाधन' खंड है, जिसमें ऐसे संसाधन सम्मिलित हैं जिसकी बच्चों को इस प्रोजेक्ट को ऑफ़लाइन पूरा करने की ज़रूरत होगी। सुनिश्चित करें कि प्रत्येक बच्चे को इन संसाधनों की प्रतिलिपि तक पहुँच प्राप्त होती है। इस खंड में निम्नलिखित फाइलें शामिल हैं:

* weather/main.py
* weather/collect.py
* weather/display.py
* weather/weather.txt

आपको 'स्वयंसेवक संसाधन' खंड में इस प्रोजेक्ट का पूर्ण किया गया संस्करण भी मिल सकता है, जिसमें निम्न शामिल हैं:

* weather-finished/main.py
* weather-finished/collect.py
* weather-finished/display.py
* weather-finished/weather.txt

(उपर्युक्त सभी संसाधन प्रोजेक्ट और स्वयंसेवक `.zip` फ़ाइलों के रूप में भी डाउनलोड किए जा सकते हैं।)

## सीखने के उद्देश्य

* भौतिक कंप्यूटिंग - सेंसर;
* डेटा - फाइलों में लिखना और उनसे पढ़ना।

यह प्रोजेक्ट [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum) के निम्नलिखित पहलुओं के तत्वों को पूरा करता है:

* [किसी समस्या को हल करने के लिए प्रोग्रामिंग संरचनाओं को जोड़ें।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ

* मौसम की अलग-अलग स्थितियों का अनुकरण करना - मौसम की अलग-अलग स्थितियों का अनुकरण करने के लिए Sense HAT एमुलेटर का उपयोग करना। 
* रिकॉर्ड या दबाव को रिकॉर्ड करना और प्रदर्शित करना - किसी अलग Sense HAT सेंसर से डेटा रिकॉर्ड करना और परिणामों का ग्राफ बनाना। 

--- /collapse ---

--- collapse ---
---
title: प्रोजेक्ट सामग्री
---

## प्रोजेक्ट संसाधन

* [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/weather-logger-project-resources.zip)
* [Weather Logger' ('वेदर लॉगर') स्टार्टर प्रोजेक्ट](http://jumpto.cc/weather-go)
* [ऑफ़लाइन स्टार्टर Python फ़ाइल](resources/weather-logger-main.py)
* [डेटा एकत्र करने के लिए ऑफ़लाइन Python फ़ाइल](resources/weather-logger-collect.py)
* [डेटा प्रदर्शित करने के लिए ऑफ़लाइन Python फ़ाइल](resources/weather-logger-display.py)
* [ऑफ़लाइन मौसम डेटा फ़ाइल](resources/weather--loggerweather.txt)

## क्लब लीडर संसाधन

* [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/weather-logger-volunteer-resources.zip)
* [ऑनलाइन पूर्ण Trinket Tightrope प्रोजेक्ट](https://trinket.io/python/5e246d8212)
* [ऑफ़लाइन स्टार्टर Python फ़ाइल](resources/weather-logger-finished-main.py)
* [डेटा एकत्र करने के लिए ऑफ़लाइन Python फ़ाइल](resources/weather-logger-finished-collect.py)
* [डेटा प्रदर्शित करने के लिए ऑफ़लाइन Python फ़ाइल](resources/weather-logger-finished-display.py)
* [ऑफ़लाइन मौसम डेटा फ़ाइल](resources/weather-logger-finished-weather.txt)

--- /collapse ---
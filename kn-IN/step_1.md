## ಪರಿಚಯ:

ಈ ಯೋಜನೆಯಲ್ಲಿ ನೀವು Sense HAT ನ ಸಂವೇದಕಗಳಿಂದ ಡೇಟಾವನ್ನು ಸಂಗ್ರಹಿಸಿ ಅದನ್ನು ಫೈಲ್‌ಗೆ ಲಾಗ್ ಮಾಡುತ್ತೀರಿ. ನಂತರ ಆ ಡೇಟಾವನ್ನು ಲೈನ್ ಗ್ರಾಫ್ ಆಗಿ ಪ್ರದರ್ಶಿಸಲು ನೀವು PyGal ಮಾಡ್ಯೂಲ್ ಅನ್ನು ಬಳಸುತ್ತೀರಿ.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/5e246d8212?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark">
</iframe> <img src="images/weather-final.png" />
</div>

### ಕ್ಲಬ್ ಮುಖಂಡರಿಗೆ ಹೆಚ್ಚುವರಿ ಮಾಹಿತಿ

ನೀವು ಈ ಯೋಜನೆಯನ್ನು ಮುದ್ರಿಸಬೇಕಾದರೆ, ದಯವಿಟ್ಟು [ಮುದ್ರಕ-ಸ್ನೇಹಿ ಆವೃತ್ತಿಯನ್ನು ಬಳಸಿ](https://projects.raspberrypi.org/kn-IN/projects/weather-logger/print).

--- collapse ---
---
title: ಕ್ಲಬ್ ನಾಯಕ ಟಿಪ್ಪಣಿಗಳು
---

## ಪರಿಚಯ:

ಈ ಯೋಜನೆಯಲ್ಲಿ, Sense HAT ಸಂವೇದಕಗಳಿಂದ ಡೇಟಾವನ್ನು ಫೈಲ್‌ಗೆ ಹೇಗೆ ಉಳಿಸುವುದು ಎಂದು ಮಕ್ಕಳು ಕಲಿಯುತ್ತಾರೆ ಮತ್ತು ನಂತರ PyGal ಗ್ರಾಫ್‌ನಲ್ಲಿ ಡೇಟಾವನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತಾರೆ.

## ಆನ್‌ಲೈನ್ ಸಂಪನ್ಮೂಲಗಳು

**ಈ ಯೋಜನೆಯು Python 3 ಬಳಸುತ್ತದೆ.** ನೀವು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ Python ಬರೆಯಲು, [Trinket](https://trinket.io/) ಬಳಸಲು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ. ಈ ಯೋಜನೆಯು ಈ ಕೆಳಗಿನ trinket ಅನ್ನು ಒಳಗೊಂಡಿದೆ:

* ['ಹವಾಮಾನದ ಲಾಗರ್' Starter Trinket - jumpto.cc/weather-go](http://jumpto.cc/weather-go)

ಪೂರ್ಣವಾದ ಯೋಜನೆಯನ್ನು ಒಳಗೊಂಡಿರುವ trinket ಸಹ ಇದೆ:

* ['ಹವಾಮಾನದ ಲಾಗರ್' ಮುಗಿದಿದೆ - trinket.io/python/5e246d8212](https://trinket.io/python/5e246d8212)

## ಆಫ್‌ಲೈನ್ ಸಂಪನ್ಮೂಲಗಳು

ಈ ಯೋಜನೆಯನ್ನು Sense HAT ಹೊಂದಿರುವ Raspberry Pi ಕಂಪ್ಯೂಟರ್ ನಲ್ಲಿ [ಆಫ್ ಲೈನ್ ನಲ್ಲಿಯೂ ಪೂರ್ಣಗೊಳಿಸಬಹುದು](https://www.codeclubprojects.org/en-GB/resources/physical-sense-hat/). ಈ ಯೋಜನೆಗಾಗಿ 'ಯೋಜನೆ ವಸ್ತುಗಳು' ಲಿಂಕ್ ಕ್ಲಿಕ್ ಮಾಡುವ ಮೂಲಕ ನೀವು ಪ್ರಾಜೆಕ್ಟ್ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪಡೆಯಬಹುದು. ಈ ಲಿಂಕ್ 'ಯೋಜನೆ ಸಂಪನ್ಮೂಲಗಳ' ವಿಭಾಗವನ್ನು ಒಳಗೊಂಡಿದೆ, ಇದರಲ್ಲಿ ಮಕ್ಕಳು ಈ ಯೋಜನೆಯನ್ನು ಆಫ್‌ಲೈನ್‌ನಲ್ಲಿ ಪೂರ್ಣಗೊಳಿಸಬೇಕಾದ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಒಳಗೊಂಡಿದೆ. ಈ ಸಂಪನ್ಮೂಲಗಳ ತದ್ರೂಪ ವು ಪ್ರತಿ ಮಗುವಿಗೆ ಅನುಮತಿ ಇದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಈ ವಿಭಾಗವು ಈ ಕೆಳಗಿನ ಫೈಲ್‌ಗಳನ್ನು ಒಳಗೊಂಡಿದೆ:

* weather/main.py
* weather/collect.py
* weather/display.py
* weather/weather.txt

ಈ ಯೋಜನೆಯ ಒಂದು ಸಂಪೂರ್ಣ ಆವೃತ್ತಿಯು ಕೂಡ 'ಸ್ವಯಂಸೇವಕ ಸಂಪನ್ಮೂಲಗಳು' ವಿಭಾಗದಲ್ಲಿ ಲಭ್ಯವಿದೆ. ಇದರಲ್ಲಿ:

* weather-finished/main.py
* weather-finished/collect.py
* weather-finished/display.py
* weather-finished/weather.txt

(ಮೇಲಿನ ಎಲ್ಲ ಕಡತಗಳನ್ನು ಪ್ರಾಜೆಕ್ಟ್ ಆಗಿ ಹಾಗೂ ಸ್ವಯಂಸೇವಕ `.zip` ಕಡತಗಳಾಗಿ ಸಹ ಡೌನ್‌ಲೋಡ್ ಮಾಡಬಹುದು.)

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

* ಫಿಸಿಕಲ್ ಕಂಪ್ಯೂಟಿಂಗ್ - ಸಂವೇದಕಗಳು;
* ಡೇಟಾ - ಫೈಲ್‌ಗಳಿಗೆ ಬರೆಯುವುದು ಮತ್ತು ಓದುವುದು.

ಈ ಯೋಜನೆ [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum) ಇದರ ಪಠ್ಯಕ್ರಮವನ್ನು ಅನುಸರಿಸುತ್ತದೆ:

* [ಸಮಸ್ಯೆಯನ್ನು ಪರಿಹರಿಸಲು ಪ್ರೋಗ್ರಾಮಿಂಗ್ ರಚನೆಗಳನ್ನು ಸಂಯೋಜಿಸಿ.](https://www.raspberrypi.org/curriculum/programming/builder)

## ಸವಾಲುಗಳು

* ವಿಭಿನ್ನ ಹವಾಮಾನ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಅನುಕರಿಸಿ - Sense HAT ಎಮ್ಯುಲೇಟರ್ ಬಳಸಿ ವಿಭಿನ್ನ ಹವಾಮಾನ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಅನುಕರಿಸಬಹುದು. 
* ಆರ್ದ್ರತೆ ಅಥವಾ ಒತ್ತಡವನ್ನು ರೆಕಾರ್ಡ್ ಮಾಡಿ ಮತ್ತು ಪ್ರದರ್ಶಿಸಿ - ಬೇರೆ Sense HAT ಸಂವೇದಕದಿಂದ ಡೇಟಾವನ್ನು ರೆಕಾರ್ಡ್ ಮಾಡಿ ಮತ್ತು ಫಲಿತಾಂಶಗಳನ್ನು ಗ್ರಾಫ್ ಮಾಡಿ. 

--- /collapse ---

--- collapse ---
---
title: ಯೋಜನೆಯ ವಸ್ತುಗಳು
---

## ಯೋಜನೆಯ ಸಂಪನ್ಮೂಲಗಳು

* [ಎಲ್ಲಾ ಪ್ರಾಜೆಕ್ಟ್ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಹೊಂದಿರುವ .zip ಫೈಲ್](resources/weather-logger-project-resources.zip)
* [ಹವಾಮಾನದ ಲಾಗರ್ ಸ್ಟಾರ್ಟರ್ ಯೋಜನೆ](http://jumpto.cc/weather-go)
* [ಆಫ್‌ಲೈನ್ ಸ್ಟಾರ್ಟರ್ Python ಫೈಲ್](resources/weather-logger-main.py)
* [ಡೇಟಾವನ್ನು ಸಂಗ್ರಹಿಸಲು ಆಫ್‌ಲೈನ್ Python ಫೈಲ್](resources/weather-logger-collect.py)
* [ಡೇಟಾವನ್ನು ಪ್ರದರ್ಶಿಸಲು ಆಫ್‌ಲೈನ್ Python ಫೈಲ್](resources/weather-logger-display.py)
* [ಆಫ್‌ಲೈನ್ ಹವಾಮಾನ ಡೇಟಾ ಫೈಲ್](resources/weather--loggerweather.txt)

## ಕ್ಲಬ್ ನಾಯಕನ ಸಂಪನ್ಮೂಲಗಳು

* [ಎಲ್ಲಾ ಪ್ರಾಜೆಕ್ಟ್ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಹೊಂದಿರುವ .zip ಫೈಲ್](resources/weather-logger-volunteer-resources.zip)
* [ಆನ್ಲೈನ್ ನಲ್ಲಿ ಸಂಪೂರ್ಣಗೊಂಡಿರುವ trinket Tightrope ಯೋಜನೆಗಳು](https://trinket.io/python/5e246d8212)
* [ಆಫ್‌ಲೈನ್ ಸ್ಟಾರ್ಟರ್ Python ಫೈಲ್](resources/weather-logger-finished-main.py)
* [ಡೇಟಾವನ್ನು ಸಂಗ್ರಹಿಸಲು ಆಫ್‌ಲೈನ್ Python ಫೈಲ್](resources/weather-logger-finished-collect.py)
* [ಡೇಟಾವನ್ನು ಪ್ರದರ್ಶಿಸಲು ಆಫ್‌ಲೈನ್ Python ಫೈಲ್](resources/weather-logger-finished-display.py)
* [ಆಫ್‌ಲೈನ್ ಹವಾಮಾನ ಡೇಟಾ ಫೈಲ್](resources/weather-logger-finished-weather.txt)

--- /collapse ---
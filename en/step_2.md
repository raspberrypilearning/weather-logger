## Logging the temperature

First let's log the temperature to a file every 5 seconds. You can use the emulator to change the temperature. 

+ Open the Weather Logger Starter Trinket: <a href="http://jumpto.cc/weather-go" target="_blank">jumpto.cc/weather-go</a>. 

    __Some files and code have been added for you.__
    
+ Click on `collect.py`. This is where you'll write the code to collect the temperature data. Let's open the `weather.txt` file and write the temperature to it every five seconds.

    Add the highlighted code to `collect.py`:

    ![screenshot](images/weather-collect.png)
    
    Opening the file with `a` means that data will be appended to the end of the file.  
       
    Writing a newline character `\n` puts each temperature reading on its own line. 
    
+ Click on `weather.txt`. It should be empty. This is where the data will be stored. 

    ![screenshot](images/weather-file.png)

+ Now click Run. Use the temperature slider on the emulator to change the temperature. You should see the temperature reading added to the end of `weather.txt` every five seconds. 

    Remember that the emulator tries to behave like a real Sense HAT so you won't see exactly the same reading even if you don't change the emulator. 
    
    ![screenshot](images/weather-temperature.png)

+ Click the square `Stop` button when you have finished collecting data. 

    ![screenshot](images/weather-stop.png)

+ You can highlight the data in `weather.txt` and delete it if you want to start collecting new temperature data. Collect around 10 temperature readings.         
       


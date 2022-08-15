# Task 1. Software configuration
> Because of the war, I ended up in a foreign country without work. I think that this is a *perfect* job that will allow me to work remotely from anywhere in the world. It is a great advantage for me because I have a child (I think people with children understand me 😅). 
>> My goal is a decent salary that will allow me to ___travel😎___ and give a good ___education___ to my son.

### For header
- //*[@id="__next"]/form/div/div[1]/h5
- //*[text()="Scouts Panel"]
- //div/h5
### For login
- //*[@id="login"] 
- (//input[@class="MuiInputBase-input MuiInput-input"])[1]
- //*[@type="text"]
### For password
- //*[@id="password"]
- //*[@type="password"]
- //*[@name="password"]
- (//input[@class="MuiInputBase-input MuiInput-input"])[2]
### For hyperlink
- //*[@id="__next"]/form/div/div[1]/a
- //*[text()="Remind password"]
- //*[contains(@class, "MuiLink-underlineHover")]
### For choosing language
- //*[@id="__next"]/form/div/div[2]/div/input
- //*[@value="en"]
- //*[contains(@class, "nativeInput")]
### For sig in button
- //*[@id="__next"]/form/div/div[2]/button
- //*[@type="submit"]
- //*[@class="MuiButton-label"]
- //*[contains(@class, "MuiButtonBase-root")]
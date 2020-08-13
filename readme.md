Google Chrome offline game (T Rex) bot using Python.

**You need to turn off your internet connection to run this program.**

### How to use

- I prefer using Virtual environment to play with new libraries and packages so that my core packages remain unharmed.
Create and activate virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
- Install necessary packages:
```
pip install -r requirements.txt
```
- Ubuntu users should install `scrot` which is required to run the program:
```
sudo apt-get install scrot
```
If any error occurs add `--fix-missing`:
```
sudo apt-get install scrot -y --fix-missing
```
- Run the program:
```
python t_rex_bot.py
```

#### (Optional)Running Python code using IDLE3 in Virtual Environment

To run IDLE3 while `venv` is activated use the following command. Then browse and open the file using `idle3`.

		(venv)$ python -m idlelib.idle


## References

* [Pyautogui Examples](https://pyautogui.readthedocs.io/en/latest/#examples "Pyautogui Examples")
* [Chapter 18 – Controlling the Keyboard and Mouse with GUI Automation](https://automatetheboringstuff.com/chapter18/ "Chapter 18 – Controlling the Keyboard and Mouse with GUI Automation")

#### Disclaimer: This application is still in development phase.

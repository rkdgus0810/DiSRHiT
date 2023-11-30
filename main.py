import time
import RPi.GPIO as GPIO
import Adafruit_PCA9685

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class Servo_Controller_Class:
    def __init__(self,Channel,ZeroOffset):
        self.mChannel = Channel
        self.m_ZeroOffset = ZeroOffset

        self.mPwm = Adafruit_PCA9685.PCA9685(address = 0x40)
        self.mPwm.set_pwm_freq(60)
    
    def SetPos(self,pos):
        pulse = (650-150)*pos/180+150+self.m_ZeroOffset
        self.mPwm.set_pwm(self.mChannel,0,int(pulse))

    def Cleanup(self):
        self.SetPos(90)
        time.sleep(1)

if __name__ == '__main__':
    Servo = Servo_Controller_Class(Channel = 0, ZeroOffset = -90)

    try:
        Servo.SetPos(0)
        time.sleep(1)
        Servo.SetPos(90)
        time.sleep(1)
        Servo.SetPos(180)
        time.sleep(1)
    except KeyboardInterrupt:
        print("Ctrl + C: "+Colors.BLUE+"KeyboardInterrupt"+Colors.END)
    except Exception as e:
        print(Colors.RED+"Exception error: "+Colors.END+str(e))
    finally:
        Servo.Cleanup()
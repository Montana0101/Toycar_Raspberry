# encoding = 'utf-8'
import RPi.GPIO as GPIO
import time 

IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1,GPIO.OUT)  #设置LED所接针脚模式为OUT（输出）
GPIO.setup(IN2,GPIO.OUT)  
GPIO.setup(IN3,GPIO.OUT)  
GPIO.setup(IN4,GPIO.OUT)  
GPIO.setwarnings(False) #关闭GPIO端口模式改变警告

def up():
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)


def down():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 1)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 1)


def turn_left():
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)


def turn_right():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)
    
def main():
    while True:
        up()
        time.sleep(1)
        
if __name__=='__main__':
    try :
        main()
    except:
        GPIO.cleanup()
        print('关闭程序')
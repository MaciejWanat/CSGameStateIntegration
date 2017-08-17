import json
import requests
import time
from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PA12
led1 = port.PA11
led2 = port.PA18
led3 = port.PA19
led4 = port.PG7

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)
gpio.setcfg(led1, gpio.OUTPUT)
gpio.setcfg(led2, gpio.OUTPUT)
gpio.setcfg(led3, gpio.OUTPUT)
gpio.setcfg(led4, gpio.OUTPUT)

bomb_status = ''
health_status = ''

def zeroData():
    bomb_status = ''
    health_status = ''

def readData(lines):
    bomb_status = lines[0].rstrip('\n')
    health_status = lines[1].rstrip('\n')

def main():

    bomb_time = None
    current_bomb_status = ''
    current_health_status = ''
    #current_health_status_v2 = 0

    print('Reading CS:GO info!')
    while True:
        f = open('game_info', 'r')
        lines = f.readlines()

        if(len(lines) != 0):
            readData(lines)
        else:
            zeroData()
        
        #bomb control - light when bomb is planted
        if bomb_status == 'planted':
            print('Bomb planted!')
            if current_bomb_status != 'planted':
                gpio.output(led4, 1)
                current_bomb_status = 'planted'
                print('Planted!')
            if bomb_time is None:
                bomb_time = time.time()
            total_bomb_time = time.time() - bomb_time
            #print 'Bomb planted for {} seconds'.format(total_bomb_time)    #bomb time output
        elif bomb_status == 'exploded' and current_bomb_status != 'exploded':
            print('Bomb exploded!')
            current_bomb_status = 'exploded'
            gpio.output(led4, 0)
        elif bomb_status == 'defused' and current_bomb_status != 'defused':
            print('Bomb defused!')
            current_bomb_status = 'defused'
            pio.output(led4, 0)
        elif bomb_status == '' and current_bomb_status != '':
            print('No bomb status!')
            current_bomb_status = ''
            bomb_time = None	
            
        #health control v1 - light when >=50             
        if health_status != '':           
            if int(health_status) >= 50 and current_health_status != '>=50':
                print('Health >= 50')
                current_health_status = '>=50'
                gpio.output(led4, 1)
            elif int(health_status) < 50 and current_health_status != '<50':
                print('Health < 50')
                current_health_status = '<50'                
                gpio.output(led4, 0)

        if health_status == '' and current_health_status != '':
            current_health_status = ''
            print('No health info')  
                   
        '''
        #health control v2 - blink when getting hit
        if health_status != '':     
            if int(health_status) > int(current_health_status_v2)
                current_health_status_v2 = int(health_status)       
            elif int(health_status) < int(current_health_status_v2):
                print('Got hit!')
                current_health_status_v2 = int(health_status)
                gpio.output(led4, 1)
                sleep(0.1)
                gpio.output(led4, 0)

        if health_status == '' and current_health_status_v2 != '':
            current_health_status = 0
            print('No health info') 
        '''
        f.close()

if __name__ == "__main__":
    main()

## add the following to sonic pi
##
### Welcome to Sonic Pi v3.0.1
##
##live_loop :listen do
##  set_sched_ahead_time! 0.1
##end
##
##live_loop :listen do
##  note = sync "/osc/play_this"
##  use_synth note[1]
##  play note[0]
##  puts note
##end


# run the folling in the shell
from sense_hat import SenseHat
## from sense_emu import SenseHat
from time import sleep
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient ('127.0.0.1',4559)

sense = SenseHat()
inst = "piano"


while True:
    data = sense.get_orientation()
    pitch = data['pitch']
    yaw = data['yaw']
    roll = data['roll']
    
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.direction == "left":
            inst = "dark_ambience"
        elif event.direction == "up":
            inst = "beep"
        elif event.direction == "right":
            inst = "mod_dsaw"
        elif event.direction == "down":
            inst = "prophet"
    note = (pitch/18)+60
    sender.send_message('/play_this', (note, inst))
    
    sleep(0.1)
    #sense.clear()
 

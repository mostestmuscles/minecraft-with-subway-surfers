import keyboard
import subprocess

# startup
# run this: 
# adb start-server

control_ss = True
SUBWAY_SURFERS_SCENE_AUDIO_ID = 14
SUBWAY_SURFERS_SCENE_ID = 13

SWIPE_POSITIONS = {
    'CENTER': {'x': 450, 'y': 560},
    'LEFT': {'x': 350, 'y': 560},
    'RIGHT': {'x': 550, 'y': 560},
    'TOP': {'x': 450, 'y': 460},
    'BOTTOM': {'x': 450, 'y': 660},
}

def tap_screen(x, y):
    global control_ss
    if not control_ss:
        return
    subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)], shell=True, capture_output=True, text=True)

def double_tap_screen(x, y):
    global control_ss
    if not control_ss:
        return
    tap_screen(x, y)
    tap_screen(x, y)

def restart_game_tap():
    tap_screen(735, 1520)

def hoverboard_tap():
    double_tap_screen(545, 1030)

def swipe_screen_to(position):
    if not control_ss:
        return
    print('swipe')
    command = ['adb', 'shell', 'input', 'swipe', str(SWIPE_POSITIONS['CENTER']['x']), str(SWIPE_POSITIONS['CENTER']['y']), str(SWIPE_POSITIONS[position]['x']), str(SWIPE_POSITIONS[position]['y']), '1']
    res = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(res.stdout)

def swipe_up():
    swipe_screen_to('TOP')

def swipe_down():
    swipe_screen_to('BOTTOM')

def swipe_right():
    swipe_screen_to('RIGHT')

def swipe_left():
    swipe_screen_to('LEFT')

def toggle_control_ss():
    global control_ss
    control_ss = not control_ss

# !!
# Hey you! Edit the keyboard shortcuts here!
# !!
keyboard_to_controller_map = {
    'space': swipe_up,
    'a': swipe_left,
    's': swipe_down,
    'd': swipe_right,
    # 'q': hoverboard_tap,
    '5': restart_game_tap,
    '6': toggle_control_ss,
}

keyboard_controls_dict = {}
for key in keyboard_to_controller_map.keys():
    keyboard_controls_dict[key] = False

def on_key_hooked(event):
    if event.name.lower() not in keyboard_to_controller_map.keys():
        return
    is_keydown = event.event_type == keyboard.KEY_DOWN
    if is_keydown:
        on_key_down(event)
    else:
        on_key_up(event)

def on_key_down(event):
    global keyboard_controls_dict
    key = event.name.lower()
    if keyboard_controls_dict[key]:
        return
    print('key press')
    
    fn_to_run = keyboard_to_controller_map[key]
    fn_to_run()
    keyboard_controls_dict[key] = True

def on_key_up(event):
    global keyboard_controls_dict
    key = event.name.lower()
    
    print('key up')
    keyboard_controls_dict[key] = False

for key in keyboard_to_controller_map.keys():
    keyboard.hook_key(key, on_key_hooked)

try:
    keyboard.wait()
except KeyboardInterrupt:
    keyboard.unhook_all()

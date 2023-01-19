import pynput
import time


def record(path, ignore_keyboard, ignore_mouse, runtime):
    log = open(path, "w")
    start = time.time()

    # Mouse Listeners
    def on_move(x, y):
        log.write(f"m {time.time() - start}: {x} {y}\n")

    def on_click(x, y, button, pressed):
        if pressed:
            log.write(f"cp {time.time() - start}: {x} {y} {button._name_}\n")
        else:
            log.write(f"cr {time.time() - start}: {x} {y} {button._name_}\n")

    def on_scroll(x, y, dx, dy):
        if dy != 0:
            log.write(f"sv {time.time() - start}: {x} {y} {dy}\n")
        if dx != 0:
            log.write(f"sh {time.time() - start}: {x} {y} {dx}\n")

    # Keyboard Listeners
    def on_press(key):
        log.write(f"kp {time.time() - start}: {key._name_ if isinstance(key, pynput.keyboard.Key) else key.char}\n")

    def on_release(key):
        log.write(f"kr {time.time() - start}: {key._name_ if isinstance(key, pynput.keyboard.Key) else key.char}\n")

    if not ignore_mouse:
        mlistener = pynput.mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
        mlistener.daemon = True
        mlistener.start()
    if not ignore_keyboard:
        klistener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
        klistener.daemon = True
        klistener.start()

    print(f"Recording for {runtime} seconds...")

    time.sleep(runtime)

    log.close()

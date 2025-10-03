from machine import Pin
import time, sys
from hx711 import HX711

DT_PIN = 5    # GP5
SCK_PIN = 6   # GP6
REFERENCE_UNIT = 114

BTN_PIN = 16        # <-- button GPIO in RP2040
DEBOUNCE_MS = 40	# Set Avg Perid

_capture_requested = False
_last_irq_ms = 0

def _button_irq(pin):
    # Debounced falling-edge press (active-low)
    global _capture_requested, _last_irq_ms
    now = time.ticks_ms()
    if time.ticks_diff(now, _last_irq_ms) > DEBOUNCE_MS:
        _capture_requested = True
        _last_irq_ms = now

def clean_and_exit():
    print("Cleaning up...")
    print("Bye!")
    sys.exit()

def snapshot_weight(hx, n=10, inter_ms=5):
    """
    Take a short burst of readings and return a trimmed mean
    (reject 1 min and 1 max if possible) for robustness.
    """
    vals = []
    for _ in range(n):
        vals.append(hx.get_weight(1))   # 1 sample per call
        time.sleep_ms(inter_ms)

    vals.sort()
    if len(vals) >= 5:
        vals = vals[1:-1]  # drop one low and one high outlier
    return sum(vals) / len(vals)

def main():
    hx = HX711(dout=DT_PIN, pd_sck=SCK_PIN, gain=128)
    time.sleep_ms(200)

    print("Taring... remove any load.")
    hx.tare()
    print("Tare done! Add weight now...")

    hx.set_reference_unit(REFERENCE_UNIT)

    # Button: pull-up, active-low, IRQ on falling edge
    btn = Pin(BTN_PIN, Pin.IN, Pin.PULL_UP)

    btn.irq(trigger=Pin.IRQ_FALLING, handler=_button_irq)

    # Optional: continuous live read for monitoring
    print("Reading... press the button to CAPTURE a snapshot.\n")
    
    try:
        while True:
            # Lightweight continuous reading (optional)
            live = hx.get_weight(3)
            #print("live:", live)

            # If a press was detected, take a robust snapshot
            global _capture_requested
            if _capture_requested:
                print('captured')
                print('live')
                _capture_requested = False
                snap = snapshot_weight(hx, n=12, inter_ms=4)
                print(">>> CAPTURED:", snap)

            # Keep HX711 powered to be responsive
            # (You can still power-cycle if you want lower noise/consumption)
            time.sleep(0.05)

    except KeyboardInterrupt:
        clean_and_exit()

if __name__ == "__main__":
    main()

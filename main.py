from machine import Pin
import time, sys
from hx711 import HX711

DT_PIN = 5   # GP5
SCK_PIN = 6  # GP6
REFERENCE_UNIT = 114

def clean_and_exit():
    print("Cleaning up...")
    print("Bye!")
    sys.exit()

def main():
    # Pass pin numbers; driver internally constructs Pin(...)
    hx = HX711(dout=DT_PIN, pd_sck=SCK_PIN, gain=128)

    time.sleep_ms(200)

    print("Taring... remove any load.")
    hx.tare()
    print("Tare done! Add weight now...")

    hx.set_reference_unit(REFERENCE_UNIT)
    # Optional: hx.set_reading_format("MSB", "MSB")  # defaults are usually fine

    while True:
        try:
            val = hx.get_weight(5)
            print(val)

            # Power-cycling each read isn't required; you can just read again.
            # If you want to keep it:
            hx.power_down()
            time.sleep_ms(1)
            hx.power_up()
            time.sleep(0.1)

        except KeyboardInterrupt:
            clean_and_exit()

if __name__ == "__main__":
    main()

import serial
import csv
import time

# Establish serial communication with Arduino


arduino_port = '/dev/cu.usbserial-0001'  
baud_rate = 115200
output_file = 'serial_data.csv'

try:
    # Open the serial port
  	# Set a timeout to prevent the program from hanging indefinitely
    ser = serial.Serial(arduino_port, baud_rate, timeout=1) 
    time.sleep(2) # Allow time for the serial port to open and the Arduino to reset
    print(f"Connected to {ser.port}")
    with open(output_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        while True:
            # Read a line of data
            line = ser.readline()
            if line:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([timestamp, line])
                # Decode the bytes to a string and strip whitespace/newlines
                file.flush()
                decoded_line = line.decode('utf-8').strip()
                print(f"Received: {line.strip()}")

except serial.SerialException as e:
    print(f"Serial error: {e}") # Handles errors like 'port not found' or 'port in use'
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")


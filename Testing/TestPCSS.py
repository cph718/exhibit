#Code to test Servo can be controlled

#import serial
import time
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
)

def run_sync_simple_client():
    client = ModbusClient.ModbusSerialClient(port='/dev/ttyUSB0', framer=Framer.ASCII, baudrate=19200, bytesize=7, parity="N", stopbits=2)

    print("connect to server")
    client.connect()

    print("get and verify data")
    try:
        #rr = client.read_holding_registers(0x0fa0, 2, slave=1)
        #rr = client.read_holding_registers(1, 1, slave=1)
        rr = client.read_coils(1, 1, slave=1)
    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
        client.close()
        return
    if rr.isError():
        print(f"Received Modbus library error({rr})")
        client.close()
        return
    if isinstance(rr, ExceptionResponse):
        print(f"Received Modbus library exception ({rr})")
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        client.close()

    #client.write_register(0x0003, 0x0, slave=1) # Set to PR Mode

    rr = client.read_holding_registers(0x0fa0, 0x0002, slave=1)
    print(rr.registers)

    print("close connection")
    client.close()

if __name__ == "__main__":
    run_sync_simple_client()
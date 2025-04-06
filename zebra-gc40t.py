import os
import usb.core
import usb.util
import usb.backend.libusb1

# Author: Pratomrerk B.
# Update: 2025-04-07
# Print to Zebra GC420t with USB (low-level)

# Driver: https://www.zebra.com/ap/en/support-downloads/printers/desktop/gc420t.html
# Utilities: https://www.zebra.com/us/en/support-downloads/software/printer-software/printer-setup-utilities.html

def check_backend_usblib():
    if usb.backend.libusb1.get_backend() is None:
        return False
    else:
        return True 

def get_usb_port(id_vendor, id_product):
    print(f'[+] Find Vendor ID: {id_vendor}, Product ID: {id_product}')
    dev = usb.core.find(idVendor=id_vendor, idProduct=id_product)
    if dev is None:
        raise ValueError('Device not found')
    print('[+] Set the active configuration')
    dev.set_configuration()
    cfg = dev.get_active_configuration()
    intf = cfg[(0, 0)]
    ep_out = usb.util.find_descriptor(intf, custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)
    return ep_out

def set_to_zpl_mode():
    return '! U1 setvar "device.languages" "zpl"'


if __name__ == '__main__':

    if check_backend_usblib() == False:
        print(f'[+] Install libusb')
        print('    1. xcopy libusb-1.0.dll C:\\Windows\\System32')
        print('    2. Open Zadig')
        print('    3. Options -> List All Devices and select Zebra GC420t')
        print('    4. Change USB Printing Support to libusbK (or libusb-win32)')
        print('    5. Click Replace Driver')
        os.exit()

    # Get hardware id Zebra GC420t
    # 1. Open Device Manager
    # 2. Select libusbK devices -> ZTC GC420t
    # 3. Properties -> Details -> Property -> Hardware id 
    # 4. Value in items 2
    # Ex.: USB\VID_0A5F&PID_00D3\54XXXXXXXXXX
    VID = 0x0A5F
    PID = 0x00D3
    usb = get_usb_port(VID, PID)

    # Sent to USB endpoint
    # zpl design: https://labelary.com/viewer.html
    zpl = b"""
    ^XA
    ^FO50,50^ADN,36,20^FDHello from USB!^FS
    ^XZ
    """
    usb.write(zpl)
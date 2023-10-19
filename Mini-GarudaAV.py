import asyncio

from aioclamd import ClamdAsyncClient

print("--------------------------------------------------------------\n")

devby= "PT Media Pengembangan Teknologi Indonesia Jaya\n"
author= "Author: Ananda Rauf Maududi\n"
devdate= "09 September 2023\n"
nameprogram= "Mini Garuda Antivirus\n"

print(devby)
print(author)
print(devdate)
print(nameprogram)
print("--------------------------------------------------------------\n")

class MenuMiniGarudaAV():
    def menu():
        print("Menu Mini Garuda Antivirus:\n")
        print
        print("1.Scan Virus")
        print("2.Exit")

class ScanVir():
    def scanvir(self):

        # scan file by path folder
        # scan file by name file
        async def main(host, port):
            clamd = ClamdAsyncClient(host, port)
            print(await clamd.scan('/etc/clamav/clamd.conf'))
            asyncio.run(main("127.0.0.1", 3310))
       
       


MenuMiniGarudaAV.menu()

choosemenu = int(input("Please choose number on menu:"))

ScanVirs = ScanVir()

if choosemenu== 1:
    ScanVirs.scanvir()

elif choosemenu== 2:
    print("Thanks for using ^-^\n")
    print("Dont forget share and give star ^-^")
    exit

else:
    print("Not found, sorry!")
    print("Please try again!")

MenuMiniGarudaAV.menu()

choosemenu = int(input("Please choose number on menu:"))

 

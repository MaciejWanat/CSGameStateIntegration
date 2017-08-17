# CSGameStateIntegration
Server application writing out Game State Integration info from CS:GO using [CSGSI](https://github.com/rakijah/CSGSI).

It's a classic .NET Console Application.

Project also contains client written in Python, which is an application that interprets info from server and cotrols LEDs on Orange Pi.

The idea is that server runs on Windows machine, where it can read information from ingame state integration, and then saves it to the file.
Client is running on Orange Pi and has no access to game running on Windows, but it reads from file created by Server.
File created by server must be accesable for both Windows and Orange Pi machine. 

If you want to try it, the best way is to create shared folder and run .exe server file on Windows machine and then run Python client file on Orange Pi.

Dont forget about the proper configuration of CS itself - you can find example on the bottom of [CSGSI page](https://github.com/rakijah/CSGSI).
# VBS-Stager

This Python script generates a Visual Basic Script (VBS) stager that reads and executes a PowerShell script from a given URL.
It also provides an option to add persistence to the generated stager.

## Features

- Generates a VBS stager to reads and execute a PowerShell script from URL.
- Optional persistence feature to automatically run the stager on system startup.
- Colorized terminal output for a better user experience.

## Requirements

- Python 3.x
- `pyfiglet` library
- `colorama` library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/malwarekid/VBS-Stager.git
    ```

2. Install the required libraries:

    ```bash
    pip3 install pyfiglet colorama
    ```

## Usage

1. Run the script:

    ```bash
    python3 VBS-Stager.py
    ```
```
python3 VBS-Stager.py

 _    ______ _____      _____ __                       
| |  / / __ ) ___/     / ___// /_____ _____ ____  _____
| | / / __  \__ \______\__ \/ __/ __ `/ __ `/ _ \/ ___/
| |/ / /_/ /__/ /_____/__/ / /_/ /_/ / /_/ /  __/ /    
|___/_____/____/     /____/\__/\__,_/\__, /\___/_/     
                                    /____/             
                                        By @malwarekid

Enter the URL of the PowerShell script: https://raw.githubusercontent.com/malwarekid/GoodUSB/master/msg.ps1
Enter the output file name (default: stager.vbs): 
Do you want to add persistence to the stager? (yes/no, default: no): yes
Stager script saved to stager.vbs
```

2. Enter the URL of the PowerShell script when prompted.

3. Optionally, specify the output file name. If not specified, the default name is `stager.vbs`.

4. Choose whether to add persistence to the stager. Enter `yes` or `no`. The default is `no`.

5. The generated stager script will be saved to the specified output file.

## Author

[Malwarekid](https://github.com/malwarekid)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Notes

Feel free to contribute, report issues, or provide feedback and dont forget to follow me on [Instagram](https://www.instagram.com/malwarekid/) and [github](https://github.com/malwarekid/) Happy Hacking!

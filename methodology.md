
## Method and Implementation /Deployment:

Our project utilizes the [ProVerif manual](https://bblanche.gitlabpages.inria.fr/proverif/manual.pdf) to download the application and then execute it on command line. We test the control query given in the manual to see how the application works and its response to the query (hello.pv, hello.ext), in these initial runs we test whether the Cocks and RSA bitstrings can be intercepted by the attacker.
![]

### Deployment
**Install homebrew on macbook**
To install Homebrew on your MacBook Air, you can follow these steps:

1. Open the Terminal application on your MacBook Air. You can find it by going to Launchpad or using the Spotlight search (press Command + Space and type "Terminal").

2. In the Terminal, paste the following command and press Enter:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

3. This command will download and run the Homebrew installation script. You may be prompted to enter your administrator password. Type your password carefully (it won't be visible) and press Enter.

4. The installation process may take a few minutes. It will display the progress and complete the installation.

5. Once the installation is finished, you can test Homebrew by running the following command in the Terminal:

```bash
brew --version
```

If Homebrew is installed correctly, it will display the version number.

That's it! You have successfully installed Homebrew on your MacBook Air. You can now use it to install various software packages and utilities through the Terminal.

To download and install ProVerif on MacBook Air, follow these steps:

1. Open a web browser and go to the ProVerif website: https://www.proverif.inria.fr/.
2. On the website, navigate to the "Download" section.
3. Click on the appropriate download link based on your operating system (in this case, macOS).
4. Save the downloaded file to a location on your MacBook Air.

Now, to install ProVerif:

1. Locate the downloaded file (usually in the "Downloads" folder).
2. Double-click the downloaded file to open it. This will typically extract the ProVerif installation files.
3. Open the Terminal application. You can find it by pressing Command + Spacebar, typing "Terminal," and pressing Enter.
4. In the Terminal, navigate to the directory where the ProVerif installation files are extracted. For example, if the files are in the "Downloads" folder, type:
   ```
   cd ~/Downloads
   ```
5. Use the following command to make the ProVerif executable:
   ```
   chmod +x proverif
   ```
6. Finally, run the installation by executing the following command:
   ```
   ./proverif
   ```
   This will start the ProVerif installation process.

Follow the on-screen instructions to complete the installation. Once installed, you can run ProVerif by typing `proverif` in the Terminal.

Note: Make sure your MacBook Air has the required software dependencies installed, such as OCaml and opam, before installing ProVerif. You may need to follow additional steps to install these dependencies. Refer to the ProVerif documentation for more details.
## Installing on VS code
1. Install Visual Studio Code: If you haven't already, download and install Visual Studio Code from the [official website](https://code.visualstudio.com/).

2. Open Visual Studio Code: Launch Visual Studio Code on your computer.

3. Install the ProVerif extension: In Visual Studio Code, click on the Extensions icon on the left sidebar (or press `Ctrl+Shift+X`). Search for "ProVerif" in the Extensions Marketplace. Click on the "ProVerif" extension by "ProVerif Team" and click the "Install" button.

4. Configure ProVerif: Once the extension is installed, you may need to configure the ProVerif executable path. Go to File > Preferences > Settings (or press `Ctrl+,`) to open the settings. Search for "ProVerif" in the search bar. Look for the setting "Proverif: Executable Path" and provide the path to the ProVerif executable file on your system.

5. Open a ProVerif file: Create or open a ProVerif file with the `.pv` extension in Visual Studio Code. The ProVerif extension should automatically recognize the file and provide syntax highlighting and other features.

6. Run ProVerif: To run ProVerif on your ProVerif file, you can use the command palette (press `Ctrl+Shift+P`) and search for "ProVerif: Run". Alternatively, you can right-click on the file and select "Run ProVerif" from the context menu.

### Running proverif
In terminal type: 
```
   ./proverif <filename.pv>
   ```
# Cryptography: Modelling And Verifying Key Exchange Using ProVerif
## Introduction:

Cryptography is a field that focuses on communication security which allows senders and recipients to transmit information without interference from adverse third parties. This study employs protocols of data encryption, whereby messages are converted into secret code (ciphertext), and decryption, in which the recipient decodes the message. 
Data encryptions ensure that information (data-at-rest or data-in-transit) remains undiscovered from unauthorised persons(attackers) and thus secure message transit between client and server or two parties is maintained.

In order for two parties to interact, there needs to be key exchange which allows the client and server to communicate over a secure channel so that attackers cannot create a copy. This exchange typically requires the use of a single key shared between the participants for encryption and decryption, hence known as symmetric key cryptography.

This event poses a problem because both the client and the server need a secret key that is recognisable to both parties to communicate through channels. If these individuals cannot establish an initial secret key, that is, the first key exchange, it will be impossible to generate a secure communication channel against third parties.

Cryptographic protocols are everywhere and are working behind the scenes to the form foundation of all internet communication including banking, e-commerce and even social media. We have been designing these protocols for decades in order to make them as robust as possible but there are still several cyber-attacks on these protocols. The question now is how can we create protocols which are robust against different types of attacks- this is the main evaluation point of this thesis.
In order to explore this further, we are going to use a tool called ProVerif which uses the symbolic model (otherwise known as the Dolev-Yao model) of cryptographic protocols in order to analyse them. The key features of ProVerif are that it is able to handle multiple cryptographic primitives which includes shared-key and public-key cryptography as well as Diffie-Hellman key exchanges (which will be discussed further in this thesis). The security of cryptographic protocols is automatically analysed by this tool developed by Bruno Blanchet. Many well-known cryptographic case studies have utilised ProVerif to analyse the security of these protocols. Most notably, Kusters and Trufderung have examined the security of the Diffie-Hellman protocol using ProVerif and this protocol which is the main focus of this thesis. 
To prevent the possibility of attackers, Public-key/ Asymmetric cryptography is used- a dual-key exchange system implementing a private key used by owner to decrypt messages and public key is used to encrypt the message. The public key can also be used across insecure channels (it still does not pose any security risk against the secret message). This is known as the Diffie-Hellman (DH) Key exchange protocol. It allows the two parties to interact over public channels to establish a “handshake” and share secret without interference whilst using a public key to encrypt or decrypt their messages which are secured by private keys. Thus, the DH protocol implements both symmetric and asymmetric key exchange methods- using public keys for a secure message within a chosen open channel and using the private key to demand for authentication.

The reliance on the symbolic model of cryptography otherwise known as the Dolev-Yao model is key to the function of ProVerif. Although assessing a protocols level of security is easier and more accessible to all users using a Dolev-Yao model, it does pose some limitations where it does not accurately represent the actual cryptography of the real world as it misses a lot of detail and possibilities. This is opposed to using the computational model of cryptographic primitives which is utilised by tool such as CryptoVerif which takes into account a more detailed analysis of these protocols. It is for this reason why ProVerif loses some accuracy within its results.
Within this tool, cryptographic primitives are treated as black boxes in the sense that these algorithms programmed for security are perfect and no adversary can break them individually in themselves. And for this example we disregard the actual algorithms they represent and how they are implemented; the main focus here is on how these cryptographic primitives interact with each other and the users (protocols)

Therefore, when analysing attacks on cryptographic protocols we consider the Dolev-Yao attacker which is a powerful attacker, this attacker can capture everything communicated between two parties (the sender and receiver) by recording, replying and modifying the messages sent between the two parties; the attacker cannot however break the underlying cryptographic primitives (which are essentially used to conceal the messages, parallel to encryption).


## AUTOMATED REASONING: PROVERIF

Automated reasoning is a field of computer science that deals with use of applying logical inference to a set of assumption in order to achieve automacy in computer systems. ProVerif is an exemplary tool used in cryptography which uses automated reasoning (based on the Dolev-Yao adversary model) to estimate and define the security properties of encrypted data as well as verify privacy.

## Method and Implementation /Deployment:

Our project utilizes the [ProVerif manual](https://bblanche.gitlabpages.inria.fr/proverif/manual.pdf) to download the application and then execute it on command line. We test the control query given in the manual to see how the application work and its response to the query (hello.pv, hello.ext), in these initial runs we test whether the Cocks and RSA bitstrings can be intercepted by the attacker.

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
##



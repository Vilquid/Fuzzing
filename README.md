# English
We first create a list of A going from 20 to 20 which will be used as an argument later.

We put these arguments behind 3 commands which admit MKD, CWD, STOR arguments. Now we need to send these commands. So we create a socket and we connect to the server. We must then identify ourselves. We of course have restricted access on the server, the login being ftp and the password ftp.

We will therefore send USER ftp then PASS ftp and then continue with the rest of the commands with our arguments. Then, we close the socket.

<strong>EIP</strong>

Here is a python program that will send unique arguments to know exactly the number of bytes needed to overwrite EIP.

# Français

Nous créons tout d'abord une liste de A allant de 20 en 20 ce qui va nous servir d'argument par la suite.

Nous mettons ces arguments derrière 3 commandes qui admettent des arguments MKD, CWD, STOR. Il nous faut maintenant envoyer ces commandes. Nous créons donc un socket et nous nous connectons sur le serveur. Il nous faut alors nous identifier. Nous avons bien sûr un accès restreint sur serveur, le login étant ftp et le mot de passe ftp.

Nous enverrons donc USER ftp puis PASS ftp pour ensuite continuer avec le reste des commandes avec nos arguments. Nous fermons ensuite le socket.

<strong>EIP</strong>

Voici un programme python qui va envoyer des arguments uniques pour connaître exactement le nombre d'octets nécessaires pour écraser EIP.

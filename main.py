#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
from datetime import datetime
from Message import Message
from Client import Client

#Pages web

login_html = """
<html>
    <head>
    	<title></title>
    	<meta charset="utf-8" />
    	<style>
    		body {
    			background-attachment: fixed;
    			background-repeat: no-repeat;
    			background-size: 100%;

    		}

    		#ban-title {
    			color: turquoise;
    			text-align: center;
    			position: relative;
    			top: 5%;
    			font-size: 80px;
    			background-color: purple;
				border-radius: 20px;
    		}

    		#form {
    			color: turquoise;
    			font-size: large;
    			text-align: center;
    			position: relative;
    			top: 20%;
    			border: 1px;
    			padding-top: 70px;
    			padding-bottom: 60px;
    			background-color: gray;
				border-radius: 20px;
    		}

    		form {
    			display: flex;
    			flex-direction: column;
    			justify-content: center;
    			align-items: center;
    			padding: 0;
    			margin: auto;
    			width: 400px;
    		}

    		.row p {
    			text-align: left;
    			width: 100%;
    			padding: 0;
    		}

    		#conn{
    			background-color: lime;
    			color: rebeccapurple;
    			border: none;
    		}

    		.row {
    			width: 100%;
    			justify-content: space-between;
    			display: flex;
    		}

    		input {
    			height: 30px;
    			border-radius: 0rem;
    			padding: auto;
    			cursor: pointer;
    			font-size: 0.8rem;
    			font-weight: 700;
    		}

    		input[type="submit"]{
    				height: 30px;
    				border-radius: 0rem;
    				background-color: blue;
    				color: white;
    				font-size: 1.3rem;
    				font-weight: 700;
    		}
    	</style>
    </head>

    <body>

    	<div id="ban-title">Chat-Room</div>

    	<div id="form">
    		<form method="POST" action="" >

    			<div class="row">
    				<p><label for="name"><b>Nom:</b></label></p>
    				<p><input type="text" name="name" id="name" /></p>
    			</div>

    			<div class="row">
    				<p><label for="password"><b>Mot De Passe:</b></label></p>
    				<p><input type="password" name="password" id="password" /></p>
    			</div>

    			<p><input type="submit" name="submitl" value="Connexion" /></p>
    
    			<p><b>Vous n'avez pas de compte ?</b> <input id="conn" type="submit" name="inscription" value="Inscription" /></p>

    		</form>
    	</div>

    </body>
<html>

"""

signup_html = """
<html>
	<head>
		<title></title>
		<meta charset="utf-8" />

		<style>
			body {
				background-attachment: fixed;
				background-repeat: no-repeat;
				background-size: 100%;
			}

			#ban-title {
				color: turquoise;
				text-align: center;
				position: relative;
				top: 5%;
				font-size: 80px;
				background-color: purple;
				border-radius: 10px;
			}

			#form {
				color:turquoise;
				font-size: large;
				text-align: center;
				position: relative;
				top: 20%;
				border: 1px;
				padding-top: 70px;
				padding-bottom: 60px;
				background-color: gray;
				border-radius: 20px;
			}

			form {
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;
				padding: 0;
				margin: auto;
				width: 400px;
			}

			#conn{
				background-color: lime;
    			color: rebeccapurple;
				border: none;
			}

			.row p {
				text-align: left;
				width: 100%;
				padding: 0;
			}

			.row {
				width: 100%;
				justify-content: space-between;
				display: flex;
			}

			input {
				height: 30px;
				border-radius: 0.2rem;
				padding: auto;
				cursor: pointer;
				font-size: 0.8rem;
				font-weight: 700;
			}

			input[type="submit"]{
					height: 30px;
					border-radius: 0rem;
    				        background-color: blue;
					color: white;
					font-size: 1.3rem;
					font-weight: 700;
			}
		</style>
	</head>
	
	<body>

	<div id="ban-title">Chat-Room</div>

	<div id="form">
		<form method="POST" action="">

			<div class="row">
				<p><label for="name"><b>Nom:</b></label></p>
				<p><input type="text" name="name" id="name" /></p>
			</div>

			<div class="row">
				<p><label for="password"><b>Mot De Passe:</b></label></p>
				<p><input type="password" name="password" id="password" /></p>
			</div>

			<div class="row">
				<p><label for="confirm_password"><b>Confirmez Mot De Passe:</b></label></p>
				<p><input type="password" name="confirm_password" id="confirm_password" /></p>
			</div>

			<p><input type="submit" name="submits" value="Inscription" /></p>
			
			<div id="lien-inscript"><b>Vous avez deja un compte ?</b> <input id="conn" type="submit" name="connexion" value="Connexion" /></div>
		</form>
		
	</div>

	</body>
<html>

"""

chatroom_debut = """
<html>
	<head>
		<title></title>
		<meta charset="utf-8"/>
		<style>
			
			body{
				background-image: url("live-chat.jpg");
				background-attachment:fixed;
				background-repeat:no-repeat;
				background-size:100%;
			}
			
			#ban-title{
				color: turquoise;
				text-align:center;
				position:relative;
				top:5%;
				font-size:80px;
				background-color: purple;
				border-radius: 10px;
			}

			#root {
			color: magenta;
			font-size: large;
			text-align: center;
			position: relative;
			top: 20%;
			border: 1px;
			padding-top: 70px;
			padding-bottom: 30px;
			background-color: lawngreen;
			border-radius: 15px;
			}

			.msg{
				text-align: left;
				padding : 0.1rem;
				margin: auto;
				font-size: 1.3rem;
			}

			input[type="submit"]{
				height: 30px;
				border-radius: 0rem;
    			background-color: slateblue;
				color: white;
				font-size: 1.3rem;
				font-weight: 700;
			}

			.message__block{
				background-color: rgba(0,0,0,0.7);
				color: gold;
				font-weight: 700;
				width: 700px;
				margin: auto;
				margin-top: 10px;
				border-radius: 4px;
				border: 1px solid black;
				padding: 5px;
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-text: left;
			}

		</style>
	</head>
	
	<body>
	
		<div id="ban-title">Chat-Room</div>
		
		<div id="root">
"""

chatroom_fin = """
<form method="POST" action="">
				<p class="write">
					<textarea name="message" class="msg" cols="45" rows="3"></textarea>
				</p>
	
				<p><input type="submit" name="send" id="envoyer" value="Poster"/> </p>
			</form>
		</div>
		
	</body>
	
<html>

"""

chatroom = chatroom_debut + chatroom_fin

#La liste des messages en html
message__blocks = []

def message__block(header,body): 
	return  """
<div class="message__block"> """ + header + """ </div>

"""	      	

#Tableaux de sauvegarde de donnees des clients
membres = []

error = ""

client = Client("","")
found = False

class MainHandler(webapp2.RequestHandler):
	
    def get(self):
        #We use """ to display an html doc
        self.response.write(login_html)

    
    def post(self):
		global found
		global client
		global membres
		global message__blocks
		global chatroom
		
		#We get the arguments list
		args = self.request.arguments()

		#Login.html
		if (u'inscription' in args):
			self.response.out.write(signup_html)
		else:

			if (u'submitl' in args):
				
				client = Client( self.request.get("name"), self.request.get("password") )
				found = False

				for membre in membres:
					if( membre.equal(client) ):
						self.response.out.write(chatroom)
						found = True
						
				if (not found):
					error = "Informations de connexion invalides !"
					self.response.out.write( "<center style=\"font-size: 1.4rem; width: auto; color: red; background-color: white;\" >"+ error +"</center>" + " <br><br> " + login_html)						

			else:
				pass
					
		
		#Sign-up.html
		if(u'connexion' in args):
			self.response.out.write(login_html)
		else:

			if (u'submits' in args):
				found = False

				if( self.request.get("password") != self.request.get("confirm_password") ):
					error = "Les mots de passes ne correspondent pas !"
					self.response.out.write( "<center style=\"font-size: 1.4rem; width: auto; color: red; background-color: white;\" >"+ error +"</center>" + " <br><br> " + signup_html)
				else:	
					client = Client( self.request.get("name"), self.request.get("password") )
					
					#On verifie s'il n'est pas deja present
					for membre in membres:
						if( membre.equal(client) ):
							self.response.out.write(chatroom)
							found = True
							pass

					#s'il est present on retourne a la page d'enregistrement		
					if (found):
						error = "Le membre existe deja !"
						self.response.out.write( "<center style=\"font-size: 1.4rem; width: auto; color: red; background-color: white;\" >"+ error +"</center>" + " <br><br> " + signup_html)
					#sinon on l'enregistre et on se rend sur la page de connexion
					else:
						membres.append(client)
						self.response.out.write(login_html)

			else:
				pass
			#We save the user and bring him to the Chat page
			
		#Chat.html
		if((u'send' in args) and (len(self.request.get("message")) > 0) and found ):
			message = Message(client, self.request.get("message"))
			header = message.getHeader()
			body = message.getMessage()

			message__blocks.append( message__block(header,body) )

			chatroom = chatroom_debut

			for div in message__blocks:
				chatroom += div

			chatroom += chatroom_fin
			self.response.out.write(chatroom)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
 

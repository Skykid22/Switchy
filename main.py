logs = input(' Enter a name: ')

def infoLogs( logs ):
  switcher = { 
    "Maxim": " \'Sir. Maxim is the inventor of all things inside the nexus as well as this facility itself. He recruits prodigies of Engineering, Science, Magic, Among other things.He lives only by his genetic modifications.\' ", 
    "AI": "Not created by Sir Maxim but definitely improved apon, Take me for reference. ", 
    "Simons": "You just wanted to search your own name didn't you Ms Simons? ;3 'Nice and sweet teacher, but easily distracted and overwhelmed'", 
    "Nexus": " 'Massive technological structure designed and built by Sir.Maxim you are here!' '", 
  }
  print( switcher.get( logs, " I don't have a database for that. " )) 

infoLogs( logs ) 



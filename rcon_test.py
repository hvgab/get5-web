from rcon.source import Client
import os
server = os.getenv('rcon_server')
port = os.getenv('rcon_port')
password = os.getenv('rcon_password')

commands = [
    'status',
    
    'cvarlist',
    
    'differences',
    'heartbeat',
    ['changelevel', 'de_dust2'],
    ['host_workshop_map', '123'],
    'listissues',
    ['maps', '*'],
    
    
    # 'mp_pause_match',       # Pause the match in the next freeze time
    # 'mp_scrambleteams', 	# Scramble the teams and restart the game
    # 'mp_swapteams', 	    # Swap the teams and restart the game
    # 'mp_switchteams', 	    # Switch teams and restart the game
    # 'mp_tournament_restart', 	# Restart Tournament Mode on the current level.
    # 'mp_unpause_match', 	# Resume the match
    # 'mp_warmup_end', 	    # End warmup immediately.
    # 'mp_warmup_start', 	    # Start warmup.
    'mp_player_dump_properties',

    # 'plugin_load', 	# plugin_load <filename> : loads a plugin
    # 'plugin_pause', 	# plugin_pause <index> : pauses a loaded plugin
    # 'plugin_pause_all', 	# pauses all loaded plugins
    'plugin_print', 	# Prints details about loaded plugins
    # 'plugin_unload', 	# plugin_unload <index> : unloads a plugin
    # 'plugin_unpause', 	# plugin_unpause <index> : unpauses a disabled plugin
    # 'plugin_unpause_all', 	# unpauses all disabled plugins 

    # Cheats
    'replay_death',  # 	start hltv replay of last death
    'replay_start',  # 	Start GOTV replay: replay_start <delay> [<player name or index>]
    'replay_stop',  # 	stop hltv replay 

    ['say', 'say test'],

    'stats',

    'tv_broadcast_status',  # Print out broadcast status
    'tv_clients',  # Shows list of connected GOTV clients [-instance <inst> ]
    # 'tv_mem',  # hltv memory statistics
    'tv_msg',  # Send a screen message to all clients [-instance <inst> ]
    'tv_record',  # Starts GOTV demo recording [-instance <inst> ]
    'tv_relay',  # Connect to GOTV server and relay broadcast.
    # 'tv_retry',  # Reconnects the GOTV relay proxy
    'tv_status',  # Show GOTV server status.
    # 'tv_stop',  # Stops the GOTV broadcast [-instance <inst> ]
    # 'tv_stoprecord',  # Stops GOTV demo recording [-instance <inst> ]
    'tv_time_remaining',  # Print remaining tv broadcast time 

    'users',
]


for command in commands[-7:]:
    with Client(server, port, passwd=password) as client:
        print(command)
        print("\n")
        if isinstance(command, list):
            response = client.run(*command)
        else:
            response = client.run(command)
        print(response)
        print("\n\n")
        input("...")
def env_setup(name):

    
    
#     acc='KEYSTONE-SANDBOX', un='ZWORTZMAN@KEYSTONESTRATEGY.COM', rl='sandbox_zwortzman_role', 
#               db='sandbox_zwortzman', wh='sandbox_zwortzman_wh'):

    connection_parameters = {
        'account': 'KEYSTONE-SANDBOX',
        'user': name,
        'authenticator': 'externalbrowser',
        'role': None,
        'database': None,
        'schema' : 'PUBLIC',
        'warehouse': None
    }
    
    names = name.split('@')
    token = names[0]
    
    connection_parameters['role'] = 'sandbox_'+token+'_role'
    connection_parameters['database'] = 'sandbox_'+token
    connection_parameters['warehouse'] = 'sandbox_'+token+'_wh'
    
    return connection_parameters
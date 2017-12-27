from front_end.models import ERC20Address

class AddERC20Token():
    
    def __init__(self, user, token_address, network_id):
        
        #check if token already exist, if not push it in db
        
        if ERC20Address.objects.filter(user_id__username=user.username, token_address=token_address, network_id=network_id).exists():
            #do nothing
            pass
        else:
            new_token = ERC20Address()
            new_token.user_id = user
            new_token.token_address = token_address
            new_token.network_id = network_id
            
            new_token.save()
            
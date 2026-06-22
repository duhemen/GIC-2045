def sign_all_pillars(block, keys):
    pilar_list = ["eksekutif", "legislatif", "yudikatif", "akademisi", "privat"]
    for auth in pilar_list:
        block.sign_block(auth, keys[auth])
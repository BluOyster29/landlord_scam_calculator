
def rent_calculator(tenant, room_size, common_space, total_space):
    
    total = (room_size + common_space) / total_space
    
    print('\n{} pays {}% of total rent\n'.format(tenant, int(total * 100)))
    
    return total

def get_rent(tenant, percentage, price_app, furniture, common_price):
    
    rent = int(percentage * price_app)
    
    print('\n{} is responsible for {}% of the appartment'.format(tenant,(int(percentage * 100))))

    if furniture == 0:
        print('Assuming the rent only includes common space furnishings')
        
        rent += common_price
        
    elif furniture == 1:
        print('Assuming the rent includes furnishings from bedrooms as well')
        rent += (rent * 0.15)
    
    print('{} pays {}kr a month\n'.format(tenant, int(rent)))
    
    return rent

def main(data):
    
if __name__ == '__main__':
    
    toy_data = {
        #total_price of appartment kr
        base_cost_appartment : 10834,

        #room sizes m2
        total_sm : 85, #total square meters
        v_rum : 9, 
        o_rum : 9, 
        r_rum : 6, 
        a_rum : 6, 
        z_rum : 12,        
        common_space : 43, #common space m2

        # split common space
        common_space_per_hm : common_space / 5,

        #furniture
        furniture : 0.15,

        #sgsprice on website
        sgs_price : 10279,

        # total split space 
        total_shared_space : total_sm / 6,

        ## what we've actually been paying for 5 months
        rob_actually_paid : 2500,
        ana_actually_paid : 2500,
        od_actually_paid : 2500,
        ver_actually_paid : 2500,
        zig_actually_paid : 834,
    }

    main(toy_data)
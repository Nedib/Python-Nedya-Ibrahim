EXPECTED_BAKE_TIME = 40 
def bake_time_remaining(elapsed_bake_time:int)->int:
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining

PREPARATION_TIME = 2

def preparation_time_in_minutes(number_of_layers):
    time_to_prepare = number_of_layers * PREPARATION_TIME
    return time_to_prepare

    time_to_prepair = EXPECTED_BAKE_TIME = 40 

def bake_time_remaining(elapsed_bake_time:int)->int:
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time

    return time_remaining


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    total_elapsed_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_elapsed_time



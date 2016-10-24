"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#

from collections import namedtuple

# Lookup table for brevet distance to speeds. Since there's
# No direct logical rule for calculating them, it's simpler
# and easier to modify by keeping them in one discrete place.

# Speeds are dictated by where precisely the control in question
# is placed on the entire brevet. They are divided by thresholds,
# which must be *met* to progress to the next one, so long
# as the brevet length is shorter than the actual position.

# So if a brevet is categorized as 200 km, but the last control
# is at 204 km, it is still treated as though it were less than
# 200 km. If a brevet is 300 km and a control is at 200 km, it
# is treated as though it were in the 200 - 400 range.

SpeedLimit = namedtuple('SpeedLimit', ['threshold', 'speedtype'])

limits = {SpeedLimit(threshold=0, speedtype='slow'):15,
          SpeedLimit(threshold=0, speedtype='fast'):34,
          SpeedLimit(threshold=200, speedtype='slow'):15,
          SpeedLimit(threshold=200, speedtype='fast'):32,
          SpeedLimit(threshold=400, speedtype='slow'):15,
          SpeedLimit(threshold=400, speedtype='fast'):30,
          SpeedLimit(threshold=600, speedtype='slow'):11.428,
          SpeedLimit(threshold=600, speedtype='fast'):28,
          SpeedLimit(threshold=1000, speedtype='slow'):13.333,
          SpeedLimit(threshold=1000, speedtype='fast'):26}

# EXCEPTIONS:
# Because reasons, the brevets include a number of rules that supercede
# the patterns described above, They are as follows:
#   - The closing time of the starting checkpoint for a brevet is
#       always one hour after it opens.
#   - The overall time limit for a 200 km brevet is always 13.5
#       hours, regardless of the actual position of the final
#       control.

def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    start = arrow.get(brevet_start_time)

    if control_dist_km == 0:
        return brevet_start_time  # See Exceptions

    offset = find_offset(control_dist_km, 'fast', brevet_dist_km)

    result = start.replace(hours=+offset).isoformat()
    
    return result

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    
    start = arrow.get(brevet_start_time)

    if control_dist_km == 0:
        return start.replace(hours=+1).isoformat()     # See Exceptions
    elif control_dist_km >= 200 and brevet_dist_km == 200:
        return start.replace(hours=+13.5).isoformat()  # See Exceptions

    offset = find_offset(control_dist_km, 'slow', brevet_dist_km)
    
    return start.replace(hours=+offset).isoformat()

def find_offset( control_position, speedtype, brevet_max ):
    """
    Takes the position of the control and the type of speed sought, and returns
    the offset in hours those two should create from the start time based on
    the speed limits.

    If the control position exceeds the brevet type's theoretical maximum, it
    stays in the lesser category. For instance, a 200 km brevet will not
    gauge any control by the >= 200 km range, even if the last controls are
    beyond 200 km.
    """
    # The dictionary keys are all named tuples - SpeedLimits. At their
    # 0 index, they contain the valid thresholds listed in the limits.
    # We take the highest threshold that is less than or equal to the
    # control distance, and place that in the threshold value. BUT if 
    # the control distance is less than the brevet's maximum, we check 
    # for a control position that is less than the brevet maxiumum to
    # shift which range it will fall under down one category.
    if (control_position < brevet_max):
        threshold = max(SL[0] for SL in limits if SL[0] <= control_position)
    else:
        threshold = max(SL[0] for SL in limits if SL[0] <= brevet_max)
    
    speed = limits[SpeedLimit(threshold, speedtype)]
    print(speed)
    return control_position / speed
